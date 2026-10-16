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

## Repo map (historical notes, kept for maintainers)


## AdvisorSEO repo map (same block in every AdvisorSEO repo; source of truth: advisorppc-org/advisorseo/REPO_MAP.md)

This repo is one of six that make up AdvisorSEO (advisorseo.ai), a product of AdvisorPPC that runs as its OWN separate
stack (ADR-0005). GitHub org `advisorppc-org`. Hub: `advisorppc-org/advisorseo` (local `~/AdvisorSEO`): read its
`README.md` and `board/BOARD.md` before any task.

| repo | role | local (Air) | DGX mirror | serves |
|---|---|---|---|---|
| advisorseo | project OS | `~/AdvisorSEO` | `~/AdvisorSEO` |: |
| advisorseo-mcp | MCP connector (Python, 37 tools) | `~/advisorppc-gravity` (remote `advisorseo`) | `~/AdvisorSEO/repos/advisorseo-mcp` | mcp.advisorseo.ai |
| advisorseo-app | web app: login, dashboard, OAuth consent, billing | `~/gravity-content-engine` | `~/AdvisorSEO/repos/advisorseo-app` | app.advisorseo.ai |
| advisorseo-site | site, docs, privacy, terms, support | `~/advisorseo-site` | `~/AdvisorSEO/repos/advisorseo-site` | advisorseo.ai |
| advisorseo-claude-plugin | Claude Code plugin (public) | `~/advisorseo-claude-plugin` | `~/AdvisorSEO/repos/advisorseo-claude-plugin` | Claude Code directory |
| advisorseo-connect-wp | WordPress plugin free + Pro | `~/advisorseo-connect-wp` | `~/AdvisorSEO/repos/advisorseo-connect-wp` | wordpress.org, customer sites |

NOT AdvisorSEO, never build/push/deploy AdvisorSEO from them: `advisorppc-org/advisorppc-gravity` (AdvisorPPC engine,
upstream only), `gravity.advisorppc.com`, the `*-old` archives, `~/advisorppc-connectors/gravity` (stale), `marketingadvisorai/*`.
Frozen wire contracts: tool names `gravity_*`, paths `/gravity/mcp`, `/gravity/v1/lead`, `/gravity/oauth/consent`,
attribute `data-gravity-form`, `workspace_id` tenancy. "Gravity" is codename only; users see AdvisorSEO.
Push: `source ~/ENV/git-load.sh && gpush` (origin = advisorppc-org, class-approved 2026-09-19) and `git push dgx <branch>`. No tokens in URLs or output.
