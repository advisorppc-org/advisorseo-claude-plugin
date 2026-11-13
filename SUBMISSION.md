# Directory submission pack

Why: every field the claude.ai/directory/manage portal asks for is prepared here, so the submission happens in one sitting and the listing copy is reviewed in git before it is public.

Order: submit the MCP connector first, then the plugin paired with it. Updates ship by merging to the tracked branch (`main`).

## 1. Connector submission

| Field | Value |
|---|---|
| Name | Advisor SEO, AEO, GEO |
| Server URL | https://mcp.advisorseo.ai/mcp |
| Transport | Streamable HTTP, https only |
| Authentication | OAuth (sign-in and consent at app.advisorseo.ai) |
| Tool count | 358 on the connector's main branch on 2026-11-13 (read-only and write tools, annotated; writes to a site, a record or a Google account preview first). Confirm the count on the deployed connector on the day of submission |

## 2. Plugin submission

| Field | Value |
|---|---|
| Name | Advisor SEO, AEO, GEO |
| Slug | advisorseo (unchanged) |
| Repository | https://github.com/advisorppc-org/advisorseo-claude-plugin (must be public before the listing goes live) |
| Tracked branch | main |
| Version | 0.4.0 |
| License | MIT |
| Icon | `icon.png`, 512 by 512 PNG, 4,790 bytes (the advisorseo.ai site icon) |
| Homepage | https://advisorseo.ai |
| Documentation | https://advisorseo.ai/docs |
| Support | https://advisorseo.ai/support |
| Privacy policy | https://advisorseo.ai/privacy |
| Terms of service | https://advisorseo.ai/terms |
| Categories | Marketing; Productivity |

### One-liner (200 characters or fewer)

SEO, AEO and GEO in Claude: keyword research, rank tracking, site audits, answer-ready pages, AI visibility with sample sizes, and Google and Bing data. Every change is previewed and approved first.

### Description (2,000 characters or fewer)

Advisor SEO, AEO, GEO helps a business get found in Google, in Bing and in the answers AI assistants give.

SEO: research keywords from the queries you already earn and from Google and Bing volume, track daily positions from your own Search Console, audit the live site with evidence for each finding, and read Search Console, Google Analytics 4, Tag Manager, Bing Webmaster Tools and Core Web Vitals.

AEO: check whether AI search and user-fetch crawlers may read your site, read one page the way a crawler does to see whether it answers early enough to be quoted, and build structured data only from facts you supply.

GEO: track the prompts buyers ask, record the answers you collect, and report how often they name and cite you with n and an interval, beside the visits and leads AI assistants sent. Check your brand on the sources AI answers cite, and find mentions that do not link to you.

It also plans the ten pages most worth winning and writes a monthly report with a source for every number.

Controls you can audit: sign-in is OAuth 2.1, authorization code with PKCE (S256) and dynamic client registration, so no password is pasted. Tokens carry the scopes mcp:tools and mcp:read. Every change to a site, a record or a Google account first returns a preview, and happens only after you approve it in your own next message. A publish to a live site also needs an owner or admin to approve that exact change in the app.

Every rate comes with n and an interval, or the words "insufficient data". It never claims a rank position inside an AI assistant, and it never scrapes consumer AI apps: AI answers are recorded only when you or your assistant collected them.

Skills: start-here, connect-and-import, site-audit, keyword-research, rank-tracking, pages-to-win, search-console, bing-webmaster, analytics-ga4, tag-manager-tracking, core-web-vitals, ai-readiness-check, answer-ready-pages, ai-visibility, brand-and-mentions, approve-and-measure-change, monthly-report and leads.

### Use cases

1. "Can ChatGPT and Claude read my site?" Every AI bot is marked ok or blocked, with the reason.
2. "Audit my site." Up to ten findings with page, evidence and fix, compared with the last run.
3. "What pages should I create?" Up to ten pages, each with a gap type and the metric it should move.
4. "Publish that post." A preview, your approval, the publish, and the metric to watch.
5. "Any new leads?" New leads, each lead's history, and status moves with notes.
6. "Which queries bring clicks?" Search Console queries, pages, sitemaps and URL inspection.
7. "Audit my GTM container." Tags, triggers and consent checked, with draft fixes on approval.
8. "Are AI assistants citing us?" Presence and citation rates from collected answers, with n and an interval.
9. "What moved this week?" Daily Google positions with 7 and 28 day movers.
10. "Write this month's SEO report." One month of search and AI search results, each number with its source.

