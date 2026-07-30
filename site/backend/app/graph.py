"""kb/ → 인메모리 그래프.

kb/ 가 SSOT 이므로 DB 를 두지 않는다 (ADR-0003).
검증기(quality/validate_kb.py)와 코드를 공유하지 않는다 — 역할이 다르다.
공유하는 것은 kb/schema/ontology.yaml 이라는 계약뿐이다.
"""
from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

import yaml

# 로더가 절대 읽지 않는 경로 — 공개 사이트 원칙 (03-site-blueprint.md §7)
EXCLUDED = {"_private", "_research"}


def parse_date(value: Any) -> date | None:
    if not isinstance(value, str):
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


@dataclass
class Edge:
    predicate: str
    source: str
    target: str
    qualifiers: dict = field(default_factory=dict)
    valid_from: str | None = None
    valid_to: str | None = None
    evidence: list = field(default_factory=list)
    inverse: bool = False

    def active_at(self, at: date | None) -> bool:
        if at is None:
            return True
        vf, vt = parse_date(self.valid_from), parse_date(self.valid_to)
        if vf and at < vf:
            return False
        if vt and at >= vt:
            return False
        return True


@dataclass
class Node:
    id: str
    type: str
    layer: str
    raw: dict
    path: str
    out: list[Edge] = field(default_factory=list)
    inc: list[Edge] = field(default_factory=list)

    @property
    def label(self) -> dict:
        return self.raw.get("label") or {}

    @property
    def title(self) -> str:
        lb = self.label
        return lb.get("short") or lb.get("ko") or lb.get("en") or self.id


@dataclass
class Graph:
    nodes: dict[str, Node] = field(default_factory=dict)
    facts: list[dict] = field(default_factory=list)
    states: list[dict] = field(default_factory=list)
    metrics: list[dict] = field(default_factory=list)
    contradictions: list[dict] = field(default_factory=list)
    alog: list[dict] = field(default_factory=list)
    ontology: dict = field(default_factory=dict)
    loaded_at: str = ""

    # ── 조회 ──
    def get(self, node_id: str) -> Node | None:
        return self.nodes.get(node_id)

    def by_type(self, node_type: str) -> list[Node]:
        return [n for n in self.nodes.values() if n.type == node_type]

    def type_counts(self) -> dict[str, int]:
        c: dict[str, int] = defaultdict(int)
        for n in self.nodes.values():
            c[n.type] += 1
        return dict(sorted(c.items(), key=lambda x: -x[1]))

    def confidence_counts(self) -> dict[str, int]:
        c: dict[str, int] = defaultdict(int)
        for n in self.nodes.values():
            for ev in n.raw.get("evidence") or []:
                if isinstance(ev, dict) and ev.get("confidence"):
                    c[ev["confidence"]] += 1
        for f in self.facts:
            if f.get("confidence"):
                c[f["confidence"]] += 1
        return {k: c.get(k, 0) for k in ("A", "B", "C", "D")}

    def jurisdiction_of(self, node: Node) -> str | None:
        """노드의 관할. 명시 필드 → HAS_JURISDICTION 엣지 → ID namespace 순."""
        if node.raw.get("jurisdiction"):
            return node.raw["jurisdiction"]
        for e in node.out:
            if e.predicate == "HAS_JURISDICTION":
                return e.target
        if node.type == "JUR":
            return node.id
        ns = node.id.split(":", 1)[1].split("-", 1)[0]
        return f"JUR:{ns}" if ns not in ("x",) else None


def _iter_yaml(root: Path) -> Iterable[Path]:
    for base in ("entities", "sources"):
        d = root / base
        if not d.exists():
            continue
        for p in sorted(d.rglob("*.yaml")):
            if EXCLUDED & set(p.parts):
                continue
            yield p


def _iter_jsonl(path: Path) -> Iterable[dict]:
    if not path.exists():
        return
    for f in sorted(path.rglob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("//"):
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue


def load(kb_root: Path) -> Graph:
    g = Graph()
    g.loaded_at = datetime.now().isoformat(timespec="seconds")

    onto_path = kb_root / "schema" / "ontology.yaml"
    if onto_path.exists():
        g.ontology = yaml.safe_load(onto_path.read_text(encoding="utf-8")) or {}

    for p in _iter_yaml(kb_root):
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not data.get("id"):
            continue
        g.nodes[data["id"]] = Node(
            id=data["id"],
            type=data.get("type", ""),
            layer=data.get("layer", ""),
            raw=data,
            path=p.relative_to(kb_root.parent).as_posix(),
        )

    # 엣지 + 역엣지
    for node in g.nodes.values():
        for raw_edge in node.raw.get("edges") or []:
            if not isinstance(raw_edge, dict) or not raw_edge.get("to"):
                continue
            e = Edge(
                predicate=raw_edge.get("predicate", ""),
                source=node.id,
                target=raw_edge["to"],
                qualifiers=raw_edge.get("qualifiers") or {},
                valid_from=raw_edge.get("valid_from"),
                valid_to=raw_edge.get("valid_to"),
                evidence=raw_edge.get("evidence") or [],
            )
            node.out.append(e)
            tgt = g.nodes.get(e.target)
            if tgt is not None:
                inv = Edge(**{**e.__dict__, "inverse": True})
                tgt.inc.append(inv)

    for rec in _iter_jsonl(kb_root / "facts"):
        (g.contradictions if str(rec.get("id", "")).startswith("CTR:") else g.facts).append(rec)
    g.states.extend(_iter_jsonl(kb_root / "states"))
    g.metrics.extend(_iter_jsonl(kb_root / "metrics"))
    g.alog.extend(_iter_jsonl(kb_root / "alog"))

    return g
