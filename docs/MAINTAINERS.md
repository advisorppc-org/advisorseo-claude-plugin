# Maintainers

Why: this file was the repo-root CLAUDE.md. A root CLAUDE.md is not loaded by a plugin and makes `claude plugin validate --strict` warn, so the maintainer notes live here.

## Package rules

Why: these are the rules the directory review and the strict validator apply.

- Plugin files: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.mcp.json`, `skills/<name>/SKILL.md`, `icon.png`, `README.md`, `LICENSE`. No `commands/`, `agents/`, `hooks/` or top-level `bin/` (chat and Cowork refuse a plugin with `bin/`; agents and hooks are ignored in claude.ai chat).
- No tracked `.zip`, `.pdf`, `.ico` or other non-image binary, and no file over 256 KiB. `dist/` is ignored.
- Listing copy, skills, README and manifests never say the codename or the parent company name; tool names such as `gravity_overview` may appear in tool-call examples only. `scripts/validate.sh` enforces this.
- Skills name only tools deployed on mcp.advisorseo.ai today. Skills that need undeployed tools wait in `docs/ROADMAP.md`.
- Gate: `scripts/validate.sh` (runs `claude plugin validate --strict .` when the CLI is present, plus the repo checks). CI runs it on every push and pull request.
- Evals: `evals/`, run by the lead on a seat before each release, never in CI.

## Build receipts

Why: zip files in git trigger a directory reviewer hold, and receipts belong to a release, not to the source tree.

Build a bundle with `git archive --format=zip -o dist/advisorseo-<version>.zip HEAD` (dist/ is ignored). Attach the zip, the validate output and the eval report to the GitHub Release for that tag (`gh release create v<version> dist/advisorseo-<version>.zip validate.txt --draft`). The release page is the receipt; nothing from `dist/` or `evidence/` is committed.

## Releases

Why: the directory tracks the default branch, so a merge is a release.

Bump `version` in `.claude-plugin/plugin.json`, run `scripts/validate.sh`, run the evals, open a draft PR, merge on green CI plus an independent MERGE verdict, then tag `v<version>`.

## Repo map

Why: a maintainer needs to know which repository serves which surface; internal paths, push recipes and history live in the private engineering library, not in this public repository.

This repository is one of six that make up AdvisorSEO (advisorseo.ai), which runs as its own separate stack.

| Repository | Role | Serves |
|---|---|---|
| advisorseo | project hub: plans, board, decisions | (internal) |
| advisorseo-mcp | MCP connector, 37 deployed tools | mcp.advisorseo.ai |
| advisorseo-app | web app: sign-in, dashboard, OAuth consent, billing | app.advisorseo.ai |
| advisorseo-site | site, docs, privacy, terms, support | advisorseo.ai |
| advisorseo-claude-plugin | this plugin (public) | Claude directory |
| advisorseo-connect-wp | WordPress plugin, free and Pro | wordpress.org, customer sites |

- Tool names, connector paths and the lead-form attribute are frozen wire contracts. Never rename them in this plugin; users only ever see the AdvisorSEO name.
- Local checkouts, mirrors, push commands and the list of repositories that are not AdvisorSEO are in the private engineering library (the AdvisorSEO repo map). Never put tokens in URLs or output.
