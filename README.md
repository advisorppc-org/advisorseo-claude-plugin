# AdvisorSEO Plugin

Read your saved AdvisorSEO workspace in Claude: websites, tracked keywords and saved content. Review drafts, compare keyword research and plan the pages you are missing. Read-only.

## Overview

This plugin connects Claude to the AdvisorSEO connector at `https://mcp.advisorseo.ai/claude-directory` and adds five skills that know how to use it well. Every answer is built from the records saved in your AdvisorSEO workspace. The connection is read-only: it cannot publish, edit or delete anything, and suggestions stay in the chat for you to apply.

Saved records are stored research, not live search rankings, traffic or revenue. When the saved data is too thin to support a comparison, the skills say "insufficient data" instead of guessing.

## Requirements

- An AdvisorSEO account with at least one website: [advisorseo.ai](https://advisorseo.ai). Websites, keyword research and content are added in the AdvisorSEO app at app.advisorseo.ai.
- The **AdvisorSEO connector** (`https://mcp.advisorseo.ai/claude-directory`), included in this plugin's `.mcp.json`. The first AdvisorSEO call opens a browser window where you sign in and approve read-only access (OAuth with PKCE). No key, password or header is pasted into the chat.
- Works with Claude Code, Cowork, and Claude on the web and desktop.

## Install

Claude Code, inside a session:

```
/plugin marketplace add advisorppc-org/advisorseo-claude-plugin
/plugin install advisorseo@advisorseo
```

From a shell:

```
claude plugin install advisorseo --marketplace advisorppc-org/advisorseo-claude-plugin
```

Claude on the web, desktop and Cowork: open Customize, then Plugins, and add the marketplace repository `advisorppc-org/advisorseo-claude-plugin`, or install AdvisorSEO from the Claude directory once it is listed.

Connector only, without the skills:

```
claude mcp add --transport http advisorseo https://mcp.advisorseo.ai/claude-directory
```

## Skills

Skills are triggered conversationally. Describe what you want and Claude loads the right skill.

| Skill | Trigger phrases |
|-------|----------------|
| `start-here` | "What can AdvisorSEO do", "show my SEO workspace", "which sites do I have", "where do I start" |
| `keyword-review` | "Show my saved keywords", "which keywords are we tracking for [site]", "compare keyword difficulty and intent" |
| `content-review` | "Review my draft", "what content do we have for [site]", "read the saved post about [topic]", "suggest edits" |
| `content-gap-plan` | "What pages should I create", "which keywords have no page yet", "plan my content" |
| `more-capabilities` | "What else can this connector do", "can AdvisorSEO publish to WordPress" |

## What Each Skill Produces

**Start here**: the workspace counts (websites, keywords, strategies, content by status), the right website picked by domain, and a route to the next skill. Counts are stored records, never described as performance.

**Keyword review**: a table of saved keywords with stored volume, difficulty, intent, status and last-checked date, sorted to answer your question, plus how old the research is.

**Content review**: one saved record read against its target keyword, with 3 to 5 suggested edits (current text, suggested text, why) and the record ID. Bodies over 12,000 characters are flagged as truncated.

**Content gap plan**: up to 10 saved keywords that have no page yet, sorted by intent, stored volume and difficulty, each with a working title, plus drafts worth finishing first.

**More capabilities**: what this connection can read, and how to add the separate, opt-in full AdvisorSEO connector if you want publishing and editing. Nothing is enabled for you.

## Tools used

The skills call only the six read-only tools on the connector:

| Tool | What it reads |
|---|---|
| `advisorseo_overview` | Counts of stored websites, keywords, strategies and content states |
| `advisorseo_list_sites` | A page of websites with IDs, names, domains and status |
| `advisorseo_list_keywords` | A page of saved keyword records for one website |
| `advisorseo_list_content` | A page of saved content titles, status, target keyword and word count for one website |
| `advisorseo_get_content` | One saved content record with up to 12,000 characters of its body |
| `advisorseo_search_tools` | Searches this connection's capabilities; runs nothing |

## Data flow

| Where | What is sent or returned | When |
|---|---|---|
| mcp.advisorseo.ai | Your tool calls and their arguments; stored records come back to Claude | Every AdvisorSEO tool call |
| app.advisorseo.ai | Sign-in and the read-only consent page | At first use, and when you manage your account |

The plugin runs no local code, makes no other network calls and has no hooks. It ships text skills, an icon, one connector address and repository checks for maintainers. Your authorization is held in Claude's own credential store; remove the plugin or disconnect the connector to revoke it.

## Setup

1. Install this plugin.
2. Ask "show my SEO workspace". Claude opens the AdvisorSEO sign-in once; approve the read-only access.
3. Use any skill above.

See [CONNECTORS.md](CONNECTORS.md) for the connector and the optional full connector.

## Privacy, terms and support

- Docs: [advisorseo.ai/docs](https://advisorseo.ai/docs)
- Privacy: [advisorseo.ai/privacy](https://advisorseo.ai/privacy)
- Terms: [advisorseo.ai/terms](https://advisorseo.ai/terms)
- Support: [SUPPORT.md](SUPPORT.md), [advisorseo.ai/support](https://advisorseo.ai/support) or support@advisorseo.ai
- Security reports: [SECURITY.md](SECURITY.md)

## License

MIT, see [LICENSE](LICENSE).
