# 온체인 자금세탁 유형 (Typologies)

> 가상자산 자금세탁의 실제 패턴. 어떻게 layering 하는가. 마지막 업데이트: 2026-04-17.

## TL;DR
- 자금세탁자는 온체인의 **익명성 + 속도 + 자동화** 를 최대한 활용
- 핵심 7가지 유형: **믹서, 체인호핑, peel chain, DEX swap, 브리지 활용, 프라이버시코인, OTC 환전**
- 2025-2026 트렌드: **cross-chain laundering** (체인 점프 layering) + **CMLN** (중국어 자금세탁 네트워크)
- 스테이블코인이 불법거래의 **84%** (Chainalysis 2026)
- 탐지는 **클러스터링 + attribution + behavior pattern** 으로

---

## 1. 자금세탁 패턴 7가지

### A. Mixer / Tumbler (믹서)
- **개념**: 여러 사용자의 자금을 한 풀에 섞은 뒤 무작위로 출금 → 입출금 매핑 끊기
- **대표**:
  - **Tornado Cash** (Ethereum) — 2022 OFAC 제재 → 2025-03 해제
  - **Wasabi Wallet** (Bitcoin) — CoinJoin
  - **Samourai Whirlpool** (Bitcoin) — CoinJoin, 2024 운영자 체포
  - **JoinMarket** (Bitcoin) — P2P CoinJoin
- **탐지 신호**: 알려진 믹서 주소 노출, anomalous 입출금 패턴, denomination이 표준화됨

### B. Chain Hopping (체인 점프)
- **개념**: BTC → ETH → USDT(Tron) → BNB → ... 처럼 여러 체인 점프
- **목적**: 분석 도구가 한 체인에서 끊기는 점 노림
- **2026 트렌드**: 가장 많이 쓰이는 layering 방식. **cross-chain bridge가 핵심 인프라**

### C. Cross-chain Bridge 활용
- **개념**: A 체인에서 자금을 잠그고 B 체인에서 wrapped 토큰 발행 → 추적 단절
- **대표 브리지**: Wormhole, LayerZero, Synapse, Stargate, Across, Hop
- **위험**: 브리지 자체가 해킹 표적 (Wormhole $325M, Ronin $625M, Nomad $190M, Multichain $231M)
- **탐지**: 브리지 입출금 짝짓기, 시간/금액 매칭

### D. Peel Chain (껍질 사슬)
- **개념**: 큰 금액 주소에서 **소액씩 떼어내(peel)** 다른 주소로 보내고 잔액은 또 다른 주소로 → 길게 늘여진 사슬 패턴
- **목적**: 사람이 일일이 따라가기 어렵게 만듦
- **탐지**: 그래프 분석 (in-degree/out-degree, 분기 패턴)

### E. DEX Swap (탈중앙거래소 활용)
- **개념**: KYC 없는 DEX(Uniswap, PancakeSwap, Curve)에서 토큰 교환 → 자산 형태 변환
- **layering 효과**: 출처가 ETH인 자금이 USDT, 다른 ERC-20으로 바뀌면 흐름 단절감
- **탐지**: DEX 컨트랙트 노출 + swap 후 행동 패턴

### F. DeFi Lending / Liquidity Pool
- **개념**: Aave/Compound에 입금 → 다른 자산으로 인출, 또는 LP 토큰화
- **layering 효과**: 자산 형태 변환 + 다른 사용자 자금과 혼합
- **탐지**: 비정상적 LP 진입/퇴출 패턴

### G. Privacy Coin
- **Monero (XMR)**: ring signature + stealth address + RingCT — **사실상 추적 불가**
- **Zcash (ZEC)**: zk-SNARK shielded transaction
- **Dash**: PrivateSend (CoinJoin 변형, 약함)
- **거래소 상장 회피 추세**: FATF 권고 + 한국/일본은 사실상 상장 폐지
- **OTC/P2P 환전**으로 들어가서 다시 BTC로 나오는 경로가 일반적

### H. NFT Wash Trading
- **개념**: 자기들끼리 NFT를 사고팔며 가격 부풀려 자금 이전 정당화
- **유형**:
  - **Self-trading** (같은 사람이 양쪽)
  - **Loop trading** (3자 이상 순환)
  - **인플레이션 펌프** (가격 띄워서 외부에 매도)
- **탐지**: 짧은 시간 내 같은 NFT의 반복 거래, 주소 클러스터

### I. OTC Desk (Off-Exchange Counter)
- **개념**: 익명/저KYC OTC desk에서 가상자산 ↔ 법정화폐 환전
- **위험 OTC**: 중국어권 텔레그램 OTC, P2P 거래소(Paxful, LocalBitcoins 폐쇄)
- **CMLN** (Chinese Money Laundering Network)이 이 영역에서 부상 — 2025년 $16.1B 처리

## 2. 자금세탁 3단계 (가상자산 매핑)

