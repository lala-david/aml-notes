# EU — MiCA, AMLR/AMLD6, TFR

> EU의 가상자산 규제 3종 세트: MiCA(시장규제) + AMLR/AMLD6(AML) + TFR(Travel Rule). 마지막 업데이트: 2026-04-17.

## TL;DR
- **MiCA** (Markets in Crypto-Assets Regulation) — 가상자산 시장 통합 규제. **2024-12-30 전면 시행**
- **2026-07-01**: grandfathering 종료 — 모든 CASP는 라이센스 획득 의무
- **AMLR + AMLD6** (AML 패키지) — **2027-07-10 적용**, EU 27개국 단일 규칙
- **TFR** (Transfer of Funds Regulation) — EU판 Travel Rule, **임계금액 없음 (모든 거래)**
- 신규 감독기구 **AMLA** (EU AML Authority) 설립, 2025년부터 본격 운영
- **CASP** = Crypto-Asset Service Provider (≈ 한국 VASP)

---

## 1. EU 가상자산 규제 3종 세트

| 법령 | 정체성 | 발효 |
|---|---|---|
| **MiCA** | 가상자산 **시장 규제** (라이센스, 발행, 거래) | 2024-12-30 |
| **AMLR** (AML Regulation) | AML **단일 규칙** (회원국 직접 적용) | 2027-07-10 |
| **AMLD6** (6th AML Directive) | AML **지침** (회원국 국내법화) | 2027-07-10 |
| **TFR** | EU **Travel Rule** | 2024-12-30 (MiCA와 동시) |

= 한국으로 치면 (가상자산이용자보호법 + 특금법 + 트래블룰)에 해당.

## 2. MiCA — Markets in Crypto-Assets Regulation

### 정체성
- **EU 최초의 통합 가상자산 규제** (Regulation = 회원국 직접 적용, 국내법 변환 불필요)
- 2023-06 채택, **2024-12-30 전면 시행**

### 적용 대상: CASP
- **CASP = Crypto-Asset Service Provider** = VASP의 EU 버전
- 다음 중 하나 이상을 영업으로 하면 CASP:
  1. 자산의 **수탁/관리** (custody)
  2. **거래소** 운영
  3. **주문 집행/매칭**
  4. **포트폴리오 관리**
  5. **이전 서비스**
  6. **자문**
  7. **인수/배치**

### 토큰 분류
MiCA는 토큰을 3개 카테고리로:
1. **ART** (Asset-Referenced Token) — 여러 통화/자산 바스켓 페그
2. **EMT** (E-Money Token) — 단일 fiat 페그 (USDC, USDT 같은 스테이블코인)
3. **Other Crypto-Assets** — 위 2개를 제외한 모든 것 (BTC, ETH, NFT 일부 제외 등)

→ **ART와 EMT는 발행 라이센스 의무** (CASP와 별도)

### 라이센스
- 회원국 NCA(National Competent Authority)에서 발급
- **EU passporting**: 한 국가에서 받으면 27개국 영업 가능
- 발급 요건: 자본금, 거버넌스, 내부통제, AML 정책

### Grandfathering (전환기간)
- 기존 사업자는 **2026-07-01 까지** 또는 **라이센스 획득/거부 결정시까지** 종전 라이센스로 영업 가능
- 회원국별 길이 다름 (최대 18개월)
- → **2026-07-01 이후 모든 EU CASP는 MiCA 라이센스 보유**

### 2026 전환점
- 2026년부터 **NCA가 onboarding → active supervision으로 전환**
- 형식적 라이센스 시대 → 실효성 검사 시대

## 3. TFR — Travel Rule (EU 버전)

### 정체성
- **Regulation (EU) 2023/1113** — Transfer of Funds Regulation 개정안
- MiCA와 같은 패키지로 통과, **2024-12-30 시행**

### EU TFR의 특이점
- **임계금액 없음** — **모든 가상자산 이전에 적용** (FATF 1,000 EUR, 한국 100만원과 다름)
- **unhosted wallet** (개인지갑) 거래도 적용:
  - 1,000 EUR 초과 시 — **고객 신원 + 지갑 소유 검증** 의무
  - 단, 미국과 달리 unhosted wallet 자체를 금지하지는 않음
- **Originator + Beneficiary 모두 정보 필요**

### Travel Rule 정보 (TFR)
- 송신인: 이름, 주소, 계좌번호/지갑주소, 신원확인번호 또는 출생지/생년월일
- 수신인: 이름, 계좌번호/지갑주소

### CASP 의무
- 상대 CASP가 미준수 시 **반복 위반자 차단/거절**
- AMLA에 보고

