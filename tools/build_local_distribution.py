#!/usr/bin/env python3
"""Build the existing Claude package from explicit files, without developer context."""
from hashlib import sha256
import json
from pathlib import Path
import shutil
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
ALLOWLIST = (
    '.claude-plugin/plugin.json', '.mcp.json', 'LICENSE',
    'skills/seo-content-plan/SKILL.md',
    'skills/publish-to-wordpress/SKILL.md',
    'skills/lead-triage/SKILL.md',
    'skills/seo-workspace-review/SKILL.md',
)


def payloads(source):
    source = source.resolve()
    result = {}
    for relative in (*ALLOWLIST, '.claude-plugin/marketplace.json'):
        path = source / relative
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(source):
            raise ValueError(f'Expected contained regular source file: {relative}')
        result[relative] = path.read_bytes()
    plugin = json.loads(result['.claude-plugin/plugin.json'])
    marketplace = json.loads(result['.claude-plugin/marketplace.json'])
    assert plugin['name'] == marketplace['name'] == 'advisorseo'
    assert len(marketplace['plugins']) == 1
    entry = marketplace['plugins'][0]
    assert entry['name'] == plugin['name']
    assert entry['version'] == plugin['version']
    assert entry['source'] == './'
    assert json.loads(result['.mcp.json']) == {
        'advisorseo': {'type': 'http', 'url': 'https://mcp.advisorseo.ai/mcp'}
    }, 'Existing connector identity, transport, and endpoint must remain unchanged'
    entry['source'] = './plugins/advisorseo'
    result['.claude-plugin/marketplace.json'] = (json.dumps(marketplace, indent=2, ensure_ascii=False) + '\n').encode()
    return result


def archive_bytes(files):
    import io
    buf = io.BytesIO()
    with ZipFile(buf, 'w', compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(files.items()):
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return buf.getvalue()


def build(source=ROOT, output=DIST):
    files = payloads(source)
    output.mkdir(parents=True, exist_ok=True)
    if output.is_symlink():
        raise ValueError('Distribution output must not be a symlink')
    artifact = output / 'local-marketplace'
    if artifact.is_symlink():
        raise ValueError('Artifact output must not be a symlink')
    marketplace_files = {
        '.claude-plugin/marketplace.json': files['.claude-plugin/marketplace.json'],
        **{f'plugins/advisorseo/{name}': files[name] for name in ALLOWLIST},
    }
    with tempfile.TemporaryDirectory(prefix='.local-build-', dir=output) as temp:
        staged = Path(temp) / 'local-marketplace'
        for name, data in marketplace_files.items():
            path = staged / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        if artifact.exists():
            shutil.rmtree(artifact)
        staged.rename(artifact)
    archives = {
        'advisorseo-local-draft.zip': archive_bytes({f'advisorseo-marketplace/{name}': data for name, data in marketplace_files.items()}),
        'advisorseo-plugin-draft.zip': archive_bytes({f'advisorseo/{name}': files[name] for name in ALLOWLIST}),
    }
    for name, data in archives.items():
        path = output / name
        if path.is_symlink():
            raise ValueError(f'Archive output must not be a symlink: {name}')
        path.write_bytes(data)
    receipt = {
        'status': 'local draft; not installed or released',
        'plugin_name': 'advisorseo',
        'version': json.loads(files['.claude-plugin/plugin.json'])['version'],
        'plugin_file_count': len(ALLOWLIST),
        'skill_count': sum(name.startswith('skills/') for name in ALLOWLIST),
        'marketplace_file_count': len(marketplace_files),
        'plugin_allowlist': list(ALLOWLIST),
        'source_sha256': {name: sha256((source / name).read_bytes()).hexdigest() for name in (*ALLOWLIST, '.claude-plugin/marketplace.json')},
        'artifact_sha256': {name: sha256(data).hexdigest() for name, data in sorted(marketplace_files.items())},
        'archive_sha256': {name: sha256(data).hexdigest() for name, data in archives.items()},
    }
    (output / 'build-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return receipt


if __name__ == '__main__':
    receipt = build()
    print(f"Built local AdvisorSEO {receipt['version']}: {receipt['plugin_file_count']} plugin files, "
          f"{receipt['skill_count']} skills and separate marketplace; no install")
