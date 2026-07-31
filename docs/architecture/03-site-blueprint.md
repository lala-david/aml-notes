# 공개 사이트 설계 — 규제 계보 탐색기

> **상태: 보류 (2026-07-31).** 구현체를 저장소에서 걷어냈다.
> 지금은 지식베이스에 데이터를 쌓는 것이 먼저다. 화면은 데이터가
> 충분해진 뒤에 다시 꺼낸다.
>
> 이 문서는 **설계 기록으로 남긴다.** 구현을 다시 시작할 때 처음부터
> 다시 정하지 않기 위해서다.
>
> 구현체(FastAPI + React, 38개 파일)는 커밋 `e0aeeeb` 의 `site/` 에 있다.
> 되살리려면 `git checkout e0aeeeb -- site/`.
>
> **되살릴 때 알고 있어야 할 것** — 그때 겪은 문제와 결론:
> - 프론트가 백엔드 포트를 직접 알면 두 포트가 어긋나는 순간 화면
>   전체가 오류로 덮인다. Vite 프록시로 같은 출처를 부르게 할 것.
> - 화면에 기계 필드명(`travel_rule_threshold`, `PARENT_REG`,
>   `DOC:...`)이 그대로 나가면 사람이 읽지 못한다. 표시 이름을 따로 둘 것.
> - 한정자는 **관계에 붙은 값**이다. 노드에 적으면 「트래블룰
>   1,000,000원」처럼 정반대로 읽힌다.
> - 조문 요약은 법률 문장이라 정확하지만 어렵다. `plain` 필드
>   (node.schema.json 에 등재해 둠)를 앞세우고 정밀한 서술을 아래 남길 것.
> - 계보는 방향이 있는 사슬이므로 힘기반 배치가 맞지 않는다.
>   React Flow + dagre(rankdir=LR)로 그렸다.

---

## 1. 무엇을 만드는가

**조문 하나를 클릭하면 그 의무가 어디서 왔고, 누가 바꿀 수 있고, 언제부터 그랬는지를 끝까지 따라갈 수 있는 사이트.**

KB 가 가진 것 중 다른 자료에 없는 셋을 판다.

| 자산 | 왜 다른 데 없나 |
|---|---|
| **시점 질의** (`as_of`) | 이중시간을 넣은 규제 자료가 없다. "2024-12-30 시점 지형"을 보여줄 수 있는 곳이 없다 |
| **위임 사슬** | 법률만 보면 임계값을 모른다. 시행령까지 따라가야 실무 기준이 나오는 경로가 그래프로 있다 |
| **증거 결속** | 모든 주장에 원문 인용·확신도·출처가 붙어 있다 |

---

## 2. "온톨로지식"의 의미 — 화면을 손으로 만들지 않는다

```
❌ 페이지를 하나씩 기획 → 데이터를 끼워넣기
✅ 노드 타입마다 렌더러 하나 → URL 이 곧 노드 ID → 페이지는 자동 생성
```

`/n/PROV:kr-tfia-art5-3` 렌더러 하나를 만들면 조문 4개가 아니라 **앞으로 등재될 250개 조문 전부**가 페이지를 갖는다. 새 노드를 넣으면 사이트가 자라고, 잘못 넣으면 validator 가 막는다.

### 2.1 프론트가 온톨로지와 어긋나지 않게 하는 장치

| 장치 | 효과 |
|---|---|
| `GET /api/ontology` | 클래스·술어·불변식을 API 가 그대로 노출. 프론트가 **스키마를 읽어 렌더링**한다 |
| `node.schema.json` → TS 타입 생성 | 스키마가 바뀌면 **프론트 컴파일이 깨진다** |
| 타입별 렌더러 등록표 | 미등록 타입은 범용 렌더러로 폴백 — 새 클래스가 생겨도 사이트가 죽지 않는다 |

---

## 3. 화면 (전부 그래프 투영)

