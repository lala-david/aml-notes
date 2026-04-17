# What is AML? — 자금세탁방지 기초

> 자금세탁(Money Laundering)이란 무엇이고, AML(Anti-Money Laundering)이 왜 존재하는가. 마지막 업데이트: 2026-04-17.

## TL;DR
- **자금세탁(ML)**: 범죄로 얻은 돈의 출처를 숨겨 합법적인 자금처럼 보이게 하는 행위
- **AML**: 그걸 막기 위한 법/제도/기술/운영의 총합. 짝꿍 개념으로 **CFT** (테러자금조달방지)가 있음
- 자금세탁은 전통적으로 **3단계 모델**: Placement → Layering → Integration
- 가상자산은 이 3단계가 다 **온체인**에서 일어날 수 있어서 추적은 쉬워졌지만 속도/규모가 폭증함
- AML 의무의 큰 줄기: **고객을 알고(KYC) → 거래를 모니터링하고(KYT/TM) → 의심되면 신고(STR)**

---

## 1. 자금세탁이 뭔가

자금세탁(Money Laundering, ML)은 마약·사기·뇌물·해킹·탈세 등 **범죄로 발생한 더러운 돈(dirty money)** 의 출처를 가려 **마치 합법적으로 번 돈인 것처럼** 보이게 만드는 일련의 과정.

목적은 단순:
1. **출처(origin)를 숨긴다** — 어디서 온 돈인지 모르게
2. **추적을 어렵게 한다** — 흐름을 끊는다
3. **합법 경제에 통합한다** — 합법적으로 쓸 수 있게

자금세탁이 막히면 범죄 수익화가 어려워지므로, AML은 단순 금융규제가 아니라 **마약/조직범죄/테러/사이버범죄/대량살상무기 확산 자체를 억제하는 수단**으로 다뤄짐.

## 2. 고전적 3단계 모델 (Placement → Layering → Integration)

FATF / UNODC가 표준으로 쓰는 모델.

### Stage 1. Placement (배치)
- **더러운 돈을 금융 시스템에 처음 집어넣는 단계**
- 예: 현금다발을 은행에 분할 입금(structuring/smurfing), 카지노 칩 구매 후 환전, 현금→가상자산 거래소 입금
- **가장 위험하고 가장 탐지하기 쉬운 단계** → AML의 1차 방어선이 여기 집중됨

### Stage 2. Layering (은닉)
- **여러 번의 거래를 통해 돈의 흐름을 복잡하게 만들어 추적을 끊는 단계**
- 예: 여러 계좌·국가·법인 간 송금, 가상자산이라면 mixer(믹서), chain hopping(체인호핑), peel chain, DeFi swap, NFT wash trading
- **가장 길고 창의적인 단계** — 온체인 분석 기술이 주로 이 단계 분석에 쓰임

### Stage 3. Integration (통합)
- **세탁된 돈이 합법 자산으로 다시 등장하는 단계**
- 예: 부동산 매입, 럭셔리 자산 구매, 합법 사업체 인수, 대출 상환, 가상자산이라면 OTC desk를 통한 법정화폐 환전
- 이 시점에서 잡히면 자산몰수가 어려움 → 그 전 단계에서 막는 게 핵심

> **핵심 통찰:** 가상자산에서는 이 3단계가 **모두 한 트랜잭션 안에 압축**되거나 **24시간 내 다 끝날 수도** 있음. 전통 금융 대비 속도가 압도적.

## 3. AML과 CFT의 관계

- **AML (Anti-Money Laundering)**: 범죄수익 → 합법자산 변환을 막음
- **CFT (Combating the Financing of Terrorism)**: 테러조직으로의 자금조달을 막음
- **CPF (Counter-Proliferation Financing)**: 대량살상무기 확산금융 차단

CFT는 ML과 정반대 방향임에 주의:
- **ML**: 더러운 돈 → 깨끗하게 (사후)
- **TF**: 합법 자금이라도 → 테러에 쓰이면 막아야 (사전)
- 그래서 출처가 합법이어도 **수취인/용도가 위험**하면 차단 — 제재(sanctions) 스크리닝이 핵심

세 가지를 묶어 흔히 **AML/CFT** 또는 **AML/CFT/CPF** 로 표기.

## 4. AML 의무의 큰 줄기 (어떤 회사든 비슷함)

가상자산사업자(VASP) 든 은행이든 결제사든, AML 의무의 뼈대는 같음:

1. **신고/등록(Licensing)** — 당국에 사업자 등록 (한국: FIU 신고)
2. **고객확인(KYC/CDD)** — 누구와 거래하는지 확인
3. **위험기반접근(RBA, Risk-Based Approach)** — 고객/상품/지역별 리스크 등급 매기고 그에 맞춰 통제
4. **강화실사(EDD)** — 고위험 고객(PEP, 고위험국, 비대면 등)에 추가 확인
5. **거래모니터링(TM/KYT)** — 비정상 거래 패턴 탐지
6. **제재 스크리닝(Sanctions Screening)** — OFAC/UN/EU 제재 대상 차단
7. **의심거래보고(STR/SAR)** — 의심되면 FIU에 신고
8. **기록보관(Record Keeping)** — 한국은 **15년** (가상자산이용자보호법)
9. **내부통제(Internal Controls)** — AML 책임자(AMLO/CO) 임명, 정책·교육·내부감사

위 9개는 어떤 AML 책에서도 반복 등장. 가상자산 특화 의무는 여기에 **Travel Rule**이 추가된다고 보면 됨.

## 5. 누가 만든 룰을 따르는가 (글로벌 거버넌스)

```
FATF (국제 표준 제정, 권고안 발표, 회원국 평가)
  └── 각국이 국내법으로 도입
        ├── 한국: 특금법, 가상자산이용자보호법 (감독: FIU/FSC)
        ├── 미국: BSA, USA PATRIOT Act (감독: FinCEN/OFAC)
        ├── EU: AMLD 시리즈 → AMLR + MiCA + TFR (감독: AMLA, ESMA, NCA)
        └── 일본/싱가포르/홍콩 등 각자 도입
```

**FATF는 법을 만드는 게 아니라 권고안(Recommendation)을 발표.** 회원국이 이를 국내법으로 도입하지 않으면 **상호평가(Mutual Evaluation)** 에서 낮은 점수를 받고 **FATF Grey/Black List**에 오를 수 있음 → 국가 신용도/은행 거래에 직접 타격.

가상자산에 대한 결정적 권고는:
- **FATF Recommendation 15** — VASP에 AML/CFT 의무 부과
- **FATF Recommendation 16** — Travel Rule (송수신인 정보 동반)

## 더 읽을거리
- [`why_crypto_aml.md`](why_crypto_aml.md) — 왜 가상자산은 다른가
- [`key_concepts.md`](key_concepts.md) — KYC/KYT/CDD/EDD/STR/CTR 정의
- [`../01_regulations/global_fatf.md`](../01_regulations/global_fatf.md) — FATF 권고안 상세
- [FATF — Money Laundering](https://www.fatf-gafi.org/en/topics/money-laundering.html)
- [UNODC — Money Laundering](https://www.unodc.org/unodc/en/money-laundering/overview.html)
