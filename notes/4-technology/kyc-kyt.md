# KYC / KYT — 가상자산 AML 기술의 두 축

> KYC(사람을 안다) + KYT(거래·지갑을 안다). 가상자산만의 조합. 이 글을 읽고 나면 두 시스템이 왜 **한 Risk Engine 안에 통합**돼야 하는지, 그리고 벤더 선정에서 무엇을 봐야 하는지 판단할 수 있게 됩니다. 마지막 업데이트: 2026-04-17.

## TL;DR
- **KYC**: 사람·법인의 신원확인 (공통)
- **KYT**: 거래·지갑주소의 위험 분석 (가상자산 특화)
- 두 개가 결합되어 **고객 단위 risk score**가 형성됨
- KYC 기술 스택: **OCR + Liveness + Face matching + PEP/제재 DB + AML watchlist**
- KYT 기술 스택: **Address attribution + Cluster analysis + Exposure scoring + Behavior detection**

---

## 1. KYC 프로세스 — 5단계 파이프라인

### 왜 파이프라인 구조인가

KYC는 "신분증 한 번 찍고 끝"이 아니라 **onboarding → verification → screening → assessment → ongoing monitoring**로 이어지는 연속 공정입니다. 각 단계가 막히면 이후 단계 전체가 실패하므로, 실무에서는 단계마다 **실패 지점과 fallback**을 명확히 설계해야 합니다.

### 파이프라인 구조

```
1. Onboarding (가입)
   ├─ 개인정보 수집 (이름·생년월일·주소·연락처)
   ├─ 신분증 OCR + 진위확인
   ├─ Liveness check (얼굴 영상 + 신분증 사진 매칭)
   └─ 휴대폰·이메일 인증

2. Verification (검증)
   ├─ 본인인증 (한국: PASS, 카카오 인증)
   ├─ 주소 증빙 (공과금·은행거래내역)
   └─ 직업·소득 (선택, EDD 시 필수)

3. Screening (스크리닝)
   ├─ PEP 데이터베이스 매칭
   ├─ Sanctions list (OFAC·UN·EU·외교부)
   ├─ Adverse media (부정적 보도)
   └─ 가상자산 지갑주소 OFAC SDN

4. Risk Assessment (위험평가)
   ├─ 국가 위험 (FATF Grey/Black, 외교부 분류)
   ├─ 직업 위험 (현금집약 업종, 정부·외교)
   ├─ 거래 의도 (예상 금액·빈도·상대국)
   └─ 종합 risk score → 등급 (LOW/MED/HIGH)

5. Ongoing Monitoring (지속 모니터링)
   ├─ 거래 패턴 vs 신고 의도 비교
   ├─ 위험요소 변경 시 재실사
   └─ EDD 트리거 발동 시 추가 절차
```

용어:
- **OCR (Optical Character Recognition)** — 이미지에서 텍스트를 자동 추출.
- **Liveness Check** — 실제 살아있는 사람인지 검증. 사진·영상·3D mask 스푸핑 방어.
- **Adverse Media** — 부정적 뉴스·소송·제재. PEP·Sanctions를 넘어서는 **평판 리스크** 확인.

### 실무 포인트

5단계 중 가장 자주 실패하는 건 **5번 Ongoing Monitoring**입니다. 신규 고객에게는 엄격하지만 기존 고객은 "이미 승인된 사람"이라고 방치하는 게 전형적 실수. 고위험 고객은 분기 1회, 저위험도 연 1회는 재실사(refresh)를 자동 큐에 올리는 시스템이 필요합니다.

---

## 2. KYC 기술 컴포넌트

### 이 표를 어떻게 읽어야 하나

각 컴포넌트는 **대체 가능한 벤더**가 여러 개 있습니다. 선정 시 고려할 축은 (1) 한국 신분증 포맷 지원 정확도, (2) Liveness 스푸핑 방어 수준, (3) 국외 PEP DB 커버리지, (4) SDK 연동 용이성. 대형사일수록 **컴포넌트별로 다른 벤더**를 쓰는 모듈형 구조.

