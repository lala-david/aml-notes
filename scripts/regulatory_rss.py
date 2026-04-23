#!/usr/bin/env python3
"""
Regulatory RSS Aggregator
주요 AML 규제기관의 RSS 피드를 수집해 최근 변화를 JSON·Markdown으로 출력.

Usage:
    python scripts/regulatory_rss.py [--days N] [--output-dir DIR] [--verbose]

Requires:
    pip install -r scripts/requirements.txt
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import feedparser  # type: ignore
except ImportError:
    print(
        "[ERROR] feedparser 미설치. `pip install -r scripts/requirements.txt` 후 재실행.",
        file=sys.stderr,
    )
    sys.exit(2)


# 실제 공개 RSS 피드 (2026-04 기준)
# 일부 기관 (한국 FSC/KoFIU/FSS 등) 은 공식 RSS 미제공 → 웹 스크레이핑은 별도 이슈
FEEDS: dict[str, str] = {
    # 국제
    "FATF": "https://www.fatf-gafi.org/en/publications.rss",
    "BIS": "https://www.bis.org/doclist/alldeliverables.rss",
    # 미국
    "SEC_Press": "https://www.sec.gov/news/pressreleases.rss",
    "FinCEN_News": "https://www.fincen.gov/news/news-releases/feed",
    "OFAC_Recent": "https://ofac.treasury.gov/media/rss/recent-actions",
    "DOJ_News": "https://www.justice.gov/news/rss",
    "CFTC_Press": "https://www.cftc.gov/PressRoom/PressReleases/feed",
    # EU
    "ESMA_News": "https://www.esma.europa.eu/news.rss",
    # 아시아
    "MAS_News": "https://www.mas.gov.sg/news.rss",
    "HK_SFC": "https://apps.sfc.hk/edistributionWeb/gateway/EN/news-and-announcements/news/feed/",
    # 업계 (1차 분석 · 사건 신속 대응)
    "Chainalysis_Blog": "https://www.chainalysis.com/blog/feed/",
    "Elliptic_Blog": "https://www.elliptic.co/blog/rss.xml",
    "TRM_Blog": "https://www.trmlabs.com/feed",
}

# 제목·요약 매칭 키워드 (영어·한국어 혼합)
KEYWORDS: list[str] = [
    # 영어
    "money laundering", "aml", "cft", "terrorism financing",
    "crypto", "cryptocurrency", "virtual asset", "vasp",
    "sanctions", "ofac", "sdn", "fatf", "travel rule",
    "stablecoin", "defi", "mixer", "tornado", "privacy coin",
    "kyc", "kyt", "suspicious activity", "sar", "str",
    "enforcement", "fine", "settlement", "consent order",
    "mica", "amla", "fincen",
    # 한국어
    "자금세탁", "가상자산", "특금법", "이용자보호법", "제재",
    "금융정보분석원", "트래블룰", "가상자산사업자",
]


def matches_keyword(entry) -> bool:
    """제목 또는 요약에 키워드가 하나라도 포함되면 True."""
    text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
    return any(kw.lower() in text for kw in KEYWORDS)


def parse_date(entry) -> datetime:
    """published / updated 를 UTC datetime 으로. 둘 다 없으면 now."""
    for field in ("published_parsed", "updated_parsed"):
        val = entry.get(field)
        if val:
            try:
                return datetime(*val[:6], tzinfo=timezone.utc)
            except (TypeError, ValueError):
                continue
    return datetime.now(timezone.utc)


def fetch_source(name: str, url: str, cutoff: datetime, verbose: bool = False) -> list[dict]:
    """한 피드에서 cutoff 이후 · 키워드 매칭 항목 수집. 실패해도 빈 리스트 반환."""
    items: list[dict] = []
    try:
        feed = feedparser.parse(
            url,
            request_headers={"User-Agent": "aml-notes-regulatory-watch/1.0"},
        )
        if feed.bozo and not feed.entries:
            print(
                f"  [WARN] {name}: parse error ({getattr(feed, 'bozo_exception', 'unknown')})",
                file=sys.stderr,
            )
            return items
        for entry in feed.entries:
            pub = parse_date(entry)
            if pub < cutoff:
                continue
            if not matches_keyword(entry):
                continue
            items.append({
                "source": name,
                "title": (entry.get("title", "") or "").strip(),
                "url": entry.get("link", ""),
                "date": pub.isoformat(),
                "summary": (entry.get("summary", "") or "").strip()[:500],
            })
    except Exception as e:  # noqa: BLE001 — 피드 하나가 전체를 중단시키지 않도록
        print(f"  [ERROR] {name}: {e}", file=sys.stderr)
    return items


def write_json(path: Path, items: list[dict], window_days: int) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "window_days": window_days,
        "total": len(items),
        "items": items,
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def write_markdown(path: Path, items: list[dict], window_days: int) -> None:
    with path.open("w", encoding="utf-8") as f:
        f.write(f"# Regulatory Changes (last {window_days} days)\n\n")
        f.write(f"Generated: `{datetime.now(timezone.utc).isoformat()}`\n\n")
        f.write(f"Total items: **{len(items)}**\n\n")
        if not items:
            f.write("_No significant regulatory changes detected in the window._\n")
            return
        # 출처별 그룹핑
        by_source: dict[str, list[dict]] = {}
        for it in items:
            by_source.setdefault(it["source"], []).append(it)
        for src in sorted(by_source):
            f.write(f"## {src} ({len(by_source[src])})\n\n")
            for it in by_source[src]:
                f.write(
                    f"- [{it['title']}]({it['url']}) — `{it['date'][:10]}`\n"
                )
            f.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=7, help="Last N days (default 7)")
    parser.add_argument("--output-dir", default=".", help="Output directory (default cwd)")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    all_items: list[dict] = []
    for name, url in FEEDS.items():
        if args.verbose:
            print(f"Fetching {name}...", file=sys.stderr)
        items = fetch_source(name, url, cutoff, verbose=args.verbose)
        all_items.extend(items)
        if args.verbose:
            print(f"  -> {len(items)} matching items", file=sys.stderr)

    all_items.sort(key=lambda x: x["date"], reverse=True)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "regulatory-changes.json"
    md_path = output_dir / "regulatory-changes.md"
    write_json(json_path, all_items, args.days)
    write_markdown(md_path, all_items, args.days)

    print(f"JSON:     {json_path} ({len(all_items)} items)")
    print(f"Markdown: {md_path}")

    # exit code 1 = 신규 항목 있음 (CI 에서 이슈 생성 트리거용)
    return 1 if all_items else 0


if __name__ == "__main__":
    sys.exit(main())
