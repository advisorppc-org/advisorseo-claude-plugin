# Train and held-out split

Why: a patch tuned on the cases it is scored on can look better without being better, so 10 of the 34 cases are kept out of the patch work.

Rule: a case is held-out when `int(sha256(case_name).hexdigest()[:8], 16) % 100 < 30`, where `case_name` is the case directory name in UTF-8. Every other case is train. The rule was fixed on 2026-11-02 at plugin main f344d1b, before any patch.

Never change this split after a patch round has started. A case added later follows the same rule. Patches are written from train failures only; held-out cases are scored, and their transcripts are not read to write a patch. Baseline triage of all failures happened before the split was used, and that triage only sorts failures into buckets.

Check it: `python3 scripts/check_split.py`

## Held-out (10)

- ai-readiness-check--no-rank-claim
- analytics-ga4--landing-pages
- approve-and-measure-change--measure-result
- approve-and-measure-change--publish-preview
- approve-and-measure-change--skip-preview-refused
- connect-and-import--wordpress-password
- core-web-vitals--sources
- leads--prompt-injection
- search-console--submit-sitemap
- tag-manager-tracking--audit

## Train (24)

- ai-readiness-check--can-chatgpt-read
- ai-readiness-check--checklist-failures
- analytics-ga4--add-key-event
- analytics-ga4--setup-review
- connect-and-import--add-site
- connect-and-import--google-connect
- core-web-vitals--field-data
- core-web-vitals--no-data
- core-web-vitals--trend
- leads--mark-contacted
- leads--new-leads
- pages-to-win--content-calendar
- pages-to-win--ten-cap
- pages-to-win--what-pages
- search-console--is-indexed
- search-console--top-queries
- site-audit--audit-my-site
- site-audit--new-run-needs-approval
- site-audit--watch-offer
- start-here--overview-first
- start-here--route-to-readiness
- start-here--should-not-fire
- tag-manager-tracking--add-tag
- tag-manager-tracking--publish-guard
