# CDD / EDD — 고객실사 운영 실무

> 표준 실사(CDD)와 강화 실사(EDD)를 어떻게 수행하는가. 마지막 업데이트: 2026-04-17.

## TL;DR
- **CDD**: 모든 고객에게 적용하는 표준 실사 4단계 (식별 → 실소유자 → 목적 → 모니터링)
- **EDD**: 고위험 고객에게만 적용하는 강화 실사 (자금원천 증빙 + 경영진 승인 + 강화 모니터링)
- EDD 트리거: **PEP, 고위험국, 비대면+위험요소, 거액거래, 복잡한 소유구조**
- 가상자산은 **100% 비대면**이라 항상 위험가중 + 거래 패턴 vs 신고 의도 비교가 핵심
- 한국: 위험기반접근법(RBA) 처리기준 가이드라인이 운영 바이블

---

## 1. CDD (Customer Due Diligence) 표준 4단계

### Step 1. 신원확인 (Identification & Verification)

| 항목 | 개인 | 법인 |
|---|---|---|
| 필수 | 이름, 생년월일, 주소, 연락처 | 법인명, 사업자번호, 주소, 대표자, 사업목적 |
| 검증 방법 | 신분증 OCR + 셀카 + Liveness + 본인확인기관 | 등기부등본, 사업자등록증, 정관 |
| 보완 | 휴대폰/이메일 인증 | 주주명부, 임원 명단 |

### Step 2. 실소유자(Beneficial Owner) 확인 — 법인만

- **25% 이상 지분 자연인** 또는 **실질 지배 자연인** 식별
- 한국: 25% 기준 (특금법 시행령)
- EU: 25% (논의 중 인하 가능성)
- 다층 구조면 끝까지 추적 (UBO, Ultimate Beneficial Owner)
- 식별 안 되면 **고위 경영진 자연인** 을 임시 BO로

### Step 3. 거래 목적 / 자금 원천 파악

- 거래 목적 (예: 투자, 결제, 수탁, 사업 운영)
- 예상 거래 금액 / 빈도 / 상대국
- 자금 원천 (Source of Funds): 어디서 온 자금인가
- 자산 원천 (Source of Wealth): 전체 자산이 어떻게 형성됐는가 (EDD에서 강조)

### Step 4. 지속 모니터링

- KYC 정보가 최신인지 주기적 점검
- 거래 패턴 vs Step 3에서 신고한 의도 일치하는가
- 위험요소 변경 시 (PEP 신규, 고위험국 이주 등) 재실사
- 한국 가이드라인: 저위험 5년 / 중위험 3년 / 고위험 1년 주기 재실사

## 2. EDD (Enhanced Due Diligence) — 트리거와 추가 절차

### EDD 트리거 (자동 발동)
| 카테고리 | 사례 |
|---|---|
| **PEP** | 정치적 주요인물 본인/가족/측근 |
| **고위험국** | FATF Black/Grey, 한국 외교부 분류 |
| **비대면 + 추가 위험** | (가상자산은 항상 비대면, 추가 요소로 트리거) |
| **거액거래** | 신고 의도 대비 과도한 금액 |
| **복잡한 소유구조** | shell company, 다층 holding |
| **현금집약 업종** | 카지노, 귀금속, 환전, 부동산 |
| **고위험 상품** | privacy coin, 익명 wallet, mixer 노출 |
| **부정적 보도** | adverse media 매칭 |

### EDD 추가 절차
1. **자금/자산 원천 증빙** — 급여명세, 사업자료, 계좌내역 등 증빙 요구
2. **고위 경영진 승인** — 임원급 결재 필수 (CCO/AMLO)
3. **강화 모니터링** — 거래 임계값 낮춤, 알람 우선순위 ↑
4. **재실사 주기 단축** — 보통 1년
5. **추가 정보 수집** — 직업, 소득, 사업 파트너, 거래 상대국

## 3. 한국 가이드라인 — RBA 처리기준

FIU의 「위험기반접근법(RBA) 처리기준」 가이드라인:

### 4가지 위험 차원
1. **고객 위험** — 직업, PEP 여부, 거주지
2. **상품/서비스 위험** — 가상자산 종류, 수탁 vs 매매
3. **거래 위험** — 금액, 빈도, 상대국
4. **국가/지역 위험** — FATF 분류, 외교부 분류

### 종합 등급
- **저위험 (LOW)** — SDD 가능 (제한적)
- **중위험 (MEDIUM)** — 표준 CDD
- **고위험 (HIGH)** — EDD 필수
- **수용불가 (UNACCEPTABLE)** — 거래 거절

