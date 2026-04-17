# DeFi / NFT / Privacy Coin — 특수 영역 AML 리스크

> 중앙화 VASP 외부의 회색지대. 마지막 업데이트: 2026-04-17.

## TL;DR
- **DeFi**: 운영자 식별 어려움 → AML 의무 적용 모호. 그러나 OFAC은 Tornado Cash 제재로 "코드도 제재 가능" 시도 (2025-03 해제)
- **NFT**: wash trading + 자금이전 정당화 도구. FATF는 NFT를 사례별로 VA로 분류
- **Privacy Coin**: Monero/Zcash. 한국·일본 거래소는 사실상 상장 폐지
- **Cross-chain Bridge**: layering 핵심 인프라이자 해킹 1순위 표적
- **MEV bot, flash loan**: 가격 조작 + 자금세탁 결합 가능

---

## 1. DeFi (Decentralized Finance)

### 정체성
- **중개자 없는 금융** — 스마트컨트랙트가 직접 lending/swap/derivatives 처리
- 대표: Uniswap, Aave, Compound, Curve, MakerDAO, GMX
- TVL(Total Value Locked) 수백억 달러 규모

### AML 관점 문제
| 항목 | 이슈 |
|---|---|
| **운영자 식별** | DAO/익명 개발자 → 누가 VASP인가? |
| **KYC 부재** | 사용자가 wallet만 연결, 신원 확인 없음 |
| **글로벌 즉시 접근** | 제재국 사용자도 제한 없이 사용 가능 |
| **자금세탁 도구화** | DEX swap이 layering 인프라 |
| **fork 가능성** | 한 코드베이스가 무한 복제 |

### 규제 현황 (2026 시점)
- **FATF**: DeFi에 사실상 운영 통제권 가진 자(developer, governance token holder)는 VASP 의무 부담 가능 (2021 가이던스)
- **미국**: 인프라법 broker 정의, FIT21 등 입법 추진. Uniswap Labs SEC Wells Notice (2024)
- **EU MiCA**: "fully decentralized" DeFi는 적용 제외, 단 frontend 운영자는 적용 가능
- **한국**: 2단계 입법에서 다룰 예정, 현재 명확한 룰 없음

### 회색지대 맵
```
완전 탈중앙 (코드만 존재) ────────────── 중앙화 (회사 운영)
  ↑                                          ↑
  AML 규제 거의 불가                      VASP로 직접 적용

중간:
- DAO 거버넌스 토큰 보유자
- Frontend 운영자 (uniswap.org)
- Routing infrastructure
- 1inch 같은 aggregator
```

→ "frontend 운영자" 가 점점 규제 타겟이 되는 추세 (Uniswap Labs).

### 주요 DeFi 자금세탁 패턴
1. **Swap layering**: ETH → USDT → DAI → ETH → USDT (출처 단절)
2. **Liquidity Pool 세탁**: LP 입금 → 다른 자산으로 인출
3. **Flash Loan Attack 결합**: 가격 조작 + 차익 인출 → 즉시 mixer
4. **MEV bot 활용**: sandwich/arbitrage으로 자금 흐름 위장

## 2. NFT (Non-Fungible Token)

### AML 관점에서 NFT의 본질
- **고유 자산** + **가격 자율 책정** + **즉시 글로벌 거래**
- → **거래 가격을 임의로 조작 가능** = 자금세탁자에게 매력적

### 주요 패턴
| 패턴 | 설명 |
|---|---|
| **Wash trading** | 자기들끼리 NFT를 사고팔아 가격/거래량 부풀림 |
| **Self-laundering** | A 주소에서 B 주소로 NFT 매수 (사실상 같은 사람) |
| **Trading mule** | 더러운 자금으로 정당한 NFT 매수 → 합법자산화 |
| **Phishing 결합** | 가짜 NFT 민팅으로 피해자 wallet drain |
| **Royalty manipulation** | 로열티를 자기 주소로 받게 설정 |

### 시장 통계 (Chainalysis 등)
- 2022~2023 NFT 광풍 시 **wash trading 비중 추정 25~50%**
- 2025년 NFT 시장 위축 → 거래량 자체 감소
- 그래도 high-value collection (BAYC, CryptoPunks) 중심으로는 여전 활동

### FATF 입장
- NFT가 **fungible해질 수 있고 결제/투자 수단으로 쓰이면** VA로 분류 (2021 가이던스)
- 단순 collectible은 VA 아님 — 사례별 판단

