---
name: bing-webmaster
description: Use for Bing and the engines that share its index, for example "connect Bing Webmaster Tools", "how am I doing on Bing", "what Bing searches do I show up for", "how many pages has Bing indexed", "Bing crawl errors", "set up IndexNow", "tell Bing this page changed", or "is my site in Copilot's index". Connects the owner's own Bing Webmaster Tools key, reads queries, index status, crawl issues and backlinks, and announces changed pages through IndexNow on approval.
license: MIT
metadata:
  version: 0.4.0
---

# Bing Webmaster and IndexNow

Why: Bing's index feeds Copilot and several other assistants and search engines, and it is the only free official source of backlinks. A site that is healthy on Bing is readable by more than Bing.

## Rules that come first

1. The Bing key is the site owner's own, from Bing Webmaster Tools, Settings, API Access. Ask the user to paste it only for the connect call. Never repeat it back, never put it in a summary, and never store it anywhere but the connect tool.
2. Connecting, disconnecting, storing an IndexNow key and submitting URLs are writes. Show the preview, wait for the user's yes in a new turn, then call again with `confirm=true`.
3. These are Bing's numbers, not Google's. Say so beside every figure. A state of `empty`, `partial`, `not_connected` or `not_verified` is not zero: report the state and the `next_action` the tool returned.
4. IndexNow `accepted` means the list was received, not that a page was crawled or indexed. Google does not use IndexNow.
5. Being in Bing's index does not mean an assistant will cite the page. Never state a rank or position inside an AI assistant. Any rate comes with its n plus an interval, or the words "insufficient data".

## Steps

1. Get the site from **start-here**.
2. Is it connected and verified: `advisorseo_bing_sites(site_id)`. If `not_connected`, walk the user to their key, then `advisorseo_bing_connect(site_id, site_url, api_key)` (preview, approval turn, confirm; the key is checked against Bing before anything is stored). `advisorseo_bing_disconnect(site_id)` removes it.
3. Read:
   - `advisorseo_bing_index_status(site_id, days)`: pages in the index, crawled pages, errors and the change over the window.
   - `advisorseo_bing_crawl_issues(site_id)`: each URL Bing had trouble with and why.
   - `advisorseo_bing_queries(site_id)`: Bing searches with impressions, clicks and average position.
   - `advisorseo_bing_backlinks(site_id)`: pages with inbound links, or the links to one `url`.
   - `advisorseo_bing_keywords(site_id, keyword)`: Bing volume and related keywords.
4. IndexNow, for a WordPress site running the AdvisorSEO Connect plugin: `advisorseo_indexnow_connect(site_id, key)` with the key the plugin's settings show (preview, then confirm; the key file is fetched and must match). `advisorseo_indexnow_remove(site_id)` forgets it.
5. Announce changed pages: `gravity_indexnow_submit(site_id, urls=[...])`, at most 100 pages on the connected host (preview, then confirm).
6. Report the state, the two or three issues that block the most pages, and one next step. A page fix goes through **approve-and-measure-change**.

## Check

The lead's eval proves this skill when, for "how am I doing on Bing?", the reply calls `advisorseo_bing_sites` or `advisorseo_bing_index_status`, labels the numbers as Bing's, reports a `not_connected` or `empty` state as that state and not as zero, never repeats an API key, and calls no write tool with `confirm=true` before a user approval turn. Any rate carries its n or the words "insufficient data".
