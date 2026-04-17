# Why Crypto AML? — 가상자산 AML이 왜 다른가

> 전통 금융 AML과 가상자산 AML의 본질적 차이. 마지막 업데이트: 2026-04-17.

## TL;DR
- 가상자산은 **공개 원장(public ledger)** 이라 추적은 오히려 쉬움 → "투명성의 역설"
- 그러나 **속도/24-7/국경 없음/익명 주소/스마트컨트랙트/체인 다양성** 으로 운영 난이도가 폭증
- 자금세탁자는 **mixer / cross-chain bridge / DeFi / privacy coin / 스테이블코인** 을 layering 도구로 활용
- 2025년 기준 **불법 거래의 84%가 스테이블코인**에서 발생 (Chainalysis 2026 Crypto Crime Report)
- 그래서 가상자산 AML은 **온체인 분석(KYT) + 오프체인 KYC** 의 결합이 핵심

---

## 1. 전통 금융 AML과 가상자산 AML 비교

| 항목 | 전통 금융 (은행) | 가상자산 (VASP/온체인) |
|---|---|---|
| 거래 원장 | 비공개 (은행 내부) | **공개 원장 (public blockchain)** |
| 거래 속도 | 영업시간/결제망 의존 (T+1~T+3) | **24/7, 분 단위 결제(Finality)** |
| 국경 | 환거래은행 네트워크 거쳐야 함 | **국경 자체가 의미 없음** |
| 식별자 | 계좌번호 = 실명 연결됨 | **주소(address) = 가명(pseudonym)** |
| 거래 방식 | 송금 지시 → 은행이 처리 | **사용자가 직접 서명, 즉시 확정** |
| 자금흐름 차단 | 동결(freeze) 가능 | 일반 자산은 차단 불가, **스테이블코인은 발행자가 freeze 가능** |
| 자산 종류 | 통화 단일 | 수만 개 토큰, NFT, 합성자산, 파생상품 |
| 중개 | 항상 중개자 존재 | **DeFi는 중개자 없음 (코드가 중개)** |
| 신원 확인 | 지점/오피스에서 대면 가능 | **100% 비대면(non-face-to-face)** |

## 2. "투명성의 역설" — 추적은 쉬운데 왜 어려운가

가상자산은 모든 거래가 공개 블록체인에 기록되므로 **이론적으로는 누구나 흐름을 본다**. 전통 금융은 이걸 못 함.

그런데 실무에서 어려운 이유:

1. **주소(address) ≠ 사람(identity)** — 한 사람이 수십~수만 개 주소를 만듦
2. **체인이 너무 많음** — Bitcoin, Ethereum, Solana, Tron, BNB, Polygon, Avalanche, ... 그리고 L2 (Arbitrum, Optimism, Base, ...)
3. **체인 간 이동(cross-chain bridge)** — 흐름이 한 체인에서 끊어지고 다른 체인에서 다시 시작
4. **익명/프라이버시 도구** — Mixer (Tornado Cash, Wasabi), Privacy coin (Monero, Zcash)
5. **DeFi의 무중개성** — KYC 없는 DEX, lending, AMM이 layering 인프라가 됨
6. **스마트컨트랙트의 복잡성** — 한 트랜잭션이 수십 개 내부호출(internal call)을 일으킴
7. **속도** — 사고 발생 후 **48시간 내** 수억 달러가 mixer를 거쳐 OTC로 빠짐 (Bybit 사례)

→ 그래서 **블록체인 분석(blockchain analytics)** 이라는 새로운 산업이 등장. Chainalysis, Elliptic, TRM Labs, Crystal, Merkle Science 등.

## 3. 가상자산 자금세탁의 새로운 도구들

전통 ML 도구 (smurfing, shell company 등) 외에 가상자산만의 layering 도구:

### Mixer / Tumbler
- 여러 사용자의 자금을 섞어 입출금 관계를 끊음
- 예: **Tornado Cash** (Ethereum 기반, 2022년 OFAC 제재 → 2025년 3월 제재 해제), Wasabi/Samourai (Bitcoin CoinJoin)

