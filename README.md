# AdvisorSEO for Claude

Get found in Google and in AI assistants. AdvisorSEO checks whether AI crawlers can read your site, audits it, picks the pages most worth winning, and makes changes only after you approve a preview, then tells you how the result will be measured.

This repository is the AdvisorSEO plugin for Claude Code, claude.ai and Claude Desktop. It bundles the AdvisorSEO connector (`https://mcp.advisorseo.ai/mcp`) and seven skills that know how to use it well.

Why: one install gives Claude both the connector and the know-how, so the first answer is a useful one and no change reaches a live site without your yes.

## Install

Claude Code 2.1.275 or later, inside a session:

```
/plugin install advisorseo --marketplace advisorppc-org/advisorseo-claude-plugin
```

From a shell:

```
claude plugin install advisorseo --marketplace advisorppc-org/advisorseo-claude-plugin
```

Two steps, for older Claude Code versions:

```
/plugin marketplace add advisorppc-org/advisorseo-claude-plugin
/plugin install advisorseo@advisorseo
```

Connector only, without the skills:

```
claude mcp add --transport http advisorseo https://mcp.advisorseo.ai/mcp
```

claude.ai and Claude Desktop: open Customize, then Plugins, and add the marketplace repository `advisorppc-org/advisorseo-claude-plugin`, or install AdvisorSEO from claude.ai/directory once it is listed. A plugin installed on your account also loads in Claude Code as `advisorseo@synced`.

For a team, add this to the repository's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "advisorseo": {
      "source": { "source": "github", "repo": "advisorppc-org/advisorseo-claude-plugin" }
    }
  },
  "enabledPlugins": { "advisorseo@advisorseo": true }
}
```

The first AdvisorSEO call opens a browser window where you sign in to your AdvisorSEO account and approve access. No key, password or header is ever pasted into the chat.

## What it does

Why: each skill answers one question a site owner actually asks, and Claude picks the skill from your words.

| Skill | Ask it like this | What you get |
|---|---|---|
| start-here | "How is my site doing?" | The workspace overview, the right site picked, and a route to the next skill |
| ai-readiness-check | "Can ChatGPT read my site?" | Every AI search and user-fetch bot marked ok or blocked, with the reason, plus failed checklist items |
| site-audit | "Audit my site" | Up to 10 findings with page and evidence, what changed since the last run, an optional recurring watch |
| pages-to-win | "What pages should I create?" | Up to 10 pages, each with a gap type and the metric it should move, saved to your plan on approval |
| approve-and-measure-change | "Publish that post" | A preview, your explicit yes, the change, and the metric to check afterwards |
| connect-and-import | "Add my site" | Platform detected, site record and business profile saved, WordPress and Google connection explained |
| leads | "Any new leads?" | New leads, one lead's full history, and status moves with a note on each |

Every skill reports a rate with its sample size plus an interval, or says "insufficient data". No skill ever claims a rank position inside an AI assistant, and no skill queries or scrapes consumer AI apps.

## Every write asks first

Why: these tools can change a live website, so a preview and a separate approval turn are the safety line.

The first call to a write tool changes nothing and returns a preview. The change happens only when the tool is called again with `confirm=true`, after you approve in your own next message. These are the tools the skills use that change something:

| Write tool | What it changes |
|---|---|
| `gravity_create_site`, `gravity_update_site` | Your site record in AdvisorSEO, including the stored WordPress address |
| `gravity_set_profile` | Your business profile in AdvisorSEO |
| `gravity_add_keywords` | Your stored keyword list |
| `gravity_add_strategies` | Your content plan |
| `gravity_save_content` | A stored page or article (the previous version is kept) |
| `gravity_publish_wordpress` | Your live WordPress site, as a published post or a WordPress draft |
| `gravity_publish_site`, `gravity_unpublish_site` | The hosted AdvisorSEO site for a site record |
| `gravity_update_lead` | A lead's status and notes |
| `gravity_audit_domain`, `gravity_audit_watch` | Starts an audit run, or a recurring audit schedule |
| `gravity_crawl_site` | Imports your site's public pages into your AdvisorSEO workspace |

Tool names keep the connector's fixed wire prefix; they are all AdvisorSEO tools.

## Data flow

Why: you should know every place your data goes before you install anything.

| Where | What is sent or fetched | When |
|---|---|---|
| mcp.advisorseo.ai | Your tool calls and their arguments; results come back to Claude | Every AdvisorSEO tool call |
| app.advisorseo.ai | Sign-in and the OAuth consent page; your account, plan and Google connection | At install, and when you manage your account |
| Your website (public pages, robots.txt, llms.txt) | Fetched by the AdvisorSEO server, the way a crawler would | Audits, AI readiness checks, crawls |
| Google APIs, under your own Google OAuth consent | Search Console and Analytics reads for the properties you connect | Only after you connect Google in app.advisorseo.ai |
| Google PageSpeed Insights | The public URL of the page being checked | Page speed checks |
| Your WordPress site, with the application password you stored | The article you approved | Only on a confirmed publish |

The plugin itself runs no local code: it ships skills (text), an icon and one remote connector address. Nothing personal is stored in this repository. Your authorization is held in Claude's own credential store and can be revoked by removing the plugin or disconnecting Claude from your AdvisorSEO account.

## Requirements

- An AdvisorSEO account: [advisorseo.ai](https://advisorseo.ai).
- For publishing: a WordPress site with an application password stored on your AdvisorSEO site record. An application password is not your WordPress login password.

## Privacy, terms and support

Why: these are the pages the directory and your own reviewers will check.

- Docs: [advisorseo.ai/docs](https://advisorseo.ai/docs)
- Privacy: [advisorseo.ai/privacy](https://advisorseo.ai/privacy)
- Terms: [advisorseo.ai/terms](https://advisorseo.ai/terms)
- Support: [advisorseo.ai/support](https://advisorseo.ai/support) or support@advisorseo.ai

## License

MIT, see [LICENSE](LICENSE).
