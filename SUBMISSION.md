# Directory submission pack

Why: every field the claude.ai/directory/manage portal asks for is prepared here, so the owner submits in one sitting and the listing copy is reviewed in git before it is public.

Order: submit the MCP connector first, then the plugin paired with it. Updates ship by merging to the tracked branch (`main`).

## 1. Connector submission

| Field | Value |
|---|---|
| Name | AdvisorSEO |
| Server URL | https://mcp.advisorseo.ai/claude-directory |
| Transport | Streamable HTTP, https only |
| Authentication | OAuth (sign-in and read-only consent at app.advisorseo.ai), scope `mcp:read` |
| Tool count | 6, all read-only |

## 2. Plugin submission

| Field | Value |
|---|---|
| Name | AdvisorSEO |
| Slug | advisorseo |
| Repository | https://github.com/advisorppc-org/advisorseo-claude-plugin (public) |
| Tracked branch | main |
| Version | 0.3.0 |
| License | MIT |
| Icon | `icon.png`, 512 by 512 PNG (the advisorseo.ai site icon) |
| Homepage | https://advisorseo.ai |
| Documentation | https://advisorseo.ai/docs |
| Support | https://advisorseo.ai/support |
| Privacy policy | https://advisorseo.ai/privacy |
| Terms of service | https://advisorseo.ai/terms |
| Categories | Marketing; Productivity |

### One-liner (200 characters or fewer)

Read your saved AdvisorSEO workspace in Claude: websites, tracked keywords and saved content. Review drafts and plan missing pages. Read-only.

### Description (2,000 characters or fewer)

AdvisorSEO helps a business plan and improve the content that gets it found in search. This plugin connects Claude to your AdvisorSEO workspace so you can work with the research and drafts you have already saved there.

Ask "show my SEO workspace" and Claude reads the counts of your saved websites, keywords, strategies and content, picks the right website, and suggests where to start. Ask "which keywords are we tracking" for a table of stored volume, difficulty and intent with the date the research was last checked. Ask "review my draft" and Claude reads the saved record against its target keyword and suggests three to five edits, each with the current text, the suggested text and the reason. Ask "what pages should I create" for up to ten saved keywords that have no page yet, sorted by intent, volume and difficulty.

The connection is read-only. It cannot publish, edit or delete anything, and every suggestion stays in the chat for you to apply in AdvisorSEO. Saved records are described as stored research, never as live rankings, traffic or revenue, and when the data is too thin the skills say "insufficient data". Retrieved text is treated as data, never as instructions.

Sign in once with your AdvisorSEO account and approve read-only access. No key or password is pasted into the chat. The plugin bundles the connector and five skills: start-here, keyword-review, content-review, content-gap-plan and more-capabilities. It runs no local code and has no hooks.

### Use cases

1. "Show my SEO workspace." Counts of saved records, the right website, and a next step.
2. "Which keywords are we tracking for my site?" Stored volume, difficulty and intent, with the research date.
3. "Review my draft about water heaters." Three to five edits with the record ID.
4. "What pages should I create?" Up to ten keywords with no page yet.
5. "Can AdvisorSEO publish to WordPress?" What this connection reads, and how to add the separate full connector.

### Data handling answers

| Question | Answer |
|---|---|
| What data does the plugin access? | Stored records in the AdvisorSEO workspace the user approved: websites (name, domain, status), saved keywords, saved content. No credentials, lead contacts or lead-form keys. |
| Where is it sent? | mcp.advisorseo.ai (tool calls), app.advisorseo.ai (sign-in and consent). Results go to the user's Claude session. |
| Does the plugin run local code? | No. Skills are text; the connector is remote over https. No hooks. |
| Does it write? | No. All six tools are read-only (`readOnlyHint: true`). |
| Credentials | OAuth through Claude's credential store. Nothing is pasted into chat. |
| Retention and deletion | As stated at https://advisorseo.ai/privacy. |
| Payments | The plugin takes no payment and the directory reads add no paid tier. |

### Contacts, entity and account

Why: ownership of the listing is the irreversible part, and the brand shown must be AdvisorSEO only.

| Field | Value |
|---|---|
| Publisher shown | AdvisorSEO (decided by the owner, 2026-10-15) |
| Legal entity | Advisor Media Group LLC (decided by the owner, 2026-10-15; also the LICENSE copyright holder) |
| Submitting account | The same claude.ai organization that already holds the company's existing directory listing (decided by the owner, 2026-10-15) |
| Support contact | support@advisorseo.ai |
| Security contact | Recommended: security@advisorseo.ai. Owner decision pending. |
| Security page | Recommended: https://advisorseo.ai/security, listing the controls below. Owner decision pending (the URL returns 404 today). |

Why: enterprise buyers, and the agents acting for them, pick the vendor whose controls they can audit, and the portal asks for a security contact.

### Controls stated in the listing

Why: every control named in listing copy must be checkable today, and no certification is claimed.

| Control | Evidence checked 2026-10-21 |
|---|---|
| OAuth with PKCE S256 and dynamic client registration | https://mcp.advisorseo.ai/.well-known/oauth-authorization-server (`code_challenge_methods_supported: ["S256"]`, `registration_endpoint`) |
| Read-only scope | https://mcp.advisorseo.ai/.well-known/oauth-protected-resource/claude-directory (`scopes_supported: ["mcp:read"]`) |
| Read-only tools | every tool carries `readOnlyHint: true`, `destructiveHint: false` |
| Sign-in required | the server URL returns 401 without a token |

No certification (SOC 2, ISO 27001 or other) is claimed.

## Blockers before submit

Why: each of these stops or delays review.

1. Reviewer account: a test AdvisorSEO workspace with a website, saved keywords and saved content, and its sign-in shared with the reviewer through the portal.
2. A real Claude sign-in run against the exact server URL, with all six tools called once.
3. Security contact and a /security page: not live on advisorseo.ai yet.

All four URL fields were checked on 2026-10-21 and return 200: /docs, /support, /privacy, /terms.
