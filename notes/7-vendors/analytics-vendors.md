# Blockchain Analytics 벤더 — 시장 지도

> Chainalysis / Elliptic / TRM Labs / Crystal / Merkle Science 비교. 마지막 업데이트: 2026-04-17.

## TL;DR
- 글로벌 4대: **Chainalysis (시장 표준)** / **Elliptic (컴플라이언스 강세)** / **TRM Labs (cross-chain/실시간 강세)** / **Crystal Intelligence (러시아·동유럽 강세)**
- 신흥: **Merkle Science (예측/행동 분석), Nominis (VASP 특화), AnChain.AI**
- 한국 진입: 4사 모두 한국 거래소·수탁업자에 활발히 영업
- 자체 구축은 거의 불가능 → **벤더 라이센스 + 자체 한국 특화 분석 보완**이 현실
- 가격은 비공개, 보통 **수십~수백 K USD/년** (규모/체인수에 따라)

---

## 1. 4대 벤더 비교

### A. Chainalysis
- **본사**: 뉴욕, 2014 설립
- **포지션**: **시장 표준** — 미 연방정부(FBI, IRS, FBI) 표준 도구
- **주력**:
  - Reactor (조사)
  - KYT (실시간 모니터링)
  - Sanctions API
  - Crypto Investigations
- **데이터**: $24조+ 가치, 10억+ 주소 매핑 (2023 기준)
- **임팩트**: $34B+ 가치 동결/회수 기여
- **한국**: VerifyVASP 합작, 4대 거래소 다수 사용
- **강점**: 라벨 DB 깊이, 정부/LE 신뢰, 매년 Crypto Crime Report
- **약점**: 가격 비싸다는 평, UI 복잡

### B. Elliptic
- **본사**: 런던, 2013 설립
- **포지션**: **컴플라이언스 + 위험 스코어링 강세**
- **주력**:
  - Lens (지갑 스크리닝)
  - Navigator (조사)
  - Discovery (위험 탐지)
  - "Holistic" 기술
- **데이터**: 20억+ 라벨 주소, 100+ 자산 지원
- **처리량**: 200만+ 스크리닝/월
- **강점**: sub-second 스크리닝, 영국/EU 강세
- **약점**: cross-chain 후발

### C. TRM Labs
- **본사**: 샌프란시스코, 2018 설립
- **포지션**: **실시간 + cross-chain 강세, 차세대**
- **주력**:
  - Forensics (조사)
  - Transaction Monitoring
  - Travel Rule
  - Multichain Tracing
- **데이터**: **30+ 네트워크** 지원 (4사 중 가장 많음)
- **강점**: cross-chain 추적, 빠른 신규 체인 통합, 모던 UX
- **약점**: 라벨 DB가 Chainalysis보다 얕음 (단 빠르게 따라잡는 중)

### D. Crystal Intelligence (Crystal Blockchain)
- **본사**: 암스테르담, 2018 설립 (Bitfury 출신)
- **포지션**: **러시아·동유럽 attribution 강세**
- **주력**:
  - Crystal Expert (조사)
  - Crystal Compliance (스크리닝)
- **강점**: 러시아어권 거래소·다크넷 attribution, BTC 깊이
- **약점**: 글로벌 대형사 도입률 낮음

## 2. 신흥/특화 벤더

### Merkle Science
- 싱가포르, **예측 행동 분석**
- 머신러닝 기반 위험 탐지
- 한국·동남아 활발

### Nominis
- VASP 특화 SaaS, **간편한 통합**
- Chainalysis/TRM 대안 포지션

### AnChain.AI
- AI/ML 강조, smart contract 분석

### Coinfirm (지금은 Lukka에 인수)
- 폴란드 출신
- AML/KYT

### Solidus Labs
- 시장 모니터링 + AML 결합
- 거래소 시세조종 탐지

### Inca Digital
- 시장 분석 + 위험 탐지

## 3. 도메인별 추천 (관점별)

### 거래소 KYT
- 1순위: **Chainalysis KYT, TRM Labs**
- 2순위: Elliptic Lens
- 한국 특화: + 자체 한국 거래소 attribution

### 수탁업자 KYT
- **출금 주소 스크리닝**이 핵심
- Chainalysis Address Screening, TRM Address Screening, Elliptic Lens
- 빠른 응답 속도 (real-time API)

