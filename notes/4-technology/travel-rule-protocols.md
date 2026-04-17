# Travel Rule Protocols — 기술 표준 / 메시징 프로토콜

> Travel Rule을 실제로 어떻게 메시지로 주고받는가. 마지막 업데이트: 2026-04-17.

## TL;DR
- **메시지 표준 = IVMS101** (사실상 글로벌 표준, 모든 프로토콜이 페이로드로 사용)
- **전송 프로토콜**은 다양: TRP, TRISA, OpenVASP, VerifyVASP, CODE, Notabene Gateway
- 두 가지 모델: **분산형 (TRISA, OpenVASP)** vs **폐쇄형 (VerifyVASP, CODE)**
- **상호운용성(interoperability)** 이 가장 큰 기술 과제 — Notabene Gateway가 부상한 이유
- **VASP Discovery** (지갑 → VASP 매핑)는 별도 인프라 (DTI, GLEIF LEI, attribution DB)

---

## 1. 표준 vs 프로토콜 — 헷갈리지 말 것

| 구분 | 역할 | 예시 |
|---|---|---|
| **메시지 표준** | 무엇을 담는가 (필드 구조) | IVMS101 |
| **전송 프로토콜** | 어떻게 주고받는가 (네트워크) | TRISA, TRP, OpenVASP, VerifyVASP, CODE |
| **VASP Discovery** | 누가 누구인가 (라우팅) | Attribution DB, DTI, GLEIF LEI |

→ 같은 IVMS101 메시지를 다른 프로토콜로 주고받을 수 있음.

## 2. IVMS101 표준 상세

### 정체성
- **InterVASP Messaging Standard 101**
- 2020년 InterVASP Joint Working Group (JWG) 합의
- 참여: Sygna(CoolBitX), TRISA(CipherTrace), Notabene, Securrency 등
- JSON Schema 기반

### 핵심 데이터 모델
```
IVMS101 Message
├── Originator (송신인)
│   ├── OriginatorPersons: [NaturalPerson | LegalPerson]
│   └── AccountNumbers: [지갑주소]
├── Beneficiary (수신인)
│   ├── BeneficiaryPersons: [...]
│   └── AccountNumbers: [...]
├── OriginatingVASP
├── BeneficiaryVASP
├── TransferPath
└── PayloadMetadata
```

### NaturalPerson 필수/선택
- **Name** (필수): primary + secondary identifier
- **GeographicAddress** (선택)
- **NationalIdentification** (선택): passport, ID 등
- **DateAndPlaceOfBirth** (선택)
- **CountryOfResidence** (선택)
- **CustomerIdentification** (선택)

