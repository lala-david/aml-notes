# KYC / KYT — 가상자산 AML 기술의 두 축

> KYC(사람을 안다) + KYT(거래/지갑을 안다). 가상자산만의 조합. 마지막 업데이트: 2026-04-17.

## TL;DR
- **KYC**: 사람/법인의 신원확인 (공통)
- **KYT**: 거래/지갑주소의 위험 분석 (가상자산 특화)
- 두 개가 결합되어 **고객 단위 risk score** 가 형성됨
- KYC 기술 스택: **OCR + Liveness + Face matching + PEP/제재DB + AML watchlist**
- KYT 기술 스택: **Address attribution + Cluster analysis + Exposure scoring + Behavior detection**

---

## 1. KYC 프로세스 단계

```
1. Onboarding (가입)
   ├─ 개인정보 수집 (이름/생년월일/주소/연락처)
   ├─ 신분증 OCR + 진위확인
   ├─ Liveness check (얼굴 영상 + 신분증 사진 매칭)
   └─ 휴대폰/이메일 인증

2. Verification (검증)
   ├─ 본인인증 (PASS, 카카오 등 한국)
   ├─ 주소 증빙 (공과금/은행거래내역)
   └─ 직업/소득 (선택, EDD 시 필수)

3. Screening (스크리닝)
   ├─ PEP 데이터베이스 매칭
   ├─ Sanctions list (OFAC/UN/EU/외교부)
   ├─ Adverse media (부정적 보도)
   └─ 가상자산 지갑주소 OFAC SDN

4. Risk Assessment (위험평가)
   ├─ 국가 위험 (FATF Grey/Black, 한국 외교부 분류)
   ├─ 직업 위험 (현금집약 업종, 정부, 외교)
   ├─ 거래 의도 (예상 금액/빈도/상대국)
   └─ 종합 risk score → 등급 (LOW/MED/HIGH)

5. Ongoing Monitoring (지속 모니터링)
   ├─ 거래 패턴 vs 신고 의도 비교
   ├─ 위험요소 변경 시 재실사
   └─ EDD 트리거 발동 시 추가 절차
```

## 2. KYC 기술 컴포넌트

| 컴포넌트 | 기술 | 벤더 예시 |
|---|---|---|
| **OCR** | 신분증 텍스트 추출 | Sumsub, Onfido, ARGOS, IDology |
| **Document Authentication** | 위변조 검증 (홀로그램/MRZ/배경) | Sumsub, Jumio |
| **Liveness Check** | 실제 사람 vs 사진/영상 (3D depth) | Sumsub, FaceTec, iProov |
| **Face Matching** | 신분증 사진 vs 실시간 셀카 | 위와 동일 |
| **PEP / Sanctions DB** | 글로벌 watchlist 매칭 | LSEG World-Check, Dow Jones, ComplyAdvantage |
| **Adverse Media** | 뉴스/제재/소송 검색 | ComplyAdvantage, RDC |
| **Korean ID Verification** | 본인확인기관 (PASS, 카카오인증) | 한국 본인확인기관 |
| **Risk Scoring** | RBA 점수 계산 | 자체 또는 ComplyAdvantage, Featurespace |

## 3. KYT 프로세스

```
1. Address Discovery (주소 등록)
   ├─ 입금 주소 = 자체 발급 → 자동 매핑
   ├─ 출금 주소 = 사용자 입력 → 외부지갑 등록
   └─ Travel Rule 카운터파티 주소

2. Address Attribution (행위자 매핑)
   ├─ Chainalysis/TRM/Elliptic 라벨 DB 조회
   ├─ 자체 클러스터링 결과
   └─ 카운터파티 VASP 식별

3. Exposure Analysis (노출 분석)
   ├─ Direct exposure (1-hop): 바로 mixer/SDN인가
   ├─ Indirect exposure (N-hop): N단계 안에 위험 주소
   ├─ Source vs Destination 분리
   └─ exposure score 계산

4. Behavior Detection (행위 탐지)
   ├─ Peel chain 진입 패턴
   ├─ 분할 입출금 (smurfing)
   ├─ 즉시 pass-through
   └─ 비정상 시간/금액

5. Decision (의사결정)
   ├─ Score ≥ threshold → 거래 보류
   ├─ Manual review queue
   └─ STR 후보 큐
```

## 4. KYT 핵심 개념

### Cluster (클러스터)
- 같은 사람/엔티티가 통제하는 주소 집합
- 휴리스틱 + 머신러닝 + 라벨링으로 구성
- 한 거래소가 수백만 개 deposit 주소 → 한 클러스터로 묶임

