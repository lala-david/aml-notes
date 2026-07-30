# quality/ — 검증 및 품질 관리

지식베이스의 무결성을 **기계가 강제**하는 지점입니다. 여기를 통과하지 못한 것은 지식이 아닙니다.

---

## 도구

### `validate_kb.py` — 지식 그래프 무결성 검증 ⭐

```bash
pip install -r quality/requirements.txt
python quality/validate_kb.py                  # 검증 + 리포트 생성
python quality/validate_kb.py --strict         # 경고도 실패로 취급
python quality/validate_kb.py --json           # 결과를 JSON 으로
python quality/validate_kb.py --today 2026-12-31  # 기준일 지정 (SLA 테스트)
```

**종료 코드**: `0` 통과 · `1` 차단 위반 존재 · `2` 실행 오류

검사 계층 9단계 — 스키마 → 참조 무결성 → 온톨로지 제약 → 시간 정합성 → 증거 결속 →
인용 검증 → 링크 헬스 → 중복 탐지 → 금칙어.

| 규칙군 | 정의 문서 |
|---|---|
| I-1 ~ I-12 | [`docs/ontology/04-node-edge-spec.md`](../docs/ontology/04-node-edge-spec.md) §8 |
| ID-1 ~ ID-9 | [`docs/ontology/05-identifier-scheme.md`](../docs/ontology/05-identifier-scheme.md) §7 |
| T-1 ~ T-7 | [`docs/ontology/06-timeline-model.md`](../docs/ontology/06-timeline-model.md) §8 |
| Q-1 ~ Q-8 | [`01-data-quality.md`](../docs/governance/01-data-quality.md) §4 |
| ONT-1 ~ ONT-3 | 술어 정의역·치역 — `kb/schema/ontology.yaml` |

**차단 vs 경고**: 기계적으로 판정 가능하고 오탐이 없는 것만 차단합니다. 경고를 차단으로 만들면
CI 가 상시 빨간불이 되어 아무도 보지 않게 됩니다.

### 산문 계층 검증

```bash
python quality/validate_links.py          # 내부 상대 링크
python quality/validate_mermaid.py        # Mermaid 블록 mmdc 컴파일
python quality/check_external_urls.py     # 외부 URL 생존 (느림 — 분기·수동만)
```

`validate_mermaid.py` 는 mmdc 툴체인·설정·캐시를 `charts/` 에서 참조합니다.
사전에 `cd charts && npm install` 이 필요합니다.

---

## 산출물

| 파일 | 생성 | 내용 |
|---|---|---|
| `dq_report.md` | 매 실행 | 품질 스코어카드 · 확신도 분포 · 미검증 부채 · 위반 목록 |

`dq_report.md` 는 생성물입니다. 직접 편집하지 마세요.

### 종합 점수 산식

```
100 - 5.0×(차단 위반) - 0.5×(경고) - 0.2×(확신도 D 노드)
```

**중요한 것은 절대값이 아니라 추세입니다.** 점수가 내려가는데 이유를 모르면 그것이 문제입니다.

---

## 미검증 부채

확신도 `C`/`D` 인 지식은 **부채로 계상**합니다 (D 는 2 단위).

| 규칙 | 내용 |
|---|---|
| 상한 | 전체의 **5%** 초과 시 신규 저확신도 유입 차단 |
| 상환 | 원문 확보로 A/B 승격, 또는 검증 불가 판정 후 제거 |
| 가시화 | 스코어카드에 상시 노출 |

이 장치가 없으면 "일단 넣어두고 나중에 확인"이 누적되어 신뢰도가 무너집니다.
대부분의 지식베이스가 이렇게 죽습니다.

---

## 규칙 설정

- [`rules/README.md`](rules/README.md) — 금칙어 목록 운용 (I-12)
- `rules/forbidden_terms.local.txt` — **gitignore 대상.** 목록 자체가 무엇을 숨기려 했는지
  드러내므로 커밋하지 않습니다. CI 에서는 시크릿으로 주입합니다.

---

## CI

| 워크플로 | 트리거 | 역할 |
|---|---|---|
| `kb-validate.yml` | `kb/**` 변경 · 매일 06:30 KST | 그래프 검증 + 파생물 재현성 확인 |
| `validate.yml` | `**/*.md` 변경 | 산문 링크·Mermaid |

`kb-validate.yml` 은 파생물 재현성도 검사합니다 — `kb/derived/` 가 재생성 결과와 다르면
누군가 생성물을 손으로 고친 것이므로 실패시킵니다 ([ADR-0003](../docs/adr/0003-file-ssot-defer-engine.md)).
