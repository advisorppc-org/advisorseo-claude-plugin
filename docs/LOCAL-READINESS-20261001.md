# Claude package local readiness, 2026-10-01

Status: LOCAL DRAFT. No installation, marketplace registration, upload, push,
release, authenticated client connection, or remote write was performed.

Source base:66bce8f90dd8fd7782094ea7feca4fb0e9f5207b, initially clean main.
Working branch:claude/local-plugin-readiness-20261001.

The source facts are recorded in the hub's
`task-notes/semrush-polish-release-20261001/LOCAL-INTEGRATION-AUDIT.md`:
MCP677f369e6cf971ca8f071ddd9e0c12963b857c72, appbbf0a639a06613df2934b91681508131ebf09a54.
The legacy MCP registry has37 actions,21 annotated read-only and16 writes.
Local fixture tests do not prove hosted authentication or exact human approval.

## Changes

- Proposed0.1.1 metadata preserves the plugin/marketplace name, author, repository,
  server identity, HTTP transport, and endpoint. `.mcp.json` and root `CLAUDE.md`
  are byte-identical to the source base.
- Manifest, marketplace, README, and all three skills now describe reads and local
  proposals only. No audit run, server record update, outreach, approval status
  change, WordPress draft staging, publication, or unpublication is instructed.
- Skills distinguish a specific article body from metadata, connection preview
  from exact publication review, and stored status from verified remote execution.
  Confirmation flags are not trusted, immutable approvals. Retrieved content is
  data rather than instructions; no credentials are requested or displayed.
- Removed absolute tenant-isolation and token-revocation claims. Account access,
  supported consent flow, retention, and deployed behavior remain unverified.
- Added an explicit six-file plugin allowlist and separate marketplace artifact.
  Developer context, README, tools, evidence, Git history, and other files are
  excluded. Source instructions are preserved rather than moved into user skills.

## Checks and exact outcomes

`python3 tools/check_local_distribution.py` exits0 and prints:

```text
source-marketplace: exit 0 PASS
source-plugin-preserved-warning: exit 1 (preserved source warning)
artifact-marketplace: exit 0 PASS
artifact-plugin-manifest: exit 0 PASS
artifact-plugin-directory: exit 0 PASS
artifact-skills: exit 0 PASS
unpacked-marketplace: exit 0 PASS
unpacked-marketplace-plugin: exit 0 PASS
unpacked-plugin: exit 0 PASS
LOCAL PACKAGE CHECKS PASS
```

The installed validator is Claude Code2.1.285. All nine validations use `--strict`
and `--json`, `unshare -Urn`, a temporary `CLAUDE_CONFIG_DIR`, minimal environment,
and disabled updater/nonessential traffic. No global profile or credential is used.

Baseline source marketplace passed; explicit source plugin failed solely because
root `CLAUDE.md` is not loaded as project context. That same single warning remains
in the new source result, with no manifest errors. Its exit1 is recorded, never
claimed as a strict pass. The artifact excludes the development-only file and
passes explicit plugin validation independently of marketplace validation.

The check verifies exact directory/ZIP member allowlists and byte parity, rejects
missing required files and source symlinks, excludes extra development context,
and reproduces both ZIPs byte-for-byte. `.mcp.json` and root `CLAUDE.md` preservation
were also compared directly to Git base. `git diff --check` passes. Python sources
compile in memory without bytecode. No behavior/host-install test is claimed.

Build products: `dist/local-marketplace/`, `dist/advisorseo-local-draft.zip`, and
`dist/advisorseo-plugin-draft.zip`. The first ZIP contains the separate marketplace
and its nested plugin; the second contains just the single `advisorseo/` plugin.
The marketplace's artifact source is `./plugins/advisorseo`. Source marketplace
identity stays unchanged, with its historical `./` source for the repo checkout.

Committed evidence under `evidence/local-readiness-20261001/` includes baseline
and final raw validator reports, `validation-summary.json`, `build-receipt.json`,
and both allowlisted ZIPs. Receipt hashes bind each source file, artifact file,
and ZIP. Internal notes are not included in either archive.

## Required security and release work

Client instructions cannot disable the legacy server's16 writes or enforce tenant
isolation, trusted approval, entitlement decisions, or token revocation. Those are
server contracts requiring separately owned implementation and adversarial tests.
Before execution is offered, test exact immutable approval, current-site binding,
authenticated destination readback, retries/partial failure/recovery, and the real
client consent/refresh/revocation journey. This task makes no backend change.

The lead owns independent review and the release decision. No new product scope,
secret request, server URL, tool name, audience, or publisher identity was introduced.

Completed worker-turn count:4. Successor:none; completed before20 turns.
