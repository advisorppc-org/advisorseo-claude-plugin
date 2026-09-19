---
name: seo-content-plan
description: Use when someone wants an SEO content plan, an editorial calendar, or a first article for a website — for example "plan three months of blog posts for my plumbing business", "what should we write about to rank", "turn these keywords into a calendar", or "write the first post". Takes a business profile and target keywords, stores them against the site in AdvisorSEO, builds a scheduled content calendar, and writes the first draft.
---

# Plan SEO content and write the first draft

Work in order. Every write below answers with a preview first and changes nothing
until it is called again with `confirm=true`. Show the person the preview, wait for
their word, then confirm. Never pass `confirm=true` on the first call.

## 1. Find or register the site

- `gravity_list_sites` — list the sites in the workspace and pick the one being worked on.
- No matching site: `gravity_create_site` with `name` and `domain`. Preview, then confirm.
  Note the `site_id` that comes back; every later call needs it.

## 2. Read the business profile

- `gravity_get_profile(site_id)` — business name, type, location, brand voice, target
  audience, selling points, services, hours.
- `configured: false` means nothing is stored yet. Ask the person for what is missing,
  then `gravity_set_profile(site_id, ...)`. Preview, then confirm.

The profile is what makes the plan specific to this business rather than generic. Do not
skip it — a calendar built without it is guesswork.

## 3. Ground the plan in the site's real state (recommended)

- `gravity_audit_domain(domain)` — run an SEO audit of the live domain. This one is a
  read that still takes `confirm`; preview, then confirm to run it.
- `gravity_audit_findings(run_id)` — the findings from that run.
- `gravity_audit_history(domain)` — earlier runs, to see what has changed.

Let real findings steer the plan: gaps the audit names are usually better topics than
anything invented from scratch.

## 4. Store the keywords

Keyword research is yours to do — think it through from the profile, the audit and what
the business actually sells. AdvisorSEO stores what you hand it; it does no research of
its own.

- `gravity_add_keywords(site_id, keywords=[...])` — each item takes `keyword` (required),
  `search_volume`, `difficulty` (1-100), `cpc_cents`, `intent` (`informational`,
  `commercial`, `transactional` or `navigational`), `page_type` and `cluster_id`.
  Preview shows a count and a sample; confirm to store.
- `gravity_list_keywords(site_id)` — read back what is stored.

## 5. Build the calendar

- `gravity_add_strategies(site_id, items=[...])` — each item takes `title` (required),
  `target_keyword`, `content_type` (`blog_post`, `service_page`, `landing_page` or
  `faq_page`), `search_intent`, `priority` (1 = highest), `notes`, and `days_from_now`,
  which sets the scheduled publish date. Space the dates to a cadence the business can
  actually keep. Preview, then confirm.
- `gravity_list_strategies(site_id)` — read the calendar back and show it.

## 6. Write the first draft

Write the article yourself, in the brand voice from the profile, against the planned
item's target keyword and search intent.

- `gravity_save_content(site_id, title=..., content=..., meta_title=...,
  meta_description=..., target_keyword=..., content_type=..., strategy_id=...,
  status="draft")` — `content` is the HTML body. Pass the `strategy_id` of the calendar
  item so the draft stays tied to its plan. Preview, then confirm.
- `gravity_list_content(site_id)` — confirm it landed.

## 7. Close the loop

- `gravity_overview(site_id)` — keyword, calendar, content and lead counts in one read.

Report what was stored, what is scheduled and when, and what the next draft is. Publishing
is a separate step: hand off to the publish-to-wordpress skill when the draft is reviewed.