### 조사/포렌식 (LE 협조용)
- **Chainalysis Reactor** (시각화 강력)
- TRM Forensics
- Crystal Expert (러시아 자금)

### Cross-chain 추적
- TRM Multichain
- Chainalysis Crosschain (2023+)
- Elliptic는 후발

### 시장 모니터링 (시세조종)
- Solidus Labs
- Nasdaq Trade Surveillance (전통 → 가상자산 확장)

### Travel Rule + KYT 통합
- Notabene (Travel Rule) + Chainalysis (KYT) 조합 흔함

## 4. 평가 기준

벤더 선정 시 고려:

| 기준 | 설명 |
|---|---|
| **체인 커버리지** | 몇 개 네트워크 지원? L2 포함? |
| **라벨 DB 깊이** | 거래소/믹서/SDN 라벨 정확도 |
| **API 성능** | 응답 속도, 가용성 SLA |
| **가격 모델** | 정액 vs 사용량 vs 라이센스 |
| **UI/UX** | 분석가 효율 |
| **법집행 신뢰도** | 검사/소송 시 증거 인정 |
| **현지 attribution** | 한국 거래소 매핑 정확도 |
| **통합 용이성** | SDK, Webhook, 문서 품질 |
| **Compliance 보고** | 내장 보고서 양식 |
| **고객 지원** | 한국 시간대 대응 |

## 5. 가격 (참고치, 비공개)

- 소규모 VASP: **$30K~$80K/년**
- 중규모: **$100K~$300K/년**
- 대규모 거래소: **$500K~$수M/년**
- Address screening API: **건당 ~$0.05~$0.50** (볼륨 따라)
- Reactor 등 조사 도구: **사용자당 $20K~$50K/년**

→ 협상 가능. 멀티 모듈 번들 할인.

## 6. POC (Proof of Concept) 체크리스트

벤더 선정 전 시범 사용:

```
□ 우리 거래소 입금 주소 attribution 정확도 테스트
□ 알려진 한국 mixer/스캠 wallet 탐지 여부
□ Lazarus 관련 주소 + 그 cluster 인식 여부
□ Cross-chain (BTC ↔ ETH ↔ Tron) 추적 정확도
□ API 응답 속도 (p99) 측정
□ False positive 비율 측정
□ Sanctions feed 갱신 주기
□ 한국 시간대 지원 인력
□ 데이터 export 형식 (STR 작성용)
□ 법집행 자료 인정 사례
```

## 7. 자체 구축 vs 벤더

### 자체 구축의 한계
- 라벨 DB가 핵심 자산 — 글로벌 attribution은 자체로 불가능
- 글로벌 거래소·믹서·다크넷 모니터링 인력 비용
- 검사·법집행 신뢰도 (벤더 도구가 더 인정받음)

### 자체 구축의 장점
- 한국 특화 attribution (현지 거래소, 사기 wallet)
- 사내 KYC + KYT 결합 분석
- 비용 절감 (대형사 한정)

### 현실적 답
- **하이브리드** — 글로벌 벤더 + 자체 한국 특화
- 한국 거래소들도 대부분 이 형태

## 8. 미래 트렌드

- **AI/ML 기반 행동 분석** 강화
- **실시간 cross-chain** 표준화
- **공유 attribution** (산업 컨소시엄 가능성)
- **ZKP 시대 대응** — 프라이버시 + 컴플라이언스 양립

## 더 읽을거리
- [`travel_rule_vendors.md`](travel_rule_vendors.md) — Travel Rule 솔루션 비교
- [`korea_solutions.md`](korea_solutions.md) — 한국 시장 솔루션
- [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) — 기술적 기반
- [Chainalysis 공식](https://www.chainalysis.com/)
- [Elliptic 공식](https://www.elliptic.co/)
- [TRM Labs 공식](https://www.trmlabs.com/)
- [Crystal Intelligence 공식](https://crystalintelligence.com/)
- [Merkle Science 공식](https://www.merklescience.com/)
- [Crypto Trace Labs — 4사 비교](https://cryptotracelabs.com/blog/chainalysis-vs-elliptic-vs-trm-labs-vs-crystal-intelligence-platform-comparison-for-investigators/)
