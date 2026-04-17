# Travel Rule — 가상자산 송수신인 정보 동반 의무

> FATF R.16의 가상자산 적용. 운영 난이도 1순위. 마지막 업데이트: 2026-04-17.

## TL;DR
- VASP가 다른 VASP에게 가상자산을 이전할 때 **송신인+수신인 정보를 함께 전달** 해야 하는 의무
- 임계금액: **한국 100만원 / 미국 $3,000 / EU 없음 (모든 거래) / FATF 권고 USD-EUR 1,000**
- **Sunrise Issue** (관할별 시행 격차)와 **VASP 식별** (지갑주소만 보고 누구 VASP인지 알기 어려움)이 핵심 난제
- 메시지 표준: **IVMS101** (사실상 글로벌 표준)
- 프로토콜: **TRP, TRISA, OpenVASP, VerifyVASP, CODE, Notabene Gateway**
- 한국: **VerifyVASP** (Upbit) + **CODE** (빗썸/코빗/코인원) — 두 솔루션 연동

---

## 1. Travel Rule이 뭐고 왜 만들어졌나

전통 송금에서 SWIFT MT103 메시지에 송신인/수신인 정보가 함께 가듯이, 가상자산 이전에서도 **돈만 보내지 말고 사람 정보도 같이 보내라**는 의무.

**원래는** 미국 BSA의 1996년 룰 → **FATF가 2019년 권고 16(R.16)을 가상자산까지 확장**.

목적:
- 자금세탁의 **layering 단계 차단**
- VASP 간 책임 추적 가능성 확보
- 수신 측에서 **이상 거래(SDN, mixer 등) 사전 차단**

## 2. 핵심 정보 항목

### 송신인(Originator) 정보
| 필드 | FATF | 한국 | EU TFR |
|---|---|---|---|
| 이름 | ✅ | ✅ | ✅ |
| 가상자산 주소 | ✅ | ✅ | ✅ |
| 신원확인번호 (또는 출생지/생년월일) | ✅ | (정보보호 이슈로 일부) | ✅ |
| 주소 | ✅ | (이름+주소 둘 중 하나) | ✅ |

### 수신인(Beneficiary) 정보
| 필드 | FATF | 한국 | EU TFR |
|---|---|---|---|
| 이름 | ✅ | ✅ | ✅ |
| 가상자산 주소 | ✅ | ✅ | ✅ |

→ 송신인 정보가 항상 더 많이 요구됨 (수신인은 이미 받는 측 VASP가 알고 있음).

## 3. 임계금액 비교

| 관할 | 임계 | 비고 |
|---|---|---|
| FATF 권고 | USD/EUR 1,000 | 회원국 자율 결정 |
| **한국** | **100만원** | 특금법 시행령 §10의10 |
| **미국 (FinCEN)** | **$3,000** | BSA Travel Rule 1996 |
| **EU TFR** | **없음 (모든 거래)** | 가장 엄격 |
| 일본 | 100,000엔 | 2023 시행 |
| 싱가포르 | SGD 1,500 | 2020 시행 |

→ 한국 사업자가 EU 카운터파티와 거래 시 **EU 기준(임계 없음)** 으로 해야 함.

## 4. 메시지 표준: IVMS101

### 정체성
- **InterVASP Messaging Standard 101** — Travel Rule 메시지의 글로벌 표준
- 2020년 InterVASP 공동 작업 그룹(JWG) 합의
- JSON Schema로 송수신인 정보 표준화
- **모든 주요 프로토콜이 IVMS101을 메시지 페이로드로 사용**

### 핵심 구조
```json
{
  "originator": {
    "naturalPerson": {
      "name": { "primaryIdentifier": "...", "secondaryIdentifier": "..." },
      "geographicAddress": { ... },
      "dateAndPlaceOfBirth": { ... },
      "nationalIdentification": { ... }
    },
    "accountNumber": ["bc1q..."]
  },
  "beneficiary": { ... },
  "originatingVASP": { "legalPerson": { ... } },
  "beneficiaryVASP": { ... },
  "transferPath": { ... }
}
```

→ 프로토콜은 달라도 메시지 안의 정보는 IVMS101로 통일됨.

## 5. Travel Rule 프로토콜 (전송 방식)

| 프로토콜 | 운영 | 모델 | 비고 |
|---|---|---|---|
| **TRISA** | 비영리, CipherTrace 시작 | 분산형 | 인증서 기반, 오픈소스 |
| **TRP** | 21 Analytics 등 | API 기반 | REST, 가벼움 |
| **OpenVASP** | OpenVASP Association | 분산형 | Ethereum 기반 |
| **VerifyVASP** | Upbit + Chainalysis 합작 | 폐쇄형 (consortium) | 한국 + 글로벌 |
| **CODE** (Code) | 빗썸+코빗+코인원 합작 | 폐쇄형 (consortium) | 한국 |
| **Notabene** | Notabene Inc. (미국) | SaaS, 멀티프로토콜 | Gateway로 다른 프로토콜 연결 |
| **Sumsub Travel Rule** | Sumsub | SaaS | KYC 통합 |
| **Sygna** | CoolBitX (대만) | API | 아시아 강세 |

### 분산형 vs 폐쇄형
- **분산형(TRISA, OpenVASP)**: 누구나 참여 가능, 신뢰는 인증서로
- **폐쇄형(VerifyVASP, CODE)**: 사전 검증된 VASP만 참여, 신뢰는 컨소시엄으로

