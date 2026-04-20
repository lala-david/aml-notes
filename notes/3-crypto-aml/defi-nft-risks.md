# DeFi / NFT / Privacy Coin — 특수 영역 AML 리스크

> 중앙화 VASP **외부의 회색지대**. 이 글을 읽고 나면 왜 DeFi·NFT·Privacy Coin이 "사업자 없는 자금세탁 인프라"가 됐는지, 그리고 규제가 왜 이 영역에서 계속 지연되는지 이해하게 됩니다. 마지막 업데이트: 2026-04-17.

## TL;DR
- **DeFi**: 운영자 식별 어려움 → AML 의무 적용 모호. OFAC의 Tornado Cash 제재(2022) → 2025-03 해제는 "코드를 제재할 수 있는가" 판례의 전환점
- **NFT**: wash trading + 자금이전 정당화 도구. FATF는 NFT를 사례별로 VA로 분류
- **Privacy Coin**: Monero·Zcash. 한국·일본 거래소는 사실상 상장 폐지
- **Cross-chain Bridge**: layering 핵심 인프라이자 해킹 1순위 표적
- **MEV bot · flash loan**: 가격 조작 + 자금세탁 결합 가능

---

## 1. DeFi (Decentralized Finance)

### 정체성

**DeFi**는 중개자 없이 스마트컨트랙트가 직접 lending·swap·derivatives를 처리하는 금융 인프라. 대표 프로토콜로 Uniswap(DEX), Aave(lending), Compound(lending), Curve(stablecoin AMM), MakerDAO(stablecoin 발행), GMX(derivatives) 등이 있으며 TVL(Total Value Locked, 예치 자산 가치)은 수백억 달러 규모.

용어:
- **TVL (Total Value Locked)** — 프로토콜에 예치된 자산의 총 USD 환산 가치. DeFi 지표로 가장 흔히 사용.
- **AMM (Automated Market Maker)** — 사람 중개인 없이 알고리즘이 자동 가격 결정하는 DEX 구조.
- **DAO (Decentralized Autonomous Organization)** — 거버넌스 토큰 홀더의 투표로 운영되는 조직.

### 왜 AML에서 문제인가

| 항목 | 이슈 |
|---|---|
| **운영자 식별** | DAO·익명 개발자 → **누가 VASP인가**? |
| **KYC 부재** | 사용자가 wallet만 연결, 신원 확인 없음 |
| **글로벌 즉시 접근** | 제재국 사용자도 제한 없이 사용 가능 |
| **자금세탁 도구화** | DEX swap이 layering 인프라 |
| **Fork 가능성** | 한 코드베이스가 무한 복제. 프런트엔드 차단해도 포크로 우회 |

### 규제 현황 (2026 시점)

- **FATF**: DeFi에 사실상 운영 통제권을 가진 자(developer, governance token holder)는 VASP 의무 부담 가능 (2021 가이던스).
- **미국**: 인프라법 broker 정의 확장, FIT21 등 입법 추진. 2024년 Uniswap Labs에 SEC Wells Notice 발부.
- **EU MiCA**: "fully decentralized" DeFi는 적용 제외, 단 **frontend 운영자는 적용 가능**.
- **한국**: 2단계 입법에서 다룰 예정, 현재 명확한 룰 없음.

### 회색지대 맵

```
완전 탈중앙 (코드만 존재) ──────────────── 중앙화 (회사 운영)
  ↑                                          ↑
  AML 규제 거의 불가                      VASP로 직접 적용

중간 영역 — 점점 규제 타겟이 되는 층:
- DAO 거버넌스 토큰 보유자 (비례 통제력)
- Frontend 운영자 (uniswap.org)
- Routing infrastructure
- 1inch 같은 aggregator
```

### 주요 DeFi 자금세탁 패턴

