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

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
errors: list[str] = []
LIVE = set((ROOT / "scripts/live-tools.txt").read_text().split())
ALLOWED_FM = {"name", "description", "license", "metadata"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
BANNED_EXT = {".zip", ".pdf", ".ico", ".tar", ".gz", ".tgz", ".exe", ".bin", ".dll", ".so", ".dylib", ".jar", ".whl"}
REPO_SLUG = "advisorppc-org/advisorseo-claude-plugin"


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
market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
if market.get("name") != "advisorseo" or not any(p.get("name") == plugin["name"] for p in market.get("plugins", [])):
    fail("marketplace.json: name or plugin entry wrong")

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
    for tool in set(re.findall(r"gravity_[a-z_]+", text)):
        if tool not in LIVE:
            fail(f"{s.relative_to(ROOT)}: names {tool}, which is not a deployed tool")
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
# Why: the repository is public, so every tracked text file is listing copy for the brand rule.
for p in tracked():
    if p.suffix.lower() in IMAGE_EXT or p.relative_to(ROOT).parts[0] == "skills":
        continue
    if str(p.relative_to(ROOT)) in ("README.md", "SUBMISSION.md", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "scripts/check_package.py"):
        continue
    listing_words(p, p.read_text())
    if re.search(r"(~/|/home/)[A-Za-z]", p.read_text()):
        fail(f"{p.relative_to(ROOT)}: internal home path")
# Skills may name "AI rank" only inside the rule that forbids stating one.
for s in skills:
    banned_words(s, s.read_text(), allow_ai_rank=True)
for tool in set(re.findall(r"gravity_[a-z_]+", (ROOT / "README.md").read_text())):
    if tool not in LIVE:
        fail(f"README.md: names {tool}, which is not a deployed tool")
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

print(f"skills: {len(skills)}; README words outside code: {words}; tracked files: {len(tracked())}")
if errors:
    print("FAIL")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("PASS: repo checks")
