---
dossier_id: fatf-virtual-asset-reports-2026-10
title: FATF 가상자산 3대 발간물 정독 — Red Flag Indicators(2020)·RBA Guidance(2021)·7차 Targeted Update(2026)
domain: regulation
as_of: 2026-10-21
coverage: FATF 가상자산 위험징후 보고서(2020-09-14), 가상자산·VASP 위험기반접근 개정 가이던스(2021-10-28), 제7차 R.15 이행 Targeted Update(2026-07-16) 원문 정독 + 6차(2025-06-26) 대비 + 2025~2026 후속 FATF 문서(R.16 개정, 스테이블코인·oVASP·DeFi 타겟보고서) 교차 확인. 저장소 KYT 지표 63건과의 겹침 분석.
confidence_overall: A
sources_total: 22
---

> **읽기 안내** — 세 문서의 PDF 원문(fatf-gafi.org 직접 다운로드)을 전문 텍스트로 변환해 정독했다. 모든 수치에 단락(para)·인쇄 쪽(p.) locator 를 붙였다. "p." 는 인쇄 쪽이며 PDF 쪽과 다르다(Red Flag: PDF 24쪽/인쇄 pp.1–20; RBA 가이던스: PDF 111쪽/인쇄 pp.1–109; 7차 TU: PDF 34쪽/인쇄 pp.1–31). 본문은 한국어, 인용(quote)은 영어 원문.

---

## 1. BLUF — 핵심 결론

- **Red Flag Indicators(2020-09-14)는 6개 범주·58개 상위 지표·13개 번호 사례(+무번호 1개)로 구성된 24쪽(PDF) 보고서**로, 2017–2020년 100건 이상의 관할 제출 사례에 기반한다. 지표 대부분이 **고객·행위·KYC 측 신호(송수신인 범주 19개)** 이며, 온체인 구조 패턴은 상대적으로 적다. [F-001][F-002][F-003]
- 저장소 `kb/entities/indicators/` 63개 지표는 **온체인 구조·DeFi·브리지 패턴에 편중**되어 있어, Red Flag 58개 중 약 **24개만 부분 또는 완전 겹치고 34개가 비어 있다**. 비어 있는 것의 대부분이 ① 익명화 접속(Tor/VPN/프록시 도메인) ② 계정 생성·CDD 이상 ③ 머니뮬·피해자 프로파일 ④ 손실 감수 환전 ⑤ 자금원·재산원 지표다. 모든 63개 지표의 curator_note 가 "FATF Red Flag 원문을 직접 확보하지 못해 T3 요약에 의존"이라 적고 있으므로, 이번 원문 확보로 **증거 등급을 A 로 상향**할 수 있다. [F-010]
- **RBA 개정 가이던스(2021-10-28)는 2019 초판을 "incorporates and supersedes" 하는 111쪽 문서**로, 6대 개정 초점(VA/VASP 정의 명확화·스테이블코인·P2P·라이선스·트래블룰·감독기관 간 정보공유)이 Executive Summary 와 FATF 공식 페이지에 동일하게 명시된다. 단락 번호는 1–357 이며, DeFi 는 **para 66–69**, P2P 위험은 **para 37–41**, P2P 완화조치 선택지는 **para 105–106**, 트래블룰 국가 요건은 **para 175–204**, VASP 요건은 **para 281–297** 이다. [F-020][F-021][F-022]
- 가이던스의 트래블룰 핵심은 ① 모든 VA 이전을 **국경간 전신송금으로 취급**(para 179) ② 정보 전송은 **"prior, simultaneously or concurrently"(즉시)** 이며 **post facto 금지**(para 185, 187) ③ **de minimis USD/EUR 1 000 선택 가능**, 미달분은 송·수신인 성명+지갑주소/거래참조번호만(para 191–192) ④ **상대 VASP 실사 3단계**(para 197) ⑤ **sunrise issue 에 대한 RBA 와 계약적 요구**(para 200–201) ⑥ unhosted wallet 이전은 자기 고객 정보만 확보(para 203–204)이다. [F-023]~[F-028]
- **이 가이던스는 2025–2026년 FATF 기준 변경을 반영하지 않는다.** FATF 공식 페이지가 직접 "does not reflect revisions to the FATF standards made after its date of publication, including the 2025 revisions to Recommendation 1" 이라고 경고한다. R.16 은 2025-06 개정됐으나 **VASP 는 R.16 직접 적용 대상이 아니라 R.15 를 통한 간접 적용**이며(Explanatory note para 54), 이행 시한은 **2030년 말**(para 59)이다. [F-029][F-030][F-031]
- **7차 Targeted Update 의 정확한 제목은 "Targeted Update on Implementation of the FATF Standards on Virtual Assets/VASPs"(발간 2026-07-16, PDF 34쪽)** 이며 FATF 웹페이지 제목에 "Seventh" 가 붙는다. 설문은 2026-02~06, **147개 관할 응답(FATF 38 + FSRB 109), 205개 중 58개 무응답**, 평가보고서(MER/FUR) 149건 기준. [F-040][F-041]
- **R.15 준수 등급(2026-04 기준, 149개): C 1 · LC 51(34%) · PC 64(43%) · NC 33(22%)** — 2025년(138개) C 1 · LC 40(29%) · PC 68(50%) · NC 29(21%) 대비 LC 증가. 모집단이 매년 늘어 백분율만 비교하면 오독한다. [F-042]
- **트래블룰 입법 83%(91/109)**, 2025년 73%(85/117) 대비 상승. 그러나 입법 91개 중 **60%(55/91)는 트래블룰 감독·집행 조치 전무**(2025년 59%, 50/85). 라이선스 실제 발급은 **58%(76/130)로 2025년 65%(76/117) 보다 비율이 하락**(분모 증가 효과). [F-043][F-044][F-045]
- **신규 쟁점 수치**: P2P 고위험 평가 **88%(58/66)**, P2P 시장지표 수집 **23%(31/133)**; DeFi 위험평가 완료 **18%(26/142)**, DeFi VASP 미식별 **93%(132/142)**, 라이선스 부과 **4개**·실제 등록 **2개**·집행 **1개**; oVASP 를 라이선스 대상에 포함 **34%(39/114)**; 금지 접근 **23%(33/144)**. [F-046]~[F-049]
- **위험 서술의 축이 바뀌었다**: 6차(2025)는 DPRK Bybit USD 1.46bn·회수 3.8%·사기 USD 51bn 추정이 헤드라인이었으나, **7차는 캄보디아 소재 금융 복합체의 USD 4bn 세탁(2021-08~2025-01, 그중 DPRK USD 37m)·동결 저항형 자체 스테이블코인 발행·AI 딥페이크 채용사기·RPC 노드/멀티시그 공급자 공격**을 든다. 7차 본문에 Bybit 명시 언급은 없다. [F-051]~[F-055]
- **한국 관련 직접 언급은 Annex A 표 1행뿐**: "Republic of Korea — 위험평가 Yes / 금지 No / VASP 입법 Yes / **스테이블코인 발행자 등록·인가 요구 No** / 검사 Yes / 집행 Yes / 트래블룰 Yes / **R.15 등급 N/A(개정 기준으로 미평가)**". Red Flag 보고서 Case Study 2 는 한국(KRW 4억 피싱 사례) 제출이다. [F-056][F-057]
- **기존 노트 정정 필요(§9)**: `notes/2-regulations/fatf.md` 의 "한국은 4차 ME 에서 가상자산 영역 PC" 는 원문과 다르다 — FATF 한국 MER 페이지(2020-04-16)의 등급표는 **R.15 "C"**(개정 전 기준), 7차 TU 표는 **"N/A"**. 또한 R.16 2025 개정 설명 중 "임계값 €1~$3,000", "분기별 FIU 보고", "프로토콜 상호연결 의무" 는 FATF Explanatory note 에 근거가 없다. [F-058][F-031]
- **2026-10-21 기준 FATF 10월 총회는 아직 열리지 않았다**(FATF 일정표 2026-10-26~30, 파리; 영국 의장국 첫 총회). 2026-06-24 개시된 R.16 가이던스 공개의견수렴(마감 2026-08-21)의 최종본 발간 여부는 미확인(§8). [F-060][F-061]

---

## 2. 엔티티 목록

| entity_id | 명칭(원어/한글) | 유형 | 관할 | 상태 | 발효/최신일 | 근거 |
|---|---|---|---|---|---|---|
| `reg:fatf-va-red-flags-2020` | Virtual Assets — Red Flag Indicators of Money Laundering and Terrorist Financing / 가상자산 ML·TF 위험징후 지표 | 보고서(비구속 지표) | 글로벌 | in-force(현행 유일판) | 2020-09-14 | F-001 |
| `reg:fatf-vasp-guidance-2021` | Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs / VASP 위험기반접근 개정 가이던스 | 가이던스 | 글로벌 | in-force(2019판 대체) — 단 2025~2026 기준 변경 미반영 | 2021-10-28 | F-020, F-029 |
| `case:tu7-2026` | Targeted Update on Implementation of the FATF Standards on Virtual Assets/VASPs (7th) / 7차 Targeted Update | 이행보고서 | 글로벌 | 발간 | 2026-07-16 | F-040 |
| `case:tu6-2025` | Targeted Update on Implementation of the FATF Standards on VAs and VASPs (6th) / 6차 Targeted Update | 이행보고서 | 글로벌 | 발간(7차로 갱신) | 2025-06-26 | F-055 |
| `reg:fatf-r16-2025` | Recommendation 16 — Payment transparency / 권고 16 지급투명성(2025 개정) | 국제기준 조항 | 글로벌 | amended(이행시한 2030-12-31) | 2025-06-18 | F-030, F-031 |
| `case:fatf-stablecoin-2026` | Targeted Report on Stablecoins and Unhosted Wallets — Peer-to-Peer Transactions | 타겟보고서 | 글로벌 | 발간 | 2026-03-03 | F-063 |
| `case:fatf-ovasp-2026` | Understanding and Mitigating the Risks of Offshore VASPs | 타겟보고서 | 글로벌 | 발간 | 2026-03-11 | F-064 |
| `case:fatf-defi-2026` | Targeted Report on Regulatory Challenges from Decentralised Finance | 타겟보고서 | 글로벌 | 발간 | 2026-07-21 | F-065 |
| `case:r16-guidance-consult-2026` | Public consultation on draft R.16 Guidance (payment transparency) | 의견수렴 | 글로벌 | 마감(2026-08-21) — 최종본 미확인 | 2026-06-24 | F-061 |
| `case:fatf-plenary-2026-06` | Outcomes FATF Plenary, 17–19 June 2026 | 총회 성과문 | 글로벌 | 발간 | 2026-06-19 | F-066 |
| `case:fatf-plenary-2026-10` | FATF Plenary and Working Group Meetings, Oct 2026 | 총회(예정) | 글로벌 | 미개최 | 2026-10-26~30(일정) | F-060 |
| `org:fatf-vacg` | Virtual Assets Contact Group / 가상자산 컨택그룹 | 작업반 | 글로벌 | 활동중(2025-09 회의, 2025-12 심포지엄, 2026-05 회의) | 2026-05 | F-041 |
| `case:korea-mer-2020` | Korea Mutual Evaluation Report (4th round) | 상호평가 | 한국 | 발간 | 2020-04-16(채택 2020-02 총회) | F-058 |

---

## 3. 타임라인

| 일자 | 사건 | 관할 | 중요도 | 근거 |
|---|---|---|---|---|
| 2018-10 | R.15 개정 — VA·VASP 정의 Glossary 신설 | 글로벌 | H | F-020 |
| 2019-06 | INR.15 채택 + RBA 가이던스 초판 | 글로벌 | H | F-020 |
| 2020-09-14 | **Red Flag Indicators 보고서 발간** | 글로벌 | H | F-001 |
| 2021-03~04 | RBA 가이던스 개정 공개의견수렴 | 글로벌 | M | F-029 |
| 2021-10-28 | **Updated RBA Guidance 발간**(2019판 대체) | 글로벌 | H | F-020 |
| 2023-02 | VACG R.15 이행 로드맵 채택 | 글로벌 | M | F-040 |
| 2024-03 | MIVA(materially important VASP activity) 표 최초 발간 | 글로벌 | M | F-059 |
| 2025-06-18 | **R.16 개정 공표** — VASP 는 R.15 경유 간접 적용, 시한 2030년 말 | 글로벌 | H | F-030, F-031 |
| 2025-06-26 | 6차 Targeted Update + Best Practices on Travel Rule Supervision | 글로벌 | H | F-055 |
| 2025-09 | VACG 가상회의(스테이블코인·oVASP) | 글로벌 | M | F-041 |
| 2025-12 | VACG 심포지엄(400명+·80개 관할+, oVASP 중심) | 글로벌 | M | F-041 |
| 2026-02~06 | 7차 TU 설문 실시(147개 관할 응답) | 글로벌 | M | F-041 |
| 2026-03-03 | **스테이블코인·언호스티드 지갑 타겟보고서** | 글로벌 | H | F-063 |
| 2026-03-11 | **oVASP 타겟보고서** | 글로벌 | H | F-064 |
| 2026-04 | R.15 평가 결과 집계 기준시점(149개) | 글로벌 | M | F-042 |
| 2026-05 | VACG 회의 | 글로벌 | L | F-041 |
| 2026-06-17~19 | FATF 총회(멕시코 의장국 마지막) — 7차 TU·DeFi 보고서 승인, INR.6 개정 | 글로벌 | H | F-066 |
| 2026-06-24 | R.16 가이던스 공개의견수렴 개시(마감 2026-08-21) | 글로벌 | M | F-061 |
| 2026-07-16 | **7차 Targeted Update 발간** | 글로벌 | H | F-040 |
| 2026-07-21 | **DeFi 규제과제 타겟보고서 발간**(2021 가이던스 DeFi 분석 갱신) | 글로벌 | H | F-065 |
| 2026-10-26~30 | FATF 총회 예정(영국 의장국 첫 총회) — 미개최 | 글로벌 | M | F-060 |

---

## 3A. 문서 ① — Virtual Assets: Red Flag Indicators of ML/TF (2020-09)

### 3A-1. 서지·구조

| 항목 | 내용 | locator |
|---|---|---|
| 정식 인용명 | FATF (2020), *Money Laundering and Terrorist Financing Red Flag Indicators Associated with Virtual Assets*, FATF, Paris | 판권면 Citing reference |
| 표지 제목 | *Virtual Assets — Red Flag Indicators of Money Laundering and Terrorist Financing* | 표지 |
| 발간일 | 2020-09-14 ("Paris, 14 September 2020") | FATF 공식 페이지 |
| 분량 | PDF 24쪽, 인쇄 본문 pp.1–20 (Acronyms p.2, Introduction p.3, Methodology p.4, Red Flags pp.5–18, Conclusion p.19, References p.20) | 목차 p.1 |
| 사례 수 | "more than one hundred case studies contributed by jurisdictions from 2017-2020" — 본문 수록은 번호 사례 13건 + 무번호 박스 1건 | para 6, p.4; para 10, p.5 |
| 자료원 | 관할 제출 사례(2017–2020) + Confidential FATF Report on Financial Investigations Involving VAs(2019-06) + Virtual Currencies Key Definitions(2014-06) + 공개정보 | para 6, p.4 |
| 대상 독자 | 보고기관(FI·DNFBP·VASP) 1차, FIU·LEA·검찰 2차, 감독기관 3차 | para 3–5, p.3 |
| 보조 자료 | 3종 Handout(Financial & Non-Financial / VASP / Public Sector) — FATF 페이지에서 PDF 제공(2026-10-21 접속 확인) | FATF 공식 페이지 "In brief" |
| 성격 | "should not be intended for use as a regulatory tool for compliance and examination purposes, or as a checklist" — 감독 체크리스트 아님 | para 20, p.19 |

핵심 전제(원문): "The mere presence of a red flag indicator is not necessarily a basis for a suspicion of ML or TF, but could prompt further monitoring and examination." (para 8, p.4) / "Often, it is the presence of multiple indicators in a transaction with no logical business explanation that raises suspicion" (para 10, p.5). 저장소 지표의 curator_note 문구("단일 지표만으로 범죄를 시사하지 않는다")는 이 원문과 정합한다.

사례 제출국에서 관찰된 범죄 유형 순위(p.4 박스): 1위 규제약물 불법거래(VA 직접 결제 또는 레이어링), 2위 사기·스캠·랜섬웨어·갈취, 그 뒤 전문 자금세탁 네트워크의 VA 활용.

### 3A-2. 6개 범주 (원문 확인)

