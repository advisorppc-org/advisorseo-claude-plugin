# Directory submission pack

Why: every field the claude.ai/directory/manage portal asks for is prepared here, so the submission happens in one sitting and the listing copy is reviewed in git before it is public.

Order: submit the MCP connector first, then the plugin paired with it. Updates ship by merging to the tracked branch (`main`).

## 1. Connector submission

| Field | Value |
|---|---|
| Name | AdvisorSEO |
| Server URL | https://mcp.advisorseo.ai/mcp |
| Transport | Streamable HTTP, https only |
| Authentication | OAuth (sign-in and consent at app.advisorseo.ai) |
| Tool count | 336 (read-only and write tools, annotated; writes to a site, a record or a Google account preview first) |

## 2. Plugin submission

| Field | Value |
|---|---|
| Name | AdvisorSEO |
| Slug | advisorseo |
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

Get found in Google and in AI assistants: AI-crawler readiness, site audits, Search Console, GA4 and Tag Manager, with changes to your site and Google previewed and approved first.

### Description (2,000 characters or fewer)

AdvisorSEO helps a business get found in Google and in the answers AI assistants give. Install it and Claude can check whether AI search and user-fetch crawlers are allowed to read your site, audit the live site and explain each finding with its evidence, choose the ten pages most worth winning with the gap each one fills and the metric it should move, and track the leads your site brings in.

It works on its own: it watches the site, proposes each change with its reason, asks for one approval, applies it, then measures and reports the result with n and an interval, or insufficient data (site-audit and ai-readiness-check watch, site-audit and pages-to-win propose, approve-and-measure-change applies and measures, leads reports pipeline results).

Controls you can audit: sign-in is OAuth 2.1, authorization code with PKCE (S256) and dynamic client registration, so no key or password is ever pasted. Tokens carry the scopes mcp:tools and mcp:read. Nothing changes on your site without your yes. Every change to a site, a record or a Google account first returns a preview of exactly what it would do, and the change happens only after you approve it in your own next message. Publishing to WordPress tests the connection and shows the exact article before anything reaches your live site, and you can stage it as a WordPress draft instead.

Every result statement comes with n and an interval, or the words "insufficient data", and AdvisorSEO never claims a rank position inside an AI assistant. It never scrapes consumer AI apps.

It reads and, on your approval, changes Google Search Console, Google Analytics 4 and Google Tag Manager under your own Google consent, and reads Core Web Vitals from the Chrome UX Report.

The plugin bundles the AdvisorSEO connector and thirteen skills: start-here, ai-readiness-check, site-audit, pages-to-win, approve-and-measure-change, connect-and-import, leads, search-console, analytics-ga4, tag-manager-tracking core-web-vitals, connect-your-site and publish-blog-seo-aeo-geo.

Publishing routes are checked per user: WordPress through secure application-password or working plugin setup, coded sites through Claude Code, and Shopify, Wix, Framer, Webflow or other CMSs through their available official Claude connectors when they support publishing. Otherwise the result is an export, not a live publish.

### Use cases

1. "Can ChatGPT and Claude read my site?" Every AI bot is marked ok or blocked, with the reason.
2. "Audit my site." Up to ten findings with page, evidence and fix, compared with the last run.
3. "What pages should I create?" Up to ten pages, each with a gap type and the metric it should move.
4. "Publish that post." A preview, your approval, the publish, and the metric to watch.
5. "Any new leads?" New leads, each lead's history, and status moves with notes.
6. "Which queries bring clicks?" Search Console queries, pages, sitemaps and URL inspection.
7. "Audit my GTM container." Tags, triggers and consent checked, with draft fixes on approval.

### Data handling answers

| Question | Answer |
|---|---|
| What data does the plugin access? | The user's AdvisorSEO workspace: sites, business profile, keywords, plans, content and leads. Public pages of the user's site for audits and crawler checks. Search Console and Analytics only for properties the user connected. Google Search Console, Analytics and Tag Manager for accounts the user connects. |
| Where is it sent? | mcp.advisorseo.ai (tool calls), app.advisorseo.ai (sign-in, consent, account), Google APIs under the user's own OAuth (Search Console, Analytics, Tag Manager), Chrome UX Report under AdvisorSEO's API key (public URLs only), Google PageSpeed Insights (public URLs), the user's WordPress site on a confirmed publish. |
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
| Publisher shown | Advisor Media Group LLC |
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

1. Repository slug: install lines and the repository URL contain the GitHub organization name, which carries the parent company name. Moving the repo to an AdvisorSEO-named organization would remove it from the listing copy.

All four URL fields were checked with curl on 2026-10-15 and return 200 with AdvisorSEO page titles: /docs, /support, /privacy, /terms.
