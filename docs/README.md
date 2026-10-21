# 설계 문서 색인

가상자산 AML 지식베이스의 운영 설계 문서. **읽는 순서대로** 배열했다.

클래스·술어·불변식의 정의는 문서가 아니라 기계판 스키마 하나에 있다 →
[`../kb/schema/schema.yaml`](../kb/schema/schema.yaml) · [`node.schema.json`](../kb/schema/node.schema.json) · [`edge.schema.json`](../kb/schema/edge.schema.json)

---

## 1. 먼저 읽을 것

| 문서 | 내용 |
|---|---|
| [`PLAN.md`](PLAN.md) | **마스터 계획** — 단계 구성, 최종 상태 정의, 리스크 |
| [`architecture/02-storage-topology.md`](architecture/02-storage-topology.md) | 저장소 위상 — 파일 SSOT, 디렉터리 규약, 개행 정규화 |

---

## 2. 거버넌스

지식이 어떻게 검증되고 유지되는가.

| 문서 | 내용 |
|---|---|
| [`governance/01-data-quality.md`](governance/01-data-quality.md) | 품질 6차원, 검증 9계층, 인용 검증, 스코어카드, 미검증 부채 |
| [`governance/02-provenance-confidence.md`](governance/02-provenance-confidence.md) | 출처 등급 T1~T5, 확신도 A~D, 계보, 상충 레지스트리 |
| [`governance/03-review-workflow.md`](governance/03-review-workflow.md) | 역할, 승격 절차, 큐레이터 체크리스트, 큐 위생, 사후 감사 |

---

## 3. 수집

지식이 어떻게 매일 갱신되는가.

| 문서 | 내용 |
|---|---|
| [`ingestion/01-source-registry.md`](ingestion/01-source-registry.md) | 소스 등재 기준, FEED 스키마, 카테고리, 한국 소스 특수 문제 |
| [`ingestion/02-daily-pipeline.md`](ingestion/02-daily-pipeline.md) | 모듈 구성, 실행 순서, 수집 규율, 명단 diff, 브리프 형식 |

---

## 4. 결정 기록

| 문서 | 내용 |
|---|---|
| [`adr/0002-bitemporal-model.md`](adr/0002-bitemporal-model.md) | 이중시간 모델 채택 |
| [`adr/0003-file-ssot-defer-engine.md`](adr/0003-file-ssot-defer-engine.md) | 파일 SSOT · 그래프 엔진 유보 |

---

## 5. 핵심 원칙 요약

| # | 원칙 | 근거 문서 |
|---|---|---|
| 1 | **시점 없는 주장 금지** — 모든 사실에 유효기간 | adr/0002 |
| 2 | **증거 없는 노드 금지** — 모든 노드가 출처에 결속 | governance/02 |
| 3 | **불변 원본** — 수집 원문은 절대 수정하지 않음 | ingestion/02 |
| 4 | **자동은 제안까지, 확정은 사람이** | governance/03 |
| 5 | **상충은 지우지 않고 기록** | governance/02 |
| 6 | **강등은 자동, 승격은 사람** | governance/02 |
| 7 | **모른다는 것을 아는 상태가 잘못 아는 상태보다 낫다** | governance/02 |
| 8 | **공개 저장소는 중립적 산업 지식만** — 비공개 조직 관련 내용 0 | PLAN §9 |