1. **Swap layering**: ETH → USDT → DAI → ETH → USDT (출처 단절).
2. **Liquidity Pool 세탁**: LP 입금 → 다른 자산으로 인출.
3. **Flash Loan Attack 결합**: 가격 조작 → 차익 인출 → 즉시 mixer.
4. **MEV bot 활용**: sandwich/arbitrage으로 자금 흐름 위장.

### 실무 포인트

"frontend 운영자가 규제 타겟이 된다"가 현재 글로벌 흐름의 핵심입니다. 프런트엔드(uniswap.org, aave.com 같은 웹페이지)를 운영하는 회사는 KYC 구현·제재 스크리닝·지역 차단이 가능하므로, 규제 압력이 여기로 몰립니다. "코드는 규제 불가"이지만 "그 코드를 사용하기 쉽게 만드는 회사는 규제 가능"이라는 논리.

---

## 2. NFT (Non-Fungible Token)

### AML 관점에서 NFT의 본질

NFT는 **고유 자산 + 가격 자율 책정 + 즉시 글로벌 거래**라는 조합을 갖습니다. 이게 의미하는 바: **거래 가격을 임의로 조작 가능** → 자금세탁자에게 매력적인 도구. 주식시장의 시세조종과 구조적으로 같은 리스크.

### 주요 패턴

| 패턴 | 설명 |
|---|---|
| **Wash trading** | 자기들끼리 NFT를 사고팔아 가격·거래량 부풀림 |
| **Self-laundering** | A 주소에서 B 주소로 NFT 매수 (사실상 같은 사람) |
| **Trading mule** | 더러운 자금으로 정당한 NFT 매수 → 합법자산화 |
| **Phishing 결합** | 가짜 NFT 민팅으로 피해자 wallet drain |
| **Royalty manipulation** | 로열티를 자기 주소로 받게 설정 |

### 시장 통계

- 2022~2023 NFT 광풍 시 wash trading 비중 추정 **25~50%** (Chainalysis)
- 2025년 NFT 시장 위축 → 거래량 자체 감소
- 그래도 high-value collection (BAYC, CryptoPunks) 중심으로는 여전 활동

### FATF·한국 입장

- **FATF (2021 가이던스)**: NFT가 **fungible해질 수 있고 결제·투자 수단으로 쓰이면** VA로 분류. 단순 collectible은 VA 아님 — 사례별 판단.
- **한국 (2024-06 FSC 가이드라인)**: 결제수단 사용, 대량발행, 펀더멘털 분할(예: 부동산 NFT 조각화) → VA로 간주. 단순 디지털 아트 NFT → 비-VA.

### 실무 포인트

NFT 마켓플레이스 운영 시 **wash trading 모니터링**은 자율 통제 수준이 아니라 **감독당국이 사실상 기대**하는 영역입니다. OpenSea·Blur·Magic Eden 같은 글로벌 대형사는 이미 자체 탐지 팀을 운영. 한국 NFT 사업자도 동일 수준을 갖추는 게 규제 부담 경감의 지름길.

---

## 3. Privacy Coin

### 대표 코인과 기술

| 코인 | 기술 | 추적 가능성 |
|---|---|---|
| **Monero (XMR)** | Ring Signature + Stealth Address + RingCT | **거의 불가** |
| **Zcash (ZEC)** | zk-SNARK shielded transaction | shielded 사용 시 불가 (선택적) |
| **Dash** | PrivateSend (CoinJoin 변형) | 제한적 추적 가능 |
| **Grin / Beam** | MimbleWimble | 어려움 |

### 각 기술의 원리 한 줄 요약

- **Ring Signature (Monero)** — 여러 명의 서명자 중 누가 실제 서명자인지 모르게. 기본적으로 "용의자가 여러 명"으로 수사를 난해하게 함.
- **Stealth Address (Monero)** — 받는 주소가 매 거래마다 새로 생성. 같은 사람이 받아도 다른 주소로 보임.
- **RingCT (Monero)** — 거래 금액 자체도 암호화. 발신·수신·금액 3요소가 모두 숨겨짐.
- **zk-SNARK (Zcash)** — 영지식 증명으로 "거래가 유효함"만 증명, 내용은 완전 숨김.

