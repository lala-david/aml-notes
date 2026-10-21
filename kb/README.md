# kb/ — 지식 그래프

> 이 디렉터리가 **단일 진실 원천(SSOT)** 입니다. 그래프·인덱스·산문은 전부 여기서 파생됩니다.
> 클래스·술어·불변식 정의 → [`schema/schema.yaml`](schema/schema.yaml)

---

## 규칙 5개

1. **1 노드 = 1 파일.** 파일 경로는 ID 에서 결정됩니다 — `REG:kr-tfia` → `entities/regulations/kr-tfia.yaml`
2. **ID 는 불변.** 오타로 만든 것도 고치지 않고 `MERGED_INTO` 로 처리합니다
3. **덮어쓰기 금지.** 정정은 폐기 표시 + 새 레코드
4. **`derived/` 는 생성물** — 직접 편집 금지. CI 가 재생성 결과와 대조합니다
5. **증거 없는 노드 금지** — `SRC`·`CONCEPT`·`CAP` 만 예외

변경 전 `python ../quality/validate_kb.py` 로 확인하세요. 차단 위반이 있으면 merge 되지 않습니다.

---

## 구조

```
kb/
├── schema/                    데이터 스키마 — 여기가 규범
│   ├── schema.yaml               34 클래스 · 50 술어 · 14 불변식
│   ├── node.schema.json          노드 공통 JSON Schema
│   └── edge.schema.json          엣지 공통 JSON Schema
│
├── entities/                  엔티티 노드 (명사) + 일부 시간 노드
│   ├── jurisdictions/            JUR — 관할
│   ├── regulators/               ORG — 감독기관·국제기구
│   ├── regulations/              REG — 규범
│   │   └── {reg}/provisions/       PROV — 조문 (규범 하위)
│   ├── obligations/              OBL — 의무 (관할 탈각 추상 의무)
│   ├── controls/                 CTL — 통제 수단
│   ├── concepts/                 CONCEPT — 용어·개념
│   ├── risks/                    RISK — 위험요인
│   ├── typologies/               TYP — 자금세탁 유형론 (전술)
│   ├── techniques/               TEC — 기법
│   ├── indicators/               IND — 탐지 지표
│   ├── chains/ assets/           CHAIN · ASSET — 체인·가상자산
│   ├── protocols/                PROTO — 믹서·브리지·트래블룰 프로토콜
│   ├── vasps/ vendors/           VASP · VEND — 사업자·솔루션 공급자
│   ├── capabilities/             CAP — 벤더 역량 비교축
│   ├── threat-actors/            ACT — 위협행위자
│   ├── events/ eras/             EVT · ERA — 사건·국면
│   ├── incidents/ enforcement/   INC · ENF — 사고·집행조치
│   └── cases/                    CASE — 판례·소송
│
├── facts/                     원자적 사실 (JSONL, append-only)
│   ├── {YYYY}-{MM}.jsonl
│   └── contradictions.jsonl      상충 레지스트리 — 어느 쪽도 삭제하지 않음
├── states/{YYYY}.jsonl        구간 상태 (이중시간)
├── metrics/{measure}.jsonl    관측 수치 (시계열)
│
├── sources/                   출처 레지스트리
│   ├── {ns}-{slug}.yaml          SRC — 발행처
│   └── documents/                DOC — 개별 문서
│
└── derived/                   🤖 생성물 — 직접 편집 금지
    └── crosswalk/                관할 비교표 (scripts/build_crosswalk.py)
```

빈 디렉터리는 `.gitkeep` 으로 유지됩니다 — **설계상 존재해야 하는 자리이며 아직 안 채워진 것**입니다.

---

## 현재 상태 (2026-10-21)

| 항목 | 수 | 비고 |
|---|---:|---|
| 노드 | **333** | 목표 1,200 |
| 사실 (FACT) | 49 | |
| 구간 상태 (STATE) | 3 | |
| 상충 (CTR) | 7 | **전부 판정 완료** |

**클래스별**: IND 80 · TEC 62 · DOC 56 · SRC 45 · ORG 26 · PROV 21 · REG 18 · JUR 8 · TYP 8 · EVT 4 · VEND 2 · 기타 3

**확신도 분포** (증거 단위): A 238 · B 196 · C 7 · D 0 — 미검증 부채 1.6% (상한 5%)

### 채워진 것

- **트래블룰 관할 크로스워크** — 국제기준(INR.15 §7(b))과 8개 관할 조문. 한국은 2027-02-18 / 2027-02-19 두 구간으로 분할
- **한국 특금법 위임 사슬** — 법률 제5조의3·제6조제3항 → 시행령 제10조의10
- **출처 레지스트리** — `ingest/config/sources.yaml` 의 50개 피드가 참조하는 SRC·ORG 전량
- **유형론** — 7전술 · 62기법 · 80지표 (FATF Red Flag 2020 원문 결속 39건, 신규 17건)
- **한국 위임 사슬 확장** — 특금법 → 시행령 §10의10·§10의20 → FIU 고시 §28-2, 이용자보호법 §12, 통신사기피해환급법

### 비어 있는 것

`protocols/` · `vasps/` · `threat-actors/` ·
`incidents/` · `enforcement/` · `eras/` — 리서치 도시에에 자료는 있으나 아직 노드로 등재하지 않았습니다.

---

## 알려진 부채

| # | 내용 |
|---|---|
| 1 | 신규 노드 다수가 **확신도 B/C** — 증거가 자체 실측 기록뿐. 1차 문서로 재결속 필요 |
| 2 | `CONCEPT:x-virtual-asset` 에 **`DEFINES` 엣지 0개** — 정의 차이가 규제 범위를 가르는데 조문 미연결 |
| 3 | `PROV` 대부분 **`text_orig` 미확보** — FATF INR.15 §7(b) 만 전문 등재됨 |

부채 현황은 `python ../quality/validate_kb.py` 실행 후 [`../quality/dq_report.md`](../quality/dq_report.md) 에서 확인합니다.

---

## 자주 쓰는 명령

```bash
python quality/validate_kb.py              # 무결성 검증 (차단 위반 시 exit 1)
python scripts/build_crosswalk.py          # 관할 비교표 재생성
python scripts/build_crosswalk.py --stdout --as-of 2020-01-01   # 시점 질의
```
