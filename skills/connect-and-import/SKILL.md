---
name: connect-and-import
description: Use for setting up a website in AdvisorSEO, for example "add my site", "connect my website", "set up AdvisorSEO", "import my site", "connect WordPress", "connect Google Search Console", "what platform is my site on", or "fill in my business profile". Detects the site's platform, creates the site record, saves the business profile, and explains where WordPress and Google connections are made.
license: MIT
metadata:
  version: 0.3.0
---

# Connect and import a site

Why: every other skill works from the site record and the business profile. Getting them right once saves a wrong answer in every later conversation.

## Rules that come first

1. Never ask for a password, API key, token or authorization header in the chat. Google is connected through a consent link the site owner opens in their own browser.
2. Creating a site, updating it and saving the profile are writes. Show the preview, wait for the user's yes in a new turn, then call with `confirm=true`.
3. Check `gravity_list_sites` before creating a site, so the same domain is not added twice.
4. Any rate you report comes with its n plus an interval, or the words "insufficient data". Never state an AI rank position.

## Steps

1. `gravity_overview()` then `gravity_list_sites()`: is the domain already there?
2. `gravity_detect_platform` for the domain: WordPress, Shopify or another platform. This decides how pages are published later.
3. `gravity_create_site` with `name` and `domain`. Preview, approval turn, then confirm. Keep the `site_id` it returns.
4. `gravity_get_profile(site_id)`, then `gravity_set_profile(site_id, ...)` with business name, type, location, brand voice, target audience, selling points, services and hours. Ask the user for what you do not know. Preview, approval turn, then confirm.
5. WordPress: the user creates an application password in WordPress (Users, Profile, Application Passwords) and stores it with the site address on the site record, either in the web app or with `gravity_update_site` (preview, approval turn, confirm). The first publish preview in **approve-and-measure-change** tests the connection.
6. Google Search Console, Analytics and Tag Manager: `gravity_google_connect_url(site_id)` gives a link that expires in 10 minutes. The site owner opens it, signs in with the Google account that can see the property, and allows the read-only Search Console and Analytics permissions. Tag Manager asks for its own link on first use. Then `gravity_gsc_sites` and `gravity_google_set_properties` choose the property. See **search-console**, **analytics-ga4** and **tag-manager-tracking**.
7. Optional: `gravity_crawl_site` to import the site's pages so audits and plans start from what exists. `gravity_crawl_pages` reads the imported pages.
8. Finish with **ai-readiness-check** as the first useful result.

## Check

The lead's eval proves this skill when the reply calls `gravity_list_sites` before `gravity_create_site`, calls `gravity_detect_platform`, never asks for a password or key in chat, points Google connection to app.advisorseo.ai, and passes `confirm=true` only after a user approval turn.
