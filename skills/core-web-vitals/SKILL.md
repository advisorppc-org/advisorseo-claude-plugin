---
name: core-web-vitals
description: Use for page speed and Core Web Vitals, for example "is my site fast", "check my Core Web Vitals", "why is my LCP slow", "has my page speed improved", "PageSpeed score for this page". Reads real-user field data, its history over time, and lab tests. Not for a full site audit (use site-audit).
license: MIT
metadata:
  version: 0.3.0
---

# Core Web Vitals

Why: field data is what Google measures from real Chrome users, and a single lab run can mislead in either direction.

## Rules that come first

1. Name the source of every number. Field data is real Chrome users over 28 days at the 75th percentile. A lab test is one simulated load.
2. `no_field_data` means too little Chrome traffic to publish. It is neither a failure nor a zero. A metric Google did not return is unknown, never zero.
3. A trend claim needs the periods shown, or the words "insufficient data". Never promise a ranking gain from a speed fix.
4. `gravity_geo_pagespeed` stores its snapshot, so it previews first: wait for the user's yes in a new turn, then call again with `confirm=true`.

## Steps

1. Field data today: `gravity_cwv_field` with `url` or `origin` and a `form_factor`. Report LCP, INP, CLS and TTFB with the good, needs-improvement and poor shares.
2. History: `crux_query_history` with the same `url` or `origin` in `body`. Report the direction across the collection periods it returns.
3. Lab: `gravity_geo_pagespeed` when no field data exists or a specific page needs a diagnosis. Keep it clearly separate from field data.
4. Status `unconfigured`: say this check is not enabled on the deployment yet, and offer the other source. Never make up a number.
5. Finish with the worst metric, the likely cause from the result, and how the user will know it worked.

## Check

The lead's eval proves this skill when the reply calls `gravity_cwv_field` first, labels the data as field data, and treats `no_field_data` as neither a failure nor a zero.
