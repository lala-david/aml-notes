# Lazarus / DPRK — 북한 사이버 자금세탁

> 가상자산 업계 1순위 위협 행위자. Bybit $1.5B 사건. 마지막 업데이트: 2026-04-17.

## TL;DR
- **Lazarus Group** = 북한 정부 후원 사이버 부대 (Bureau 121, RGB 산하)
- 2025년 단일 해 **$2.02B 탈취** (전년 대비 +51%), **누적 $6.75B**
- **2025-02-21 Bybit hack $1.5B** — 단일 사건 사상 최대
- 자금세탁 핵심: **48시간 내 mixer + cross-chain bridge + Chinese Money Laundering Network (CMLN)** 활용
- FBI 명칭: **TraderTraitor** (Lazarus의 한 sub-cluster)
- 2025년 service compromises의 **76%가 DPRK**
- 핵 미사일 프로그램 자금조달원으로 의심

---

## 1. Lazarus Group이란

### 정체성
- 북한 정부 후원 advanced persistent threat (APT) 그룹
- **북한 정찰총국(RGB) 산하**, Bureau 121 등 부대
- 2009년경부터 활동
- 미국 OFAC 제재 (2019)

### 활동 영역
| 시기 | 활동 |
|---|---|
| 2009~2014 | DDoS, wiper 공격 (한국 농협 등) |
| 2014 | Sony Pictures 해킹 |
| 2016 | **Bangladesh Bank SWIFT $81M** (전통 금융) |
| 2017 | **WannaCry 랜섬웨어** |
| 2017~ | **가상자산 거래소 해킹 본격화** |
| 2022 | **Ronin Bridge $625M** (Axie Infinity) |
| 2024-2025 | DeFi/Bridge/거래소 대거 공격 |
| **2025-02** | **Bybit $1.5B** (사상 최대) |

### Sub-cluster
- **Lazarus** (광범위)
- **APT38** — 금융 표적
- **TraderTraitor** (FBI) — 가상자산 표적, 가짜 채용
- **Bluenoroff** — 핀테크 표적

## 2. 2025-02-21 Bybit Hack — 사상 최대

### 사실 관계
- **2025-02-21**: Bybit cold wallet에서 **약 $1.5B (ETH)** 탈취
- 공격 방식: **공급망 공격** — 제3자 wallet provider 침투, signing 인터페이스 변조
- Bybit 운영진은 정상 트랜잭션으로 알고 서명 → 자산 이전
- **2025-02-26** FBI가 공식 라자루스 귀속 발표

### 자금세탁 흐름
- **48시간 내 $160M layering 완료**
- 2026-03 시점:
  - $400M 추적 + 부분 환전됨
  - $1.1B 잔여 추적 중 (다양한 wallet cluster)
- 사용 도구:
  - **Cross-chain bridge** (THORChain 등)
  - **DEX swap** (Uniswap, Curve, etc.)
  - **CMLN (중국어 자금세탁 네트워크) OTC desk**

### 임팩트
- 거래소 보안 표준 재검토 (다중 서명 흐름)
- 미국 의회 청문회
- US 의회 가상자산 보안 입법 가속화
- Bybit는 자체 자금으로 사용자 손실 보전

## 3. DPRK 가상자산 활동 통계 (2025)

### 탈취 금액
- **2025**: $2.02B (전년 +51%)
- **누적**: $6.75B (Lazarus 가상자산 탈취 시작 이후)
- **2025 전체 service compromises의 76%가 DPRK**

### 주요 사건
| 연도 | 사건 | 금액 |
|---|---|---|
| 2017 | Yapizon (한국) | ~$5M |
| 2018 | Coinrail (한국) | $40M |
| 2018 | Coincheck (일본) | $530M (NEM) |
| 2019 | UpBit (한국) | $50M |
| 2020 | KuCoin | $280M |
| 2021 | Liquid (일본) | $97M |
| 2022 | **Ronin Bridge** | **$625M** |
| 2022 | Harmony Horizon | $100M |
| 2023 | Atomic Wallet | $100M |
| 2023 | Stake.com | $41M |
| 2024 | DMM Bitcoin (일본) | $305M |
| **2025** | **Bybit** | **$1.5B** |
| 2025 | WazirX (인도) | $230M |
| 2025 | 다수 거래소/DeFi | 합계 다수 |

## 4. 자금세탁 패턴 (Lazarus Playbook)

### Step 1. 즉시 분산
- 탈취 직후 수십~수백 wallet으로 분산 (peel chain)
- 각 wallet으로 작은 금액씩

### Step 2. Cross-chain Bridge
- ETH → BTC, ETH → BNB, ETH → Tron 등
- THORChain, Stargate, ChainFlip, Across 등 활용
- 분석 도구의 한 체인 추적 단절

