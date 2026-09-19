---
name: publish-to-wordpress
description: Use when an article held in AdvisorSEO should go to a WordPress site — for example "publish that post", "push the draft live", "send the article to WordPress", "stage it as a WordPress draft first", or "is the WordPress connection working". Runs the draft, review, confirm, publish flow, always showing a preview of exactly what would be sent before anything goes live.
---

# Send an approved article to WordPress

This is the one flow that changes a live website. It runs in four beats — draft,
review, confirm, publish — and the preview beat is never skipped, never merged into
the confirm beat, and never run in the same turn as the confirm without the person
answering in between.

## 1. Find the draft

- `gravity_list_content(site_id=..., status="draft")` — the site's articles as metadata
  only: title, slug, status, word count, SEO score. `status` filters to `draft`,
  `approved` or `published`.
- `gravity_list_content(content_id=...)` — that single page in full, including its HTML
  and markdown body. This is the call that gets you the article itself; the list call
  never returns a body.

## 2. Review it with the person

Show them the article and its meta fields. Check the obvious things before anything
leaves the workspace:

- The title and meta description read like the business, not like filler.
- The target keyword is actually used, and not stuffed.
- Links and claims are real.
- Nothing in the body is a placeholder.

Fix anything they flag with `gravity_save_content(content_id=..., ...)` — preview first,
then `confirm=true`. Every edit snapshots the previous body as a version, so a bad edit
is recoverable.

## 3. Mark it approved

WordPress will only accept a page whose status is `approved` or `published`.

- `gravity_save_content(content_id=..., status="approved")` — preview, then confirm.
  Approving also stamps the approval time.

## 4. Preview the publish — always

- `gravity_publish_wordpress(content_id, wp_status="publish")` **without** `confirm`.
  This tests the WordPress connection and returns exactly what would be published.
  It sends nothing.

Show that preview to the person in full. If the connection test fails, stop and report
it — the site's WordPress address and stored sign-in details are set on the site record
with `gravity_update_site`, and fixing them is their call, not yours.

## 5. Publish only on an explicit go-ahead

- `gravity_publish_wordpress(content_id, wp_status="publish", confirm=true)` — live on
  the site.
- `wp_status="draft"` instead stages the article inside WordPress for a human to press
  publish there. When the person is unsure, or it is the first article to this site,
  offer the WordPress draft route first.

Do not confirm on an implied yes, a general earlier approval, or your own judgement that
the article is good. The go-ahead must be for this article, in this turn.

## 6. Verify

- `gravity_list_content(site_id=..., status="published")` — the page should now be listed
  as published.
- Report the live URL that came back, and note the publish in what you tell the person.

If the person asks to skip the preview, do the preview anyway and show it. It costs one
call and it is the only thing standing between a draft and somebody's live website.