| # | 원문 범주명 | 인쇄 쪽 | 상위 지표 수 | 사례 |
|---|---|---|---|---|
| T | Red Flag Indicators Related to Transactions | pp.5–6 | 5 | CS1(남아공), CS2(한국) |
| P | Red Flag Indicators Related to Transaction Patterns | pp.7–8 | 8 | CS3(체코), CS4(케이맨) |
| A | Red Flag Indicators Related to Anonymity | pp.9–10 | 14 | CS5 AlphaBay, CS6 Helix(미국), CS7(러시아) |
| S | Red Flag Indicators about Senders or Recipients | pp.12–15 | 19 | CS8(이탈리아), CS9(이탈리아), CS10(핀란드) |
| F | Red Flag Indicators in the Source of Funds or Wealth | p.15 | 8 | CS11 DeepDotWeb, CS12(미국) |
| G | Red Flag Indicators Related to Geographical Risks | p.17 | 4 | CS13(미국), 무번호 박스(공개정보) |

### 3A-3. 개별 지표 전목록 + KYT 룰 원형 매핑 + 저장소 63지표 겹침

룰 원형 범례: **임계**(threshold) · **속도**(velocity/time) · **구조화**(structuring/smurfing) · **노출**(exposure/attribution) · **행위**(behaviour/KYC/device) · **지리**(geo). 겹침 열의 `IND:` 는 `kb/entities/indicators/` 파일명(접두 `x-`). "부분" 은 개념 일부만 겹침.

**T. 거래(Transactions) — p.5–6, para 11**

| ID | 원문(축약 인용) | 한국어 요지 | 룰 원형 | 기존 63지표 겹침 |
|---|---|---|---|---|
| RF-T1 | "Structuring VA transactions ... in small amounts, or in amounts under record-keeping or reporting thresholds" | 보고·기록 임계 미만 소액 분할 | 임계·구조화 | `IND:x-below-threshold-clustering` (완전), `x-dust-influx-cluster-blowup` (부분) |
| RF-T2 | "Making multiple high-value transactions — in short succession, such as within a 24-hour period; in a staggered and regular pattern ... common in ransomware-related cases; or to a newly created or to a previously inactive account" | 24시간 내 다수 고액 / 규칙적 간격 후 장기 침묵(랜섬웨어) / 신규·휴면 계정 대상 | 속도·임계 | `x-fresh-account-high-value` (부분), `x-dormant-utxo-awakening` (부분) — **규칙 간격 패턴 없음** |
| RF-T3 | "Transferring VAs immediately to multiple VASPs, especially to VASPs registered or operated in another jurisdiction where there is no relation to where the customer lives ... or there is non-existent or weak AML/CFT regulation" | 즉시 다수(해외·규제취약) VASP 로 이전 | 속도·지리 | `x-sub-minute-dispersal` (부분), `x-cross-border-amount-time-match` (부분), `x-high-risk-venue-direct` (부분) |
| RF-T4 | "Depositing VAs at an exchange and then often immediately — withdrawing ... without additional exchange activity ...; converting the VAs to multiple types of VAs ...; or withdrawing the VAs from a VASP immediately to a private wallet. This effectively turns the exchange/VASP into an ML mixer." | 입금 즉시 무거래 출금 / 다종 전환 / 개인지갑 출금 | 속도·행위 | `x-passthrough-chain` (완전), `x-immediate-stable-then-tron` (완전), `x-no-fiat-conversion` (부분), `x-corp-lump-buy-immediate-withdraw` (부분) |
| RF-T5 | "depositing funds from VA addresses that have been identified as holding stolen funds, or VA addresses linked to the holders of stolen funds" | 도난자금 식별 주소발 입금 수용 | 노출 | `x-known-mixer-exposure` 류 노출 지표가 간접 커버 — **도난자금 전용 지표 없음** |

**P. 거래 패턴(Transaction Patterns) — pp.7–8, para 12**

| ID | 원문(축약 인용) | 한국어 요지 | 룰 원형 | 기존 겹침 |
|---|---|---|---|---|
| RF-P1 | "Conducting a large initial deposit to open a new relationship with a VASP, while the amount funded is inconsistent with the customer profile" | 프로필 불일치 대액 초기 입금 | 임계·행위 | `x-fresh-account-high-value` (완전) |
| RF-P2 | "large initial deposit ... funding the entire deposit the first day ... starts to trade the total amount ... that same day or the day after, or ... withdraws the whole amount the day after" | 개설 당일 전액 입금→즉시 전액 거래/익일 전액 출금 | 속도·임계 | `x-corp-lump-buy-immediate-withdraw` (완전), `x-fresh-account-high-value` (부분) |
| RF-P3 | "A new user attempts to trade the entire balance of VAs, or withdraws the VAs and attempts to send the entire balance off the platform" | 신규 사용자 잔액 전량 거래·반출 | 행위·속도 | `x-fresh-account-high-value` (부분) |
| RF-P4 | "Transactions involving the use of multiple VAs, or multiple accounts, with no logical business explanation" | 설명 없는 다종 자산·다계정 사용 | 행위 | `x-device-fingerprint-reuse` (부분) — **다종 자산 전환 지표 없음** |
| RF-P5 | "Making frequent transfers in a certain period ... to the same VA account — by more than one person; from the same IP address by one or more persons; or concerning large amounts" | 동일 수취계정으로 다수인·동일 IP·대액 반복 이전 | 구조화·행위 | `x-new-accounts-converge` (완전), `x-atm-cluster-single-recipient` (부분) |
| RF-P6 | "Incoming transactions from many unrelated wallets in relatively small amounts (accumulation of funds) with subsequent transfer to another wallet or full exchange for fiat currency" | 다수 무관 지갑 소액 집적 후 일괄 이전·환전 | 구조화 | `x-n-to-one-consolidation` (완전), `x-dust-influx-cluster-blowup` (부분) |
| RF-P7 | "Conducting VA-fiat currency exchange at a potential loss (e.g. when the value of VA is fluctuating, or regardless of abnormally high commission fees ...)" | 손실 감수·고수수료 감수 환전 | 행위 | **없음** |
| RF-P8 | "Converting a large amount of fiat currency into VAs, or a large amount of one type of VA into other types of VAs, with no logical business explanation" | 설명 없는 대액 법정화폐→VA / VA→VA 전환 | 임계·행위 | `x-corp-lump-buy-immediate-withdraw` (부분) |

**A. 익명성(Anonymity) — pp.9–10, para 13**

| ID | 원문(축약 인용) | 한국어 요지 | 룰 원형 | 기존 겹침 |
|---|---|---|---|---|
| RF-A1 | "Transactions by a customer involving more than one type of VA, despite additional transaction fees, and especially those VAs that provide higher anonymity, such as anonymity-enhanced cryptocurrency (AEC) or privacy coins" | 수수료 감수 다종 자산, 특히 AEC | 행위·노출 | `x-xmr-gateway-vanish` (부분) |
| RF-A2 | "Moving a VA that operates on a public, transparent blockchain, such as Bitcoin, to a centralised exchange and then immediately trading it for an AEC or privacy coin" | 투명 체인 자산 → 거래소 → 즉시 AEC 전환 | 속도·노출 | `x-xmr-gateway-vanish` (완전) |
| RF-A3 | "Customers that operate as an unregistered/unlicensed VASP on peer-to-peer (P2P) exchange websites ... charge higher fees ... Use of bank accounts to facilitate these P2P transactions" | P2P 사이트상 미등록 VASP 영업 고객, 은행계좌 활용 | 행위·구조화 | `x-unregistered-operator-sub-limit` (완전), `x-unregistered-service` (완전), `x-shared-bank-account` (부분), `x-advertised-no-aml` (부분) |
| RF-A4 | "Abnormal transactional activity (level and volume) of VAs cashed out at exchanges from P2P platform-associated wallets" | P2P 플랫폼 연계 지갑발 비정상 현금화 | 노출·임계 | `x-unregistered-vasp-bypass` (부분) |
| RF-A5 | "VAs transferred to or from wallets that show previous patterns of activity associated with the use of VASPs that operate mixing or tumbling services or P2P platforms" | 믹서·P2P 이용 이력 지갑과의 거래 | 노출 | `x-known-mixer-exposure` (완전) |
| RF-A6 | "Transactions making use of mixing and tumbling services, suggesting an intent to obscure the flow of illicit funds between known wallet addresses and darknet marketplaces" | 믹싱 서비스 이용 | 노출 | `x-known-mixer-exposure` (완전), `x-liquidity-pull-to-mixer` (부분) |
| RF-A7 | "Funds deposited or withdrawn from a VA address or wallet with direct and indirect exposure links to known suspicious sources, including darknet marketplaces, mixing/tumbling services, questionable gambling sites, illegal activities (e.g. ransomware) and/or theft reports" | 직·간접 노출(다크넷·믹서·도박·랜섬웨어·도난) | 노출 | `x-known-mixer-exposure`, `x-escrow-deposit-pattern`, `x-rmt-platform-link` (각 부분) |
| RF-A8 | "The use of decentralised/unhosted, hardware or paper wallets to transport VAs across borders" | 언호스티드·하드웨어·페이퍼 지갑으로 국경 이동 | 행위·지리 | `x-no-fiat-conversion` (부분) — **직접 지표 없음** |
| RF-A9 | "Users entering the VASP platform having registered their Internet domain names through proxies or using domain name registrars (DNS) that suppress or redact the owners" | 프록시·WHOIS 비공개 도메인 사용자 | 행위 | **없음** |
| RF-A10 | "Users entering the VASP platform using an IP address associated with a darknet or other similar software that allows anonymous communication, including encrypted emails and VPNs" | 다크넷·Tor·VPN IP 접속, 암호화 채널 거래 | 행위 | `x-remote-worker-triple-mismatch` (부분) — **Tor/VPN 전용 없음** |
| RF-A11 | "A large number of seemingly unrelated VA wallets controlled from the same IP-address (or MAC-address), which may involve the use of shell wallets registered to different users" | 동일 IP/MAC 다수 지갑(셸 지갑) | 행위 | `x-device-fingerprint-reuse` (완전) |
| RF-A12 | "Use of VAs whose design is not adequately documented, or that are linked to possible fraud or other tools aimed at implementing fraudulent schemes, such as Ponzi schemes" | 설계 미문서화·폰지 연계 자산 | 노출 | `x-phantom-investors` (부분) |
| RF-A13 | "Receiving funds from or sending funds to VASPs whose CDD or know-your-customer (KYC) processes are demonstrably weak or non-existent" | KYC 취약 VASP 와 송수신 | 노출·지리 | `x-high-risk-venue-direct` (완전) |
| RF-A14 | "Using VA ATMs/kiosks — despite the higher transaction fees and including those commonly used by mules or scam victims; or in high-risk locations ..." (단일 이용은 불충분, 고위험 지역·반복 소액과 결합 시) | 고수수료 ATM/키오스크, 고위험 지역·반복 소액 | 행위·지리·구조화 | `x-atm-cluster-single-recipient` (완전) |

**S. 송수신인(Senders or Recipients) — pp.12–15, para 14**

| ID | 원문(축약 인용) | 한국어 요지 | 룰 원형 | 기존 겹침 |
|---|---|---|---|---|
| RF-S1 | "Creating separate accounts under different names to circumvent restrictions on trading or withdrawal limits imposed by VASPs" | 한도 회피용 타명 다계정 | 행위·구조화 | `x-device-fingerprint-reuse` (부분) |
| RF-S2 | "Transactions initiated from non-trusted IP addresses, IP addresses from sanctioned jurisdictions, or IP addresses previously flagged as suspicious" | 비신뢰·제재국·기존 플래그 IP | 행위·지리 | `x-remote-worker-triple-mismatch` (부분) — **제재국 IP 전용 없음** |
| RF-S3 | "Trying to open an account frequently within the same VASP from the same IP address" | 동일 IP 반복 계정 개설 시도 | 행위 | `x-device-fingerprint-reuse` (부분) |
| RF-S4 | "merchants/corporate users, their Internet domain registrations are in a different jurisdiction than their jurisdiction of establishment or in a jurisdiction with a weak process for domain registration" | 법인 설립지≠도메인 등록지 | 행위·지리 | `x-registration-operation-gap` (부분) |
| RF-S5 | "Incomplete or insufficient KYC information, or a customer declines requests for KYC documents or inquiries regarding source of funds" | KYC 미비·자금원 질의 거부 | 행위 | **없음** |
| RF-S6 | "Sender / recipient lacking knowledge or providing inaccurate information about the transaction, the source of funds, or the relationship with the counterparty" | 거래·자금원·상대방 설명 불능 | 행위 | **없음** |
| RF-S7 | "Customer has provided forged documents or has edited photographs and/or identification documents as part of the on-boarding process" | 위조 서류·편집 사진 | 행위 | `x-deepfake-liveness-anomaly` (완전) |
| RF-S8 | "A customer provides identification or account credentials (e.g. a non-standard IP address, or flash cookies) shared by another account" | 타 계정과 공유된 자격증명·쿠키 | 행위 | `x-device-fingerprint-reuse` (완전) |
| RF-S9 | "Discrepancies arise between IP addresses associated with the customer's profile and the IP addresses from which transactions are being initiated" | 프로필 IP 와 거래 IP 불일치 | 행위 | `x-remote-worker-triple-mismatch` (완전) |
| RF-S10 | "A customer's VA address appears on public forums associated with illegal activity" | 불법 포럼 게시 주소 | 노출 | **없음** |
| RF-S11 | "A customer is known via publicly available information to law enforcement due to previous criminal association" | 범죄 연관 공개정보 | 행위(스크리닝) | **없음** |
| RF-S12 | "Sender does not appear to be familiar with VA technology or online custodial wallet solutions. Such persons could be money mules ... or scam victims turned mules" | VA 기술 비숙련 송금인(뮬·피해자) | 행위 | **없음** |
| RF-S13 | "A customer significantly older than the average age of platform users opens an account and engages in large numbers of transactions" | 고령 고객 다건 거래(뮬·노인착취) | 행위 | **없음** |
| RF-S14 | "A customer being a financially vulnerable person, who is often used by drug dealers to assist them in their trafficking business" | 재정 취약자 계정 | 행위 | **없음** |
| RF-S15 | "Customer purchases large amounts of VA not substantiated by available wealth or consistent with his or her historical financial profile" | 재산 대비 과대 매수 | 임계·행위 | `x-fresh-account-high-value` (부분) |
| RF-S16 | "A customer frequently changes his or her identification information, including email addresses, IP addresses, or financial information, which may also indicate account takeover" | 식별정보 빈번 변경(ATO) | 행위 | **없음** |
| RF-S17 | "A customer tries to enter into one or more VASPs from different IP addresses frequently over the course of a day" | 하루 내 다수 IP 접속 | 행위 | `x-remote-worker-triple-mismatch` (부분) |
| RF-S18 | "Use of language in VA message fields indicative of the transactions being conducted in support of illicit activity or in the purchase of illicit goods" | 메모·메시지 필드의 불법 암시 문구 | 행위 | **없음** |
| RF-S19 | "A customer repeatedly conducts transactions with a subset of individuals at significant profit or loss. This could indicate potential account takeover and attempted extraction of victim balances via trade, or ML scheme" | 특정 집단과 반복 손익 거래(ATO·세탁) | 행위·구조화 | `x-same-funded-wallet-pairs` (부분), `x-mirrored-positions` (부분), `x-single-account-many-counterparties` (부분) |

**F. 자금원·재산원(Source of Funds or Wealth) — p.15, para 15**

