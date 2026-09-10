#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parent
required = ['approved-campaign-input.md', 'script.md', 'storyboard.md', 'asset-rights-register.csv', 'generation-plan.md', 'qc-report.md', 'security-boundary-test-matrix.md', 'human-release-decision.md']
missing = [name for name in required if not (root / name).exists()]
if missing:
    raise SystemExit("FAIL missing: " + ", ".join(missing))
for name in required:
    if (root / name).is_file() and (root / name).stat().st_size == 0:
        raise SystemExit("FAIL empty: " + name)
print("PASS - lab bundle and evidence template are complete")
