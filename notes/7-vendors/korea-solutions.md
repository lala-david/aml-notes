# 한국 시장 솔루션 지도

> 한국 가상자산 AML **인프라를 만드는 회사들**. 이 글을 읽고 나면 신규 한국 VASP가 "처음부터 무엇을 구매하고 연동해야 하는가"의 지도가 머릿속에 생기고, 한국 특수 인프라(본인확인기관·DAXA·ISMS)를 국내 규제 문맥에서 이해할 수 있게 됩니다. 마지막 업데이트: 2026-04-17.

## TL;DR
- **KYC**: ARGOS Identity, ICONLOOP MyID, NICE·KCB(본인확인기관), Sumsub(글로벌)
- **본인확인**: PASS, 카카오인증, NICE, KCB, KISA 본인확인기관
- **KYT**: Chainalysis, TRM Labs, Elliptic (글로벌 4사 모두 한국 진입)
- **Travel Rule**: VerifyVASP (Upbit계) + CODE (빗썸·코빗·코인원 합작) + Notabene (글로벌)
- **수탁·MPC**: 한국디지털자산수탁 계열(신한은행 파트너), Kodax(KB+해시드+해치랩스), Bestcoin Custody, BitGo Korea(검토 진행)
- **거래 모니터링·Case Management**: 자체 구축 + Solidus Labs·NICE Actimize 일부

---

## 1. 한국 가상자산 산업 지도

### 한눈에 보기

```
[ 거래소 ]                   [ 수탁·Custody ]              [ 분석·솔루션 ]
업비트 (두나무)             신한은행 계열 수탁사             람다256, 블록체인 R&D 다수
빗썸                        Kodax (KB+해시드+해치랩스)       Chainalysis Korea
코빗 (NXC)                  BitGo Korea (검토)              TRM Labs Korea
코인원                      Bestcoin Custody                Elliptic
GOPAX                       (은행 자체 수탁 검토)           ARGOS Identity
한빗코                                                      ICONLOOP
프로비트                                                    오지스 등

[ 본인확인 ]                 [ 위험 데이터 ]                  [ 인프라 ]
PASS (이통3사)              World-Check                     KISA
NICE                        Dow Jones Risk Center           한국인터넷진흥원
KCB                         ComplyAdvantage                 (ISMS 인증)
카카오인증                   외교부 제재명단
```

### 실무 포인트

한국 VASP를 새로 설립할 때 **이 지도의 4개 축(거래소·수탁·분석·본인확인)을 모두 고려**해야 합니다. 하나라도 빠지면 FIU 신고가 안 되거나, 신고 후 검사에서 지적받습니다.

---

## 2. KYC · 본인확인

### 한국 특수: 본인확인기관

한국 「정보통신망법」의 "본인확인기관" 지정 받은 곳:

- **PASS** — SKT·KT·LG U+ 합작 (이통사 본인확인)
- **NICE 평가정보**
- **KCB (Korea Credit Bureau)**
- **금융결제원**
- **카카오인증**

가상자산 거래소가 KYC 시 거의 필수로 사용 (실명 + 휴대폰 + 신분증).

### 왜 본인확인기관이 필수인가

글로벌 KYC 벤더(Sumsub 등)가 아무리 좋아도, **한국 주민등록증의 실명·실주소·실제 본인 여부**를 확인하려면 결국 한국 법에서 지정한 본인확인기관을 거쳐야 합니다. 글로벌 벤더는 신분증 OCR·얼굴 매칭은 해도 **주민번호 실명 조회 권한**이 없기 때문. 실무 구성은 "글로벌 벤더(OCR·Liveness) + 한국 본인확인기관(실명 조회)" 하이브리드.

### KYC SDK·플랫폼

