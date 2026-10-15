#!/usr/bin/env bash
# Why: one gate, run the same way locally and in CI, so a green PR means the package passes review checks.
set -euo pipefail
cd "$(dirname "$0")/.."
status=0
if command -v claude >/dev/null 2>&1; then
  echo "== claude plugin validate --strict ."
  claude plugin validate --strict . || status=1
  echo "== claude plugin validate --strict .claude-plugin/plugin.json"
  claude plugin validate --strict .claude-plugin/plugin.json || status=1
  echo "== claude plugin validate --strict skills"
  claude plugin validate --strict skills || status=1
else
  echo "== claude CLI not found; skipping the CLI validator (repo checks still run)"
fi
echo "== repo checks"
python3 scripts/check_package.py . || status=1
exit $status
