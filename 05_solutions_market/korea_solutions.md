# 한국 시장 솔루션 지도

> 한국 가상자산 AML 인프라를 만드는 회사들. 마지막 업데이트: 2026-04-17.

## TL;DR
- **KYC**: ARGOS Identity, ICONLOOP MyID, NICE/KCB (본인확인기관), Sumsub (글로벌)
- **본인확인**: PASS, 카카오인증, NICE, KCB, KISA 본인확인기관
- **KYT**: Chainalysis, TRM Labs, Elliptic (글로벌 4사 모두 한국 진입)
- **Travel Rule**: VerifyVASP (Upbit계) + CODE (빗썸/코빗/코인원 합작) + Notabene (글로벌)
- **수탁/MPC**: 한국디지털자산수탁 계열 (신한은행 파트너), Kodax (KB+해시드+해치랩스), Bestcoin Custody, BitGo Korea (검토 진행)
- **거래 모니터링/Case Management**: 자체 구축 + Solidus Labs / NICE Actimize 일부

---

## 1. 한국 가상자산 산업 지도 (간략)

```
[ 거래소 ]                   [ 수탁/Custody ]              [ 분석/솔루션 ]
업비트 (두나무)             신한은행 계열 수탁사              람다256, 블록체인 R&D 다수
빗썸                        Kodax (KB+해시드+해치랩스)       Chainalysis Korea
코빗 (NXC)                  BitGo Korea (검토)              TRM Labs Korea
코인원                      Bestcoin Custody                Elliptic
GOPAX                       (은행 자체 수탁 검토)            ARGOS Identity
한빗코                                                      ICONLOOP
프로비트                                                    오지스 등
                            
[ 본인확인 ]                 [ 위험 데이터 ]                  [ 인프라 ]
PASS (이통3사)              World-Check                     KISA
NICE                        Dow Jones Risk Center           한국인터넷진흥원
KCB                         ComplyAdvantage                 (ISMS 인증)
카카오인증                   외교부 제재명단                  
```

## 2. KYC / 본인확인

### 한국 특수: 본인확인기관
한국 「정보통신망법」 의 "본인확인기관" 지정 받은 곳:
- **PASS** — SKT/KT/LG U+ 합작 (이통사 본인확인)
- **NICE 평가정보**
- **KCB (Korea Credit Bureau)**
- **금융결제원**
- **카카오인증**

→ 가상자산 거래소가 KYC 시 거의 필수로 사용 (실명 + 휴대폰 + 신분증).

### KYC SDK/플랫폼
| 회사 | 강점 |
|---|---|
| **ARGOS Identity** | 한국 토종, 가상자산 거래소 다수 사용, 글로벌 KYC 지원 |
| **ICONLOOP (MyID)** | DID 기반, 신한은행 등 |
| **Sumsub** | 글로벌 1위 KYC, 한국 진입 활발 |
| **Onfido** | 글로벌, 일부 한국 사용 |
| **Veriff** | 글로벌 |
| **Jumio** | 글로벌, 신분증 검증 강세 |

## 3. KYT / Blockchain Analytics (한국 진입)

### 글로벌 4사 모두 진입
- **Chainalysis** — 한국 사무소, 람다256과 합작 (VerifyVASP)
- **TRM Labs** — 한국 영업 활발
- **Elliptic** — 한국 진입
- **Crystal Intelligence** — 한국 진입
- **Merkle Science** — 한국 일부

### 한국 자체
- 글로벌 attribution 따라가기 어려워 토종 KYT 회사는 적음
- 일부 블록체인 R&D 회사가 자체 분석 모듈 보유

## 4. Travel Rule

### 양강 구도 (한국)
| 솔루션 | 회원사 | 운영자 |
|---|---|---|
| **VerifyVASP** | Upbit + 글로벌 다수 | 람다256 (두나무) + Chainalysis |
| **CODE** | 빗썸, 코빗, 코인원 | 코드 (3사 합작법인) |

### 두 솔루션 연동
- 2022-03-25 시행 직후 분리 → 1개월 후 연동
- 현재 4대 거래소 간 자유 송금 가능

### 글로벌 호환
- Notabene Gateway 사용 시 글로벌 1500+ VASP 호환
- VerifyVASP 자체도 글로벌 회원사 다수

## 5. 수탁 (Custody)

