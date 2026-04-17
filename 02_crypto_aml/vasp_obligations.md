# VASP 의무 — 가상자산사업자가 해야 할 일 정리

> VASP가 법적·실무적으로 떠안는 9대 의무를 한 장에. 마지막 업데이트: 2026-04-17.

## TL;DR
- VASP 의무는 글로벌(FATF) → 각국법(특금법/BSA/AMLR)으로 내려옴
- 핵심 9가지: **신고/라이센스 → KYC/CDD → EDD → 거래 모니터링 → 제재 스크리닝 → STR/CTR → Travel Rule → 기록보관 → 내부통제**
- **수탁업자(custody)도 VASP** — 의무는 거래소와 동일 (강도는 상품 특성에 따라 RBA로 차등)
- 한국에서 위반 시: 형사처벌 + 신고 취소 + 평판 리스크

---

## 1. VASP 정의 다시 확인

| 관할 | 용어 | 정의 (간단히) |
|---|---|---|
| FATF | VASP | 매수도/교환/이전/보관/관련 금융서비스 영업 |
| 한국 | 가상자산사업자 | 매도매수/교환/이전/보관관리/중개 (특금법 §2) |
| 미국 | MSB (Money Services Business) | 가상통화 administrator/exchanger |
| EU | CASP | 수탁/거래소/주문집행/포트폴리오관리/이전/자문/인수배치 (MiCA) |

→ 실질 정의는 거의 같음. **수탁(custody)도 VASP** 라는 게 핵심.

## 2. VASP 9대 의무 (RBA 기반)

```
   ┌─────────────────────────────────────┐
   │  1. 신고/라이센스 (Authorization)     │  ← 진입 단계
   ├─────────────────────────────────────┤
   │  2. KYC / CDD                        │
   │  3. EDD (고위험 고객)                  │  ← 고객 단계
   │  4. 거래 모니터링 / KYT                │
   │  5. 제재 스크리닝 (Sanctions)          │
   │  6. STR / CTR (의심거래/현금거래 보고)   │  ← 운영 단계
   │  7. Travel Rule (송수신인 정보 동반)    │
   │  8. 기록 보관 (Record Keeping)         │
   ├─────────────────────────────────────┤
   │  9. 내부통제 + AMLO (조직)             │  ← 거버넌스
   └─────────────────────────────────────┘
```

### 1. 신고/라이센스
- 한국: FIU 신고 (3년 갱신, 2026-01 개정으로 대주주 자격심사 추가)
- 미국: FinCEN MSB 등록 + 주별 Money Transmitter License
- EU: MiCA CASP 라이센스 (NCA 발급, EU passporting)

### 2. KYC / CDD
- 신원확인: 이름, 생년월일, 주소, 연락처
- **실소유자(Beneficial Owner) 확인**: 법인 25% 지분 자연인
- **거래 목적 / 자금 원천** 파악
- **지속 모니터링** — onboarding 1회로 끝나지 않음

### 3. EDD (강화된 실사)
- 트리거: PEP, 고위험국, 비대면 + 추가 위험요소, 거액거래, 복잡한 소유구조
- 추가 절차: 자금/자산 출처 증빙, 고위경영진 승인, 더 빈번한 재실사

### 4. 거래 모니터링 / KYT
- 룰 기반 + 머신러닝 기반 패턴 탐지
- **온체인 KYT** — 가상자산은 추가로 입출금 주소의 위험 노출 분석
- 알람 발생 → 1선 검토 → 2선 escalation → 필요시 STR

### 5. 제재 스크리닝
- 고객 신원 vs OFAC/UN/EU/한국 외교부 명단
- **지갑 주소 vs OFAC SDN 가상자산 주소** (실시간 차단)
- 공급망 거래(예: 결제 수신) 시에도 스크리닝

### 6. STR / CTR
- **STR**: 의심되면 지체 없이 FIU에 보고 (금액 무관)
- **CTR**: 한국 1천만원, 미국 $10K 이상 현금거래 (가상자산은 적용 모호)
- **누설 금지** (tipping-off): 고객에게 STR 사실 알리면 별도 처벌

