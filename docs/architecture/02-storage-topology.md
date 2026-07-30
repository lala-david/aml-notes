# 저장소 위상 · 파일 규약

> **원칙**: 파일이 단일 진실 원천(SSOT) · 그래프·인덱스는 언제든 재생성 가능

---

## 1. 왜 파일인가 (DB 가 아니라)

| 요구 | 파일(Git) | DB |
|---|---|---|
| 변경 이력 | 커밋 단위 완전 보존 | 별도 감사 테이블 필요 |
| 리뷰 | PR diff 로 사람이 검토 | 어려움 |
| 계보 | "누가 언제 왜"가 커밋에 내장 | 별도 구현 |
| 이식성 | 벤더 종속 없음 | 종속 |
| 협업 | 브랜치·충돌 해결 | 락 기반 |
| 질의 성능 | 나쁨 | 좋음 |

지식베이스에서 **가장 중요한 것은 질의 성능이 아니라 검토 가능성**이다. 잘못된 사실이 들어가는 것을 막는 것이 빠르게 조회하는 것보다 우선한다. 질의는 빌드 산출물이 담당한다.

전환 시점: 노드 20,000 초과 또는 다중 동시 편집자 5인 초과. 그때도 파일은 SSOT 로 유지하고 DB 는 캐시로 둔다.

---

## 2. 디렉터리 규약

```
kb/
├── schema/
│   ├── ontology.yaml
│   ├── node.schema.json
│   ├── edge.schema.json
│   └── types/{TYPE}.schema.json
├── entities/
│   ├── jurisdictions/{ns}-{slug}.yaml
│   ├── regulators/{ns}-{slug}.yaml
│   ├── regulations/
│   │   ├── {ns}-{slug}.yaml
│   │   └── {ns}-{slug}/provisions/{path}.yaml
│   ├── obligations/{ns}-{slug}.yaml
│   ├── controls/ concepts/ risks/
│   ├── typologies/ techniques/ indicators/
│   ├── chains/ assets/ protocols/
│   ├── vasps/ vendors/ capabilities/ threat-actors/
│   ├── events/{ns}-{slug}.yaml
│   ├── eras/ incidents/ enforcement/ cases/
├── facts/
│   ├── {YYYY}-{MM}.jsonl              # 월별 분할
│   └── contradictions.jsonl
├── states/{YYYY}.jsonl
├── metrics/{measure}.jsonl
├── sources/
│   ├── {ns}-{slug}.yaml               # SRC
│   └── documents/{ns}-{slug}.yaml     # DOC
├── derived/                            # 🤖 생성물 — 직접 편집 금지
│   ├── index/
│   ├── crosswalk/
│   └── timeline/
└── .counters.json
```

### 2.1 경로 = ID 규칙

파일 경로는 ID 에서 결정적으로 도출된다. validator 가 이를 검사한다(ID-5).

```
REG:kr-tfia            → kb/entities/regulations/kr-tfia.yaml
PROV:kr-tfia-art5-3    → kb/entities/regulations/kr-tfia/provisions/art5-3.yaml
OBL:x-travel-rule-originator → kb/entities/obligations/x-travel-rule-originator.yaml
DOC:kr-lawgokr-tfia-20260101 → kb/sources/documents/kr-lawgokr-tfia-20260101.yaml
```

이렇게 하면 **ID 만 알면 파일을 찾을 수 있고**, 반대로 파일 위치가 잘못된 ID 를 잡아낸다.

### 2.2 `derived/` 는 생성물

`kb/derived/` 는 `build_graph` 가 만든다. 직접 편집 금지이며, CI 가 재생성 결과와 커밋된 내용이 일치하는지 검사한다. 불일치는 곧 "누군가 생성물을 손으로 고쳤다"는 뜻이다.

---

## 3. 파일 포맷 규약

| 항목 | 규칙 |
|---|---|
| 인코딩 | UTF-8 (BOM 없음) |
| 개행 | LF |
| YAML | 2칸 들여쓰기, 앵커·별칭 금지(diff 가독성) |
| JSONL | 1줄 1레코드, 정렬된 키, 개행 문자 이스케이프 |
| 날짜 | ISO 8601 `YYYY-MM-DD`, 시각은 `Z` 표기 UTC |
| 문자열 | 한국어 원문 그대로. 로마자 변환 금지 |
| 빈 값 | `null` 명시 (필드 생략과 구분) |

