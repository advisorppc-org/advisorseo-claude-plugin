# Security Policy

## Scope

This repository holds the plugin manifests, the marketplace definition, text skills, documentation, evaluation cases and repository checks. It holds no secrets and ships no code that runs when the plugin is used: there are no hooks, agents, commands or local servers. The repository checks under `scripts/` and `tests/` run only when a maintainer or CI runs them.

The AdvisorSEO connector is a hosted service at `mcp.advisorseo.ai`. The connector this plugin points at is read-only.

## Reporting a vulnerability

If you believe you have found a security issue in the hosted connector, the sign-in flow, or anything in this repository:

- Email **support@advisorseo.ai** with the subject line `SECURITY`.
- Include what you found, how to reproduce it, and the impact you believe it has. Please do not access other customers' data.
- Do not open a public GitHub issue for security reports.

We acknowledge reports within 3 business days and keep you informed through triage and remediation.

## Supported versions

Only the latest version of the plugin on the default branch is supported. The hosted connector is updated server-side; those fixes reach every user without a plugin update.