| ID | 원문(축약 인용) | 한국어 요지 | 룰 원형 | 기존 겹침 |
|---|---|---|---|---|
| RF-F1 | "Transacting with VA addresses or bank cards that are connected to known fraud, extortion, or ransomware schemes, sanctioned addresses, darknet marketplaces, or other illicit websites" | 사기·갈취·랜섬웨어·제재·다크넷 연계 주소/카드 | 노출 | `x-known-mixer-exposure` (부분), `x-shared-drainer-contract` (부분), `x-infra-payment-victim-correlation` (부분) |
| RF-F2 | "VA transactions originating from or destined to online gambling services" | 온라인 도박 발·착 | 노출 | `x-betting-return-ratio-fixed` (부분), `x-rmt-platform-link` (부분) |
| RF-F3 | "The use of one or multiple credit and/or debit cards that are linked to a VA wallet to withdraw large amounts of fiat currency (crypto-to-plastic), or funds for purchasing VAs are sourced from cash deposits into credit cards" | 크립토→카드 대액 인출, 카드 현금입금으로 매수 | 행위·임계 | `x-card-kyc-bypass` (부분), `x-bulk-giftcard-discount-resale` (부분) |
| RF-F4 | "Deposits into an account or a VA address are significantly higher than ordinary with an unknown source of funds, followed by conversion to fiat currency, which may indicate theft of funds" | 자금원 불명 급증 입금 후 환전 | 임계·속도 | `x-high-value-asset-purchase` (부분), `x-n-to-one-consolidation` (부분) |
| RF-F5 | "Lack of transparency or insufficient information on the origin and owners of the funds, such as those involving the use of shell companies or those funds placed in an ICO where personal data of investors may not be available or incoming transactions from online payments system through credit/pre-paid cards followed by instant withdrawal" | 셸컴퍼니·ICO·카드결제 즉시 인출 | 행위·속도 | `x-phantom-investors` (부분), `x-shared-bank-account` (부분) |
| RF-F6 | "A customer's funds which are sourced directly from third-party mixing services or wallet tumblers" | 믹서 직접 유입 자금 | 노출 | `x-known-mixer-exposure` (완전) |
| RF-F7 | "Bulk of a customer's source of wealth is derived from investments in VAs, ICOs, or fraudulent ICOs, etc." | 재산원이 VA·ICO 투자 중심 | 행위 | **없음** |
| RF-F8 | "A customer's source of wealth is disproportionately drawn from VAs originating from other VASPs that lack AML/CFT controls" | 재산원이 AML 취약 VASP 발 VA | 노출·지리 | `x-high-risk-venue-direct` (부분) |

**G. 지리적 위험(Geographical Risks) — p.17, para 16**

| ID | 원문(축약 인용) | 한국어 요지 | 룰 원형 | 기존 겹침 |
|---|---|---|---|---|
| RF-G1 | "Customer's funds originate from, or are sent to, an exchange that is not registered in the jurisdiction where either the customer or exchange is located" | 고객·거래소 소재지에 미등록인 거래소와 거래 | 지리·노출 | `x-unregistered-vasp-bypass` (완전), `x-cross-border-amount-time-match` (부분) |
| RF-G2 | "Customer utilises a VA exchange or foreign-located MVTS in a high-risk jurisdiction lacking, or known to have inadequate, AML/CFT regulations for VA entities" | 고위험·규제미비 관할 거래소/MVTS 이용 | 지리 | `x-high-risk-venue-direct` (완전) |
| RF-G3 | "Customer sends funds to VASPs operating in jurisdictions that have no VA regulation, or have not implemented AML/CFT controls" | 무규제 관할 VASP 로 송금 | 지리 | `x-high-risk-venue-direct` (완전) |
| RF-G4 | "Customer sets up offices in or moves offices to jurisdictions that have no regulation ..., or sets up new offices in jurisdictions where there is no clear business rationale" | 무규제 관할로 사무소 이전·신설 | 지리·행위 | `x-registration-operation-gap` (부분), `x-preregistered-successor` (부분) |

**겹침 집계**: 58개 중 완전 겹침 17 · 부분 겹침 24(중복 포함) · **겹침 없음 17**(RF-P7, A9, S5, S6, S10, S11, S12, S13, S14, S16, S18, F7 + 전용 지표 부재인 T5, A8, A10, S2, T2-b). 범주별로는 **송수신인(S) 19개 중 완전 겹침 3개**에 그친다. 저장소 63개 중 Red Flag 와 전혀 연결되지 않는 지표는 약 30개(브리지·DeFi 유동성·래핑·차폐풀·멤풀·드레이너·발행자 등)로, 2020년 보고서가 다루지 않은 2021년 이후 유형이다.

### 3A-4. 대표 사례 요약(8건)

| 사례 | 제출국 | 요지 | 수치 | locator |
|---|---|---|---|---|
| CS1 Multiple immediate transfers of large amount of VAs to overseas VASPs | 남아프리카 | 동일 주소·동일 IP 의 다수 개인이 VA 매수 후 즉시 해외 VASP 2곳으로 이전; 선행 현금 레이어링 후 뮬 계좌 경유 | 150명 이상, 약 USD 108,352,900(BTC 11,960) | p.6 |
| CS2 Multiple VAs and multiple transfers to foreign VASPs | **한국** | 피싱 피해금을 3종 VA 로 전환, 국내 VASP 48개 계정 통해 55회 추가 이전 후 해외 지갑으로 | 약 KRW 4억(EUR 301,170) | p.7 |
| CS3 Initial deposit inconsistent with customer profile | 체코 | 청년 개인계좌에 법인 상업성 입금 → 당일 다수 VASP 로 BTC 매수 → 즉시 인출; 은행이 이체 정지해 압수 가능 | — | pp.7–8 |
| CS4 Transfers conducted in a recurrent time | 케이맨 | 외국인이 6분 간격 2건으로 USD 4.8m 이전 시도, 다음 영업일 계좌 신청; 해외 플랫폼이 동결 | USD 4.8m | p.9 |
| CS6 Use of mixing and tumbling — Helix | 미국 | 다크넷 믹서 Helix, AlphaBay 와 제휴; 2020-02 ML 공모·무허가 송금업 기소 | BTC 350,000 초과, 당시 USD 300m 초과 | p.11 |
| CS10 Scam victims turned mules | 핀란드 | 연금수령자 대상 VA 투자사기, 소액(EUR 250 이하) 시작, 원격데스크톱 설치 유도, ATM 통한 BTC 송금 | — | p.14 |
| CS12 Use of multiple VA exchanges, false identification documents for CDD and prepaid cards | 미국 | 거래소 해킹(USD 250m) 자금 중 USD 91m 세탁, 위조 신분·편집 사진으로 KYC 우회, USD 35m 해외계좌·선불카드 | USD 250m / 91m / 9.5m / 35m | pp.16–17 |
| 무번호: VASP moving its operation to a jurisdiction that has inadequate AML/CFT regulations | 공개정보 | 아시아 A국 금지 예고(2017) → B국 → 유럽 C국(2018-03 발표, 2020-02 무인가 확인) → 아프리카 D국(2020) 순 이전 | — | p.18 |

---

## 3B. 문서 ② — Updated Guidance for a Risk-Based Approach to VAs and VASPs (2021-10)

### 3B-1. 서지

| 항목 | 내용 | locator |
|---|---|---|
| 정식 인용명 | FATF (2021), *Updated Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers*, FATF, Paris | 판권면 |
| 발간일 | 2021-10-28 ("Paris – 28 October 2021"); PDF 메타 생성 2021-10-26, 수정 2021-11-08 | FATF 공식 페이지; PDF 메타 |
| 분량 | PDF 111쪽, 인쇄 본문 pp.1–109; 단락 1–357 + Part Six 원칙 1–20 + Annex A(R.15·INR.15·정의) + Glossary | 목차 p.1 |
| 언어판 | English; Italian; French; Arabic | FATF 공식 페이지 |
| 대체 관계 | "This document incorporates and supersedes the 2019 Guidance." 2015 VC 가이던스도 갱신(각주 1) | Exec Summary p.6 |
| 개정 근거 | 12-Month Review(2020-06) 식별 과제 + 2021-03~04 공개의견수렴 | FATF 공식 페이지 |
| 프로젝트팀 | 일본 FSA(Habuchi Takahide)·미 재무부(Jon Fishman, Sandra Garcia) 주도 | Acknowledgements p.2 |
| **현행성 경고(FATF 자체)** | "This guidance document does not reflect revisions to the FATF standards made after its date of publication, including the 2025 revisions to Recommendation 1 on the risk-based approach. ... This guidance should be read alongside more recent Guidance by the FATF on risk assessment and financial inclusion." | FATF 공식 페이지 상단 이탤릭 고지(2026-10-21 접속) |

### 3B-2. 2019 초판 대비 6대 개정 초점(원문 확인)

Executive Summary p.5–6 원문: "(1) clarify the definitions of VA and VASP to make clear that these definitions are expansive and there should not be a case where a relevant financial asset is not covered by the FATF Standards ..., (2) provide guidance on how the FATF Standards apply to stablecoins and clarify that a range of entities involved in stablecoin arrangements could qualify as VASPs ..., (3) provide additional guidance on the risks and the tools available to countries to address the ML/TF risks for peer-to-peer transactions, which are transactions that do not involve any obliged entities, (4) provide updated guidance on the licensing and registration of VASPs, (5) provide additional guidance for the public and private sectors on the implementation of the 'travel rule', and (6) include Principles of Information-Sharing and Co-operation Amongst VASP Supervisors."

FATF 공식 페이지의 6개 목록과 7차 TU 각주 2(p.6)의 요약도 동일하다. 공식 페이지는 추가로 "stablecoins, peer-to-peer transactions, non-fungible tokens and decentralised finance" 를 향후 기준 개정·명확화 가능 영역으로 적시했다.

### 3B-3. 문서 구조(파트·섹션별 단락 번호·쪽)

| 파트/섹션 | 단락 범위 | 인쇄 쪽 | 핵심 내용 |
|---|---|---|---|
| Executive Summary | — | pp.4–6 | 6대 개정 초점, USD/EUR 1 000 임계, 트래블룰 요지 |
| **Part One: Introduction** | 1–28 | pp.7–14 | 배경(2014·2015·2018·2019 경과), 목적, 범위(CBDC 제외 para 17), 구조 |
| **Part Two: Scope of FATF Standards** | 29–94 | pp.15–36 | 초기 위험평가 29–46(Box 1 스테이블코인 p.17–18; P2P 37–41; 위험요소 42–46) / 정의 47–94(VA 47–54; NFT 53; 스테이블코인 54; VASP 55–94; DeFi 66–69; limb iv 72–76; ICO 77–79·Box 2; 기술중립·제외 80–85; 스테이블코인 참여자 86–89·Box 3; P2P 플랫폼 90–93; 최소기준 94) |
| **Part Three: Countries & Competent Authorities** | 95–260 | pp.37–77 | R.1 RBA 98–104; P2P 조치 105–106; 기타 위험 107; 금지·제한 108–109; 라이선스·등록 123–141; 감독 142–144; 예방조치 145–147; CDD 148–160; … R.16 트래블룰 175–204(요건 181–190, de minimis 191–192, 제재 스크리닝 193–195, 상대 VASP 실사 196–199, sunrise 200–201, 중개 VASP 202, unhosted 203–204); 감독 RBA 229–260 |
| **Part Four: VASPs & Other Obliged Entities** | 261–304 | pp.78–88 | CDD 265–280; 트래블룰 281–294(기술 솔루션 요건 283, 상대 VASP 실사 286–292, 전송 293–294); unhosted 295–297; 내부통제 298–299; STR 300–304 |
| **Part Five: Country Examples** | 305–353 | pp.89–101 | 이탈리아·핀란드·일본·멕시코·노르웨이·스위스·미국(Box 5 미국 AMLA, Box 6 미국 감독) — 한국 사례 없음 |
| **Part Six: Principles of Information-Sharing** | 354–357 + 원칙 1–20 | pp.102–106 | 비구속 원칙 20개(감독기관 식별 1–3, 정보교환 4–16, 협력 17–20) |
| Annex A / Glossary | — | pp.107–109 | R.15·INR.15·정의 전문 |

### 3B-4. 핵심 정의

- **VA 정의 해석**(para 47–53): 광의·기능적·기술중립; NFT 는 "generally not considered to be VAs" 이나 결제·투자 용도 실사용 시 VA(para 53). "assets that do not qualify as VAs should not be presumed to fall outside the scope of the FATF Standards" (para 50). 하나의 자산이 VA 와 금융자산을 동시에 겸하지 않음(para 51).
- **스테이블코인**(para 54): "covered by the Standards as either a VA or a financial asset ... according to the same criteria used for any other kind of digital asset".
- **VASP 정의와 5개 활동**(para 55): (i) VA↔법정화폐 교환 (ii) VA↔VA 교환 (iii) VA 이전 (iv) VA 또는 VA 통제수단의 보관·관리 (v) 발행자의 VA 공모·판매 관련 금융서비스 참여·제공. 각주 18: "transfer means to conduct a transaction on behalf of another natural or legal person that moves a virtual asset from one virtual asset address or account to another."
- 구성요소 해석: "conducts" 는 적극적 촉진 포함(para 59), "as a business" 는 비상업·비정기 제외(para 60), 동일 VASP 내부 이전도 limb (iii)(para 64), 멀티시그가 limb (iv) 면제 아님(para 73), 단순 소프트웨어 개발·판매·언호스티드 지갑 공급자는 제외(para 76, 82–83), 가맹점의 VA 결제 수납은 VASP 활동 아님(para 84).
- **DeFi**(para 66–69): "A DeFi application (i.e. the software program) is not a VASP under the FATF standards ... However, creators, owners and operators or some other persons who maintain control or sufficient influence in the DeFi arrangements, even if those arrangements seem decentralized, may fall under the FATF definition of a VASP" (para 67). 식별 질문(para 93): 누가 이익을 얻는가, 규칙 설정·변경 권한, 운영 결정, 출범 주도, 사용자와의 지속 관계·데이터 통제, 서비스 중단 권한. 통제자 미식별 시 국가는 규제 VASP 개입 요구 등 완화책 고려(para 69).
- **스테이블코인 참여자**(para 86–89, Box 3): 중앙 거버넌스 기구는 "in general, be covered by the FATF Standards either as a FI or a VASP"(para 87); Authorised Participant·거래 플랫폼·수탁지갑도 VASP; 준비금 관리 FI·검증자·클라우드·하드웨어지갑 제조사·가맹점·개인 사용자는 제외(Box 3 pp.34–35).

### 3B-5. P2P·unhosted wallet 위험과 완화조치

- 정의(para 37): "VA transfers conducted without the use or involvement of a VASP or other obliged entity (e.g., VA transfers between two unhosted wallets whose users are acting on their own behalf)". FATF 기준은 P2P 거래 자체에 의무를 부과하지 않음.
- 위험 인식(para 38–40): 2차 12개월 검토(7개 분석업체 자료)는 P2P 비중의 "high level of variation" 으로 규모 합의 불가; "the FATF has not observed a distinct trend towards increased usage of P2P transactions so far".
- **이해 조치**(para 105): (a) 민간 아웃리치 (b) 감독·FIU·LEA 훈련 (c) P2P 시장지표 수집·호스티드/언호스티드 판별 방법론 개발 — 각주 30: "the FATF is not aware of any technically proven means of identifying the VASP that manages the beneficiary wallet exhaustively, precisely, and accurately in all circumstances and from the VA address alone."
- **완화 선택지**(para 106, 비한정): (a) 의무기관↔비의무기관 간 이동 가시성 통제(VA 판 CTR·기록보존) (b) 언호스티드 지갑 거래 중점 위험기반 강화감독 (c) RBA 상 허용 주소/출처로만 거래 (d) VASP·의무기관 간 거래로만 제한 (e) 비의무기관 거래 허용 VASP 에 추가 요건(강화 기록·EDD) (f) RBA 적용 가이던스·유형론 발간 (g) 공개 주의·캠페인.
- **VASP 측 조치**(para 295–297): 고객에게서 송수신인 정보 확보, 언호스티드 거래 데이터 수집·모니터링, 추가 제한 선택지 (a) 위험기반 통제틀 강화 (b) 신뢰 평가된 언호스티드 지갑/의무기관으로만 거래 허용 검토.

### 3B-6. 트래블룰(R.16) 핵심 단락