**`.gitattributes` 로 개행을 강제한다** — Windows 환경에서 CRLF 가 섞이면 diff 가 무의미해진다.

### 3.1 JSONL 키 정렬

JSONL 은 diff 가능성을 위해 키를 알파벳순으로 정렬해 쓴다. 정렬하지 않으면 같은 내용도 매번 다른 줄로 보인다.

---

## 4. 데이터 레이크

```
data/
├── raw/                   🚫 gitignore
│   └── {YYYY}/{MM}/{DD}/{feed-slug}/
│       ├── {ISO8601}.{ext}          # 응답 원문
│       └── {ISO8601}.meta.json      # 요청·응답 메타
├── staging/               🚫 gitignore
│   └── items/{YYYY-MM-DD}.jsonl
└── curated/               ✅ 커밋
    ├── runs/{YYYY-MM}.jsonl
    ├── signals/{YYYY-MM}.jsonl
    ├── tasks/{YYYY-MM}.jsonl
    └── snapshots/                    # 명단 파일 정규화 스냅샷
        └── {list-slug}/{YYYY-MM-DD}.jsonl
```

### 4.1 raw 를 커밋하지 않는 이유

| 이유 | 설명 |
|---|---|
| 용량 | 일일 수십 MB, 1년이면 저장소가 감당 못 함 |
| 라이선스 | 원문 전량 재배포는 이용약관 위반 가능 |
| 가치 | 재수집 가능하거나, 필요한 부분은 `DOC.snapshot_path` 로 별도 보존 |

**단, 증거로 쓰인 문서의 스냅샷은 예외**다. 인용 검증에 필요하므로 `DOC` 에 결속된 스냅샷은 별도 보존 정책을 적용한다 (용량 제한 시 텍스트만 추출 보관).

### 4.2 보존 정책

| 대상 | 보존 |
|---|---|
| `raw/` 전체 | 90일 (로컬), 이후 증거 결속분만 |
| 증거 결속 스냅샷 | 영구 |
| `staging/` | 30일 |
| `curated/` | 영구 (Git) |

---

## 5. 빌드 산출물

```
build/                      🚫 gitignore
├── graph.json              # 정규화된 노드·엣지 (역엣지 포함)
├── graph.sqlite            # 질의용
├── index/
│   ├── fts.sqlite
│   └── embeddings.bin
└── export/
    ├── jsonld/
    ├── stix/
    └── csv/
```

`build/` 는 전부 재생성 가능하므로 커밋하지 않는다. 단 `kb/derived/` 의 일부(타임라인 마크다운, 크로스워크 표)는 사람이 읽는 산출물이므로 커밋한다.

### 5.1 재현성 요구

```
git clone → build_graph → 동일한 build/ 산출물
```

이것이 보장되지 않으면 SSOT 원칙이 깨진 것이다. 빌드에 외부 네트워크 호출이 들어가면 안 되며, 필요한 데이터는 전부 저장소 안에 있어야 한다.

---

## 6. 대용량 대응

| 상황 | 임계 | 대응 |
|---|---|---|
| FACT JSONL 비대 | 파일당 50MB | 월별 → 주별 분할 |
| 노드 수 | 20,000 | DB 캐시 도입 검토 |
| raw 용량 | 10GB | 외부 오브젝트 스토리지 |
| 스냅샷 | — | 텍스트 추출본만 보관 |
| Git 저장소 | 1GB | 이력 정리 또는 LFS |

---

## 7. gitignore 정책

```gitignore
# 검증 전 리서치 원시 산출물 — 절대 커밋 금지
_research/

# 비공개 분석 레이어
_private/

# 데이터 레이크 랜딩·스테이징 (curated 만 커밋)
data/raw/
data/staging/

# 빌드 산출물
build/

# 런타임 출력
regulatory-changes.json
regulatory-changes.md
```

`_research/` 와 `_private/` 는 **이중 방어**를 건다.

1. `.gitignore` 로 스테이징 차단
2. CI 금칙어 스캔으로 혹시 커밋된 경우 차단

리서치 산출물은 검증 전 상태이므로 확신도가 낮은 주장이 섞여 있다. 그것이 그대로 공개되면 지식베이스의 신뢰도 기준이 무너진다. **검증 게이트를 통과한 것만 `kb/` 로 옮긴다.**
