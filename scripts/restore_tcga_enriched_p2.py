#!/usr/bin/env python3
"""Reconstruit data/tcga_enriched_p2.csv
SHA256: 6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd
"""
import base64, gzip, hashlib
from pathlib import Path

def load_b64():
    p = Path("data/tcga_enriched_p2.csv.gz.b64")
    if p.exists():
        return p.read_text().strip()
    a = Path("data/tcga_enriched_p2.csv.gz.b64.a").read_text().strip()
    b = Path("data/tcga_enriched_p2.csv.gz.b64.b").read_text().strip()
    return a + b

def main():
    raw = gzip.decompress(base64.b64decode(load_b64()))
    h = hashlib.sha256(raw).hexdigest()
    expected = "6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd"
    assert h == expected, f"got {h}"
    out = Path("data/tcga_enriched_p2.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(raw)
    print(f"OK {out} bytes={len(raw)} sha256={h}")

if __name__ == "__main__":
    main()
