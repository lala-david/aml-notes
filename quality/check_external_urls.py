#!/usr/bin/env python3
"""
Scan markdown for external URLs, HEAD-check each to detect 404s.
Uses concurrent requests. Reports only non-2xx / non-3xx responses.
"""
from __future__ import annotations

import re
import sys
import concurrent.futures as cf
from pathlib import Path

try:
    import urllib.request as req
    import urllib.error
except ImportError:
    print("urllib not available", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")

EXCLUDE = {"node_modules", ".git", "mermaid-cache", "output", "print/days"}


def iter_md(root: Path):
    for p in root.rglob("*.md"):
        rel = p.relative_to(root).as_posix()
        parts = set(rel.split("/"))
        if parts & EXCLUDE:
            continue
        yield p


def check(url: str) -> tuple[str, int | str]:
    try:
        r = req.Request(url, method="HEAD",
                        headers={"User-Agent": "AML-Notes-LinkCheck/1.0"})
        with req.urlopen(r, timeout=12) as resp:
            return url, resp.status
    except urllib.error.HTTPError as e:
        # Some hosts reject HEAD — retry GET
        if e.code in (405, 403):
            try:
                r = req.Request(url, method="GET",
                                headers={"User-Agent": "AML-Notes-LinkCheck/1.0"})
                with req.urlopen(r, timeout=12) as resp:
                    return url, resp.status
            except Exception as e2:
                return url, str(e2)[:80]
        return url, e.code
    except Exception as e:
        return url, str(e)[:80]


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    urls: set[str] = set()
    sources: dict[str, list[str]] = {}
    for f in iter_md(ROOT):
        text = f.read_text(encoding="utf-8")
        for _, u in URL_RE.findall(text):
            urls.add(u)
            sources.setdefault(u, []).append(f.relative_to(ROOT).as_posix())

    print(f"Checking {len(urls)} unique external URLs...\n", flush=True)

    bad = []
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        results = ex.map(check, urls)
        for i, (url, status) in enumerate(results, 1):
            ok = isinstance(status, int) and 200 <= status < 400
            mark = "OK " if ok else "FAIL"
            print(f"[{mark}] [{status}] {url}", flush=True)
            if not ok:
                bad.append((url, status))

    print(f"\n\nSummary: total={len(urls)}, failing={len(bad)}\n")
    for url, status in bad:
        print(f"\n[{status}] {url}")
        for src in sources.get(url, []):
            print(f"   used in: {src}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
