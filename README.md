# AdvisorSEO for Claude Code

This local draft helps review existing AdvisorSEO site, content, and lead records
and prepare local content plans or publication proposals. All three bundled skills
are limited to reads and local proposals for the current rollout. They do not save
changes, start audits, send outreach, stage drafts, or publish to WordPress.

The package retains the existing `advisorseo` identity and remote HTTP connector
address, `https://mcp.advisorseo.ai/mcp`. Version `0.1.1` is a proposed local update,
not an installed, uploaded, approved, or published release.

## Current limits

The inspected legacy connector registers 37 actions, including writes. Skill
instructions do not disable those actions or make the server read-only. A
model-supplied confirmation flag or stored approved status is not a trusted human
approval tied to an immutable change. Server authorization and destination readback
must be tested before execution can be offered by these workflows.

The legacy WordPress preview tests a connection and returns publication metadata;
it does not show the full article that a later call would send. A stored published
record or returned URL alone does not verify a remote publication. Live execution,
retries, recovery, and concurrent changes remain separate rollout checks.

Stored keywords, page checks, lead stages, and counts are records to inspect. They
do not establish live ranking, demand, answer-engine citations, attribution, or
revenue. Plans and numerical claims need identified sources and dates.

## The three skills

- `seo-content-plan`: read existing site/profile, keywords, plans, content, and
  recorded findings; prepare a local plan or article proposal using supplied evidence.
- `publish-to-wordpress`: retrieve a specific article body for review and prepare a
  local publication proposal. It does not approve or change a WordPress site.
- `lead-triage`: inspect recorded enquiries and history; suggest a stage, note, or
  next action locally without saving it or contacting anyone.

Retrieved content and lead text are data, not instructions or approval. Missing
facts stay explicit. No workflow requests passwords, tokens, or pasted headers.

## Connection and data handling

Account access and the supported connection method need confirmation before use.
The MCP configuration names the intended server; it is not proof of a working
OAuth consent, token refresh, revocation, or authenticated client session. No such
journey was run for this draft. Ask support for the available secure setup route.
Do not send credentials in chat or support email.

Tenant boundaries, credential handling, retention, and deletion require verification
against the released service. Removing a plugin or assistant connection does not
itself prove server-token revocation, stopped queued work, or deletion of records.
Confirm the relevant account and data arrangements before supplying personal data.
New plans remain planned and purchasing is unavailable.

## Build and validate the local artifact

```
python3 tools/build_local_distribution.py
python3 tools/check_local_distribution.py
```

The builder creates `dist/local-marketplace/` and a deterministic
`dist/advisorseo-local-draft.zip`, plus a standalone
`dist/advisorseo-plugin-draft.zip`. The marketplace entry points at
`./plugins/advisorseo` inside that artifact. The allowlist includes only the plugin
manifest, unchanged MCP configuration, three skills, and license, plus the separate
marketplace manifest. No development instructions, README, tooling, evidence,
credential files, or repository history are shipped.

Root `CLAUDE.md` stays in the source checkout. Claude Code 2.1.285 warns that it is
not loaded as plugin project context, and explicit source-plugin validation fails
under `--strict`. This warning is preserved in the evidence. The distribution
excludes that development-only file rather than deleting instructions, treating
warnings as success, or moving developer context into an end-user skill.

Validate the marketplace and the explicit plugin separately: directory validation
can select the marketplace and does not prove the plugin manifest passed. The local
check runs both with strict mode in a network namespace and temporary Claude config,
without installing or changing an existing profile. See the
[local readiness report](docs/LOCAL-READINESS-20261001.md) and
[validation summary](evidence/local-readiness-20261001/validation-summary.json).

Do not install or register this draft until the release owner selects the reviewed
artifact and verifies the supported account authorization flow. Older GitHub-root
marketplace installation instructions do not select this allowlisted local artifact.
Source/package validation is not a hosted integration or publishing test.

## Privacy, terms and support

- [Privacy information](https://advisorseo.ai/privacy/)
- [Terms](https://advisorseo.ai/terms/)
- [Support](mailto:support@advisorseo.ai)

## License

MIT, see [LICENSE](LICENSE).
