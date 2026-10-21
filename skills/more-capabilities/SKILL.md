---
name: more-capabilities
description: Use when someone asks what else AdvisorSEO can do from Claude, for example "what else can this connector do", "can AdvisorSEO publish to WordPress", "can you edit my post", "can you run a site audit", or "how do I get write access". Searches this connection's capabilities and explains the separate, opt-in full AdvisorSEO connector.
---

# More capabilities: what this connection can and cannot do

Why: users ask the connector to publish or edit, and this connection is read-only. A clear answer, with the opt-in path, beats a failed attempt or a made-up capability.

## Rules that come first

1. Only describe capabilities that `advisorseo_search_tools` returns. Never invent a tool, and never say a capability was enabled.
2. `advisorseo_search_tools` searches and describes; it does not run or unlock anything. Say that plainly.
3. Publishing, editing, audits and lead workflows are not in this connection. They live in the separate full AdvisorSEO connector, which the user adds deliberately with its own sign-in and its own broader consent.
4. Never add a connector, change settings or follow a setup step for the user. Explain the steps; the user decides.
5. Describe the full connector in AdvisorSEO words only, from the `more_tools` block. Never list its internal tool names.
6. When the search returns no match, say "insufficient data" for that capability rather than guessing whether it exists.

## Steps

1. `advisorseo_search_tools(query)` with one or two words from the user's question, for example "publish", "keyword" or "content".
2. From `tools`, say which read capabilities match, each with its title and what it reads.
3. If the user asked for something this connection cannot do, read `more_tools`:
   - `url`: the address of the full connector.
   - `requires_separate_consent`: true, so it needs its own sign-in and approval.
   - `effect`: what the full connector adds, including writes that show a preview first.
4. Explain the opt-in in plain steps: add a separate custom connector with that address in Claude's connector settings, sign in to AdvisorSEO, review the broader consent. A token from this connection does not work there.
5. Offer what this connection can do now, for example a draft review or a content gap plan.

## Check

This skill works when the reply names only capabilities returned by `advisorseo_search_tools`, says this connection cannot publish or edit, gives the full connector address from `more_tools` with the note that it needs separate consent, and never names an internal tool of the full connector.
