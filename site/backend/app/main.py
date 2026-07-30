"""가상자산 AML 지식베이스 API.

kb/ 를 인메모리 그래프로 적재해 노출한다. 읽기 전용.
"""
from __future__ import annotations

import os
from datetime import date
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from . import graph as g_mod
from . import queries as q

KB_ROOT = Path(os.environ.get("KB_ROOT", Path(__file__).resolve().parents[3] / "kb"))

app = FastAPI(
    title="가상자산 AML 지식베이스 API",
    version="0.1.0",
    description=(
        "규제 계보 탐색기의 백엔드. kb/ 지식 그래프를 투영한다.\n\n"
        "**주의** — 학습·참조용이며 법률 자문이 아니다. "
        "확신도 `C`/`D` 와 `proposed` 상태는 그대로 인용하지 말 것."
    ),
    docs_url="/docs",
)

# 개발 기본값 — vite dev(5173) · vite preview(4173) 를 localhost/127.0.0.1 양쪽으로.
# 호스트 표기가 다르면 CORS 는 다른 오리진으로 취급한다.
_DEV_ORIGINS = [
    f"http://{host}:{port}"
    for host in ("localhost", "127.0.0.1")
    for port in (5173, 4173, 3000)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        o.strip() for o in os.environ.get("CORS_ORIGINS", ",".join(_DEV_ORIGINS)).split(",") if o.strip()
    ],
    allow_methods=["GET"],
    allow_headers=["*"],
)

G: g_mod.Graph = g_mod.load(KB_ROOT)


def _at(as_of: str | None) -> date | None:
    if not as_of:
        return None
    d = q.as_of_param(as_of)
    if d is None:
        raise HTTPException(400, f"as_of 형식 오류: {as_of} (YYYY-MM-DD)")
    return d


# ── 메타 ──

@app.get("/api/ontology", tags=["meta"], summary="온톨로지 — 클래스·술어·불변식")
def get_ontology():
    """프론트 렌더링의 근거. 화면을 손으로 만들지 않기 위해 스키마를 그대로 노출한다."""
    o = G.ontology
    return {
        "version": o.get("version"),
        "updated": o.get("updated"),
        "classes": o.get("classes", {}),
        "predicates": o.get("predicates", {}),
        "invariants": o.get("invariants", []),
        "confidence_levels": o.get("confidence_levels", {}),
        "source_tiers": o.get("source_tiers", {}),
        "lifecycle_states": o.get("lifecycle_states", []),
    }


@app.get("/api/stats", tags=["meta"], summary="현황 통계")
def get_stats():
    layers: dict[str, int] = {}
    for n in G.nodes.values():
        layers[n.layer] = layers.get(n.layer, 0) + 1
    return {
        "loaded_at": G.loaded_at,
        "nodes": len(G.nodes),
        "by_type": G.type_counts(),
        "by_layer": layers,
        "facts": len(G.facts),
        "states": len(G.states),
        "metrics": len(G.metrics),
        "contradictions": len(G.contradictions),
        "unresolved_contradictions": sum(
            1 for c in G.contradictions if c.get("resolution") == "unresolved"
        ),
        "action_log": len(G.alog),
        "confidence": G.confidence_counts(),
    }


# ── 노드 ──

@app.get("/api/nodes", tags=["nodes"], summary="노드 검색·필터")
def list_nodes(
    q_: str | None = Query(None, alias="q", description="ID·제목·요약·별칭 부분일치"),
    type: str | None = Query(None, description="클래스 코드 (REG·PROV·OBL…)"),
    jurisdiction: str | None = Query(None, description="JUR:kr 형태"),
    tag: str | None = None,
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    return q.search(G, q=q_, node_type=type, jurisdiction=jurisdiction, tag=tag,
                    limit=limit, offset=offset)


@app.get("/api/nodes/{node_id:path}/neighbors", tags=["nodes"], summary="이웃 그래프")
def get_neighbors(node_id: str, depth: int = Query(1, ge=1, le=3), as_of: str | None = None):
    if G.get(node_id) is None:
        raise HTTPException(404, f"노드 없음: {node_id}")
    return q.neighbors(G, node_id, depth=depth, at=_at(as_of))


@app.get("/api/nodes/{node_id:path}", tags=["nodes"], summary="노드 상세")
def get_node(node_id: str, as_of: str | None = None):
    detail = q.node_detail(G, node_id, at=_at(as_of))
    if detail is None:
        raise HTTPException(404, f"노드 없음: {node_id}")
    return detail


# ── 질의 ──

@app.get("/api/crosswalk/{obl_id:path}", tags=["query"], summary="관할 크로스워크 (as_of 지원)")
def get_crosswalk(obl_id: str, as_of: str | None = Query(None, description="YYYY-MM-DD")):
    """추상 의무에 걸린 각국 조문을 시점 기준으로 비교한다."""
    cw = q.crosswalk(G, obl_id, at=_at(as_of))
    if cw is None:
        raise HTTPException(404, f"의무 노드 없음: {obl_id}")
    return cw


@app.get("/api/lineage/{node_id:path}", tags=["query"], summary="위임·이행 계보")
def get_lineage(node_id: str, as_of: str | None = None):
    lin = q.lineage(G, node_id, at=_at(as_of))
    if lin is None:
        raise HTTPException(404, f"노드 없음: {node_id}")
    return lin


# ── 레코드 ──

@app.get("/api/facts", tags=["records"], summary="원자적 사실")
def list_facts(
    subject: str | None = None,
    confidence: str | None = Query(None, pattern="^[ABCD]$"),
    limit: int = Query(200, ge=1, le=1000),
):
    items = G.facts
    if subject:
        items = [f for f in items if f.get("subject") == subject]
    if confidence:
        items = [f for f in items if f.get("confidence") == confidence]
    return {"total": len(items), "items": items[:limit]}


@app.get("/api/contradictions", tags=["records"], summary="상충 레지스트리")
def list_contradictions(resolution: str | None = None):
    items = G.contradictions
    if resolution:
        items = [c for c in items if c.get("resolution") == resolution]
    items = sorted(items, key=lambda c: (c.get("resolution") != "unresolved", c.get("id", "")))
    return {"total": len(items), "items": items}


@app.get("/api/alog", tags=["records"], summary="액션 로그")
def list_alog(action: str | None = None, limit: int = Query(200, ge=1, le=1000)):
    items = [a for a in G.alog if not action or a.get("action") == action]
    items = sorted(items, key=lambda a: a.get("executed_at", ""), reverse=True)
    return {"total": len(items), "items": items[:limit]}


@app.get("/api/health", tags=["meta"], include_in_schema=False)
def health():
    return {"ok": True, "nodes": len(G.nodes), "loaded_at": G.loaded_at}