| URL | 정체 | 우선순위 |
|---|---|---|
| `/n/{id}` | 노드 상세 — 타입별 렌더러 + 증거 패널 + 이웃 그래프 | P0 |
| `/obl/{id}` | **크로스워크 + 시점 슬라이더** — 추상 의무에 걸린 관할 비교 | **P0 ⭐** |
| `/lineage/{prov}` | 계보 — 조문 → 위임 → 국제기준 경로 | P0 |
| `/search` | 노드 검색·필터 (타입·관할·태그·확신도) | P1 |
| `/contradictions` | 상충 레지스트리 — 미판정 상단 | P1 |
| `/alog` | 변경 이력 — 누가 언제 왜 | P1 |
| `/timeline` | 3트랙 역사 + 인과 사슬 | P2 *(데이터 등재 후)* |
| `/ontology` | 온톨로지 자체 탐색 — 클래스·술어 관계도 | P2 |

**먼저 만들 것은 시점 슬라이더**다. 나머지는 잘 만든 위키로도 흉내 낼 수 있지만 이건 못 한다.

---

## 4. 백엔드 — Python FastAPI

### 4.1 왜 Go 가 아닌가

그래프 로더·불변식·`as_of` 질의 로직이 **이미 Python 으로 존재한다**(`quality/validate_kb.py`, `scripts/build_crosswalk.py`).
Go 로 다시 쓰면 SSOT 해석이 두 언어에 중복되고, **둘이 어긋나는 순간 어느 쪽이 맞는지 알 수 없어진다.**
그건 이 KB 가 막으려던 실패 그 자체다.

성능은 제약이 아니다 — 1,200 노드는 메모리에 통째로 올라간다. Swagger 는 FastAPI 가 자동 생성한다.

### 4.2 중복을 피하는 방식 — 공유하는 것은 코드가 아니라 스키마

```
kb/schema/ontology.yaml   ← 단일 계약
      ├─→ quality/validate_kb.py   (강제한다)
      └─→ site/backend/app/graph.py (투영한다)
```

검증기와 API 는 **역할이 다르므로 코드를 공유하지 않는다.** 대신 둘 다 `ontology.yaml` 을 읽는다.
술어 정의역·치역, 클래스 목록, 불변식이 한 파일에만 존재하므로 어긋날 수 없다.

### 4.3 구조

```
site/backend/
├── app/
│   ├── main.py          FastAPI 앱 · CORS · 예외 처리
│   ├── graph.py         kb/ → 인메모리 그래프 (역엣지 생성 포함)
│   ├── queries.py       as_of · lineage · crosswalk · neighbors
│   ├── models.py        Pydantic 응답 모델
│   └── routers/
│       ├── nodes.py     /api/nodes
│       ├── query.py     /api/crosswalk · /api/lineage
│       ├── meta.py      /api/ontology · /api/stats
│       └── records.py   /api/facts · /api/contradictions · /api/alog
├── tests/
└── requirements.txt
```

### 4.4 API

| 엔드포인트 | 역할 |
|---|---|
| `GET /api/ontology` | 클래스·술어·불변식 — **프론트 렌더링의 근거** |
| `GET /api/stats` | 노드·사실·상충 수, 확신도 분포 |
| `GET /api/nodes` | 목록·필터 (`type`, `jurisdiction`, `tag`, `q`) |
| `GET /api/nodes/{id}` | 상세 — 엣지 해석 + 증거 + 역참조 |
| `GET /api/nodes/{id}/neighbors` | 이웃 그래프 (`depth`) |
| `GET /api/crosswalk/{obl_id}` | **관할 비교 (`as_of` 지원)** |
| `GET /api/lineage/{prov_id}` | 위임·이행 경로 역추적 |
| `GET /api/facts` | 사실 (필터: `subject`, `confidence`) |
| `GET /api/contradictions` | 상충 레지스트리 |
| `GET /api/alog` | 액션 로그 |

