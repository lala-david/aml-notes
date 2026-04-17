# Travel Rule 벤더 — 시장 지도

> 메시징 프로토콜 + Travel Rule SaaS 시장. 마지막 업데이트: 2026-04-17.

## TL;DR
- 시장 양상: **컨소시엄형 (VerifyVASP, CODE, Sygna)** vs **SaaS Gateway (Notabene)** vs **분산형 (TRISA, TRP)**
- 한국 양강: **VerifyVASP** (Upbit + 글로벌) + **CODE** (빗썸/코빗/코인원)
- 글로벌 1위: **Notabene** (1500+ VASP, 멀티프로토콜 게이트웨이)
- 핵심 선택 기준: **카운터파티 호환성** + **Sunrise 대응** + **IVMS101 충실도**

---

## 1. 시장 구조

```
[ 메시지 표준: IVMS101 (모두 공통 사용) ]
                  │
   ┌──────────────┼──────────────┬──────────────────┐
   ▼              ▼              ▼                  ▼
컨소시엄형        SaaS           분산형            특화형
─────────       ─────          ─────             ─────
VerifyVASP     Notabene       TRISA            Sumsub TR
CODE           Sumsub TR      TRP              Sygna
Global TR      Global TR      OpenVASP         (KYC 통합)
                                                
사전 검증     멀티프로토콜    오픈 PKI          KYC 결합
회원사만      Gateway         누구나 참여
```

## 2. 주요 벤더 상세

### A. Notabene
- **본사**: 미국 뉴욕, 2020 설립
- **포지션**: **글로벌 1위 + 멀티프로토콜 Gateway**
- **사용자**: 1500+ VASP
- **특징**:
  - **Notabene Gateway** — TRISA/TRP/VerifyVASP/CODE 등 다중 프로토콜 동시 연결
  - **Sunrise Issue 해결책**으로 부상
  - VASP Discovery 통합
- **장점**: 한 번 연결로 글로벌 호환
- **약점**: 기업 가입비, 운영자 의존

### B. VerifyVASP
- **운영**: 람다256 (두나무 자회사) + Chainalysis
- **포지션**: **한국 + 아시아 컨소시엄**
- **사용**: Upbit, Bithumb Singapore, OKX 등 글로벌
- **특징**:
  - 사전 검증 컨소시엄 (closed)
  - Chainalysis attribution 통합
  - 한국 4대 거래소 중 Upbit 채택
- **장점**: 회원사 신뢰성, 한국 친화
- **약점**: 비회원사와 직접 호환 X (CODE/Notabene와 연동 필요)

### C. CODE (CodeVASP)
- **운영**: 코드 (빗썸+코빗+코인원 합작법인)
- **포지션**: **한국 컨소시엄**
- **사용**: 빗썸, 코빗, 코인원 + 일부 외부
- **특징**:
  - 폐쇄형 컨소시엄
  - 2022 시행 시점부터 운영
  - VerifyVASP와 연동
- **장점**: 한국 시장 깊이, 합작 거래소 자체 운영
- **약점**: 글로벌 호환성 한정

### D. Sumsub Travel Rule
- **본사**: 영국 (Sumsub은 KYC 1위 중 하나)
- **포지션**: **KYC + Travel Rule 통합**
- **특징**: KYC SDK 사용 중인 VASP에게 자연스러운 추가
- **장점**: KYC와 동일 인프라
- **약점**: KYC 미사용시 매력 적음

### E. Sygna
- **운영**: CoolBitX (대만)
- **포지션**: **아시아권 강세**
- **사용**: 일본, 동남아 거래소 다수
- **특징**: 자체 hub 구조

### F. Global Travel Rule (GTR)
- **운영**: BitGo 등 컨소시엄
- **사용**: 일부 미국·중남미

### G. TRISA
- **운영**: 비영리 (CipherTrace 시작 → Mastercard 인수)
- **포지션**: **분산형 오픈소스**
- **특징**: PKI 기반, gRPC, 오픈
- **사용**: 일부 LATAM, 신흥시장

### H. TRP
- **운영**: 21 Analytics + ING 등
- **특징**: REST API 기반, 가벼움

## 3. 벤더 선택 매트릭스

