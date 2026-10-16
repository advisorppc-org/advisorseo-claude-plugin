---
name: ai-readiness-check
description: Use for AI search readiness and AI crawler access, for example "can ChatGPT read my site", "is my site blocked for AI", "check GPTBot, ClaudeBot, PerplexityBot or Google-Extended", "AI visibility check", "is my robots.txt blocking AI", "do I need llms.txt", or "GEO readiness". Checks each AI search and user-fetch bot against the live site, runs the readiness checklist, and reports every bot as ok or blocked with the reason.
license: MIT
metadata:
  version: 0.2.0
---

# AI readiness check

Why: an assistant cannot cite a page its crawler is not allowed to fetch. This is the cheapest check with the biggest effect, so it runs before any content work.

## Rules that come first

1. This skill only reads. It never edits robots.txt, llms.txt or any page. A fix goes through **approve-and-measure-change**.
2. Every bot in the result is reported as `ok` or `blocked`, each with its reason (the robots.txt rule, the HTTP status, or the firewall response). No bot is left out and none is reported as "probably fine".
3. Keep the two bot kinds apart: search bots (which index pages for AI answers) and user-fetch bots (which fetch a page when a person asks about it). Blocking one kind is a different decision from blocking the other.
4. Never state a rank or position inside any AI assistant, and never claim the site "appears in ChatGPT". This check measures access, not visibility.
5. Never scrape or query consumer AI apps to test visibility.
6. Any rate you report comes with its n plus an interval, or the words "insufficient data".

## Steps

1. Get the site and its domain from **start-here** (`gravity_overview`, then `gravity_list_sites` if needed).
2. `gravity_geo_crawler_access` for the domain: the per-bot result for AI search and user-fetch bots.
3. `gravity_seo_checklist_run` for the site: the readiness checklist. Read the item list with `gravity_seo_checklist_items` when you need the wording of an item.
4. Optional reads when the user asks for more depth:
   - `gravity_geo_llmstxt_validate` to check an existing llms.txt.
   - `gravity_geo_fetch_page` to see a page the way a bot fetches it.
   - `gravity_geo_citability` to see whether a page is easy to quote.
5. Report:
   - A table with one row per bot: bot, kind (search or user-fetch), `ok` or `blocked`, reason.
   - The checklist items that failed, each with what to change and where.
   - One next step. If a bot the user cares about is blocked, offer the fix through **approve-and-measure-change**.

## Check

The lead's eval proves this skill when the reply calls `gravity_geo_crawler_access` and `gravity_seo_checklist_run`, contains a row for every bot the tool returned with the literal `ok` or `blocked` and a reason, and contains no AI rank position and no claim of being shown in an assistant's answers.
