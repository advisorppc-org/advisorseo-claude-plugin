---
name: rank-tracking
description: Use for tracking Google positions over time and explaining a change, for example "track my rankings", "where do I rank for my keywords", "what moved this week", "which keywords are on page two", "why did my clicks drop", "impressions are up but clicks are flat", "why does this page not rank for this keyword", or "is AI search taking my clicks". Stores daily positions from the site's own Search Console, reads what moved over 7 and 28 days, compares two periods, and checks one page against one keyword.
license: MIT
metadata:
  version: 0.4.0
  needs: "advisorseo_search_trend (connector pull request 96)"
---

# Rank tracking

Why: a position is useful only next to its history and its clicks. This skill keeps the history from the site's own Search Console, so every movement it reports is one Google recorded.

## Rules that come first

1. Positions are Google's average position in Google Search for this site, from Search Console. Never present one as a rank inside an AI assistant.
2. Data ends three days ago, when Search Console is final. Say the dates of each window you compare.
3. A change is reported with its impressions as n. On a keyword with few impressions say "insufficient data" instead of calling a move real.
4. `impressions_up_clicks_flat` is consistent with an AI Overview or another search feature answering the query. It is not proof of one. Say it that way.
5. `advisorseo_search_trend` is not available yet on every connection. If it is not in the connected tool list, say the period comparison is not available yet and use `advisorseo_rank_table` with `gravity_gsc_search_analytics` instead.
6. `advisorseo_rank_snapshot` writes AdvisorSEO's own rank tables and reads Google. Show the plan it returns, wait for the user's yes in a new turn, then call again with `confirm=true`.

## Steps

1. Get the site from **start-here**. Google must be connected: if not, hand off to **connect-and-import**.
2. Store positions: `advisorseo_rank_snapshot(site_id, days)` without `confirm` returns the plan. After approval, `confirm=true` stores position, clicks, impressions and best page per keyword per day. The first run can backfill up to 90 days.
3. Read the table: `advisorseo_rank_table(site_id, sort="change_7d")`. A `no_snapshot` status means nothing is stored yet: go back to step 2. Useful filters: `movers="down"`, `min_position=10.01` with `max_position=20` for page two, `min_impressions` to drop noise.
4. What changed between two periods: `advisorseo_search_trend(site_id, days)` gives each query and page a trend (`rising`, `falling`, `steady`, `new`, `lost` or `impressions_up_clicks_flat`) and puts AI assistant sessions beside Organic Search sessions.
5. Why one page does or does not rank: `advisorseo_onpage_check(site_id, keyword, url)` checks title, meta, h1, internal links, structured data, canonical, noindex and field Core Web Vitals, and lists the next three fixes.
6. Report: the biggest movers with dates, clicks and impressions, the page two keywords closest to page one, and one next step. A fix goes through **approve-and-measure-change**. A page that loses clicks to an answer feature goes to **answer-ready-pages**.

## Check

The lead's eval proves this skill when, for "what moved this week?", the reply calls `advisorseo_rank_table`, names the dates compared, gives impressions beside each move or says "insufficient data", states no position inside an AI assistant, and the first `advisorseo_rank_snapshot` call carries no `confirm`.
