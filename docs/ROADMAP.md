# Roadmap

Why: a skill that names a tool the deployed connector does not have fails in front of a user. Skills that wait for tools are written down here and ship only when their tools are live on mcp.advisorseo.ai.

## Next (waits for deployed tools)

Each entry names the user question, the tools it needs, and the gate. Exact tool names are taken from the advisorseo-mcp main branch when it deploys; this lane could not read that branch, so names below are the capability, not the wire name.

### search-console-wins
- Shipped in 0.3.0 as search-console, with analytics-ga4, tag-manager-tracking and core-web-vitals.

### Shipped in 0.4.0
- ai-visibility-tracking shipped as ai-visibility. Its data-source gate holds by design: the connector asks no engine anything, and answers are recorded only when a person or the calling assistant collected them.
- change-proposals shipped inside approve-and-measure-change: a publish that answers `approval_required` goes through `gravity_propose_change`, an approval in the app, and the publish tool with the approval id.
- llms-txt-and-schema shipped inside answer-ready-pages.
- New: keyword-research, rank-tracking, answer-ready-pages, brand-and-mentions, bing-webmaster, monthly-report.

### Waits for connector pull requests 95 and 96
- Four skills name six tools from those pull requests ahead of time, listed in `scripts/pending-tools.txt` and in the README. When they merge and deploy, move the names to `scripts/live-tools.txt`, remove the `needs` line and the fallback rule from each skill, and remove the README section.

### Planned in the connector, no skill yet
- AI answer sentiment and accuracy, unique facts versus competitors, cost-ranked fixes and name, address and phone consistency. They fold into ai-visibility, answer-ready-pages, site-audit and brand-and-mentions when their tools exist.
- Social post planning (`advisorseo_social`) is on the connector's main branch and has no skill yet.

### Names held for work in progress elsewhere
- connect-your-site and publish-blog-seo-aeo-geo are being written in another checkout. Do not add skills with those names here.

## Retired in v0.2.0

- seo-workspace-review: depended on a separate directory connection the plugin does not ship.
- seo-content-plan: folded into pages-to-win.
- publish-to-wordpress: folded into approve-and-measure-change.
- lead-triage: replaced by leads.
