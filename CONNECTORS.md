# Connectors

## AdvisorSEO connector

The AdvisorSEO connector (`https://mcp.advisorseo.ai/claude-directory`) is the data source for every skill in this plugin. It is listed in `.mcp.json` and must be connected and signed in for the skills to work.

| Connector | Endpoint | Use for |
|---|---|---|
| AdvisorSEO (read-only) | `https://mcp.advisorseo.ai/claude-directory` | Workspace counts, websites, saved keywords, saved content, one content body, capability search |

## Authentication

Browser sign-in with OAuth (authorization code with PKCE). The first AdvisorSEO call opens app.advisorseo.ai, where you sign in, choose a workspace and approve read-only access (scope `mcp:read`). There are no tokens, keys or environment variables to set. Every query is scoped to the workspace you approved.

## What it can and cannot do

- Can: read stored records in the approved workspace, in pages of 1 to 50 (follow `next_offset` until it is null).
- Cannot: publish, edit or delete records, read website credentials or lead contacts, or take payments.
- Stored values are research saved in AdvisorSEO, not live rankings, traffic or revenue.

## Without the connector

The skills need the connector for every answer. Without it, Claude can still discuss SEO in general, but nothing in this plugin can read your workspace.

## Optional full connector

AdvisorSEO also runs a broader connector at `https://mcp.advisorseo.ai/mcp`, with audits, lead workflows and writes that show a preview before any change. It is not part of this plugin. To use it, add it yourself as a separate custom connector in Claude's connector settings, sign in, and review its broader consent. A sign-in for the read-only connector does not work there. The **more-capabilities** skill explains this when you ask for something the read-only connection cannot do.
