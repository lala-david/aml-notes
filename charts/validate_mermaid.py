#!/usr/bin/env python3
"""
Scan all markdown files for ```mermaid blocks, compile each via mmdc,
report which blocks fail to parse.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHARTS_DIR = Path(__file__).resolve().parent
MMDC = CHARTS_DIR / "node_modules" / ".bin" / (
    "mmdc.cmd" if os.name == "nt" else "mmdc"
)
CFG = CHARTS_DIR / "mermaid_config.json"
CACHE = CHARTS_DIR / "mermaid-cache"
CACHE.mkdir(parents=True, exist_ok=True)

BLOCK_RE = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)

EXCLUDE = {"node_modules", ".git", "print/days", "mermaid-cache"}


def iter_md(root: Path):
    for p in root.rglob("*.md"):
        rel = p.relative_to(root).as_posix()
        if any(rel.startswith(x) for x in EXCLUDE):
            continue
        yield p


def compile_block(source: str, tag: str) -> tuple[bool, str]:
    key = hashlib.sha1(source.encode("utf-8")).hexdigest()[:16]
    src = CACHE / f"{key}.mmd"
    out = CACHE / f"{key}.svg"
    src.write_text(source, encoding="utf-8")
    try:
        r = subprocess.run(
            [str(MMDC), "-i", str(src), "-o", str(out), "-c", str(CFG), "-b", "transparent"],
            capture_output=True, timeout=60, text=True, encoding="utf-8",
        )
        if r.returncode != 0:
            return False, (r.stderr or r.stdout).strip()[:800]
        return True, ""
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"
    finally:
        src.unlink(missing_ok=True)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    files = sorted(iter_md(ROOT))
    bad = []
    ok_count = 0

    for f in files:
        text = f.read_text(encoding="utf-8")
        blocks = BLOCK_RE.findall(text)
        for idx, b in enumerate(blocks):
            tag = f"{f.relative_to(ROOT).as_posix()}#mermaid-{idx+1}"
            ok, err = compile_block(b, tag)
            if ok:
                ok_count += 1
                continue
            bad.append((tag, err, b))
            print(f"\n[FAIL] {tag}")
            # Short error summary
            first_line = err.splitlines()[0] if err else "(no stderr)"
            print(f"   {first_line[:180]}")

    print(f"\n\nSummary: OK={ok_count}, FAIL={len(bad)}")
    if bad:
        print("\n--- Failed blocks (source for manual fix) ---\n")
        for tag, err, block in bad:
            print(f"## {tag}")
            print("```mermaid")
            print(block)
            print("```")
            print()
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
