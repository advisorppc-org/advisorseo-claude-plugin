#!/usr/bin/env python3
"""Why: the split only protects against overfitting if nobody can quietly move a case, so this recomputes it from the rule."""
import hashlib
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent / "evals"
cases = sorted(p.parent.name for p in root.glob("*/prompt.md"))
held = [c for c in cases if int(hashlib.sha256(c.encode()).hexdigest()[:8], 16) % 100 < 30]
text = (root / "SPLIT.md").read_text()
listed_held = re.findall(r"^- (\S+)$", text.split("## Held-out")[1].split("## Train")[0], re.M)
listed_train = re.findall(r"^- (\S+)$", text.split("## Train")[1], re.M)
train = [c for c in cases if c not in held]
if listed_held != held or listed_train != train:
    print("split drifted from the rule in evals/SPLIT.md")
    sys.exit(1)
print(f"split ok: {len(held)} held-out, {len(train)} train")