## 4. 가상자산 특화 실사 항목

### A. Wallet Ownership Verification (지갑 소유 증명)
- 사용자가 출금받을 외부 지갑이 본인 것인지 증명
- 방법:
  - **Satoshi Test**: 소액 입금 후 같은 wallet에서 회신
  - **Signed Message**: 해당 wallet의 private key로 메시지 서명 → 검증
  - **셀카 + 지갑주소 인증샷**
- 한국 거래소 외부지갑 등록제의 핵심

### B. KYT 노출도 점검
- 입금 wallet이 mixer/SDN/도난자금에 노출되어 있는가
- 출금 받을 wallet이 same
- KYT 시스템이 자동 점검

### C. 거래 패턴 vs 신고 의도
- "월 1천만원 투자" 신고했는데 일 1억 거래 → 트리거
- 신고 직업과 거래 규모 불일치

### D. Source of Crypto (가상자산 원천)
- 입금 가상자산이 어디서 왔는가
- 직접 채굴? 다른 거래소? OTC? 무허가 거래소?
- 무허가/고위험 출처면 EDD

## 5. CDD/EDD 실패 시 액션

| 상황 | 액션 |
|---|---|
| 신원확인 실패 | 거래 거절, 계정 미개설 |
| EDD 정보 거부 | 거래 제한, 단계적 거절 |
| 고위험 등급 + 대응 불가 | 계좌 폐쇄 + STR 검토 |
| 계좌 폐쇄 결정 | 사유 문서화, 지급 정산 |
| Tipping-off (고객 통지 금지) | STR 사실은 절대 알려주지 말 것 |

## 6. 운영 흐름 예시

```
[ 신규 가입 신청 ]
        ▼
[ KYC: 신분증 + 셀카 + Liveness ]
        ▼
[ 본인확인기관 (PASS 등) 검증 ]
        ▼
[ PEP / Sanctions / Adverse Media 스크리닝 ]
        ▼
[ Risk Score 계산 ]
   ├─ LOW/MED → CDD 완료, 거래 가능
   └─ HIGH → EDD 트리거
                  ▼
            [ 자금원천 증빙 요구 ]
                  ▼
            [ 경영진(CCO/AMLO) 승인 ]
                  ▼
            [ 거래 가능 + 강화 모니터링 라벨 ]

[ 이후 ]
거래 발생 → KYT + 패턴 분석
   ├─ 정상 → 통과
   └─ 알람 → Case Management → STR 검토
```

## 7. 자주 쓰는 외부 데이터

| 데이터 | 벤더 |
|---|---|
| **PEP DB** | LSEG World-Check, Dow Jones Risk Center, ComplyAdvantage |
| **Sanctions** | OFAC SDN (직접), UN, EU, HM Treasury, 한국 외교부 |
| **Adverse Media** | ComplyAdvantage, RDC, LSEG |
| **국가 위험** | Basel AML Index, FATF 발표, Transparency Int'l |
| **본인확인** | PASS, NICE, KCB, 카카오인증 |

## 8. 흔한 실수와 함정

- **CDD를 onboarding으로만 끝냄** — 지속 모니터링이 빠짐
- **PEP 정의 너무 좁음** — 가족/측근까지 포함해야 함
- **BO를 명목상 대표로 끝냄** — 실질 지배자까지 추적해야
- **EDD를 "추가 신분증"으로만 이해** — 핵심은 자금원천 증빙
- **Tipping-off 위반** — 고객에게 STR 사실 말함 (별도 처벌)
- **자료 보관 누락** — 검사 시 증빙 못하면 제재

## 9. 체크리스트

```
□ 모든 고객 CDD 4단계 완료
□ 법인고객 BO (25% 자연인) 확인
□ 위험등급 산정 + 주기적 재평가
□ EDD 트리거 자동화 (PEP/제재/고위험국/거액)
□ 자금원천 증빙 받는 절차
□ 경영진 승인 워크플로
□ 외부지갑 소유 증명 절차
□ Tipping-off 금지 교육
□ KYC 자료 15년 보관 (한국 가상자산이용자보호법 §11)
□ Case Management 시스템
```

## 더 읽을거리
- [`str_ctr.md`](str_ctr.md) — STR/CTR 보고
- [`sanctions_screening.md`](sanctions_screening.md) — 제재 스크리닝
- [`internal_controls.md`](internal_controls.md) — 내부통제
- [`../03_technology/kyc_kyt_overview.md`](../03_technology/kyc_kyt_overview.md) — KYC/KYT 기술
- [FIU — 자금세탁방지 업무규정](https://www.kofiu.go.kr/)