### Cross-chain Bridge
- A 체인에서 자금을 잠그고 B 체인에서 같은 가치의 토큰을 발행 → 추적이 끊어짐
- 2025-2026년 자금세탁 트렌드 1위가 **cross-chain laundering** (체인 점프 layering)

### Chain Hopping
- BTC → ETH → USDT(Tron) → BNB → XMR → ... 처럼 여러 체인을 점프하며 흔적 흐림

### Peel Chain
- 큰 금액 주소에서 소액씩 떼어내(peel) 다른 주소로 보내고, 나머지는 또 다른 주소로 — 길게 늘여진 사슬 패턴

### DeFi 활용
- **Swap (DEX)**: KYC 없이 토큰 교환 → 자산 형태 변환
- **Lending/Liquidity Pool**: 입금 후 다른 자산으로 인출 → 출처 단절 효과
- **Wash trading on NFT**: 자기들끼리 NFT를 사고팔며 가격 부풀려 자금 이전 정당화

### Privacy Coin
- **Monero (XMR)**: ring signature + stealth address로 거의 추적 불가 → FATF 권고에서 사실상 거래소 상장 금지 권고
- **Zcash (ZEC)**: shielded transaction (zk-SNARK)

### 스테이블코인의 부상
- 2025년 불법 거래의 **84%가 스테이블코인** (USDT, USDC 등) — Chainalysis 2026
- 이유: 가격 변동성 없음 + 글로벌 환금성 + Tron 같은 저수수료 체인 활용
- 동시에 **발행자(Tether, Circle)가 freeze/burn 가능** → 양날의 검

## 4. 위협 행위자 지형

가상자산을 표적으로 하거나 도구로 쓰는 주요 행위자:

| 행위자 | 주요 활동 | 규모 |
|---|---|---|
| **DPRK Lazarus Group** | 거래소/wallet 공급망 해킹 | 2025년 $2.02B 탈취, 누적 $6.75B |
| **Chinese Money Laundering Networks (CMLN)** | Laundering-as-a-Service | 2025년 $16.1B 처리, 1,800+ 활성 wallet |
| **랜섬웨어 그룹** | 피해자에게 BTC 요구 후 mixer 세탁 | 연 수억 달러 |
| **다크넷 마켓** | 마약·무기·해킹툴 거래 | 감소 추세지만 여전 활동 |
| **Pig Butchering / Romance Scam 조직** | 동남아/아프리카 인신매매 결합 | 2025년 사기 규모 $17B |
| **국가 차원 제재 회피** | 러시아 A7A5 stablecoin ($93.3B/년 거래) | 국가 단위 |

## 5. 그래서 가상자산 AML은 어떻게 다른가 — 운영 관점

| AML 의무 | 전통 금융 | 가상자산 |
|---|---|---|
| **KYC** | 신분증, 대면확인, 주소증빙 | 100% 비대면 + **지갑 주소 소유 증명 (Proof of Address Ownership)** |
| **거래 모니터링** | 룰 기반 TM 시스템 | 룰 + **온체인 KYT** (주소 위험점수, 클러스터 분석) |
| **Travel Rule** | SWIFT MT103에 포함 | **별도 메시징 프로토콜 필요 (IVMS101)**, 미연결 VASP는 sunrise 문제 |
| **제재 스크리닝** | 이름/생년월일 매칭 | 이름 + **지갑 주소 매칭 (OFAC SDN 주소 목록)** |
| **STR** | 거래 패턴 기반 | 거래 패턴 + **온체인 노출(exposure) 기반** |
| **기록보관** | 5~10년 | 한국 **15년** (이용자보호법) |

## 더 읽을거리
- [`what_is_aml.md`](what_is_aml.md) — AML 기초
- [`../notes/3-crypto-aml/onchain-typology.md`](../notes/3-crypto-aml/onchain-typology.md) — 온체인 자금세탁 유형 상세
- [`../notes/6-cases/lazarus-dprk.md`](../notes/6-cases/lazarus-dprk.md) — DPRK 사례
- [Chainalysis 2026 Crypto Crime Report](https://www.chainalysis.com/reports/crypto-crime-2026/)