| 회사 유형 | 추천 |
|---|---|
| **한국 거래소 (대형)** | VerifyVASP 또는 CODE + Notabene Gateway (글로벌) |
| **한국 수탁업자** | (Travel Rule 적용 범위 검토 후) Notabene 또는 컨소시엄 |
| **글로벌 거래소** | Notabene Gateway (멀티프로토콜) |
| **소규모 VASP** | Notabene SaaS 또는 Sumsub (KYC 결합) |
| **EU CASP** | Notabene + TRP (TFR 임계 없음 대응) |
| **신흥시장 VASP** | TRISA (오픈소스, 무료 가능) |

## 4. 통합 vs 분리

### Travel Rule + KYT 통합 운영
```
KYC (Sumsub/ARGOS) 
  └─ Travel Rule (Sumsub 또는 Notabene)
       └─ KYT (Chainalysis/TRM)
            └─ Risk Engine (자체)
```

### 통합형 단일 벤더
- Sumsub: KYC + Travel Rule
- TRM Labs: KYT + Travel Rule (TRM Travel Rule)
- Chainalysis: KYT (Travel Rule 자체 모듈은 미약, VerifyVASP 합작 통해 제공)

## 5. 한국 시장 운영 패턴 (2026 기준)

```
Upbit (VerifyVASP 회원)
  ├─ 빗썸/코빗/코인원 (CODE) → VerifyVASP ↔ CODE 연동으로 송수신
  ├─ 글로벌 VASP → VerifyVASP 직접 또는 Notabene Gateway
  └─ 미연결 VASP → 송금 거절 또는 수동 검토

빗썸/코빗/코인원 (CODE 회원)
  ├─ Upbit → CODE ↔ VerifyVASP 연동
  ├─ 글로벌 VASP → CODE 또는 Notabene Gateway
  └─ 미연결 → 동일

Custody / 신규 VASP
  └─ Travel Rule 적용 범위 점검 (직접 이전 행위 발생 시)
     ├─ 컨소시엄 가입 (VerifyVASP 또는 CODE) — 비용 + 검증
     └─ Notabene Gateway — 빠른 진입
```

## 6. POC 체크리스트

```
□ 우리가 받는 카운터파티 VASP 호환 여부
□ IVMS101 메시지 정확도 (필드 누락/오류)
□ 응답 속도 (p99) — 사용자 UX 영향
□ Sunrise 폴백 정책 지원
□ 한국 100만원 임계 자동 계산
□ 미연결 카운터파티 처리 흐름
□ 메시지 보관 (15년) 지원
□ PII 암호화 + 한국 PIPA 호환
□ 한국어 + 한국 시간대 지원
□ 가격 모델 (트랜잭션당 vs 정액)
```

## 7. 가격 (참고치)

- 소규모: $20K~$50K/년 + 트랜잭션 당 ~$0.10
- 중규모: $80K~$200K/년
- 대규모 거래소: $500K~$1M+/년
- 컨소시엄 가입비: 별도 (VerifyVASP/CODE는 회원사 협의)

## 8. 미래 트렌드

### 표준화 / 단일화
- IVMS101 v2 등 표준 발전
- DTI (ISO 24165) 토큰 식별자 + LEI 결합
- AI 기반 자동 매칭

### 호환성 강화
- 멀티프로토콜 Gateway 표준화
- VASP Directory 글로벌화

### Privacy 강화
- ZKP 기반 PII 보호
- Selective disclosure

### FATF R.16 개정 반영
- 2026 후반 가이던스 → 모든 벤더 업데이트
- 2030 발효 대비 시스템 차세대화

## 더 읽을거리
- [`analytics_vendors.md`](analytics_vendors.md) — KYT 벤더 비교
- [`korea_solutions.md`](korea_solutions.md) — 한국 시장 솔루션
- [`../notes/3-crypto-aml/travel-rule.md`](../notes/3-crypto-aml/travel-rule.md) — Travel Rule 운영
- [`../notes/4-technology/travel-rule-protocols.md`](../notes/4-technology/travel-rule-protocols.md) — 프로토콜 기술
- [Notabene 공식](https://notabene.id/)
- [VerifyVASP 공식](https://www.verifyvasp.com/)
- [CodeVASP 공식](https://www.codevasp.com/ko)
- [TRISA 공식](https://trisa.io/)
- [21 Analytics (TRP)](https://www.21analytics.co/)
- [Sumsub Travel Rule](https://sumsub.com/travel-rule/)
