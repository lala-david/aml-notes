# 미국 — BSA, FinCEN, OFAC

> 미국 가상자산 AML 체계: BSA → FinCEN(자금세탁) + OFAC(제재) → GENIUS Act(스테이블코인). 마지막 업데이트: 2026-04-17.

## TL;DR
- **BSA (Bank Secrecy Act, 1970)** — 미국 AML의 모법. 2001 USA PATRIOT Act로 강화
- **FinCEN** — 미국 FIU. 가상자산은 **MSB (Money Services Business)** 로 등록 의무
- **OFAC** — 제재 집행 기관. **SDN List에 가상자산 지갑주소 등재** (Lazarus, Tornado Cash 등)
- **2025-07 GENIUS Act** — 스테이블코인을 BSA 적용 대상으로 명시
- **2026-04-08** FinCEN+OFAC 합동 제안 → 시행규정 **2026-07-18 마감**, 전면 시행 **2027-01-18**
- 2025년 강력한 enforcement: **OKX $500M+ DOJ 합의, Paxful $3.5M FinCEN 벌금**

---

## 1. BSA — 미국 AML의 토대

| 항목 | 내용 |
|---|---|
| 제정 | 1970 (Bank Secrecy Act = Currency and Foreign Transactions Reporting Act) |
| 핵심 의무 | CTR ($10,000+), SAR (의심거래), 기록보관, AML 프로그램 운영 |
| 2001 PATRIOT Act | KYC + EDD + 외국 PEP + 환거래은행 |
| 적용 | 은행 + MSB + 증권회사 + 카지노 + 선물중개업자 + (가상자산) |

## 2. FinCEN

- **풀이**: Financial Crimes Enforcement Network
- **소속**: 미국 재무부
- **역할**: BSA 시행, SAR/CTR 수집·분석, 정책 발표, MSB 등록 관리

### 가상자산 = MSB
- 2013년 FinCEN 가이던스: **가상통화 administrator/exchanger는 MSB**
- MSB 등록 → AML 프로그램 + SAR + 기록보관 의무
- 거래소뿐 아니라 mixer, wallet provider도 해당될 수 있음

### Travel Rule (FinCEN 버전)
- BSA Travel Rule (1996년부터): **$3,000 이상** 송금 시 송수신인 정보 동반
- 가상자산에도 적용 (2019년 재확인)
- FATF 권고($1,000)보다 임계금액이 높음

### 주요 FinCEN 가이던스
- 2013-03-18: 가상통화 가이던스 (FIN-2013-G001)
- 2019-05-09: CVC(Convertible Virtual Currency) 모델 가이던스
- 2020-10-23: Travel Rule 가상자산 적용 명확화 제안
- 2024-2025: Mixer 관련 정보수집 명령

## 3. OFAC

- **풀이**: Office of Foreign Assets Control
- **소속**: 미국 재무부
- **역할**: 경제·무역 제재 집행 (이란/북한/러시아/베네수엘라 등 + 테러조직 + 마약카르텔)

### SDN List (Specially Designated Nationals)
- 거래 금지 대상자 명단
- **가상자산 지갑주소도 등재** — 거래 시 미국법 위반

### 가상자산 SDN 사례 (시간순)
| 연도 | 대상 | 비고 |
|---|---|---|
| 2018 | 이란 비트코인 주소 (Marinov, Khorashadizadeh) | OFAC 첫 가상자산 SDN |
| 2020 | 러시아 Lazarus 관련 주소 | DPRK 자금세탁 차단 |
| 2022-08 | **Tornado Cash 스마트컨트랙트** | DeFi 첫 제재, 큰 논쟁 |
| 2022-11 | Hydra Market | 다크넷 |
| 2024 | Garantex 추가 제재 | 러시아 거래소 |
| **2025-03-21** | **Tornado Cash 제재 해제** | 5th Circuit 패소 후 |

### Tornado Cash 제재의 의미
- 미국 첫 **스마트컨트랙트 자체 제재**
- 2024-11 5th Circuit: "**OFAC이 권한을 초과**했다, 컨트랙트는 'property'가 아니다" 판결
- 2025-03 OFAC이 제재 해제
- **DeFi 영역에서 OFAC의 한계가 드러난 사건** — 향후 입법으로 보완 시도

## 4. 주요 Enforcement 사례 (가상자산)

| 연도 | 대상 | 벌금 | 사유 |
|---|---|---|---|
| 2020 | BitMEX | $100M | KYC 미흡, AML 프로그램 결여 |
| 2021 | BitGo | $98K | OFAC 제재 위반 |
| 2022 | Bittrex | $29M | OFAC + FinCEN 결합 |
| 2023 | **Binance** | **$4.3B** | 역대 최대, AML/제재 복합 |
| 2023 | Kraken | $30M (SEC) | (등록 미신고) |
| 2024-2025 | **OKX** | **$500M+ DOJ** | KYC 약함, 수십억 의심거래 |
| 2025 | **Paxful** | **$3.5M FinCEN** | $500M 불법자금 처리 |

