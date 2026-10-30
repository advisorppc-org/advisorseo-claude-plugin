---
name: site-audit
description: Use for a website audit or technical SEO review, for example "audit my site", "what is wrong with my website", "run an SEO audit", "check my site health", "what changed since the last audit", "watch my site for problems", or "show the audit findings". Runs an audit of the live domain, reads its findings in plain priority order, compares with earlier runs, and can put the domain on a recurring watch.
license: MIT
metadata:
  version: 0.3.0
---

# Site audit

Why: findings tell the owner what to fix first. A grade or a score does not, so this skill reports findings with their evidence and their effect.

## Rules that come first

1. Report findings, never letter grades. Do not invent an overall score and do not translate one into A to F.
2. Do not recommend adding FAQ schema or FAQ blocks as a fix. It is not counted as a finding to act on.
3. Starting an audit and starting a watch are actions the user must approve. Show the preview the tool returns, wait for the user's yes in a new turn, then call again with `confirm=true`.
4. Each finding carries the page it was found on and the evidence the tool returned. No finding without evidence.
5. Any rate you report (share of pages failing, for example) comes with its n plus an interval, or the words "insufficient data". Never state an AI rank position.

## Steps

1. Get the site and domain from **start-here**.
2. `gravity_audit_history(domain)`: earlier runs. If a recent run exists, offer to read it instead of running a new one.
3. `gravity_audit_domain(domain)`: preview first, then `confirm=true` after the user approves.
4. `gravity_audit_findings(run_id)`: the findings of that run.
5. Present at most 10 findings, highest effect first. For each: what is wrong, where, the evidence, the fix, and who can make it (the user, their developer, or AdvisorSEO through **approve-and-measure-change**).
6. When there is an earlier run, say what was fixed, what is new and what is unchanged.
7. Offer `gravity_audit_watch` to re-check the domain on a schedule (preview, then confirm). `gravity_audit_due` lists the watched domains that are due.
8. For page speed questions, `gravity_geo_pagespeed` reads the speed data for a page.

## Check

The lead's eval proves this skill when the reply calls `gravity_audit_domain` (or reads an earlier run with `gravity_audit_history`) and `gravity_audit_findings`, lists findings with page and evidence, contains no letter grade (no "grade A" to "grade F" and no "score of"), contains no FAQ-schema advice, and never passes `confirm=true` in the same turn as the first preview.
