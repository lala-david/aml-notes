# Sanctions Screening — 제재 스크리닝

> 거래 전·중·후 모든 단계에서 제재 대상자 차단. 마지막 업데이트: 2026-04-17.

## TL;DR
- 핵심 리스트: **OFAC SDN (미국), UN Consolidated, EU CFSP, HM Treasury (영국), 한국 외교부**
- 가상자산 추가: **OFAC SDN의 가상자산 지갑주소** — 거래 전 실시간 차단 필수
- 매칭 방식: **이름(fuzzy) + 생년월일 + 국적 + 지갑주소 (정확매칭)**
- 사전 / 실시간 / 사후 모니터링 3중 체크
- 위반 시 형사처벌 + 거대 벌금 (Binance $4.3B 사례)

---

## 1. 제재의 종류

### 카테고리별
| 카테고리 | 예시 |
|---|---|
| **국가 제재** | 북한, 이란, 시리아, 쿠바, 베네수엘라, 미얀마 |
| **러시아 분리 제재** | 푸틴 측근, 올리가르히, 러시아 은행 (2022~) |
| **테러조직** | 알카에다, ISIS, Hamas, Hezbollah |
| **마약 카르텔** | 멕시코·콜롬비아 카르텔 |
| **사이버 범죄** | Lazarus, Evil Corp |
| **확산금융** | 핵·미사일 관련 |
| **부패** | Magnitsky Act 관련 (글로벌 인권 침해) |

### 제재 형태
- **자산 동결 (asset freeze)** — 미국 관할 내 자산 동결
- **거래 금지 (transaction ban)** — 미국인/기업 거래 금지
- **2차 제재 (secondary sanctions)** — 외국인이라도 미국 시장 접근 차단
- **무역 금지 (trade embargo)** — 특정 품목/서비스 금지

## 2. 핵심 리스트

| 리스트 | 발행 | 가상자산 포함? | 갱신 |
|---|---|---|---|
| **OFAC SDN List** | 미국 재무부 | ✅ (지갑주소 등재) | 수시 |
| **OFAC Consolidated** | 미국 재무부 (SDN 외 추가) | 일부 | 수시 |
| **UN Consolidated** | UN 안보리 | 명시 X (이름 위주) | 수시 |
| **EU Consolidated Financial Sanctions** | EU | 일부 | 수시 |
| **HM Treasury Sanctions List** | 영국 | 일부 | 수시 |
| **한국 외교부 제재대상자** | 한국 | (종속적, UN/OFAC 반영) | 수시 |

## 3. OFAC의 가상자산 지갑주소 등재

### 역사적 사례
| 연도 | 대상 | 비고 |
|---|---|---|
| 2018 | 이란 BTC 주소 (Marinov, Khorashadizadeh) | 첫 가상자산 SDN |
| 2020 | DPRK 라자루스 관련 ETH/BTC | |
| 2022-08 | **Tornado Cash 컨트랙트** | DeFi 첫 제재 |
| 2022-11 | Hydra Market (다크넷) | |
| 2024 | Garantex 추가 제재 (러시아) | |
| **2025-03** | **Tornado Cash 제재 해제** | 5th Circuit 패소 |

### OFAC SDN 가상자산 검색
- 공식: https://sanctionssearch.ofac.treas.gov/
- 가상자산 영역도 같은 검색
- API: 일부 벤더가 라이센스 (Chainalysis, TRM)

## 4. 스크리닝 매칭 방식

### A. 이름 매칭 (Fuzzy)
- 동음이의 / 음역 다양성 처리 (Mohammed vs Mohammad)
- Levenshtein distance, Jaro-Winkler, Soundex 등
- **너무 느슨**: false positive 폭발
- **너무 빡빡**: false negative

### B. 보조 식별자
- 생년월일
- 국적 / 거주지
- 신원확인번호 (passport 등)
- 회사명 / 직책

### C. 가상자산 지갑주소 매칭
- **정확 매칭** (exact match) — 동일 주소
- **클러스터 매칭** (extended) — 같은 클러스터 내 주소
- **Hop 노출** (indirect) — N hop 내 도달 주소

## 5. 스크리닝 시점

### A. 사전 (Onboarding) 스크리닝
- 신규 가입 시 KYC 정보로 매칭
- 매칭되면 가입 거절 또는 보류
- 가입 후 정보 변경 시 재스크리닝

### B. 실시간 (Transaction) 스크리닝
- 거래 발생 직전:
  - 송신/수신 wallet OFAC SDN 매칭
  - 카운터파티 VASP 제재국 여부
  - 거래 메타데이터 (memo, tag) 매칭
- 매칭되면 **거래 차단 + 자동 알람**

### C. 사후 (Periodic) 스크리닝
- 모든 고객/wallet을 주기적으로 (일/주/월) 전체 스크리닝
- 새로 SDN 추가된 항목과 기존 데이터 매칭
- "잠재 노출" 발견 시 STR 검토

