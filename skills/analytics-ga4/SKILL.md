---
name: analytics-ga4
description: Use for Google Analytics 4 work on a connected site, for example "how many sessions from organic search", "which landing pages convert", "what is happening on my site right now", "mark this event as a key event", "add a custom dimension", "check my GA4 setup", "what is my data retention". Reads reports, realtime and property settings, and changes GA4 configuration after approval. Not for Search Console queries (use search-console).
license: MIT
metadata:
  version: 0.3.0
---

# GA4 analytics

Why: traffic only matters when it is tied to what visitors did, and GA4 setup errors quietly corrupt every later number.

## Rules that come first

1. Any rate or change you report comes with its n plus an interval, or the words "insufficient data". Say so when a result is flagged `sampled` or `thresholded`.
2. Every GA4 tool that creates, updates, archives or deletes changes the user's GA4 property. Show the preview, wait for the user's yes in a new turn, then call again with `confirm=true`. Say first when a change affects data collected from now on, and that past data does not change.
3. Deleting a property or account, and submitting a user deletion, need the exact name repeated in that yes, because they cannot be undone from here.
4. Never ask for a password, key or Measurement Protocol secret in chat.

## Steps

1. Get the site from **start-here**. `gravity_google_connection(site_id)` shows the connection and the chosen property.
2. Not connected, or `needs_reconsent`: hand the site owner the link and wait.
3. No property set: `ga4_account_summaries_list(site_id)`, ask which property, then `gravity_google_set_properties`.
4. Reports: `ga4_get_metadata` for valid field names, then `gravity_ga4_report`. `ga4_check_compatibility` explains a refused combination. `ga4_realtime_report` covers the last 30 minutes. `ga4_run_pivot_report` covers cross-tabs.
5. Setup review: `ga4_streams_list`, `ga4_streams_get_enh_meas`, `ga4_key_events_list`, `ga4_get_retention`, `ga4_audiences_list`, and `ga4_accounts_change_history` for who changed what. Report each gap with the setting and its current value.
6. Changes: `ga4_key_events_create`, `ga4_custom_dims_create`, `ga4_custom_metrics_create`, `ga4_update_retention`, `ga4_streams_update_enh_meas`, each preview first.
7. Tag not firing: go to **tag-manager-tracking**.

## Check

The lead's eval proves this skill when the reply calls `gravity_ga4_report` for a traffic question, reports n or "insufficient data" on any rate, and calls `ga4_key_events_create` with no `confirm=true` in the first turn.
