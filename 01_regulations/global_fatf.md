# FATF — 국제 자금세탁방지 표준

> Financial Action Task Force, 가상자산 AML의 모든 룰의 출발점. 마지막 업데이트: 2026-04-17.

## TL;DR
- FATF는 1989년 G7이 설립한 정부간 기구. **법은 안 만들고 권고(Recommendation)** 발표
- 회원국은 권고를 국내법으로 도입 → **상호평가**로 점수 매김 → 낮으면 **Grey/Black List**
- 가상자산 핵심 권고: **R.15** (VASP에 AML/CFT 부과), **R.16** (Travel Rule)
- 한국은 FATF 회원국 + APG 회원 → 권고 미이행 시 직접 페널티
- **2025-06-18, R.16 개정** → 2030년 말 발효, VASP는 별도 tailored framework로 적용
- **2026 후반에 가이던스 발표 예정**

---

## 1. FATF 기본 구조

| 항목 | 내용 |
|---|---|
| 설립 | 1989년 (G7 파리정상회의) |
| 본부 | 파리 (OECD 내 사무국) |
| 회원국 | 39개 (한국 포함) + 2개 지역기구 (EU, GCC) |
| 한국 가입 | 2009년 |
| 역할 | AML/CFT/CPF 국제 표준 설정 + 회원국 평가 + 비협력국 식별 |

## 2. FATF 40 Recommendations

40개 권고로 구성. 가상자산 관련 핵심:

### Recommendation 15 — New Technologies
- 신기술(가상자산 포함)에서 발생하는 ML/TF 위험을 평가하고 관리할 의무
- **2018년 개정**: 가상자산(VA)과 가상자산사업자(VASP)를 명시적으로 포함
- VASP는 AML/CFT 의무를 다른 금융기관과 동일하게 부담

### Recommendation 16 — Wire Transfers (Travel Rule)
- 송금 시 **송신인/수신인 정보를 함께 동반(travel)** 해야 한다는 룰
- **2019년 개정 (Travel Rule을 가상자산까지 확장)**: VASP 간 가상자산 이전에도 적용
- **2025-06-18 개정**: 결제 산업 변화 반영, 2030년 말 발효
- VASP는 직접이 아닌 **별도 tailored framework** 로 적용

### Recommendation 1 — Risk-Based Approach
- **위험기반접근(RBA)** — 모든 AML 의무의 운영 원칙

### Recommendation 10~12 — Customer Due Diligence
- CDD, EDD, PEP에 대한 표준

### Recommendation 20 — STR
- 의심거래 보고 의무

### Recommendation 22 — DNFBPs
- 비금융전문가(변호사, 회계사, 부동산, 카지노, 귀금속상)에 대한 AML 의무

## 3. VASP 정의 (FATF Glossary)

> A **virtual asset service provider** is any natural or legal person who, as a business, conducts one or more of the following activities for or on behalf of another natural or legal person:
> 1. Exchange between virtual assets and fiat currencies
> 2. Exchange between one or more forms of virtual assets
> 3. Transfer of virtual assets
> 4. Safekeeping and/or administration of virtual assets
> 5. Participation in and provision of financial services related to an issuer's offer and/or sale of a virtual asset

→ 한국 특금법의 VASP 정의와 사실상 동일.

## 4. Travel Rule (R.16) 핵심 요건

VASP가 다른 VASP에게 가상자산을 이전할 때, **임계금액(threshold) 이상이면** 다음 정보를 함께 전달:

**송신인(Originator):**
- 이름
- 계좌번호 또는 가상자산 주소
- 주소, 신원확인번호(국가식별번호 등) 또는 출생지/생년월일

**수신인(Beneficiary):**
- 이름
- 계좌번호 또는 가상자산 주소

**임계금액:**
- FATF 권고: **USD/EUR 1,000** (각국 자율 결정)
- 한국: **100만원** (특금법)
- 미국: **$3,000** (FinCEN)
- EU TFR: **임계금액 없음 (모든 거래)**

수신 측 VASP는 받은 정보를 검증하고, **누락/이상 시 보류 또는 거절** 가능.

## 5. 2025-06-18 R.16 개정의 의미