## 6. 운영 흐름

```
[ 신규 가입 ] → KYC + Sanctions Screening (이름/DOB/국적) 
                  ├─ Hit → 가입 거절
                  └─ No Hit → 가입 승인

[ 거래 요청 ] → Sanctions Screening (이름 + wallet 주소)
                  ├─ Hit (high confidence) → 차단 + STR 보고
                  ├─ Hit (low confidence) → 수동 검토
                  └─ No Hit → 거래 진행

[ 일일 배치 ] → 전체 고객 + wallet vs SDN 갱신본
                  ├─ 신규 매칭 → 즉시 동결 + 분석 + STR
                  └─ 기존 통과 → 다음 사이클
```

## 7. False Positive 처리 (Disposition)

### 일반적 시나리오
- "Kim Min-soo" 검색 → 다수 동명이인
- 생년월일/국적 다르면 → 명백한 false positive → 통과
- 모호하면 → 추가 자료 요청 → 분석가 판단

### Disposition 코드 (예)
| 코드 | 의미 |
|---|---|
| TP-Confirmed | 진짜 매칭 → 차단 + STR |
| FP-Different DOB | DOB 다름, 통과 |
| FP-Different Nationality | 국적 다름, 통과 |
| FP-Different Address | 주소 다름, 통과 |
| Pending | 추가 정보 필요 |

→ 모든 disposition은 **로그 기록 + 검사 시 증빙**.

## 8. 고난이도 케이스

### A. 동명이인 (Common Name)
- "Kim", "Mohammed", "Wang" 같은 흔한 이름
- 보조 식별자가 핵심

### B. 음역(Transliteration)
- 한자/아랍어/러시아어 → 영문 음역 다양
- "Kim" vs "Gim" vs "Kym"

### C. 회사명 변형
- "ABC Corp" vs "ABC Corporation" vs "ABC Co., Ltd."
- 약어, 띄어쓰기, 콤마 등

### D. Wallet 주소 — 클러스터 노출
- 직접 매칭은 없으나 **같은 클러스터에 SDN 주소** 존재
- → 위험 노출 인정 → 강화 모니터링

### E. Privacy Coin 거래
- 추적 불가 → 사실상 모든 거래가 잠재 위험
- 한국에선 거래소 상장 폐지로 우회

## 9. 한국 특수 — 어디서 정보를 받나

| 출처 | 무엇 |
|---|---|
| 외교부 | UN/EU/OFAC 반영 + 한국 자체 |
| FIU | 가상자산 위험 wallet 정보 (협조 시) |
| KISA | 사이버 위협 정보 (랜섬웨어 wallet 등) |
| 글로벌 벤더 | World-Check, Dow Jones, ComplyAdvantage |
| KYT 벤더 | Chainalysis, TRM, Elliptic SDN wallet feed |

## 10. 위반 시 처벌

### 미국 OFAC (가장 강력)
- 민사벌금: 거래당 최대 $300K+
- 형사: 최대 30년 징역, $1M+ 벌금
- **2차 제재**: 외국인이라도 미국 시장 접근 차단

### 사례
- **Binance** $4.3B (2023) — OFAC + FinCEN 결합
- **Bittrex** $29M (2022)
- **BitGo** $98K (2021)

### 한국
- 외환거래법, 특정범죄가중처벌법 등
- 외교부 제재 위반 시 형사처벌
- + 특금법 위반 결합

## 11. 체크리스트

```
□ OFAC + UN + EU + 외교부 명단 일일 갱신
□ 사전 스크리닝 (onboarding)
□ 실시간 스크리닝 (모든 거래)
□ 사후 배치 스크리닝 (전체 고객)
□ Wallet 주소 OFAC SDN 매칭
□ KYT 벤더 SDN feed 통합
□ False Positive disposition 로그
□ 매칭 시 차단 + STR + 보고 SOP
□ Adverse Media 모니터링
□ 외환거래법 호환성 점검
□ 임직원 교육 (OFAC 2차 제재 인식)
```

## 더 읽을거리
- [`cdd_edd.md`](cdd_edd.md) — Onboarding 스크리닝 통합
- [`str_ctr.md`](str_ctr.md) — 매칭 시 STR
- [`../01_regulations/us_bsa_fincen.md`](../01_regulations/us_bsa_fincen.md) — OFAC 제도 상세
- [`../06_cases_typologies/tornado_cash.md`](../06_cases_typologies/tornado_cash.md) — DeFi 제재 사례
- [OFAC 공식](https://ofac.treasury.gov/)
- [OFAC SDN List 검색](https://sanctionssearch.ofac.treas.gov/)
- [UN Consolidated List](https://www.un.org/securitycouncil/content/un-sc-consolidated-list)