| 쟁점 | 단락 | 원문 요지 |
|---|---|---|
| 적용 범위 | 179 | (a) 전통 전신송금 (b) VASP↔의무기관 간 VA 이전 (c) VASP↔비의무기관(unhosted). (a)(b)는 전면 적용, (c)는 특수 적용. "Countries should treat all VA transfers as cross-border wire transfers" |
| 수수료 제외 | 180 | 채굴 수수료·가스는 트래블룰 범위 밖 |
| 요구정보 | 181–183, Box 4, Table 1 | 송신기관: 송금인 성명·계좌(지갑주소)·주소/국가ID/고객ID/생년월일·장소, 수취인 성명·계좌. 수취기관은 송금인 정보 정확성 검증 의무 없음("may assume that the data has been verified by the ordering VASP") |
| 즉시성 | 184–185, 187 | "'Immediately' ... means that providers should submit the required information prior, simultaneously or concurrently with the transfer itself"; "Post facto submission of the required information should not be permitted" — 배치 전송은 즉시성 충족 시 허용 |
| 안전성 | 186 | 무결성·가용성·무단공개 방지; 상대 VASP 가 정보보호 불가 판단 시 변경 절차 허용 |
| 체인 외 전송 | 188 | "It is not necessary for the information to be attached directly to the VA transfer itself" — 기술 중립 |
| LEI | 189 | 법인에 선택적 LEI 사용 권장 |
| **de minimis** | 191–192 | "Countries may choose to adopt a de minimis threshold for VA transfers of USD/EUR 1 000" — 미달분: 송수신인 성명 + 지갑주소 또는 고유 거래참조번호, 의심 없으면 미검증 |
| 제재 스크리닝 | 193–195 | 정보가 체인과 분리되므로 별도 스크리닝; 지갑 보류, 사업자 지갑 경유 후 고객 지갑 이동 등 통제 예시 |
| **상대 VASP 실사** | 196–199 | 3단계: Phase 1 상대가 VASP 인지 판별 → Phase 2 상대 VASP 식별(신뢰 DB) → Phase 3 적격성 평가. 매 거래마다 불필요, 주기적 갱신. 국가는 기계판독 가능 VASP 목록 유지 권장(198). "jurisdictions may also consider designating all VASPs from countries which do not effectively implement licensing or registration requirements as high-risk"(199) |
| **sunrise** | 200–201 | 단계적 집행 허용·대체조치 요구; "originating entities can require travel rule compliance from beneficiaries by contract or business practice"; 자체 통제 예시 — 내부이전 한정, 확인된 1인칭(first-party) 이전만 허용, 강화 모니터링 |
| 중개 VASP | 202 | 체인 상 정보 전달·5년 기록 |
| unhosted | 203–204 | 고객 측 정보 확보·STR·제재 의무 적용, 추가 제한 선택 가능 |
| VASP 솔루션 요건 | 283 | (a) 상대 VASP 탐색 (b) 즉시 전송 (c) 대량·다중 목적지 안정 처리 (d) 안전 전송 (e) 무단공개 방지 (f) 후속 소통 채널 |
| 상대 실사 정보원 | 289–291 | 법인등기·VASP 목록·BO 등기; 독립 감사 확인; Wolfsberg 질의서를 출발점 예시로 언급(각주 58) |

CDD 임계: "the occasional transaction designated threshold above which VASPs are required to conduct CDD is USD/EUR 1 000 (rather than USD/EUR 15 000)" (para 146, 264; INR.15 para 7(a)); 국가가 더 낮출 수 있음(para 152); DNFBP(카지노 등)가 VA 활동 시 1 000 적용(para 267).

### 3B-7. 라이선스·등록·감독·정보공유

- **어디서 등록하는가**(para 125–128): 최소 "created" 관할(INR.15 para 3); 자연인은 사업장 소재지(서버 위치도 고려요소); 호스트 관할의 추가 요구 가능 — "jurisdictions may consider that broader coverage is the safer course"(127); 비거주 VASP 식별 기준: 사무소·서버·고객센터 위치, 특정국 대상 광고, 웹·앱 언어, 유통망, 고객 질문지(128).
- **식별 도구·인가 조건**(para 130–134): 블록체인 분석·웹스크래핑/OSINT·제보·STR·과거 신청이력·LEA 정보로 미등록자 식별; 출범 전 AML 프로그램 입증, 범죄자 BO·경영 배제·지분변경 사전승인(133), 상주 임원·실질 경영·광고에 인가번호 표기·외주 데이터 접근(134).
- 비이행국 VASP 를 고위험 지정 선택(para 137, 199) — 7차 TU Annex A para 8 이 para 199 를 그대로 인용.
- **감독**(para 142): 자율규제기구(SRB) 불가, 권한 있는 당국만; 검사·자료징구·제재·인가취소 권한.
- **Part Six 원칙**(비구속, para 355): 감독기관 식별·문의채널·등록부 공개(원칙 1–3), 지위 무관 정보교환·양자/다자/감독 콜리지(4–5), 규제 지위·주주·거래·사용자 정보 제공(6), 비밀유지법·진행 조사·기관 성격 차이를 거절 사유로 금지(9), 선제 공유 트리거: 사이버사고·외국 VASP 의 무규제 영업·역외 운영 의심(13), 1차 감독기관 식별은 선택(17), MOU 신속 체결(18).

### 3B-8. 2025–2026 기준 변경으로 갱신·대체된 부분 — "함께 읽어야 할 후속 문서"

| 가이던스 해당 부분 | 후속 문서(일자) | 변화 요지 | 상태 | 확신도 |
|---|---|---|---|---|
| Part Three R.1 RBA(para 98–104) 전반 | R.1/INR.1 개정(2025-02) | FATF 공식 페이지 고지: 2025년 R.1 개정 미반영, 위험평가·금융포용 최신 가이던스와 함께 읽을 것 | 기준 개정 완료 | A(고지 원문) |
| R.16 전 단락(175–204, 281–294) | **R.16 "Payment transparency" 개정(2025-06-18) + Explanatory note** | "FATF has agreed not to bring VASPs directly into the scope of R.16 but to apply the updated requirements indirectly through R.15, and to continue working on travel rule implementation through the existing framework, including through the tailored framework of R.15" (note para 54); de minimis 상한 USD/EUR 1,000 유지(para 33, INR.16 para 8·10); "a majority of respondents agreed with the end of 2030 ... The FATF will expect that most, or all of the new requirements are in effect by that date"(para 59) | amended, 이행시한 2030년 말 | A |
| 동 | 개정 R.16 평가 Methodology Annex IV(2025-10) | 채택되었으나 미발효 — 현행 평가는 구 R.16 기준 | enacted, not in force | B(wave1 F-008 인용, 이번 재확인 안 함) |
| 동 | **R.16 가이던스 공개의견수렴(2026-06-24~08-21)** | 오인송금·금융포용·디지털지갑·데이터보호 쟁점; 최종본 미확인 | 의견수렴 마감, 최종본 미확인 | B(FATF 페이지 JS 차단, FIAU Malta 요약) |
| 트래블룰 감독(para 200–201, 229–260) | Best Practices on Travel Rule Supervision(2025-06-26) | 감독 모범사례; 7차 TU 가 집행 부진 원인 참조문서로 지정(para 25–26) | 발간 | A(존재)·내용 미정독 |
| P2P·unhosted(para 37–41, 105–106, 203–204, 295–297) + 스테이블코인(Box 1, 54, 86–89, 104, 139, 249) | **Targeted Report on Stablecoins and Unhosted Wallets(2026-03-03)** | 250종+·시총 USD 3,000억+(2025 중반); Chainalysis 인용 불법거래 84%; 발행자에 동결·소각·회수·상환 시 CDD·allow/deny-listing 권고; "FATF Standards do not require jurisdictions to adopt regulatory frameworks for stablecoin arrangements beyond those already applicable to VASPs" | 발간 | A(공식 페이지)·PDF 미정독 |
| 라이선스 소재지(para 125–128, 137) | **Understanding and Mitigating the Risks of Offshore VASPs(2026-03-11)** | oVASP 정의; 활동기반 접근 46%; 네스팅·소매 위장; 감독기관 간·FIU 간 채널 | 발간 | A(공식 페이지)·PDF 미정독 |
| DeFi(para 66–69, 80–82, 92–93) | **Targeted Report on Regulatory Challenges from DeFi(2026-07-21)** | "updates and complements the FATF's previous analysis of Decentralised Finance ... as set out in the FATF's 2021 Updated Guidance"; 기능적·위험기반 접근, 통제 존재 판정 권고; 7차 TU 각주 1 의 3분류(식별 가능 통제자 / 실질 중앙화이나 통제자 미식별 / 진정 탈중앙 — 앞 둘에 기준 적용) | 발간(가이던스 아님, 기준 변경 없음) | A(공식 페이지)·PDF 미정독(403) |
| 위험평가(para 42–46, 101) | 7차 TU para 11: ML NRA Guidance 에 VA/VASP 부속서 "expected ... later in 2026" | 국가위험평가 가이던스 부속서 예고 | 예고 | A(TU7 원문) |
| 이행 현황 전반 | 7차 Targeted Update(2026-07-16) | §3C | 발간 | A |

---

## 3C. 문서 ③ — 7th Targeted Update on Implementation of the FATF Standards on VAs/VASPs (2026-07)

### 3C-1. 서지·방법

| 항목 | 내용 | locator |
|---|---|---|
| 정식 인용명 | FATF (2026), *Targeted Update on Implementation of the FATF Standards on Virtual Assets/VASPs*, FATF, Paris | 판권면 Citing reference |
| 웹 제목 | "Seventh Targeted Update on Implementation of the FATF Standards on Virtual Assets/VASPs" | FATF 공식 페이지 |
| 발간일 | 2026-07-16 ("Paris, 16 July 2026"); PDF 메타 생성 2026-07-16 12:38 | 공식 페이지·보도자료; PDF 메타 |
| 분량 | **PDF 34쪽**(표지·판권·뒷표지 포함), 인쇄 pp.1–31. 공식 PDF 와 FIAU Malta 미러 모두 34쪽(미러는 2026-07-23 재생성, 표 레이아웃 미세 차이) | PDF 메타 |
| 구조 | Exec Summary·Key Findings·권고·Next steps(pp.2–6) / Introduction(6–7) / Section One R.15 이행(8–18) / Section Two 위험(19–24) / Section Three 다음 단계(24) / Annex A MIVA 표(25–31) | 목차 p.1 |
| 설문 | 2026-02~06, **147개 관할 응답(FATF 38 + FSRB 109)**, 자기보고·미검증, 조건분기(skip logic). "the report infers that jurisdictions (58 out of 205) that did not respond to the survey have not made progress on R.15" | para 3, p.7; 각주 3–4 |
| 질문군별 응답 수 | 위험평가·정책 145 / 라이선스·감독 130 / 트래블룰 129 / DeFi 142 / NFT·unhosted·P2P 138 | 각주 3, p.7 |
| 기타 자료원 | VACG 회의(2025-09, 2026-05), VACG 심포지엄(2025-12), MER/FUR 149건(2026-04 기준) | para 3 |
| 검증 데이터 제공 | Chainalysis, TRM Labs | 공식 페이지 Acknowledgements |
| 6차 대비 방법 차이 | 6차: 응답 163개(위험평가 기준), 무응답 42/205, TR 응답 117, DeFi·NFT·unhosted·P2P 146; MIVA 표 98% → 7차 97% | TU6 각주·para 21, p.17 |

### 3C-2. 헤드라인 수치 — 6차(2025-06-26) 와 나란히

| 지표 | 6차(2025) | 7차(2026) | 7차 locator |
|---|---|---|---|
| 평가(MER/FUR) 관할 수 | 138 | **149**(2026-04) | para 5, p.8 |
| R.15 C / LC / PC / NC | 1 / 40(29%) / 68(50%) / 29(21%) | **1 / 51(34%) / 64(43%) / 33(22%)** | para 5–6, Fig 1.1, p.8 |
| 연도별 LC 추이(Fig 1.1) | 2022 12(23%)→2023 24(25%)→2024 32(25%)→2025 40(29%) | →2026 51(34%) | Fig 1.1 |
| 15.3(위험평가) met/mostly met | — | 48/149 | para 10, p.10 |
| 15.4(라이선스) met/mostly met | — | 59/149(40%) | para 18, p.14 |
| VA/VASP 위험평가 실시 | 76%(124/163) | **86%(124/145)** | para 9, Fig 1.4, pp.10–11 |
| 규제 접근 결정 | 82%(134/163) | **89%(128/144)**; 미결정 11%(16/144) | para 12, p.11 |
| 허용 / 부분금지 / 전면금지 | 62%(101/163) / 10%(16) / 10%(17) | **66%(95/144) / 8%(12) / 15%(21)** → 금지 합계 23% (2023 11%, 2024 14%, 2025 20%) | para 12, 14, Fig 1.5, pp.11–14 |
| 금지국 중 불법 VASP 집행 | 9/17 | **16/21** | para 17, p.14 |
| 금지국 R.15 등급(33개) | LC 5 / PC 13 / NC 4 / NA 11 | LC 6 / PC 12 / NC 4 / NA 11 | Fig 1.7, p.14 |
| 라이선스·등록 요구 | — | 73%(95/130) | para 18, p.14 |
| **실제 인가·등록 발급** | 65%(76/117) | **58%(76/130)** | para 18, Fig 1.8, pp.14–15 |
| 감독검사 실시 / 집행조치 | 73%(70/96) / 73%(70/96) | **81%(77/95) / 71%(67/95)** | para 19, p.15 |
| 고위험 평가국 중 인가 입법 부재 | 유사 | 10%(5/50) | para 20, p.15 |
| 설립·소재 기준 인가 요구 | 83%(80/96) | 44%(50/114) | para 21, Fig 1.9, pp.15–16 |
| **oVASP 인가 요구(확장 접근)** | 37%(35/96) | **34%(39/114)** | para 21 |
| **트래블룰 입법 완료** | 73%(85/117) | **83%(91/109)** (2023 35/39%, 2024 65/69%) | para 24, Fig 1.10, pp.16–17 |
| 트래블룰 입법 진행 중 | 14/117 | 11/109 | para 24 |
| **입법국 중 TR 감독·집행 전무** | 59%(50/85) | **60%(55/91)** | para 25, p.17 |
| DeFi 위험평가 완료 / 진행 | — | **18%(26/142) / 9%(12/142)** | para 46(a), p.23 |
| DeFi VASP 미식별 | 75%(35/47, 인가요구국 중) | **93%(132/142)** | para 46(b) |
| DeFi 에 완화조치 적용 | 48%(47/99) 인가 요구 | **31%(44/142)**; 인가 부과 **4개**, 실제 등록 **2개** | para 46(c) |
| DeFi 집행 | 7개 감독·집행 | **1개** | para 47, p.23 |
| DeFi 민간 소통 | — | 35%(50/142) | para 46(d) |
| **P2P 고위험 평가** | — | **88%(58/66)**; 중 8%(5), 저 5%(3) | para 38, p.21 |
| **P2P 시장지표 수집** | — | **23%(31/133)** | para 38, p.22 |
| 스테이블코인 불법 비중 | "a majority of all on-chain illicit activity is now transacted in stablecoins"(추정, 수치 없음); USDT on Tron | 7차 본문에 비중 수치 없음 — 2026-03-03 타겟보고서 참조(Chainalysis 84%) | TU6 para 35, p.20; TU7 para 35–36, p.21 |
| DPRK | Bybit USD 1.46bn(2025 최대 단일 탈취), 회수 3.8%, BTC 지갑 35·ETH 지갑 125,000 | Bybit 명시 없음; 캄보디아 복합체 경유 **USD 37m** DPRK 자금; RPC 노드·멀티시그 공급자 등 제3자 인프라 공격 | TU6 para 28–29, p.19; TU7 para 30, 33, pp.19–20 |
| 사기·OCG | 업계 추정 2024 사기·스캠 온체인 USD 51bn; scam-as-a-service | **캄보디아 복합체 USD 4bn(2021-08~2025-01)**; 스페인 Operation Borrelli **EUR 460m·5,000명 피해(2025-06)** | TU6 para 31, p.20; TU7 para 29–31, p.19 |
| AI 악용 | 챗봇·딥페이크 피해자 기망 가능성 언급 | **딥페이크 영상 면접 채용사기로 USD 1m+ 탈취(주로 스테이블코인)**; AI 코딩 도구·에이전트로 스마트컨트랙트 취약점 분석·익스플로잇 생성; 오픈웨이트 모델·자가호스팅 GPU 로 안전장치 우회 | TU7 para 34, p.20 |
| 스테이블코인 신규 유형 | 발행자 동결·차단 기능 논의 | **"deliberate issuance of proprietary stablecoins specifically designed to circumvent law enforcement intervention"** — 제3자 발행자가 USD 29m 동결한 뒤 복합체가 "immune to asset freezing" 마케팅 자체 코인 발행, 다중 체인+자체 체인 | TU7 para 35, p.21 |
| TF 와 스테이블코인 | — | ISIL·AQ 가 BTC 보다 스테이블코인 선호, 주소 로테이션·micro-splitting·multi-hop; Tron USDT; 가스비 조달 은닉 서비스 | TU7 para 33, 36, pp.20–21 |
| MIVA 표 | 비FATF 20+9 추가, 시장 98% | 비FATF +2(거래량 1·사용자 1), 시장 **97%**; **스테이블코인 발행자 등록 요구 열 신설** | Annex A para 2, 7; 표 pp.27–31 |
| 동반 발간물 | Best Practices on Travel Rule Supervision | 스테이블코인(03-03)·oVASP(03-11)·DeFi(07-21) 타겟보고서 | Table 1.1, p.6 |
| VACG 아웃리치 | 2025-04 민간 대면회의 | 2025-09 가상회의, **2025-12 심포지엄 400명+·80개 관할+** | TU7 para 27–28, p.18 |

### 3C-3. FATF 권고(공공·민간) 및 다음 단계