### 7. Travel Rule
- 임계금액 이상 VASP 간 이전 시 송수신인 정보 동반
- 한국: 100만원 / 미국: $3,000 / EU: 임계 없음
- 솔루션 연동 필수 (CODE / VerifyVASP / Notabene 등)

### 8. 기록 보관
- 한국: **15년** (가상자산이용자보호법, 더 긴 쪽 적용)
- 미국 BSA: 5년
- EU AMLR: 5년 (논의 중)
- 보관 대상: KYC 자료, 거래 기록, STR 사본, 내부 조사 기록

### 9. 내부통제 + AMLO
- **자금세탁방지 보고책임자(AMLO/MLRO) 임명** — 임원급
- AML 정책·절차 문서화
- **3중 방어선** (영업/컴플라이언스/감사)
- 임직원 정기 교육 (연 1회 이상)
- 내부 감사 + 외부 감사

## 3. 사업 유형별 의무 강도 차이 (RBA)

| 사업 유형 | KYC | KYT | Travel Rule | 특이사항 |
|---|---|---|---|---|
| **거래소** (Upbit, 빗썸) | 강 | 강 | 강 | 가장 풀스택, 상장심사 의무 |
| **수탁업** (custody) | 중~강 | 중 | 부분적용 (이전 시) | **자산 분리보관** 최우선 |
| **OTC desk** | 강 | 중 | 강 | 거액 거래 → STR 트리거 多 |
| **결제 PG** | 중 | 강 | 강 | 가맹점 KYC + 거래 실시간 |
| **NFT 마켓플레이스** | 중 | 중 | 약 | wash trading 모니터링 |
| **DeFi 프로토콜** | (사업자 식별 어려움) | — | — | 회색지대, 입법 진행 중 |

→ 수탁업은 KYC + 자산 분리보관 + 보안이 1순위. 거래소는 모든 영역 풀스택.

## 4. 의무 위반 → 처벌

| 관할 | 미신고 영업 | KYC 위반 | STR 미보고 |
|---|---|---|---|
| 한국 | 5년/5천만원 | 1년/1천만원 | 1년/1천만원 |
| 미국 | $250K~ + 형사 | 민사벌금 | $500K~ |
| EU | 회원국별, 최대 €10M 또는 매출 5% | 동일 | 동일 |

→ 추가로: **신고 취소 + CCO/CEO 개인 책임 + 평판 리스크**.

## 5. 회사 컴플라이언스 프로그램 (실무 4 pillars)

미국 BSA가 명시한 **4 pillars** + 확장 (5 pillars로 확장됨):

1. **Internal Controls** — 정책, 절차, 시스템
2. **Designated AMLO** — 임명된 책임자
3. **Training** — 임직원 교육
4. **Independent Audit** — 독립 감사
5. **CDD / Beneficial Ownership** — 2018 추가

→ 한국 FIU 검사 시에도 사실상 이 5개 항목을 봄.

## 6. 수탁업자(custody) 관점 추가 의무

수탁업은 거래 자체를 적게 하지만 다음이 핵심:

- **자기자산-고객자산 분리** (가상자산이용자보호법)
- **고객별 segregated wallet** vs **omnibus wallet** 정책
- **콜드월렛 비율** (시행령 80%)
- **출금 승인 다중서명 (MPC/HSM)**
- **출금 시 KYT** — 외부 보내는 주소가 OFAC SDN, mixer, 도난자금 노출인지
- **재증명(Proof of Reserves)** — 고객 자산 실제 보유 증명

## 더 읽을거리
- [`travel_rule.md`](travel_rule.md) — Travel Rule 상세
- [`onchain_typology.md`](onchain_typology.md) — 온체인 자금세탁 유형
- [`../03_technology/kyc_kyt_overview.md`](../03_technology/kyc_kyt_overview.md) — KYC/KYT 기술
- [`../04_compliance_ops/cdd_edd.md`](../04_compliance_ops/cdd_edd.md) — CDD/EDD 운영
- [FIU — 가상자산사업자 신고 매뉴얼](https://www.fsc.go.kr/comm/getFile?srvcId=BBSTY1&upperNo=75409&fileTy=ATTACH&fileNo=6)
