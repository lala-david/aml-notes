# AML Study — 가상자산/온체인 자금세탁방지 학습 노트

> 가상자산/온체인 업계 종사자를 위한 AML 자율 학습 노트.
> 시작: 2026-04-17

---

## 1. 학습 로드맵

가상자산 업계에서 AML을 0부터 배우는 사람을 위한 권장 순서:

1. **`00_overview/`** — AML이 뭔가? 왜 가상자산은 다른가? 핵심 용어 (KYC/KYT/CDD/EDD/STR/CTR)
2. **`01_regulations/`** — 누가 뭘 시키는가
   - 한국 (특금법, 가상자산이용자보호법) → FATF → US (BSA/FinCEN/OFAC) → EU (MiCA/AMLR) 순
3. **`02_crypto_aml/`** — 가상자산 특화: VASP 의무, Travel Rule, 온체인 자금세탁 유형
4. **`03_technology/`** — KYC/KYT, 블록체인 분석, Travel Rule 프로토콜
5. **`04_compliance_ops/`** — 실제 운영: CDD/EDD, STR/CTR, 제재 스크리닝
6. **`05_solutions_market/`** — 시장에 나와 있는 솔루션과 벤더 지도
7. **`06_cases_typologies/`** — 실제 사례 (라자루스, Tornado Cash, 주요 enforcement)
8. **`07_glossary/`** — 용어 사전
9. **`references/`** — 원문 링크 / 추가 학습 자료

---

## 2. 디렉토리 규칙

```
aml/
├── README.md                       # 이 문서. 마스터 인덱스.
├── 00_overview/                    # 두 자리 prefix는 학습 순서를 의미
├── 01_regulations/
│   └── README.md                   # 하위 주제 인덱스가 있으면 README.md 추가
├── 02_crypto_aml/
├── 03_technology/
├── 04_compliance_ops/
├── 05_solutions_market/
├── 06_cases_typologies/
├── 07_glossary/
└── references/
```

**파일 네이밍**
- 영문 snake_case (`korea_fiu_act.md`, `travel_rule.md`)
- 한국 관련은 `korea_` prefix, 글로벌은 `global_`, 미국 `us_`, EU `eu_`
- 사례 파일은 `사건명_주체.md` (`lazarus_dprk.md`, `tornado_cash.md`)
- 한글 파일명 금지 (Windows 인코딩 이슈 + git diff 가독성)

**파일 내용 규칙**
- 본문은 **한국어**, 법/기술 용어는 영문 병기 (예: 자금세탁방지(AML), 고객확인(KYC))
- 문서 상단에 **한 줄 요약 + 출처 링크 + 마지막 업데이트 날짜**
- 사실 주장에는 **출처 URL + 발행일** 표기 (규제는 빠르게 변함)
- "현재"/"최근" 같은 상대 표현 금지 → "2026년 4월 기준" 으로 명시
- 각 파일 하단에 **`## 더 읽을거리`** 섹션으로 관련 문서/링크 정리

**문서 구조 권장**
```markdown
# 제목

> 한 줄 요약. 마지막 업데이트: YYYY-MM-DD.

## TL;DR
- 3~5개 bullet

## 본문 섹션들...

## 더 읽을거리
- [링크 제목](url) — 한 줄 설명
```

---

## 3. 적용 영역별 학습 우선순위

가상자산 업계의 주요 사업 유형별로 무엇을 더 봐야 하는가:

| 사업 유형 | 우선 학습 영역 |
|---|---|
| **가상자산 거래소** | VASP 의무 풀스택 + Travel Rule + 시세조종 규제 |
| **수탁업 (custody)** | 자기/고객자산 분리 + KYT (출금 주소) + 보안/MPC |
| **온체인 분석/솔루션** | 블록체인 분석 기법 + attribution + cross-chain |
| **결제 PG** | 가맹점 KYC + 실시간 거래 모니터링 + Travel Rule |
| **OTC desk** | EDD + STR + 거액 거래 모니터링 |

→ **VASP 컴플라이언스 + 온체인 분석 + Travel Rule 솔루션** 이 한국 시장의 핵심 학습 영역.

---

## 4. 우선순위 Top 5 (시간 없을 때)

먼저 봐야 할 5개 문서:

1. [`00_overview/what_is_aml.md`](00_overview/what_is_aml.md) — 자금세탁의 3단계 (Placement → Layering → Integration)
2. [`01_regulations/korea_fiu_act.md`](01_regulations/korea_fiu_act.md) — 특금법, 우리 회사들이 직접 적용받는 법
3. [`02_crypto_aml/travel_rule.md`](02_crypto_aml/travel_rule.md) — Travel Rule (FATF R.16), 가장 핫한 운영 이슈
4. [`02_crypto_aml/onchain_typology.md`](02_crypto_aml/onchain_typology.md) — 믹서/체인호핑/peel chain 등 자금세탁 패턴
5. [`06_cases_typologies/lazarus_dprk.md`](06_cases_typologies/lazarus_dprk.md) — Bybit $1.5B 해킹, 업계 1순위 위협 행위자

---

## 5. 주요 약어 빠른 참조

| 약어 | 풀이 |
|---|---|
| AML | Anti-Money Laundering, 자금세탁방지 |
| CFT | Combating the Financing of Terrorism, 테러자금조달방지 |
| KYC | Know Your Customer, 고객확인 |
| KYT | Know Your Transaction, 거래확인 (블록체인 분석 기반) |
| CDD / EDD | Customer Due Diligence / Enhanced DD, 고객실사/강화실사 |
| STR / CTR | Suspicious / Currency Transaction Report, 의심거래/고액현금거래 보고 |
| VASP | Virtual Asset Service Provider, 가상자산사업자 |
| CASP | Crypto-Asset Service Provider (EU MiCA 용어, ≈ VASP) |
| FATF | Financial Action Task Force, 국제자금세탁방지기구 |
| FIU | Financial Intelligence Unit, 금융정보분석원 (한국) |
| FinCEN | Financial Crimes Enforcement Network (미국 FIU) |
| OFAC | Office of Foreign Assets Control (미국 제재 당국) |
| MiCA | Markets in Crypto-Assets Regulation (EU) |
| AMLR | EU AML Regulation |
| BSA | Bank Secrecy Act (미국 1970) |
| IVMS101 | InterVASP Messaging Standard 101 (Travel Rule 메시지 표준) |
| TFR | Transfer of Funds Regulation (EU Travel Rule) |

전체 용어는 [`07_glossary/terms.md`](07_glossary/terms.md) 참고.

---

## 6. 진척도

| 영역 | 상태 |
|---|---|
| 00_overview | 초안 완료 |
| 01_regulations | 초안 완료 (한국/FATF/US/EU) |
| 02_crypto_aml | 초안 완료 |
| 03_technology | 초안 완료 |
| 04_compliance_ops | 초안 완료 |
| 05_solutions_market | 초안 완료 |
| 06_cases_typologies | 초안 완료 |
| 07_glossary | 초안 완료 |
| references | 초안 완료 |

> **Note:** 모든 문서는 **2026년 4월 17일 기준**의 1차 초안. 정확성/최신성은 원문(법령정보센터, FATF, FSC, ESMA 등) 재확인 필수.
