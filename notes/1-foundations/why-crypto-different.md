# Why Crypto AML? — 가상자산 AML이 왜 다른가

> 전통 금융 AML과 가상자산 AML의 본질적 차이. 이 글을 읽고 나면 "공개 원장인데 왜 어려운가"라는 직관적 모순을 설명할 수 있고, 가상자산 AML이 투자한 도구 지형(mixer, bridge, stablecoin)의 **왜**를 이해하게 됩니다. 마지막 업데이트: 2026-04-17.

## TL;DR
- 가상자산은 **공개 원장(public ledger)** 이라 추적이 오히려 쉬움 → 하지만 실무는 어려움, 이게 "투명성의 역설"
- 운영 난이도가 폭증하는 이유: **속도·24/7·국경 없음·익명 주소·스마트컨트랙트·체인 다양성**
- 자금세탁자는 **mixer / cross-chain bridge / DeFi / privacy coin / 스테이블코인** 을 layering 도구로 활용
- 2025년 기준 **불법 거래의 84%가 스테이블코인**에서 발생 (Chainalysis 2026 Crypto Crime Report)
- 그래서 가상자산 AML은 **온체인 분석(KYT) + 오프체인 KYC** 의 결합이 핵심

---

## 1. 전통 금융 AML과 가상자산 AML의 구조적 차이

### 왜 "다르다"를 먼저 이해해야 하나

은행 AML 경력자가 가상자산 회사에 들어오면 가장 먼저 혼란을 겪는 지점이 **"원칙은 같은데 도구가 완전히 다르다"** 입니다. 고객확인(KYC), 의심거래보고(STR), 제재 스크리닝 — 용어는 같지만 실행 환경이 판이하게 달라서, 전통 금융 룰북을 그대로 가져오면 작동하지 않습니다. 이 섹션은 그 차이를 한 표로 잡고 갑니다.

용어:
- **VASP (Virtual Asset Service Provider)** — 가상자산사업자. FATF 정의로 매도·매수·교환·이전·보관·관련 금융서비스를 영업으로 하는 자. 한국 특금법 §2는 동일한 정의를 차용.
- **Public Ledger (공개 원장)** — 누구나 블록 탐색기(예: Etherscan)로 열람 가능한 거래 기록 데이터베이스. 블록체인의 본질 속성.
- **Finality (결제 완결성)** — 한 번 확정된 거래는 되돌릴 수 없음. 비트코인은 6 confirmation, 이더리움 PoS는 슬롯 2개 정도.

### 이 표를 어떻게 읽어야 하나

왼쪽이 전통 은행에서 당연하게 여겨지는 속성, 오른쪽이 가상자산 환경에서 그 속성이 어떻게 바뀌거나 사라지는지를 대조합니다. 가상자산 AML 설계의 거의 모든 어려움은 이 9개 행 중 어느 하나에서 비롯됩니다.

| 항목 | 전통 금융 (은행) | 가상자산 (VASP/온체인) |
|---|---|---|
| 거래 원장 | 비공개 (은행 내부) | **공개 원장 (public blockchain)** |
| 거래 속도 | 영업시간·결제망 의존 (T+1~T+3) | **24/7, 분 단위 결제(finality)** |
| 국경 | 환거래은행 네트워크 거쳐야 함 | **국경 자체가 의미 없음** |
| 식별자 | 계좌번호 = 실명 연결됨 | **주소(address) = 가명(pseudonym)** |
| 거래 방식 | 송금 지시 → 은행이 처리 | **사용자가 직접 서명, 즉시 확정** |
| 자금흐름 차단 | 동결(freeze) 가능 | 일반 자산은 차단 불가, **스테이블코인은 발행자가 freeze 가능** |
| 자산 종류 | 통화 단일 | 수만 개 토큰, NFT, 합성자산, 파생상품 |
| 중개 | 항상 중개자 존재 | **DeFi는 중개자 없음 (코드가 중개)** |
| 신원 확인 | 지점·오피스에서 대면 가능 | **100% 비대면(non-face-to-face)** |

### 실무 포인트

표의 각 행이 AML 통제의 어느 부분을 무너뜨리는지 한 줄로 정리하면: **공개 원장**은 KYT를 가능하게 하지만, **가명 주소**는 KYC 없이 KYT만으로는 주체 식별이 불가, **24/7·국경 없음**은 실시간 통제를 강제, **비가역성**은 사후 조치(동결·환원) 불가를 의미. 이 조합 때문에 가상자산 AML은 "Pre-transaction screening"(거래 발생 전 차단)의 비중이 전통 금융과 비교할 수 없게 커집니다.