| 회사 | 강점 |
|---|---|
| **ARGOS Identity** | 한국 토종, 가상자산 거래소 다수 사용, 글로벌 KYC 지원 |
| **ICONLOOP (MyID)** | DID 기반, 신한은행 등 |
| **Sumsub** | 글로벌 1위 KYC, 한국 진입 활발 |
| **Onfido** | 글로벌, 일부 한국 사용 |
| **Veriff** | 글로벌 |
| **Jumio** | 글로벌, 신분증 검증 강세 |

### 실무 포인트

한국 거래소들은 대부분 **ARGOS Identity를 메인**으로 쓰고, 글로벌 고객 대응이 필요한 경우에만 Sumsub을 보조로 씁니다. ARGOS가 한국 주민등록증·운전면허증·외국인등록증 처리를 가장 안정적으로 하고, 한국 시간대 지원도 강점.

---

## 3. KYT · Blockchain Analytics (한국 진입)

### 글로벌 4사 모두 진입

- **Chainalysis** — 한국 사무소, 람다256과 합작 (VerifyVASP)
- **TRM Labs** — 한국 영업 활발
- **Elliptic** — 한국 진입
- **Crystal Intelligence** — 한국 진입
- **Merkle Science** — 한국 일부

### 한국 자체

글로벌 attribution을 따라가기 어려워 **토종 KYT 회사는 적음**. 일부 블록체인 R&D 회사가 자체 분석 모듈 보유.

### 실무 포인트

한국 고유 특성상 **한국 중소 거래소·불법 사이트 attribution** 은 글로벌 벤더가 약한 영역. 대형 거래소들은 Chainalysis·TRM에 **한국 특화 라벨 DB를 자체 구축**해서 결합 사용합니다. 이 자체 DB를 만들어가는 것도 몇 년씩 걸리는 작업.

---

## 4. Travel Rule — 양강 구도

### 시장 구조

| 솔루션 | 회원사 | 운영자 |
|---|---|---|
| **VerifyVASP** | Upbit + 글로벌 다수 | 람다256 (두나무) + Chainalysis |
| **CODE** | 빗썸, 코빗, 코인원 | 코드 (3사 합작법인) |

### 두 솔루션 연동

2022-03-25 시행 직후 **분리 상태** → 이용자 민원 폭주 → 1개월 후 연동 완료. 현재 4대 거래소 간 자유 송금 가능.

### 글로벌 호환

- Notabene Gateway 사용 시 글로벌 1,500+ VASP 호환
- VerifyVASP 자체도 글로벌 회원사 다수

### 실무 포인트

신규 VASP에게 가장 흔한 선택 문제는 **VerifyVASP vs CODE vs Notabene**. 한국 고객 중심이면 VerifyVASP·CODE 중 하나, 글로벌 고객 있으면 Notabene 추가. "셋 다 가입"은 운영 부담이 크므로 실제로는 드뭅니다.

---

## 5. 수탁 (Custody)

| 회사 | 모델 | 비고 |
|---|---|---|
| **신한은행 계열 수탁사** | 거래소·블록체인사·R&D 합작 모델, 시중은행 파트너 | 상장사·재단·일반법인 등 고객 세그먼트별 라인업 |
| **Kodax** | KB국민은행 + 해시드 + 해치랩스 | KB금융 산하 |
| **Bestcoin Custody** | 우리은행 등 | |
| **BitGo Korea** | 글로벌 BitGo 한국 | 검토 단계 |
| (자체 운영) | 거래소 자체 수탁 | Upbit, 빗썸 등 |

### 수탁 기술 스택

- **MPC (Multi-Party Computation)**: Fireblocks, Copper, Coinbase Cloud, BitGo
- **HSM (Hardware Security Module)**: Thales, Ledger Enterprise
- **Cold Storage**: 물리적 격리
- **Multi-sig**: BTC 2-of-3, ETH Gnosis Safe

### 실무 포인트

2024-07 가상자산이용자보호법 시행 이후 한국 수탁업 시장이 **은행계열 + 블록체인 R&D 합작** 형태로 빠르게 재편됐습니다. 순수 테크 스타트업으로는 규제 대응 비용이 커서, **시중은행이 돈을 대고 블록체인 R&D가 기술을 대는** 조합이 주류가 됐습니다.

