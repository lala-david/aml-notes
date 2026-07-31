# site/ — 규제 계보 탐색기

`kb/` 지식 그래프를 읽어 보여주는 공개 웹. 읽기 전용.

> 설계 → [`../docs/architecture/03-site-blueprint.md`](../docs/architecture/03-site-blueprint.md)

---

## 실행

```bash
# 백엔드 (터미널 1)
cd site/backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
#   API      http://localhost:8000
#   Swagger  http://localhost:8000/docs

# 프론트 (터미널 2)
cd site/frontend
npm install
npm run dev            # http://localhost:5173 (포트가 잡혀 있으면 다음 번호로)
```

**백엔드를 먼저 띄운다.** 프론트만 띄우면 모든 화면이 비고 상단에
연결 실패 안내가 뜬다.

프론트는 브라우저에서 같은 출처로 `/api` 를 부르고, Vite 가 백엔드로
넘긴다(`vite.config.ts`). 그래서 두 포트를 손으로 맞출 필요가 없고 CORS 도
개발에서는 관여하지 않는다. 백엔드를 8000 이 아닌 곳에 띄웠다면
`site/frontend/.env.local` 에 대상만 바꿔 준다.

```bash
VITE_API_TARGET=http://127.0.0.1:8100
```

프론트와 백엔드를 **서로 다른 호스트**에 배포할 때만 `VITE_API_BASE` 로
절대주소를 준다. 이 경우 브라우저가 직접 부르므로 백엔드 `CORS_ORIGINS`
에 프론트 출처를 넣어야 한다.

---

## 구조

```
site/
├── backend/                Python FastAPI
│   ├── app/
│   │   ├── main.py           라우트 · CORS
│   │   ├── graph.py          kb/ → 인메모리 그래프 (역엣지 생성)
│   │   └── queries.py        as_of · crosswalk · lineage · search
│   └── requirements.txt
└── frontend/               React + TypeScript (Vite)
    ├── scripts/gen-types.mjs   kb/schema/*.json → src/types/kb.gen.ts
    └── src/
        ├── api.ts             API 클라이언트
        ├── components.tsx     AsOfControl · ConfidenceBadge · NodeChip · EvidenceList
        ├── pages.tsx          화면
        └── App.tsx            라우팅
```

---

## 화면

| URL | 내용 |
|---|---|
| `/` | 현황 · 클래스별 노드 수 |
| `/search` | 노드 검색·필터 |
| `/n/{id}` | **노드 상세** — 속성 · 증거 · 사실 · 관계 · 큐레이터 메모 |
| `/obl/{id}` | **크로스워크 + 시점 슬라이더** |
| `/lineage/{id}` | 위임·이행 계보 |
| `/facts` | 원자적 사실 (확신도 필터) |
| `/sources` | 출처 레지스트리 (등급별) |
| `/contradictions` | 상충 — 미판정 상단 |
| `/ontology` | 온톨로지 자체 |
| `/alog` | 액션 로그 |

---

## 설계 원칙

**화면을 손으로 만들지 않는다.** `/n/{id}` 렌더러 하나가 모든 노드를 처리한다.
새 노드를 등재하면 페이지가 자동으로 생긴다.

**프론트가 온톨로지와 어긋날 수 없다.**

```bash
npm run gen:types    # kb/schema/*.json → src/types/kb.gen.ts
```

스키마가 바뀌면 프론트 컴파일이 깨진다.

**신뢰 표시가 1급이다.** 확신도 `A`~`D` 와 출처 등급 `T1`~`T5` 를 색으로 구분한다.
지식베이스가 "확실한 것과 아닌 것"을 구별해 두었는데 화면이 뭉개면 그 노력이 사라진다.

**`_private/`·`_research/` 는 로더가 읽지 않는다.** 경로 자체를 `graph.py` 의 `EXCLUDED` 에서 배제한다.

---

## API

Swagger `/docs` · OpenAPI `/openapi.json`

| 엔드포인트 | 비고 |
|---|---|
| `GET /api/ontology` | 클래스·술어·불변식 — 프론트 렌더링 근거 |
| `GET /api/stats` | 노드·사실·확신도 분포 |
| `GET /api/nodes` | `q` `type` `jurisdiction` `tag` |
| `GET /api/nodes/{id}` | 엣지 해석 + 증거 + 역참조 |
| `GET /api/nodes/{id}/neighbors` | `depth` 1~3 |
| `GET /api/crosswalk/{obl_id}` | **`as_of` 지원** |
| `GET /api/lineage/{node_id}` | 위임·이행 경로 |
| `GET /api/facts` | `subject` `confidence` |
| `GET /api/contradictions` | |
| `GET /api/alog` | |

전 엔드포인트가 `as_of=YYYY-MM-DD` 를 받는다(해당되는 경우).

---

## 확인된 동작

```
GET /api/crosswalk/OBL:x-travel-rule-originator
  → 3행: INR.15 §7(b) · 제5조의3 · 제10조의10 제1호

GET /api/crosswalk/OBL:x-travel-rule-originator?as_of=2020-01-01
  → 1행: INR.15 §7(b)      (한국 트래블룰 시행 2022-03-25 이전)

GET /api/lineage/PROV:kr-tfia-art5-3
  → 제5조의3 → (PART_OF) 특금법 → (IMPLEMENTS) R.15
  → 제5조의3 → (DELEGATES_TO) 시행령 제10조의10 → (IMPOSES) 트래블룰
```

---

## 미구현

- 타임라인 (`EVT` 데이터 등재 후)
- 그래프 시각화 (`/api/nodes/{id}/neighbors` 는 이미 node/link 배열 반환)
- 전문 검색 — 현재는 부분일치. 한국어 형태소 처리 미적용
- 배포 설정 (Dockerfile · CI)