---

## 2. 투명성의 역설 — 공개 원장인데 왜 어려운가

### 핵심 긴장점

가상자산은 모든 거래가 공개 블록체인에 기록되므로 **이론상으로는 누구나 흐름을 본다**. 이 속성만 놓고 보면 가상자산은 전통 금융보다 오히려 AML에 유리해 보입니다. 그런데 현실 AML 실무는 정반대 — 왜?

답은 **"보인다"와 "식별된다"는 다르다**는 한 줄에 있습니다. 공개 원장에는 주소(예: `0x7F...`)가 적혀 있지 실명이 적혀 있지 않습니다. 주소를 **사람·법인과 연결**하는 일이 별개 작업이며, 이게 블록체인 분석 산업의 본질적 가치입니다.

용어:
- **Pseudonymity (가명성)** — 실명은 아니지만 특정 식별자(주소)에 행동 이력이 계속 축적되는 속성. 완전 익명(anonymity)과는 다름.
- **Address (주소)** — 블록체인 상 자금의 목적지. 비트코인은 `bc1...`, 이더리움은 `0x...`. 한 사람이 수만 개 만들 수 있음.
- **Address Attribution (주소 귀속)** — 주소/클러스터를 알려진 엔티티(거래소, Tornado Cash, OFAC SDN 등)에 연결하는 작업.

### 추적을 막는 7가지 실무 장애물

1. **주소 ≠ 사람** — 한 사람이 수십~수만 개 주소를 자유롭게 만듦. 표준 지갑(MetaMask 등)이 자동으로 새 주소를 생성하므로 사용자는 인식조차 안 하고 클러스터를 키움.
2. **체인이 너무 많음** — Bitcoin, Ethereum, Solana, Tron, BNB, Polygon, Avalanche, Sui, Aptos에 L2(Arbitrum, Optimism, Base, zkSync) 수십 개. 각각 데이터 구조·주소 형식이 다름.
3. **Cross-chain Bridge** — A 체인에서 자금을 잠그고 B 체인에서 대응 토큰을 발행. 분석 도구는 한 체인만 추적하다 B로 연결된 순간 **추적 단절**이 생김.
4. **익명·프라이버시 도구** — Mixer(Tornado Cash, Wasabi), Privacy Coin(Monero, Zcash). Monero는 링 서명+stealth address로 **사실상 추적 불가** 수준.
5. **DeFi의 무중개성** — KYC 없는 DEX(Uniswap, Curve), lending(Aave), AMM(Automated Market Maker)이 layering 인프라가 됨. 규제가 "사업자"를 식별할 수 없는 환경.
6. **스마트컨트랙트 복잡성** — 한 트랜잭션이 수십 개 internal call을 유발. 분석 도구가 각 internal call의 자금 효과까지 풀어내야 함.
7. **속도** — 2025-02 Bybit 해킹에서 **48시간 내 $160M이 mixer→bridge→OTC로 layering** 완료. 전통 금융 AML의 T+1 주기에서는 상상할 수 없는 템포.

### 왜 블록체인 분석 산업이 탄생했나

위 7개를 풀어내려면 **"주소 → 엔티티"** 매핑 DB가 필수. 이 DB는 하루아침에 만들 수 없고, CIOH(Common Input Ownership Heuristic, 공통 입력 소유 휴리스틱) 같은 알고리즘 + 수년간 쌓아 온 라벨링 + 다크웹 OSINT + 거래소 협업으로만 만들어집니다. Chainalysis·Elliptic·TRM Labs·Crystal·Merkle Science가 쌓아 올린 attribution DB가 이 산업의 moat입니다.

### 실무 포인트

"우리 회사는 블록체인 분석 도구를 사지 않고 자체 개발하겠다"는 계획은 대부분 실패합니다. 왜냐하면 자체 개발은 알고리즘(CIOH, change detection)은 베낄 수 있어도 **누적 라벨링**을 따라잡을 수 없기 때문. 실무에서는 Chainalysis/TRM/Elliptic 중 1개를 기본 도구로 쓰고, 자체 개발은 한국 거래소 attribution 같은 **국지적 보완**에 제한하는 구조가 표준입니다.

---

## 3. 가상자산 자금세탁의 새로운 도구들

### 개요

