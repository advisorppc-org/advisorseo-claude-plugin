#!/usr/bin/env python3
"""Repo checks for the AdvisorSEO plugin package.

Why: the directory review rejects or holds a plugin for these issues, and the
strict CLI validator does not cover all of them (README length, binaries,
listing words, tool names that are not deployed).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
# Why: a release must not ship a skill whose tool is still in an open connector pull request.
RELEASE = "--release" in sys.argv
ROOT = Path(ARGS[0] if ARGS else ".").resolve()
errors: list[str] = []
LIVE = set((ROOT / "scripts/live-tools.txt").read_text().split())
# Tools in open connector pull requests: name, then the pull request number.
PENDING = {
    line.split()[0]: line.split()[1]
    for line in (ROOT / "scripts/pending-tools.txt").read_text().splitlines()
    if line.strip() and not line.startswith("#")
}
DISPLAY_NAME = "Advisor SEO, AEO, GEO"
ALLOWED_FM = {"name", "description", "license", "metadata"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
BANNED_EXT = {".zip", ".pdf", ".ico", ".tar", ".gz", ".tgz", ".exe", ".bin", ".dll", ".so", ".dylib", ".jar", ".whl"}
REPO_SLUG = "advisorppc-org/advisorseo-claude-plugin"
# Every wire prefix a skill may name. Hyphenated words such as gtm-container never match.
TOOL_NAME = r"\b(?:gravity|gtm|ga4|gsc|crux|advisorseo)_[a-z0-9_]+"


def fail(msg: str) -> None:
    errors.append(msg)


def tracked() -> list[Path]:
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return [ROOT / p for p in out.splitlines() if (ROOT / p).exists()]


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", " ", text, flags=re.S)


def listing_words(path: Path, text: str) -> None:
    # Tool names (gravity_*) are wire names and allowed in tool-call examples.
    t = re.sub(r"gravity_[a-z_]+", "", text)
    t = t.replace(REPO_SLUG, "")
    if re.search(r"gravity", t, re.I):
        fail(f"{path.relative_to(ROOT)}: codename outside a tool name")
    if re.search(r"advisorppc", t, re.I):
        fail(f"{path.relative_to(ROOT)}: parent company name outside the repository slug")
    if "\u2014" in text:
        fail(f"{path.relative_to(ROOT)}: em-dash")


# 1. Manifests
plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", plugin.get("name", "")):
    fail("plugin.json: name missing or not kebab-case")
if re.match(r"(claude-|anthropic-|cc-plugin-)", plugin["name"]) or "official" in plugin["name"]:
    fail("plugin.json: reserved name prefix or 'official'")
if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
    fail("plugin.json: version is not semver")
for key in ("homepage", "repository", "documentationUrl", "supportUrl", "privacyPolicyUrl", "termsOfServiceUrl"):
    if key in plugin and not str(plugin[key]).startswith("https://"):
        fail(f"plugin.json: {key} is not an https URL")
if "license" not in plugin or not (ROOT / "LICENSE").exists():
    fail("license field or LICENSE file missing")
if "icon" in plugin:
    icon = ROOT / plugin["icon"]
    if not icon.exists() or icon.stat().st_size > 256 * 1024:
        fail("icon missing or over 256 KiB")
if plugin.get("displayName") != DISPLAY_NAME:
    fail(f"plugin.json: displayName is not {DISPLAY_NAME!r}")
market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
if market.get("name") != "advisorseo" or not any(p.get("name") == plugin["name"] for p in market.get("plugins", [])):
    fail("marketplace.json: name or plugin entry wrong")
for entry in market.get("plugins", []):
    if entry.get("name") == plugin["name"] and entry.get("displayName", DISPLAY_NAME) != DISPLAY_NAME:
        fail("marketplace.json: displayName differs from plugin.json")
if PENDING.keys() & LIVE:
    fail(f"pending-tools.txt: already live, move out: {sorted(PENDING.keys() & LIVE)}")
readme_text = (ROOT / "README.md").read_text()

# 2. .mcp.json
mcp = json.loads((ROOT / ".mcp.json").read_text())
for name, srv in mcp.get("mcpServers", mcp).items():
    url = srv.get("url", "")
    if not url.startswith("https://"):
        fail(f".mcp.json: {name} is not an https URL")
    if srv.get("command") in ("npx", "uvx"):
        fail(f".mcp.json: {name} uses an unpinned launcher")

# 3. Layout
for d in ("commands", "agents", "hooks", "bin"):
    if (ROOT / d).exists():
        fail(f"top-level {d}/ is not allowed in this plugin")
if (ROOT / "CLAUDE.md").exists():
    fail("root CLAUDE.md is not loaded by plugins; keep it in docs/MAINTAINERS.md")

# 4. Skills
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    fail("no skills found")
for s in skills:
    text = s.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        fail(f"{s.relative_to(ROOT)}: no frontmatter")
        continue
    keys = re.findall(r"^([a-zA-Z_]+):", m.group(1), re.M)
    if set(keys) - ALLOWED_FM:
        fail(f"{s.relative_to(ROOT)}: frontmatter keys {sorted(set(keys) - ALLOWED_FM)} not allowed")
    name = re.search(r"^name: (.+)$", m.group(1), re.M)
    desc = re.search(r"^description: (.+)$", m.group(1), re.M)
    if not name or name.group(1).strip() != s.parent.name:
        fail(f"{s.relative_to(ROOT)}: name does not match folder")
    if not desc or len(desc.group(1)) >= 1024:
        fail(f"{s.relative_to(ROOT)}: description missing or 1,024 characters or more")
    body = text[m.end():]
    if "Why:" not in body:
        fail(f"{s.relative_to(ROOT)}: no Why line")
    if "## Check" not in body:
        fail(f"{s.relative_to(ROOT)}: no Check section")
    if "insufficient data" not in body:
        fail(f"{s.relative_to(ROOT)}: no 'insufficient data' rule")
    waiting = set()
    for tool in set(re.findall(TOOL_NAME, text)):
        if tool in PENDING:
            waiting.add(tool)
        elif tool not in LIVE:
            fail(f"{s.relative_to(ROOT)}: names {tool}, which is not a connector tool")
    # Why: a skill written ahead of its tool must say so to the maintainer (needs), to the user
    # (a fallback line) and in the README, so nobody is told a tool exists when it does not.
    rel = s.relative_to(ROOT)
    needs = re.search(r"^  needs: (.+)$", m.group(1), re.M)
    if waiting and RELEASE:
        fail(f"{rel}: names {sorted(waiting)}, still in open connector pull requests")
    for tool in sorted(waiting):
        if not needs or tool not in needs.group(1):
            fail(f"{rel}: names pending tool {tool} without listing it in metadata needs")
        if "not available yet" not in body:
            fail(f"{rel}: names pending tool {tool} without a 'not available yet' fallback")
        if f"`{tool}`" not in readme_text.split("## Waiting on the connector")[-1].split("\n## ")[0]:
            fail(f"{rel}: pending tool {tool} is not listed under 'Waiting on the connector' in README.md")
    if needs and not waiting:
        fail(f"{rel}: metadata needs is set but no pending tool is named; remove it")
    listing_words(s, text)

# 5. Listing copy
# Why: hype words and unmeasured claims are what an auditing buyer or reviewer rejects first.
BANNED = [r"\bguarantee(d|s)?\b", r"#1\b", r"\binstant(ly)?\b", r"\brevolutionary\b", r"\bAI rank"]


def banned_words(path: Path, text: str, allow_ai_rank: bool = False) -> None:
    prose = strip_code(text)
    for pat in BANNED:
        if allow_ai_rank and "AI rank" in pat:
            continue
        if re.search(pat, prose, re.I):
            fail(f"{path.relative_to(ROOT)}: banned word matching {pat}")
    if "!" in re.sub(r"`[^`]*`", "", prose):
        fail(f"{path.relative_to(ROOT)}: exclamation mark")


for f in ("README.md", "SUBMISSION.md", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    p = ROOT / f
    listing_words(p, p.read_text())
    banned_words(p, p.read_text())
# Skills may name "AI rank" only inside the rule that forbids stating one.
for s in skills:
    banned_words(s, s.read_text(), allow_ai_rank=True)
for tool in set(re.findall(TOOL_NAME, (ROOT / "README.md").read_text())):
    if tool not in LIVE and tool not in PENDING:
        fail(f"README.md: names {tool}, which is not a connector tool")
words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", strip_code((ROOT / "README.md").read_text())))
if words < 40:
    fail(f"README.md: {words} words outside code blocks (needs 40 or more)")

# 6. Files
for p in tracked():
    rel = p.relative_to(ROOT)
    if p.suffix.lower() in BANNED_EXT:
        fail(f"{rel}: banned file type")
    if p.stat().st_size > 256 * 1024:
        fail(f"{rel}: over 256 KiB")
    if p.suffix.lower() not in IMAGE_EXT:
        try:
            p.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            fail(f"{rel}: non-image binary")

# 6. Eval graders
# Why: the eval runner compiles patterns as JavaScript, so an inline (?i) throws, the grader fails, and no
# skill can pass the case. CI never runs evals, so this is the only check that sees it before a release.
for g in sorted(ROOT.glob("evals/*/graders/*.md")):
    head = g.read_text(encoding="utf-8").split("---")[1]
    if 'type: "regex"' not in head:
        continue
    found = re.search(r'^pattern: "(.*)"$', head, re.M)
    rel = g.relative_to(ROOT)
    if not found:
        fail(f"{rel}: regex grader with no pattern")
        continue
    pattern = found.group(1).encode().decode("unicode_escape")
    if re.search(r"\(\?[a-zA-Z]+\)", pattern):
        fail(f"{rel}: inline flags throw in the eval runner; use a flags field")
    flags = re.search(r'^flags: "(.*)"$', head, re.M)
    if flags and set(flags.group(1)) - set("dgimsuvy"):
        fail(f"{rel}: flags the eval runner does not know")
    if "(?P<" in pattern:
        fail(f"{rel}: Python-only named group; the eval runner uses JavaScript")
    try:
        re.compile(pattern)
    except re.error as e:
        fail(f"{rel}: pattern does not compile: {e}")

print(f"skills: {len(skills)}; README words outside code: {words}; tracked files: {len(tracked())}")
if errors:
    print("FAIL")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("PASS: repo checks")
