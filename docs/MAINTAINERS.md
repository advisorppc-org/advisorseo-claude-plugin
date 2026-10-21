# Maintainers

Why: a root CLAUDE.md is not loaded by a plugin and makes `claude plugin validate --strict` warn, so the maintainer notes live here.

## Package rules

Why: these are the rules the directory review and the strict validator apply.

- Plugin files: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.mcp.json` (mcpServers form), `skills/<name>/SKILL.md`, `icon.png`, `README.md`, `CONNECTORS.md`, `LICENSE`, `SECURITY.md`, `SUPPORT.md`, `CHANGELOG.md`. No `commands/`, `agents/`, `hooks/` or top-level `bin/`.
- `.mcp.json` names exactly one server, `https://mcp.advisorseo.ai/claude-directory`, the same URL as the connector listing.
- Skills name only the six tools in `scripts/live-tools.txt`, the read-only tools on that endpoint. Refresh the list from a live `tools/list` before each release.
- Skill frontmatter is `name` and `description` only; the description carries the trigger phrases.
- No tracked `.zip`, `.pdf`, `.ico` or other non-image binary, and no file over 256 KiB. `dist/` is ignored.
- Listing copy, skills, README and manifests use the AdvisorSEO name only. No em dashes.
- Gate: `scripts/validate.sh` runs `claude plugin validate --strict` when the CLI is present, `scripts/check_package.py` and `tests/check_skills.sh`. CI runs it on every push and pull request.
- Evals: `evals/`, run by a maintainer on a Claude seat before each release, never in CI.

## Build receipts

Why: zip files in git trigger a directory reviewer hold, and receipts belong to a release, not to the source tree.

Build a bundle with `git archive --format=zip -o dist/advisorseo-<version>.zip HEAD` (dist/ is ignored). Attach the zip, the validate output and the eval report to the GitHub Release for that tag.

## Releases

Why: the directory tracks the default branch, so a merge is a release.

Bump `version` in `.claude-plugin/plugin.json`, add the CHANGELOG entry, run `scripts/validate.sh`, run the evals, open a draft PR, merge on green CI plus an independent review, then tag `v<version>`.