### 한국 입장
- NFT는 **2024년 6월 FSC 가이드라인** 으로 일부 명확화
- 결제수단/대량발행/펀더멘털 분할 → VA로 간주
- 단순 디지털 아트 NFT → 비-VA

## 3. Privacy Coin

### 대표
| 코인 | 기술 | 추적 가능성 |
|---|---|---|
| **Monero (XMR)** | Ring Signature + Stealth Address + RingCT | **거의 불가** |
| **Zcash (ZEC)** | zk-SNARK shielded transaction | shielded 사용 시 불가 (선택적) |
| **Dash** | PrivateSend (CoinJoin 변형) | 제한적 추적 가능 |
| **Grin/Beam** | MimbleWimble | 어려움 |

### 거래소 상장 회피
- FATF 권고: 거래소가 privacy coin 취급 시 추가 위험관리 필요
- 한국: **2021년 특금법 시행과 함께 4대 거래소가 privacy coin 전량 상장폐지** (Monero, Zcash, Dash 등)
- 일본: 2018년부터 privacy coin 상장 금지
- 미국/EU: 일부 거래소 상장 유지, 단 강화감시
- → privacy coin은 **OTC, P2P, 비규제 거래소** 로 빠짐

### 추적 시도
- **Monero**: Chainalysis가 부분적 분석 도구 발표 (2020) — 효과는 제한적
- **Zcash**: shielded 사용 비율이 낮아 (대부분 transparent 사용) 분석 가능

## 4. Cross-chain Bridge

### 정체성
- A 체인 자산을 잠그고 B 체인에서 wrapped 토큰 발행
- 예: ETH 잠그고 → BSC에서 WETH 발행

### AML 관점
- **Layering 핵심 인프라** — chain 간 끊김 발생
- 2025-2026 자금세탁 트렌드 1위가 cross-chain
- 분석 도구가 cross-chain tracing 기능 강화 중

### 해킹 표적
| 사고 | 연도 | 손실 |
|---|---|---|
| Poly Network | 2021 | $611M (이후 반환) |
| Wormhole | 2022 | $325M |
| Ronin Bridge | 2022 | $625M (Lazarus) |
| Nomad | 2022 | $190M |
| Harmony Horizon | 2022 | $100M (Lazarus) |
| Multichain | 2023 | $231M |

→ 브리지 자체가 honeypot. 해킹 → 자금이 다시 다른 브리지로 → 세탁.

## 5. MEV / Flash Loan / 기타 DeFi 도구

### MEV (Maximal Extractable Value)
- 블록 생성 시 트랜잭션 순서 조작으로 이득
- AML 관점: **Sandwich attack** 으로 가격 조작 → 자금세탁/시세조종 결합 가능

### Flash Loan
- **담보 없이** 한 트랜잭션 안에서 빌리고 갚는 대출
- AML 관점: 가격 조작 → 차익 추출 → 즉시 mixer
- 사례: bZx, Cream Finance, Beanstalk 등

### Re-staking / LST / LRT
- Lido (LST), EigenLayer (LRT) 같은 새로운 layer
- 자산 형태 변환이 가능해 layering 도구화 가능
- 분석 도구가 아직 따라가는 중

## 6. 회사 관점 — 어떻게 대응하나

### 거래소
- DeFi 입출금 차단/제한 정책
- DEX 컨트랙트 주소 라벨링
- bridge 출금 시 추가 KYT
- privacy coin 상장 금지

### 수탁업자
- 고객의 DeFi 사용 위탁 시 별도 정책
- staking/restaking 위탁 시 출금 흐름 분석
- NFT 수탁 시 attribution 강화

### 분석/솔루션 회사
- DeFi/NFT 분석 모듈 개발 가치
- cross-chain tracing 기능
- 새로운 프로토콜 라벨링 자동화

## 더 읽을거리
- [`onchain_typology.md`](onchain_typology.md) — 자금세탁 7유형
- [`travel_rule.md`](travel_rule.md) — Travel Rule (DeFi 적용 한계)
- [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) — cross-chain tracing
- [`../notes/6-cases/tornado-cash.md`](../notes/6-cases/tornado-cash.md) — DeFi 첫 제재 사례
- [Transnet — DeFi Compliance 2026 Guide](https://transnetinc.com/navigating-compliance-challenges-in-defi-a-2026-guide)
- [Steptoe — Tornado Cash & DeFi AML implications](https://www.steptoe.com/en/news-publications/blockchain-blog/critical-tornado-cash-developments-have-significant-implications-for-defi-aml-and-sanctions-compliance.html)
