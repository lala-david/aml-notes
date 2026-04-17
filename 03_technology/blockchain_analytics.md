# Blockchain Analytics — 온체인 분석 기법

> KYT의 기술적 기반. 어떻게 익명 주소를 분석하는가. 마지막 업데이트: 2026-04-17.

## TL;DR
- 블록체인 분석의 두 축: **Clustering** (주소 묶기) + **Attribution** (주소→엔티티 매핑)
- 핵심 휴리스틱: **Common Input Ownership, Change Detection, Deposit Heuristic**
- Bitcoin (UTXO 모델) 과 Ethereum (Account 모델) 분석법이 다름
- Cross-chain 추적은 **시간/금액 매칭 + 브리지 인덱싱** 으로
- 한계: privacy coin, 새 mixer, off-chain (CEX 내부) 거래

---

## 1. 두 축: Clustering + Attribution

블록체인 분석은 결국 두 가지 질문에 답하는 것:

1. **이 주소들이 같은 사람인가?** → Clustering
2. **이 클러스터는 누구인가?** → Attribution

> Clustering (구조 분석) + Attribution (라벨 데이터) = 전체 분석 능력

## 2. 주요 클러스터링 휴리스틱

### A. Common Input Ownership (공통 입력 소유권) — Bitcoin
- **가장 기본적이고 강력한 휴리스틱**
- 한 트랜잭션의 여러 input 주소 = 같은 사람이 통제
- 이유: 비트코인은 트랜잭션 서명 시 모든 input의 private key가 필요
- 한계: CoinJoin 같은 multi-party 트랜잭션엔 안 통함

### B. Change Detection (거스름돈 식별)
- UTXO 모델에서 거스름돈은 새 주소로 반환됨
- 휴리스틱:
  - 한 input → 두 output 중 한 쪽이 거스름돈
  - 같은 클러스터 / 새 주소 / 더 작은 금액 등 패턴
- 정확도가 높지 않아 보조 휴리스틱

### C. Deposit Heuristic (거래소 입금 식별)
- 거래소는 사용자별 입금 주소 발급 → 받은 자금을 consolidation 주소로 모음
- 입금 주소 → consolidation 흐름을 따라가면 거래소 클러스터 식별 가능
- 거래소 attribution의 핵심 방법

### D. Behavior-based Clustering (행동 기반)
- 시간대, 금액, 거래 빈도 패턴이 비슷한 주소들
- ML 기반
- 약한 신호지만 다른 휴리스틱과 결합 시 강함

### E. Multi-input Heuristic for Ethereum (계정 모델)
- Ethereum은 UTXO가 아닌 **계정 모델** → Bitcoin 휴리스틱 직접 적용 불가
- 대신:
  - 같은 EOA(Externally Owned Account)가 여러 contract와 상호작용
  - smart contract 호출 패턴
  - gas 지불 주소 분석
  - 같은 ENS 도메인 사용

## 3. Attribution (귀속)

### 데이터 소스
| 소스 | 예시 |
|---|---|
| **자체 거래** | 분석회사가 거래소에 입금해 라벨 확보 |
| **공개 정보** | 거래소가 공개한 hot/cold wallet |
| **다크넷 마켓** | 마켓 운영 관찰로 주소 라벨링 |
| **법집행 정보** | 압수/체포로 노출된 주소 |
| **OFAC SDN** | 정부 발표 |
| **Smart Contract 분석** | 컨트랙트 deployer, 함수 호출 |
| **소셜 / OSINT** | 트위터, 텔레그램에서 주소 노출 |

### 라벨 카테고리 (Chainalysis 기준 예시)
- Exchange (Binance, Upbit, ...)
- DEX (Uniswap, Curve, ...)
- Mixer (Tornado Cash, Wasabi, ...)
- Sanctions (OFAC SDN)
- Stolen Funds (해킹 자금)
- Ransomware (LockBit, BlackCat, ...)
- Darknet Market
- Scam (Pig Butchering, Romance, ...)
- Gambling
- Mining Pool
- High-risk Jurisdiction Exchange
- ATM
- Merchant Service
- ...

## 4. Exposure Score 계산

### Direct Exposure (직접 노출)
- 분석 대상 주소가 위험 주소와 직접 거래

### Indirect Exposure (간접 노출, N-hop)
- N hop 안에서 위험 주소에 도달
- N=1: direct, N=2: 한 단계 거쳐, ...
- 보통 5-hop까지 분석

### 가중치 적용
- 거래 금액
- 시간 거리 (오래된 거래 가중치 ↓)
- 위험 카테고리 (OFAC > mixer > high-risk exchange)

### 예시 점수 계산
```
주소 0xABC...의 risk score:
- Direct exposure to Tornado Cash: 50점
- 2-hop to OFAC SDN: 30점
- Direct exposure to Binance (low risk): 0점
→ 총합 80점 (HIGH)
```

## 5. Cross-chain Tracing

### 도전
- 한 체인에서 끊어진 흐름이 다른 체인에서 시작
- 중간에 wrapped 토큰화 → 같은 가치 다른 형태

