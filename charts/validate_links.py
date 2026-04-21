#!/usr/bin/env python3
"""
Scan all project markdown files for relative links (md/svg/png) and report
which targets don't exist on disk. Ignores http(s) external URLs and anchors.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {"node_modules", ".git", "print/days", "mermaid-cache", "charts/output"}

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def iter_md(root: Path):
    for p in root.rglob("*.md"):
        rel = p.relative_to(root).as_posix()
        parts = set(rel.split("/"))
        if parts & {"node_modules", ".git", "mermaid-cache", "output"}:
            continue
        if any(rel.startswith(x) for x in EXCLUDE_DIRS):
            continue
        yield p


def is_external(ref: str) -> bool:
    return ref.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    broken: list[tuple[str, str, str]] = []
    checked = 0

    for f in sorted(iter_md(ROOT)):
        text = f.read_text(encoding="utf-8")
        for label, ref in LINK_RE.findall(text):
            # strip trailing fragment
            bare = ref.split("#", 1)[0].split("?", 1)[0].strip()
            if not bare or is_external(ref):
                continue
            # backtick wrapped paths
            bare = bare.strip().strip("`")
            # resolve relative to file
            try:
                target = (f.parent / bare).resolve()
            except Exception:
                broken.append((f.relative_to(ROOT).as_posix(), ref, "resolve error"))
                continue
            checked += 1
            if not target.exists():
                broken.append((f.relative_to(ROOT).as_posix(), ref, label[:60]))

    print(f"Checked: {checked}   Broken: {len(broken)}\n")
    for src, ref, label in broken:
        print(f"[BROKEN] {src}")
        print(f"   link: {ref}")
        print(f"   text: {label}")
        print()
    return 0 if not broken else 1


if __name__ == "__main__":
    sys.exit(main())
