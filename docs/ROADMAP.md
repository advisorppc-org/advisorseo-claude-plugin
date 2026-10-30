# Roadmap

Why: a skill that names a tool the deployed connector does not have fails in front of a user. Skills that wait for tools are written down here and ship only when their tools are live on mcp.advisorseo.ai.

## Next (waits for deployed tools)

Each entry names the user question, the tools it needs, and the gate. Exact tool names are taken from the advisorseo-mcp main branch when it deploys; this lane could not read that branch, so names below are the capability, not the wire name.

### search-console-wins
- Shipped in 0.3.0 as search-console, with analytics-ga4, tag-manager-tracking and core-web-vitals.

### change-proposals
- Ask: "What would you change this week?", "show me the proposals".
- Needs: the proposal and job tools (create, list, approve, run status).
- Output: one proposal per change with preview, approval state and the metric it should move. Folds into approve-and-measure-change when it lands.
- Gate: proposal approval is enforced server-side, not only in the skill.

### ai-visibility-tracking
- Ask: "Are AI assistants citing us?", "track our AI visibility".
- Needs: the AI visibility tools from the connector main branch, backed by sanctioned sources only (official APIs or the user's own data). Never scraping consumer AI apps.
- Output: citation counts with n plus an interval, or "insufficient data". Never a rank position inside an assistant.
- Gate: a written data-source review that confirms no consumer app is scraped.

## v0.2.x candidates (tools already live)

- llms-txt-and-schema: `gravity_geo_llmstxt_generate`, `gravity_geo_schema_build` and `gravity_geo_brand_footprint` are deployed today. A skill can draft llms.txt and schema for review, then hand placement to approve-and-measure-change. Not shipped in v0.2.0 to keep the first listing small and every skill covered by an eval.

## Retired in v0.2.0

- seo-workspace-review: depended on a separate directory connection the plugin does not ship.
- seo-content-plan: folded into pages-to-win.
- publish-to-wordpress: folded into approve-and-measure-change.
- lead-triage: replaced by leads.
