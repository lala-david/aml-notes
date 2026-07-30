"""그래프 질의 — as_of · crosswalk · lineage · neighbors."""
from __future__ import annotations

from datetime import date

from .graph import Graph, Node, parse_date

# 위임·이행 계보를 거슬러 올라갈 때 따라가는 술어
LINEAGE_UP = ("DELEGATES_TO", "IMPLEMENTS", "PART_OF", "IMPOSES")

NS_LABEL = {
    "kr": "🇰🇷 한국", "us": "🇺🇸 미국", "eu": "🇪🇺 EU", "gb": "🇬🇧 영국",
    "jp": "🇯🇵 일본", "sg": "🇸🇬 싱가포르", "hk": "🇭🇰 홍콩", "ae": "🇦🇪 UAE",
    "au": "🇦🇺 호주", "intl": "🌐 국제기준", "x": "— 무국적",
}


def node_brief(g: Graph, node_id: str) -> dict | None:
    n = g.get(node_id)
    if n is None:
        return None
    return {
        "id": n.id,
        "type": n.type,
        "layer": n.layer,
        "title": n.title,
        "label": n.label,
        "status": n.raw.get("status", "active"),
    }


def _min_confidence(evidence: list) -> str | None:
    """엣지에 붙은 증거 중 가장 낮은 확신도. A<B<C<D 이므로 max 가 최저 신뢰."""
    vals: list[str] = []
    for e in evidence:
        if isinstance(e, dict):
            c = e.get("confidence")
            if isinstance(c, str):
                vals.append(c)
    return max(vals) if vals else None


def node_detail(g: Graph, node_id: str, at: date | None = None) -> dict | None:
    n = g.get(node_id)
    if n is None:
        return None

    def render(edges, direction: str) -> list[dict]:
        out = []
        for e in edges:
            if not e.active_at(at):
                continue
            other = e.target if direction == "out" else e.source
            out.append({
                "predicate": e.predicate,
                "direction": direction,
                "node": node_brief(g, other) or {"id": other, "missing": True},
                "qualifiers": e.qualifiers,
                "valid_from": e.valid_from,
                "valid_to": e.valid_to,
                "confidence": _min_confidence(e.evidence),
                "evidence": e.evidence,
            })
        return out

    body = {k: v for k, v in n.raw.items() if k not in ("edges",)}
    return {
        **body,
        "title": n.title,
        "path": n.path,
        "edges_out": render(n.out, "out"),
        "edges_in": render(n.inc, "in"),
        "facts": [f for f in g.facts if f.get("subject") == node_id],
        "states": [s for s in g.states if s.get("subject") == node_id],
    }


def neighbors(g: Graph, node_id: str, depth: int = 1, at: date | None = None) -> dict:
    """이웃 그래프 — 프론트 시각화용 node/link 배열."""
    seen: set[str] = set()
    links: list[dict] = []
    frontier = {node_id}
    for _ in range(max(1, min(depth, 3))):
        nxt: set[str] = set()
        for nid in frontier:
            if nid in seen:
                continue
            seen.add(nid)
            n = g.get(nid)
            if n is None:
                continue
            for e in list(n.out) + list(n.inc):
                if not e.active_at(at):
                    continue
                links.append({"source": e.source, "target": e.target, "predicate": e.predicate})
                nxt.add(e.target if e.source == nid else e.source)
        frontier = nxt - seen
    seen |= frontier
    return {
        "root": node_id,
        "nodes": [b for b in (node_brief(g, i) for i in sorted(seen)) if b],
        "links": links,
    }