### Data handling answers

| Question | Answer |
|---|---|
| What data does the plugin access? | The user's AdvisorSEO workspace: sites, business profile, keywords, plans, content and leads. Public pages of the user's site for audits and crawler checks. Search Console and Analytics only for properties the user connected. Google Search Console, Analytics and Tag Manager for accounts the user connects. |
| Where is it sent? | mcp.advisorseo.ai (tool calls), app.advisorseo.ai (sign-in, consent, account), Google APIs under the user's own OAuth (Search Console, Analytics, Tag Manager), Chrome UX Report under AdvisorSEO's API key (public URLs only), Google PageSpeed Insights (public URLs), Bing Webmaster Tools under the user's own key, IndexNow on a confirmed submit and after each approved publish once a key is connected, the user's WordPress site through the AdvisorSEO Connect plugin for AI crawler counts, Google Ads Keyword Planner and a Google results API under AdvisorSEO's own access (keywords only), public pages of other sites the user names, the user's WordPress site on a confirmed publish. |
| Does the plugin run local code? | No. Skills are text; the connector is remote over https. |
| Does it write? | Yes, through the tools listed in README.md, including Search Console, Analytics and Tag Manager. Changes preview first and wait for an approval turn; the README names the one that only saves a measurement. |
| Credentials | OAuth through Claude's credential store. Nothing is pasted into chat. WordPress uses an application password stored on the site record. |
| Storage | The encrypted Google connection and chosen properties, and rank and PageSpeed snapshots the user runs. Other Google reports are not stored. |
| Retention and deletion | As stated at https://advisorseo.ai/privacy. |
| Consumer AI apps | Never scraped or queried. |
| Payments | Payments processed by Stripe under the AdvisorSEO label. The plugin itself takes no payment. |

### Contacts, entity and account

Why: ownership of the listing is the irreversible part, and the brand shown must be AdvisorSEO only.

| Field | Value |
|---|---|
| Publisher shown | AdvisorSEO |
| Legal entity | Advisor Media Group LLC (also the LICENSE copyright holder) |
| Submitting account | The same claude.ai organization that already holds the company's existing directory listing |
| Support contact | support@advisorseo.ai |
| Security contact | support@advisorseo.ai until a security address exists. |

Why: enterprise buyers, and the agents acting for them, pick the vendor whose controls they can audit, and the portal asks for a security contact.

### Controls stated in the listing

Why: every control named in listing copy must be checkable today, and no certification is claimed.

| Control | Evidence checked 2026-10-15 |
|---|---|
| OAuth 2.1, authorization code with PKCE S256, dynamic client registration | https://mcp.advisorseo.ai/.well-known/oauth-authorization-server (`code_challenge_methods_supported: ["S256"]`, `registration_endpoint`); stated on /docs and /privacy |
| Scoped tokens (`mcp:tools`, `mcp:read`) | same metadata, `scopes_supported` |
| Approval before any site write | preview-first write tools with `confirm=true`, enforced in every skill and tested by evals/ guards |
| WordPress application password stored encrypted and revocable | stated on /privacy and /docs |
| Data-handling table | README.md, "Data flow" |

Not stated in listing copy until confirmed (lead to verify on the deployed connector): scoped agent keys and a tool-call audit log. Neither is documented on advisorseo.ai, and neither could be checked from the deployed connector's public metadata. No certification (SOC 2, ISO 27001 or other) is claimed.

## Blockers before submit

Why: each of these stops or delays review.

0. Six tools named by four skills are still in open connector pull requests (see README, "Waiting on the connector"). `python3 scripts/check_package.py . --release` fails until `scripts/pending-tools.txt` is empty. Do not submit before it passes. The "Publisher shown" brand and the new display name also need the owner's yes on the day.

1. Repository slug: install lines and the repository URL contain the GitHub organization name, which carries the parent company name. Moving the repo to an AdvisorSEO-named organization would remove it from the listing copy.

All four URL fields were checked with curl on 2026-10-15 and return 200 with AdvisorSEO page titles: /docs, /support, /privacy, /terms.
