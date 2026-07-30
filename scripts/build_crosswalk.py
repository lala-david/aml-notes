#!/usr/bin/env python3
"""
관할 크로스워크 생성기

추상 의무(OBL) 하나에 걸린 각국 조문(PROV)의 IMPOSES 한정자를 모아
관할 비교표를 생성한다. 손으로 유지하던 비교표를 질의 결과로 대체하는 것이 목적이다.

설계 근거: docs/ontology/01-semantic-layer.md §2.1

Usage:
    python scripts/build_crosswalk.py                    # 전체 의무
    python scripts/build_crosswalk.py --obl OBL:x-travel-rule-originator
    python scripts/build_crosswalk.py --as-of 2024-12-30 # 시점 질의
    python scripts/build_crosswalk.py --stdout           # 파일 대신 표준출력
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("[ERROR] PyYAML 미설치. pip install -r quality/requirements.txt", file=sys.stderr)
    sys.exit(2)


def parse_date(value) -> date | None:
    if not isinstance(value, str):
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def load_nodes(kb_root: Path) -> dict[str, dict]:
    """노드를 적재한다.

    ⚠️ rglob 은 파일시스템 순회 순서를 따르므로 OS 마다 다르다.
    정렬하지 않으면 파생물이 비결정적이 되어 재현성 검사가 깨진다.
    """
    nodes: dict[str, dict] = {}
    for base in (kb_root / "entities", kb_root / "sources"):
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and data.get("id"):
                nodes[data["id"]] = data
    return nodes


def edge_active_at(edge: dict, at: date | None) -> bool:
    """as_of 시점에 이 엣지가 유효한가."""
    if at is None:
        return True
    vf = parse_date(edge.get("valid_from"))
    vt = parse_date(edge.get("valid_to"))
    if vf and at < vf:
        return False
    if vt and at >= vt:
        return False
    return True


def collect(nodes: dict[str, dict], at: date | None) -> dict[str, list[dict]]:
    """의무별로 그것을 부과하는 조문 목록을 모은다."""
    by_obl: dict[str, list[dict]] = defaultdict(list)
    for nid, node in nodes.items():
        if node.get("type") != "PROV":
            continue
        for edge in node.get("edges") or []:
            if edge.get("predicate") != "IMPOSES":
                continue
            if not edge_active_at(edge, at):
                continue
            q = edge.get("qualifiers") or {}
            confs = [
                c for ev in (edge.get("evidence") or [])
                if isinstance(ev, dict) and isinstance(c := ev.get("confidence"), str)
            ]
            by_obl[edge["to"]].append({
                "prov": nid,
                "prov_label": (node.get("label") or {}).get("short")
                              or (node.get("label") or {}).get("ko", nid),
                "reg": node.get("parent_reg", ""),
                "citation": node.get("citation_path", ""),
                "namespace": nid.split(":", 1)[1].split("-", 1)[0],
                "threshold": q.get("threshold"),
                "currency": q.get("currency"),
                "grace_until": q.get("grace_until"),
                "valid_from": edge.get("valid_from"),
                "valid_to": edge.get("valid_to"),
                "confidence": min(confs) if confs else "?",
            })
    return by_obl


NAMESPACE_LABEL = {
    "kr": "🇰🇷 한국", "us": "🇺🇸 미국", "eu": "🇪🇺 EU", "gb": "🇬🇧 영국",
    "jp": "🇯🇵 일본", "sg": "🇸🇬 싱가포르", "hk": "🇭🇰 홍콩", "ae": "🇦🇪 UAE",
    "au": "🇦🇺 호주", "intl": "🌐 국제기준", "x": "— 무국적",
}


def render(obl_id: str, obl: dict, rows: list[dict], at: date | None) -> str:
    label = obl.get("label") or {}
    lines = [
        f"# 관할 크로스워크 — {label.get('ko', obl_id)}",
        "",
        f"> 🤖 자동 생성 (`python scripts/build_crosswalk.py`). 직접 편집하지 마세요.",
        f"> 의무 노드: `{obl_id}`"
        + (f" · 기준 시점: **{at.isoformat()}**" if at else " · 기준 시점: 전체"),
        "",
    ]
    if obl.get("summary"):
        lines += ["> " + " ".join(str(obl["summary"]).split()), ""]

    if not rows:
        lines += ["_이 의무를 부과하는 조문이 등재되지 않았습니다._", ""]
        return "\n".join(lines)

    lines += [
        "| 관할 | 근거 조문 | 임계값 | 통화 | 유효기간 | 확신도 |",
        "|---|---|---:|---|---|---|",
    ]
    # ⚠️ 정렬 키에 prov 를 포함해야 한다. 같은 관할에 조문이 둘 이상이면
    #    namespace 만으로는 동률이 되고, 안정 정렬 특성상 입력 순서가 그대로 남아
    #    OS 별로 결과가 갈린다 (CI 재현성 검사가 이를 잡았다).
    for r in sorted(rows, key=lambda x: (x["namespace"] != "intl", x["namespace"], x["prov"])):
        jur = NAMESPACE_LABEL.get(r["namespace"], r["namespace"])
        thr = f"{r['threshold']:,}" if isinstance(r["threshold"], (int, float)) else "임계값 없음"
        cur = r["currency"] or "—"
        period = f"{r['valid_from'] or '?'} ~ {r['valid_to'] or '현재'}"
        lines.append(
            f"| {jur} | `{r['citation'] or r['prov']}` | {thr} | {cur} | {period} | {r['confidence']} |"
        )

    lines += ["", "## 등재된 조문", ""]
    for r in sorted(rows, key=lambda x: x["prov"]):
        lines.append(f"- `{r['prov']}` — {r['prov_label']} (소속 규범 `{r['reg']}`)")

    missing = [ns for ns in ("us", "eu", "gb", "jp", "sg", "hk", "au")
               if ns not in {r["namespace"] for r in rows}]
    if missing:
        lines += [
            "",
            "## 미등재 관할",
            "",
            "다음 관할은 리서치에서 값이 확인되었으나 아직 PROV 노드가 생성되지 않았습니다.",
            "",
            "- " + ", ".join(NAMESPACE_LABEL.get(m, m) for m in missing),
        ]
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kb-root", default="kb")
    ap.add_argument("--out-dir", default="kb/derived/crosswalk")
    ap.add_argument("--obl", default=None, help="특정 의무만")
    ap.add_argument("--as-of", default=None, help="시점 질의 (YYYY-MM-DD)")
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")  # type: ignore[union-attr]

    kb_root = Path(args.kb_root)
    at = parse_date(args.as_of) if args.as_of else None
    if args.as_of and at is None:
        print(f"[ERROR] --as-of 형식 오류: {args.as_of}", file=sys.stderr)
        return 2

    nodes = load_nodes(kb_root)
    by_obl = collect(nodes, at)

    targets = [args.obl] if args.obl else sorted(
        nid for nid, n in nodes.items() if n.get("type") == "OBL"
    )
    if not targets:
        print("[WARN] OBL 노드가 없습니다.", file=sys.stderr)
        return 0

    out_dir = Path(args.out_dir)
    written = 0
    for obl_id in targets:
        obl = nodes.get(obl_id)
        if obl is None:
            print(f"[WARN] 의무 노드 없음: {obl_id}", file=sys.stderr)
            continue
        text = render(obl_id, obl, by_obl.get(obl_id, []), at)
        if args.stdout:
            print(text)
        else:
            out_dir.mkdir(parents=True, exist_ok=True)
            slug = obl_id.split(":", 1)[1]
            (out_dir / f"{slug}.md").write_text(text, encoding="utf-8")
            written += 1

    if not args.stdout:
        print(f"크로스워크 {written}건 생성 → {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
