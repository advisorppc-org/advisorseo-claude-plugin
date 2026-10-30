# AdvisorSEO for Claude

Get found in Google and in AI assistants, with controls your security team can check. AdvisorSEO checks whether AI crawlers can read your site, audits it, picks the pages most worth winning, and changes nothing on your site until you approve a preview. Controls: sign-in is OAuth 2.1 (authorization code with PKCE S256 and dynamic client registration, so no key is ever pasted), tokens carry the scopes `mcp:tools` and `mcp:read`, every site write needs your approval in a separate turn, and the data-handling table below lists every place your data goes. Every result it reports comes with n and an interval, or the words "insufficient data".

This repository is the AdvisorSEO plugin for Claude Code, claude.ai and Claude Desktop. It bundles the AdvisorSEO connector (`https://mcp.advisorseo.ai/mcp`) and eleven skills that know how to use it well.

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
| search-console | "Which queries bring clicks?" | Queries, pages, countries and devices from Search Console, URL inspection, sitemap status and submission |
| analytics-ga4 | "Which landing pages convert?" | GA4 reports and realtime, a setup review, and key events or custom dimensions added on approval |
| tag-manager-tracking | "Audit my GTM container" | Tags, triggers and consent checked, and draft changes made on approval |
| core-web-vitals | "Is my site fast?" | Real-user field data, its history, and lab tests, each labelled by source |

Every skill reports a rate with its sample size plus an interval, or says "insufficient data". No skill ever claims a rank position inside an AI assistant, and no skill queries or scrapes consumer AI apps.

## How it works on its own

Why: an owner wants the site improved without having to ask each time, and without losing control of what changes.

AdvisorSEO watches the site (**site-audit** with a recurring watch, **ai-readiness-check**), proposes each change with its reason and the metric it should move (**site-audit**, **pages-to-win**), asks for one approval and applies it (**approve-and-measure-change**), then measures and reports the result with n and an interval, or "insufficient data" (**approve-and-measure-change**, **leads**).

## Every write asks first

Why: these tools can change a live website, so a preview and a separate approval turn are the safety line.

The first call to a tool that changes your site, your records or your Google accounts changes nothing and returns a preview. The change happens only when the tool is called again with `confirm=true`, after you approve in your own next message. Two tools save without a preview, and neither touches your site or Google: `gravity_geo_pagespeed` saves a PageSpeed measurement, and `gravity_google_set_properties` records which Google properties belong to a site after you choose them. These are the tools the skills use that change something:

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
| `gravity_gsc_submit_sitemap`, `gsc_sitemaps_delete`, `gsc_sites_add`, `gsc_sites_delete` | Your Google Search Console account |
| `gravity_seo_checklist_run` | Runs the SEO checklist and saves the result in your workspace |
| `gravity_geo_pagespeed` | Saves a PageSpeed measurement in your workspace, with no preview |
| `gravity_google_set_properties` | Records the Google properties chosen for a site |
| `ga4_*` tools that create, patch, update, archive, delete, approve, cancel, provision, reorder or link | Your Google Analytics 4 account and properties. A link shares a property's data with the linked product |
| `gtm_*` tools that create, update, delete, revert, sync, combine, move, link or import | Draft workspaces and containers in your Google Tag Manager account |
| `gtm_versions_publish`, `gtm_versions_set_latest` | The Tag Manager version live on your website, or the one marked latest |

Google writes also need your Google consent. AdvisorSEO's first Google link asks for read-only access to Search Console and Analytics. Tag Manager reads and each kind of change ask the first time you use them, with a link that adds only that permission.

Tool names keep the connector's fixed wire prefix; they are all AdvisorSEO tools.

## Data flow

Why: you should know every place your data goes before you install anything.

| Where | What is sent or fetched | When |
|---|---|---|
| mcp.advisorseo.ai | Your tool calls and their arguments; results come back to Claude | Every AdvisorSEO tool call |
| app.advisorseo.ai | Sign-in and the OAuth consent page; your account, plan and Google connection | At install, and when you manage your account |
| Your website (public pages, robots.txt, llms.txt) | Fetched by the AdvisorSEO server, the way a crawler would | Audits, AI readiness checks, crawls |
| Google APIs, under your own Google OAuth consent | Search Console, Analytics and Tag Manager reads, and the writes you approve | Only after you open the Google connect link and approve |
| Google Chrome UX Report | The public URL or origin being checked, under AdvisorSEO's own API key | Core Web Vitals checks |
| Google PageSpeed Insights | The public URL of the page being checked | Page speed checks |
| Your WordPress site, with the application password you stored | The article you approved | Only on a confirmed publish |

AdvisorSEO stores your encrypted Google connection and chosen properties, and any rank snapshot or PageSpeed measurement you run. Other Google reports are returned and not stored. Ask Claude to disconnect Google for a site to delete its connection; https://advisorseo.ai/privacy has the detail.

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