전통 ML의 도구(smurfing, shell company 등)는 가상자산에서도 그대로 쓰이지만, 가상자산만의 추가 도구가 5~6가지 있습니다. 각 도구는 자금세탁 3단계 중 주로 **Layering**에 집중돼 있고, 도구별로 탐지 방법이 다르므로 KYT 룰 세트도 도구별로 분리해 관리하는 게 표준입니다.

### Mixer / Tumbler — 자금 섞기

여러 사용자의 자금을 한 풀(pool)에 모아 섞은 뒤 다시 뽑아내는 서비스. 입금 주소와 출금 주소의 **온체인 연결을 끊는** 것이 목적.

- **Tornado Cash** — Ethereum 기반. zk-SNARK(영지식 증명)로 풀에서 뽑을 때 "내가 입금한 사람"이라는 사실만 증명하고 어느 입금이었는지는 가립. 2022-08 OFAC 제재 → 2024-11 Van Loon v. Treasury 5th Circuit 판결 → 2025-03-21 지정 해제.
- **Wasabi / Samourai** — Bitcoin CoinJoin. 여러 사용자가 동시에 동일 금액을 섞는 방식. Samourai 개발자는 2024년 체포.

**탐지 포인트**: Mixer는 특유의 **트랜잭션 지문(fingerprint)** 이 있음 — 균등 금액, 특정 output 수, 특정 스크립트 패턴. KYT는 이 지문으로 mixer 입출금 주소 클러스터를 자동 라벨링함.

### Cross-chain Bridge — 체인 점프

A 체인에서 자금을 잠그고 B 체인에서 같은 가치의 토큰을 발행하는 프로토콜.

- 예: ETH(Ethereum) → wBTC(Ethereum) → BTC(Bitcoin) 브리지
- 2025~2026년 자금세탁 트렌드 1위가 **cross-chain laundering** — FBI·Chainalysis 모두 같은 결론
- Lazarus가 애용하는 THORChain, Stargate, ChainFlip, Across

**탐지 어려운 이유**: 브리지 진입 측과 출구 측이 **서로 다른 체인**이라, KYT 도구가 두 체인을 함께 보지 않으면 흐름이 끊어진 것처럼 보임. Chainalysis Crosschain Tracing, TRM Labs Universal 같은 기능이 이 문제를 정확히 겨냥.

### Chain Hopping — 체인 점프의 연장

BTC → ETH → USDT(Tron) → BNB → XMR(Monero) → ... 처럼 여러 체인을 점프하며 흔적을 흐리는 기법. Cross-chain bridge의 조합으로 실현.

### Peel Chain — 긴 사슬로 떼어내기

큰 금액이 들어온 주소에서 **소액을 한 번씩 떼어내(peel)** 다른 주소로 보내고, 나머지는 또 다른 주소로. 이 과정을 수십~수백 번 반복해 **긴 사슬 모양**의 흐름을 만듦.

**왜 쓰나**: 수사기관이 "첫 주소"에서 "마지막 환전 주소"까지 추적하려면 수십 단계를 거쳐야 하고, 중간에 exchange deposit이 섞이면 끊기기 쉬움. **전통 금융의 smurfing(분할입금)의 온체인 버전**이라고 이해하면 직관적.

**탐지 포인트**: Peel chain은 시각적 특징이 강함 — 한 주소에서 거의 같은 간격으로 비슷한 소액이 빠져나가는 패턴. 그래프 분석 도구에서 쉽게 발견.

### DeFi 활용 — 무중개 Layering

DeFi(Decentralized Finance, 탈중앙 금융) 프로토콜은 KYC를 요구하지 않으므로 layering 인프라로 자주 악용됨.

- **Swap (DEX)** — Uniswap, Curve, PancakeSwap. 토큰 A를 토큰 B로 바꿔 **자산 형태 변환**.
- **Lending / Liquidity Pool** — Aave, Compound. 토큰 입금 후 다른 자산으로 인출하거나, LP 토큰 발행 → 소각으로 출처 흐림.
- **Flash Loan** — 한 트랜잭션 안에서 대출→사용→상환을 마치는 기술. 복잡한 swap chain을 한 번에 실행해 분석 난이도를 높임.
- **NFT Wash Trading** — 자기들끼리 NFT를 고가에 사고팔며 **가격을 부풀려** 자금 이전을 정당화. 2024~2025년 주요 typology.

### Privacy Coin — 설계 자체가 익명