## 6. 한국 시장의 Travel Rule

### 두 솔루션 양강 체제
| 솔루션 | 운영자 | 사용 거래소 |
|---|---|---|
| **VerifyVASP** | 람다256 (두나무 자회사) + Chainalysis | **Upbit**, 다수 글로벌 |
| **CODE** | 코드 (빗썸+코빗+코인원 합작법인) | **빗썸, 코빗, 코인원** |

### 두 솔루션 연동
- 2022-03-25 시행 직후엔 **분리** 운영 → 4대 거래소 간 송금 불가능 시기 존재
- 시행 1개월여 후 **VerifyVASP ↔ CODE 연동** 완료
- 현재는 **4대 거래소 간 자유로운 송금** 가능

### 외부지갑(unhosted wallet) 등록제
- 거래소가 자체 정책으로 **출금 받을 외부지갑을 사전 등록** 받음
- 등록 시 본인인증 (인증샷 + 화이트리스트)
- 법령 강제는 아니지만 **사실상 표준** 운영

## 7. 두 가지 핵심 난제

### A. Sunrise Issue (관할별 시행 격차)
- A국은 시행, B국은 미시행 → A국 VASP가 B국 VASP에게 송금 시 메시징 불가
- **Notabene 같은 멀티프로토콜 게이트웨이** 가 부상한 이유
- 해결: 글로벌 동시 시행이 이상이지만 현실은 점진적 → **무선택 폴백 정책** (예: 송금 보류, 자체 검토)

### B. VASP 식별 (Counterparty Discovery)
- 지갑주소만 보고 그게 어느 VASP의 것인지 어떻게 아는가?
- 해결책:
  - **Chainalysis/TRM/Elliptic 의 attribution DB** — 주소 → VASP 매핑
  - **자체 검증 컨소시엄** (VerifyVASP, CODE) — 회원사 주소 사전 등록
  - **API 조회** (Notabene Gateway가 멀티 DB 통합 조회)
  - **DTI (Digital Token Identifier)** — 토큰 ID 표준화 (ISO 24165)

### C. (보너스) Personal Data 보호
- Travel Rule은 PII(개인정보)를 VASP 간 전송하는 것 → **GDPR/한국 개인정보보호법** 충돌
- 해결: 암호화 전송, 목적 한정, 보존 기간 명확화
- EU TFR도 GDPR 호환 명시

## 8. 운영 흐름 (한국 거래소 출금 예시)

```
1. 사용자 A → Upbit에서 1억원 ETH를 빗썸 사용자 B에게 출금 요청
2. Upbit 시스템 → 출금 요청을 KYT 시스템에 통과
3. KYT → 수신 주소 위험도 체크 (mixer? SDN? 화이트리스트?)
4. Upbit 시스템 → VerifyVASP Travel Rule 메시지 생성 (IVMS101)
5. VerifyVASP ↔ CODE 게이트웨이를 통해 빗썸으로 메시지 전송
6. 빗썸 → 메시지 수신, 수신인 B 정보 확인 (자기 고객인지)
7. 빗썸 → 수락 응답 → Upbit
8. Upbit → 온체인 송금 실행 (트랜잭션 broadcast)
9. 빗썸 → 입금 확인, B의 잔고에 반영
10. 양사 → Travel Rule 메시지 보관 (15년)
```

→ 5번 메시지 교환이 안 되거나 timeout 시 **송금 자체가 멈춤** = 사용자 UX 충격. 그래서 카운터파티 호환성이 운영 핵심.

## 9. 2025-06-18 FATF R.16 개정의 영향

- 결제 산업 변화 반영, 메시징 표준 명확화
- VASP는 **별도 tailored framework** 로 적용
- **2026 후반 가이던스 발표 예정** — 한국 FIU도 이를 반영한 시행령 개정 가능성
- **2030년 말 발효** — 회사들은 그전에 시스템 업그레이드 준비

## 10. 회사 체크리스트

```
□ Travel Rule 솔루션 도입 (VerifyVASP / CODE / Notabene 등)
□ IVMS101 메시지 정확성 검증
□ 카운터파티 VASP 호환성 점검 (Sunrise Issue)
□ 미연결 카운터파티 처리 정책 (송금 거절/보류)
□ unhosted wallet 등록제 운영
□ Travel Rule 메시지 15년 보관
□ 개인정보보호법/GDPR 호환성 점검
□ 2026 후반 FATF 가이던스 모니터링
```

## 더 읽을거리
- [`vasp_obligations.md`](vasp_obligations.md) — VASP 의무 종합
- [`../notes/4-technology/travel-rule-protocols.md`](../notes/4-technology/travel-rule-protocols.md) — 프로토콜 기술 상세
- [`../notes/7-vendors/travel-rule-vendors.md`](../notes/7-vendors/travel-rule-vendors.md) — 벤더 비교
- [`../notes/7-vendors/korea-solutions.md`](../notes/7-vendors/korea-solutions.md) — 한국 솔루션
- [Notabene — Travel Rule Messaging Protocols](https://notabene.id/travel-rule-messaging-protocols)
- [21 Analytics — FATF Travel Rule Status 2026](https://www.21analytics.co/blog/fatf-crypto-travel-rule-status-2026/)
- [Sumsub — FATF Travel Rule 2026](https://sumsub.com/blog/what-is-the-fatf-travel-rule/)
- [TokenPost — 한국 거래소 트래블룰 정리](https://www.tokenpost.kr/article-88025)