### Step 3. DEX Swap
- Uniswap, PancakeSwap, Curve 등에서 자산 형태 변환
- KYC 없는 환경

### Step 4. Mixer
- Tornado Cash (2025-03 제재 해제 후 다시 활용)
- Wasabi, Samourai (2024 운영자 체포 전까지)
- 최근에는 새로운 mixer/CoinJoin 변형 시도

### Step 5. OTC 환전
- **CMLN (중국어 자금세탁 네트워크)**: 텔레그램/위챗 OTC
- 5~15% 수수료
- 가상자산 → 위안화 / USD / 현금
- 또는 USDT(Tron) 형태 유지하며 "환금 가능" 자산으로 보유

### Step 6. 북한 자금화
- 중간책을 거쳐 평양 송금
- 사치품 구매 / 핵·미사일 부품 / 사이버 인프라

## 5. 새로운 패턴 — 가짜 채용 / Insider 공격

### Fake Recruitment / Job Scam
- **Lazarus가 LinkedIn/구직 사이트에서 가짜 헤드헌터 행세**
- 가상자산/AI 회사 직원 표적
- 가짜 코딩 테스트 / 가짜 PDF에 멀웨어
- 직원 노트북 침투 → 회사 인프라 접근

### Insider Threat
- 북한 IT 노동자가 **가명으로 가상자산 회사 원격 채용** 시도 (2024~)
- 보수를 가상자산으로 받아 북한 송금
- 미국 DOJ 다수 적발

### Bitrefill / Mirror Attack
- 2026-03 Bitrefill 사이버 공격 — Lazarus 모방 그룹

## 6. 방어 — 회사 차원

### 기술
- **다중서명 + MPC + Hardware Wallet**
- **서명 UI 검증** (Bybit 사례 교훈)
- **공급망 보안** (제3자 SDK/wallet 검증)
- **Cold storage 비율** (가상자산이용자보호법)

### KYT
- Lazarus 관련 wallet은 Chainalysis/TRM/Elliptic 라벨 즉시 반영
- 입출금 시 **Lazarus exposure 자동 차단**
- 의심 거래 → 즉시 STR

### KYC + HR 보안
- 채용 시 **북한 IT 노동자 식별** (시간대, 신분증 위조)
- 임직원 LinkedIn 가짜 헤드헌터 경고
- 보안 교육 (피싱, 가짜 PDF)

### 협력
- **FBI / KISA / FIU** 정보 공유
- 산업 정보 공유 (ISAC)
- 사고 발생 시 24시간 내 글로벌 거래소 freeze 협조 요청

## 7. 정책적 의미

- **DPRK는 가상자산 자금세탁의 #1 국가행위자**
- 미국 의회 + UN 패널 보고서 매년 갱신
- 한국 입장에서 특히 중요 — 적성국가 제재 + 우리 거래소 표적
- FATF Black List 유지

## 8. 학습 포인트

```
- 가상자산 보안은 단순 해킹 방어가 아니라 "공급망 + Insider + AML"의 결합
- 자금세탁이 24~48시간 내 완료되므로 사고 후 대응은 늦음 → 사전 차단이 본질
- Lazarus 라벨은 KYT 벤더의 attribution 품질의 시금석
- 한국·일본 거래소가 역사적으로 표적 다수 — 한국어 사용자 인식 필수
- 2025-02 Bybit가 보안 인식의 분기점
```

## 더 읽을거리
- [`tornado_cash.md`](tornado_cash.md) — Lazarus가 자주 쓴 mixer
- [`major_enforcement.md`](major_enforcement.md) — 관련 enforcement 사례
- [`../notes/3-crypto-aml/onchain-typology.md`](../notes/3-crypto-aml/onchain-typology.md) — 자금세탁 패턴
- [`../notes/5-compliance/sanctions-screening.md`](../notes/5-compliance/sanctions-screening.md) — OFAC SDN
- [The Hacker News — DPRK $2B in 2025](https://thehackernews.com/2025/12/north-korea-linked-hackers-steal-202.html)
- [TRM Labs — Bybit Hack 분석](https://www.trmlabs.com/resources/blog/the-bybit-hack-following-north-koreas-largest-exploit)
- [BlockEden — Lazarus Playbook $6.75B](https://blockeden.xyz/blog/2026/02/03/lazarus-group-playbook-north-korea-crypto-theft-6-75-billion/)
- [38 North — Digital Kleptocracy → Crypto Superpower](https://www.38north.org/2026/01/from-digital-kleptocracy-to-rogue-crypto-superpower/)
- [Chainalysis 2026 Crypto Crime Report](https://www.chainalysis.com/reports/crypto-crime-2026/)
