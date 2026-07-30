# 참고 출처 및 저작자 표시

본 저장소가 **설계 방법론**의 근거로 사용한 외부 저작물과 그 라이선스 의무를 기록한다.
가상자산 AML 사실관계의 출처는 `kb/sources/` 에 `SRC`·`DOC` 노드로 관리한다.

---

## 온톨로지 설계 방법론

### The Palantir Impact: Ontology Strategy Connecting Data and AI

| 항목 | 내용 |
|---|---|
| 원제 | パランティアの衝撃：データとAIを繋ぐ「オントロジー」戦略 |
| 저자 | Satoshi Yamauchi (山内怜史) — AI Strategist, Leading.AI |
| 출처 | https://github.com/Leading-AI-IO/palantir-ontology-strategy |
| 참조 커밋 | `d57c543e97f33f4d3d1240846267dd881b018bd1` (2026-07-28) |
| 라이선스 | **CC BY 4.0** — https://creativecommons.org/licenses/by/4.0/ |
| 저작권 | © 2026 Satoshi Yamauchi / Leading AI |
| KB 노드 | `SRC:jp-leadingai` · `DOC:jp-leadingai-palantir-ontology` |
| 로컬 사본 | `_research/sources/palantir-ontology-strategy/` (gitignore) |

> **저작자 표시 (CC BY 4.0 요구사항)**
> 본 저장소의 온톨로지 계층 구조는 위 저작물의 Semantics/Kinetics 이분 및
> 브랜치-리뷰 통치 모델에 근거한다.
> © 2026 Satoshi Yamauchi / Leading AI — Licensed under CC BY 4.0.
> **변경 사항 있음** — 아래 §채택·확장·미채택 참조.

#### 채택한 것

| 개념 | 본 저장소 적용 |
|---|---|
| **Semantics / Kinetics 이분** | L1 SEMANTIC(명사) / L3 KINETIC(동사) |
| Kinetics = Action · Function · Dynamic security | `ACTION`·`FUNC`·`ROLE` 클래스 |
| **Action Log** — 액션 실행을 객체로 영구 기록, 대상에 연결 | `ALOG` 클래스 |
| **Ontology Proposals** — 브랜치 → 테스트 → 제안 → 리뷰 → 머지 | git 브랜치 + PR + 체크리스트 |
| 접근통제 2축 — 행 단위(RV) + 속성 단위(MDO) | 노드 단위 + 속성 단위 통제 규칙 |
| Funnel 의 batch / streaming 구분 | 일일 파이프라인 / 제재 명단 2회·일 |
| "읽기 모델과 변경 모델을 함께 닫는다" | 변경 경로를 모델 안에 정의 |

#### 확장한 것 (원 출처에 없음)

| 추가 | 이유 |
|---|---|
| **L2 DYNAMIC 이중시간 계층** | 규제 도메인은 "언제 효력이 있었나(valid time)"와 "우리가 언제 알았나(transaction time)"를 분리해야 한다. Palantir 표준에는 시간 계층이 없다 |
| 출처 등급 T1~T5 · 확신도 A~D | 규제 사실의 신뢰도 관리 |
| 상충 레지스트리 | 출처가 엇갈릴 때 어느 쪽도 지우지 않는 규율 |
| 신선도 SLA | 제재 1일 ~ 유형론 180일 |
| 3트랙 역사 타임라인 + 인과 엣지 | 규정의 취지를 계보로 이해하기 위해 |

#### 채택하지 않은 것

| 미채택 | 이유 |
|---|---|
| Foundry 백엔드 5서비스 (OMS · Object DB · OSS · Actions · Funnel) | 제품 아키텍처이며 파일 기반 SSOT 설계([ADR-0003](adr/0003-file-ssot-defer-engine.md))와 층위가 다르다 |
| Restricted Views · MDO 등 제품 기능명 | 개념만 차용하고 구현은 자체 설계 |
| AI FDE 런타임 | 에이전트는 `_research/` 제안까지만 (`ROLE:x-agent`) |

> ⚠️ 위 저작물의 Palantir 제품 아키텍처 서술은 **2차 정보**다. 본 저장소는 설계 사고방식만
> 차용하며 제품 사양을 주장하지 않는다. 제품 사양 확인이 필요하면 Palantir 공식 문서를 볼 것 —
> https://www.palantir.com/docs/foundry/ontology/overview/

관련 결정 → [ADR-0004](adr/0004-kinetic-layer-correction.md)

---

## 온톨로지 학술 정의

위 저작물이 인용한 1차 문헌. 본 저장소도 동일 정의를 전제한다.

| 문헌 | 정의 |
|---|---|
| Gruber, T. R. (1993). *A translation approach to portable ontology specifications.* [DOI](https://link.springer.com/article/10.1007/BF00993851) | "explicit specification of a conceptualization" |
| Studer, R., Benjamins, V. R., & Fensel, D. (1998). *Knowledge engineering: Principles and methods.* [DOI](https://doi.org/10.1016/S0169-023X(97)00039-6) | "formal, explicit specification of a **shared** conceptualization" |

Studer 의 "shared" 가 본 저장소에 직접 적용된다 — 온톨로지는 개인 메모가 아니라
**여러 사람·에이전트·시스템이 공유하는 형식 명세**여야 한다. 그래서 클래스 추가에 ADR 을 요구하고,
자유 문자열 대신 열거형을 강제한다.

---

## 상호운용 표준

내보내기 대상으로 정렬한 표준. 채택 근거는 [`ontology/04-node-edge-spec.md §7`](ontology/04-node-edge-spec.md).

| 표준 | 용도 |
|---|---|
| JSON-LD | 외부 공개용 그래프 직렬화 |
| SKOS | `CONCEPT`·`TYP`·`TEC` 분류 계층 |
| PROV-O | `DOC`·`ITEM`·`RUN` 계보 표현 |
| STIX 2.1 | `ACT`·`TEC`·`IND` → intrusion-set · attack-pattern · indicator |
| IVMS101 | 트래블룰 데이터 모델 (도메인 표준) |

---

## 본 저장소 라이선스

문서 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 코드 [MIT](../LICENSE).

CC BY 4.0 저작물을 근거로 사용했으므로 본 저장소 문서도 동일 계열 라이선스를 유지한다.