- **공공부문**(pp.3–4): ① 위험평가에 (i) 자국 설립 VASP (ii) 자국 내 영업 oVASP (iii) 자국 통제자 기반 스테이블코인 발행자·DeFi (iv) P2P·unhosted (v) 신기술 포함 ② 신뢰 자료원 활용 ③ 감독틀 — 설립 VASP·스테이블코인 발행자·적격 DeFi 인가, "Where relevant, require VASPs operating cross-border (oVASPs) to be licensed or registered", 온·오프사이트 검사, 무인가 영업 제재 ④ 국제·민관 협력 — 신속 동결·압수 인프라.
- **민간부문**(p.5): ⑤ "VASPs, including Stablecoin issuers and qualifying DeFi arrangements, should establish robust AML/CFT/CPF compliance frameworks and implement the Travel Rule"; KYC·지갑 스크리닝·블랙리스트·화이트리스트·동결·차단 능력 ⑥ 타겟보고서 기반: (i) unhosted 지갑 고위험 활동 EDD (ii) 거래모니터링·블록체인 분석으로 급속 이전 탐지 (iii) "detect accounts used by oVASPs that misrepresent themselves as retail users, restrict or exit higher-risk relationships, and monitor fiat on- and off-ramp activity linked to unlicensed or weakly supervised offshore platforms" (iv) 프로토콜·브리지·믹서·크로스체인 노출 평가.
- **다음 단계**(para 49–50, p.24): 지속 모니터링·평가·위험분석·역량구축; 6차가 약속한 "스테이블코인·oVASP·DeFi 타겟페이퍼(2025-10~2026-06)" 는 3건 모두 이행됨(2026-03-03, 03-11, 07-21).

### 3C-4. 한국 관련 언급(전부)

- Annex A 표(p.29, PDF p.31) "Republic of Korea" 행 — 좌표 기반 재구성: **위험평가 Yes · 명시적 금지 No · VASP 인가·AML 입법 Yes · 스테이블코인 발행자 등록/인가 요구 No · 감독검사 Yes · 집행·감독조치 Yes · 트래블룰 입법 Yes · R.15 등급 N/A**. 각주 3: "For jurisdictions which have not been assessed against the revised FATF Standards on VAs and VASPs, the R.15 rating is marked as not applicable (N/A)."
- 본문 내 "Korea" 는 DPRK(북한) 언급 외 없음. 6차 보고서도 동일.
- Red Flag 보고서 Case Study 2 "Source: South Korea"(p.7) — KRW 4억 피싱 자금, 국내 VASP 48개 계정·55회 이전.
- RBA 가이던스 Part Five 국가 사례(이탈리아·핀란드·일본·멕시코·노르웨이·스위스·미국)에 한국 없음.

### 3C-5. 같은 시기 FATF 관련 발간물·행사(확인 목록)

| 일자 | 문서/행사 | 확인 방법 | 비고 |
|---|---|---|---|
| 2026-03-03 | Targeted Report on Stablecoins and Unhosted Wallets — Peer-to-Peer Transactions (PDF 5 MB) | 공식 페이지 200 | PDF 직접 URL 추정 경로 404 — 페이지 링크 경유 필요 |
| 2026-03-11 | Understanding and Mitigating the Risks of Offshore VASPs (PDF 4 MB) | 공식 페이지 200, PDF HEAD 200 | 나이지리아 FIU(USD 6억 지갑), 인도네시아 FIU, 영국 FCA 1,000+ 사이트 차단, NZ VAIRG·인도 Sub-Group, 케이맨–ADGM 협력 사례 |
| 2026-06-17~19 | FATF 총회 성과문 — 캐나다·튀르키예 5차 MER 채택, 알제리·나미비아 회색명단 해제, BiH·이라크 편입, INR.6 인도적 예외 개정, 영국 의장국 우선순위 승인, 인도 Vivek Aggarwal 부의장 | 공식 페이지 200 | VA 관련: 7차 TU·DeFi 보고서 승인(2026-07 발간) |
| 2026-06-24 | R.16 가이던스 공개의견수렴 개시(마감 2026-08-21) | FATF 페이지 JS 차단(403); FIAU Malta·검색 요약 | confidence B |
| 2026-07-16 | 7차 Targeted Update + 보도자료 "FATF calls for closing of regulatory gaps as virtual asset illicit finance risks become more complex" | 공식 페이지·PDF 200 | — |
| 2026-07-21 | Targeted Report on Regulatory Challenges from DeFi (PDF 5 MB) + 보도 "FATF urges action to respond to emerging risks from Decentralised Finance" | 공식 페이지 200, PDF 403 | — |
| 2026-10-26~30 | FATF Plenary and Working Group Meetings, Paris(영국 의장국 첫 총회) | FATF 일정표 200 | 2026-10-21 기준 미개최; 보도(T4)는 본회의 10-28~30 |

---

## 4. 원자적 사실 (Atomic Facts)

```
F-001
claim: FATF 는 2020-09-14 "Virtual Assets — Red Flag Indicators of Money Laundering and Terrorist Financing"(PDF 24쪽, 인쇄 pp.1–20)을 발간했다.
entity: reg:fatf-va-red-flags-2020
source_url: https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets-red-flag-indicators.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Paris, 14 September 2020 - Virtual assets use innovative technology to swiftly transfer value around the world ... Based on more than 100 case studies collected by members of the FATF Global Network, it highlights the most important red flag indicators that could suggest criminal behaviour."
note: PDF 직접 URL https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf (1,132,000 bytes, 2026-10-21 200 응답). 페이지 분류는 "FATF Recommendations, Methods and Trends".
```

```
F-002
claim: 보고서의 지표는 2017–2020년 관할 제출 100건 이상의 사례, 2019-06 비공개 FATF 금융조사 보고서, 2014-06 가상통화 보고서 및 공개정보에 기반한다.
entity: reg:fatf-va-red-flags-2020
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "The red flag indicators included in this report are based on more than one hundred case studies contributed by jurisdictions from 2017-2020, the findings of the Confidential FATF Report on Financial Investigations Involving Virtual Assets (June 2019) and the published FATF Report Virtual Currencies Key Definitions and Potential AML/CFT Risks (June 2014), as well as information on the misuse of VAs available in the public domain."
note: para 6, p.4. 본문 수록 사례는 번호 13건 + 무번호 1건이며 "100건 이상" 은 기초자료 수다.
```

```
F-003
claim: 지표 범주는 6개(Transactions / Transaction Patterns / Anonymity / Senders or Recipients / Source of Funds or Wealth / Geographical Risks)이며 상위 지표는 합계 58개(5·8·14·19·8·4)다.
entity: reg:fatf-va-red-flags-2020
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Red Flag Indicators Related to Transactions 5 / Red Flag Indicators Related to Transaction Patterns 7 / Red Flag Indicators Related to Anonymity 9 / Red Flag Indicators about Senders or Recipients 12 / Red Flag Indicators in the Source of Funds or Wealth 15 / Red Flag Indicators Related to Geographical Risks 17"
note: 목차 p.1(숫자는 쪽). 58개 집계는 본 도시에가 상위 불릿(■) 기준으로 센 것이며 하위 ○ 불릿 포함 시 늘어난다.
```

```
F-006
claim: 거래 범주 지표에 "입금 후 즉시 개인지갑 출금은 거래소를 사실상 믹서로 전환한다" 는 서술과, 24시간 내 다수 고액·규칙적 간격(랜섬웨어 전형)·신규/휴면 계정 대상 거래 지표가 포함된다.
entity: reg:fatf-va-red-flags-2020
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "withdrawing the VAs from a VASP immediately to a private wallet. This effectively turns the exchange/VASP into an ML mixer." / "in a staggered and regular pattern, with no further transactions recorded during a long period afterwards, which is particularly common in ransomware-related cases"
note: pp.5–6, para 11. 저장소 `x-passthrough-chain` 의 원형이다.
```

```
F-007
claim: 익명성 범주는 Tor/VPN·프록시 도메인·동일 IP/MAC 다수 지갑·AEC 전환·믹서·언호스티드/하드웨어/페이퍼 지갑 국경이동·ATM 등 14개 지표를 열거하며, 하드웨어·페이퍼 지갑 등 보안 목적 사용은 그 자체로 불법이 아니라고 단서한다.
entity: reg:fatf-va-red-flags-2020
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "the mere presence of these features in an activity does not automatically suggest an illicit transaction. For example, the use of a hardware or paper wallet may be legitimate as a way to secure VAs against thefts." / "A large number of seemingly unrelated VA wallets controlled from the same IP-address (or MAC-address), which may involve the use of shell wallets registered to different users"
note: para 13, pp.9–10. ATM 지표는 "A single use of an ATM/kiosk is not enough in and of itself to constitute a red flag" 단서 포함.
```

```
F-008
claim: 송수신인 범주(19개)는 계정 생성 이상 4·CDD 이상 3·프로필 4·뮬/피해자 프로필 4·기타 4로 구성되며, 고령 고객·VA 기술 비숙련 송금인·재정 취약자를 뮬·피해자 신호로 든다.
entity: reg:fatf-va-red-flags-2020
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Sender does not appear to be familiar with VA technology or online custodial wallet solutions. Such persons could be money mules recruited by professional money launderers, or scam victims turned mules" / "A customer significantly older than the average age of platform users opens an account and engages in large numbers of transactions"
note: para 14, pp.12–15. 저장소 63지표 중 이 하위범주에 대응하는 것이 없다.
```

```
F-010
claim: 저장소 `kb/entities/indicators/` 63개 지표의 curator_note 는 모두 "FATF Red Flag Indicators 원문을 직접 확보하지 못해 T3 요약에 의존했다"(확신도 B)고 기재하고 있다.
entity: reg:fatf-va-red-flags-2020
source_url: C:\Users\강성준\Desktop\app\aml\kb\entities\indicators\x-below-threshold-clustering.yaml
publisher: 저장소 내부
tier: T1(내부 1차자료)
confidence: A
retrieved: 2026-10-21
quote: "확신도 B — FATF Red Flag Indicators 원문을 직접 확보하지 못해 T3 요약에 의존했다. 임계값·수치는 도시에 표기를 그대로 옮긴 것이며 관할별 기준과 다를 수 있다."
note: 샘플 2건(`x-below-threshold-clustering`, `x-known-mixer-exposure`) 확인, 나머지는 동일 템플릿. evidence doc 은 "DOC:x-typology-taxonomy-2026".
```

```
F-020
claim: FATF 는 2021-10-28 "Updated Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers"(PDF 111쪽)를 발간했으며, 이 문서는 2019-06 초판을 통합·대체한다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Paris – 28 October 2021 - The virtual asset sector is fast-moving and technologically dynamic" / (PDF p.6) "This document incorporates and supersedes the 2019 Guidance."
note: PDF https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf (3,574,282 bytes; 메타 Title "Updated Guidance for a Risk-Based Approach for Virtual Assets and Virtual Asset Service Providers", 생성 2021-10-26, 수정 2021-11-08).
```

```
F-021
claim: 2021 개정은 6개 영역 — VA/VASP 정의 명확화, 스테이블코인 적용, P2P 위험·도구, 라이선스·등록, 트래블룰 이행, 감독기관 간 정보공유 원칙 — 에 집중했다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "These revisions focused on six key areas where greater guidance from the FATF was sought. These are to (1) clarify the definitions of VA and VASP ..., (2) provide guidance on how the FATF Standards apply to stablecoins ..., (3) provide additional guidance on the risks and the tools available to countries to address the ML/TF risks for peer-to-peer transactions ..., (4) provide updated guidance on the licensing and registration of VASPs, (5) provide additional guidance for the public and private sectors on the implementation of the 'travel rule', and (6) include Principles of Information-Sharing and Co-operation Amongst VASP Supervisors."
note: Executive Summary pp.5–6. 7차 TU 각주 2(p.6)도 동일 6개를 열거.
```

```
F-022
claim: 가이던스 단락 번호는 1–357 이며 DeFi 는 para 66–69, P2P 위험 37–41, P2P 완화 선택지 105–106, 라이선스 123–141, 트래블룰(국가) 175–204, 트래블룰(VASP) 281–294, unhosted(VASP) 295–297, 정보공유 원칙 Part Six 이다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "67. A DeFi application (i.e. the software program) is not a VASP under the FATF standards, as the Standards do not apply to underlying software or technology (see paragraph 82 below). However, creators, owners and operators or some other persons who maintain control or sufficient influence in the DeFi arrangements, even if those arrangements seem decentralized, may fall under the FATF definition of a VASP where they are providing or actively facilitating VASP services."
note: 단락 범위는 PDF 전문 텍스트에서 확인(§3B-3 표). 각주 7·8·23 이 내부 참조(37–41, 86–90, 104–106)를 명시해 교차검증 가능.
```

```
F-023
claim: 가이던스는 모든 VA 이전을 국내 아닌 국경간 전신송금으로 취급하도록 요구하며, R.16 은 VASP↔의무기관 간 이전에 전면 적용되고 unhosted wallet 이전에는 특수 방식으로 적용된다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Countries should treat all VA transfers as cross-border wire transfers, in accordance with INR. 1, rather than domestic wire transfers, based on the cross-border nature of VA activities and VASP operations. For transfers involving unhosted wallets (i.e., (c) above), the requirements of R.16 apply in a specific way"
note: para 179, p.56.
```

```
F-024
claim: "즉시(immediately)" 는 이전 이전·동시·병행 전송을 뜻하며 사후(post facto) 전송은 허용되지 않고, 배치 전송은 즉시성 충족 시 허용된다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "'Immediately,' ... means that providers should submit the required information prior, simultaneously or concurrently with the transfer itself." / "The submission of originator and beneficiary information in batches is acceptable, as long as submission occurs immediately and securely as per the FATF Standards. Post facto submission of the required information should not be permitted"
note: para 185, 187, pp.59–60. para 188: 정보가 체인 상 거래에 부착될 필요 없음(기술중립).
```

```
F-025
claim: 국가는 VA 이전에 USD/EUR 1 000 de minimis 임계를 채택할 수 있으며, 미달 이전에는 송수신인 성명과 지갑주소(또는 고유 거래참조번호)만 수집하고 의심 없으면 검증하지 않는다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Countries may choose to adopt a de minimis threshold for VA transfers of USD/EUR 1 000 in line with the FATF Standards ... For VA transfers under the threshold, countries should require that VASPs collect: a. the name of the originator and the beneficiary; and b. the VA wallet address for each or a unique transaction reference number."
note: para 191–192, p.61; VASP 측 para 294, p.86. CDD 임시거래 임계도 USD/EUR 1 000(para 146, 149, 264, 266; 각주 37 "The FATF agreed to lower the threshold amount for VA-related transactions to USD/EUR 1 000").
```

```
F-026
claim: 상대 VASP 실사는 3단계(상대가 VASP 인지 판별 → 상대 VASP 식별 → 적격성 평가)로 제시되며, FATF 는 지갑주소만으로 수취 VASP 를 완전·정확히 식별하는 기술적으로 입증된 수단을 알지 못한다고 명시한다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "To date, the FATF is not aware of any technically proven means of identifying the VASP that manages the beneficiary wallet exhaustively, precisely, and accurately in all circumstances and from the VA address alone"
note: para 197(a), p.62; 동일 문장 각주 30(p.39). para 196: 매 이전마다 실사 불필요, 주기적 갱신. para 198: 기계판독 VASP 목록 권장.
```

```
F-027
claim: sunrise issue 에 대해 가이던스는 단계적 집행과 대체조치를 허용하고, 송신 VASP 가 계약·사업관행으로 수취 측에 트래블룰 준수를 요구할 수 있으며, 내부이전 한정·확인된 1인칭 이전만 허용·강화 모니터링을 자체 통제 예시로 든다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "some jurisdictions will require their VASPs to comply with the travel rule prior to other jurisdictions (i.e., the 'sunrise issue') ... Regardless of the lack of regulation in the beneficiary jurisdiction, originating entities can require travel rule compliance from beneficiaries by contract or business practice." / "Examples include VASPs restricting VA transfers to within their customer base (i.e., internal transfers of VAs within the same VASP), only allowing confirmed first-party transfers outside of their customer base ... and enhanced monitoring of transactions."
note: para 200–201, p.64; VASP 측 para 287, p.84.
```

