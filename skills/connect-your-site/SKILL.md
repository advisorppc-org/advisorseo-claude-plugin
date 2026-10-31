---
name: connect-your-site
description: Use when someone asks to connect any website or CMS for publishing, including WordPress, Shopify, Wix, Framer, Webflow, Next.js or a custom coded site. Detects the platform, checks the publishing route actually available to this user, and hands off to WordPress setup, Claude Code, or that CMS's official Claude connector. Never treats a registered domain as a publishing connection.
license: MIT
metadata:
  version: 0.4.0
---

# Connect your site

Why: a site owner should know which connection can publish to their site before sharing access or drafting a blog.

## Rules that come first

1. Never request, repeat or pass a password, API key, token or authorization header through chat. If one was pasted, do not echo it; ask the user to revoke it and use secure setup. WordPress uses an application password, never the admin login password.
2. A domain in AdvisorSEO is a site record, not proof of a working publishing connection. Detection is a hint, not authorization. Check the user's actual available connectors and permissions.
3. Every stored change uses a preview and explicit approval in a separate user turn before `confirm=true`. Do not create a connection, install a plugin, grant access or deploy without the user's specific approval.
4. No AI rank claims. Report a rate with its sample size and interval, or say "insufficient data".

## Choose the route

1. Read `gravity_overview()` and `gravity_list_sites()` to avoid duplicate sites. If a secret was pasted, handle that first even if no connector is available.
2. Call `gravity_detect_platform(domain)` for the public domain. Read the candidates, evidence, confidence and connect status. Confirm uncertain detection with the owner. The AdvisorSEO detector currently supports a direct connection only for WordPress; its "not yet" for other platforms describes the AdvisorSEO adapter, not every possible Claude route.
3. Explain the relevant route below before any write. Use **connect-and-import** only for registering the site, profile, public page import and Google consent. Return to this skill for publishing readiness.

| Website | Publishing route | Readiness check |
|---|---|---|
| WordPress | AdvisorSEO's WordPress plugin path if the user already has a working installed plugin; otherwise the WordPress REST application-password path stored through the secure AdvisorSEO connection page. | Read the saved site's `has_wp_credentials` and WordPress address without exposing credentials. An installed plugin alone is not proof of API access. The connector's first `gravity_publish_wordpress` preview must test the connection. |
| Coded site, including Next.js, Astro or a custom repository | Claude Code with the user's authorized repository. Inspect its existing blog/content model and deployment workflow; prepare a branch and content diff for review. | Confirm repository access, build command, content location and the owner's deploy approval. This plugin does not provision a custom-site adapter or deploy a repository by registering a domain. |
| Shopify, Wix, Framer, Webflow or another CMS | That CMS's official Claude connector, when the user has it available and connected and it exposes the needed content-write/publish capability. | Inspect the actual connector and permissions. Some connectors expose only reads or a subset of CMS features. Do not invent a connector URL, operation or permission, or claim every CMS can publish today. |
| No suitable connector, unknown platform or missing write capability | Prepare an export of the blog and metadata, with manual CMS instructions or a Claude Code handoff where the site has source access. | Say publishing is unavailable through the current connection. Ask for the supported route; never report the site as connected for publishing. |

WordPress setup: use the site's secure connection page, or the existing working plugin setup. The WordPress authorization endpoint returned by detection is only a candidate endpoint; do not put credentials in a chat or a general link. Do not promise a public plugin download, directory release or an automatic credential handoff that has not been verified. If setup is missing or fails, stop at a draft and report the exact missing step. Never use `gravity_update_site` to transport a secret supplied in chat.

Custom-site adapters require a pre-existing site connection configured outside this skill. No available AdvisorSEO tool creates that connection today. Do not substitute `gravity_publish_site`: it publishes an AdvisorSEO-hosted site, not a Shopify, Wix, Framer, Webflow or repository-backed website.

## Finish

Report the detected platform, chosen route, evidence of access, and any missing setup. Then use **publish-blog-seo-aeo-geo** to prepare the content, with a preview before publishing. Google consent remains a separate optional connection through **connect-and-import**. OAuth authorization still occurs in the service's own browser flow; never bypass it.

## Check

For "connect my Wix site", detect the platform and check for the user's official Wix connector and its publish capability. If absent, offer an export and say the direct AdvisorSEO adapter is not available. Do not ask for a WordPress password or call a WordPress publishing operation. For a coded site, hand off to Claude Code and a reviewed repository diff, not an invented custom connection.