Swagger UI 는 `/docs`, OpenAPI 스키마는 `/openapi.json`.

### 4.5 적재 전략

기동 시 `kb/` 전량을 메모리에 적재하고 역엣지를 생성한다. 파일이 SSOT 이므로 **DB 없음**(ADR-0003).
재적재는 `POST /api/admin/reload` 또는 프로세스 재시작. 공개 배포에서는 빌드 시점 스냅샷을 굽는다.

---

## 5. 프론트 — React + TypeScript

### 5.1 TS 를 쓰는 실질 이유

`kb/schema/node.schema.json` 에서 **TS 타입을 생성한다.** 스키마가 바뀌면 프론트 컴파일이 깨진다.
이것이 "프론트가 온톨로지와 어긋날 수 없다"의 구현이다.

```
kb/schema/*.json  --json-schema-to-typescript-->  frontend/src/types/kb.ts
```

### 5.2 렌더러 등록 방식

```ts
const renderers: Partial<Record<NodeType, Renderer>> = {
  REG:  RegulationView,
  PROV: ProvisionView,
  OBL:  ObligationView,
  // ...
}
// 미등록 타입 → GenericNodeView 폴백. 새 클래스가 생겨도 사이트가 죽지 않는다.
```

### 5.3 핵심 컴포넌트

| 컴포넌트 | 하는 일 |
|---|---|
| `AsOfSlider` | 시점 이동. 전 화면의 질의에 `as_of` 를 주입 |
| `EvidenceBadge` | 확신도 A~D + 출처 tier. 클릭하면 원문 인용 패널 |
| `LineageGraph` | 위임·이행 경로 시각화 |
| `CrosswalkTable` | 관할 × 임계값 비교 |
| `NodeChip` | 어디서든 노드 참조를 링크로 |

### 5.4 신뢰 표시가 1급이다

확신도 `C`/`D` 와 `proposed` 상태는 **화면에서 시각적으로 구분**되어야 한다.
지식베이스가 "확실한 것과 아닌 것"을 구별해 두었는데 사이트가 뭉개면 그 노력이 사라진다.

---

## 6. 배포

공개 읽기 전용이므로 두 경로가 가능하다.

| 방식 | 조건 |
|---|---|
| **정적 생성** | 빌드 시 API 응답을 전부 구워 정적 호스팅. `as_of` 는 클라이언트 계산 |
| **API 상주** | FastAPI 컨테이너 + 프론트 정적. 시점 질의를 서버가 계산 |

초기에는 **API 상주**로 간다 — `as_of` 조합이 많아 사전 생성이 비효율적이다.
트래픽이 늘면 응답 캐시를 앞에 둔다.

---

## 7. 공개 원칙

- **회사 관련 내용 없음.** 저장소와 동일한 원칙이 사이트에도 적용된다
- **면책 상시 노출** — 법률 자문이 아니며 확신도 `C`/`D` 와 `proposed` 는 그대로 인용 금지
- **출처 링크 필수** — 모든 주장에서 원문으로 갈 수 있어야 한다
- `_private/`·`_research/` 는 **API 가 읽지 않는다** (경로 자체를 로더에서 배제)

---

## 8. 착수 순서

| # | 단계 | 산출 |
|---|---|---|
| 1 | 그래프 로더 + `/api/ontology` `/api/stats` `/api/nodes` | 백엔드 기동·Swagger |
| 2 | `/api/crosswalk` (`as_of`) + `/api/lineage` | **차별화 기능** |
| 3 | 프론트 스캐폴드 + TS 타입 생성 + `NodeView` | 페이지 자동 생성 |
| 4 | `AsOfSlider` + `CrosswalkTable` | 시점 이동 데모 |
| 5 | 증거 패널 · 상충 · 액션 로그 | 신뢰 표시 |
| 6 | 타임라인 | 데이터 등재 후 |