## 4. AMLR + AMLD6 (AML 패키지)

### 패키지 구성 (2024년 입법)
1. **AMLR** (Regulation) — 단일 규칙, 직접 적용
2. **AMLD6** (Directive) — 보완 지침
3. **AMLA Regulation** — EU AML Authority 설립

### 적용 일정
- **2027-07-10 본격 적용**
- AMLD5 + 회원국 국내법 → AMLR + AMLD6로 통합

### 주요 변화
- **27개국 단일 규칙** — 종전엔 각국마다 차이가 있었음
- **현금거래 한도 €10,000 EU 전체 적용**
- **CASP를 명시적으로 포함** (의무자 목록에 등재)
- **EDD 트리거 강화** — 고위험국, 비대면, 복잡한 구조 등

### CASP에 적용되는 AMLR 의무
- KYC + 실소유자 확인 (25% 기준)
- CDD/EDD
- 거래 모니터링
- STR (FIU 보고)
- 기록보관
- 내부통제 + AMLO 임명
- **TFR 준수**

## 5. AMLA — EU AML Authority

- **신규 설립**: 2024년 EU 법으로 설립
- **본부**: 프랑크푸르트
- **본격 운영**: 2025년 시작, 2028년경 직접 감독 개시 예정
- **역할**:
  - EU 차원의 AML 룰북 단일 해석
  - 가장 위험한 40여 개 cross-border 금융기관 **직접 감독**
  - 회원국 NCA 조정
  - FIU 협력 강화

→ EU 단일 시장에서 **AML 분절성 해소**가 목적.

## 6. EU vs 한국 vs 미국 — 가상자산 AML 비교

| 항목 | EU | 한국 | 미국 |
|---|---|---|---|
| 시장규제 | MiCA | 가상자산이용자보호법 | (조각) SEC/CFTC |
| AML | AMLR + AMLD6 | 특금법 | BSA + USA PATRIOT |
| Travel Rule 임계 | **없음 (모든 거래)** | **100만원** | **$3,000** |
| Unhosted wallet | 1,000 EUR+ 신원검증 | 외부지갑 등록제 (자율) | 명시 룰 부재 |
| 단일 라이센스 | ✅ EU passporting | (한국 단일) | ❌ 주별 |
| 감독기구 (AML) | AMLA + NCA | FIU | FinCEN + OFAC |
| 스테이블코인 | EMT (MiCA) | 2단계 입법 예정 | GENIUS Act |

## 7. 한국 사업자가 EU 진출 시 체크

```
□ MiCA CASP 라이센스 (EU 회원국 1개에서)
□ EU passporting 활용 계획
□ AMLR 컴플라이언스 프로그램
□ TFR 솔루션 연동 (Notabene, Sumsub 등)
□ ART/EMT 발행 시 별도 라이센스
□ AMLA 직접 감독 대상 여부 검토 (대형사만)
□ unhosted wallet 1,000 EUR+ 신원검증 절차
□ EU GDPR + AML 기록보관 충돌 관리
```

## 8. 주요 시점 정리

| 시점 | 사건 |
|---|---|
| 2020-09 | EU Commission, MiCA 초안 공개 |
| 2023-06 | MiCA 채택 + TFR 채택 |
| 2024-06-30 | MiCA — ART/EMT 부분 시행 |
| **2024-12-30** | **MiCA + TFR 전면 시행** |
| 2025 | AMLA 본격 운영 시작 |
| **2026-07-01** | **MiCA grandfathering 종료** |
| **2027-07-10** | **AMLR + AMLD6 적용** |
| 2028~ | AMLA 직접 감독 개시 |

## 더 읽을거리
- [`global_fatf.md`](global_fatf.md) — FATF 권고와의 관계
- [`korea_fiu_act.md`](korea_fiu_act.md) — 한국과 비교
- [`../notes/7-vendors/travel-rule-vendors.md`](../notes/7-vendors/travel-rule-vendors.md) — TFR 솔루션
- [ESMA — MiCA 페이지](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)
- [Jones Day — MiCA + AMLR 분석](https://www.jonesday.com/en/insights/2025/07/crypto-assets-casps-and-amlcft-compliance-the-new-european-regulatory-landscape-under-mica-and-amlr)
- [Sumsub — MiCA 2026 가이드](https://sumsub.com/blog/crypto-regulations-in-the-european-union-markets-in-crypto-assets-mica/)
- [VinciWorks — 2026 EU crypto law outlook](https://vinciworks.com/blog/what-to-expect-in-2026-for-crypto-law-and-policy/)
