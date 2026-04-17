# Key Concepts — AML 핵심 용어 정리

> 외우기 전에 차이부터 잡고 가야 할 핵심 용어들. 마지막 업데이트: 2026-04-17.

## TL;DR
- **KYC ≠ CDD ≠ EDD** — 점점 강도가 세지는 동심원
- **KYC vs KYT** — KYC는 사람을 안다, KYT는 거래/지갑을 안다 (가상자산 특화)
- **STR vs CTR** — STR은 의심거래, CTR은 임계금액 초과 현금거래
- **AMLO / MLRO / CCO** — AML 책임자, 회사 안에 반드시 있어야 하는 직책
- **PEP** — 정치적 주요인물, 자동으로 EDD 대상

---

## 1. 고객 식별 / 실사 라인 (KYC / CDD / EDD)

세 용어가 같은 듯 다름. 동심원 구조로 이해:

```
┌─────────────────────────────────────┐
│ KYC (Know Your Customer)            │  ← 가장 큰 우산 개념
│ ┌─────────────────────────────────┐ │
│ │ CDD (Customer Due Diligence)    │ │  ← 표준 실사
│ │ ┌─────────────────────────────┐ │ │
│ │ │ EDD (Enhanced DD)           │ │ │  ← 고위험 고객에게만
│ │ └─────────────────────────────┘ │ │
│ │ SDD (Simplified DD)             │ │  ← 저위험에게만
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

### KYC (Know Your Customer)
- **고객확인** — "이 사람이 정말 본인이 맞는가" 를 확인하는 광범위 개념
- 신분증, 주소증빙, 셀카 + 신분증 (Liveness Check) 등
- 가상자산 거래소 가입 시 하는 그것

### CDD (Customer Due Diligence)
- **고객실사** — KYC를 한 다음 그 고객의 **위험을 평가하고 지속 모니터링** 하는 과정
- 4단계: ① 신원확인 ② 실소유자(Beneficial Owner) 확인 ③ 거래목적 파악 ④ 지속 모니터링
- 모든 고객에게 적용

### EDD (Enhanced Due Diligence)
- **강화된 고객실사** — 고위험 고객에게만 추가로 적용
- 트리거: PEP, 고위험국 거주, 비대면, 거액 거래, 복잡한 소유구조, 현금 집약 사업 등
- 추가 절차: 자금출처(Source of Funds) 증빙, 자산출처(Source of Wealth) 증빙, 고위경영진 승인, 더 빈번한 모니터링

### SDD (Simplified Due Diligence)
- **간소화된 실사** — 저위험 고객에게만 적용 가능 (정부기관, 상장기업 등)
- 한국 가상자산 분야는 사실상 거의 적용 안 됨

## 2. KYC vs KYT — 가상자산의 핵심 구분

| 구분 | KYC (Know Your Customer) | KYT (Know Your Transaction) |
|---|---|---|
| 대상 | **사람/법인** | **거래/지갑주소** |
| 시점 | 주로 onboarding 때 | **상시 (real-time)** |
| 데이터 | 신분증, 셀카, 주소 | 온체인 흐름, 클러스터, exposure |
| 도구 | Sumsub, Onfido, ARGOS | Chainalysis KYT, TRM, Elliptic Lens |
| 가상자산 특화 여부 | 전통 금융과 동일 | **가상자산 특화 (블록체인 분석)** |

KYT는 가상자산 산업에서 만들어진 개념. 본질적으로는 전통 금융의 **TM (Transaction Monitoring)** 의 가상자산 버전인데, **공개 원장을 활용한 외부 입출금 분석** 이 더해진다는 점에서 차별화.

## 3. 보고 의무 — STR / SAR / CTR

| 약어 | 풀이 | 트리거 | 한국에서 |
|---|---|---|---|
| **STR** | Suspicious Transaction Report | 의심스러운 거래 (금액 무관) | FIU에 보고 |
| **SAR** | Suspicious Activity Report (US 용어) | 위와 동일 (FinCEN 용어) | (미국 BSA) |
| **CTR** | Currency Transaction Report | **임계금액 초과 현금거래** (한국 1천만원, 미국 $10,000) | FIU에 보고 (자동) |
| **STR + SAR + CTR** | 통칭 "보고 의무" | | |

가상자산에서 **CTR은 적용 모호**함 (현금거래가 아니므로). 실무에서는 STR이 압도적으로 중요.

## 4. RBA — Risk-Based Approach (위험기반접근)

FATF가 2012년 권고 개정에서 명시화한 핵심 원칙:

> "고객/상품/거래/지역의 **위험 수준에 비례해서** AML 통제를 적용하라"

= 모든 고객을 똑같이 취급하지 말고, **고위험에는 EDD, 저위험에는 SDD** 식으로 자원을 배분하라는 것.

가상자산에서 RBA의 실질적 의미:
- 고객 risk score (KYC + 거래 패턴 + 지갑 노출) 자동 산정
- score ≥ threshold 이면 EDD trigger
- score 변화 시 재실사

## 5. PEP — Politically Exposed Person

**정치적 주요인물** = 고위 공직자, 그 가족, 그 측근.

분류:
- **Foreign PEP** (외국 PEP): 항상 EDD 대상
- **Domestic PEP** (국내 PEP): 위험기반 평가
- **International Org PEP** (국제기구 PEP): 위험기반 평가

PEP 자체가 범죄자라는 뜻이 아니라, **부패/뇌물에 노출될 위험이 구조적으로 높음** → 무조건 강화감시.

PEP 데이터베이스: World-Check (LSEG), Dow Jones Risk Center, ComplyAdvantage 등 상용 DB로 스크리닝.

## 6. Beneficial Owner (실소유자)

- **법인 고객의 실제 지배자/수익자** — 명의상 대표가 아니라 **실질 지배 25% 이상** 소유 자연인
- 한국 특금법: 25% 기준
- EU AMLR: 25% 기준 (논의 중 인하 가능성)
- **목적**: shell company를 통한 익명화 차단

## 7. Sanctions Screening (제재 스크리닝)

차단해야 할 명단과 매칭:

| 리스트 | 발행 |
|---|---|
| **OFAC SDN List** (Specially Designated Nationals) | 미국 재무부 OFAC |
| **UN Consolidated Sanctions List** | UN 안보리 |
| **EU Consolidated Financial Sanctions** | EU |
| **HM Treasury Sanctions List** | 영국 |
| **한국 외교부 제재대상자** | 한국 |

가상자산 추가:
- **OFAC SDN의 가상자산 지갑 주소** — Lazarus 관련, Tornado Cash 관련 (2022) 등
- 거래 발생 전 송신/수신 주소를 모두 스크리닝

## 8. AMLO / MLRO / CCO — AML 책임자

| 약어 | 풀이 | 비고 |
|---|---|---|
| **AMLO** | Anti-Money Laundering Officer | 일반 명칭 |
| **MLRO** | Money Laundering Reporting Officer | 영국/EU 명칭, STR 보고 책임자 |
| **CCO** | Chief Compliance Officer | 컴플라이언스 총괄 |
| **DMLRO** | Deputy MLRO | 부책임자 |

한국 특금법은 "**자금세탁방지 보고책임자**" 임명을 의무화. 임원급이어야 함.

## 9. Three Lines of Defense (3중 방어선)

은행/VASP 내부 통제 모델:

1. **1선 (Business / Frontline)**: 영업 부서 — 고객 응대, KYC 1차 수행
2. **2선 (Compliance / Risk)**: 컴플라이언스 팀 — 정책 수립, TM 운영, STR 신고, 모니터링
3. **3선 (Internal Audit)**: 내부감사 — 1선/2선이 제대로 돌아가는지 독립 검증

규제당국 검사 시 이 3중 구조의 실효성을 본다.

## 10. 자주 헷갈리는 짝

| A | B | 차이 |
|---|---|---|
| **AML** vs **CFT** | 자금세탁방지 vs 테러자금조달방지 | ML은 사후, TF는 사전 |
| **KYC** vs **CDD** | 신원확인 vs 종합실사 | CDD가 더 큰 개념 |
| **CDD** vs **EDD** | 표준 vs 강화 | EDD = 고위험 추가 |
| **KYC** vs **KYT** | 사람 vs 거래/지갑 | KYT = 가상자산 특화 |
| **STR** vs **CTR** | 의심거래 vs 임계초과 현금 | 가상자산은 STR 위주 |
| **VASP** vs **CASP** | 글로벌/한국 용어 vs EU 용어 | 본질 동일 |
| **FATF** vs **FIU** | 국제 표준제정자 vs 각국 실행기관 | FATF는 권고, FIU는 집행 |
| **AMLR** vs **AMLD** | EU 규정(직접효력) vs EU 지침(국내법화 필요) | AMLR이 더 강함 |

## 더 읽을거리
- [`what_is_aml.md`](what_is_aml.md) — AML 기초 3단계 모델
- [`../04_compliance_ops/cdd_edd.md`](../04_compliance_ops/cdd_edd.md) — CDD/EDD 실무
- [`../07_glossary/terms.md`](../07_glossary/terms.md) — 전체 용어 사전
