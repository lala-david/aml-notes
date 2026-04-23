# 벤더 성능 비교 — KYT·Travel Rule·KYC 정량 평가

> AML 벤더 선정의 핵심은 "기능 비교"가 아니라 **운영 데이터 비교** — FP율·응답 시간·비용·한국 지원·통합 난이도. 본 페이지는 공개 정보·산업 보고서·실무자 인터뷰 기반 추정치를 모은 **PoC 보조 자료**. 마지막 업데이트: 2026-04-23.

## ⚠️ 데이터 출처 안내

벤더 성능 데이터는 대부분 **NDA 보호** 상태. 본 페이지는 다음에서 추정:
- 공개 산업 보고서 (Chainalysis Crypto Crime Report, Elliptic 연간 보고)
- VASP 공개 사례·블로그 (Coinbase·Kraken·Upbit 인터뷰)
- 컨퍼런스 발표 (ACAMS·Chainalysis Links·Consensus)
- 한국 DAXA 공동 PoC 후기 (비공식 청취)

수치는 **참고용**이며, 실제 PoC 또는 RFP 통한 검증 필수. 정확도 95%+ 보장 못 함.

## TL;DR

- **KYT 빅5**: Chainalysis · Elliptic · TRM · Crystal · Merkle Science
- **Travel Rule**: Notabene Gateway 글로벌 1위 / 한국은 VerifyVASP·CODE 양강
- **KYC**: Sumsub·Jumio 글로벌 1·2위 / 한국은 ARGOS·KYC365·코인플러그
- **선택 기준 5요소**: FP율·Latency·비용·한국 지원·통합 난이도
- 한국 4대 거래소 표준 조합: **Chainalysis KYT + VerifyVASP/CODE + ARGOS**

## 1. KYT 벤더 성능 비교

### 1.1 핵심 지표 비교 표 (추정)

| 지표 | Chainalysis | Elliptic | TRM Labs | Crystal | Merkle Science |
|---|---|---|---|---|---|
| **누적 라벨 주소** | ~1B+ | ~500M | ~700M | ~300M | ~200M |
| **지원 체인** | 100+ | 50+ | 70+ | 40+ | 30+ |
| **API 응답 p50** | ~150~250ms | ~200~300ms | ~180~280ms | ~250~400ms | ~200~350ms |
| **API 응답 p99** | ~800ms~1.5s | ~1~2s | ~900ms~2s | ~1.5~3s | ~1~2.5s |
| **FP rate (raw)** | ~70~85% | ~75~90% | ~70~85% | ~80~92% | ~75~88% |
| **FP rate (tuned)** | ~30~50% | ~35~55% | ~30~50% | ~45~65% | ~35~55% |
| **연간 비용** (중형 VASP) | $200K~$500K | $150K~$400K | $150K~$400K | $100K~$300K | $80K~$250K |
| **한국 지원** | ✓ Korean office (서울) | ✓ APAC team | ✓ Singapore | △ EU 중심 | △ Singapore |
| **한국 4대 거래소** | Upbit·Bithumb·Coinone·Korbit | Bithumb·Coinone | Upbit·Coinone (보조) | 일부 | 일부 |
| **Cross-chain** | ✓ Strong | ✓ Strong | ✓ **Best** | ✓ Strong | △ |
| **Behavior ML** | ✓ Lynx GNN | ✓ Behavioral Analytics | ✓ Standard | △ | △ |

### 1.2 벤더별 강점·약점

#### Chainalysis (시장 1위 ~50% 점유)
- **강점**: 라벨 DB 최대, 한국 서울 오피스, 모든 한국 4대 채택
- **약점**: 비용 최고, Cross-chain은 TRM 대비 약함
- **포지셔닝**: "안 쓰면 검사관에게 설명 어려움"

#### Elliptic (~20% 점유)
- **강점**: EU·UK 강세, Behavioral Analytics 정확도 높음
- **약점**: 한국 라벨 상대적 적음, APAC 지원 시간차
- **포지셔닝**: 글로벌 + EU 진출 시 1순위

#### TRM Labs (신흥, ~15% 점유)
- **강점**: Cross-chain 추적 1위, 가격 경쟁력
- **약점**: 한국 라벨 부족, 서울 오피스 없음
- **포지셔닝**: 신흥 VASP·DeFi 분석

#### Crystal (~10%)
- **강점**: 러시아·LATAM 강세, 가격
- **약점**: 한국 시장 거의 없음
- **포지셔닝**: 신흥시장 진출

#### Merkle Science (~5%)
- **강점**: 가격, Compliance focus, Singapore 본사
- **약점**: 라벨 DB 작음
- **포지셔닝**: 소규모 VASP·예산 제약

### 1.3 한국 4대 거래소 채택 현황 (추정)