→ **BSA 위반 + 제재 위반 결합 처벌**이 트렌드. CCO 개인 처벌도 증가.

## 5. GENIUS Act (2025-07 통과)

- **풀이**: Generating Innovation in Unified Stablecoins Act (가칭, 정확한 명칭 확인 필요)
- 의미: **payment stablecoin을 BSA 적용 대상으로 공식화**
- 발행자 의무:
  - AML 프로그램
  - KYC + CDD
  - 거래 모니터링
  - SAR 보고
  - **OFAC 스크리닝**
  - **freeze, burn, reject 능력 의무화** — 스마트컨트랙트 레벨에서 제재 대상 거래 차단

### 시행 일정
- **2026-07-18**: 시행규정(implementing regulations) 발표 마감
- **2027-01-18**: 전면 enforcement 시작

### 2026-04-08 FinCEN + OFAC 합동 제안
- 스테이블코인 발행자가 BSA + 제재 의무 이행하는 구체적 방법 제안
- 1차 시장(발행/상환)뿐 아니라 **2차 시장(거래)** 까지 컴플라이언스 책임 확장

→ Tether, Circle 같은 발행자에게 큰 영향. 한국에 진출한 USDC/USDT 사용 시에도 freeze 정책 영향.

## 6. 미국 외부 영향력 (역외 적용)

미국은 다음 leverage로 사실상 글로벌 적용:

1. **USD 결제망** — 환거래 은행을 통해 모든 달러 거래에 영향력
2. **OFAC 2차 제재** — 미국인이 아니어도 SDN과 거래하면 미국 시장 접근 차단
3. **Cloud/Infra 의존도** — AWS, Cloudflare, Github 등이 OFAC 준수
4. **달러화 스테이블코인 (USDC, USDT)** — 발행자가 미국 OFAC 준수 의무

→ 한국 VASP도 미국 룰을 사실상 따라야 하는 이유.

## 7. SEC vs CFTC vs FinCEN — 미국의 분절된 가상자산 규제

미국은 가상자산을 한 기관이 다 못 봄:

| 기관 | 시각 | 다루는 것 |
|---|---|---|
| **SEC** | "대부분 증권" | 토큰 발행, 거래소 등록 |
| **CFTC** | "BTC/ETH는 상품" | 파생상품, 시장 조작 |
| **FinCEN** | "AML 의무자" | MSB 등록, SAR |
| **OFAC** | "제재 집행" | SDN 차단 |
| **OCC** | "은행 감독" | 은행의 가상자산 사업 |
| **IRS** | "세무" | 자산으로 과세 |

→ 한 사업자가 4~5개 기관에 동시 대응. 한국의 (FIU + 금융위/금감원) 단순함과 대비.

## 8. 한국 사업자가 알아야 할 미국 룰

| 상황 | 적용 |
|---|---|
| 한국에서만 영업 | 직접 적용 X, 단 OFAC 제재는 항시 의식 |
| 미국 고객 받음 | **MSB 등록 + 주별 Money Transmitter License** |
| USD 결제망 사용 | OFAC 준수 (사실상 모든 달러 거래) |
| USDC/USDT 사용 | 발행자가 OFAC 따름 → freeze 가능성 |
| 라자루스 의심 거래 | 미국 사법공조 요청 가능성 |

## 더 읽을거리
- [`korea_fiu_act.md`](korea_fiu_act.md) — 한국 특금법과 비교
- [`global_fatf.md`](global_fatf.md) — FATF가 미국에 어떻게 평가받는지
- [`../notes/6-cases/tornado-cash.md`](../notes/6-cases/tornado-cash.md) — Tornado Cash 제재 상세
- [FinCEN 공식 사이트](https://www.fincen.gov/)
- [OFAC SDN List 검색](https://sanctionssearch.ofac.treas.gov/)
- [Treasury — Tornado Cash 제재 보도자료 (2022)](https://home.treasury.gov/news/press-releases/jy0916)
- [PwC — FinCEN AML overhaul (2026-04)](https://www.pwc.com/us/en/industries/financial-services/library/our-take/fincen-proposes-aml-overhaul-apr-13-2026.html)
- [Latham — US Crypto Policy Tracker](https://www.lw.com/en/us-crypto-policy-tracker/regulatory-developments)
- [Grant Thornton — Crypto compliance 2026](https://www.grantthornton.com/insights/articles/banking/2026/crypto-compliance-in-2026)
