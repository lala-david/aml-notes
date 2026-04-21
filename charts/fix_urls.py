#!/usr/bin/env python3
"""
Replace known-broken URLs with working replacements across all project
markdown files. Safe to run multiple times.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE = {"node_modules", ".git", "mermaid-cache", "output"}

# Verified 2026-04: broken URL -> replacement
REPLACEMENTS = {
    # Steptoe blog restored to a path that resolves
    "https://www.steptoe.com/en/news-publications/blockchain-blog.html":
        "https://www.steptoe.com/en/news-publications",
    "https://www.steptoe.com/en/news-publications/blockchain-blog":
        "https://www.steptoe.com/en/news-publications",

    # Law Times — specific articles moved; use search/main
    "https://www.lawtimes.co.kr/news/articleView.html?idxno=214789":
        "https://m.lawtimes.co.kr",
    "https://www.lawtimes.co.kr/LawFirm-NewsLetter/214374":
        "https://m.lawtimes.co.kr",
    "https://www.lawtimes.co.krnews/articleView.html?idxno=214789":
        "https://m.lawtimes.co.kr",
    "https://www.lawtimes.co.krLawFirm-NewsLetter/214374":
        "https://m.lawtimes.co.kr",
    "https://www.lawtimes.co.kr/":
        "https://m.lawtimes.co.kr/",

    # law.go.kr specific lsiSeq — human search URLs work in browser
    "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=252787":
        "https://www.law.go.kr/법령/특정금융거래정보의보고및이용등에관한법률",
    "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=261099":
        "https://www.law.go.kr/법령/가상자산이용자보호등에관한법률",

    # DOJ restructured
    "https://www.justice.gov/criminal/criminal-vns/cryptocurrency":
        "https://www.justice.gov/criminal",

    # Big 4 pages shuffled — link to their homes
    "https://kpmg.com/xx/en/our-insights/financial-services.html":
        "https://kpmg.com/xx/en/home.html",
    "https://www2.deloitte.com/us/en/services/risk-financial-advisory.html":
        "https://www2.deloitte.com/us/en.html",
    "https://www.ey.com/en_us/financial-services/regulatory-and-public-policy":
        "https://www.ey.com/en_us",

    # GLEIF restructured
    "https://www.gleif.org/en/about-lei/introducing-the-legal-entity-identifier-lei":
        "https://www.gleif.org/en/about-lei/this-is-lei",

    # VerifyVASP docs moved
    "https://docs.verifyvasp.com/reference/ivms101/ivms101":
        "https://www.verifyvasp.com/",

    # FATF page paths corrected
    "https://www.fatf-gafi.org/en/topics/money-laundering.html":
        "https://www.fatf-gafi.org/en/topics/money-laundering",
    "https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Updated-Guidance-RBA-VA-VASP.html":
        "https://www.fatf-gafi.org/en/publications/Virtualassets/Updated-guidance-rba-virtual-assets.html",
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # Replace longer URLs first so prefix replacements don't mangle sub-paths
    ordered = sorted(REPLACEMENTS.items(), key=lambda kv: -len(kv[0]))

    changed_files = 0
    total_subs = 0
    for p in ROOT.rglob("*.md"):
        parts = set(p.relative_to(ROOT).as_posix().split("/"))
        if parts & EXCLUDE:
            continue
        orig = p.read_text(encoding="utf-8")
        new = orig
        local_subs = 0
        for old_url, new_url in ordered:
            count = new.count(old_url)
            if count:
                new = new.replace(old_url, new_url)
                local_subs += count
        if new != orig:
            p.write_text(new, encoding="utf-8")
            changed_files += 1
            total_subs += local_subs
            print(f"  {p.relative_to(ROOT).as_posix()}: {local_subs} subs")

    print(f"\nChanged {changed_files} files, {total_subs} URL replacements.")


if __name__ == "__main__":
    main()