- **Monero (XMR)** — Ring signature(서명자 여러 명 중 누군지 모름) + stealth address(받는 주소가 매 거래마다 새로 생성) + RingCT(금액도 가림). 사실상 추적 불가. FATF 권고에서 "privacy coin은 거래소 상장 금지 검토"라 명시.
- **Zcash (ZEC)** — zk-SNARK 기반 shielded transaction. 다만 많은 사용자가 비shielded 모드를 써서 실제 익명성은 Monero보다 약함.

한국·일본 주요 거래소는 대부분 privacy coin을 상장 폐지했습니다 — 규제 부담이 매출보다 크다는 판단.

### 스테이블코인의 부상

2025년 불법 거래의 **84%가 스테이블코인** (USDT, USDC 등) — Chainalysis 2026 Crypto Crime Report.

**왜 이 비중이 커졌나**:
- 가격 변동성 없음 → 시간 지연 동안 손실 위험 X
- Tron USDT 같은 저수수료 체인에서 국경을 초월한 결제 가능
- 글로벌 환금성 (전 세계 거래소에서 거래됨)
- OTC 네트워크가 USDT 기준으로 형성돼 환전 편의성 최고

**양날의 검**: 동시에 **발행자(Tether, Circle)가 freeze/burn 가능**. OFAC가 주소를 제재 지정하면 Tether/Circle은 그 주소의 USDT를 동결하며, 심한 경우 burn(소각)까지 수행. 가상자산 중 **유일하게 동결 가능**한 자산군이라는 점에서 제재 집행의 지렛대로 쓰임.

### 실무 포인트

KYT 룰 세트를 처음 설계할 때는 **6개 도구별 하위 룰 그룹**으로 나누는 게 유지보수에 유리합니다: (1) Mixer exposure, (2) Bridge exposure, (3) Peel chain pattern, (4) DeFi anomaly, (5) Privacy coin touch, (6) Sanctioned stablecoin. 룰이 섞이면 false positive 원인을 역추적하기 어려워지기 때문.

---

## 4. 위협 행위자 지형

### 이 표를 어떻게 읽어야 하나

AML 부서가 실시간으로 방어해야 할 주요 위협 행위자 목록입니다. **규모**와 **수법**이 다 다르므로 방어 전략도 차별화해야 합니다 — Lazarus는 사고 후 48시간 대응이, CMLN은 지속적 KYC 품질이, 랜섬웨어는 피해자 주소 블랙리스트 공유가 핵심입니다.

| 행위자 | 주요 활동 | 규모 |
|---|---|---|
| **DPRK Lazarus Group** | 거래소·wallet 공급망 해킹 | 2025년 $2.02B 탈취, 누적 $6.75B |
| **Chinese Money Laundering Networks (CMLN)** | Laundering-as-a-Service (텔레그램·위챗 OTC) | 2025년 $16.1B 처리, 1,800+ 활성 wallet |
| **랜섬웨어 그룹** | 피해자에게 BTC 요구 후 mixer 세탁 | 연 수억 달러 |
| **다크넷 마켓** | 마약·무기·해킹툴 거래 | 감소 추세지만 여전 활동 |
| **Pig Butchering / Romance Scam 조직** | 동남아·아프리카 인신매매 결합 사기 | 2025년 사기 규모 $17B |
| **국가 차원 제재 회피** | 러시아 A7A5 stablecoin ($93.3B/년 거래) | 국가 단위 |

### 각 행위자의 고유한 운영 특성

- **Lazarus Group** — 북한 정찰총국(RGB) 산하. 목표는 **핵·미사일 프로그램 외화 조달**. 공급망 공격(3rd-party wallet provider 침투)에 능숙하고 **48시간 playbook**(분산→bridge→mixer→CMLN OTC)이 정형화됨.
- **CMLN** — 개별 조직이 아니라 **네트워크**. 텔레그램·위챗에서 "USDT를 인민폐로 5% 수수료 환전" 광고. Lazarus 세탁의 환전 파트너 역할을 하지만 일반 범죄수익도 서비스.
- **Pig Butchering** — 동남아 범죄조직이 인신매매한 인력을 **사기 농장**에 투입. 피해자에게 가짜 투자 플랫폼을 유도해 가상자산을 이체시킴. 2025년 기준 연 $17B 규모로 **단일 typology 중 최대**.

### 실무 포인트

