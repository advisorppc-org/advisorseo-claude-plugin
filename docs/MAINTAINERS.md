# CLAUDE.md — advisorseo-claude-plugin

Claude Code plugin repo (PUBLIC): .claude-plugin/plugin.json, .mcp.json → https://mcp.advisorseo.ai/mcp, skills/; gate claude plugin validate --strict.

## AdvisorSEO repo map (same block in every AdvisorSEO repo; source of truth: advisorppc-org/advisorseo/REPO_MAP.md)

This repo is one of six that make up AdvisorSEO (advisorseo.ai), a product of AdvisorPPC that runs as its OWN separate
stack (ADR-0005). GitHub org `advisorppc-org`. Hub: `advisorppc-org/advisorseo` (local `~/AdvisorSEO`): read its
`README.md` and `board/BOARD.md` before any task.

| repo | role | local (Air) | DGX mirror | serves |
|---|---|---|---|---|
| advisorseo | project OS | `~/AdvisorSEO` | `~/AdvisorSEO` | — |
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