---

## 6. 거래 모니터링·Case Management

### 한국 시장 현실

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

### 실무 포인트

Case Management 도구는 **분석가 생산성을 3배까지 바꾸는** 영역. 한국 거래소들은 자체 구축을 택하는 경우가 많은데, 이는 **자사 데이터 포맷·KYC 필드와 긴밀한 통합**이 필요하기 때문. 다만 소규모 VASP는 글로벌 Unit21·Hummingbird를 쓰면 출발 속도가 훨씬 빠릅니다.

---

## 7. 컨설팅·자문

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

### 실무 포인트

한국 가상자산 규제는 법령·시행령·감독규정·가이드라인이 4층 구조로 복잡해서 **법무법인 자문이 필수**입니다. 특히 FIU 신고 준비·Travel Rule 개인정보 보호·2단계 입법 대응은 내부 법무만으로 감당하기 어렵고, 외부 대형 법무법인과의 정기 자문 계약이 표준.

---

## 8. 정보보안·ISMS

VASP 신고 시 필수:

- **KISA (한국인터넷진흥원)** — ISMS 인증 발급
- **ISMS-P (개인정보 포함)** — 강화된 인증
- 외부 컨설팅: 안랩, 시큐아이, 이스트시큐리티 등

### 실무 포인트

ISMS 인증 준비는 평균 **6개월~1년** 걸리는 대형 프로젝트입니다. VASP 신고를 계획한다면 **ISMS 인증 취득을 가장 먼저 시작**해야 하고, 이 기간이 사실상 신고 시점을 결정합니다.

---

## 9. 협회·자율규제

| 단체 | 역할 |
|---|---|
| **한국블록체인협회** | 가상자산 산업 협회 |
| **DAXA (디지털자산거래소공동협의체)** | 4대 거래소(업비트·빗썸·코빗·코인원) 자율규제 |
| **한국디지털자산사업자연합회** | 일부 사업자 |

DAXA는 자율적으로 **상장 심사 가이드라인**, **공동 모니터링** 등 운영.

### 실무 포인트

DAXA 기준은 법적 강제력은 없지만 **사실상 산업 표준**입니다. 신규 프로젝트가 한국 상장을 준비할 때 DAXA 기준을 맞추는 게 1차 관문이고, 이 기준 미달이면 4대 거래소 어디에도 상장이 어렵습니다.

---

## 10. 인접 분야 — Stablecoin

### 한국 stablecoin 발행 시도

- 2026년 시점 한국 stablecoin 정식 발행은 제한적
- 2단계 입법에서 stablecoin 규율 다룰 예정
- **글로벌 USDT·USDC**가 한국 거래소에서 활발 거래
- **Tether·Circle**의 OFAC 협조 시 freeze 영향

### 실무 포인트

한국 원화 기반 stablecoin은 규제 공백 상태로 2026년 현재까지 정식 출시가 안 됐습니다. 2단계 입법이 통과되면 **은행·보험사 주도의 stablecoin 발행**이 가능해질 것으로 예상되며, 이는 가상자산 업계의 판도를 크게 바꿀 수 있는 변수.

---

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
□ 한국어 + 한국 시간대 24/7 컴플라이언스 인력
```

## 더 읽을거리
- [`analytics-vendors.md`](analytics-vendors.md) — KYT 글로벌 벤더
- [`travel-rule-vendors.md`](travel-rule-vendors.md) — Travel Rule 벤더
- [`../2-regulations/korea-fiu-act.md`](../2-regulations/korea-fiu-act.md) — 특금법
- [`../2-regulations/korea-user-protection.md`](../2-regulations/korea-user-protection.md) — 가상자산이용자보호법
- [DAXA 공식](https://www.daxa.or.kr/)
- [한국블록체인협회](https://www.kblockchain.org/)
- [KISA — ISMS 인증](https://isms.kisa.or.kr/)