### Attribution (귀속)
- 클러스터 → 알려진 엔티티 (Binance, Tornado Cash, OFAC SDN, ...)
- attribution DB가 KYT 벤더의 핵심 IP
- Chainalysis: 24조 달러+ 가치, 10억+ 주소 매핑

### Exposure (노출도)
- 한 주소가 위험 주소와 어떤 관계에 있는가
- **Direct**: 바로 거래
- **Indirect (N-hop)**: N단계 안에서 도달
- **Risk Category 별 점수**: mixer 노출, SDN 노출, ransomware 노출 등

### Risk Score
- KYC 정보 + KYT 노출도 + 거래 패턴 종합
- 보통 0~100 점수
- threshold 넘으면 자동 액션 (보류/거절/STR 큐)

## 5. KYC vs KYT — 한눈에

| 구분 | KYC | KYT |
|---|---|---|
| 대상 | 사람 | 거래/지갑 |
| 시점 | Onboarding 위주 + 주기적 | **상시 (real-time)** |
| 데이터 소스 | 신분증/PEP DB/신용평가 | **공개 블록체인** + 라벨 DB |
| 가상자산 특화? | 일부 (지갑 등록 등) | **완전 특화** |
| 정적 vs 동적 | 정적 (변경 적음) | **동적 (매 거래마다)** |
| 핵심 도전 | 위변조, deepfake, 합성신분 | 익명성, 클러스터링, cross-chain |

→ 두 시스템이 **연결되어 한 risk score를 만드는 게 이상적 아키텍처**.

## 6. 통합 Risk Engine 아키텍처 (개념도)

```
┌─────────────────────────────────────────────────────────────┐
│                      Customer Profile                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ KYC Data     │  │ Wallet Map   │  │ Behavior     │       │
│  │ (KYC vendor) │  │ (KYT vendor) │  │ (자체 분석)   │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
│         └─────────────────┼──────────────────┘               │
│                           ▼                                   │
│                  ┌─────────────────┐                          │
│                  │  Risk Engine    │                          │
│                  │  (룰 + ML)       │                          │
│                  └────────┬────────┘                          │
│                           ▼                                   │
│   ┌──────────────────────┴─────────────────────────┐         │
│   │  Actions: 차단 / EDD trigger / STR 큐 / 통과    │         │
│   └────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

## 7. 한국 거래소/수탁업자 기술 스택 예시

| 영역 | 한국 시장 선택지 |
|---|---|
| **KYC SDK** | ARGOS Identity, ICONLOOP MyID, Sumsub (글로벌) |
| **본인확인** | PASS, 카카오인증, NICE, KCB |
| **PEP/제재 DB** | LSEG World-Check, Dow Jones, ComplyAdvantage, 자체 DB |
| **KYT** | Chainalysis KYT, TRM Labs, Elliptic Lens, Crystal, 자체 |
| **Travel Rule** | VerifyVASP, CODE, Notabene |
| **Risk Engine** | 자체 (대형사) 또는 ComplyAdvantage, Quantexa |
| **Case Management** | NICE Actimize, Hummingbird, Unit21 |

## 8. 실무 운영 포인트

### 알람 폭주(Alert Fatigue)
- 룰 너무 느슨하면 알람 폭주 → 1선이 처리 못함 → STR 누락
- 룰 너무 빡빡하면 거짓양성 다수 → 고객 불만
- → **튜닝**이 운영의 90%

### False Positive vs False Negative
- FP (오탐) : 정상고객 차단 → 고객 손실
- FN (미탐) : 실제 자금세탁 통과 → 규제 위반
- 가상자산 영역은 **FN 비용이 더 큼** (벌금 + 평판)

### 사람 + 기계
- 100% 자동화 불가능 — 모호한 알람은 결국 분석가가 판단
- AMLO + analyst 팀의 역량이 핵심
- 좋은 case management 도구 = 분석가 효율 ×3

## 더 읽을거리
- [`blockchain_analytics.md`](blockchain_analytics.md) — KYT의 기술적 기반
- [`travel_rule_protocols.md`](travel_rule_protocols.md) — Travel Rule 기술
- [`../04_compliance_ops/cdd_edd.md`](../04_compliance_ops/cdd_edd.md) — CDD/EDD 운영
- [`../05_solutions_market/analytics_vendors.md`](../05_solutions_market/analytics_vendors.md) — 벤더 비교
- [Merkle Science — Enhancing AML with Blockchain Analytics](https://www.merklescience.com/enhancing-anti-money-laundering-efforts-with-advanced-blockchain-analytics)
- [CoinCover — KYT and AML overlap](https://www.coincover.com/blog/how-aml-and-kyt-overlap-with-wallet-protection-coincover)
