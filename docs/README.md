# 설계 문서 색인

가상자산 AML 지식베이스의 설계 문서 전체. **읽는 순서대로** 배열했다.

---

## 1. 먼저 읽을 것

| 문서 | 내용 |
|---|---|
| [`PLAN.md`](PLAN.md) | **마스터 계획** — 단계 구성, 최종 상태 정의, 에이전트 운용, 리스크 |
| [`architecture/01-overview.md`](architecture/01-overview.md) | **3계층 아키텍처 총론** — 왜 그래프인가, 계층 간 순환, 저장소 위상 |

---

## 2. 온톨로지

지식이 어떤 모양으로 저장되는가.

| 문서 | 내용 |
|---|---|
| [`ontology/01-semantic-layer.md`](ontology/01-semantic-layer.md) | **L1 의미 계층** — 무엇이 존재하는가 (명사). 4개 축, 추상 의무 설계 |
| [`ontology/02-dynamic-layer.md`](ontology/02-dynamic-layer.md) | **L2 동적 계층** — 언제 참이었는가. 이중시간, 상태기계, 원자적 사실 |
| [`ontology/03-kinetic-layer.md`](ontology/03-kinetic-layer.md) | **L3 운동 계층** — 무엇을 바꿀 수 있는가 (동사). 액션·함수·권한·액션로그 |
| [`ontology/04-node-edge-spec.md`](ontology/04-node-edge-spec.md) | **노드·엣지 전체 명세** ⭐ 규범적 정의. 38 클래스 · 60+ 술어 |
| [`ontology/05-identifier-scheme.md`](ontology/05-identifier-scheme.md) | 식별자 체계 — ID 형식, 불변성, 병합 규칙 |
| [`ontology/06-timeline-model.md`](ontology/06-timeline-model.md) | **타임라인 모델** — 3트랙, 인과 사슬, 국면 구분 |

기계판: [`../kb/schema/ontology.yaml`](../kb/schema/ontology.yaml) · [`node.schema.json`](../kb/schema/node.schema.json) · [`edge.schema.json`](../kb/schema/edge.schema.json)

---

## 3. 거버넌스

지식이 어떻게 검증되고 유지되는가.

| 문서 | 내용 |
|---|---|
| [`governance/01-data-quality.md`](governance/01-data-quality.md) | 품질 6차원, 검증 9계층, 인용 검증, 스코어카드, 미검증 부채 |
| [`governance/02-provenance-confidence.md`](governance/02-provenance-confidence.md) | 출처 등급 T1~T5, 확신도 A~D, 계보, 상충 레지스트리 |
| [`governance/03-review-workflow.md`](governance/03-review-workflow.md) | 역할, 승격 절차, 큐레이터 체크리스트, 큐 위생, 사후 감사 |

---

## 4. 수집

지식이 어떻게 매일 갱신되는가.

| 문서 | 내용 |
|---|---|
| [`ingestion/01-source-registry.md`](ingestion/01-source-registry.md) | 소스 등재 기준, FEED 스키마, 카테고리, 한국 소스 특수 문제 |
| [`ingestion/02-daily-pipeline.md`](ingestion/02-daily-pipeline.md) | 모듈 구성, 실행 순서, 수집 규율, 명단 diff, 브리프 형식 |

---

## 5. 결정 기록 · 출처

| 문서 | 내용 |
|---|---|
| [`adr/0001-property-graph-over-rdf.md`](adr/0001-property-graph-over-rdf.md) | 프로퍼티 그래프를 RDF 대신 채택 |
| [`adr/0002-bitemporal-model.md`](adr/0002-bitemporal-model.md) | 이중시간 모델 채택 |
| [`adr/0003-file-ssot-defer-engine.md`](adr/0003-file-ssot-defer-engine.md) | 파일 SSOT · 그래프 엔진 유보 |
| [`adr/0004-kinetic-layer-correction.md`](adr/0004-kinetic-layer-correction.md) | ⭐ **Kinetic 계층 정의 정정** · 액션 모델 도입 |
| [`references.md`](references.md) | 외부 출처 및 저작자 표시 (CC BY 4.0) |

## 6. 보류 중

| 문서 | 상태 |
|---|---|
| [`architecture/03-site-blueprint.md`](architecture/03-site-blueprint.md) | ⚠️ **결정 보류** — Go + React 공개 사이트. 최종 단계 |

---

## 6. 핵심 원칙 요약

문서를 다 읽을 시간이 없다면 이것만.

| # | 원칙 | 근거 문서 |
|---|---|---|
| 1 | **그래프 우선** — 지식은 노드·엣지로 먼저, 산문은 그 투영 | architecture/01 |
| 2 | **시점 없는 주장 금지** — 모든 사실에 유효기간 | ontology/02 |
| 3 | **증거 없는 노드 금지** — 모든 노드가 출처에 결속 | governance/02 |
| 4 | **불변 원본** — 수집 원문은 절대 수정하지 않음 | ingestion/02 |
| 5 | **자동은 제안까지, 확정은 사람이** | ontology/03, governance/03 |
| 6 | **L1은 골격, L2는 살** — 시간을 의미 계층에 넣지 않음 | ontology/01 |
| 7 | **상충은 지우지 않고 기록** | governance/02 |
| 8 | **강등은 자동, 승격은 사람** | governance/02 |
| 9 | **모른다는 것을 아는 상태가 잘못 아는 상태보다 낫다** | governance/02 |
| 10 | **공개 저장소는 중립적 산업 지식만** — 비공개 조직 관련 내용 0 | PLAN §9 |

---

## 7. 저장소 구조 한눈에

```
aml/
├── docs/            📘 설계 문서 (여기)
├── kb/              🧠 지식 그래프 (L1 + L2) — 커밋·리뷰 대상
│   ├── schema/         온톨로지·JSON Schema
│   ├── entities/       노드 인스턴스 (YAML)
│   ├── facts/          원자적 사실 (JSONL)
│   ├── states/         구간 상태 (JSONL)
│   ├── sources/        출처·문서 레지스트리
│   └── derived/        생성물: 인덱스·크로스워크·타임라인
├── ingest/          ⚡ L3 수집 파이프라인
├── data/            📦 데이터 레이크 (raw·staging 은 gitignore)
├── quality/         ✅ 검증 규칙·리포트
├── intel/           📰 분석 산출물 (브리프·평가서·워치리스트)
├── notes/ …         📖 산문 계층 (그래프에 재결속)
├── _research/       🚫 gitignore — 검증 전 리서치 원시 산출물
└── _private/        🚫 gitignore — 비공개 분석 레이어
```