def crosswalk(g: Graph, obl_id: str, at: date | None = None) -> dict | None:
    """추상 의무 하나에 걸린 관할별 조문 비교.

    손으로 유지하던 비교표를 질의 결과로 대체한다.
    """
    obl = g.get(obl_id)
    if obl is None or obl.type != "OBL":
        return None

    rows: list[dict] = []
    for e in obl.inc:
        if e.predicate != "IMPOSES" or not e.active_at(at):
            continue
        prov = g.get(e.source)
        if prov is None:
            continue
        ns = prov.id.split(":", 1)[1].split("-", 1)[0]
        q = e.qualifiers or {}
        rows.append({
            "provision": node_brief(g, prov.id),
            "citation": prov.raw.get("citation_path") or prov.id,
            "regulation": node_brief(g, prov.raw.get("parent_reg", "")) if prov.raw.get("parent_reg") else None,
            "namespace": ns,
            "jurisdiction_label": NS_LABEL.get(ns, ns),
            "threshold": q.get("threshold"),
            "currency": q.get("currency"),
            "scope_note": q.get("scope_note"),
            "valid_from": e.valid_from,
            "valid_to": e.valid_to,
            "confidence": _min_confidence(e.evidence),
            "evidence": e.evidence,
        })

    rows.sort(key=lambda r: (r["namespace"] != "intl", r["namespace"], r["provision"]["id"]))
    present = {r["namespace"] for r in rows}
    return {
        "obligation": {**(node_brief(g, obl_id) or {}), "summary": obl.raw.get("summary")},
        "as_of": at.isoformat() if at else None,
        "rows": rows,
        "missing_jurisdictions": [
            {"namespace": ns, "label": NS_LABEL[ns]}
            for ns in ("us", "eu", "gb", "jp", "sg", "hk", "au") if ns not in present
        ],
    }


def lineage(g: Graph, node_id: str, at: date | None = None, max_depth: int = 6) -> dict | None:
    """조문에서 출발해 위임·이행 관계를 거슬러 올라간 경로."""
    start = g.get(node_id)
    if start is None:
        return None

    paths: list[list[dict]] = []

    def walk(nid: str, trail: list[dict], seen: set[str]) -> None:
        if len(trail) > max_depth:
            paths.append(trail)
            return
        n = g.get(nid)
        steps = [
            e for e in (n.out if n else [])
            if e.predicate in LINEAGE_UP and e.active_at(at) and e.target not in seen
        ]
        if not steps:
            if trail:
                paths.append(trail)
            return
        for e in steps:
            walk(e.target, trail + [{
                "predicate": e.predicate,
                "from": node_brief(g, e.source),
                "to": node_brief(g, e.target),
                "qualifiers": e.qualifiers,
                "confidence": _min_confidence(e.evidence),
            }], seen | {e.target})

    walk(node_id, [], {node_id})
    return {
        "root": {**(node_brief(g, node_id) or {}), "summary": start.raw.get("summary")},
        "as_of": at.isoformat() if at else None,
        "paths": paths,
    }


def search(
    g: Graph,
    q: str | None = None,
    node_type: str | None = None,
    jurisdiction: str | None = None,
    tag: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> dict:
    items: list[Node] = []
    needle = (q or "").lower().strip()
    for n in g.nodes.values():
        if node_type and n.type != node_type:
            continue
        if tag and tag not in (n.raw.get("tags") or []):
            continue
        if jurisdiction and g.jurisdiction_of(n) != jurisdiction:
            continue
        if needle:
            hay = " ".join([
                n.id, n.title,
                str(n.raw.get("summary") or ""),
                " ".join(str(a) for a in (n.raw.get("aliases") or [])),
                " ".join(str(v) for v in n.label.values()),
            ]).lower()
            if needle not in hay:
                continue
        items.append(n)

    items.sort(key=lambda n: (n.type, n.id))
    total = len(items)
    page = items[offset: offset + limit]
    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "items": [
            {**(node_brief(g, n.id) or {}),
             "summary": n.raw.get("summary"),
             "tags": n.raw.get("tags") or [],
             "jurisdiction": g.jurisdiction_of(n)}
            for n in page
        ],
    }


def as_of_param(value: str | None) -> date | None:
    return parse_date(value) if value else None