### 거래소 상장 회피 추세

- **FATF 권고**: 거래소가 privacy coin 취급 시 추가 위험관리 필요.
- **한국**: 2021년 특금법 시행과 함께 4대 거래소가 privacy coin 전량 상장폐지 (Monero, Zcash, Dash 등).
- **일본**: 2018년부터 privacy coin 상장 금지.
- **미국·EU**: 일부 거래소 상장 유지, 단 강화감시.
- 결과: privacy coin은 **OTC·P2P·비규제 거래소**로 밀려남.

### 추적 시도

- **Monero**: Chainalysis가 부분적 분석 도구 발표 (2020) — 효과는 제한적, 완전 분석은 여전 불가.
- **Zcash**: shielded 사용 비율이 낮아(대부분 transparent 사용) 분석 가능한 비중이 큼. **"선택적 프라이버시"** 는 실무상 프라이버시가 아님.

### 실무 포인트

한국 거래소에서는 privacy coin 입금을 **자동 차단**하는 게 표준. 입금 시 "알 수 없는 자산"이 도착하면 반려. 출금 시점에는 수신 주소가 privacy coin 관련 지갑(알려진 Monero exchange 주소 등)인지 KYT가 확인. 운영 부담이 크지 않은 편이지만, privacy coin을 자체 수용하려는 시도는 규제 리스크가 너무 커서 거의 없습니다.

---

## 4. Cross-chain Bridge

### 정체성

A 체인 자산을 **잠그고(lock)** B 체인에서 **wrapped 토큰**을 발행. 예: ETH를 Ethereum 컨트랙트에 잠그고 BSC에서 wETH 발행. 반대로 환원하려면 B에서 소각(burn) → A에서 해제.

### AML 관점

- **Layering 핵심 인프라** — chain 간 끊김 발생.
- 2025~2026 자금세탁 트렌드 1위가 cross-chain.
- 분석 도구가 cross-chain tracing 기능을 공격적으로 강화 중 (Chainalysis Crosschain, TRM Multichain).

### 해킹 표적 역사

브리지는 AML 관점과 무관하게 **해킹 1순위 표적**이기도. 자금이 한 곳에 집중되는 honeypot 구조.

| 사고 | 연도 | 손실 |
|---|---|---|
| Poly Network | 2021 | $611M (이후 반환) |
| Wormhole | 2022 | $325M |
| **Ronin Bridge** | 2022 | **$625M** (Lazarus) |
| Nomad | 2022 | $190M |
| Harmony Horizon | 2022 | $100M (Lazarus) |
| Multichain | 2023 | $231M |

→ 브리지가 해킹 → 자금이 다시 다른 브리지로 → 세탁. **해킹과 세탁이 같은 인프라를 순환**하는 구조.

### 실무 포인트

출금 주소가 브리지 컨트랙트이면 **고위험 카테고리**로 다뤄야 합니다. 브리지 자체가 범죄적이지는 않지만, 브리지로 나간 자금의 **다음 홉**을 추적할 수 없다면 그 시점 exposure는 사실상 unknown. 공격적 회사는 모든 브리지 출금에 자동 STR 후보 큐잉을 적용하고, 안전한 회사는 이 리스크를 감수하고 빠른 UX를 택합니다.

---

## 5. MEV · Flash Loan · 기타 DeFi 도구

### MEV (Maximal Extractable Value)

블록 생성 시 **트랜잭션 순서 조작**으로 얻는 이득. 블록 생성자(validator)나 MEV 봇이 활용.

**AML 관점**: **Sandwich attack**(피해 거래 앞뒤로 거래 끼워 넣어 가격 올리고 되돌림)으로 가격 조작 → 자금세탁·시세조종과 결합 가능.

### Flash Loan

