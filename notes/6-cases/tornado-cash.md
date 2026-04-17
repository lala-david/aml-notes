# Tornado Cash — DeFi 첫 OFAC 제재와 그 결말

> 코드를 제재할 수 있는가? DeFi AML의 분기점. 마지막 업데이트: 2026-04-17.

## TL;DR
- **2022-08-08**: OFAC가 Tornado Cash 스마트컨트랙트 자체를 SDN List에 등재 (DeFi 첫 제재)
- 7B+ 달러 자금세탁 중 **Lazarus의 $455M+ 포함**
- **2024-11-26**: 5th Circuit 연방항소법원 — "OFAC 권한 초과, 컨트랙트는 'property' 아니다"
- **2025-03-21**: OFAC 공식 제재 해제
- 그러나 **개발자 Roman Storm 형사재판 별도 진행 중** (2024 기소)
- 의미: 코드 자체 제재의 법적 한계 + DeFi/스마트컨트랙트 컴플라이언스 미해결 과제

---

## 1. Tornado Cash란

### 정체성
- **이더리움 기반 mixer 스마트컨트랙트**
- 2019년 출시 (Roman Semenov, Roman Storm 개발)
- **zk-SNARK** 기반 zero-knowledge proof 사용
- 사용자가 ETH/USDT 등 입금 → 다른 주소로 무관계 인출

### 작동 방식 (간단)
```
1. 사용자 A가 1 ETH를 Tornado pool에 입금
2. 입금 시 commitment 생성 (해시)
3. 시간 지난 후 다른 wallet B로 인출 요청 + zk-SNARK 증명
4. 컨트랙트가 증명 검증 → B에게 1 ETH 출금
5. A→B 연결고리 끊어짐 (on-chain에서 매핑 안 보임)
```

### 사용 분포
- 합법 사용 (프라이버시 추구)
- 불법 사용 (해킹 자금 세탁)
- 추정 합법:불법 비율 의견 분분 — Lazarus만 $455M+ 사용

## 2. 2022-08-08 OFAC 제재

### 결정
- 미국 재무부 OFAC가 **Tornado Cash 스마트컨트랙트 주소 등재**
- $7B+ 자금세탁 (2019~2022 누적)
- 그중 **Lazarus 관련 $455M+** 포함 (Ronin, Harmony 등)
- 미국인의 Tornado Cash 사용 금지

### 영향
- Circle (USDC 발행자) 즉시 Tornado 주소 USDC freeze
- Github가 Tornado Cash 저장소 일시 삭제 (이후 재공개)
- DeFi 사용자들이 자기 주소 freeze 우려
- **개발자 Roman Storm + Roman Semenov 미국 형사 기소** (2023-08)
- 한 개발자 Alexey Pertsev 네덜란드 체포 (2022) → 2024 유죄 (이후 항소 중)

### 정당성 논쟁
- 옹호: 라자루스가 실제 사용했음, 효과적 제재
- 비판:
  - 코드/스마트컨트랙트는 "person"도 "property"도 아님
  - 합법 사용자 무차별 처벌
  - 표현의 자유 침해 (코드 = speech)
  - DeFi/오픈소스 미래에 위협

## 3. 법적 도전

### Coin Center 등 소송
- Coin Center, Tornado 사용자들이 OFAC 제소
- 1심: OFAC 손
- 항소심으로 이어짐

### 5th Circuit 항소법원 (2024-11-26)
- 판결: **"OFAC overstepped its congressionally defined authority"**
- 핵심 논리:
  - IEEPA(국제비상경제권한법)는 "property"에 적용
  - **immutable smart contract는 property로 볼 수 없음**
  - 누구도 통제하지 않는 코드는 제재 대상 부적합
- → OFAC 패소

### OFAC 제재 해제 (2025-03-21)
- 5th Circuit 판결 후 OFAC가 SDN에서 Tornado Cash 제거
- "여전히 mixer는 위험하다" 입장 유지
- 개별 거래/사용자 제재는 가능