```
F-028
claim: P2P 거래 위험 완화를 위해 국가가 고려할 수 있는 선택지 7개(VA 판 CTR·기록보존, unhosted 중점 강화감독, 허용 주소 한정, 의무기관 간 거래 한정, 비의무기관 거래 VASP 에 추가 요건, RBA 가이던스, 공개 주의)가 para 106 에 비한정 목록으로 제시된다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "a. controls that facilitate visibility of P2P activity and/or VA activity crossing between obliged entities and non-obliged entities (these controls could include VA equivalents to currency transaction reports or a record-keeping rule relating to such transfers); b. ongoing risk-based enhanced supervision of VASPs ... with a specific focus on unhosted wallet transactions ...; c. obliging VASPs to facilitate transactions only to/from addresses/sources that have been deemed acceptable in line with their RBA; d. obliging VASPs to facilitate transactions only to/from VASPs and other obliged entities; e. placing additional AML/CFT requirements on VASPs that allow transactions to/from non-obliged entities"
note: para 106, pp.39–40. para 37 P2P 정의; para 40 "the FATF has not observed a distinct trend towards increased usage of P2P transactions so far"(2021 시점).
```

```
F-029
claim: FATF 공식 페이지는 2021 가이던스가 발간 이후의 기준 개정(2025년 R.1 개정 포함)을 반영하지 않으며 위험평가·금융포용 최신 가이던스와 함께 읽어야 한다고 고지한다.
entity: reg:fatf-vasp-guidance-2021
source_url: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "This guidance document does not reflect revisions to the FATF standards made after its date of publication, including the 2025 revisions to Recommendation 1 on the risk-based approach. A full list of updates to the Recommendations, by date, is included as Annex II of the FATF Recommendations. This guidance should be read alongside more recent Guidance by the FATF on risk assessment and financial inclusion."
note: 페이지 상단 이탤릭 고지. 같은 페이지가 개정 근거로 12-Month Review 와 2021-03~04 공개의견수렴을 명시.
```

```
F-030
claim: 2025-06 R.16 개정 설명서는 VASP 를 R.16 직접 적용 대상에 넣지 않고 R.15 를 통해 간접 적용하며 VACG 지원 아래 기존 트래블룰 틀을 유지한다고 밝힌다.
entity: reg:fatf-r16-2025
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Explanatory%20note%20for%20revised%20R.16.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Consistent with the feedback received in both public consultations, FATF has agreed not to bring VASPs directly into the scope of R.16 but to apply the updated requirements indirectly through R.15, and to continue working on travel rule implementation through the existing framework, including through the tailored framework of R.15 and the support of the FATF's Virtual Asset Contact Group (VACG). Overall, while VASPs will have to comply with the new requirements imposed by the revised R.16, they will continue to be the target of substantial FATF support. INR.15 will be updated, if necessary"
note: Explanatory note para 54, p.12. para 55: 응답 VASP 들이 오인송금 식별 등 신규 의무 기술을 이미 보유한다고 응답.
```

```
F-031
claim: 개정 R.16 의 이행 시한은 2030년 말이며, de minimis 임계는 국내·국경간 모두 USD/EUR 1,000 이하로 유지된다.
entity: reg:fatf-r16-2025
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Explanatory%20note%20for%20revised%20R.16.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "a majority of respondents agreed with the end of 2030, which has been identified as a as a realistic deadline for implementation. The FATF will expect that most, or all of the new requirements are in effect by that date." / "Countries may adopt a de minimis threshold (no higher than USD/EUR 1,000) for cross-border wire payments or value transfers"
note: para 59(p.12), para 33(p.7), 개정 INR.16 para 8·10. 원문 오타 "as a as a" 그대로. `notes/2-regulations/fatf.md` 의 "€1~$3,000 범위 재량" 서술은 이 문서와 상충(§9).
```

```
F-040
claim: FATF 는 2026-07-16 제7차 "Targeted Update on Implementation of the FATF Standards on Virtual Assets/VASPs"(PDF 34쪽, 인쇄 pp.1–31)를 발간했다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-updated-virtualassets-vasps-2026.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Paris, 16 July 2026 - This targeted update assesses progress and remaining gaps in the implementation of Recommendation 15 (R.15) across the FATF Global Network" / (판권면) "FATF (2026), Targeted Update on Implementation of the FATF Standards on Virtual Assets/VASPs, FATF, Paris, France"
note: PDF https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf (3,467,117 bytes; pypdf 34쪽; 메타 생성 2026-07-16 12:38 CEST). FIAU Malta 미러(665,255 bytes, 2026-07-23 재생성)도 34쪽. wave1 도시에 F-013 의 "35 PDF페이지, 인쇄 p.1~33" 과 상충(§5).
```

```
F-041
claim: 7차 설문은 2026-02~06 실시되어 147개 관할(FATF 38 + FSRB 109)이 응답했고, 글로벌 네트워크 205개 중 58개 무응답은 미진전으로 추정 처리됐으며, 질문군별 응답 수는 위험평가 145·라이선스 130·트래블룰 129·DeFi 142·NFT/unhosted/P2P 138 이다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "The survey collected responses from 147 jurisdictions (38 FATF members and 109 FSRB members). Responses were self-reported and have not been independently verified. ... the report infers that jurisdictions (58 out of 205) that did not respond to the survey have not made progress on R.15" / "Risk assessment and policy approach to VASPs: 145 respondents; licensing/registering and supervising VASPs: 130 respondents; Travel Rule implementation: 129 respondents; DeFi; 142 respondents; treatment of NFTs, unhosted wallets, and P2P: 138 respondents."
note: para 3 p.7, 각주 3–4. 자료원에 VACG 회의(2025-09, 2026-05)·심포지엄(2025-12) 포함. 6차는 163개 응답(위험평가 질문군), 무응답 42/205.
```

```
F-042
claim: 2026-04 기준 R.15 기술준수 평가 149개 관할 중 C 1, LC 51(34%), PC 64(43%), NC 33(22%)이며, 2025년 138개 중 C 1, LC 40(29%), PC 68(50%), NC 29(21%)에서 개선됐다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "The proportion of jurisdictions that are largely compliant (LC) increased from 29% (40 of 138 jurisdictions) in 2025 to 34% (51 of 149 jurisdictions) in 2026, and the proportion of jurisdictions partially compliant (PC) with the revised R.15 also decreased slightly from 50% (68 of 138 jurisdictions) in 2025 to 43% (64 of 149 jurisdictions) in 2026. 6. ... from 21% (29 of 138 jurisdictions in 2025) to 22% (33 of 149 jurisdictions in 2026). As in 2025, only one jurisdiction continues to be fully compliant (C) with R.15."
note: para 5–6, Figure 1.1, p.8. Figure 1.1 연도별: 2022 LC 12(23%)/PC 33(62%)/NC 8(15%); 2023 24(25%)/50(51%)/23(24%); 2024 32(25%)/65(50%)/32(25%). 세부기준: 15.3 met/mostly met 48/149(para 10), 15.4 59/149=40%(para 18).
```

```
F-043
claim: 2026 설문에서 트래블룰 입법 완료는 83%(91/109, 2025년 73% 85/117), 진행 중 11/109(2025년 14/117)이다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "For the 2026 survey, 83% of respondents (91 of 109 jurisdictions) have passed legislation implementing the Travel Rule (see Figure 1.10), up from 73% (85 of 117) in 2025. An additional 11 of 109 jurisdictions reported being in the process of implementing the Travel Rule, compared to 14 of 117 jurisdictions in 2025."
note: para 24, pp.16–17. Figure 1.10 추이: 2023 35(39%), 2024 65(69%), 2025 85(73%), 2026 91(83%). 분모(응답 수)가 매년 달라 절대수 병기 필수.
```

```
F-044
claim: 트래블룰 입법 91개 관할 중 60%(55개)는 트래블룰 준수 관련 지적·지시·집행·감독조치를 아직 취하지 않았다(2025년 59%, 50/85).
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Slightly more than half of the 91 jurisdictions (60%; 55 of 91) that have passed legislation implementing the Travel Rule have not yet issued findings or directives or taken enforcement or other supervisory actions against VASPs focused on Travel Rule compliance."
note: para 25, p.17. Key Findings(p.3)는 같은 수치를 "almost half" 로 표현해 본문(60%)과 어긋남(§5). 6차 para 22: 59%(50/85).
```

```
F-045
claim: 2026년 라이선스·등록 요구 관할은 73%(95/130)이나 실제 인가·등록 발급은 58%(76/130)로 2025년 65%(76/117)보다 비율이 낮고(절대수 동일 76), 감독검사 실시는 81%(77/95, 2025년 73% 70/96), 집행조치는 71%(67/95, 2025년 73% 70/96)다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "73% of respondents (95 of 130), excluding those that prohibit or plan to prohibit VASPs entirely, report that they require VASPs to be licensed or registered. However, progress in actual licensing or registration appears more limited. In the 2026 survey, 58% of respondents (76 of 130) reported having licensed or registered a VASP in practice, compared with 65% (76 of 117) in 2025." / "supervisory inspections of VASPs (81%; 77 of 95) and taking enforcement actions or other administrative actions against VASPs (71%; 67 of 95)"
note: para 18–19, pp.14–15. FATF 자체가 설문과 평가 결과의 불일치·혼란 응답(검사했다면서 인가 미발급 등)을 경고(para 19).
```

```
F-046
claim: 2026 설문에서 P2P 거래를 고위험으로 평가한 관할은 88%(58/66), 중위험 8%(5), 저위험 5%(3)이며, P2P 시장지표를 수집·평가하는 관할은 23%(31/133)에 그친다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "88% of jurisdictions (58 of 66) rated P2P transactions as high risk, while 8% (5 of 66) rated them as medium and 5% (3 of 66) as low. FATF has previously conducted market metric analysis of P2P transactions but was unable to present definitive figures due to significant discrepancies in data across companies. As the 2026 survey results indicate that only 23% (31 of 133) of respondent jurisdictions indicated that they collect and assess P2P market metrics"
note: para 38, pp.21–22. 2021 가이던스 para 39·105(c)의 "시장지표 수집" 권고가 5년 뒤에도 23% 이행.
```

```
F-047
claim: DeFi 관련 2026 설문: 위험평가 완료 18%(26/142), 진행 9%(12/142), 자국 내 VASP 해당 DeFi 미식별 93%(132/142), 완화조치 적용 31%(44/142), 라이선스 부과 4개, 실제 등록 2개, 민간 소통 35%(50/142), 집행 1개.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "a. Only a minority (18%; 26 of 142) have assessed the risks associated with DeFi arrangements ... b. A large majority (93%; 132 of 142) have not identified DeFi arrangements operating in their territory that qualify as VASPs ... c. While some jurisdictions (31%; 44 of 142) reported that their risk mitigation measures apply to DeFi arrangements, only four jurisdictions have imposed licensing or registration requirements, and just two have actually licensed or registered such arrangements in practice." / "with only one jurisdiction reporting to have taken enforcement actions in practice"
note: para 46–47, p.23. 6차(2025)는 다른 모집단(99개 선진국 중 48% 47개 인가 요구, 4개 등록, 7개 감독·집행)이라 직접 비교 불가(§5).
```

```
F-048
claim: 라이선스 요구 관할 114개 중 34%(39개)가 자국에 설립·소재하지 않은 oVASP 에도 특정 요건 충족 시 인가·등록을 요구하며(2025년 37%, 35/96), 설립·소재 기준 요구는 44%(50/114)다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Around two-fifths of jurisdictions with VASPs licensing or registration requirements (44%; 50 of 114) report meeting this standard ... Approximately a third of jurisdictions (34%; 39 of 114) reported taking a more extensive approach by requiring offshore VASPs (that are not created or located in their jurisdictions) to be licensed/registered if VASPs meet certain other requirements."
note: para 21, Figure 1.9, pp.15–16. 2026-03-11 oVASP 보고서의 "활동기반 접근 46%" 와 모집단·정의가 달라 수치 불일치(§5).
```

```
F-049
claim: 2026년 VA/VASP 금지 접근 관할은 23%(33/144; 전면 21, 부분 12)로 2023 11%(16/151)→2024 14%(20/147)→2025 20%(33/163)에서 계속 증가했고, 전면 금지 21개 중 16개가 불법 VASP 집행조치를 보고했다(2025년 9/17, 2024년 9/14).
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "23% of respondents reported opting to prohibit VASPs, indicating a steady increase over the past few years, rising from 11% of survey respondents in 2023 (16 of 151), 14% in 2024 (20 of 147) and 20% in 2025 (33 of 163)." / "16 of 21 jurisdictions explicitly prohibiting the use of VAs and VASPs reported taking such actions, compared with 9 of 17 in the 2025 Targeted Update and 9 of 14 in the 2024 Targeted Update."
note: para 12, 14, 17, Figure 1.5–1.7, pp.11–14. 부분금지의 전형은 "결제수단 사용 금지 + 투자·거래 제한 허용"(para 15). MENAFATF 에서 금지 접근이 흔함(para 13).
```

```
F-051
claim: 7차 TU 는 캄보디아 소재 금융 복합체가 2021-08~2025-01 최소 USD 40억을 세탁했고 그중 최소 USD 3,700만이 DPRK 사이버 탈취자금이라고 서술한다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "competent authorities found that a Cambodia-based financial services conglomerate laundered at least USD 4 billion in illicit proceeds between August 2021 and January 2025, functioning as a critical node connecting cyber-enabled fraud networks, underground banking infrastructure, and VA-based money laundering pipelines." / "Of the USD 4 billion in aggregate illicit proceeds processed, at least USD 37 million has been attributed to DPRK cyber heists"
note: para 29–30, p.19; 각주 13(미 재무부·영국 공동조치), 14, 16(Federal Register 2025-10-16 FinCEN 특별조치 "Huione Group"). 본문은 기업명을 쓰지 않고 각주 URL 에만 등장.
```

```
F-052
claim: 7차 TU 는 동결 저항을 명시적 목적으로 한 자체 스테이블코인 발행을 신규 유형으로 보고하며, 제3자 발행자가 USD 2,900만 이상을 동결한 사건이 발행 동기였다고 서술한다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "A particularly notable development in the misuse of virtual assets within VA-enabled fraud ecosystems is the deliberate issuance of proprietary stablecoins specifically designed to circumvent law enforcement intervention. ... launched a USD-pegged stablecoin marketed as immune to asset freezing ... This capability gap was exploited following an instance in which a third-party stablecoin issuer froze assets valued at over USD 29 million held in a wallet linked to the same conglomerate"
note: para 35, p.21. 시사점(원문): VASP 가 "issuer-level asset freeze/burn mechanisms" 를 준수 안전장치로 의존하지 못할 수 있음.
```

```
F-053
claim: 7차 TU 는 AI 를 사기·해킹·세탁 전주기 위험요인으로 지목하며, 딥페이크 영상 면접을 이용한 채용사기로 USD 100만 이상(주로 스테이블코인)이 탈취된 사례와 AI 코딩 도구·에이전트의 익스플로잇 생성 가능성을 든다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "attackers have used synthetic profiles and deepfake video interviews in AI-enabled recruitment scams to build victims' trust, before inducing them to install malware or grant wallet access, resulting in the theft of more than USD 1 million in virtual assets, primarily stablecoins. AI coding assistants and AI agents may also be used to analyse smart contract vulnerabilities, generate exploit code and identify attack paths"
note: para 34, p.20. 6차(para 31)는 "AI (chatbots, deepfakes) could be used to scam victims" 수준의 가능성 언급.
```

```
F-054
claim: 7차 TU 는 DPRK 가 VASP·DeFi 프로토콜뿐 아니라 RPC 노드·멀티시그 보안 공급자 등 제3자 인프라 취약점을 악용하고 브리지·언호스티드 지갑·OTC 로 세탁하며, TF 에서 Tron 기반 USDT 와 가스비 조달 패턴 은닉 서비스가 관찰된다고 서술한다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "The DPRK continues to exploit vulnerabilities not only in VASPs and DeFi protocols, but also in the wider third-party infrastructure on which these services rely, including RPC nodes and multi-signature security providers, while laundering proceeds through bridges, unhosted wallets and OTC networks. In relation to terrorist financing, the use of Tron-based USDT, as well as the emergence of services that obscure gas-fee funding patterns"
note: para 33, p.20. 7차 본문에 "Bybit"·"1.46" 문자열 없음(grep 확인).
```