| 거래소 | KYT 1차 | KYT 2차 (보조) |
|---|---|---|
| Upbit | Chainalysis | TRM (cross-chain 보조) |
| Bithumb | Chainalysis | Elliptic (글로벌 보조) |
| Coinone | Chainalysis | TRM (보조) |
| Korbit | Chainalysis | (단일) |

**관찰**: 한국 4대 모두 Chainalysis = 사실상 표준. 2차 벤더는 cross-chain·EU 등 특정 영역 보강용.

### 1.4 FP rate 튜닝 실증

기본 설정 시 FP 70~90%. 다음 튜닝으로 30~50% 감축:

1. **Customer KYC tier 통합** — Tier 3 (full KYC) override × 0.7
2. **Behavior pattern 결합** — 정상 패턴 × 0.85
3. **Whitelist 운영** — 한 번 disposition 받은 pair 5년 유지
4. **Threshold 상향** — Severity ≥ "Medium" only
5. **Korean fuzzy tuning** — 성씨 필터 + 다축 매칭

**튜닝 효과 예시 (가상 한국 VASP)**:
- 기본 (Chainalysis default): 일 alert 200+, FP 85%, STR 0.5%
- 튜닝 후: 일 alert 30~40, FP 35%, STR 5%
- **Analyst 시간 ~80% 절약**

## 2. Travel Rule 벤더 비교

### 2.1 핵심 지표 비교 표

| 지표 | Notabene | VerifyVASP | CODE | TRISA | TRP |
|---|---|---|---|---|---|
| **연결 VASP 수** | 1,500+ | ~50 (한국·아시아 중심) | ~30 (한국 중심) | ~200 | ~100 |
| **한국 4대 거래소** | 보조 게이트웨이 | Upbit·Bithumb·Coinone·Korbit (메인) | Bithumb·Coinone (메인) | △ | △ |
| **메시지 전달 p50** | ~3~7초 | ~2~3초 (한국 내) | ~2~4초 (한국 내) | ~5~10초 | ~3~6초 |
| **Sunrise rate** | ~5~10% | ~15~25% | ~20~30% | ~40~60% | ~30~50% |
| **연간 비용** | $50K~$300K | $30K~$200K | $30K~$200K | 무료 (오픈소스) | $20K~$150K |
| **IVMS101 지원** | ✓ Full | ✓ Full | ✓ Full | ✓ Full | ✓ Full |

### 2.2 벤더별 포지셔닝

- **Notabene**: 글로벌 게이트웨이 1위, 멀티프로토콜 라우팅
- **VerifyVASP**: 한국·아시아 컨소시엄 (Sygna 후신), Lambda256(두나무 자회사) 운영
- **CODE**: 한국 4대 거래소 컨소시엄, 한국 100만원 임계 자동
- **TRISA**: 분산형 오픈소스 (CipherTrace 시작 → Mastercard), 무료
- **TRP**: 21 Analytics, 영국 중심

### 2.3 한국 VASP 표준 조합

- **Upbit**: VerifyVASP 메인 + Notabene 글로벌 보조
- **Bithumb·Coinone·Korbit**: CODE 메인 + Notabene 보조
- **신규 한국 VASP**: Notabene 우선 가입 → 추후 VerifyVASP/CODE 검토

## 3. KYC 벤더 비교

### 3.1 글로벌 vs 한국 시장 분리

| 지표 | Sumsub | Jumio | Onfido | Persona | ARGOS (KR) | KYC365 (KR) |
|---|---|---|---|---|---|---|
| **KYC 처리 속도** | 30s~3min | 1~5min | 30s~3min | 1~3min | 5~30s (한국 빠름) | 5~30s |
| **얼굴 인식 정확도** | ~99.5% | ~99.7% | ~99.5% | ~99.6% | ~99.0% | ~99.0% |
| **본인확인기관 연동** | ✗ | ✗ | ✗ | ✗ | ✓ PASS·NICE·KCB | ✓ |
| **연간 비용** (중형) | $50K~$200K | $80K~$300K | $40K~$150K | $30K~$120K | ₩50M~₩200M | ₩50M~₩200M |
| **한국 PIPA 호환** | △ (별도 합의) | △ | △ | △ | ✓ | ✓ |

### 3.2 한국 시장 특수성

- **본인확인기관(PASS·NICE·KCB)** 의무 연동 → 글로벌 KYC만으로 부족
- 한국 4대 = 한국 KYC + 글로벌 KYC 2단 조합 일반적
  - 1차: 본인확인기관 (실명·주소·주민번호 검증)
  - 2차: 추가 신원 (여권·국적·PEP·SDN 스크리닝)

## 4. PoC 체크리스트 (벤더 선정 시)

### 4.1 PoC 대상 벤더 선정

- 메인 후보 2~3 (Chainalysis·Elliptic·TRM 중)
- 보조 후보 1~2 (Crystal·Merkle Science 중)

### 4.2 PoC 평가 항목 (12주, 4단계)

