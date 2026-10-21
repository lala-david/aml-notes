# 데이터 품질 스코어카드 — 2026-10-21

> 자동 생성 — `python quality/validate_kb.py`. 직접 편집하지 마세요.

## 종합

| 항목 | 값 |
|---|---|
| **종합 점수** | **90.5** / 100 |
| 노드 | 333 |
| 사실(FACT) | 49 |
| 상태(STATE) | 3 |
| 관측(METRIC) | 0 |
| 차단 위반 | 0 |
| 경고 | 19 |

## 확신도 분포

| 등급 | 건수 |
|---|---|
| A | 238 |
| B | 196 |
| C | 7 |
| D | 0 |

**미검증 부채**: 7 단위 (1.6%) — 상한 5%

## 클래스별 노드 수

| 클래스 | 수 |
|---|---|
| CONCEPT | 1 |
| CTL | 1 |
| DOC | 56 |
| EVT | 4 |
| IND | 80 |
| JUR | 8 |
| OBL | 1 |
| ORG | 26 |
| PROV | 21 |
| REG | 18 |
| SRC | 45 |
| TEC | 62 |
| TYP | 8 |
| VEND | 2 |

## 차단 위반 (0)

_없음_

## 경고 (19)

### I-10 (18)

- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-address-on-illicit-forum.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-adverse-public-record.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-counterparty-knowledge-gap.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-credential-churn-ato.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-elderly-high-frequency.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-financially-vulnerable-account.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-hardware-wallet-cross-border.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-illicit-memo-language.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-kyc-refusal-source-of-funds.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-loss-making-conversion.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-proxy-domain-registration.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-sanctioned-jurisdiction-ip.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-stolen-funds-address-deposit.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-tor-vpn-session.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-wealth-from-va-ico-only.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\regulators\intl-bis.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\regulators\intl-fsb.yaml` — 고립 노드 (엣지 0개, 피참조 0회)
- `C:\Users\강성준\Desktop\app\aml\kb\entities\regulators\intl-unsc.yaml` — 고립 노드 (엣지 0개, 피참조 0회)

### I-12 (1)

- `C:\Users\강성준\Desktop\app\aml\quality\rules\forbidden_terms.local.txt` — 금칙어 목록 파일 없음 — 조직명 검사 생략. 일반 패턴만 적용.