**왜 개정했나:**
- 결제 산업 변화 (실시간 결제, ISO 20022, 새로운 사업자, 메시징 표준)
- 기존 R.16이 SWIFT 시대 기준이라 안 맞는 부분 발생

**핵심 변화:**
- 메시징 표준 명확화
- VASP는 **별도 tailored framework** 로 적용 (Virtual Asset Contact Group이 작업)
- 가이던스 **2026 후반** 발표 예정

**일정:**
- 발효: **2030년 말**
- 각국이 그 전까지 국내법화

→ 한국도 이에 맞춰 특금법 + 시행령 추가 개정 예상.

## 6. 상호평가 (Mutual Evaluation, ME)

FATF가 회원국의 AML/CFT 이행을 평가하는 메커니즘.

**평가 항목 두 축:**
1. **Technical Compliance** — 법/규제가 권고와 일치하는가
2. **Effectiveness** — 실제로 작동하는가 (11개 Immediate Outcome)

**점수 등급:**
- **C** (Compliant) / **LC** (Largely Compliant) / **PC** (Partially Compliant) / **NC** (Non-Compliant)

**한국 ME 결과** (4차 라운드, 2020년):
- 전반적으로 양호하나 **VASP/가상자산 영역 약점** 지적 → 이후 특금법 개정의 동인

## 7. Grey List / Black List

| 리스트 | 의미 |
|---|---|
| **Black List (High-Risk Jurisdictions)** | 강화된 대응조치 (counter-measures) 적용 — 북한, 이란, 미얀마(2026 기준) |
| **Grey List (Increased Monitoring)** | 강화 모니터링 — 베트남, UAE는 빠짐, 케냐/나미비아/필리핀 등 (수시 변경) |

→ 이 리스트의 국가/관할권 고객은 자동으로 **EDD 대상 + 거래 제한** 검토.

## 8. FATF의 "Sunrise Issue" (가상자산 특화)

- VASP A국이 Travel Rule을 시행했는데, B국은 아직 안 했음
- A국 VASP가 B국 VASP에게 송금하려는데, B국 VASP는 메시징 받을 인프라가 없음
- → **글로벌 동시 적용이 안 되어 발생하는 호환성 공백**
- 해결책: Notabene Gateway, VerifyVASP 같은 멀티프로토콜 게이트웨이

## 9. FATF 발간물 (가상자산 관련 필수 문서)

| 문서 | 발행 |
|---|---|
| **Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs** | 2021-10 |
| **Targeted Update on Implementation of FATF Standards on VAs and VASPs** | 매년 발간 (가장 최근 2025) |
| **Best Practices on Travel Rule Supervision** | 2026-06-26 |
| **Explanatory Note for Revised R.16** | 2025-06 |

## 10. 그래서 회사 차원에서 뭘 해야 하나

수탁업자/거래소/Travel Rule 솔루션 회사 관점에서:

1. **R.15 + R.16 영문 원문**을 한 번 읽어둘 것
2. 한국이 **상호평가**에서 어떻게 평가받는지 추적 → 다음 평가 사이클에서 VASP 영역 더 본다
3. **2025-06 R.16 개정**의 영향 모니터링 — 2026 후반 가이던스 발표를 trigger로 내부 정책 업데이트
4. **Sunrise Issue** 대응 — 카운터파티 VASP의 Travel Rule 솔루션 호환성 점검

## 더 읽을거리
- [`korea_fiu_act.md`](korea_fiu_act.md) — 특금법이 FATF를 어떻게 반영했는지
- [`../02_crypto_aml/travel_rule.md`](../02_crypto_aml/travel_rule.md) — Travel Rule 운영 상세
- [FATF — Virtual Assets](https://www.fatf-gafi.org/en/topics/virtual-assets.html)
- [FATF — Recommendations 원문](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html)
- [FATF — 2025 Targeted Update on VAs and VASPs](https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2025-Targeted-Upate-VA-VASPs.pdf.coredownload.pdf)
- [FATF — Updated R.16 Explanatory Note](https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Explanatory%20note%20for%20revised%20R.16.pdf.coredownload.pdf)
