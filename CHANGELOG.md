# Changelog

All notable changes to this plugin are listed here. Versions follow semantic versioning.

## Unreleased

## 0.3.0 (2026-10-21)

Directory edition.

- Connector moved to the read-only directory endpoint `https://mcp.advisorseo.ai/claude-directory` (six read-only tools, scope `mcp:read`).
- `.mcp.json` uses the `mcpServers` form.
- Five skills written for the read-only tools: start-here, keyword-review, content-review, content-gap-plan, more-capabilities.
- Retired the seven skills that needed the full connector (ai-readiness-check, site-audit, pages-to-win, approve-and-measure-change, connect-and-import, leads, and the old start-here). Writes, audits and leads remain available through the separate, opt-in full connector described in CONNECTORS.md.
- New CONNECTORS.md, SECURITY.md, SUPPORT.md and this changelog. README rewritten with requirements, trigger phrases and outputs.
- Evaluation cases re-recorded against the six read-only tools.
- `displayName` and `category` added to the marketplace entry.

## 0.2.0 (2026-10-15)

- Seven skills on the full connector, submission pack, evaluation cases and a strict validation gate.

## 0.1.0

- First public package.