| 전통 ML | 가상자산 ML 예시 |
|---|---|
| **Placement** | 현금 → 거래소 입금, OTC 매수, P2P 거래 |
| **Layering** | Mixer, chain hopping, bridge, DEX swap, peel chain, NFT wash |
| **Integration** | OTC 환전, gift card 구매, 부동산/명품 결제 (BitPay 등), 합법사업체 자금화 |

→ 가상자산은 **24~48시간 내 3단계 완주** 가능 (Bybit 사례: 48시간 내 $160M layering 완료).

## 3. 2025-2026 새로운 트렌드

### A. Cross-chain Laundering 가속화
- 단일 체인 분석으로는 추적 불가
- **Chainalysis Crosschain, TRM Multichain Tracing** 같은 cross-chain 도구 부상
- 통계: 2025년 자금세탁의 상당 부분이 multi-chain

### B. CMLN (Chinese Money Laundering Networks)
- **Laundering-as-a-Service** 등장 — 수수료(보통 5~15%) 받고 세탁
- 2025년 $16.1B 처리, 1,800+ 활성 wallet, $40M/일
- 북한·러시아 자금까지 이용
- 텔레그램/위챗 기반 OTC 네트워크와 결합

### C. 스테이블코인 압도적 점유
- 불법거래의 **84%가 스테이블코인** (USDT > USDC > 기타)
- 이유: 가격 안정성 + Tron의 저수수료 + 글로벌 환금성
- 동시에 **freeze 가능** (Tether/Circle이 실제로 SDN/도난자금 freeze) → 양면

### D. 국가 단위 자금세탁
- **러시아 A7A5 stablecoin**: 2025-02 발행 후 1년 내 $93.3B 거래 — 제재 회피 인프라
- **DPRK Lazarus**: 2025년 $2.02B 탈취, 누적 $6.75B

### E. 산업화 (Professionalization)
- 단일 행위자 시대 → **분업 생태계**: 해킹팀, 세탁팀, 환전팀, OTC팀이 각자 전문화
- 마치 SaaS 처럼 서비스로 제공됨

## 4. 탐지 기법 (방어 측)

### A. Address Clustering (주소 클러스터링)
- **Common Input Ownership Heuristic** (UTXO): 같은 트랜잭션의 input 주소들은 한 사람
- **Change Detection**: 거스름돈 주소 식별
- **Deposit Heuristic**: 거래소 입금 주소가 consolidation으로 모이는 패턴

### B. Attribution (행위자 매핑)
- 클러스터를 **알려진 엔티티(거래소, 믹서, OFAC)** 에 연결
- Chainalysis/TRM/Elliptic의 라벨 DB가 이 영역의 핵심 자산

### C. Behavior Pattern Analysis
- peel chain 패턴, mixer 사용 패턴, 시간대 패턴
- 머신러닝 + 룰 베이스 결합

### D. Cross-chain Tracing
- 브리지 입출금 매칭
- 시간/금액/메타데이터 짝짓기

### E. Exposure Score (위험노출도)
- 한 주소가 직접/간접으로 **몇 hop 안에** mixer/SDN/도난자금에 닿는가
- KYT 시스템이 score 계산 → threshold 초과 시 알람

## 5. 탐지의 한계

- **Privacy coin**: 거의 추적 불가 (Monero)
- **Off-chain trade**: 거래소 내부 트랜잭션은 외부에서 안 보임
- **새로운 mixer/bridge**: 라벨링 안 된 시점에는 탐지 어려움
- **Adversarial behavior**: 분석 도구를 회피하는 패턴 학습됨 (예: 분할 금액, 무작위 시간)
- **법적 제한**: 한 회사가 다른 회사 고객 정보 보기 어려움

## 6. 거래소/수탁업자 관점 — 어떤 패턴 알람을 봐야 하나

```
□ 입금 주소가 알려진 mixer/SDN/도난자금에 N hop 내 노출
□ 출금 요청 주소가 위 동일
□ 단기간 내 다수 주소에서 분할 입금 (smurfing)
□ 입금 직후 즉시 전액 출금 (pass-through)
□ 비정상 시간대 거래 (UTC 기준 새벽 등)
□ peel chain 패턴 진입
□ DEX/bridge로의 빈번한 출금
□ NFT wash trading 의심 패턴
□ KYC 정보와 거래 패턴 불일치 (신고소득 대비 거액)
```

## 더 읽을거리
- [`vasp_obligations.md`](vasp_obligations.md) — VASP 의무
- [`defi_nft_risks.md`](defi_nft_risks.md) — DeFi/NFT/프라이버시 코인 상세
- [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) — 블록체인 분석 기법
- [`../notes/6-cases/lazarus-dprk.md`](../notes/6-cases/lazarus-dprk.md) — DPRK 사례
- [Chainalysis 2026 Crypto Crime Report](https://www.chainalysis.com/reports/crypto-crime-2026/)
- [TRM Labs Blog](https://www.trmlabs.com/resources/blog)
