#!/usr/bin/env python3
"""Reconstruit data/tcga_enriched_p2.csv depuis data/b64_chunks/
SHA256: 6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd
"""
import base64, gzip, hashlib
from pathlib import Path

def main():
    parts = sorted(Path("data/b64_chunks").glob("chunk_*.txt"))
    assert parts, "no chunks"
    b64 = "".join(p.read_text().strip() for p in parts)
    raw = gzip.decompress(base64.b64decode(b64))
    h = hashlib.sha256(raw).hexdigest()
    expected = "6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd"
    assert h == expected, f"got {h}"
    out = Path("data/tcga_enriched_p2.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(raw)
    print(f"OK {out} bytes={len(raw)} sha256={h} from {len(parts)} chunks")

if __name__ == "__main__":
    main()