### 방법
1. **Bridge Indexing**: 주요 브리지 컨트랙트의 deposit/withdraw 인덱싱
2. **Time/Amount Matching**: bridge에 들어간 금액과 시간 → 다른 체인에서 같은 시점/금액 출금 매칭
3. **Address Pattern**: 같은 주소 형식 사용 시 (보통 Lazarus처럼)
4. **Atomic Swap**: HTLC 기반 cross-chain swap 인덱싱

### 한계
- LayerZero/Wormhole 같은 generic messaging은 매칭 어려움
- 메모(memo) 없이는 정확한 매칭 안 됨
- 익명 brigde (cBridge, Synapse) 활용 시 더 어려움

## 6. UTXO 모델 vs Account 모델 분석

| 측면 | Bitcoin (UTXO) | Ethereum (Account) |
|---|---|---|
| **기본 단위** | UTXO (unspent output) | Account (EOA + Contract) |
| **클러스터링** | Common Input Ownership 강력 | EOA-Contract 패턴 분석 |
| **Smart Contract** | 제한적 (Taproot 이후 확장) | 풍부 (분석 더 복잡) |
| **Token** | (Layer 1엔 없음, Ordinals 등) | ERC-20/721/1155 풍부 |
| **분석 도구 성숙도** | 가장 성숙 | 활발히 발전 중 |

## 7. 분석 도구의 데이터 파이프라인

```
1. Node Operation (자체 풀노드 운영)
   - Bitcoin Core, Geth, Erigon, Reth
   - Archive node (전체 history)
   
2. Indexing
   - 트랜잭션 → 그래프 DB (Neo4j, JanusGraph)
   - 주소 ↔ 트랜잭션 매핑
   
3. Heuristic Clustering
   - 휴리스틱 룰 적용
   - 클러스터 ID 부여
   
4. Attribution
   - 라벨 DB (자체 + 외부)
   - 클러스터 → 엔티티 매핑
   
5. Risk Scoring
   - Exposure 계산
   - 점수 산출
   
6. API / UI
   - 외부 KYT API
   - 분석가용 시각화 도구
```

## 8. ML/AI의 활용

### 적용 영역
- **클러스터링 보조**: 휴리스틱이 잡지 못하는 패턴 발견
- **이상거래 탐지**: 비정상 패턴 학습
- **NFT wash trading 탐지**: 그래프 NN
- **새로운 mixer 식별**: 행위 패턴 분류
- **scam wallet 탐지**: phishing/rug pull 사전 식별

### 한계
- 라벨 데이터 부족 (각 회사가 자체 보유, 공개 안 함)
- adversarial behavior (분석을 회피하는 패턴 학습됨)
- 모델 설명가능성 — 규제 보고 시 "왜 STR 보고했나" 설명 필요

## 9. 자체 구축 vs 벤더 활용

### 벤더 활용 장점
- 라벨 DB가 핵심 자산 → 자체 구축 거의 불가능
- 글로벌 attribution
- 규제 당국이 인정하는 표준 도구

### 자체 구축 장점
- 비용 절감 (대형사)
- 한국 특화 라벨 (현지 거래소, 사기 wallet)
- 사내 데이터와 결합 분석

### 현실
- 대부분 **하이브리드** — 외부 KYT API + 자체 한국 특화 분석
- 한국 주요 거래소/수탁사도 Chainalysis/TRM 사용 + 자체 분석

## 10. 한계와 미래

### 한계
- Privacy coin (Monero) 거의 분석 불가
- 새 mixer / 새 bridge 라벨링 lag time
- Off-chain (CEX 내부 거래) 안 보임
- Adversarial: AI 시대에 자금세탁 자동화도 발전

### 미래 방향
- **AI 기반 패턴 탐지** 강화
- **Cross-chain analytics** 표준화
- **ZKP 적용** — 프라이버시 + 컴플라이언스 양립 시도
- **공유 attribution DB** 가능성 (산업 협력)

## 더 읽을거리
- [`kyc_kyt_overview.md`](kyc_kyt_overview.md) — KYT의 운영적 측면
- [`travel_rule_protocols.md`](travel_rule_protocols.md) — VASP 식별과의 관계
- [`../02_crypto_aml/onchain_typology.md`](../02_crypto_aml/onchain_typology.md) — 자금세탁 패턴
- [`../05_solutions_market/analytics_vendors.md`](../05_solutions_market/analytics_vendors.md) — 벤더 비교
- [TRM Labs — Blockchain Analytics 정의](https://www.trmlabs.com/glossary/blockchain-analytics)
- [Elementus — Data Science Heuristics](https://www.elementus.io/blog-post/decoding-the-chain-how-data-science-based-heuristics-reveal-blockchain-networks)
- [AMLBot — Wallet Clustering](https://blog.amlbot.com/wallet-and-entity-identification-in-blockchain-analytics/)
- [Heuristic-Based Address Clustering in Bitcoin (논문)](https://www.researchgate.net/publication/347083664_Heuristic-Based_Address_Clustering_in_Bitcoin)