```
F-055
claim: 6차 TU(2025)는 DPRK 의 Bybit USD 14.6억 탈취(2025년 최대 단일 탈취), 회수율 3.8%, BTC 지갑 35개·ETH 지갑 125,000개 사용, 2024년 사기·스캠 온체인 불법활동 약 USD 510억(업계 1개사 추정)을 보고했다.
entity: case:tu6-2025
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2025-Targeted-Upate-VA-VASPs.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "the DPRK conducted the largest single theft of VAs in in 2025, stealing $1.46 bn worth of VAs from the VASP ByBit." / "a large number of wallets in complex transaction pattens (35 bitcoin wallets and 125,000 Ethereum wallets) ... only 3.8 percent of the stolen funds had been recovered" / "One industry participant estimated that there was approximately $51 billion in illicit on-chain activity relating to fraud and scams in 2024."
note: TU6 para 28–29, 31, pp.19–20. 6차는 2025-06-26 발간(PDF 32쪽, 메타 생성 2025-06-25; 공식 페이지 "Paris, 26 June 2025"), Best Practices on Travel Rule Supervision(HEAD 200, 미정독) 동시 발간, MIVA 표 시장 비중 약 98%, 데이터 제공 Chainalysis·Lukka·Merkle Science·TRM Labs. 원문 오타 "in in", "pattens" 그대로.
```

```
F-056
claim: 7차 TU Annex A 표의 "Republic of Korea" 행은 위험평가 Yes, 명시적 금지 No, VASP 인가·AML 입법 Yes, 스테이블코인 발행자 등록·인가 요구 No, 감독검사 Yes, 집행·감독조치 Yes, 트래블룰 입법 Yes, R.15 등급 N/A 다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Republic of Korea | Yes | No | Yes | No | Yes | Yes | Yes | N/A" (표 행; 열 순서는 표 머리말 순)
note: p.29(PDF p.31). pdftotext 레이아웃 변환에서 행 정렬이 깨져 PyMuPDF 좌표 기반으로 재구성(같은 y 좌표 단어열). 각주 3: "For jurisdictions which have not been assessed against the revised FATF Standards on VAs and VASPs, the R.15 rating is marked as not applicable (N/A)." 스테이블코인 열은 2026년판에서 신설(6차 표 머리말에 없음).
```

```
F-057
claim: Red Flag 보고서 Case Study 2 는 한국 제출 사례로, 피싱 피해금 약 KRW 4억(EUR 301,170)이 3종 VA 로 전환되어 국내 VASP 48개 계정을 통해 55회 이전된 뒤 해외 지갑으로 이동했다.
entity: reg:fatf-va-red-flags-2020
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "A local VA exchange reported that approximately KRW 400 million (EUR 301 170) was stolen from phishing victims and was ultimately exchanged for VAs as a layering technique. ... transferring funds an additional 55 times through 48 separate accounts held in different local VASPs, and then to a different VA wallet located abroad. Source: South Korea"
note: p.7. 트리거는 "multiple high-value transactions transferred to a foreign VASP into one single wallet".
```

```
F-058
claim: FATF 한국 4차 상호평가 보고서(2020-02 총회 채택, 2020-04-16 공개)의 기술준수 등급표는 R.15(New technologies)를 "C"(Compliant), R.16(Wire transfers)를 "LC" 로 기재한다.
entity: case:korea-mer-2020
source_url: https://www.fatf-gafi.org/en/publications/Mutualevaluations/Mer-korea-2020.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "R.13 - Correspondent banking C R.14 - Money or value transfer services C R.15 - New technologies C R.16 - Wire transfers LC" / "Paris, 16 April 2020 – Korea has a sound legal framework to tackle money laundering and terrorist financing" / "The FATF adopted this report at its February 2020 Plenary meeting."
note: 페이지 내 등급표 텍스트. 이 평가는 2019-06 INR.15 개정 전 기준(현장방문 2019)이라 7차 TU 표는 한국을 "개정 기준 미평가(N/A)" 로 둔다. `notes/2-regulations/fatf.md` 의 "가상자산 영역 PC" 서술과 상충(§9).
```

```
F-059
claim: MIVA 표는 2024-03 최초 발간(FATF 회원 + 비FATF 20개), 2025년 비FATF 9개 추가, 2026년 2개 추가(거래량 기준 1, 사용자 기준 1)되어 글로벌 VA 시장의 약 97% 를 포괄하며, 선정 기준은 세계 거래량 0.25% 초과 및/또는 VA 보유·채택률 상위 30개국이다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "The FATF published the first table in March 2024 ... FATF members and 20 jurisdictions with materially important virtual asset service provider (VASP) activities ... The 2025 update expanded the table to incorporate 9 additional non-FATF jurisdictions ... and the 2026 update identifies 2 further jurisdictions. These jurisdictions covered in the table account for approximately 97 percent of the global VA market."
note: Annex A para 2, 6–7, pp.25–26; 각주 21: 사용자 수 공개자료 접근 불가로 사용자 기준 포함 임계 변경. 좌표 재구성 결과 데이터 행 69개(러시아 자격정지 표기 포함). para 9: 표 포함은 위험도·준수도 판단이 아님.
```

```
F-060
claim: FATF 2026년 10월 총회(영국 의장국 첫 총회)는 FATF 일정표상 2026-10-26~30 파리에서 열리며, 2026-10-21 기준 미개최다.
entity: case:fatf-plenary-2026-10
source_url: https://www.fatf-gafi.org/en/calendars/events.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "FATF Plenary and Working Group Meetings Oct 2026 Start date 2026-10-26 00:00 End date 2026-10-30 00:00 Meeting FATF Plenary and Working Group Meetings, Paris, France"
note: 보도(ANI, 2026-10-21, T4)는 본회의를 10-28~30, 멕시코·미국 MER 논의 예정으로 전함. 성과문 URL(outcomes-fatf-plenary-october-2026.html)은 404.
```

```
F-061
claim: FATF 는 2026-06-24 개정 R.16 이행 가이던스 초안 공개의견수렴을 개시했고 마감은 2026-08-21 이었다.
entity: case:r16-guidance-consult-2026
source_url: https://fiaumalta.org/news/latest-updates-from-the-fatf/
publisher: FIAU Malta(FATF 페이지 요약)
tier: T2
confidence: B
retrieved: 2026-10-21
quote: "Any responses to this public consultation should be sent by Friday 21 August 2026"
note: FATF 원 페이지 https://www.fatf-gafi.org/en/publications/Fatfrecommendations/R16-Public-Consultation-June-2026.html 는 2026-10-21 JS 챌린지(403 "Just a moment...")로 열 수 없었음. wave1 F-031 과 일치. 최종 가이던스 발간 여부 미확인(§8).
```

```
F-063
claim: FATF 는 2026-03-03 "Targeted Report on Stablecoins and Unhosted Wallets — Peer-to-Peer Transactions" 를 발간해 2025 중반 250종 이상·시총 USD 3,000억 초과를 보고하고 Chainalysis 의 "2025년 불법 VA 거래량의 84%가 스테이블코인" 추정을 인용했으며, 발행자 동결·소각·회수·상환 시 CDD·allow/deny-listing 을 모범사례로 들었다.
entity: case:fatf-stablecoin-2026
source_url: https://www.fatf-gafi.org/en/publications/Virtualassets/targeted-report-stablecoins-unhosted-wallets.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "stablecoins have expanded rapidly, with over 250 in circulation by mid-2025 and a market capitalisation exceeding USD 300 billion. Chainalysis has indicated that stablecoins accounted for 84 percent of illicit virtual asset transaction volume in 2025" / "While the FATF Standards do not require jurisdictions to adopt regulatory frameworks for stablecoin arrangements beyond those already applicable to VASPs" / "Requiring stablecoin issuers to adopt risk-based technical and governance controls, such as the ability to freeze, burn, or withdraw stablecoins in the secondary market, conduct customer due diligence at redemption, and, where appropriate, implement smart contract controls, such as allow-listing ... and deny-listing"
note: 공식 페이지 요약 기준(PDF 5 MB 미정독). 84% 는 T3 원출처를 FATF 가 인용. 7차 TU 각주 17–18 이 이 보고서를 참조.
```

```
F-064
claim: FATF 는 2026-03-11 "Understanding and Mitigating the Risks of Offshore VASPs" 를 발간해 oVASP 를 "VASPs created under the laws of one jurisdiction, with or without a physical presence, that provide services to clients residing in another jurisdiction" 으로 정의하고, 관할의 46% 만 활동기반 규제·감독 접근을 채택했다고 보고했다.
entity: case:fatf-ovasp-2026
source_url: https://www.fatf-gafi.org/en/publications/Virtualassets/Understanding-Mitigating-Risks-Offshore-VASPs.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Paris, 11 March 2026 — A new report from the Financial Action Task Force highlights how gaps in oversight of offshore Virtual Asset Service Providers (oVASPs) are exploited" / "identifies that under half (46%) of jurisdictions have adopted an activity-based approach to regulation and supervision"
note: 공식 페이지 요약. PDF https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Understanding-Mitigating-Risks-Offshore-VASPs.pdf.coredownload.inline.pdf (HEAD 200, 미정독). 사례: 나이지리아 FIU(글로벌 VASP 연계 지갑 약 USD 6억), 인도네시아 FIU(시리아 테러단체 자금), 영국 FCA(사기 사이트 1,000+ 차단), NZ VAIRG·인도 VA Sub-Group, 케이맨–ADGM 협력.
```

```
F-065
claim: FATF 는 2026-07-21 "Targeted Report on Regulatory Challenges from Decentralised Finance" 를 발간해 2021 가이던스의 DeFi 분석을 갱신·보완하고 기능적·위험기반 접근과 통제 존재 판정 권고를 제시했다.
entity: case:fatf-defi-2026
source_url: https://www.fatf-gafi.org/en/publications/Virtualassets/targeted-report-decentralised-finance-2026.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Paris, 21 July 2026 - This report updates and complements the FATF's previous analysis of Decentralised Finance (DeFi), as set out in the FATF's 2021 Updated Guidance for a Risk-Based Approach to Virtual Assets (VAs) and Virtual Asset Service Providers (VASPs)" / "effective implementation of the FATF Standards in the context of DeFi requires a functional and risk-based approach. A number of recommendations are made to help jurisdictions regulate and supervise DeFi arrangements, including to determine the existence of control."
note: PDF(5 MB) 직접 URL 은 403 — 미정독. 7차 TU 각주 1(p.4)의 DeFi 3분류와 para 48 이 이 보고서를 선행 안내.
```

```
F-066
claim: 2026-06-17~19 FATF 총회(멕시코 의장국 마지막)는 캐나다·튀르키예 5차 MER 채택, 알제리·나미비아 회색명단 해제, 보스니아헤르체고비나·이라크 편입, R.6 인도적 예외(UNSCR 2664·2761) 개정, 영국 의장국 우선순위 승인, 인도 Vivek Aggarwal 부의장 임명(2026-07~2027-06)을 결정했다.
entity: case:fatf-plenary-2026-06
source_url: https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-june-2026.html
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Paris, 19 June 2026 – The sixth and final Financial Action Task Force (FATF) Plenary meeting under the Mexican Presidency of Elisa de Anda Madrazo concluded today" / "The Plenary adopted reports of Canada and Türkiye under the new round of mutual evaluations." / "The FATF removed Algeria and Namibia from its list of jurisdictions under increased monitoring" / "At this Plenary, the FATF added Bosnia and Herzegovina and Iraq to the list"
note: `notes/2-regulations/fatf.md` §7 표의 회색명단 예시("나미비아")는 2026-06-19 해제로 구식(§9).
```

```
F-068
claim: 7차 TU 는 민간부문에 oVASP 가 소매 사용자로 위장해 개설한 계정 탐지, 고위험 관계 제한·종료, 미인가·감독취약 역외 플랫폼 연계 법정화폐 온·오프램프 모니터링, 언호스티드 지갑 고위험 활동 EDD, 프로토콜·브리지·믹서·크로스체인 노출 평가를 권고한다.
entity: case:tu7-2026
source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "iii. Conduct enhanced due diligence of oVASPs, detect accounts used by oVASPs that misrepresent themselves as retail users, restrict or exit higher-risk relationships, and monitor fiat on- and off-ramp activity linked to unlicensed or weakly supervised offshore platforms. iv. Assess risks arising from DeFi activities, including exposure to protocols, bridges, mixers, cross-chain tools"
note: 권고 6(p.5). 권고 5(ii)는 "KYC, wallet screening, blacklisting, and, where appropriate, whitelisting mechanisms as well as freezing and blocking capabilities" 를 요구. 저장소 신규 지표 후보의 1차 근거(§9).
```

---

## 5. 상충·의문점

| 쟁점 | 출처 A 주장 | 출처 B 주장 | 판단 | 재검증 방법 |
|---|---|---|---|---|
| 7차 TU 쪽수 | wave1 도시에 F-013: "35 PDF페이지, 인쇄 p.1~33" | 공식 PDF·FIAU 미러 모두 pypdf 34쪽, 마지막 본문 쪽 "31", 뒷표지 "July 2026" | **34쪽·인쇄 pp.1–31 이 맞음**(wave1 오기) | PDF 열어 쪽수 확인 |
| TR 집행 부진 비율 표현 | TU7 Key Findings p.3 "almost half of jurisdictions ... not yet having taken Travel Rule-related supervisory or enforcement action" | TU7 para 25 p.17 "Slightly more than half ... (60%; 55 of 91)" | 본문 수치(60%)가 1차; 요약 문구는 FATF 내부 불일치 | 인용 시 para 25 사용 |
| 한국 R.15 등급 | `notes/2-regulations/fatf.md`: "4차 ME 에서 가상자산 영역은 Partially Compliant" | FATF 한국 MER 페이지 등급표 "R.15 - New technologies C"; TU7 Annex A 한국 "N/A"(개정 기준 미평가) | **노트 서술 근거 없음**; 2020 MER 은 구 R.15 기준 C, 개정 기준 등급은 아직 없음 | 한국 MER 2020 PDF 기술준수 부속서 + APG/FATF 후속보고서(FUR) 재평가 여부 확인 |
| R.16 2025 개정 내용 | `fatf.md` §4: "임계값 €1~$3,000 범위 재량", "분기별 FIU 보고", "Protocol Interop 의무", "PII 보관기간 명시" | Explanatory note: de minimis "no higher than USD/EUR 1,000"(INR.16 para 8·10); 분기 보고·프로토콜 상호연결 의무 문언 없음 | **노트 서술 4건 근거 미확인** — 개정 R.16/INR.16 전문에서 재검색 필요 | 개정 R.16·INR.16 원문 전수 대조 |
| oVASP 접근 비율 | oVASP 보고서(2026-03-11): "under half (46%) of jurisdictions have adopted an activity-based approach" | TU7 para 21: "34%; 39 of 114" 가 oVASP 인가 요구 | 모집단·설문 시점·정의(활동기반 vs 역외 인가 요구)가 달라 직접 비교 불가 | oVASP 보고서 PDF 의 분모 확인 |
| DeFi 인가 비율 추이 | TU6 para 38: "48%; 47 of 99" 인가 요구(선진 99개 중) | TU7 para 46(c): "31%; 44 of 142" 완화조치 적용, 인가 부과 4개 | 질문 문항·모집단이 바뀌어 "하락" 으로 읽으면 오독 | 두 설문 문항 원문 대조(FATF 미공개) |
| 스테이블코인 불법 비중 | 2026-03-03 보고서(Chainalysis 인용) 84% | TU6 "a majority"(수치 없음); TU7 수치 없음 | FATF 자체 수치 아님 — T3 원출처 인용임을 병기 | Chainalysis 2026 Crypto Crime Report 원문 |
| 스테이블코인 발행자 열 | TU7 Annex A 머리말에 "Has required stablecoin issuers to be registered/licensed when they qualify as VASPs" 열 존재 | TU6 Annex 머리말에 해당 열 없음(grep 무결과) | 2026년판 신설로 판단 | TU6 PDF 표 머리말 육안 확인 |
| 10월 총회 일정 | FATF 일정표 2026-10-26~30 | ANI 보도 "October 28-30" | 전자는 FATF 주간(작업반 포함), 후자는 본회의 | 성과문 발간 후 확인 |

---

## 6. 출처 레지스트리