### 관할별 차이 처리
- 한국: 신원확인번호 대신 이름/주소 조합 가능
- EU TFR: 모든 필드 필수 (강제력 ↑)
- 미국 BSA: 이름/주소/계좌 + (1만 USD 초과 시 ID#)

## 3. 주요 전송 프로토콜

### A. TRISA (Travel Rule Information Sharing Architecture)
- **운영**: TRISA 비영리 (CipherTrace 시작 → Mastercard 인수)
- **모델**: 분산형, 인증서 기반 (PKI)
- **특징**:
  - VASP가 X.509 인증서로 신원 확인
  - peer-to-peer gRPC 통신
  - 오픈소스
- **장점**: 누구나 참여 가능, 중앙 의존 적음
- **단점**: 운영 복잡, VASP 식별이 별도 필요

### B. TRP (Travel Rule Protocol)
- **운영**: 21 Analytics, ING 등 주도
- **모델**: REST API 기반
- **특징**:
  - 가벼움, 표준 HTTP/HTTPS
  - JWT 또는 인증서 인증
  - 빠른 구현
- **장점**: 단순함
- **단점**: 분산형이지만 식별 메커니즘 별도

### C. OpenVASP
- **운영**: OpenVASP Association (Bitcoin Suisse, Sygnum 등)
- **모델**: 분산형, Ethereum 기반
- **특징**: ENS, Whisper messaging 활용
- **현황**: 2026년 시점 활용도 낮음 (TRISA/TRP 우세)

### D. VerifyVASP
- **운영**: 람다256 (Upbit 자회사) + Chainalysis 합작
- **모델**: 폐쇄형 컨소시엄 (사전 검증된 VASP만 참여)
- **사용**: Upbit 외 다수 글로벌 거래소
- **특징**:
  - 카운터파티 신뢰성 보장
  - 한국 4대 거래소 중 Upbit 채택
  - CODE와 연동 완료

### E. CODE
- **운영**: 코드 (빗썸 + 코빗 + 코인원 합작법인)
- **모델**: 폐쇄형 컨소시엄
- **사용**: 빗썸, 코빗, 코인원 + 일부 외부
- **특징**:
  - 한국 컨소시엄
  - 2022 시행 시점부터 운영
  - VerifyVASP와 연동

### F. Notabene Gateway
- **운영**: Notabene Inc. (미국)
- **모델**: SaaS 게이트웨이 + 멀티프로토콜
- **특징**:
  - **TRISA/TRP/OpenVASP/VerifyVASP/CODE 등 다중 프로토콜 동시 지원**
  - 한 번 연결로 다 처리
  - VASP Discovery 통합
  - **Sunrise Issue 해결책**으로 부상
- **사용**: 1500+ VASP

### G. Sygna (CoolBitX)
- **운영**: 대만 CoolBitX
- **사용**: 아시아권 거래소 다수
- **특징**: 자체 hub 구조

### H. 기타
- **Sumsub Travel Rule**: KYC 통합
- **Global Travel Rule (GTR)**: BitGo 등 일부 사용

## 4. 분산형 vs 폐쇄형 — 트레이드오프

| 항목 | 분산형 (TRISA, OpenVASP) | 폐쇄형 (VerifyVASP, CODE) |
|---|---|---|
| **참여 진입장벽** | 낮음 (오픈) | 높음 (검증 필요) |
| **신뢰 모델** | 인증서 + 검증 | 컨소시엄 사전 검증 |
| **확장성** | 높음 (이론) | 낮음 (회원사 한정) |
| **라우팅** | 별도 식별 필요 | 컨소시엄 내 자동 |
| **운영 책임** | 각자 | 컨소시엄 운영자 |
| **한국 적합성** | 낮음 | 높음 (실제 채택) |

## 5. VASP Discovery — 지갑 주소가 어느 VASP인가

### 문제
- 출금 주소 `0xABC...` 가 들어오면, 어느 VASP의 것인지 알아야 그 VASP로 메시지 보냄
- 지갑 주소만 봐서는 식별 불가

### 해결책

#### A. Attribution DB 활용
- Chainalysis/TRM/Elliptic의 라벨 DB
- 알려진 거래소 deposit 주소 → 해당 거래소 식별
- **자체 deposit 주소 ≠ 거래소 식별 정보 누락 가능성**

#### B. VASP Directory 서비스
- **OpenVASP Directory, TRISA Directory, Notabene Directory**
- 각 VASP의 메시징 endpoint + 인증서 등록
- 카운터파티 직접 조회

#### C. DTI (Digital Token Identifier, ISO 24165)
- ISO 표준 토큰 식별자 + VASP LEI 연결
- 2024년부터 EU 등 채택 시작

#### D. GLEIF LEI (Legal Entity Identifier)
- 법인 식별 글로벌 표준
- VASP가 LEI 보유 시 메시지에 포함

#### E. 카운터파티 직접 등록
- VASP끼리 사전에 주소 화이트리스트 교환

## 6. 호환성 / Interoperability 문제

### Sunrise Issue (미시행 관할 카운터파티)
- 일부 국가는 Travel Rule 시행 안 함
- → 메시지 수신할 인프라 없음
- 해결: 폴백 정책 (송금 보류, 수동 확인, 거절)

### Protocol Mismatch
- A 거래소는 TRISA 사용, B는 VerifyVASP 사용
- 직접 호환 안 됨
- 해결: **Notabene Gateway** 같은 멀티프로토콜 hub
- 또는 양 프로토콜 동시 지원 (한국: VerifyVASP + CODE 양쪽 가입)

### Schema Version Mismatch
- IVMS101에도 마이너 버전 차이 존재
- 필드 매핑 mismatch 가능성
- 해결: 표준 컨버터 / fallback 매핑

## 7. 한국 시장 운영 패턴

```
Upbit (VerifyVASP)
  ├─ 해외 VASP에게 송금: VerifyVASP 직접 또는 Notabene Gateway 경유
  └─ 빗썸/코빗/코인원에게 송금: VerifyVASP ↔ CODE 연동

빗썸/코빗/코인원 (CODE)
  ├─ 해외 VASP에게 송금: CODE 또는 Notabene Gateway
  └─ Upbit에게 송금: CODE ↔ VerifyVASP 연동

수탁업자 — Travel Rule 적용 범위 검토 필요
  ├─ 고객 출금 시 외부 VASP로 가면 적용
  └─ 내부 wallet 간 이동은 적용 X
```

## 8. 기술 스택 통합 예시

```
[ User Request: 출금 ]
        ▼
[ KYC/KYT 1차 체크 ]
        ▼
[ Sanctions Screening ]
        ▼
[ Travel Rule SDK ]
   ├─ Counterparty Discovery (Attribution DB)
   ├─ IVMS101 Message Build
   ├─ Protocol Selection (TRISA / VerifyVASP / CODE / ...)
   ├─ Send via Notabene Gateway or Direct
   ▼
[ Counterparty VASP Response ]
   ├─ Accept → 계속
   ├─ Reject → 송금 거절, 사용자 통지
   ├─ Hold → 수동 검토
   └─ Timeout → 폴백 정책
        ▼
[ On-chain Broadcast ]
        ▼
[ Travel Rule Message 보관 (15년) ]
```

## 9. 회사 도입 체크리스트

```
□ 메인 프로토콜 선택 (한국이면 VerifyVASP 또는 CODE)
□ 글로벌 호환성 (Notabene Gateway 등 검토)
□ IVMS101 메시지 검증 로직
□ Counterparty Discovery 인프라
□ 미연결 카운터파티 폴백 정책 명문화
□ 메시지 보관 (한국 15년, EU 5년 등)
□ PII 암호화 + 접근 통제
□ Audit Log
□ 시간 동기화 (NTP) — 메시지 timestamp 일치
□ 인증서 갱신 자동화 (TRISA의 경우)
```

## 더 읽을거리
- [`../notes/3-crypto-aml/travel-rule.md`](../notes/3-crypto-aml/travel-rule.md) — Travel Rule 운영
- [`../notes/7-vendors/travel-rule-vendors.md`](../notes/7-vendors/travel-rule-vendors.md) — 벤더 비교
- [`../notes/7-vendors/korea-solutions.md`](../notes/7-vendors/korea-solutions.md) — 한국 시장
- [Notabene — IVMS101 분석](https://notabene.id/travel-rule-messaging-protocols/ivms-101)
- [Notabene — VerifyVASP 분석](https://notabene.id/travel-rule-messaging-protocols/verifyvasp)
- [21 Analytics — Open-Source IVMS101](https://www.21analytics.co/blog/21-analytics-open-sources-its-intervasp-ivms-101-implementation/)
- [Sygna — IVMS101 합의 발표](https://www.sygna.io/blog/joint-working-group-adopts-ivms101-crypto-messaging-standard-for-fatf-travel-rule/)
- [VerifyVASP IVMS101 문서](https://docs.verifyvasp.com/reference/ivms101/ivms101)
- [CodeVASP 공식 사이트](https://www.codevasp.com/ko)