"회사 고객에게 어느 행위자와의 접촉 가능성이 높은가"를 기반으로 KYT 룰 우선순위를 정해야 합니다. B2C 한국 거래소라면 **Pig Butchering(피해자의 출금) + Romance Scam + 국내 보이스피싱**이 1순위, B2B 수탁업자라면 **Lazarus 공급망 + 제재 회피**가 1순위. 전체를 다 동일한 강도로 보는 건 자원 낭비입니다.

---

## 5. 가상자산 AML은 운영 관점에서 어떻게 다른가

### 이 표를 어떻게 읽어야 하나

같은 AML 의무(왼쪽 열)가 두 세계에서 어떻게 다른 도구로 구현되는지 보여줍니다. 가상자산 AML 팀을 새로 만들 때 이 6행 각각에 **전담 인프라·벤더·운영 SOP**가 필요하다는 걸 먼저 내부에 설명하는 게 예산 승인의 출발점입니다.

| AML 의무 | 전통 금융 | 가상자산 |
|---|---|---|
| **KYC** | 신분증, 대면확인, 주소증빙 | 100% 비대면 + **지갑 주소 소유 증명(Proof of Address Ownership)** |
| **거래 모니터링** | 룰 기반 TM 시스템 | 룰 + **온체인 KYT** (주소 위험점수, 클러스터 분석) |
| **Travel Rule** | SWIFT MT103에 송금정보 포함 | **별도 메시징 프로토콜 필요(IVMS101)**, 미연결 VASP는 sunrise 문제 |
| **제재 스크리닝** | 이름·생년월일 매칭 | 이름 + **지갑 주소 매칭(OFAC SDN 주소 목록)** |
| **STR** | 거래 패턴 기반 | 거래 패턴 + **온체인 노출(exposure) 기반** |
| **기록보관** | 5~10년 | 한국 **거래정보 15년** (가상자산이용자보호법 §11) + **AML 기록 5년** (특금법 §5의4) |

### 세 가지 결정적 전환

1. **Proof of Address Ownership** — 고객이 "이 지갑은 내 것"이라는 증명을 해야 Travel Rule 송수신이 가능. 실무에서는 거래소가 제공한 랜덤 문자열을 개인 지갑으로 서명해서 제출하는 방식이 표준. 전통 금융에는 없는 절차.
2. **Travel Rule의 Sunrise 문제** — 전 세계 VASP가 모두 FATF R.16을 동시에 이행하지 못해 **연결되지 않은 관할이 다수**. 한국 VASP가 연결 안 된 외국 VASP에게 송금하면 정보 교환 자체가 불가능하고, 규제는 이 경우 송금 거절 또는 자체 검토 후 결정을 요구.
3. **Exposure Score** — 전통 금융 STR은 "거래 패턴"만 보지만, 가상자산 STR은 **수신 주소가 OFAC에 얼마나 가까운지(1-hop, 2-hop, ...)** 를 정량 지표로 포함. 이게 KYT 벤더의 핵심 출력.

### 실무 포인트

전통 금융 AML 베테랑을 가상자산 회사에 신규 합류시킬 때 가장 먼저 이 3가지 전환을 교육하면 기존 경력이 70% 이상 이식 가능합니다. 반대로 이 3가지를 무시하면 "은행에서 하던 방식"이 가상자산 환경에서 오작동해 컴플라이언스 사고로 연결되기 쉽습니다.

---

## 요약 부록 — 빠른 참조용

**투명성의 역설**: 공개 원장 = 추적 가능 ✓ / 가명 주소 = 식별 불가 ✗ → 블록체인 분석 DB가 해결책
**6대 layering 도구**: Mixer · Cross-chain Bridge · Chain Hopping · Peel Chain · DeFi · Privacy Coin
**스테이블코인 역설**: 불법 거래 84%를 차지하지만 **유일하게 발행자가 freeze 가능**한 가상자산

## 더 읽을거리
- [`what-is-aml.md`](what-is-aml.md) — AML 3단계 모델 기초
- [`key-concepts.md`](key-concepts.md) — KYC·KYT·CDD·EDD 용어 체계
- [`../3-crypto-aml/onchain-typology.md`](../3-crypto-aml/onchain-typology.md) — 온체인 자금세탁 유형 상세
- [`../6-cases/lazarus-dprk.md`](../6-cases/lazarus-dprk.md) — DPRK·Bybit 사례 심화
- [Chainalysis 2026 Crypto Crime Report](https://www.chainalysis.com/reports/crypto-crime-2026/)