### Roman Storm 형사재판 (별도 진행)
- 코드 제재가 무효되어도 **개발자 형사 책임은 별개**
- 죄목: 자금세탁 공모, 무면허 송금업, 제재 위반
- 2024-2025 재판 진행
- 결과는 DeFi 개발자 책임 범위에 큰 영향

## 4. 컴플라이언스 임팩트

### 회사 차원
- 2022~2025 Tornado 노출 wallet은 **자동 차단** 표준화
- 2025-03 제재 해제 후에도 **mixer는 위험** 카테고리 유지
- 회사 정책: "Tornado 노출 = 위험점수 +50" 같은 룰 그대로

### 산업 차원
- **mixer 일반 = 고위험** 이라는 인식 자리잡음
- 각 mixer마다 라벨링 + 자동 KYT 차단 표준
- 합법 사용자 보호 vs 자금세탁 차단의 딜레마는 미해결

### DeFi 차원
- "코드 자체는 제재 못 한다"는 일부 안정감
- 그러나 **개발자 + frontend + governance token holder** 책임 가능성 확인
- DeFi 회사는 KYC/제재 체크 추가하는 곳 늘어남

## 5. 다른 Mixer 운명

| Mixer | 운명 |
|---|---|
| **Tornado Cash** | 2022 제재 → 2025 해제, 개발자 재판 중 |
| **Blender.io** | 2022-05 OFAC 제재 → 운영 중단 |
| **Sinbad.io** | 2023-11 OFAC 제재 (Blender 후신) |
| **Wasabi Wallet** | 운영 중, CoinJoin |
| **Samourai Wallet** | 2024-04 운영자 체포, 서비스 중단 |
| **JoinMarket** | P2P CoinJoin, 운영 중 |
| **Cryptomixer** | 운영 중 |

→ **운영자 식별 가능한 mixer는 거의 다 폐쇄**, 분산형만 살아남음.

## 6. 한국 시점 — 우리는 어떻게

- 한국 거래소는 Tornado 노출 wallet **차단** 표준
- 가상자산이용자보호법 + 특금법으로 mixer 사용 자체가 의심거래 → STR
- 한국 사용자는 Tornado 사용 자체가 사실상 위험
- 2025-03 제재 해제 후에도 한국 정책 변화 없음

## 7. 학습 포인트

```
- 코드를 제재할 수 있는가? 법적으로는 어렵다는 결론 (적어도 미국 IEEPA 한계)
- 그러나 개발자/frontend/governance는 별개 — 책임질 수 있다
- 회사 정책은 OFAC 제재와 별도로 mixer = 고위험 유지
- DeFi의 미래는 "탈중앙화 = AML 면책" 이 아님이 분명해짐
- ZKP 기반 프라이버시 도구의 정당한 사용과 자금세탁 도구의 분리가 미해결 과제
```

## 더 읽을거리
- [`lazarus_dprk.md`](lazarus_dprk.md) — Tornado의 주요 사용자
- [`major_enforcement.md`](major_enforcement.md) — 관련 enforcement
- [`../notes/3-crypto-aml/defi-nft-risks.md`](../notes/3-crypto-aml/defi-nft-risks.md) — DeFi AML 회색지대
- [`../notes/5-compliance/sanctions-screening.md`](../notes/5-compliance/sanctions-screening.md) — OFAC 일반
- [Treasury — Tornado Cash 제재 보도자료 (2022)](https://home.treasury.gov/news/press-releases/jy0916)
- [Venable — Treasury Lifts Sanctions on Tornado (2025)](https://www.venable.com/insights/publications/2025/04/a-legal-whirlwind-settles-treasury-lifts-sanctions)
- [Sanction Scanner — Tornado Cash 분석](https://www.sanctionscanner.com/blog/tornado-cash-a-crypto-mixing-service-now-blacklisted-by-the-us-treasury-675)
- [BTC Policy Institute — Tornado 분석](https://www.btcpolicy.org/articles/tornado-cash-where-code-privacy-and-sanctions-collide)
- [Steptoe — Tornado Cash & DeFi AML 의의](https://www.steptoe.com/en/news-publications/blockchain-blog/critical-tornado-cash-developments-have-significant-implications-for-defi-aml-and-sanctions-compliance.html)
