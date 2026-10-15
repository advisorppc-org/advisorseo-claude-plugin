---
name: pages-to-win
description: Use for choosing what to write or improve, for example "what pages should I create", "what should we write about", "which keywords can we win", "plan my content", "build a content calendar", "turn these keywords into a plan", "where are my content gaps", or "plan three months of posts". Reads the business profile, stored keywords and the existing plan, then proposes at most 10 pages to win, each with a gap type and the metric it should move, and saves the approved ones to the plan.
license: MIT
metadata:
  version: 0.2.0
---

# Pages to win

Why: a short list of pages tied to a gap and a metric gets built and measured. A long calendar of guesses does not.

## Rules that come first

1. Propose at most 10 items. Each item has a gap type and the one metric it should move.
2. Gap types, use exactly one per item: `missing page` (nothing targets the query), `weak page` (a page exists but does not answer the query), `not crawlable` (an AI or search bot cannot read it), `not citable` (hard to quote: no clear answer, no facts, no source), `wrong intent` (the page type does not match what the searcher wants).
3. The metric is something AdvisorSEO or the user can measure later: organic clicks or impressions for the target query, leads from the page, or a crawler and citability check moving from fail to pass. Never an AI rank position.
4. Saving items to the plan is a write. Show the preview, wait for the user's yes in a new turn, then call with `confirm=true`.
5. Keyword volumes and difficulty are recorded values. Say where they came from and do not present them as fresh.
6. Any rate you report comes with its n plus an interval, or the words "insufficient data".

## Steps

1. Get the site from **start-here**.
2. `gravity_get_profile(site_id)`: what the business sells, where and to whom. If `configured` is false, ask for the missing parts and save them with `gravity_set_profile` (preview, then confirm).
3. `gravity_list_keywords(site_id)`: the stored keywords. If there are none, research them from the profile, then store them with `gravity_add_keywords(site_id, keywords=[...])` (preview, then confirm). Each keyword takes `keyword` and, when known, `search_volume`, `difficulty`, `intent` and `page_type`.
4. `gravity_list_strategies(site_id)`: what is already planned. Do not propose a page that is already there.
5. `gravity_list_content(site_id)`: what already exists, to tell a `missing page` from a `weak page`.
6. Optional: run **ai-readiness-check** or read `gravity_audit_findings` when the gap may be `not crawlable` or `not citable`.
7. Propose the list as a table: page title, target query, gap type, metric to move, why this one.
8. After the user approves, `gravity_add_strategies(site_id, items=[...])`. Each item takes `title`, `target_keyword`, `content_type` (`blog_post`, `service_page`, `landing_page` or `faq_page`), `search_intent`, `priority` (1 is highest), `notes` (put the gap type and metric here) and `days_from_now`. Preview, then confirm.
9. Writing and publishing a page is the job of **approve-and-measure-change**.

## Check

The lead's eval proves this skill when the reply calls `gravity_list_keywords` and `gravity_list_strategies`, proposes no more than 10 items, every item carries one of the five gap types and a named metric, no item states an AI rank position, and `gravity_add_strategies` is only called with `confirm=true` after a user approval turn.