| source_id | 기관 | URL | tier | 갱신주기 | 접근 | 비고 |
|---|---|---|---|---|---|---|
| S-01 | FATF | https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf | T1 | 고정(2020-09) | 공개 | 1,132,000 B; 구 URL `/media/fatf/documents/recommendations/...` 도 200. 요약 전단 3종(`/content/dam/fatf-gafi/brochures/Handout-Red-Flags-VA-{VASP,Financial-Non-Financial,Public-Sector}.pdf`)·Quick-guide-RBA-VA-VASPS.pdf HEAD 200 |
| S-02 | FATF | https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets-red-flag-indicators.html | T1 | 고정 | 공개 | 브라우저 UA+Accept 헤더 필요(기본 UA 403) |
| S-03 | FATF | https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf | T1 | 고정(2021-10) | 공개 | 3,574,282 B, 111쪽 |
| S-04 | FATF | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html | T1 | 고지문 갱신됨 | 공개 | 2025 R.1 개정 미반영 고지 |
| S-05 | FATF | https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf | T1 | 연 1회(차기 2027) | 공개 | 3,467,117 B, 34쪽. FIAU Malta 미러(T2, 34쪽) https://fiaumalta.org/app/uploads/2026/07/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf |
| S-06 | FATF | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-updated-virtualassets-vasps-2026.html | T1 | — | 공개 | 과거 TU 링크 목록 포함(2020-07-07~2025-06-26) |
| S-07 | FATF | https://www.fatf-gafi.org/en/news/targeted-updated-va-vasps-2026.html | T1 | — | 공개 | 보도자료 |
| S-08 | FATF | https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2025-Targeted-Upate-VA-VASPs.pdf.coredownload.pdf | T1 | 고정 | 공개 | 32쪽(URL 의 "Upate" 오타 그대로) |
| S-09 | FATF | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-update-virtual-assets-vasps-2025.html | T1 | — | 공개 | — |
| S-10 | FATF | https://www.fatf-gafi.org/en/publications/Virtualassets/targeted-report-stablecoins-unhosted-wallets.html | T1 | — | 공개 | PDF 직접 URL 추정 경로 404 |
| S-11 | FATF | https://www.fatf-gafi.org/en/publications/Virtualassets/Understanding-Mitigating-Risks-Offshore-VASPs.html | T1 | — | 공개 | PDF `.../reports/Understanding-Mitigating-Risks-Offshore-VASPs.pdf.coredownload.inline.pdf` 200 |
| S-12 | FATF | https://www.fatf-gafi.org/en/publications/Virtualassets/targeted-report-decentralised-finance-2026.html | T1 | — | 공개 | PDF 직접 URL 403 |
| S-13 | FATF | https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-june-2026.html | T1 | 총회별 | 공개 | — |
| S-14 | FATF | https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Explanatory%20note%20for%20revised%20R.16.pdf.coredownload.pdf | T1 | 고정(2025-06) | 공개 | 987,485 B |
| S-15 | FATF | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/R16-Public-Consultation-June-2026.html | T1 | — | **JS 챌린지(403)** | 내용은 S-23 으로 대체 |
| S-16 | FATF | https://www.fatf-gafi.org/en/calendars/events.html | T1 | 수시 | 공개 | 총회 일정. 보도(T4) https://aninews.in/news/world/europe/first-fatf-plenary-under-uk-presidency-to-take-place-from-october-28-3020261021052640/ 는 본회의 10-28~30 |
| S-17 | FATF | https://www.fatf-gafi.org/en/publications/Mutualevaluations/Mer-korea-2020.html | T1 | 고정 | 공개 | 등급표 포함 |
| S-18 | FATF | https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Best-Practices-Travel-Rule-Supervision.pdf | T1 | 고정(2025-06) | 공개(HEAD 200) | 미정독 |
| S-20 | FATF | https://www.fatf-gafi.org/en/topics/virtual-assets.html | T1 | 수시 | 공개 | 주제 허브 |
| S-19 | FIAU Malta | https://fiaumalta.org/news/latest-updates-from-the-fatf/ | T2 | 수시 | 공개 | R.16 가이던스 의견수렴 마감일 |

---

## 7. 일일 수집 후보 (Ingestion Hooks)

| 명칭 | 방식 | 엔드포인트 | 포맷 | 갱신빈도 | 인증 | 주의 |
|---|---|---|---|---|---|---|
| FATF Virtual Assets 주제 페이지 | HTML | https://www.fatf-gafi.org/en/topics/virtual-assets.html | HTML | 발간 시 | 없음 | 2026-10-21 200 확인. **브라우저 UA + `Accept: text/html` 헤더 없으면 403**. RSS 링크 미발견(미검증) |
| FATF 뉴스 목록 | HTML | https://www.fatf-gafi.org/en/the-fatf/news.html | HTML | 수시 | 없음 | 200 확인 |
| FATF 행사 일정 | HTML | https://www.fatf-gafi.org/en/calendars/events.html | HTML(표) | 수시 | 없음 | 200 확인; 총회 날짜 추출 가능 |
| FATF 총회 성과문 | HTML | `https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-<month>-<year>.html` | HTML | 연 3회 | 없음 | 패턴은 2026-06 판으로 확인; 10월판은 미발간(404) |
| FIAU Malta "Latest Updates from the FATF" | HTML | https://fiaumalta.org/news/latest-updates-from-the-fatf/ | HTML | 수시 | 없음 | FATF 페이지 차단 시 대체 요약(T2) |

---

## 8. 미확인·다음 단계

- [ ] **R.16 이행 가이던스 최종본** — 2026-06-24 의견수렴(마감 08-21) 이후 최종 발간 여부·일자. FATF 페이지(S-15)가 JS 챌린지로 차단되어 미확인. 10월 총회(2026-10-26~30) 성과문에서 확인 필요.
- [ ] **2026년 10월 FATF 총회 성과** — 가상자산 관련 결정(VACG 산출물, MIVA, R.15 관련) 전부 미확인(미개최).
- [ ] **스테이블코인·oVASP·DeFi 타겟보고서 PDF 전문** — 본 도시에는 FATF 공식 페이지 요약만 정독. oVASP PDF 는 200 응답이므로 즉시 정독 가능; 스테이블코인 PDF 직접 URL 미확보(추정 경로 404); DeFi PDF 403. 특히 DeFi 3분류의 원문 정의와 oVASP 46% 의 분모 확인 필요.
- [ ] **Best Practices on Travel Rule Supervision(2025-06-26) 내용** — 존재만 확인(HEAD 200), 내용 미정독.
- [ ] **한국 R.15 재평가 여부** — 2020 MER 은 구 기준 "C", TU7 표는 개정 기준 "N/A". 한국 후속보고서(FUR)에서 개정 R.15 재평가가 있었는지 FATF/APG 문서로 확인. 노트 "PC" 서술의 출처도 추적.
- [ ] **`notes/2-regulations/fatf.md` §4 R.16 서술 4건**("€1~$3,000", "분기별 FIU 보고", "Protocol Interop", "PII 보관기간") 의 근거 — 개정 R.16·INR.16 전문 대조. Explanatory note 에는 없음.
- [ ] **개정 R.16 확대 정보항목**(송금인 주소·수취인 국가/도시·생년월일·BIC/LEI) — wave1 F-010 에 의존, 이번에 재확인 안 함(B).
- [ ] **Methodology Annex IV 발효 상태** — wave1 F-008 의존(B).
- [ ] **TU7 Figure 1.3(기준별 met/mostly met/partly/not met) 전수치** — pdftotext 변환이 붕괴되어 para 10·18 의 본문 수치(15.3: 48/149, 15.4: 59/149)만 사용. 나머지 기준(15.5~15.11)은 PDF 육안 판독 필요.
- [ ] **Red Flag 하위 불릿 포함 지표 총수** — 상위 58개 기준으로 집계; KB 에 등재할 때 하위 ○ 불릿(T2 3개, T3 2개, T4 3개, T5 1개, A14 2개)을 별도 지표로 분리할지 결정.
- [ ] **TU7 Annex A 표 69행의 국가명–값 전수 매칭** — 좌표 재구성으로 한국·일본·싱가포르·미국·홍콩 행은 확인했으나 전체 행 매칭은 미수행. 국가별 통계(예: 스테이블코인 열 "No" 국가 수) 산출 시 PDF 육안 대조 필요.
- [ ] **FATF 사이트 RSS/Atom 피드 존재 여부** — HTML 에서 미발견(미검증).

---

## 9. 기존 저장소 내용과의 차이·정정 제안

### 9-1. `notes/2-regulations/fatf.md`

| 위치 | 현행 서술 | 원문 확인 결과 | 제안 |
|---|---|---|---|
| §6 "한국 ME 결과", "자주 나오는 오해" | "4차 ME 에서 가상자산 영역은 **Partially Compliant**" | FATF 한국 MER 페이지 등급표 **R.15 "C"**(2020, 개정 전 기준); TU7 Annex A 한국 R.15 **"N/A"**(개정 기준 미평가) [F-058][F-056] | "2020 MER 은 2019 개정 전 R.15 기준으로 C; 개정 R.15 기준 등급은 2026-04 기준 미부여(N/A)" 로 교체. "PC" 출처가 있으면 §8 로 |
| §4 "R.16 2025-06 개정의 주요 변화" | "임계값 권고: €1~$3,000 범위 내 관할 재량", "분기별 FIU 보고", "Protocol Interop 의무", "PII 보관 기간 명시" | Explanatory note: de minimis **"no higher than USD/EUR 1,000"**; 나머지 3건 문언 없음 [F-031] | 4건 삭제 또는 근거 각주 보강. "VASP 는 R.15 경유 간접 적용(note para 54), 시한 2030년 말(para 59)" 은 유지 |
| TL;DR / §2 R.16 | "**2019년 개정**(Travel Rule 을 가상자산까지 확장)" | VA 확장은 2019-06 **INR.15 para 7(b)** 신설로 이뤄짐(R.16 본문 개정 아님) — 가이던스 para 178 "Recommendation 16 applies in an amended way to VAs as set out in paragraph 7(b) of INR.15" [F-023] | `kb/entities/regulations/intl-fatf-r15.yaml` curator_note(CTR:00002)와 정합하도록 수정 |
| §4 임계금액 표 | "FATF 권고: USD·EUR 1,000(각국 자율 결정)" | 가이던스 para 191: "may choose to adopt"(선택적 de minimis), 미달분 수집항목 명시 [F-025] | 미달분 요건(성명+지갑주소/거래참조번호, 의심 없으면 미검증) 추가 |
| §7 회색명단 예시 | "케냐, 나미비아, 필리핀 등" | 나미비아 2026-06-19 해제 [F-066] | 예시 갱신(또는 "2026-06-19 기준 22개국" 으로 wave1 참조) |
| §9 발간물 표 | "Targeted Update ... 가장 최근 2025" | 7차 2026-07-16 발간 [F-040] | 7차 추가; **Red Flag Indicators(2020-09-14)**, 스테이블코인(2026-03-03)·oVASP(2026-03-11)·DeFi(2026-07-21) 타겟보고서 추가 |
| TL;DR "2026 후반에 가이던스 발표 예정" | — | R.16 가이던스 의견수렴 2026-06-24~08-21, 최종본 미확인 [F-061] | 절대일자로 치환 + 미확인 표기 |
| 신규 | — | TU7 Annex A 한국 행: **스테이블코인 발행자 등록·인가 요구 "No"**(2026-02~06 자기보고) [F-056] | 한국 현황에 추가 — 2026-10 시행 예정 디지털자산 법제 논의와 연결 가능(별도 확인 필요) |
| 신규 | — | TU7 민간 권고 5–6(oVASP 소매 위장 탐지, unhosted EDD, 온·오프램프 모니터링) [F-068] | "그래서 회사 차원에서 뭘 해야 하나" 목록에 반영 |

### 9-2. `notes/3-crypto-aml/onchain-typology.md`

| 위치 | 현행 | 제안 |
|---|---|---|
| §1 "KYT 룰의 출발점" | 9개 유형만 언급 | **FATF Red Flag 2020 의 6범주 58지표를 공식 지표 원천으로 소개**하고, 9개 유형이 주로 익명성(A)·거래(T) 범주에 대응하며 송수신인(S)·자금원(F) 범주는 KYT 가 아닌 KYC/온보딩 룰 영역임을 명시 [F-003][F-008] |
| §6 체크리스트 10개 | "KYC 정보와 거래 패턴 불일치", "특정 국가 IP·VPN" 등 | 각 항목에 RF-ID 병기(예: smurfing→RF-T1/P6, pass-through→RF-T4, VPN→RF-A10/S2). 누락: 손실 감수 환전(RF-P7), 메모 필드 문구(RF-S18), 고령·비숙련 송금인(RF-S12/13), 식별정보 빈번 변경(RF-S16) |
| §3-C "스테이블코인 84%" | Chainalysis 2026 인용 | FATF 2026-03-03 타겟보고서가 같은 수치를 인용(T1 경유) — 출처 병기 [F-063]. TU7 의 **동결 저항형 자체 스테이블코인** 유형 추가 [F-052] |
| §3-D "DPRK Lazarus" | 2025 USD 2.02B 탈취 등 | TU6 공식 수치(Bybit USD 1.46bn, 회수 3.8%, BTC 35·ETH 125,000 지갑) 병기 [F-055]; TU7 의 **RPC 노드·멀티시그 공급자 공격**, 가스비 조달 은닉 서비스 추가 [F-054] |
| §3-E "산업화" | LaaS·CMLN | TU7 의 캄보디아 복합체 USD 4bn(2021-08~2025-01)·Operation Borrelli EUR 460m, **네스팅 oVASP 소매 위장** 유형 추가 [F-051][F-068] |
| 신규 | — | AI 악용(딥페이크 채용사기 USD 1m+, AI 에이전트 익스플로잇) [F-053] |
| §1 "Bybit 사례: 48시간 내 $160M layering" | 출처 없음 | FATF 문서에 없음 — 출처 보강 또는 삭제 |

### 9-3. `kb/entities/indicators/` (63건)

1. **증거 상향**: 모든 파일의 `evidence` 에 `DOC:intl-fatf-va-red-flags-2020`(신규 문서 노드, S-01) 을 추가하고, §3A-3 에서 "완전" 으로 매핑된 17개(`x-below-threshold-clustering`, `x-passthrough-chain`, `x-immediate-stable-then-tron`, `x-fresh-account-high-value`, `x-corp-lump-buy-immediate-withdraw`, `x-new-accounts-converge`, `x-n-to-one-consolidation`, `x-xmr-gateway-vanish`, `x-unregistered-operator-sub-limit`, `x-unregistered-service`, `x-known-mixer-exposure`, `x-device-fingerprint-reuse`, `x-high-risk-venue-direct`, `x-atm-cluster-single-recipient`, `x-deepfake-liveness-anomaly`, `x-remote-worker-triple-mismatch`, `x-unregistered-vasp-bypass`)는 confidence A + locator(인쇄 쪽·RF-ID)로 갱신. curator_note 의 "원문 미확보" 문구 삭제.
2. **신규 지표 후보(Red Flag 기반, 17건 공백)** — 제안 id: `x-loss-making-conversion`(RF-P7) · `x-proxy-domain-registration`(A9) · `x-tor-vpn-session`(A10) · `x-hardware-wallet-cross-border`(A8) · `x-stolen-funds-address-deposit`(T5) · `x-staggered-interval-ransom-pattern`(T2-b) · `x-sanctioned-jurisdiction-ip`(S2) · `x-kyc-refusal-source-of-funds`(S5) · `x-counterparty-knowledge-gap`(S6) · `x-address-on-illicit-forum`(S10) · `x-adverse-public-record`(S11) · `x-tech-unfamiliar-sender`(S12) · `x-elderly-high-frequency`(S13) · `x-financially-vulnerable-account`(S14) · `x-credential-churn-ato`(S16) · `x-illicit-memo-language`(S18) · `x-wealth-from-va-ico-only`(F7). `signal_type` 은 대부분 "behavioural"/"kyc" 로 새 분류 필요.
3. **신규 지표 후보(2026 FATF 문서 기반)** — `x-nested-ovasp-retail-misrepresentation`(TU7 para 41, 권고 6-iii) · `x-freeze-resistant-stablecoin-exposure`(TU7 para 35) · `x-gas-fee-funding-obfuscation`(TU7 para 33) · `x-dormant-account-stablecoin-passthrough`(TU6 para 35 "dormant accounts and transactions depositing and withdrawing stablecoins at a VASP without trading activity") · `x-micro-split-rotating-address-tf`(TU7 para 36).
4. **`fp_risk` 재검토**: Red Flag 원문이 단독 신호 약함을 명시한 지표(ATM 단일 이용 RF-A14, 하드웨어 지갑 RF-A8)는 `fp_risk: high` 로 상향 권고.
5. **문서 노드 추가 제안**: `DOC:intl-fatf-va-red-flags-2020`, `DOC:intl-fatf-vasp-guidance-2021`, `DOC:intl-fatf-tu7-2026`, `DOC:intl-fatf-stablecoin-unhosted-2026`, `DOC:intl-fatf-ovasp-2026`, `DOC:intl-fatf-defi-2026`(각 S-01~S-12 URL·발간일·쪽수 포함).

6. **`_research/wave1/fatf-intl-standards.md` 정정**: F-013 note "35 PDF페이지, 인쇄 p.1~33" → "34 PDF페이지, 인쇄 pp.1–31"; F-035 에 "147개 관할 응답(FATF 38 + FSRB 109), 무응답 58/205" 추가 [F-040][F-041].
