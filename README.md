# AdvisorSEO for Claude Code

AdvisorSEO is an AI manager that gets SEO and lead work done for a business website.
It plans content from the business's own profile and real keywords, writes and reviews
the articles, sends approved ones to WordPress, and works the leads the site captures —
inside Claude Code, in the same conversation where the work is being decided.

This repository is the Claude Code plugin. Installing it connects Claude to the
AdvisorSEO connector at `https://mcp.advisorseo.ai/mcp` and adds three skills that know
how to run the work end to end.

## Install

In Claude Code:

```
/plugin marketplace add atmosphere-ai/advisorseo-claude-plugin
/plugin install advisorseo@advisorseo
```

Then restart Claude Code, or start a new session, so the connector loads.

## Connect and consent

The connector is a remote MCP server over Streamable HTTP, authorized with OAuth. You
sign in once, in your browser, to the AdvisorSEO account that owns your sites.

1. After installing, Claude asks you to authenticate with AdvisorSEO.
2. A browser window opens on the AdvisorSEO sign-in page.
3. You review what Claude is being allowed to do and approve it.
4. The window closes and Claude can read and work your sites.

Nothing is stored in this repository and nothing is asked of you in the chat — no keys,
no passwords, no headers to paste. Your authorization is held by Claude Code's own
credential store and can be revoked at any time by removing the plugin or by revoking
the connection from your AdvisorSEO account.

Your workspace is yours alone: every call is scoped to the account you signed in with,
and one account can never read or change another's sites, content or leads.

## Every write asks first

AdvisorSEO never changes anything on the first call. Each write answers with a preview
of exactly what it would do and changes nothing; it happens only when it is called again
with your confirmation. Publishing to WordPress goes further — the preview also tests
the WordPress connection and shows you the exact article that would be sent, before a
word reaches your live site.

The skills in this plugin are written to that rule and never work around it.

## The three skills

Claude picks the right one from what you ask for; you do not have to name them.

### seo-content-plan

From a business profile and your target keywords to a scheduled content calendar and a
first draft. It reads or fills in your business profile, can run an SEO audit of the
live domain to ground the plan in real findings, stores your keywords, builds the
calendar with dates and priorities, and writes the first article.

Ask for it with something like *"plan three months of posts for my plumbing business"*
or *"turn these keywords into a calendar"*.

### publish-to-wordpress

Draft, review, confirm, publish. It finds the draft, walks you through the review, marks
it approved, previews the publish against your live WordPress, and sends it only when you
say so. It can also stage the article as a WordPress draft instead, so a human presses
publish on your own site.

Ask for it with something like *"publish that post"* or *"stage it in WordPress first"*.

### lead-triage

The leads your site captured, worked properly. It lists what is new, opens a single lead
with its full history, and moves leads through `new` → `contacted` → `qualified` →
`converted` or `lost`, with a note recording what actually happened at each step.

Ask for it with something like *"any new leads?"* or *"mark that one contacted"*.

## Requirements

- Claude Code with plugin support.
- An AdvisorSEO account — sign up at [advisorseo.ai](https://advisorseo.ai).
- For publishing: a WordPress site whose address and application password are stored on
  your AdvisorSEO site record. A WordPress application password is not your account
  login password; it is a separate one you generate in WordPress and can revoke there.

## Privacy, terms and support

- Privacy: [advisorseo.ai/privacy](https://advisorseo.ai/privacy)
- Terms: [advisorseo.ai/terms](https://advisorseo.ai/terms)
- Support: [support@advisorseo.ai](mailto:support@advisorseo.ai)

## License

MIT — see [LICENSE](LICENSE).
