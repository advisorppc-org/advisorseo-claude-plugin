# Roadmap

Why: a skill that names a tool the directory connector does not have fails in front of a user. Skills that wait for tools are written down here and ship only when their tools are live on `https://mcp.advisorseo.ai/claude-directory`.

## Next (waits for reviewed read tools on the directory endpoint)

### search-console-wins
- Ask: "Which queries am I close to winning?", "what does Search Console say?"
- Needs: read-only Search Console tools (queries, pages) on the directory endpoint, under the user's own Google consent.
- Output: up to 10 queries with clicks, impressions and Google's own average position, never an AI assistant rank, with "insufficient data" when the sample is small.

### strategy-review
- Ask: "Show my content plan", "which strategies are planned?"
- Needs: a read-only strategies list on the directory endpoint (the overview already counts them).

## Not planned for this plugin

Audits, AI crawler checks, lead workflows and every write (saving content, publishing) stay in the separate, opt-in full connector described in CONNECTORS.md. This plugin stays read-only.
