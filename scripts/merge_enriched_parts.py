#!/usr/bin/env python3
"""Reconstitue data/tcga_enriched_p2.csv depuis les 3 parties."""
from pathlib import Path
parts = sorted(Path("data").glob("tcga_enriched_p2_part*.csv"))
assert len(parts) == 3, parts
lines = []
for i, p in enumerate(parts):
    rows = p.read_text().splitlines()
    if i == 0:
        lines.extend(rows)
    else:
        lines.extend(rows[1:])
out = Path("data/tcga_enriched_p2.csv")
out.write_text("\n".join(lines) + "\n")
print(f"Wrote {out} ({len(lines)} lines)")