| 컴포넌트 | 기술 | 벤더 예시 |
|---|---|---|
| **OCR** | 신분증 텍스트 추출 | Sumsub, Onfido, ARGOS, IDology |
| **Document Authentication** | 위변조 검증 (홀로그램·MRZ·배경) | Sumsub, Jumio |
| **Liveness Check** | 실제 사람 vs 사진·영상 (3D depth) | Sumsub, FaceTec, iProov |
| **Face Matching** | 신분증 사진 vs 실시간 셀카 | 위와 동일 |
| **PEP / Sanctions DB** | 글로벌 watchlist 매칭 | LSEG World-Check, Dow Jones, ComplyAdvantage |
| **Adverse Media** | 뉴스·제재·소송 검색 | ComplyAdvantage, RDC |
| **Korean ID Verification** | 본인확인기관 (PASS, 카카오인증) | 한국 본인확인기관 |
| **Risk Scoring** | RBA 점수 계산 | 자체 또는 ComplyAdvantage, Featurespace |

### 실무 포인트

한국 특화의 핵심은 **PASS·카카오·NICE 본인확인기관 연동**. 글로벌 벤더(Sumsub 등)는 한국 주민등록증 OCR 정확도는 높아도 **본인확인기관 연동을 대신할 수 없습니다**. 실무 구성은 "글로벌 벤더 + 한국 본인확인기관" 하이브리드.

---

## 3. KYT 프로세스 — 5단계 분석 파이프라인

### KYT의 고유한 어려움

KYC는 onboarding 시점에 한 번 크게 수행하고 간헐적 재실사지만, **KYT는 매 거래마다 실시간으로 작동**해야 합니다. 고객이 1천만원 출금 요청을 누르면 수 초 안에 "이 거래 해도 되는가" 답이 나와야 UX가 유지됩니다. 이 실시간 제약이 KYT 아키텍처 설계의 최대 난제.

### 파이프라인 구조

```
1. Address Discovery (주소 등록)
   ├─ 입금 주소 = 자체 발급 → 자동 매핑
   ├─ 출금 주소 = 사용자 입력 → 외부지갑 등록
   └─ Travel Rule 카운터파티 주소

2. Address Attribution (행위자 매핑)
   ├─ Chainalysis·TRM·Elliptic 라벨 DB 조회
   ├─ 자체 클러스터링 결과
   └─ 카운터파티 VASP 식별

3. Exposure Analysis (노출 분석)
   ├─ Direct exposure (1-hop): 바로 mixer·SDN인가
   ├─ Indirect exposure (N-hop): N단계 안에 위험 주소
   ├─ Source vs Destination 분리
   └─ exposure score 계산

4. Behavior Detection (행위 탐지)
   ├─ Peel chain 진입 패턴
   ├─ 분할 입출금 (smurfing)
   ├─ 즉시 pass-through
   └─ 비정상 시간·금액

5. Decision (의사결정)
   ├─ Score ≥ threshold → 거래 보류
   ├─ Manual review queue
   └─ STR 후보 큐
```

### 실무 포인트

KYT 파이프라인에서 가장 느린 단계는 **2번 Attribution** (외부 API 호출). 실시간 성능을 위해 **자주 조회되는 주소는 캐싱**하고, 캐시 miss 시 비동기로 API 조회하는 설계가 표준. 동기 API만 의존하면 벤더 장애 시 거래 처리 전체가 멈춥니다.

---

## 4. KYT 핵심 개념

### Cluster (클러스터)

**정의**: 같은 사람·엔티티가 통제하는 주소 집합.

- 휴리스틱 + 머신러닝 + 라벨링으로 구성
- 한 거래소가 수백만 개 deposit 주소를 운영해도 분석 도구에는 **한 클러스터**로 묶임
- 클러스터 식별은 **UTXO 모델(Bitcoin)** 이 강력, **Account 모델(Ethereum)** 은 약함

### Attribution (귀속)

**정의**: 클러스터를 알려진 엔티티에 매핑. 예: 클러스터 `c12345` → "Binance", `c67890` → "Tornado Cash".