#### Phase 1 (1~2주): 기능 검증
- [ ] 지원 체인 우리 거래 자산 cover
- [ ] API 인증·연결 성공
- [ ] 샘플 100 주소 query 응답
- [ ] Webhook·alert 정상 수신

#### Phase 2 (3~6주): 실데이터 PoC
- [ ] 우리 거래 1주일 데이터 적용
- [ ] False Positive 비율 측정 (벤더별)
- [ ] False Negative 비율 (알려진 위험 주소 누락 여부)
- [ ] Latency p50·p99 측정 (1000+ query)
- [ ] 한국 IP·신용카드 거래 정상 처리

#### Phase 3 (7~10주): 한국 특수성 검증
- [ ] 한국 4대 거래소 입출금 라벨 정확도
- [ ] DAXA 공동 블랙리스트 호환
- [ ] 한국어 UI·고객 지원
- [ ] PIPA 호환 (개인정보 처리)

#### Phase 4 (11~12주): 통합 난이도·비용
- [ ] 우리 KYC·KYT·Risk Engine 통합 시간 (개발 공수)
- [ ] 운영 부담 (Alert 처리 SOP)
- [ ] 5년 TCO (계약·트래픽·인력)
- [ ] Exit 전환 비용 (벤더 변경 시 마이그레이션)

### 4.3 의사결정 매트릭스 (가중치 예시)

| 항목 | 가중치 | Chainalysis | Elliptic | TRM |
|---|---|---|---|---|
| FP rate | 25% | 8/10 | 7/10 | 8/10 |
| Latency | 15% | 9/10 | 8/10 | 8/10 |
| 한국 지원 | 20% | 10/10 | 7/10 | 5/10 |
| 비용 | 15% | 6/10 | 7/10 | 8/10 |
| Cross-chain | 15% | 7/10 | 7/10 | 10/10 |
| 통합 난이도 | 10% | 8/10 | 7/10 | 8/10 |
| **가중 총점** | 100% | **8.05** | 7.20 | 7.50 |

## 5. 벤더 협상·계약 팁 (실무자 청취)

### 5.1 가격 협상 포인트

- **트랜잭션 단가** vs **연간 정액** — 거래량 변동성 평가 후 선택
- **트래픽 상한 설정** — 폭증 시 추가 요금 방지
- **Multi-product 할인** — KYT + Reactor + Crypto Investigations 묶음
- **다년 계약** — 3~5년 시 ~20~30% 할인 가능

### 5.2 SLA 합의 점검

- API 가용성 99.9% (≈월 43분 다운 허용) 표준
- p99 Latency 보장 (벤더가 거부 시 P99 < 2s 상한 명시)
- Alert 통지 SLA (Severe → 30분 이내)
- 라벨 DB 일일 업데이트 보장

### 5.3 Exit Clause

- 데이터 export 권한 (자체 알람 history)
- Migration 지원 기간 (3~6개월)
- 위약금 상한 (계약 잔여 기간 50% 등)

## 6. 한국 신규 VASP 벤더 도입 순서

신규 VASP가 라이선스 신고 준비 시 추천 도입 순서:

1. **본인확인기관 (PASS or NICE)** — 즉시 (실명확인 의무)
2. **국내 KYC (ARGOS)** — 1개월 내 (KYC 표준화)
3. **Travel Rule (Notabene 또는 CODE)** — 영업 개시 전 의무
4. **KYT (Chainalysis)** — 영업 개시 동시 (가장 비싸지만 표준)
5. **(선택) 보조 KYT (TRM·Elliptic)** — 6개월~1년 후 cross-chain·글로벌 보강
6. **(선택) Sumsub·Jumio** — 글로벌 진출 시

**초기 1년 예상 비용**: 본인확인 ₩30M + KYC ₩100M + Travel Rule ₩50M + KYT ₩300M = **약 ₩500M (~$370K)**

## 7. 참고 자료

- [Chainalysis 2025 Crypto Crime Report](https://www.chainalysis.com/reports/)
- [Elliptic Annual Crypto Crime Report](https://www.elliptic.co/resources)
- [TRM Insights Reports](https://www.trmlabs.com/insights)
- [Notabene VASP Discovery](https://notabene.id/)
- [VerifyVASP 공식](https://www.verifyvasp.com/)
- [DAXA 공동 가이드 (비공개)]
- ACAMS Today 벤더 비교 (회원 한정)

## 더 읽을거리

- [`analytics-vendors.md`](analytics-vendors.md) — KYT 벤더 시장 지도
- [`travel-rule-vendors.md`](travel-rule-vendors.md) — Travel Rule 벤더 시장 지도
- [`korea-solutions.md`](korea-solutions.md) — 한국 시장 인프라
- [`../4-technology/blockchain-analytics.md`](../4-technology/blockchain-analytics.md) — KYT 기술 원리
