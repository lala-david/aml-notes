# ADR-0004 · Kinetic 계층 정의 정정 및 액션 모델 도입

- **상태**: 채택 (2026-07-30)
- **대체 관계**: 이 결정은 [ADR-0001](0001-property-graph-over-rdf.md) 을 보완한다 (대체하지 않음)
- **근거 출처**: `DOC:jp-leadingai-palantir-ontology` — [`../references.md`](../references.md)

## 맥락

초기 설계는 3계층을 **Semantic / Dynamic / Kinetic** 으로 명명했다. 이 어휘는 Palantir Foundry
온톨로지의 Semantics/Kinetics 이분에서 온 것이나, **원 개념을 확인하지 않고 사용했다.**

원문을 확인한 결과 정의가 어긋났다.

> "the biggest reason Palantir's ontology outperforms others is that it defines the system as an
> integration of **Semantics** (objects, properties, links) and **Kinetics** (actions, functions,
> dynamic security)"
> — `DOC:jp-leadingai-palantir-ontology` 제2장 2-1

| 개념 | 원 정의 | 초기 설계 | 판정 |
|---|---|---|---|
| Semantics | Object type · Property · Link type | L1 — 클래스·속성·술어 | ✅ 정렬 |
| Kinetics | **Action · Function · Dynamic security** | L3 — **수집 파이프라인** | ❌ 오용 |
| Funnel (indexing) | 백엔드 서비스, 온톨로지 요소 아님 | L3 의 실제 내용 | 층위 혼동 |
| Action Log | 액션 실행을 객체로 영구 기록 | 부재 | ❌ 결손 |
| Dynamic security | 명시적 온톨로지 요소 | 문서상 역할 정의만 | ❌ 결손 |

즉 초기 L3 는 Kinetics 가 아니라 **Funnel** 이었다. 그리고 진짜 Kinetics — 지식을 바꾸는
행위의 명세 — 는 모델 밖 스크립트에 흩어져 있었다.

## 결정

### 1. L3 를 재정의한다

L3 KINETIC 은 **쓰기·실행 계층**이다. 4개 클래스를 신설한다.

| 클래스 | 역할 |
|---|---|
| `ACTION` | 변경 트랜잭션 명세 — 변경 집합·제출 기준·부수효과·권한 |
| `FUNC` | 파생 계산 — 결정적, 상태 불변 |
| `ROLE` | 동적 보안 — 누가 어떤 액션을 실행할 수 있는가 |
| `ALOG` | 액션 로그 — 실행 기록을 1급 객체로 |

### 2. 수집을 계층에서 분리한다

수집·정규화·인덱싱은 온톨로지 계층이 아니라 인프라다.
`FEED`·`RUN`·`ITEM`·`SIG`·`TASK` 는 클래스로 유지하되 **`layer: funnel`** 로 재분류한다.

Funnel 은 **사실 후보까지만** 만든다. 후보가 지식이 되는 것은 액션을 통해서다.

### 3. L2 DYNAMIC 은 도메인 확장으로 명시한다

Palantir 표준에는 시간 계층이 없다. L2 이중시간은 **본 저장소가 규제 도메인을 위해 추가한 것**
이며, 그렇게 문서에 표기한다. 차용과 자체 설계를 구분하지 않으면 근거를 추적할 수 없다.

### 4. 운용 액션의 자리를 예약한다

배포된 AML 시스템이 실행할 액션(STR 제출·이체 차단·위험등급 변경 등)은 **명세만 두고 구현하지
않는다.** `IMPLEMENTS_OBLIGATION` 엣지로 L1 의 `OBL` 을 가리키게 해서
**조문 → 의무 → 통제 → 액션** 사슬을 완성한다.

## 근거

### 왜 이 정정이 장식이 아닌가

세 가지가 실제로 달라진다.

1. **변경 경로가 모델 안으로 닫힌다.** 어떤 필드가 어떤 조건에서 바뀔 수 있는지가 `ACTION`
   명세에 있다. 임의 스크립트가 임의 필드를 바꾸는 상태에서는 스키마가 사실상 없다.

2. **액션 로그가 AML 에서는 법적 요건이다.** Palantir 에서 Action Log 는 우수 설계지만,
   AML 에서 기록보존은 규제 의무다. 감독 검사의 질문은 언제나 *"이 판단의 근거는?"* 이며,
   L2 이중시간(당시 알던 것) + L3 액션 로그(당시 한 것) 없이는 답할 수 없다.

3. **AI 에이전트 권한이 구조가 된다.** `ROLE:x-agent` 는 제안만 하고 어떤 액션도 직접 실행하지
   못한다. 이것을 문서 약속이 아니라 온톨로지 요소로 두면 우회할 수 없다.

### 왜 원 출처를 그대로 따르지 않는가

Foundry 백엔드 5서비스(OMS·Object DB·OSS·Actions·Funnel) 구성은 채택하지 않았다.
제품 아키텍처이며 파일 기반 SSOT 설계([ADR-0003](0003-file-ssot-defer-engine.md))와 층위가 다르다.
차용한 것은 **설계 사고방식**이며 제품 사양을 주장하지 않는다.

## 결과

| 영향 | 내용 |
|---|---|
| 문서 | `docs/ontology/03-kinetic-layer.md` 전면 재작성 (정정 고지 포함) |
| 문서 | `docs/architecture/01-overview.md` 계층 도해 수정 |
| 스키마 | `kb/schema/ontology.yaml` — 4 클래스 + 술어 추가, `layer: funnel` 신설 |
| 스키마 | `kb/schema/node.schema.json` — type enum 확장 |
| 검증 | 불변식 K-1 ~ K-6 추가 |
| 미구현 | 액션 실행 런타임·ALOG 자동 생성·속성 단위 통제 집행 |

**정직한 현 상태**: Kinetic 계층은 *명세*가 존재하고 *집행*은 부분적이다.
`validate_kb.py` 가 제출 기준 일부를 검사하고 git 이 제안 절차를 강제하지만,
액션 런타임은 없다. 현재 변경은 사람이 파일을 편집하고 validator 가 사후 검사한다.

## 대안

- **초기 정의 유지** — "Kinetic = 수집"으로 계속 쓰기. 용어가 원 개념과 충돌해 외부 독자가
  오해하며, 진짜 액션 계층의 결손이 감춰진다. 기각.
- **Kinetic 이라는 이름 포기** — 계층을 "Ingestion"으로 개명. 용어 충돌은 해소되나 액션 계층
  결손은 그대로 남는다. 기각.
- **Palantir 모델 전면 채택** — 백엔드 5서비스까지 모사. 파일 SSOT 설계와 충돌하고 구현 비용이
  과도하다. 기각.