- Attribution DB가 **KYT 벤더의 핵심 IP**
- Chainalysis: 누적 추적 거래량 **$24T+**, 매핑 주소 **10억+** (DB 가치가 아닌 추적된 거래 볼륨)
- 신규 엔티티 라벨링은 수동 + 자동 혼합, 보통 수일~수주 lag time

### Exposure (노출도)

**정의**: 한 주소가 위험 주소와 어떤 관계에 있는가를 정량화.

- **Direct (1-hop)**: 바로 거래
- **Indirect (N-hop)**: N단계 안에서 도달
- **Risk Category 별 점수**: mixer, SDN, ransomware, scam 등 카테고리마다 가중치

### Risk Score

**정의**: KYC 정보 + KYT 노출도 + 거래 패턴을 종합한 0~100 점수.

- Threshold(예: 70점) 넘으면 자동 액션 (보류·거절·STR 후보 큐)
- 벤더마다 산정 공식이 다름 — **같은 주소에 대해 Chainalysis와 TRM이 다른 점수를 낼 수 있음**

### 실무 포인트

Risk Score를 내부 의사결정에 쓸 때 **벤더 점수 그대로**가 아니라 **회사 정책으로 재가공**하는 게 좋습니다. 예: Chainalysis 80점이지만 우리 고객 중에서 정말 위험한 패턴을 많이 본 프로필이라면 +10 가중, 일반 거래소 이체라면 -5 할인. 벤더 점수는 **원료**이고 **완성된 의사결정**은 회사 책임.

---

## 5. KYC vs KYT — 한눈에

### 이 표를 어떻게 읽어야 하나

두 시스템이 **대체재가 아니라 보완재**라는 게 핵심. 한쪽만 있으면 가상자산 AML이 작동하지 않습니다.

| 구분 | KYC | KYT |
|---|---|---|
| 대상 | 사람 | 거래·지갑 |
| 시점 | Onboarding 위주 + 주기적 | **상시 (real-time)** |
| 데이터 소스 | 신분증·PEP DB·신용평가 | **공개 블록체인** + 라벨 DB |
| 가상자산 특화? | 일부 (지갑 등록 등) | **완전 특화** |
| 정적 vs 동적 | 정적 (변경 적음) | **동적 (매 거래마다)** |
| 핵심 도전 | 위변조, deepfake, 합성신분 | 익명성, 클러스터링, cross-chain |

### 두 시스템이 통합돼야 하는 이유

KYT만 있고 KYC가 부실하면 "주소는 위험한데 그 뒤 사람은 누군지 모름" → STR 작성 불가. KYC만 있고 KYT가 부실하면 "사람은 알지만 그 사람의 지갑이 OFAC에 연결됐는지 몰라 차단 불가." 이 두 상황은 둘 다 규제 위반입니다.

### 실무 포인트

KYC 팀과 KYT 팀이 조직 상 분리돼 있는 회사가 많은데, 이러면 **Risk Score 통합**이 잘 안 됩니다. 이상적 구성은 두 팀이 공통 **Case Management 도구**를 쓰고, 분석가가 한 화면에서 고객의 KYC 정보와 KYT 노출을 함께 보는 것. 실제로 Unit21·Hummingbird 같은 도구가 이 통합 UX를 제공합니다.

---

## 6. 통합 Risk Engine 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                      Customer Profile                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ KYC Data     │  │ Wallet Map   │  │ Behavior     │       │
│  │ (KYC vendor) │  │ (KYT vendor) │  │ (자체 분석)  │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
│         └─────────────────┼──────────────────┘              │
│                           ▼                                  │
│                  ┌─────────────────┐                         │
│                  │  Risk Engine    │                         │
│                  │  (룰 + ML)      │                         │
│                  └────────┬────────┘                         │
│                           ▼                                  │
│   ┌──────────────────────┴─────────────────────────┐        │
│   │  Actions: 차단 / EDD trigger / STR 큐 / 통과   │        │
│   └────────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### 실무 포인트

이 아키텍처의 핵심은 **Risk Engine이 중심**이라는 점. KYC·KYT·Behavior가 각자 독립적으로 작동하다가 **Risk Engine에서 통합**되어 하나의 Decision이 나가는 구조여야, STR 작성 시 "이 결정에 왜 이 데이터가 쓰였나" 추적성이 확보됩니다.

