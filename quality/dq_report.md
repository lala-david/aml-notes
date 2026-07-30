# 데이터 품질 스코어카드 — 2026-07-30

> 자동 생성 — `python quality/validate_kb.py`. 직접 편집하지 마세요.

## 종합

| 항목 | 값 |
|---|---|
| **종합 점수** | **95.5** / 100 |
| 노드 | 109 |
| 사실(FACT) | 19 |
| 상태(STATE) | 3 |
| 관측(METRIC) | 0 |
| 차단 위반 | 0 |
| 경고 | 9 |

## 확신도 분포

| 등급 | 건수 |
|---|---|
| A | 44 |
| B | 34 |
| C | 7 |
| D | 0 |

**미검증 부채**: 7 단위 (8.2%) — 상한 5%

## 클래스별 노드 수

| 클래스 | 수 |
|---|---|
| ACTION | 6 |
| CONCEPT | 1 |
| CTL | 1 |
| DOC | 8 |
| EVT | 1 |
| FUNC | 1 |
| JUR | 8 |
| OBL | 1 |
| ORG | 25 |
| PROV | 4 |
| REG | 9 |
| ROLE | 3 |
| SRC | 38 |
| TYP | 1 |
| VEND | 2 |

## 차단 위반 (0)

_없음_

## 경고 (9)

### I-10 (7)

- `C:\Users\강성준\Desktop\app\aml\kb\entities\concepts\x-virtual-asset.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\regulators\intl-bis.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\regulators\intl-fsb.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\regulators\intl-unsc.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\roles\x-agent.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\roles\x-ontologist.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\typologies\x-exploit.yaml` — 고립 노드 (엣지 0개, 피참조 0회)

### I-12 (1)

- `C:\Users\강성준\Desktop\app\aml\quality\rules\forbidden_terms.local.txt` — 금칙어 목록 파일 없음 — 조직명 검사 생략. 일반 패턴만 적용.

### K-3 (1)

- `C:\Users\강성준\Desktop\app\aml\kb\alog\2026-07.jsonl:6` — ALOG.targets 항목이 실존하지 않음: CTR:00001