| 회사 | 모델 | 비고 |
|---|---|---|
| **신한은행 계열 수탁사** | 거래소+블록체인사+R&D 합작 모델, 시중은행 파트너 | 상장사·재단·일반법인 등 고객 세그먼트별 라인업 |
| **Kodax** | KB국민은행+해시드+해치랩스 | KB금융 산하 |
| **Bestcoin Custody** | 우리은행 등 | |
| **BitGo Korea** | 글로벌 BitGo 한국 | 검토 단계 |
| (자체 운영) | 거래소 자체 수탁 | Upbit, 빗썸 등 |

### 수탁 기술 스택
- **MPC (Multi-Party Computation)**: Fireblocks, Copper, Coinbase Cloud, BitGo
- **HSM (Hardware Security Module)**: Thales, Ledger Enterprise
- **Cold Storage**: 물리적 격리
- **Multi-sig**: BTC 2-of-3, ETH Gnosis Safe

## 6. 거래 모니터링 / Case Management

### 한국 시장
- 대형 거래소는 **자체 구축** 위주
- 소규모는 글로벌 솔루션 + 한국 컨설팅 결합

### 글로벌 솔루션 (한국 도입)
| 회사 | 강점 |
|---|---|
| **NICE Actimize** | 전통 금융 강세, 가상자산 확장 |
| **Solidus Labs** | 시세조종 + AML 결합 |
| **Hummingbird** | Modern UX, US 인기 |
| **Unit21** | API-first, fintech 인기 |
| **Featurespace** | ML 기반 |

## 7. 컨설팅 / 자문

### 법무법인 (가상자산 강세)
- **김·장 법률사무소** — 가상자산 전문 그룹
- **법무법인 광장** — Tech 강세
- **율촌**
- **세종**
- **태평양**
- **화우**

### 컨설팅
- **Big 4** (PwC, EY, Deloitte, KPMG) 한국 — 가상자산 컴플라이언스 자문
- **법무법인 + IT 보안 + 컴플라이언스 컨설팅** 결합 형태

## 8. 정보보안 / ISMS

VASP 신고 시 필수:
- **KISA (한국인터넷진흥원)** — ISMS 인증 발급
- **ISMS-P (개인정보 포함)** — 강화된 인증
- 외부 컨설팅: 안랩, 시큐아이, 이스트시큐리티 등

## 9. 협회 / 자율규제

| 단체 | 역할 |
|---|---|
| **한국블록체인협회** | 가상자산 산업 협회 |
| **DAXA** (디지털자산거래소공동협의체) | 4대 거래소 (업비트, 빗썸, 코빗, 코인원) 자율규제 |
| **한국디지털자산사업자연합회** | 일부 사업자 |

DAXA는 자율적으로 **상장 심사 가이드라인**, **공동 모니터링** 등 운영.

## 10. 인접 분야 — Stablecoin

### 한국 stablecoin 발행 시도
- 2026년 시점 한국 stablecoin 정식 발행은 제한적
- 2단계 입법에서 stablecoin 규율 다룰 예정
- **글로벌 USDT/USDC** 가 한국 거래소에서 활발 거래
- **Tether/Circle** OFAC 협조 시 freeze 영향

## 11. 한국 시장 진입 시 고려사항

```
□ FIU 신고 (특금법) — 3년 갱신
□ ISMS 인증 (KISA)
□ 실명확인 입출금계정 (거래소만, 은행 제휴)
□ Travel Rule 솔루션 가입 (VerifyVASP 또는 CODE)
□ KYT 벤더 선정 (글로벌 4사 + 한국 특화)
□ 본인확인기관 연동 (PASS 등)
□ AML 인력 + AMLO 임명
□ 가상자산이용자보호법 (자산 분리 보관)
□ 거래기록 15년 보존 시스템
□ 외부지갑 등록제 운영
□ 한국어 한국 시간대 24/7 컴플라이언스 인력
```

## 더 읽을거리
- [`analytics_vendors.md`](analytics_vendors.md) — KYT 글로벌 벤더
- [`travel_rule_vendors.md`](travel_rule_vendors.md) — Travel Rule 벤더
- [`../01_regulations/korea_fiu_act.md`](../01_regulations/korea_fiu_act.md) — 특금법
- [`../01_regulations/korea_user_protection.md`](../01_regulations/korea_user_protection.md) — 가상자산이용자보호법
- [DAXA 공식](https://www.daxa.or.kr/)
- [한국블록체인협회](https://www.kblockchain.org/)
- [KISA — ISMS 인증](https://isms.kisa.or.kr/)
