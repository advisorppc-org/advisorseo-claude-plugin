#!/usr/bin/env python3
"""Check exact package contents, reproducibility, and both Claude manifests offline."""
from hashlib import sha256
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from zipfile import ZipFile

from build_local_distribution import ALLOWLIST, DIST, ROOT, build, payloads

OUT = ROOT / 'evidence/directory-skill-20261003'


def main(*, package_only=False, managed_sandbox=False):
    OUT.mkdir(parents=True, exist_ok=True)
    receipt = build()
    first = {name: (DIST / name).read_bytes() for name in receipt['archive_sha256']}
    again = build()
    assert again == receipt and all((DIST / name).read_bytes() == data for name, data in first.items())
    artifact = DIST / 'local-marketplace'
    expected = {'.claude-plugin/marketplace.json', *(f'plugins/advisorseo/{name}' for name in ALLOWLIST)}
    actual = {str(p.relative_to(artifact)) for p in artifact.rglob('*') if p.is_file()}
    assert actual == expected
    assert receipt['plugin_file_count'] == len(ALLOWLIST) == 7
    assert receipt['skill_count'] == 4
    assert receipt['marketplace_file_count'] == len(expected) == 8
    assert not any(p.is_symlink() for p in artifact.rglob('*'))
    for name, digest in receipt['artifact_sha256'].items():
        assert sha256((artifact / name).read_bytes()).hexdigest() == digest, name
    for name in ALLOWLIST:
        assert (artifact / 'plugins/advisorseo' / name).read_bytes() == (ROOT / name).read_bytes(), name
    expected_marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    expected_marketplace['plugins'][0]['source'] = './plugins/advisorseo'
    assert json.loads((artifact / '.claude-plugin/marketplace.json').read_text()) == expected_marketplace
    # Missing files and symlinks are not silently followed; unrelated context stays excluded.
    with tempfile.TemporaryDirectory(prefix='advisorseo-package-fixture-') as temp:
        fixture = Path(temp)
        for name in (*ALLOWLIST, '.claude-plugin/marketplace.json'):
            target = fixture / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        (fixture / 'CLAUDE.md').write_text('Development context must not be shipped.\n')
        assert set(payloads(fixture)) == {*ALLOWLIST, '.claude-plugin/marketplace.json'}
        (fixture / 'LICENSE').unlink()
        try:
            payloads(fixture)
            raise AssertionError('Missing required file accepted')
        except ValueError:
            pass
        (fixture / 'LICENSE').symlink_to(ROOT / 'LICENSE')
        try:
            payloads(fixture)
            raise AssertionError('Source symlink accepted')
        except ValueError:
            pass
    with tempfile.TemporaryDirectory(prefix='advisorseo-plugin-validation-') as temp:
        temp = Path(temp)
        for archive, expected_members in (
            ('advisorseo-local-draft.zip', {f'advisorseo-marketplace/{name}' for name in expected}),
            ('advisorseo-plugin-draft.zip', {f'advisorseo/{name}' for name in ALLOWLIST}),
        ):
            with ZipFile(DIST / archive) as zipped:
                assert set(zipped.namelist()) == expected_members
                zipped.extractall(temp / archive)
        cli = shutil.which('claude') if not package_only else None
        assert package_only or cli, 'Installed Claude CLI is required; no download fallback'
        env = {'PATH': os.environ['PATH'], 'CLAUDE_CONFIG_DIR': str(temp / 'config'),
               'DISABLE_AUTOUPDATER': '1', 'CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC': '1'}
        prefix = [] if managed_sandbox else ['unshare', '-Urn']
        version = None if package_only else subprocess.run([*prefix, cli, '--version'], env=env, text=True, capture_output=True, check=True).stdout.strip()
        targets = [
            ('source-marketplace', ROOT / '.claude-plugin/marketplace.json', 0),
            ('source-plugin-preserved-warning', ROOT / '.claude-plugin/plugin.json', 1),
            ('artifact-marketplace', artifact / '.claude-plugin/marketplace.json', 0),
            ('artifact-plugin-manifest', artifact / 'plugins/advisorseo/.claude-plugin/plugin.json', 0),
            ('artifact-plugin-directory', artifact / 'plugins/advisorseo', 0),
            ('artifact-skills', artifact / 'plugins/advisorseo/skills', 0),
            ('unpacked-marketplace', temp / 'advisorseo-local-draft.zip/advisorseo-marketplace/.claude-plugin/marketplace.json', 0),
            ('unpacked-marketplace-plugin', temp / 'advisorseo-local-draft.zip/advisorseo-marketplace/plugins/advisorseo/.claude-plugin/plugin.json', 0),
            ('unpacked-plugin', temp / 'advisorseo-plugin-draft.zip/advisorseo/.claude-plugin/plugin.json', 0),
        ]
        validations = []
        def portable_evidence(value):
            return value.replace(str(ROOT), '<source>').replace(str(temp), '<validation>')

        for name, path, expected_exit in ([] if package_only else targets):
            run = subprocess.run([*prefix, cli, 'plugin', 'validate', '--strict', '--json', str(path)],
                                 env=env, text=True, capture_output=True)
            (OUT / f'{name}.json').write_text(portable_evidence(run.stdout))
            (OUT / f'{name}.stderr.txt').write_text(portable_evidence(run.stderr))
            report = json.loads(run.stdout)
            assert run.returncode == expected_exit, (name, run.returncode, run.stdout, run.stderr)
            if expected_exit == 0:
                assert report['success'] is True
            else:
                assert report['success'] is False
                warnings = [w['message'] for entry in report['contents'] for w in entry['warnings']]
                errors = [e for entry in [report['manifest'], *report['contents']] for e in entry['errors']]
                assert not errors and warnings == ['CLAUDE.md at the plugin root is not loaded as project context. To ship context with your plugin, use a skill (skills/<name>/SKILL.md) instead.']
            validations.append({'name': name, 'actual_exit': run.returncode, 'expected_exit': expected_exit})
            print(f"{name}: exit {run.returncode}" + (' (preserved source warning)' if expected_exit else ' PASS'))
    for name in receipt['archive_sha256']:
        shutil.copyfile(DIST / name, OUT / name)
    shutil.copyfile(DIST / 'build-receipt.json', OUT / 'build-receipt.json')
    summary = {'status': 'LOCAL PACKAGE CHECKS PASS', 'cli_version': version,
               'network_isolated': not package_only and not managed_sandbox,
               'managed_network_restricted': not package_only and managed_sandbox,
               'temporary_config': not package_only, 'installed': False,
               'plugin_file_count': receipt['plugin_file_count'],
               'skill_count': receipt['skill_count'],
               'marketplace_file_count': receipt['marketplace_file_count'],
               'validator_run_count': len(validations),
               'validator_requested': not package_only,
               'reproducible_archives': True, 'exact_allowlist': True,
               'missing_file_rejected': True, 'source_symlink_rejected': True,
               'validations': validations}
    (OUT / 'validation-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print('LOCAL PACKAGE CHECKS PASS')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    options = parser.add_mutually_exclusive_group()
    options.add_argument('--package-only', action='store_true', help='Check package contents without invoking Claude.')
    options.add_argument('--managed-sandbox', action='store_true', help='Use existing managed network restrictions rather than unshare.')
    args = parser.parse_args()
    main(package_only=args.package_only, managed_sandbox=args.managed_sandbox)