**담보 없이** 한 트랜잭션 안에서 빌리고 갚는 대출. 한 블록 내에서 완결되어야 하며, 안 되면 트랜잭션 자체가 revert.

**AML 관점**: 가격 조작 → 차익 추출 → 즉시 mixer로. 사례: bZx, Cream Finance, Beanstalk Farms 등 플래시론 공격.

### Re-staking · LST · LRT

Lido(LST, Liquid Staking Token), EigenLayer(LRT, Liquid Restaking Token) 같은 새로운 layer. 자산이 staking 토큰으로 감싸지고 또 감싸지면 **자산 형태 변환이 가능**해 layering 도구화될 수 있음. 분석 도구가 아직 완전히 따라가지 못하는 영역.

용어:
- **LST (Liquid Staking Token)** — ETH를 staking하고 그 증표로 받는 토큰 (예: stETH).
- **LRT (Liquid Restaking Token)** — LST를 다시 restaking하고 받는 토큰.
- **Flash Loan** — 담보 없이 한 트랜잭션 내 빌리고 갚는 대출.

### 실무 포인트

LST·LRT 세탁은 2025~2026년 부상 중인 신종 유형입니다. ETH → stETH → eETH(EigenLayer) → PT(Pendle) 같은 형태로 자산을 여러 번 감싸면 원래 출처가 불투명해집니다. 이 영역에 대한 attribution DB는 아직 빈약하고, KYT 벤더도 명시적 지원을 시작한 지 얼마 안 됐습니다.

---

## 6. 회사 관점 — 어떻게 대응하나

### 거래소

- DeFi 입출금 차단·제한 정책
- DEX 컨트랙트 주소 라벨링
- Bridge 출금 시 추가 KYT
- Privacy coin 상장 금지

### 수탁업자

- 고객의 DeFi 사용 위탁 시 별도 정책
- Staking·restaking 위탁 시 출금 흐름 분석
- NFT 수탁 시 attribution 강화

### 분석·솔루션 회사

- DeFi·NFT 분석 모듈 개발 가치
- Cross-chain tracing 기능
- 새로운 프로토콜 라벨링 자동화

### 실무 포인트

사업자가 DeFi 리스크를 대응하는 방법은 크게 두 접근: **차단 우선**(보수적)과 **탐지 강화**(공격적). 한국 거래소는 대체로 차단 우선으로 가고 있는데, 이게 편하지만 **경쟁 상품**(해외 거래소·탈중앙 앱)으로 고객 이탈 위험을 키웁니다. 장기적으로는 **탐지 강화 쪽으로 진화**가 필수이며, 그러려면 KYT 벤더와의 전략적 파트너십이 중요해집니다.

---

## 요약 부록 — 빠른 참조용

**DeFi 4대 패턴**: Swap layering · LP 세탁 · Flash Loan 결합 · MEV 활용
**NFT 5대 패턴**: Wash trading · Self-laundering · Trading mule · Phishing · Royalty manipulation
**Privacy Coin 운영 표준**: 상장 폐지 + 입금 차단 + 출금 KYT
**신종 영역**: LST·LRT, MEV, Flash Loan

## 더 읽을거리
- [`onchain-typology.md`](onchain-typology.md) — 자금세탁 9대 유형
- [`travel-rule.md`](travel-rule.md) — Travel Rule (DeFi 적용 한계)
- [`../4-technology/blockchain-analytics.md`](../4-technology/blockchain-analytics.md) — cross-chain tracing 기법
- [`../6-cases/tornado-cash.md`](../6-cases/tornado-cash.md) — DeFi 첫 제재 사례
- [Transnet — DeFi Compliance 2026 Guide](https://transnetinc.com/navigating-compliance-challenges-in-defi-a-2026-guide)
- [Steptoe — Tornado Cash & DeFi AML implications](https://www.steptoe.com/en/news-publications/blockchain-blog/critical-tornado-cash-developments-have-significant-implications-for-defi-aml-and-sanctions-compliance.html)