---

## 7. 한국 거래소·수탁업자 기술 스택 예시

### 이 표를 어떻게 읽어야 하나

한국 시장에서 실제 쓰이는 벤더들. 대형 거래소는 **모든 영역을 커버**하고, 중소 사업자는 **핵심(KYT+Travel Rule)만 외부 벤더**, **나머지는 자체 구축**하는 경우가 많습니다.

| 영역 | 한국 시장 선택지 |
|---|---|
| **KYC SDK** | ARGOS Identity, ICONLOOP MyID, Sumsub (글로벌) |
| **본인확인** | PASS, 카카오인증, NICE, KCB |
| **PEP / 제재 DB** | LSEG World-Check, Dow Jones, ComplyAdvantage, 자체 DB |
| **KYT** | Chainalysis KYT, TRM Labs, Elliptic Lens, Crystal, 자체 |
| **Travel Rule** | VerifyVASP, CODE, Notabene |
| **Risk Engine** | 자체 (대형사) 또는 ComplyAdvantage, Quantexa |
| **Case Management** | NICE Actimize, Hummingbird, Unit21 |

---

## 8. 실무 운영 포인트

### 알람 폭주 (Alert Fatigue)

룰이 너무 느슨하면 알람 폭주 → 1선 분석가가 처리 못 함 → STR 누락. 반대로 너무 빡빡하면 false positive 다수 → 고객 불만. **룰 튜닝이 KYT 운영의 90%** 를 차지합니다.

### False Positive vs False Negative

- **FP (False Positive, 오탐)**: 정상 고객 차단 → 고객 손실
- **FN (False Negative, 미탐)**: 실제 자금세탁 통과 → 규제 위반

가상자산 영역은 **FN 비용이 더 큽니다** (벌금 수천만 달러 + 평판 파괴). 그래서 "의심되면 차단 먼저, 해제는 사후"가 기본 운영 철학. 단 고객 경험 악화와의 균형이 필요.

### 사람 + 기계

100% 자동화는 불가능. 모호한 알람은 결국 **사람 분석가의 판단**이 필요. AMLO + 1선 analyst 팀의 역량이 KYT 성과의 절반. 좋은 Case Management 도구를 쓰면 분석가 1인 생산성이 **3배**까지 차이납니다.

### 실무 포인트

알람 처리 SLA(Service Level Agreement, 처리 시간 약속)를 내부에 명문화하는 게 중요. 예: "HIGH 알람은 1시간 내 1차 리뷰, MED는 24시간 내, LOW는 72시간 내." 이 SLA가 없으면 알람이 쌓이고, 결국 규제 검사 시 "처리 안 된 알람"이 무더기로 나옵니다.

---

## 요약 부록 — 빠른 참조용

**KYC 5단계**: Onboarding · Verification · Screening · Assessment · Monitoring
**KYT 5단계**: Discovery · Attribution · Exposure · Behavior · Decision
**통합 원칙**: KYC·KYT가 공통 Risk Engine에서 단일 Risk Score로 합쳐짐
**운영 KPI**: Alert Volume · FP/FN Ratio · Alert SLA · STR Quality

## 더 읽을거리
- [`blockchain-analytics.md`](blockchain-analytics.md) — KYT의 기술적 기반 (CIOH, attribution)
- [`travel-rule-protocols.md`](travel-rule-protocols.md) — Travel Rule 기술
- [`../5-compliance/cdd-edd.md`](../5-compliance/cdd-edd.md) — CDD·EDD 운영
- [`../7-vendors/analytics-vendors.md`](../7-vendors/analytics-vendors.md) — 벤더 비교
- [Merkle Science — Enhancing AML with Blockchain Analytics](https://www.merklescience.com/enhancing-anti-money-laundering-efforts-with-advanced-blockchain-analytics)
- [CoinCover — KYT and AML overlap](https://www.coincover.com/blog/how-aml-and-kyt-overlap-with-wallet-protection-coincover)
