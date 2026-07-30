#!/usr/bin/env python3
"""
지식베이스 검증기 — 불변식 강제

docs/ontology/04-node-edge-spec.md §8 (I-1~I-12)
docs/ontology/05-identifier-scheheme.md §7 (ID-1~ID-8)
docs/ontology/06-timeline-model.md §8 (T-1~T-7)
docs/governance/01-data-quality.md §4 (Q-1~Q-8)

Usage:
    python quality/validate_kb.py [--kb-root kb] [--report quality/dq_report.md]
                                  [--strict] [--json]

Exit code:
    0 = 차단 위반 없음
    1 = 차단(blocking) 위반 존재
    2 = 실행 오류 (스키마 파일 없음 등)

Requires:
    pip install -r quality/requirements.txt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError:
    print("[ERROR] PyYAML 미설치. pip install -r quality/requirements.txt", file=sys.stderr)
    sys.exit(2)

try:
    from jsonschema import Draft202012Validator
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


# namespace 만으로 끝나는 형태(JUR:kr)는 관할 노드에만 허용한다 — check_ids 에서 강제.
ID_RE = re.compile(r"^[A-Z]{3,7}:[a-z0-9]{1,4}(-[a-z0-9][a-z0-9-]*)?$")
SLUG_OPTIONAL_CLASSES = {"JUR"}
SEQ_ID_RE = re.compile(r"^(FACT|STATE|METRIC|SIG|TASK|RUN|ITEM|E):[0-9A-Za-z][0-9A-Za-z:-]*$")

# Q-5 상대 시간 표현 — 절대일자 동반 없이 쓰이면 경고
RELATIVE_TIME_RE = re.compile(
    r"(현재|최근|올해|작년|내년|지난달|지난해|요즘|이번\s?달|얼마\s?전|곧|향후|당분간"
    r"|currently|recently|nowadays|this year|last year)"
)
ABSOLUTE_DATE_RE = re.compile(r"(19|20)\d{2}([-./]\d{1,2})?|\d{4}년")

# Q-5 예외: 스키마 설명·메모 필드는 검사 대상에서 제외
RELATIVE_TIME_EXEMPT_FIELDS = {"curator_note", "parser_note", "tos_note", "summary_en"}

SEVERITY_BLOCK = "block"
SEVERITY_WARN = "warn"


@dataclass
class Finding:
    rule: str
    severity: str
    where: str
    message: str

    def __str__(self) -> str:
        mark = "❌" if self.severity == SEVERITY_BLOCK else "⚠️"
        return f"{mark} [{self.rule}] {self.where}: {self.message}"


@dataclass
class Node:
    id: str
    type: str
    layer: str
    path: Path
    raw: dict
    edges: list[dict] = field(default_factory=list)


@dataclass
class KB:
    nodes: dict[str, Node] = field(default_factory=dict)
    facts: list[tuple[Path, int, dict]] = field(default_factory=list)
    states: list[tuple[Path, int, dict]] = field(default_factory=list)
    metrics: list[tuple[Path, int, dict]] = field(default_factory=list)
    contradictions: list[tuple[Path, int, dict]] = field(default_factory=list)
    alog: list[tuple[Path, int, dict]] = field(default_factory=list)
    ontology: dict = field(default_factory=dict)


# ─────────────────────────────────────────────────────────────
# 로딩
# ─────────────────────────────────────────────────────────────

def load_ontology(kb_root: Path) -> dict:
    path = kb_root / "schema" / "ontology.yaml"
    if not path.exists():
        raise FileNotFoundError(f"온톨로지 파일 없음: {path}")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json_schema(kb_root: Path, name: str) -> dict | None:
    path = kb_root / "schema" / name
    if not path.exists():
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def iter_node_files(kb_root: Path) -> Iterable[Path]:
    entities = kb_root / "entities"
    sources = kb_root / "sources"
    for base in (entities, sources):
        if base.exists():
            yield from sorted(base.rglob("*.yaml"))
            yield from sorted(base.rglob("*.yml"))


def iter_jsonl(base: Path) -> Iterable[tuple[Path, int, dict]]:
    if not base.exists():
        return
    for path in sorted(base.rglob("*.jsonl")):
        with path.open(encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line or line.startswith("//"):
                    continue
                try:
                    yield path, lineno, json.loads(line)
                except json.JSONDecodeError as e:
                    yield path, lineno, {"__parse_error__": str(e)}


def load_kb(kb_root: Path, findings: list[Finding]) -> KB:
    kb = KB(ontology=load_ontology(kb_root))

    for path in iter_node_files(kb_root):
        try:
            with path.open(encoding="utf-8") as f:
                raw = yaml.safe_load(f)
        except yaml.YAMLError as e:
            findings.append(Finding("PARSE", SEVERITY_BLOCK, str(path), f"YAML 파싱 실패: {e}"))
            continue
        if not isinstance(raw, dict):
            findings.append(Finding("PARSE", SEVERITY_BLOCK, str(path), "최상위가 매핑이 아님"))
            continue
        nid = raw.get("id")
        if not nid:
            findings.append(Finding("PARSE", SEVERITY_BLOCK, str(path), "id 필드 없음"))
            continue
        if nid in kb.nodes:
            findings.append(
                Finding("ID-3", SEVERITY_BLOCK, str(path),
                        f"ID 중복: {nid} (기존 {kb.nodes[nid].path})")
            )
            continue
        kb.nodes[nid] = Node(
            id=nid,
            type=raw.get("type", ""),
            layer=raw.get("layer", ""),
            path=path,
            raw=raw,
            edges=raw.get("edges") or [],
        )

    for path, lineno, rec in iter_jsonl(kb_root / "facts"):
        # 상충 레지스트리는 FACT 가 아니라 판정 레코드 — 별도 취급
        if path.name == "contradictions.jsonl":
            kb.contradictions.append((path, lineno, rec))
            continue
        kb.facts.append((path, lineno, rec))
    for path, lineno, rec in iter_jsonl(kb_root / "states"):
        kb.states.append((path, lineno, rec))
    for path, lineno, rec in iter_jsonl(kb_root / "metrics"):
        kb.metrics.append((path, lineno, rec))
    for path, lineno, rec in iter_jsonl(kb_root / "alog"):
        kb.alog.append((path, lineno, rec))

    return kb


# ─────────────────────────────────────────────────────────────
# 유틸
# ─────────────────────────────────────────────────────────────

def parse_date(value: Any) -> date | None:
    if not value or not isinstance(value, str):
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def all_ids(kb: KB) -> set[str]:
    ids = set(kb.nodes)
    for _, _, rec in kb.facts + kb.states + kb.metrics:
        if isinstance(rec.get("id"), str):
            ids.add(rec["id"])
    return ids


def walk_strings(obj: Any, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f"{path}.{k}" if path else str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f"{path}[{i}]")


# ─────────────────────────────────────────────────────────────
# 검사 규칙
# ─────────────────────────────────────────────────────────────

def check_schema(kb: KB, kb_root: Path, findings: list[Finding]) -> None:
    """JSON Schema 검증 (jsonschema 설치 시)."""
    if not HAS_JSONSCHEMA:
        findings.append(Finding(
            "SCHEMA", SEVERITY_WARN, "-",
            "jsonschema 미설치 — 스키마 검증 생략 (pip install jsonschema)"
        ))
        return
    node_schema = load_json_schema(kb_root, "node.schema.json")
    if not node_schema:
        findings.append(Finding("SCHEMA", SEVERITY_WARN, "-", "node.schema.json 없음"))
        return
    validator = Draft202012Validator(node_schema)
    for node in kb.nodes.values():
        for err in validator.iter_errors(node.raw):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            findings.append(Finding(
                "SCHEMA", SEVERITY_BLOCK, f"{node.path}:{loc}", err.message
            ))


def check_ids(kb: KB, kb_root: Path, findings: list[Finding]) -> None:
    """ID-1·ID-2·ID-4·ID-5·ID-6"""
    classes = kb.ontology.get("classes", {})
    ns = kb.ontology.get("namespaces", {})
    allowed_ns = set(ns.get("jurisdictional", [])) | set(ns.get("special", {}))

    for node in kb.nodes.values():
        # ID-1 형식
        if not ID_RE.match(node.id):
            findings.append(Finding("ID-1", SEVERITY_BLOCK, str(node.path),
                                    f"ID 형식 위반: {node.id}"))
            continue
        prefix, rest = node.id.split(":", 1)
        namespace = rest.split("-", 1)[0]

        # ID-9 slug 필수 (관할 노드만 예외 — namespace 자체가 식별자)
        if "-" not in rest and prefix not in SLUG_OPTIONAL_CLASSES:
            findings.append(Finding("ID-9", SEVERITY_BLOCK, str(node.path),
                                    f"slug 누락: {node.id} — {prefix} 는 namespace-slug 형태 필수"))

        # ID-2 클래스 존재
        if prefix not in classes:
            findings.append(Finding("ID-2", SEVERITY_BLOCK, str(node.path),
                                    f"온톨로지에 없는 클래스: {prefix}"))
        # type 필드와 ID 접두어 일치
        if node.type and node.type != prefix:
            findings.append(Finding("ID-2", SEVERITY_BLOCK, str(node.path),
                                    f"type({node.type}) != ID 접두어({prefix})"))
        # ID-4 namespace
        if namespace not in allowed_ns:
            findings.append(Finding("ID-4", SEVERITY_BLOCK, str(node.path),
                                    f"허용되지 않은 namespace: {namespace}"))
        # ID-5 경로 정합
        expected_dir = classes.get(prefix, {}).get("dir")
        if expected_dir:
            # {reg} 같은 템플릿이 든 경로는 검사 생략
            if "{" not in expected_dir:
                actual = node.path.parent.as_posix()
                if not actual.endswith(expected_dir.removeprefix("kb/").rstrip("/")):
                    findings.append(Finding(
                        "ID-5", SEVERITY_WARN, str(node.path),
                        f"경로 불일치 — 기대 {expected_dir}, 실제 {actual}"
                    ))
        # 파일명 = slug
        if node.path.stem != rest:
            findings.append(Finding("ID-5", SEVERITY_WARN, str(node.path),
                                    f"파일명({node.path.stem}) != ID slug({rest})"))

    # ID-6 병합 체인 금지
    for node in kb.nodes.values():
        target = node.raw.get("merged_into")
        if not target:
            continue
        if target not in kb.nodes:
            findings.append(Finding("ID-6", SEVERITY_BLOCK, str(node.path),
                                    f"merged_into 대상 부재: {target}"))
        elif kb.nodes[target].raw.get("status") == "merged":
            findings.append(Finding("ID-6", SEVERITY_BLOCK, str(node.path),
                                    f"병합 체인 금지: {target} 도 merged 상태"))


def check_references(kb: KB, findings: list[Finding]) -> None:
    """ID-7 댕글링 참조 0"""
    known = all_ids(kb)
    for node in kb.nodes.values():
        for i, edge in enumerate(node.edges):
            to = edge.get("to")
            if isinstance(to, str) and to not in known:
                findings.append(Finding(
                    "ID-7", SEVERITY_BLOCK, f"{node.path}:edges[{i}]",
                    f"참조 대상 부재: {to}"
                ))
        for ev in node.raw.get("evidence") or []:
            doc = ev.get("doc") if isinstance(ev, dict) else None
            if isinstance(doc, str) and doc not in known:
                findings.append(Finding(
                    "ID-7", SEVERITY_BLOCK, str(node.path),
                    f"증거 문서 부재: {doc}"
                ))

    # JSONL 레코드(FACT·STATE·METRIC)의 subject·evidence 참조도 검사한다.
    # 이 검사가 없으면 존재하지 않는 노드를 주어로 삼은 사실이 조용히 통과한다.
    for label, records in (
        ("FACT", kb.facts), ("STATE", kb.states), ("METRIC", kb.metrics)
    ):
        for path, lineno, rec in records:
            if "__parse_error__" in rec:
                continue
            where = f"{path}:{lineno}"
            subject = rec.get("subject")
            if isinstance(subject, str) and subject not in known:
                findings.append(Finding(
                    "ID-7", SEVERITY_BLOCK, where,
                    f"{label}.subject 가 실존하지 않음: {subject}"
                ))
            for ev in rec.get("evidence") or []:
                doc = ev.get("doc") if isinstance(ev, dict) else None
                if isinstance(doc, str) and doc not in known:
                    findings.append(Finding(
                        "ID-7", SEVERITY_BLOCK, where,
                        f"{label} 증거 문서 부재: {doc}"
                    ))
            for field in ("superseded_by", "contradicted_by"):
                ref = rec.get(field)
                if isinstance(ref, str) and not ref.startswith("CTR:") and ref not in known:
                    findings.append(Finding(
                        "ID-7", SEVERITY_BLOCK, where,
                        f"{label}.{field} 가 실존하지 않음: {ref}"
                    ))


def check_predicates(kb: KB, findings: list[Finding]) -> None:
    """엣지 술어의 정의역·치역 검사"""
    preds = kb.ontology.get("predicates", {})
    for node in kb.nodes.values():
        for i, edge in enumerate(node.edges):
            where = f"{node.path}:edges[{i}]"
            p = edge.get("predicate")
            if p not in preds:
                findings.append(Finding("ONT-1", SEVERITY_BLOCK, where,
                                        f"정의되지 않은 술어: {p}"))
                continue
            spec = preds[p] or {}
            src_types = spec.get("from") or ["*"]
            dst_types = spec.get("to") or ["*"]
            if "*" not in src_types and node.type not in src_types:
                findings.append(Finding(
                    "ONT-2", SEVERITY_BLOCK, where,
                    f"{p} 의 정의역 위반: {node.type} ∉ {src_types}"
                ))
            to = edge.get("to")
            if isinstance(to, str) and ":" in to:
                to_type = to.split(":", 1)[0]
                if "*" not in dst_types and to_type not in dst_types:
                    findings.append(Finding(
                        "ONT-3", SEVERITY_BLOCK, where,
                        f"{p} 의 치역 위반: {to_type} ∉ {dst_types}"
                    ))


def check_evidence(kb: KB, findings: list[Finding]) -> None:
    """I-1 무증거 노드 금지 · I-7 FACT 증거 결속"""
    exempt = set()
    for inv in kb.ontology.get("invariants", []):
        if inv.get("id") == "I-1":
            exempt = set(inv.get("exempt_classes") or [])
    for node in kb.nodes.values():
        if node.type in exempt:
            continue
        if node.raw.get("status") in {"merged", "deprecated"}:
            continue
        if not (node.raw.get("evidence") or []):
            findings.append(Finding("I-1", SEVERITY_BLOCK, str(node.path),
                                    "evidence 없음 (최소 1개 필요)"))

    for path, lineno, rec in kb.facts:
        if "__parse_error__" in rec:
            findings.append(Finding("PARSE", SEVERITY_BLOCK, f"{path}:{lineno}",
                                    rec["__parse_error__"]))
            continue
        if not (rec.get("evidence") or []):
            findings.append(Finding("I-7", SEVERITY_BLOCK, f"{path}:{lineno}",
                                    f"FACT 에 evidence 없음: {rec.get('id')}"))


def check_provisions(kb: KB, findings: list[Finding]) -> None:
    """I-2 PROV 는 정확히 하나의 REG 에 PART_OF"""
    for node in kb.nodes.values():
        if node.type != "PROV":
            continue
        parents = [
            e for e in node.edges
            if e.get("predicate") == "PART_OF"
            and isinstance(e.get("to"), str)
            and e["to"].startswith("REG:")
        ]
        if len(parents) != 1:
            findings.append(Finding(
                "I-2", SEVERITY_BLOCK, str(node.path),
                f"PROV 의 REG PART_OF 엣지가 {len(parents)}개 (정확히 1개 필요)"
            ))


def check_states(kb: KB, findings: list[Finding]) -> None:
    """I-3 구간 유효성 · I-4 구간 중첩 금지"""
    buckets: dict[tuple[str, str], list[tuple[str, date, date | None]]] = defaultdict(list)

    for path, lineno, rec in kb.states:
        where = f"{path}:{lineno}"
        if "__parse_error__" in rec:
            findings.append(Finding("PARSE", SEVERITY_BLOCK, where, rec["__parse_error__"]))
            continue
        vf = parse_date(rec.get("valid_from"))
        vt = parse_date(rec.get("valid_to"))
        if vf is None:
            findings.append(Finding("I-3", SEVERITY_BLOCK, where, "valid_from 누락 또는 형식 오류"))
            continue
        if vt is not None and vf >= vt:
            findings.append(Finding("I-3", SEVERITY_BLOCK, where,
                                    f"valid_from({vf}) >= valid_to({vt})"))
        if rec.get("retracted_at"):
            continue  # 폐기 레코드는 중첩 검사 제외
        subject, attribute = rec.get("subject"), rec.get("attribute")
        if subject and attribute:
            buckets[(subject, attribute)].append((rec.get("id", where), vf, vt))

    for (subject, attribute), items in buckets.items():
        items.sort(key=lambda x: x[1])
        for (id_a, fa, ta), (id_b, fb, _tb) in zip(items, items[1:]):
            end_a = ta or date.max
            if end_a > fb:
                findings.append(Finding(
                    "I-4", SEVERITY_BLOCK, f"{subject}/{attribute}",
                    f"구간 중첩: {id_a}({fa}~{ta}) 와 {id_b}({fb}~)"
                ))


def check_events(kb: KB, findings: list[Finding]) -> None:
    """I-5 발생≤공표 · T-1 date_precision · T-5 significance · I-6/T-2 CAUSED"""
    for node in kb.nodes.values():
        if node.type != "EVT":
            continue
        raw = node.raw
        where = str(node.path)
        occurred = parse_date(raw.get("occurred_on"))
        announced = parse_date(raw.get("announced_on"))

        if occurred is None:
            findings.append(Finding("T-1", SEVERITY_BLOCK, where, "occurred_on 누락/형식 오류"))
        if not raw.get("date_precision"):
            findings.append(Finding("T-1", SEVERITY_BLOCK, where, "date_precision 누락"))
        if occurred and announced and occurred > announced:
            findings.append(Finding("I-5", SEVERITY_BLOCK, where,
                                    f"occurred_on({occurred}) > announced_on({announced})"))
        if raw.get("impact") == "H" and not raw.get("significance"):
            findings.append(Finding("T-5", SEVERITY_BLOCK, where,
                                    "impact:H 인데 significance 없음"))

        for i, edge in enumerate(node.edges):
            if edge.get("predicate") != "CAUSED":
                continue
            ewhere = f"{where}:edges[{i}]"
            q = edge.get("qualifiers") or {}
            basis = q.get("basis")
            if not basis:
                findings.append(Finding("T-2", SEVERITY_BLOCK, ewhere,
                                        "CAUSED 엣지에 basis 없음"))
            elif basis == "temporal_only":
                findings.append(Finding("T-2", SEVERITY_BLOCK, ewhere,
                                        "basis:temporal_only 금지 — 시간 선후는 인과 근거가 아님"))
            if not q.get("mechanism"):
                findings.append(Finding("T-2", SEVERITY_BLOCK, ewhere, "mechanism 없음"))
            if not q.get("confidence"):
                findings.append(Finding("T-2", SEVERITY_BLOCK, ewhere, "confidence 없음"))

            target = kb.nodes.get(edge.get("to", ""))
            if target and occurred:
                t_occ = parse_date(target.raw.get("occurred_on"))
                if t_occ and occurred > t_occ:
                    findings.append(Finding(
                        "I-6", SEVERITY_BLOCK, ewhere,
                        f"인과 역행: 원인({occurred}) > 결과({t_occ})"
                    ))


def check_confidence_sla(kb: KB, findings: list[Finding], today: date) -> None:
    """I-8 저확신도 노드의 review_due 90일 이내"""
    for node in kb.nodes.values():
        confs = {
            ev.get("confidence")
            for ev in (node.raw.get("evidence") or [])
            if isinstance(ev, dict)
        }
        if not confs & {"C", "D"}:
            continue
        due = parse_date(node.raw.get("review_due"))
        if due is None:
            findings.append(Finding("I-8", SEVERITY_BLOCK, str(node.path),
                                    "확신도 C/D 인데 review_due 없음"))
        elif (due - today).days > 90:
            findings.append(Finding("I-8", SEVERITY_BLOCK, str(node.path),
                                    f"확신도 C/D 의 review_due 가 90일 초과: {due}"))


def check_isolated(kb: KB, findings: list[Finding]) -> None:
    """I-10 고립 노드 (경고)"""
    referenced: set[str] = set()
    for node in kb.nodes.values():
        for edge in node.edges:
            if isinstance(edge.get("to"), str):
                referenced.add(edge["to"])
    for node in kb.nodes.values():
        if node.type in {"SRC", "DOC"}:
            continue  # 증거 결속으로 참조되므로 별도 취급
        if not node.edges and node.id not in referenced:
            findings.append(Finding("I-10", SEVERITY_WARN, str(node.path),
                                    "고립 노드 (엣지 0개, 피참조 0회)"))


def check_symmetry(kb: KB, findings: list[Finding]) -> None:
    """I-11 대칭 술어의 양방향 존재"""
    preds = kb.ontology.get("predicates", {})
    symmetric = {p for p, spec in preds.items() if (spec or {}).get("symmetric")}
    pairs: set[tuple[str, str, str]] = set()
    for node in kb.nodes.values():
        for edge in node.edges:
            p = edge.get("predicate")
            to = edge.get("to")
            if p in symmetric and isinstance(to, str):
                pairs.add((p, node.id, to))
    for p, a, b in sorted(pairs):
        if (p, b, a) not in pairs:
            findings.append(Finding("I-11", SEVERITY_BLOCK, a,
                                    f"대칭 술어 {p} 의 역방향 누락: {b} → {a}"))


def check_units(kb: KB, findings: list[Finding]) -> None:
    """Q-1 수치에 unit · Q-2 통화에 currency · Q-3 METRIC 방법론"""
    for path, lineno, rec in kb.facts:
        if "__parse_error__" in rec:
            continue
        where = f"{path}:{lineno}"
        value = rec.get("value")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if not rec.get("unit"):
                findings.append(Finding("Q-1", SEVERITY_BLOCK, where,
                                        f"수치 FACT 에 unit 없음: {rec.get('id')}"))
            unit = str(rec.get("unit") or "")
            if re.fullmatch(r"[A-Z]{3}", unit) is None and "currency" in str(rec.get("attribute", "")):
                findings.append(Finding("Q-2", SEVERITY_BLOCK, where,
                                        "통화 금액인데 ISO 통화코드 unit 아님"))

    for path, lineno, rec in kb.metrics:
        if "__parse_error__" in rec:
            findings.append(Finding("PARSE", SEVERITY_BLOCK, f"{path}:{lineno}",
                                    rec["__parse_error__"]))
            continue
        where = f"{path}:{lineno}"
        for req in ("estimator", "method"):
            if not rec.get(req):
                findings.append(Finding("Q-3", SEVERITY_BLOCK, where,
                                        f"METRIC 에 {req} 없음: {rec.get('id')}"))

    # Q-7 동일 (subject, measure, period) 의 revision 중복 금지
    seen: dict[tuple, set] = defaultdict(set)
    for path, lineno, rec in kb.metrics:
        if "__parse_error__" in rec:
            continue
        period = rec.get("period") or {}
        key = (rec.get("subject"), rec.get("measure"),
               period.get("start"), period.get("end"))
        rev = rec.get("revision")
        if rev in seen[key]:
            findings.append(Finding("Q-7", SEVERITY_BLOCK, f"{path}:{lineno}",
                                    f"동일 (subject, measure, period) 에 revision 중복: {rev}"))
        seen[key].add(rev)


def check_relative_time(kb: KB, findings: list[Finding]) -> None:
    """Q-5 상대 시간 표현 금지 (경고)"""
    for node in kb.nodes.values():
        for fpath, text in walk_strings(node.raw):
            leaf = fpath.split(".")[-1].split("[")[0]
            if leaf in RELATIVE_TIME_EXEMPT_FIELDS:
                continue
            m = RELATIVE_TIME_RE.search(text)
            if m and not ABSOLUTE_DATE_RE.search(text):
                findings.append(Finding(
                    "Q-5", SEVERITY_WARN, f"{node.path}:{fpath}",
                    f"상대 시간 표현 '{m.group(0)}' — 절대일자 병기 필요"
                ))


def check_alog(kb: KB, findings: list[Finding]) -> None:
    """K-3 · K-5 · K-8 — 액션 로그 무결성."""
    known = all_ids(kb)
    for path, lineno, rec in kb.alog:
        where = f"{path}:{lineno}"
        if "__parse_error__" in rec:
            findings.append(Finding("PARSE", SEVERITY_BLOCK, where, rec["__parse_error__"]))
            continue

        action_id = rec.get("action")
        action = kb.nodes.get(action_id or "")
        if action_id and action is None:
            findings.append(Finding(
                "K-3", SEVERITY_BLOCK, where,
                f"ALOG.action 이 실존하지 않음: {action_id} — ACTION 노드 등재 필요"
            ))

        actor_id = rec.get("actor")
        actor = kb.nodes.get(actor_id or "")
        if actor_id and actor is None:
            findings.append(Finding("K-3", SEVERITY_BLOCK, where,
                                    f"ALOG.actor 가 실존하지 않음: {actor_id}"))
        # K-5 실행 권한 확인
        elif actor and action_id:
            allowed = set(actor.raw.get("can_execute") or [])
            denied = set(actor.raw.get("cannot_execute") or [])
            if action_id in denied:
                findings.append(Finding("K-5", SEVERITY_BLOCK, where,
                                        f"{actor_id} 는 {action_id} 실행이 명시적으로 금지됨"))
            elif allowed and action_id not in allowed:
                findings.append(Finding(
                    "K-5", SEVERITY_WARN, where,
                    f"{actor_id}.can_execute 에 {action_id} 없음 — 권한 정의 갱신 필요"
                ))

        # K-3 대상 노드 실존
        for target in rec.get("targets") or []:
            if isinstance(target, str) and ":" in target and target not in known:
                findings.append(Finding(
                    "K-3", SEVERITY_WARN, where,
                    f"ALOG.targets 항목이 실존하지 않음: {target}"
                ))

        # K-4 제안 필수 액션은 proposal 을 가져야 한다.
        # 소급 기록(backfill)은 예외 — 액션 런타임 도입 이전의 변경을 사후 기록한 것이므로
        # 제안 절차가 존재하지 않았다. 다만 backfill 임을 명시해야 면제된다.
        is_backfill = rec.get("actor_identity") == "backfill"
        if action and action.raw.get("requires_proposal") and not rec.get("proposal"):
            if not is_backfill:
                findings.append(Finding(
                    "K-4", SEVERITY_WARN, where,
                    f"{action_id} 는 requires_proposal 이나 proposal 이 비어 있음 "
                    f"(소급 기록이면 actor_identity: backfill 로 표기할 것)"
                ))

        if rec.get("result") not in ("applied", "rejected", "rolled_back"):
            findings.append(Finding("K-1", SEVERITY_BLOCK, where,
                                    f"ALOG.result 값이 유효하지 않음: {rec.get('result')!r}"))


def check_source_registry(kb: KB, repo_root: Path, findings: list[Finding]) -> None:
    """ingest/config/sources.yaml 의 KB 참조 정합성.

    sources.yaml 은 KB 밖에 있어서 지금까지 검사되지 않았다. 그 결과 존재하지 않는
    SRC·노드를 가리키는 피드가 조용히 통과했다.
    """
    path = repo_root / "ingest" / "config" / "sources.yaml"
    if not path.exists():
        return
    try:
        with path.open(encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except yaml.YAMLError as e:
        findings.append(Finding("SRC-1", SEVERITY_BLOCK, str(path), f"YAML 파싱 실패: {e}"))
        return
    if not isinstance(cfg, dict):
        return

    known = all_ids(kb)
    for feed in cfg.get("feeds") or []:
        if not isinstance(feed, dict):
            continue
        fid = feed.get("id", "(id 없음)")
        where = f"ingest/config/sources.yaml:{fid}"

        src = feed.get("src")
        if isinstance(src, str) and src not in known:
            findings.append(Finding(
                "SRC-2", SEVERITY_WARN, where,
                f"src 가 KB 에 없음: {src} — SRC 노드 생성 필요"
            ))
        for node in feed.get("watch_nodes") or []:
            if isinstance(node, str) and node not in known:
                findings.append(Finding(
                    "SRC-3", SEVERITY_WARN, where,
                    f"watch_nodes 항목이 KB 에 없음: {node}"
                ))
        # 활성 피드는 실측을 통과했어야 한다
        probe = feed.get("probe") or {}
        if feed.get("enabled") and probe.get("status") not in ("ok", "ok-unparsed"):
            findings.append(Finding(
                "SRC-4", SEVERITY_BLOCK, where,
                f"enabled 인데 probe.status={probe.get('status')!r} — 미검증 소스 가동 금지"
            ))
        # robots 금지 소스는 가동할 수 없다
        if feed.get("enabled") and feed.get("robots_ok") is False:
            findings.append(Finding(
                "SRC-5", SEVERITY_BLOCK, where,
                "robots_ok: false 인 소스를 enabled 로 둘 수 없다"
            ))


def check_forbidden_terms(kb: KB, repo_root: Path, findings: list[Finding]) -> None:
    """I-12 비공개 조직 관련 문자열 유출 차단

    금칙어 목록은 quality/rules/forbidden_terms.local.txt (gitignore 대상).
    파일이 없으면 일반 패턴만 검사하고 경고를 남긴다.
    """
    terms: list[str] = []
    local = repo_root / "quality" / "rules" / "forbidden_terms.local.txt"
    if local.exists():
        for line in local.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                terms.append(line)
    else:
        findings.append(Finding(
            "I-12", SEVERITY_WARN, str(local),
            "금칙어 목록 파일 없음 — 조직명 검사 생략. 일반 패턴만 적용."
        ))

    generic = [
        r"진입\s?전략", r"경쟁\s?우위", r"사업\s?계획", r"수익\s?모델",
        r"우리\s?(회사|서비스|제품)", r"go-to-market",
    ]
    patterns = [(t, re.compile(re.escape(t), re.IGNORECASE)) for t in terms]
    patterns += [(g, re.compile(g, re.IGNORECASE)) for g in generic]

    targets = list(iter_node_files(repo_root / "kb"))
    for base in ("kb/facts", "kb/states", "kb/metrics", "intel", "docs"):
        p = repo_root / base
        if p.exists():
            targets += sorted(p.rglob("*.jsonl")) + sorted(p.rglob("*.md"))

    for path in targets:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, rx in patterns:
            m = rx.search(text)
            if m:
                findings.append(Finding(
                    "I-12", SEVERITY_BLOCK, str(path.relative_to(repo_root)),
                    f"금칙 패턴 검출: '{m.group(0)}' (규칙 {label})"
                ))


# ─────────────────────────────────────────────────────────────
# 리포트
# ─────────────────────────────────────────────────────────────

def confidence_distribution(kb: KB) -> dict[str, int]:
    dist: dict[str, int] = defaultdict(int)
    for node in kb.nodes.values():
        for ev in node.raw.get("evidence") or []:
            if isinstance(ev, dict) and ev.get("confidence"):
                dist[ev["confidence"]] += 1
    for _, _, rec in kb.facts:
        if rec.get("confidence"):
            dist[rec["confidence"]] += 1
    return dict(dist)


def score(findings: list[Finding], kb: KB) -> float:
    blocks = sum(1 for f in findings if f.severity == SEVERITY_BLOCK)
    warns = sum(1 for f in findings if f.severity == SEVERITY_WARN)
    dist = confidence_distribution(kb)
    return max(0.0, 100.0 - 5.0 * blocks - 0.5 * warns - 0.2 * dist.get("D", 0))


def write_report(path: Path, kb: KB, findings: list[Finding], today: date) -> None:
    blocks = [f for f in findings if f.severity == SEVERITY_BLOCK]
    warns = [f for f in findings if f.severity == SEVERITY_WARN]
    dist = confidence_distribution(kb)
    by_type: dict[str, int] = defaultdict(int)
    for node in kb.nodes.values():
        by_type[node.type] += 1

    lines = [
        f"# 데이터 품질 스코어카드 — {today.isoformat()}",
        "",
        "> 자동 생성 — `python quality/validate_kb.py`. 직접 편집하지 마세요.",
        "",
        "## 종합",
        "",
        f"| 항목 | 값 |",
        f"|---|---|",
        f"| **종합 점수** | **{score(findings, kb):.1f}** / 100 |",
        f"| 노드 | {len(kb.nodes)} |",
        f"| 사실(FACT) | {len(kb.facts)} |",
        f"| 상태(STATE) | {len(kb.states)} |",
        f"| 관측(METRIC) | {len(kb.metrics)} |",
        f"| 차단 위반 | {len(blocks)} |",
        f"| 경고 | {len(warns)} |",
        "",
        "## 확신도 분포",
        "",
        "| 등급 | 건수 |",
        "|---|---|",
    ]
    for grade in ("A", "B", "C", "D"):
        lines.append(f"| {grade} | {dist.get(grade, 0)} |")

    total_conf = sum(dist.values())
    debt = dist.get("C", 0) + 2 * dist.get("D", 0)
    debt_ratio = (debt / total_conf * 100) if total_conf else 0.0
    lines += [
        "",
        f"**미검증 부채**: {debt} 단위 ({debt_ratio:.1f}%) — 상한 5%",
        "",
        "## 클래스별 노드 수",
        "",
        "| 클래스 | 수 |",
        "|---|---|",
    ]
    for t in sorted(by_type):
        lines.append(f"| {t} | {by_type[t]} |")

    for title, items in (("차단 위반", blocks), ("경고", warns)):
        lines += ["", f"## {title} ({len(items)})", ""]
        if not items:
            lines.append("_없음_")
            continue
        grouped: dict[str, list[Finding]] = defaultdict(list)
        for f in items:
            grouped[f.rule].append(f)
        for rule in sorted(grouped):
            lines.append(f"### {rule} ({len(grouped[rule])})")
            lines.append("")
            for f in grouped[rule][:50]:
                lines.append(f"- `{f.where}` — {f.message}")
            if len(grouped[rule]) > 50:
                lines.append(f"- _...외 {len(grouped[rule]) - 50}건_")
            lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ─────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kb-root", default="kb")
    parser.add_argument("--report", default="quality/dq_report.md")
    parser.add_argument("--strict", action="store_true", help="경고도 실패로 취급")
    parser.add_argument("--json", action="store_true", help="결과를 JSON 으로 stdout 출력")
    parser.add_argument("--today", default=None, help="기준일 (테스트용, YYYY-MM-DD)")
    args = parser.parse_args()

    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")

    kb_root = Path(args.kb_root).resolve()
    repo_root = kb_root.parent
    today = parse_date(args.today) or date.today()

    findings: list[Finding] = []
    try:
        kb = load_kb(kb_root, findings)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 2

    check_schema(kb, kb_root, findings)
    check_ids(kb, kb_root, findings)
    check_references(kb, findings)
    check_predicates(kb, findings)
    check_evidence(kb, findings)
    check_provisions(kb, findings)
    check_states(kb, findings)
    check_events(kb, findings)
    check_confidence_sla(kb, findings, today)
    check_isolated(kb, findings)
    check_symmetry(kb, findings)
    check_units(kb, findings)
    check_relative_time(kb, findings)
    check_alog(kb, findings)
    check_source_registry(kb, repo_root, findings)
    check_forbidden_terms(kb, repo_root, findings)

    write_report(Path(args.report), kb, findings, today)

    blocks = [f for f in findings if f.severity == SEVERITY_BLOCK]
    warns = [f for f in findings if f.severity == SEVERITY_WARN]

    if args.json:
        print(json.dumps({
            "score": round(score(findings, kb), 1),
            "nodes": len(kb.nodes),
            "facts": len(kb.facts),
            "blocking": len(blocks),
            "warnings": len(warns),
            "findings": [f.__dict__ for f in findings],
        }, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f)
        print()
        print(f"노드 {len(kb.nodes)} · 사실 {len(kb.facts)} · 상태 {len(kb.states)}")
        print(f"차단 {len(blocks)} · 경고 {len(warns)} · 점수 {score(findings, kb):.1f}")
        print(f"리포트: {args.report}")

    if blocks:
        return 1
    if args.strict and warns:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
