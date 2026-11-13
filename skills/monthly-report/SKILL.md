---
name: monthly-report
description: Use for reporting results to an owner or client, for example "write this month's SEO report", "monthly report for my client", "white-label SEO report", "what did we get from SEO last month", "which posts earned their keep", "which channel sent visits to that post", "keep or kill this post", or "show the content plan with results". Builds one month's search and AI search report from the site's own sources, reads results per post and per channel, and says plainly when a source is not connected.
license: MIT
metadata:
  version: 0.4.0
---

# Monthly report

Why: a report an owner can trust shows each number with its source and its dates, and shows a gap as a gap. This skill reports what was measured and nothing else.

## Rules that come first

1. This skill only reads, except one record: `advisorseo_channel_entry_add` stores a placement the user tells you about (preview, the user's yes in a new turn, then `confirm=true`).
2. Every number names its source and its dates. A source that reads `not_connected`, `NOT-READ`, `not available` or `partial` is reported in those words, never as zero and never left out.
3. Keep the report's own section order and wording for figures. Do not round a number into a better story, and do not add a claim the report does not contain.
4. A post that reads `too-young` or `NOT-READ` is not a `kill`. Only a `kill` the tool returned is a kill, and retiring a post is still the user's decision.
5. Compare a month with the prior month only on final data. Any rate comes with its n plus an interval, or the words "insufficient data". Never state a rank or position inside an AI assistant.

## Steps

1. Get the site from **start-here**.
2. The report: `advisorseo_monthly_report(site_id, month)` with `month` as YYYY-MM (default the last complete month). It returns the structured data and a ready `markdown` report: Search Console clicks, impressions, click rate and position against the prior month, rank movers, page two and striking distance keywords, AI assistant visits, leads from AI assistants, sampled AI visibility with n, approved changes that ran, and next month's pages to win. Pass `business_name` to head it and `agency_name` to make it white-label.
3. Per post: `advisorseo_content_planner(site_id)` shows the plan by type and status with a keep, improve or kill read beside each published post. `advisorseo_content_keep_kill(content_id)` explains one post with its 28 day window.
4. Per channel: `advisorseo_channel_report(site_id, days)` shows Search Console clicks plus GA4 sessions and key events from tagged links for each post. `advisorseo_channel_link(content_id, channel)` builds the tagged link to use when a post is shared, so the next report can count it.
5. Give the user the report as written, then three lines of your own: what moved most and why you think so, what could not be read and how to connect it (**connect-and-import**, **rank-tracking** for snapshots, **ai-visibility** for samples), and one next step.

## Check

The lead's eval proves this skill when, for "write this month's SEO report", the reply calls `advisorseo_monthly_report`, keeps every figure with its source and dates, reports each `not_connected` section in those words and not as zero, calls no post a kill that the tool did not, and gives any rate with its n or the words "insufficient data".
