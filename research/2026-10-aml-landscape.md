---
dossier_id: 2026-10-aml-landscape
title: 글로벌·한국 가상자산 AML/CFT 규제 지형 — 2026-07-30 이후 변경분 중심 (기준일 2026-10-21)
domain: regulation
as_of: 2026-10-21
coverage: FATF · EU(AMLR/AMLA/MiCA/TFR) · 영국 · 미국(FinCEN/OFAC/GENIUS/CLARITY/DOJ) · 한국(특금법·시행령·신고매뉴얼·2단계 입법·법인계좌·검사) · 일본·싱가포르·홍콩·UAE·호주·인도 · 2026년 발간 범죄 통계(Chainalysis·TRM·Elliptic)
confidence_overall: B
sources_total: 58
---

> **읽는 법.** 이 도시에는 `_research/wave1/*.md`(기준일 2026-07-30)의 **후속편**이다. 2026-07-30 이전에 확정된 사실은 반복하지 않고 "무엇이 바뀌었나"만 쓴다. 바뀌지 않은 핵심 날짜(AMLR 2027-07-10, R.16 이행시한 2030년 말, MiCA 경과규정 종료 2026-07-01 등)는 비교를 위해 한 줄로만 재확인한다. 웹 검색 쿼터가 세션 중 소진되어 후반부는 **직접 URL 열기(WebFetch)·공식 PDF 다운로드**로만 검증했다. FATF 공식 사이트는 자동 수집기에 403을 돌려주어 미러(FIAU Malta PDF)·2차 보도로 보강했으며 그 경우 tier/confidence 를 낮춰 적었다.

---

## 1. BLUF — 핵심 결론

- **FATF 10월 총회는 아직 열리지 않았다.** 영국 의장국(Giles Thomson) 첫 총회가 **2026-10-28~30 파리**에서 열리고, 결과는 10-30 17:00 CEST 기자회견 이후 공표된다. 따라서 **2026-10-21 기준 현행 회색명단은 2026-06-19 판 22개 관할**(BiH·이라크 신규, 알제리·나미비아 졸업), 흑색명단은 북한·이란·미얀마 3개 그대로다. [F-001][F-002][F-003]
- **FATF 7차 Targeted Update(2026-07-16)의 헤드라인 수치**: 2026-04 기준 149개 평가 관할 중 R.15 **LC 34%(51)·PC 43%(64)·NC 22%(33)·C 1개**; 트래블룰 입법 **83%(91/109)**(2025년 73%, 85/117); 입법 관할 중 **60%(55/91)는 트래블룰 감독·집행 경험이 없음** — 다만 같은 보고서 요약문은 "almost half"로 표현해 **문서 내부 불일치**가 있다. 역외 VASP에 인가·등록을 요구하는 관할은 **34%(39/114)**. [F-004]~[F-008]
- **개정 R.16 이행 가이던스는 2026-06-24~08-21 공개 의견수렴을 마쳤고, 2026-10-21 기준 최종본은 미발간**이다. 이행 시한(2030년 말)과 평가방법론 미발효 상태는 변함없다. [F-009]
- **EU: AML 규칙제정 주체가 EBA→AMLA로 넘어갔고(2026-01-01), AMLA는 2026-10-01 AMLR 최초 RTS 3건(CDD §28(1)·거래관계 기준 §19(9)·그룹 요건 §16(4)/17(3)) 최종안을 집행위에 제출**했다. 2026-10-07에는 집행위 MiCA 재검토 의견수렴에 AML 우선과제 5개(스테이킹·대출, DeFi 통제자 정의, 무인가 스테이블코인, ART 발행자, 국경간 감독)를 제출했다. AMLR 적용개시 2027-07-10은 그대로다. [F-010]~[F-013]
- **ESMA 임시 CASP 등록부(2026-10-19 갱신)는 379행·376개 고유 LEI**로, 2026-07-30 시점(345행) 대비 약 +34행. 독일 109·프랑스 36·네덜란드 29·키프로스 25·몰타 23 순. 인가 종료 기록은 2건뿐이다. [F-014]
- **영국은 FSMA 인가 신청창을 2026-09-30 열었다(FCA 안내: 신청기간 2026-09-30~2027-02-28, 신체계 2027-10-25 시행 예정).** MLR 등록 누적 처리 391건 중 등록 17%·철회 67%·반려 12%·거부 4%(2026-08-01 기준). [F-015][F-016]
- **미국은 "제안은 늘고 확정은 없는" 상태다.** 재무부가 **GENIUS Act §3 NPRM(발행·제공·판매 범위, RIN 1505-AC95)을 2026-08-18 연방관보 게재, 의견 2026-10-19 마감**; 법 시행은 법정 최종기한 **2027-01-18**로 예상. 2026-07-16 기준 GENIUS 하위 NPRM 10건 이상이 전부 **proposed**이고 최종규칙은 0건. FinCEN AML/CFT 프로그램 규칙(2026-04 NPRM)도 2026-10-19까지 최종화 흔적이 없다. [F-017]~[F-020]
- **FinCEN은 2026-10-05 가상자산 제안규칙 2건을 공식 철회**했다 — CVC 믹싱 §311 NPRM(88 FR 72701)과 비수탁지갑 NPRM(85 FR 83840). 연방관보 철회 공고는 2026-10-06 게재. 사유는 "chilling effect on legitimate activity" 및 "deregulatory agenda". 같은 주 **A7 네트워크(러시아 A7A5·Garantex·Grinex 계열) 하위대리인 거래에 자금이체 금지 특별조치를 제안**(RIN 1506-AB77, 2026-10-05 관보, 의견 30일)했다 — 믹서 규제는 접고 러시아·이란 제재회피망 차단은 강화하는 비대칭. [F-021]~[F-024]
- **OFAC 2026 가상자산 제재의 축은 이란이다.** "Operation Economic Outcast"(2026-08-24 개시) 아래 2026-09-17 이란 거래소 BitBank·개발사 Pishtaz Simorgh·개인 3인을 E.O. 13902로 지정(2026-06~07 수억 달러 BTC를 IRGC로 이전 주장). 2026-10-01에는 A7 네트워크를 초국가범죄조직으로 지정. [F-025][F-026]
- **CLARITY Act(H.R. 3633)는 2026-09-15 상원 본회의 진행동의안 토론종결 표결에서 49-50으로 부결**(60표 필요). 법안은 상원 캘린더에 남아 재표결 가능하나 10월 선거 휴회로 2026년 내 처리 가능성은 낮다. **Tornado Cash 개발자 Storm 재심은 2027-04-26으로 연기**. [F-027][F-028]
- **한국: 개정 특금법(법률 제21358호)이 2026-08-20 시행에 들어갔고, 시행령 개정안은 2026-08-11 국무회의를 통과**했다. 핵심: 대주주 범위 확대(대표이사·이사 과반 선임 주주, 법인 최대주주의 최대주주·대표자), 불수리 요건(부채비율 200% 이하·사회적 신용·조직인력·전산·내부통제), **트래블룰 기준금액 100만원 폐지 → 전 거래**, 해외 VASP·개인지갑 이전 위험도별 차등, 1천만원 이상 자체 의심거래 관리체계. **단, 시행 시점이 둘로 갈린다**: 신고제·퇴직자 제재통보는 2026-08-20, **트래블룰 등 그 외는 "공포 후 6개월"** — 공포일을 확인하지 못했으므로 100만원 기준은 2026-10-21 기준 **아직 유효(amended, not yet in force)**로 다뤄야 한다. [F-029]~[F-033]
- **신고매뉴얼 전면 개정(2026-08-13)**: AML 전담인력 4인 이상, 전산설비 국내 소재(클라우드 국내 리전 인정), 대주주·법령준수체계 변경은 **30일 전 사전신고**. 기존 28개사는 **2026-11-20까지 재신고**(언론 보도 기준, T4) 대상이며 FIU가 44개 심사항목 현장점검 중. [F-034][F-035]
- **한국 2단계 입법(디지털자산기본법)은 2026-10-21 기준 정부안 미제출·의원안 10건 계류(proposed)**. 2026-10-08 국정감사에서 금융위원장은 "준비해 놓았고 막바지 협의"라고만 답했고 원화 스테이블코인 발행주체는 미결. **법인 실명계좌 2단계(상장사·전문투자법인)도 미시행**(마지막 공식 언급 없음, 2026-05-19 보도 기준 지연). [F-036]~[F-038]
- **한국 감독 지표(2026-10-01 '26 상반기 실태조사)**: 조사대상 26개(거래소 17·지갑 9, 신고 28개 중 2개 미제출), 평가총액 58.9조(-33%), 일평균 거래 3.1조(-44%), **총 출고 62.8조 중 트래블룰 적용 9.5조(≈15%)**, AML 인력 213/2,021명. 미신고 사업자 **인터넷 사이트 27건 접속차단(2026-10-13), 수사기관 통보 누적 44개**. 2026-07~10월 FIU의 신규 과태료·영업정지 보도자료는 없다. [F-039]~[F-041]
- **아시아**: 일본은 암호자산을 금상법으로 옮기는 개정법이 **2026-07-15 성립·07-23 공포(令和8年法律第64号, T4)**, 이관 조항 시행은 **공포 후 1년 이내 정령 지정일(≤2027-07-23)**로 **enacted-not-in-force**. 싱가포르 MAS는 **2026-09-01 PSA 개정 스테이블코인 체계 의견수렴(10-16 마감, proposed)**. 홍콩 VATP 인가는 **13개(2026-10-16 기준, 2026-05-18 NewBX가 최신)**, 스테이블코인 발행 인가는 **2개(Anchorpoint·HSBC, 2026-04-10)** 그대로. 인도 FIU-IND는 2026-09-09 역외 VDA 사업자 15곳에 PMLA 위반 통지·앱/URL 차단 요구. [F-042]~[F-049]
- **정량 지형(2025년 실적, 2026-01 발간)**: Chainalysis **≥USD 154bn**(2024 수정치 57.2bn 대비 +162%, 스테이블코인 84%, 북한 탈취 USD 2bn) vs TRM **USD 158bn**(2024 64.5bn 대비 +145%, 전체 온체인의 1.2%, 북한 USD 1.92bn, 해킹 USD 2.87bn, 제재 관련 USD 93bn 중 A7A5 ≈72bn). 두 수치는 **방법론·분모·2024 기준치가 달라 직접 비교 불가**. [F-050]~[F-053]

---

## 2. 엔티티 목록

| entity_id | 명칭(원어/한글) | 유형 | 관할 | 상태 | 발효/최신일 | 근거 |
|---|---|---|---|---|---|---|
| org:fatf-plenary-oct-2026 | FATF Plenary, October 2026 (UK Presidency 1st) | 회의 | 글로벌 | scheduled | 2026-10-28~30 | F-001 |
| reg:fatf-grey-list-2026-06 | Jurisdictions under Increased Monitoring – 19 June 2026 | 성명 | 글로벌 | in-force (현행) | 2026-06-19 | F-002 |
| reg:fatf-black-list-2026-06 | High-Risk Jurisdictions subject to a Call for Action – 19 June 2026 | 성명 | 글로벌 | in-force | 2026-06-19 | F-003 |
| doc:fatf-tu7-2026 | Seventh Targeted Update on Implementation of the FATF Standards on VAs/VASPs | 보고서 | 글로벌 | published | 2026-07-16 | F-004 |
| reg:fatf-r16-guidance-draft | Draft Guidance on Payment Transparency (R.16) | 가이던스 초안 | 글로벌 | proposed (의견수렴 종료) | 2026-06-24 / 마감 2026-08-21 | F-009 |
| org:eu-amla | Anti-Money Laundering Authority (AMLA) | 기관 | EU | operating; RTS 제출 | 2026-10-01 | F-010~F-013 |
| reg:eu-amlr-rts-cdd | Draft RTS on Customer Due Diligence, AMLR Art. 28(1) | RTS 최종안 | EU | submitted-to-Commission | 2026-10-01 | F-011 |
| reg:eu-amlr-rts-19-9 | Draft RTS on business relationships/occasional transactions, AMLR Art. 19(9) | RTS 최종안 | EU | submitted-to-Commission | 2026-10-01 | F-011 |
| reg:eu-amlr-rts-group | Draft RTS on group-wide requirements, AMLR Art. 16(4)/17(3) | RTS 최종안 | EU | submitted-to-Commission | 2026-10-01 | F-011 |
| doc:eu-amla-mica-review-response | AMLA response to Commission targeted consultation on MiCA review | 의견서 | EU | published | 2026-10-07 | F-013 |
| reg:eu-amlr | Regulation (EU) 2024/1624 (AMLR) | 규정 | EU | enacted-not-in-force | 적용개시 2027-07-10 | wave1 F-013 |
| data:esma-casp-register | ESMA interim MiCA register – CASPS.csv | 등록부 | EU | live (weekly) | 2026-10-19 | F-014 |
| reg:uk-fsma-cryptoassets-2026 | FSMA 2000 (Cryptoassets) Regulations 2026 (SI 2026/102) | 규정 | UK | enacted-not-in-force (인가창 개설) | 신청 2026-09-30~2027-02-28 / 시행 2027-10-25 | F-015 |
| reg:us-genius-s3-nprm | GENIUS Act Regulations on Payment Stablecoin Issuance, Offer, and Sale (RIN 1505-AC95) | NPRM | US | proposed | 관보 2026-08-18 / 의견 2026-10-19 | F-017 |
| reg:us-genius-act | GENIUS Act, Pub. L. 119-27 | 법률 | US | enacted-not-in-force | 서명 2025-07-18 / 예상 시행 2027-01-18 | F-018 |
| reg:us-fincen-aml-program-nprm | AML/CFT Programs NPRM (91 FR 18704) | NPRM | US | proposed (의견 마감 2026-06-09) | 2026-04-10 | F-020 |
| reg:us-fincen-cvc-mixing-311 | CVC Mixing §311 NPRM (88 FR 72701) | NPRM | US | **withdrawn** | 철회 관보 2026-10-06 | F-021 |
| reg:us-fincen-unhosted-wallet-nprm | Requirements for Certain Transactions Involving CVC or Digital Assets (85 FR 83840) | NPRM | US | **withdrawn** | 철회 관보 2026-10-06 | F-022 |
| reg:us-fincen-a7-special-measure | Special Measure Prohibiting Transmittal of Funds – A7 Network Sub-Agents (RIN 1506-AB77) | NPRM | US | proposed | 관보 2026-10-05 / 의견 30일 | F-024 |
| case:ofac-bitbank-2026-09-17 | OFAC designation – BitBank, Pishtaz Simorgh, 3 individuals (E.O. 13902) | 제재 | US | in-force | 2026-09-17 | F-025 |
| case:ofac-a7-network-2026-10-01 | OFAC designation – A7 Network as TCO (E.O. 13581) | 제재 | US | in-force | 2026-10-01 | F-026 |
| reg:us-clarity-act-hr3633 | Digital Asset Market Clarity Act (H.R. 3633) | 법안 | US | proposed (상원 토론종결 부결) | 2026-09-15 | F-027 |
| case:us-v-storm-retrial | United States v. Storm – 재심 | 형사 | US | pending | 재심 2027-04-26 | F-028 |
| reg:kr-tfia-21358 | 특정 금융거래정보의 보고 및 이용 등에 관한 법률(법률 제21358호) | 법률 | KR | **in-force** (신고제·퇴직자 부분) | 2026-08-20 | F-029 |
| reg:kr-tfia-sd-2026 | 특정금융정보법 시행령 개정안(2026-08-11 국무회의) | 대통령령 | KR | enacted; 시행 분리(8-20 / 공포+6개월) | 2026-08-11 의결 | F-030~F-033 |
| doc:kr-vasp-manual-2026 | 가상자산사업자 신고매뉴얼(2026-08-20 시행 기준) | 매뉴얼 | KR | in-force | 2026-08-13 공표 | F-034 |
| reg:kr-digital-asset-basic-act | (가칭)디지털자산기본법 / 가상자산 2단계 입법 | 법안 | KR | proposed (의원안 10건 계류, 정부안 미제출) | 2026-10-08 국감 기준 | F-036 |
| doc:kr-vasp-survey-2026h1 | '26년 상반기 가상자산사업자 실태조사 결과 | 통계 | KR | published | 2026-10-01 | F-039 |
| case:kr-unregistered-site-block-2026-10 | 미신고 가상자산사업자 사이트 27건 접속차단 | 행정조치 | KR | in-force | 2026-10-13 | F-040 |
| case:kr-dunamu-suspension-litigation | 두나무 영업일부정지 처분 취소소송(1심) | 행정소송 | KR | 1심 원고승(보도) | 2026-04-09 | F-041 |
| reg:jp-fiea-psa-amendment-2026 | 金融商品取引法及び資金決済に関する法律の一部を改正する法律(令和8年法律第64号) | 법률 | JP | enacted-not-in-force (암호자산 이관부) | 성립 2026-07-15 / 공포 2026-07-23 / 시행 ≤2027-07-23 | F-042 |
| reg:sg-psa-stablecoin-amendments | MAS Consultation Paper on Proposed Amendments to the PSA 2019 for Stablecoins Regulation | 의견수렴 | SG | proposed | 2026-09-01 / 마감 2026-10-16 | F-044 |
| data:hk-sfc-vatp-list | SFC List of licensed VATP operators | 등록부 | HK | live | 2026-10-16 | F-046 |
| data:hk-hkma-stablecoin-register | HKMA Register of Licensed Stablecoin Issuers | 등록부 | HK | live | 2026-04-23 | F-047 |
| reg:ae-cma-va-framework-2026 | UAE 연방 CMA Virtual Assets Framework (3→8 활동) | 규정 | AE | in-force (2026-04, 보도) | 2026-04 | F-048 |
| case:in-fiu-ind-15-vda-notices | FIU-IND notices to 15 offshore VDA SPs (PMLA) | 행정조치 | IN | in-force | 2026-09-09 | F-049 |
| doc:chainalysis-ccr-2026 | Chainalysis 2026 Crypto Crime Report (introduction) | 보고서 | 글로벌 | published | 2026-01-08 | F-050 |
| doc:trm-ccr-2026 | TRM Labs 2026 Crypto Crime Report | 보고서 | 글로벌 | published | 2026-01-28 | F-051 |

---

## 3. 타임라인 (2026-07-30 이후 중심; 비교용 선행 사건은 ▸ 표시)

| 일자(YYYY-MM-DD) | 사건 | 관할 | 중요도 | 근거 |
|---|---|---|---|---|
| ▸ 2026-01-01 | EU AML/CFT 규칙제정·가이던스 권한 EBA→AMLA 이관(기존 EBA 가이드라인은 대체 전까지 유효, AMLAR Art. 54) | EU | H | F-010 |
| ▸ 2026-01-08 | Chainalysis 2026 Crypto Crime Report — 2025 불법 수취 ≥USD 154bn | 글로벌 | H | F-050 |
| ▸ 2026-01-28 | TRM Labs 2026 Crypto Crime Report — 2025 불법 USD 158bn, 1.2% | 글로벌 | H | F-051 |
| ▸ 2026-04-07/10 | FinCEN AML/CFT Programs NPRM(관보 04-10, 의견 06-09 마감) | US | H | F-020 |
| ▸ 2026-04-09 | 서울행정법원, 두나무 영업일부정지 처분 취소소송 1심 원고승(보도) | KR | H | F-041 |
| ▸ 2026-04-10 | HKMA 스테이블코인 발행 인가 2건(Anchorpoint FRS01·HSBC FRS02) | HK | H | F-047 |
| ▸ 2026-05-18 | SFC, NewBX Limited(Bixin.com) VATP 인가 — 13번째 | HK | M | F-046 |
| ▸ 2026-06-19 | FATF 6월 총회 종료 — 회색명단 22개(BiH·이라크 편입, 알제리·나미비아 졸업), 흑색 3개 유지, 캐나다·튀르키예 MER 채택 | 글로벌 | H | F-002, F-003 |
| ▸ 2026-06-24 | 개정 R.16 이행 가이던스 공개의견수렴 개시 | 글로벌 | M | F-009 |
| ▸ 2026-07-01 | 호주 가상자산 트래블룰 의무 적용 개시; AUSTRAC VASP 등록부 공개(06-30) | AU | H | F-048b |
| ▸ 2026-07-15 | 일본 금상법·자금결제법 개정법 성립 | JP | H | F-042 |
| ▸ 2026-07-16 | FATF 7차 Targeted Update 발간 | 글로벌 | H | F-004 |
| ▸ 2026-07-23 | 일본 개정법 공포(令和8年法律第64号, T4) | JP | H | F-042 |
| ▸ 2026-07-29 | 금융위원장 정무위 업무보고 — 디지털자산기본법 정부안 "조만간" 제출, 10개 법안 계류 | KR | M | F-036 |
| **2026-08-01** | FCA MLR 등록 누적 통계 기준일(391건 처리, 등록 17%) | UK | M | F-016 |
| **2026-08-11** | **특정금융정보법 시행령 개정안 국무회의 의결** — 대주주 확대·불수리 요건·트래블룰 기준금액 폐지·개인지갑 차등 | KR | H | F-030~F-033 |
| **2026-08-13** | FIU·금감원, 가상자산사업자 신고매뉴얼 전면 개정 공표·설명회(신고 28개사 등 100여 명) | KR | H | F-034 |
| **2026-08-18** | **재무부 GENIUS Act §3 NPRM 연방관보 게재**(RIN 1505-AC95, 의견 60일 → 2026-10-19) | US | H | F-017 |
| **2026-08-20** | **개정 특금법(법률 제21358호) 시행** — 신고제 강화·퇴직자 제재통보 부분 | KR | H | F-029 |
| **2026-08-21** | 개정 R.16 가이던스 의견수렴 마감 | 글로벌 | M | F-009 |
| **2026-08-24** | 재무부 "Operation Economic Outcast" 개시(Economic Fury 후속) | US | M | F-025 |
| **2026-08-25(경)** | SDNY, Storm 재심을 2027-04-26로 연기(명령 "entered Tuesday", 보도 08-26) | US | M | F-028 |
| **2026-09-01** | MAS, PSA 2019 개정 스테이블코인 규제 의견수렴 개시 | SG | H | F-044 |
| **2026-09-09** | FIU-IND, 역외 VDA 사업자 15곳에 PMLA 위반 통지·앱/URL 차단 요구 | IN | M | F-049 |
| **2026-09-14** | FIU, 재신고 대비 현장점검 착수 보도(기존 28개사 2026-11-20까지 재신고) | KR | M | F-035 |
| **2026-09-15** | **CLARITY Act 상원 토론종결(진행동의안) 49-50 부결** | US | H | F-027 |
| **2026-09-17** | **OFAC, 이란 거래소 BitBank·Pishtaz Simorgh·3인 지정(E.O. 13902)** | US | H | F-025 |
| **2026-09-23** | 금융위 제16차 정례회의 — 가상자산 불공정거래 4건 고발·통보 | KR | M | F-039b |
| **2026-09-26** | 빗썸 영업일부정지(6개월) 기간 종료일(2026-03-27 개시) | KR | L | wave1 F-016 |
| **2026-09-30** | **FCA 가상자산 FSMA 인가 신청기간 개시**(~2027-02-28) | UK | H | F-015 |
| **2026-10-01** | **AMLA, AMLR 최초 RTS 3건 최종안 집행위 제출** | EU | H | F-011 |
| **2026-10-01** | 금융위·FIU '26년 상반기 가상자산사업자 실태조사 결과 발표 | KR | H | F-039 |
| **2026-10-01** | OFAC, A7 Network 초국가범죄조직 지정; FinCEN 동일자 A7 하위대리인 자금이체 금지 특별조치 NPRM 발표 | US | H | F-024, F-026 |
| **2026-10-05** | **FinCEN, CVC 믹싱 §311 NPRM·비수탁지갑 NPRM 철회 발표**(관보 10-06) | US | H | F-021, F-022 |
| **2026-10-05** | A7 특별조치 NPRM 연방관보 게재(RIN 1506-AB77, 의견 30일) | US | M | F-024 |
| **2026-10-06~07** | 방송미디어통신심의위, FIU 요청 미신고 사업자 사이트 27건 접속차단 심의 | KR | M | F-040 |
| **2026-10-07** | AMLA, 집행위 MiCA 재검토 의견수렴에 AML/CFT 우선과제 5개 제출; EU 단일 AML/CFT DB 기술기준 의견수렴 | EU | M | F-013 |
| **2026-10-08** | 정무위 국정감사 — 금융위원장 "디지털자산기본법·스테이블코인 준비 완료, 막바지 협의" | KR | H | F-037 |
| **2026-10-13** | 금융위·FIU 미신고 사업자 사이트 27건 차단 공표(수사기관 통보 누적 44개) | KR | M | F-040 |
| **2026-10-16** | SFC VATP 명단 갱신(인가 13·심사 5·철회/반려 18) | HK | M | F-046 |
| **2026-10-16** | MAS 스테이블코인 의견수렴 마감 | SG | M | F-044 |
| **2026-10-19** | GENIUS §3 NPRM 의견 마감; ESMA CASP 등록부 갱신(379행) | US/EU | M | F-017, F-014 |
| **2026-10-21** | FATF 10월 총회 예고 보도(ANI/Tribune) — 10-28~30 파리 | 글로벌 | H | F-001 |
| 2026-10-28~30 (예정) | **FATF 총회(영국 의장국 첫 회의)** — 회색명단 갱신, 멕시코·미국 MER 논의 | 글로벌 | H | F-001 |
| 2026-11-20 (예정) | 기존 가상자산사업자 재신고 기한(보도 기준, T4) | KR | H | F-035 |
| 2027-01-18 (예정) | GENIUS Act 법정 최종 시행일(규칙 미완료 시) | US | H | F-018 |
| 2027-02-28 (예정) | FCA 인가 신청기간 종료 | UK | H | F-015 |
| ~2027-02 (추정 불가) | 특금법 시행령 "그 외 부분"(트래블룰 기준금액 폐지 등) 시행 — 공포 후 6개월, **공포일 미확인** | KR | H | F-033 |
| 2027-04-26 (예정) | Storm 재심 개시 | US | M | F-028 |
| 2027-07-10 (예정) | AMLR 적용개시 | EU | H | wave1 |
| ≤2027-07-23 (예정) | 일본 암호자산 금상법 이관 조항 시행(정령 지정일) | JP | H | F-042 |
| 2027-10-25 (예정) | 영국 가상자산 신체계 시행 | UK | H | F-015 |
| 2028-07-18 (예정) | GENIUS: 디지털자산서비스제공자의 비허가 스테이블코인 취급 금지 개시 | US | M | F-018 |

---

## 4. 원자적 사실 (Atomic Facts)

### 4.1 FATF

```
F-001
claim: FATF 2026년 10월 총회(영국 의장국 Giles Thomson 체제 첫 총회)는 2026-10-28~30 파리에서 열리며, 결과 요약은 회의 종료 후 FATF 웹사이트에 게재되고 10-30 17:00 CEST 가상 기자회견이 예정되어 있다. 따라서 2026-10-21 기준 10월 총회 결과(회색명단 갱신)는 존재하지 않는다.
entity: org:fatf-plenary-oct-2026
source_url: https://www.tribuneindia.com/news/world/first-fatf-plenary-under-uk-presidency-to-take-place-from-october-28-30/
publisher: The Tribune (ANI 전재), Paris dateline
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "will take place from October 28 to 30" / "A summary of the Plenary outcomes will be published on the FATF website following the conclusion of the meeting."
note: 보도는 의제로 사기(fraud) 로드맵, 멕시코·미국 상호평가보고서 논의, "jurisdictions under increased monitoring" 진행상황 검토를 명시. 가상자산 의제는 언급 없음. FATF 공식 캘린더 페이지는 수집기 403으로 미확인.
```

```
F-002
claim: 2026-06-19 FATF 총회에서 보스니아헤르체고비나·이라크가 회색명단(Jurisdictions under Increased Monitoring)에 추가되고 알제리·나미비아가 제외되어, 2026-10-21 현재 유효한 회색명단은 22개 관할이다: 앙골라, 볼리비아, BiH, 불가리아, 카메룬, 코트디부아르, DR콩고, 아이티, 이라크, 케냐, 쿠웨이트, 라오스, 레바논, 모나코, 네팔, 파푸아뉴기니, 남수단, 시리아, 베네수엘라, 베트남, 영국령 버진아일랜드, 예멘.
entity: reg:fatf-grey-list-2026-06
source_url: https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-june-2026.html ; https://amluae.com/fatf-grey-list-countries-update-19th-june-2026/
publisher: FATF(총회 결과문, 편입·졸업 사실) / AML UAE(22개 전체 명단, 2차)
tier: T2 (FATF 결과문) / T4 (명단 재구성)
confidence: B
retrieved: 2026-10-21
quote: "At this Plenary, the FATF added Bosnia and Herzegovina and Iraq to the list of jurisdictions under increased monitoring." / "the Plenary congratulated Algeria and Namibia ... will no longer be subject to the FATF's increased monitoring process."
note: 22개 전체 명단은 FATF 원문 페이지가 수집기에 403을 돌려주어 2차 출처로 재구성했다. wave1 F-019(T1)와 숫자·변경내역이 일치. 가상자산 관련 지적을 받은 회색명단 관할(불가리아·이라크·베트남·BVI)은 wave1 F-021 참조.
```

```
F-003
claim: 2026-06-19 기준 흑색명단(High-Risk Jurisdictions subject to a Call for Action)은 북한·이란(대응조치 요구)·미얀마(강화된 고객확인 요구) 3개로 변동이 없다.
entity: reg:fatf-black-list-2026-06
source_url: https://complyadvantage.com/insights/fatf-plenary-june-2026-outcomes/
publisher: ComplyAdvantage
tier: T4
confidence: B
retrieved: 2026-10-21
quote: "continues to consist of the Democratic People's Republic of Korea, Iran, and Myanmar"
note: FATF 결과문(F-002 URL)도 "updated its statements on ... jurisdictions subject to a call for action"이라고만 하고 구성 변경을 언급하지 않음 — 변동 없음과 정합.
```

```
F-004
claim: FATF 7차 Targeted Update(2026-07-16)에 따르면 2026-04 기준 149개 관할이 R.15 기술적 이행평가를 받았고, LC 34%(51개)·PC 43%(64개)·NC 22%(33개)이며 C는 2025년과 같이 1개다. 2025년(138개 기준)은 LC 29%(40)·PC 50%(68)·NC 21%(29)였다.
entity: doc:fatf-tu7-2026
source_url: https://fiaumalta.org/app/uploads/2026/07/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF (FIAU Malta 미러 PDF; 원 공표 페이지 https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-updated-virtualassets-vasps-2026.html)
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "As of April 2026, 149 jurisdictions have been assessed ... The proportion of jurisdictions that are largely compliant (LC) increased from 29% (40 of 138 jurisdictions) in 2025 to 34% (51 of 149 jurisdictions) in 2026"
note: 로컬 텍스트 추출(pdftotext)로 확인. wave1 F-013과 동일 수치.
```

```
F-005
claim: 2026년 FATF 설문(147개 관할 응답: FATF 회원 38·FSRB 회원 109)에서 트래블룰 입법을 완료한 관할은 83%(91/109)로 2025년 73%(85/117)에서 상승했고, 추가로 11/109가 입법 진행 중이다.
entity: doc:fatf-tu7-2026
source_url: https://fiaumalta.org/app/uploads/2026/07/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "For the 2026 survey, 83% of respondents (91 of 109 jurisdictions) have passed legislation implementing the Travel Rule ... up from 73% (85 of 117) in 2025."
note: 분모 109는 "VASP를 규제하지 않는 관할은 트래블룰 질문을 받지 않음"에 따른 것. 미응답 58/205 관할은 미진전으로 추정 처리됨(보고서 각주 4).
```

```
F-006
claim: 트래블룰 입법을 완료한 91개 관할 중 60%(55/91)는 트래블룰 관련 감독 조치·지시·집행을 아직 하지 않았다 — 보고서 본문 수치. 그러나 같은 보고서의 요약문은 이를 "almost half"로 표현한다(내부 불일치).
entity: doc:fatf-tu7-2026
source_url: https://fiaumalta.org/app/uploads/2026/07/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T2
confidence: A
retrieved: 2026-10-21
quote: 본문 §25 "Slightly more than half of the 91 jurisdictions (60%; 55 of 91) that have passed legislation implementing the Travel Rule have not yet issued findings or directives or taken enforcement or other supervisory actions" / 요약 "almost half of jurisdictions that have introduced Travel Rule legislation not yet having taken Travel Rule-related supervisory or enforcement action."
note: 2차 보도(규제 뉴스레터)들은 요약문의 "almost half"를 그대로 옮긴다. 인용 시 본문 60%(55/91)를 기준으로 하고 요약문 표현을 병기할 것. §5 상충 C-01.
```

```
F-007
claim: 인가·등록 체계를 둔 114개 관할 중 34%(39/114)는 자국에 설립·소재하지 않은 역외 VASP에도 일정 요건 충족 시 인가·등록을 요구하는 확장형 접근을 취한다. 인가·등록을 요구하는 95개 관할 중 81%(77/95)가 검사, 71%(67/95)가 집행·행정조치를 했다고 응답했다.
entity: doc:fatf-tu7-2026
source_url: https://fiaumalta.org/app/uploads/2026/07/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "Approximately a third of jurisdictions (34%; 39 of 114) reported taking a more extensive approach by requiring offshore VASPs ... to be licensed/registered" / "conducting supervisory inspections of VASPs (81%; 77 of 95) and taking enforcement actions or other administrative actions against VASPs (71%; 67 of 95)"
note: 위험평가 실시 86%(124/145, 2025년 76%), 규제접근 결정 89%(128/144), 허용 66%(95/144)·금지 23%. DeFi: 31%(44/142)가 위험경감조치 적용, 인가·등록 요구 4개, 실제 인가·등록 2개.
```

```
F-008
claim: 7차 TU는 캄보디아 소재 금융서비스 복합그룹이 2021~25년 최소 USD 40억의 불법수익을 세탁했고 그중 최소 USD 3,700만이 북한 사이버 탈취 자금으로 귀속된다고 기술하며, 스페인 Operation Borrelli(2025-06)에서 EUR 4.6억·피해자 5,000명 이상 사례를 든다.
entity: doc:fatf-tu7-2026
source_url: https://fiaumalta.org/app/uploads/2026/07/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf
publisher: FATF
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "a Cambodia-based financial services conglomerate laundered at least USD 4 billion in illicit proceeds" / "at least USD 37 million has been attributed to DPRK cyber heists"
note: 보고서는 사업자명을 본문에 쓰지 않으나 각주 14가 "Huione" 기사 제목을 인용. 자체 스테이블코인을 발행해 동결을 회피하는 유형(§35)을 신규 위험으로 명시.
```

```
F-009
claim: FATF는 개정 R.16(지급 투명성) 이행 가이던스 초안에 대한 공개 의견수렴을 2026-06-24 개시하고 2026-08-21 마감했다. 가이던스는 개정 기준의 의무를 바꾸지 않으며 2030년 말 이행을 지원하는 목적이다. 2026-10-21 기준 최종 가이던스는 발간되지 않았다.
entity: reg:fatf-r16-guidance-draft
source_url: https://finreg.aoshearman.com/fatf-consults-on-guidance-to-increase-payment-transparency
publisher: A&O Shearman FinReg (FATF 공식 페이지 https://www.fatf-gafi.org/en/publications/Fatfrecommendations/R16-Public-Consultation-June-2026.html 은 수집기 403)
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "The deadline for responses is 21 August" / "intended to assist jurisdictions and firms in meeting the revised standards by the end of 2030."
note: 의견수렴 주제: 오송금 탐지(정합성 검사), 금융포용, 디지털지갑·모바일머니 등 신결제수단 적용, 데이터보호. 초안은 VASP·스테이블코인을 직접 다루지 않음(2차 출처 기준). "미발간"은 FATF 사이트·2차 보도에 발간 흔적이 없다는 부재 증거이며 10월 총회 의제일 가능성은 §8.
```

### 4.2 EU · 영국

```
F-010
claim: 2026-01-01부터 EU 차원의 AML/CFT 정책·가이던스 권한이 EBA에서 AMLA로 이관되었고, 기존 EBA AML/CFT 가이드라인·기준(트래블룰 가이드라인, 위험기반감독 가이드라인 포함)은 AMLA가 대체하기 전까지 유효하다(AMLAR Art. 54).
entity: org:eu-amla
source_url: https://www.eba.europa.eu/regulation-and-policy/anti-money-laundering-and-countering-financing-terrorism
publisher: European Banking Authority
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "From 1 January 2026, responsibility for all EU-level anti-money laundering" / "all existing EBA AML/CFT guidelines and standards remain valid until AMLA replaces them."
note: 같은 페이지의 팩트시트 문구("by 2025")와 1일 차 표기 불일치가 있으나 본문 기준 2026-01-01. 따라서 "2025~2026 EBA 가이드라인 신규 발표"는 구조적으로 발생하지 않으며, 2026년 발표분은 AMLA 명의다.
```

```
F-011
claim: AMLA는 2026-10-01 AMLR 하위 규제기술기준(RTS) 3건의 최종안 — ① 고객확인(Art. 28(1)) ② 거래관계·일회성거래·연결거래 식별기준 및 하한(Art. 19(9)) ③ 그룹 차원 최소요건 및 제3국 자회사·지점 추가조치(Art. 16(4)·17(3)) — 을 유럽집행위에 제출했다. 적용은 발효 후 6개월(축구 에이전트·구단은 2029-07-10).
entity: reg:eu-amlr-rts-cdd
source_url: https://www.amla.europa.eu/press-release-amla-finalises-key-standards-private-sector_en
publisher: AMLA
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "The final draft standards have now been submitted to the European Commission." / "For football agents and professional football clubs, they will apply from 10 July 2029."
note: CDD RTS 의견수렴은 2026-02-09~05-08(2차 보도). 보도자료에 CASP 특칙 언급 없음 — CASP는 AMLR 의무주체로서 일반 규정 적용. 집행위 채택·관보 게재 전이므로 상태는 "제출(submitted)".
```

```
F-012
claim: AMLA는 2026-10-07 EU 단일 AML/CFT 데이터베이스 관련 기술기준 초안 의견수렴(공청회)을 개시했다.
entity: org:eu-amla
source_url: https://www.amla.europa.eu/index_en
publisher: AMLA
tier: T2
confidence: B
retrieved: 2026-10-21
quote: "Press Release: AMLA consults on draft standards for an EU-wide AML/CFT database"
note: 홈페이지 목록 제목 기준(세부 문서 미열람). 직접감독 대상 잠정목록(2026-09월말 확정 예정)은 홈페이지·뉴스 목록에 공개 흔적 없음 → §8.
```

```
F-013
claim: AMLA는 2026-10-07 유럽집행위의 MiCA 재검토 표적 의견수렴에 대한 답변을 공표하며 AML/CFT 우선과제 5개를 제시했다: ① 스테이킹·대출·차입을 규제체계로 편입 검토 ② DeFi의 실효적 통제자 식별을 위한 법적 정의·공통 기준 ③ 무인가 스테이블코인에 대한 EU 일관 접근 ④ 특정 ART 발행자의 AML/CFT 규칙 편입 여부 재검토 ⑤ 서비스제공자 국경간 감독을 위한 정보요건 명확화.
entity: doc:eu-amla-mica-review-response
source_url: https://www.amla.europa.eu/amla-identifies-amlcft-priorities-review-mica_en
publisher: AMLA
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "bringing these activities within the regulatory framework" / "a clear legal definition and common criteria for identifying who exercises effective control" / "encourages a consistent EU-wide approach that removes legal uncertainty"
note: 집행위 의견수렴의 명칭·기간은 AMLA 페이지에 없음 → §8. MiCA 개정(review)은 입법 제안 전 단계(pre-proposal).
```

```
F-014
claim: ESMA 임시 MiCA 등록부 CASPS.csv(2026-10-19 갱신)는 379개 데이터 행·376개 고유 LEI를 담고 있으며, 본국 회원국별로 DE 109·FR 36·NL 29·CY 25·MT 23·ES 16·LU 13·AT/CZ/IE/LI/LV 각 12·IT 10·DK 7·HR/LT/NO/SK 각 6·BG/FI/SI 각 5·GR 4·EE 3·BE 2·IS/PT/SE 각 1이다. 인가 종료일이 기재된 행은 2건(Decubate B.V. 2026-03-26, Stratos Europe Ltd 2026-04-24)이다.
entity: data:esma-casp-register
source_url: https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv
publisher: ESMA (interim MiCA register, 주간 갱신; 안내 페이지 https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica "Last update: 19 October 2026")
tier: T1
confidence: A
retrieved: 2026-10-21
quote: 헤더 "ae_competentAuthority,ae_homeMemberState,ae_lei_name,ae_lei,ae_lei_cou_code,ae_commercial_name,..." (로컬 파싱: rows=379, distinct LEI=376)
note: 행 수 ≠ 인가 사업자 수와 완전 일치하지 않을 수 있음(동일 LEI 다중행 3건). wave1 F-007(345행, 2026-07말)에서 +34행. 등록부는 ESMA IT 시스템 통합 전 임시 포맷. 2차 출처들의 "280/300+/325" 수치는 추출 시점 차이.
```

```
F-015
claim: FCA 안내 기준 영국 가상자산 FSMA 인가 신청기간은 2026-09-30 개시, 2027-02-28 종료이며, 신체계는 2027-10-25 시행 예정이다. MLR 등록은 자동 전환되지 않고 새로 FSMA 인가를 신청해야 한다.
entity: reg:uk-fsma-cryptoassets-2026
source_url: https://www.fca.org.uk/firms/cryptoassets-information ; https://www.eisneramper.com/insights/cryptocurrency-insights/fca-cryptoasset-authorization-0926/
publisher: FCA / EisnerAmper(2026-09-25)
tier: T2 / T3
confidence: A (기간) · B (개설 사실)
retrieved: 2026-10-21
quote: FCA: "Application period starts" 30 September 2026, "Application period ends" 28 February 2027, "The new regime is expected to come into force on 25 October 2027." / EisnerAmper: "There is no automatic conversion."
note: FCA 뉴스 목록(2026-10-08~19 표시분)에 "개설" 보도자료가 없어 실제 개설은 일정 기준으로만 확인됨. SI 2026/102(2026-02-04 제정)상 규제활동 9개: 적격 스테이블코인 발행, 보관·보관 주선, QCATP 운영, 자기매매·대리매매·거래주선·거래알선, 적격 스테이킹.
```

```
F-016
claim: 2026-08-01까지 처리 완료된 FCA 가상자산 MLR 등록 사안 391건 중 17%가 등록, 67% 철회, 12% 반려(rejection), 4% 공식 거부(refusal)로 종결됐다.
entity: reg:uk-fsma-cryptoassets-2026
source_url: https://www.eisneramper.com/insights/cryptocurrency-insights/fca-cryptoasset-authorization-0926/
publisher: EisnerAmper
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "Of 391 MLR cryptoasset registration cases completed through August 1, 2026 ... 17% ended in registration, 67% in withdrawal, 12% in rejection, and 4% in formal refusal."
note: FCA 원 통계 페이지(/firms/cryptoassets-aml-ctf-regime)는 404. wave1 F-023(2026-07-01: 408 신청/388 처리/67 등록)과 정합.
```

### 4.3 미국

```
F-017
claim: 재무부는 GENIUS Act §3(12 U.S.C. 5902)을 이행하는 NPRM "GENIUS Act Regulations on Payment Stablecoin Issuance, Offer, and Sale"(RIN 1505-AC95, 도켓 TREAS-DO-2026-0496, 12 CFR Chapter XV)을 2026-08-18 연방관보 게재 일정으로 공개했고, 의견 기한은 게재 후 60일(2026-10-19)이다.
entity: reg:us-genius-s3-nprm
source_url: https://public-inspection.federalregister.gov/2026-16796.pdf
publisher: Federal Register (public inspection), Department of the Treasury
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "This document is scheduled to be published in the Federal Register on 2026-08-18" / "Treasury proposes to issue regulations to implement section 3 of the ... GENIUS Act regarding the statutory prohibitions and limitations on payment stablecoin issuance, offer, and sale in the United States."
note: 정의(issue/issuer/located in the U.S.)·면책조항(역외 발행자·DASP의 비의도적 미국 제공, P2P·자기수탁 이전)은 Jones Day 요약(https://www.jonesday.com/en/insights/2026/08/us-treasury-proposes-genius-act-rules-for-stablecoin-issuance-offer-and-sale) 참조. 상태 proposed.
```

```
F-018
claim: GENIUS Act는 최종규칙이 적시에 나오지 않아 법정 최종기한인 2027-01-18에 시행될 것으로 예상되며, 2028-07-18부터 디지털자산서비스제공자는 허가 발행자의 결제 스테이블코인만 제공·판매할 수 있다.
entity: reg:us-genius-act
source_url: https://www.jonesday.com/en/insights/2026/08/us-treasury-proposes-genius-act-rules-for-stablecoin-issuance-offer-and-sale
publisher: Jones Day
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "is expected to be effective on January 18, 2027, the statutory outside date" / "Beginning on July 18, 2028, digital asset service providers must also ensure that only payment stablecoins"
note: 법 자체는 2025-07-18 서명(wave1 F-030). 시행일은 "최종규칙 발효 후 120일 또는 제정 후 18개월 중 빠른 날" 구조에서 후자가 적용될 전망.
```

```
F-019
claim: 2026-07-16 기준 GENIUS Act 하위 규칙제정은 전부 제안 단계다: 재무부 ANPRM(관보 2025-09-19), FDIC 인가 NPRM(2025-12-19), NCUA 인가 NPRM(2026-02-12, 의견 04-13 마감), OCC 이행 NPRM(2026-03-02, 의견 05-01), 재무부 주(州)체계 "실질적 유사성" 원칙 NPRM(2026-04-03, 의견 06-02), FDIC 이행 NPRM(2026-04-10), FinCEN/OFAC PPSI AML/CFT·제재 프로그램 NPRM(2026-04-10, 의견 06-09), NCUA 이행 NPRM(2026-05-18, 의견 07-17), FDIC BSA·제재 기준 의견요청(2026-06-06, 의견 08-04), FinCEN 등 PPSI CIP NPRM(2026-06-22, 의견 08-21). 법정 규칙제정 기한(제정 후 1년, 2026-07-18)은 경과했다.
entity: reg:us-genius-act
source_url: https://www.chapman.com/assets/htmldocuments/Chapman-GENIUS-Act-Rulemaking-and-Reporting-Tracker-081126.pdf
publisher: Chapman and Cutler LLP (Tracker "As of July 16, 2026")
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "Permitted Payment Stablecoin Issuer Anti-Money Laundering/Countering the Financing of Terrorism Program and Sanctions Compliance Program Requirements issued on April 8, 2026; as published in the Federal Register on April 10, 2026 ... Comment period closes June 9, 2026."
note: 로컬 pdftotext 추출. 트래커 이후(2026-07-16~10-21) 최종규칙 공고는 FinCEN 뉴스·관보 목록에서 발견되지 않음(F-020 note). 저장소 산문의 "시행규정 2026-07-18 마감"은 의견마감이 아니라 **법정 규칙제정 기한**이다(§9).
```

```
F-020
claim: FinCEN AML/CFT 프로그램 규칙(NPRM 2026-04-07 발표, 관보 2026-04-10, 의견 2026-06-09 마감)은 2026-10-21 기준 최종화되지 않았다. FinCEN 뉴스 목록(2026-09-16~10-19 게시분)과 연방관보 공고 목록(2026-08-28~10-05)에 최종규칙이 없다.
entity: reg:us-fincen-aml-program-nprm
source_url: https://www.fincen.gov/news ; https://www.fincen.gov/resources/statutes-regulations/federal-register-notices
publisher: FinCEN
tier: T2
confidence: A (부재 증거)
retrieved: 2026-10-21
quote: (목록상 해당 기간 항목) "10/05/2026 ... Withdrawal", "10/01/2026 ... A7 Network's Sub-Agents", "09/02/2026 Geographic Targeting Order ... Southwest Border", "08/28/2026 ... Banque Misr UAE"
note: 투자자문업자 AML 규칙 준수기한 2028-01-01 연기(wave1 F-005)는 변동 없음.
```

```
F-021
claim: FinCEN은 2026-10-05 CVC 믹싱을 §311 주요 자금세탁 우려 거래군으로 지정하려던 결정과 NPRM(88 FR 72701, 2023-10-23)을 철회한다고 발표했고, 철회 공고는 2026-10-06 연방관보 게재 일정이다(철회 공고상 RIN 1506-AB47). 사유: 합법적 활동에 대한 위축 효과와 보고 부담, 행정부의 규제완화 기조.
entity: reg:us-fincen-cvc-mixing-311
source_url: https://public-inspection.federalregister.gov/2026-20429.pdf ; https://www.fincen.gov/news/news-releases/fincen-announces-withdrawals-proposed-digital-asset-related-rules
publisher: Federal Register (public inspection) / FinCEN
tier: T1 / T2
confidence: A
retrieved: 2026-10-21
quote: "FinCEN is withdrawing the proposed rulemaking published at 88 FR 72701 (October 23, 2023)" / "rule could have a chilling effect on legitimate activity and place a large reporting burden on covered financial institutions. However, FinCEN will continue to monitor activity involving CVC mixers" / FinCEN 보도: "withdrawing them as part of the Trump Administration's deregulatory agenda and ongoing efforts to ensure digital asset regulations are fit-for-purpose."
note: 원 NPRM의 RIN은 1506-AB64였으나 철회 공고는 1506-AB47(비수탁지갑 규칙과 동일 RIN)을 표기 — 공고 오기 가능성(§5 C-02). wave1 F-006("최종화되지 않음, Long-Term Actions")은 **superseded**: 상태는 withdrawn.
```

```
F-022
claim: FinCEN은 같은 날 비수탁지갑 NPRM(85 FR 83840, 2020-12-23; 은행·MSB에 비수탁지갑 또는 FinCEN 지정 관할 호스팅 지갑 관련 CVC/LTDA 거래의 보고·기록·신원확인 의무 부과안)도 공식 철회했으며(RIN 1506-AB47, 관보 2026-10-06), 추가 조치를 취하지 않겠다고 밝혔다.
entity: reg:us-fincen-unhosted-wallet-nprm
source_url: https://public-inspection.federalregister.gov/2026-20430.pdf
publisher: Federal Register (public inspection)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "FinCEN is withdrawing the proposed rule published at 85 FR 83840 (December 23, 2020)" / "FinCEN will not take any further action on this NPRM."
note: wave1 F-007은 통합의제(Unified Agenda) 기준 2024-04-12 철회로 기록했고 "연방관보 공고 없음"이라 적었다. 이번에 **관보 철회 공고가 실제 게재**되었으므로 kb/us-bsa.yaml curator_note 정정 필요(§9).
```

```
F-023
claim: FinCEN 2026-10-05 보도자료는 철회 대상 2건을 "certain digital assets, specifically convertible virtual currencies" 관련 제안으로 묶어 발표했고, 향후 디지털자산 규칙에 대한 구체적 계획은 제시하지 않았다.
entity: reg:us-fincen-cvc-mixing-311
source_url: https://www.fincen.gov/news/news-releases/fincen-announces-withdrawals-proposed-digital-asset-related-rules
publisher: FinCEN
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "The Financial Crimes Enforcement Network (FinCEN) is withdrawing the following proposed rules that would have imposed certain regulatory requirements on financial institutions related to certain digital assets, specifically convertible virtual currencies"
note: Cointelegraph(2026-10-05) 보도도 동일 요지.
```

```
F-024
claim: FinCEN은 Combating Russian Money Laundering Act §9714(a)(NDAA FY2022 §6106(b) 개정)에 따라, 러시아 연계 제재회피·자금세탁 서비스인 A7 Network가 통제하는 역외 기업("Sub-Agents")과의 거래를 러시아 불법금융 관련 주요 자금세탁 우려 거래군으로 인정하고 미국 금융기관의 관련 자금이체를 금지하는 특별조치 NPRM(RIN 1506-AB77, 도켓 FINCEN-2026-0265)을 발표했다. 관보 게재 2026-10-05, 의견 30일. 공고는 A7 네트워크가 Garantex·Grinex·A7A5(루블 스테이블코인)·InDeFi Bank 등과 연계되고 이란·테러 대리세력도 이용했다고 기술한다.
entity: reg:us-fincen-a7-special-measure
source_url: https://public-inspection.federalregister.gov/2026-20371.pdf
publisher: Federal Register (public inspection), FinCEN
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "finding transactions involving any company operating outside of the United States that is controlled by the A7 Network, a sanctions evasion and money laundering service with ties to Russia, leveraged by a wide range of illicit actors, including Iran and its terrorist proxies, to be a class of transactions of primary money laundering concern" / 각주 1 "On October 1, 2026, the Department of the Treasury's Office of Foreign Assets Control (OFAC) sanctioned the A7"
note: §311이 아닌 §9714 권한(러시아 특화) 사용. Huione §311 최종규칙(2025-11-17 시행, wave1 F-013)과 함께 "특정 네트워크 차단형" 조치가 "거래유형(믹싱) 차단형"을 대체하는 흐름.
```

```
F-025
claim: OFAC는 2026-09-17 이란 디지털자산 거래소 BitBank, 소프트웨어 개발사 Pishtaz Simorgh Electronic Trade Company(Dot One Value Creation Group 자회사), 개인 3인(Hossein Ali Zaker Hossein, Mohammad Mahdi Zaker Hossein, Seyed Adel Heidari)을 E.O. 13902에 따라 SDN에 지정했다. 재무부는 기지정자 Babak Zanjani가 2026-06~07월 BitBank로 수억 달러 상당 비트코인을 IRGC에 이전했고, 기지정 Hormuz Safe Marine Services Authority도 2026-06 이후 BitBank를 결제 경로로 썼다고 밝혔다. 이 조치는 2026-08-24 개시된 "Operation Economic Outcast"의 일부다.
entity: case:ofac-bitbank-2026-09-17
source_url: https://ofac.treasury.gov/recent-actions/20260917 ; https://home.treasury.gov/news/press-releases/sb0632/
publisher: OFAC / U.S. Department of the Treasury
tier: T1 / T2
confidence: A
retrieved: 2026-10-21
quote: OFAC: "BITBANK: IRAN, IRAN-EO13902" / Treasury: "If you support the Iranian regime, the Department of the Treasury will sanction you."
note: OFAC 공고에 디지털화폐 주소는 미기재. 재무부는 2026-01-30·07-24에도 Zanjani 연계 디지털자산 주체를 지정했다고 언급. 2026-06 Nobitex 등 4개 거래소, 2026-08 Shelbit·Aban Tether 지정은 2차 보도(The Block 2026-09-17, T4, C) 기준.
```

```
F-026
claim: OFAC는 2026-10-01 A7 Network를 E.O. 13581(개정 E.O. 13863)에 따라 초국가범죄조직(TCO)으로 지정했다.
entity: case:ofac-a7-network-2026-10-01
source_url: https://public-inspection.federalregister.gov/2026-20371.pdf
publisher: FinCEN NPRM 각주(OFAC 조치 인용)
tier: T1 (간접)
confidence: B
retrieved: 2026-10-21
quote: "A7 Network pursuant to Executive Order 13581, as amended by Executive Order 13863, for being a foreign person"
note: OFAC recent-actions 2026-10-01 페이지는 미열람(목록 10-05 이후만 노출). 재확인 과제(§8).
```

```
F-027
claim: 2026-09-15 미 상원은 H.R. 3633(CLARITY Act) 진행동의안에 대한 토론종결(cloture) 표결에서 49-50으로 60표에 미달해 부결했다. 찬성 49표는 전원 공화당, 공화당 Collins·Hawley·Moran·Tillis가 반대했고 Tillis는 재심의 동의를 위해 절차적으로 반대했다. 법안은 상원 캘린더에 남아 재표결이 가능하다.
entity: reg:us-clarity-act-hr3633
source_url: https://thedefiant.io/news/regulation/senate-blocks-clarity-act-49-50-with-no-democratic-votes-to-proceed ; https://news.bitcoin.com/clarity-act-made-126-concessions-and-still-couldnt-get-60-votes/
publisher: The Defiant / Bitcoin.com News (2026-09-15)
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "Cloture on the motion to proceed to H.R. 3633 fell 11 votes short of the 60 it needed." / "All 49 votes to proceed came from Republicans." / "Leadership can try again, and Senate rules don't prevent another attempt after the necessary intervening days."
note: senate.gov 롤콜 페이지·congress.gov는 수집기 403 — 공식 표결번호 미확인(§8). 쟁점: 공직자 윤리조항, 스테이블코인 보상(yield)에 대한 재무부 "circuit breaker", 비수탁 개발자 보호. 하원은 2025-07 294-134 통과(wave1).
```

```
F-028
claim: SDNY Failla 판사는 Roman Storm(Tornado Cash)의 미결 2개 죄목(자금세탁 공모·제재위반 공모) 재심 기일을 2027-04-26로 연기했다(명령은 2026-08-25 화요일 등재, 보도 2026-08-26). 2026-04-09 변론된 무죄판결 신청은 미결이며, 2025-08 유죄 평결(무허가 송금업 공모)에 대한 선고도 아직 없다. 검찰은 2026-03 당초 2026-10-05 또는 10-12 재심을 요청했었다.
entity: case:us-v-storm-retrial
source_url: https://decrypt.co/376577/roman-storms-tornado-cash-retrial-pushed-to-april-2027
publisher: Decrypt
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "sets the retrial for April 26, 2027 at the Thurgood Marshall Courthouse" / "His motion for acquittal, argued on April 9, remains undecided."
note: wave1 F-042("2026-03-09 재심 의사 통지")의 후속. DOJ 2025-04 Blanche 메모 기조(비수탁·탈중앙 소프트웨어에 §1960 기소 자제)는 유지된다는 전 형사국장 대행 발언을 기사가 재인용.
```

### 4.4 한국

```
F-029
claim: 「특정 금융거래정보의 보고 및 이용 등에 관한 법률」 개정법(법률 제21358호, 2026-02-19 공포)의 가상자산사업자 신고제 강화(대주주 적격성 심사 등)·퇴직자 제재조치 통보 부분은 2026-08-20 시행되었고, 그 외 부분은 공포 후 6개월 경과일에 시행된다.
entity: reg:kr-tfia-21358
source_url: https://www.fsc.go.kr/no010101/87499
publisher: 금융위원회·금융정보분석원 보도자료 「가상자산시장의 투명성 강화를 위한 「특정금융정보법 시행령」 개정안 국무회의 의결」(2026-08-11)
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "신고제와 퇴직자 제재통보 부분: 2026.8.20." / "그 외 부분: 공포 후 6개월이 지난 날"
note: wave1 F-003의 "2026-08-20 시행 예정"은 **in-force**로 상태 전환. "그 외 부분"의 기산점이 되는 시행령 공포일은 미확인(§8).
```

```
F-030
claim: 2026-08-11 국무회의를 통과한 특금법 시행령 개정안은 신고 심사 대상 대주주 범위에 최대주주 외에 "대표이사 또는 이사의 과반수를 선임한 주주"를 추가하고, 최대주주가 법인인 경우 그 법인의 최대주주와 대표자도 포함한다.
entity: reg:kr-tfia-sd-2026
source_url: https://www.fsc.go.kr/no010101/87499
publisher: 금융위원회
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "대표이사 또는 이사의 과반수를 선임한 주주가 포함되며, 최대주주가 법인이면 그 법인의 최대주주와 대표자도 포함"
note: 신고매뉴얼(F-034)은 주요주주 기준을 "의결권주식 10% 이상 등 세 가지"로 구체화.
```

```
F-031
claim: 같은 개정안은 신고 불수리 요건으로 ① 부채비율 200% 이하(이용자예치금 등은 부채총액에서 제외) ② 최근 3년간 신용질서를 해친 사실이 없을 것 ③ 부실금융기관·인허가 취소자가 아닐 것 ④ 임원·대표자의 「금융회사의 지배구조에 관한 법률」상 자격요건 충족 ⑤ 조직·인력, 물적설비, 내부통제체계 구비를 규정하며, 기존 사업자에는 부채비율·조직인력·전산·내부통제 요건을 1년간 유예한다(감독규정 부칙). 벌금형 이상 처벌 이력은 결격사유이나 대주주는 경미 위반·양벌규정 처벌 시 예외를 둔다.
entity: reg:kr-tfia-sd-2026
source_url: https://www.fsc.go.kr/no010101/87499
publisher: 금융위원회
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "부채비율 200% 이하(이용자예치금 등은 부채총액에서 제외)" / "기존 사업자는 부채비율 요건과 조직·인력·전산설비·내부통제 요건이 1년간 유예"
note: 보도(MTN 2026-09-14, T4)는 신고 28개사 중 12개사가 부채비율 200%를 충족하지 못한다고 전함(단독, confidence C).
```

```
F-032
claim: 개정 시행령은 가상자산 이전 시 정보제공(트래블룰) 기준금액을 현행 100만원 이상에서 전체 거래로 확대하고, 수취 사업자에게 정보 확보 의무(정보 누락 시 요청·거래거절 등)를 부과한다.
entity: reg:kr-tfia-sd-2026
source_url: https://www.fsc.go.kr/no010101/87499 ; https://eiec.kdi.re.kr/policy/materialView.do?num=285286
publisher: 금융위원회 / KDI 경제정보센터(FIU 보도자료 전재)
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "트래블룰 기준금액(100만원)을 폐지하여 모든 가상자산 이전거래에 자금세탁방지 의무를 부과하고"
note: **시행 시점 주의** — 이 부분은 "그 외 부분"에 해당해 공포 후 6개월 뒤 시행. 2026-10-21 기준 시행령 제10조의10 제1호의 "1백만원 이상" 기준은 **아직 유효**하며 상태는 amended-not-yet-in-force. 상세는 트래블룰 별도 도시에.
```

```
F-033
claim: 개정 시행령은 해외 가상자산사업자·개인지갑과의 이전을 위험도에 따라 차등화한다: 저위험 해외거래소로의 이전은 허용, 그 외 해외거래소·개인지갑은 송신인과 수신인이 동일한 경우에만 허용, 고위험은 금지. 1천만원 이상 거래에는 자체 의심거래 관리체계를 구축·운영해야 한다. 아울러 고객확인의 방법·대상을 명확화하고(강화된 고객확인 여부는 고객 특성·거래양태·상품 위험도로 판단), FIU의 퇴직자 제재통보 권한 중 임원 문책경고·주의적경고·주의 및 직원 제재 전체를 검사수탁기관(금감원 등)에 위탁한다.
entity: reg:kr-tfia-sd-2026
source_url: https://www.fsc.go.kr/no010101/87499
publisher: 금융위원회
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "저위험 해외거래소로의 이전은 허용 / 그 외 해외거래소·개인지갑은 송신인과 수신인이 동일한 경우에만 허용 / 고위험은 거래 금지 / 1천만원 이상 거래에는 자체 의심거래 관리체계를 구축·운영"
note: wave1 F-011의 입법예고 내용("1,000만원 이상은 위험도 무관 STR")과 최종 문구가 다름 — 최종안은 "자체 의심거래 관리체계 구축·운영"으로 표현(§5 C-04). 개정 감독규정도 함께 고시 예정이라고 명시.
```

```
F-034
claim: FIU·금감원은 2026-08-13 개정 특금법 시행(08-20)에 맞춘 「가상자산사업자 신고매뉴얼」 전면 개정안을 공표하고 설명회(신고 28개사·예비사업자 등 약 100명)를 열었다. 매뉴얼은 AML 업무 인력 4인 이상(겸직 인정 가능), 고유식별정보·개인신용정보 처리 전산설비의 국내 소재(클라우드는 국내 리전 인정), 대주주·법령준수체계 변경의 "변경 30일 전 사전신고"(종전 변경 후 14일 내 사후신고), 주요주주 기준(의결권주식 10% 이상 등 3가지), 부채비율 산정 시 이용자예치금 차감 등을 규정한다.
entity: doc:kr-vasp-manual-2026
source_url: https://www.fsc.go.kr/no010101/87521
publisher: 금융위원회 보도자료 「가상자산사업자 신고제 강화에 맞춰 신고매뉴얼을 전면 개정합니다」(2026-08-13)
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "자금세탁방지 업무 종사 인력은 4인 이상" / "변경 후 14일 이내 사후신고"에서 "변경 30일 전 사전신고" / 별첨 "'26.8.20일 시행 기준"
note: 보도자료 본문에는 재신고 기한·44개 심사항목이 없음(F-035는 언론 기준).
```

```
F-035
claim: 기존 신고 사업자는 개정 특금법에 따라 2026-11-20까지 재신고(부칙 신고)해야 하며, FIU는 2026-09 중 대주주 적격성·지배구조 포함 44개 심사항목에 대해 증빙·현장점검을 시작했고 코인마켓 거래소 6개사(09-17)·커스터디 3개사(09-18) 간담회를 예정했다.
entity: reg:kr-tfia-21358
source_url: https://news.mtn.co.kr/news-detail/2026091415254495524
publisher: 머니투데이방송(MTN) [단독] 2026-09-14
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "Existing operators must re-file by November 20, 2026" (수집기 요약; 원문 "기존 사업자들은 오는 11월 20일까지 개정 법률에 따라 재신고해야 한다")
note: 11-20은 시행일(08-20)+3개월로 법률 부칙에서 도출 가능하나 부칙 원문을 이번에 확인하지 못함. wave1 F-033도 T3 단일출처로 재검증 과제였음 → 여전히 미해결(§8). FIU 보도자료 사이트(kofiu.go.kr/kor/notification/press.do)는 2026-10-21 수집 시 오류 페이지.
```

```
F-036
claim: 2026-07-29 국회 정무위 업무보고에서 금융위원장(이억원)은 디지털자산기본법 정부안이 마련됐으나 "약간 이견이 있다"며 조만간 제출하겠다고 답했고, 당시 디지털자산·스테이블코인 관련 의원 발의 법안 10건이 계류 중이었다(2025-06 민병덕 의원안이 최초).
entity: reg:kr-digital-asset-basic-act
source_url: https://biz.sbs.co.kr/amp/article/20000325470
publisher: SBS Biz (2026-07-29)
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "최대한 신속하게 하도록 하겠다" / 계류 법안 "10개"
note: 상태 = proposed(의원안 계류) + 정부안 미제출. 2025-10 국감에서 "연내 제출"(2025년 내)을 약속했으나 지키지 못한 경과는 2차 보도.
```

```
F-037
claim: 2026-10-08 국회 정무위 국정감사에서 금융위원장은 디지털자산기본법과 스테이블코인 제도에 대해 "관련 내용은 이미 준비해 놓았고 막바지 협의를 하고 있다"고 답했으며, 라이선스 종류·제도 설계는 "시장 상황 등을 봐서 정책적으로 해 나갈 부분"이라고 했다. 여당 의원(이강일)은 원화 스테이블코인 발행주체가 미결이라고 지적했다. 정부안 제출 시점·발행주체·거래소 인허가 개편안은 제시되지 않았다.
entity: reg:kr-digital-asset-basic-act
source_url: https://www.blockmedia.co.kr/archives/1149080
publisher: 블록미디어 (2026-10-08)
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "관련 내용은 이미 준비해 놓았고 막바지 협의를 하고 있다" / "원화 스테이블코인은 누가 발행할 것인지도 결론을 내지 못했다"
note: 금융위 2026-07~10월 보도자료 목록(F-039 note)에 디지털자산기본법·가상자산위원회 항목 없음 → 공식 발표 부재와 정합. 원화 스테이블코인은 2026-10-21 기준 **입법 공백(proposed only)**.
```

```
F-038
claim: 법인의 가상자산시장 참여 2단계(상장사·전문투자자 등록법인 약 3,500개사 실명계좌 발급·투자목적 매매 시범허용)는 2026-05-19 보도 기준 세부 기준·시행일이 미정이며, 금융당국은 5대 원화거래소 KYC·STR 점검 등 "안전장치 마련" 현장점검 중이었다. 2026-07~10월 금융위 보도자료에 2단계 시행 발표는 없다.
entity: reg:kr-tfia-sd-2026
source_url: https://www.fnnews.com/news/202605191827097795 ; https://www.fsc.go.kr/no010101?srchKey=sj&srchText=%EA%B0%80%EC%83%81%EC%9E%90%EC%82%B0
publisher: 파이낸셜뉴스(2026-05-19) / 금융위 보도자료 검색목록
tier: T4 / T2
confidence: C (지연 사유) · A (공식 발표 부재)
retrieved: 2026-10-21
quote: "법인투자 허용의 경우 법률 규정 사항은 아니기 때문에 시행 시점을 정확히 가늠하기 어렵다"
note: wave1 F-022/F-023의 1단계(2025-06-01 시행)는 변동 없음. 2단계 상태: **announced(2025-02-13) · not implemented**.
```

```
F-039
claim: 금융위·FIU의 '26년 상반기 가상자산사업자 실태조사(기준 2026-06-30, 2026-10-01 공표)에 따르면 조사대상은 26개(거래소 17·지갑보관 9; 신고 28개 중 2개 자료 미제출), 국내 보유 가상자산 평가총액 58.9조원(전기 87.2조 대비 -33%; 원화마켓 58.5조·코인마켓 0.33조), 일평균 거래대금 3.1조원(-44%), 거래가능 계정 1,117.5만 개, 원화예치금 5.2조원, 거래소 영업이익 816억원·지갑보관업자 영업손실 186억원, 상장 종목 1,703개(중복 제외 673, 단독상장 234), 총 출고 62.8조원 중 트래블룰 적용 9.5조원(≈15%), 화이트리스트 이전 약 83%, AML 인력 213명/거래소 임직원 2,021명이다.
entity: doc:kr-vasp-survey-2026h1
source_url: https://www.fsc.go.kr/no010101/87835
publisher: 금융위원회·금융정보분석원 보도자료 「'26년 상반기 가상자산사업자 실태조사 결과」(2026-10-01)
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "17개 거래소, 9개 지갑·보관업자" / "Travel Rule applied to 9.5 trillion won of 62.8 trillion won in total outflows" (수집기 요약)
note: 원화마켓·코인마켓 사업자 수는 이 보도자료에 미기재. 신고 사업자 총수 28개는 변동 없음(wave1 F-012). 트래블룰 적용 비중 15%는 100만원 기준·국내 VASP 간 이전에 한정된 현행 제도의 결과로 해석 가능 — 기준금액 폐지 후 비교 지표.
```

```
F-039b
claim: 금융위는 2026-09-23 제16차 정례회의에서 가상자산 불공정거래 혐의 4건(API 자동매매 초단기 시세조종 3건, 운영사 임직원·전문매매업자의 가장매매 1건)을 고발·수사기관 통보했고, 2026-07-01에도 시세조종 혐의자를 고발했다. 2026-07-20에는 가상자산이용자보호법 시행 2년 조사 성과를 발표했다.
entity: reg:kr-vaupa
source_url: https://www.fsc.go.kr/no010101/87783 ; https://www.fsc.go.kr/no010101?srchKey=sj&srchText=%EA%B0%80%EC%83%81%EC%9E%90%EC%82%B0
publisher: 금융위원회
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "초단기 시세조종 사건 3건" / "가장매매로 거래량을 인위적으로 부풀린 사건"
note: 근거조항·누적 건수는 보도자료에 미기재. 2026-10-16 「'무기한 선물' 이용자 유의사항」도 게시(제목만 확인).
```

```
F-040
claim: FIU 요청으로 방송미디어통신심의위원회가 2026-10-06~07 심의해 운영 중인 불법 가상자산 취급업자(특금법상 미신고 사업자) 인터넷 사이트 27건을 국내 접속차단(국내 서버·운영자는 이용해지)했다(2026-10-13 공표). 수사기관 통보 누적 불법업체는 44개이며, 구글·애플 앱마켓의 신규 설치·업데이트 차단은 이미 시행 중이어서 앱·사이트 양측이 차단된 상태다.
entity: case:kr-unregistered-site-block-2026-10
source_url: https://www.fsc.go.kr/no010101/87916
publisher: 금융위원회·금융정보분석원 보도자료(2026-10-13)
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "현재 운영 중인 불법 가상자산 취급업자 사이트 27건" / "현재까지 수사기관에 통보된 불법업체는 44개"
note: wave1 F-019~F-021(통보 누적 40개, 2026-06-10)에서 +4개. 사업자 명단은 붙임(미열람).
```

```
F-041
claim: 서울행정법원은 2026-04-09 두나무의 영업일부정지(2025-03-07~06-06, 3개월) 처분 취소소송 1심에서 고의·중과실 입증이 어렵다는 취지로 원고(두나무) 승소 판결을 선고했다(보도). 빗썸은 6개월 영업일부정지·과태료 368억원 처분에 불복해 소를 제기했고 첫 변론이 2026-04-23 예정이었다. 2026-07~10월 금융위 보도자료에는 가상자산사업자 대상 신규 과태료·영업정지·기관경고 발표가 없다.
entity: case:kr-dunamu-suspension-litigation
source_url: https://www.kukinews.com/article/view/kuk202604130220 ; https://www.fsc.go.kr/no010101?srchKey=sj&srchText=%EA%B0%80%EC%83%81%EC%9E%90%EC%82%B0
publisher: 쿠키뉴스(2026-04-13) / 금융위 보도자료 목록
tier: T4 / T2
confidence: C (판결) · A (제재 발표 부재)
retrieved: 2026-10-21
quote: 수집기 요약 "the Seoul Administrative Court ruled in Dunamu's favor in the first instance on '지난 9일' ... intent or gross negligence was hard to establish"
note: wave1 F-014~F-018의 제재 사실(두나무·빗썸·코인원·코빗)은 변동 없음. **집행 지형 변화의 핵심은 '제재 → 사법심사'로 무게가 이동**한 것. FIU 항소 여부, 빗썸·코인원 소송 경과는 미확인(§8). FIU 보도자료 사이트 장애로 FIU 단독 발표는 미검증.
```

### 4.5 기타 관할

```
F-042
claim: 「金融商品取引法及び資金決済に関する法律の一部を改正する法律」은 제221회 국회에 2026-04-10 제출, 2026-07-15 성립했다(금융청). 공포는 2026-07-23, 법률번호는 令和8年法律第64号이며(2차), 암호자산 규제의 자금결제법→금상법 이관 조항은 "공포일로부터 1년을 넘지 않는 범위에서 정령으로 정하는 날"(≤2027-07-23) 시행, 무등록업자 벌칙 인상 등 일부는 2026-08-12 시행이다.
entity: reg:jp-fiea-psa-amendment-2026
source_url: https://www.fsa.go.jp/common/diet/index.html ; https://keiyaku-watch.jp/media/hourei/2026-2027-kinsyohou/ ; https://www.pwc.com/jp/ja/knowledge/news/legal-news/legal-20260728-4.html
publisher: 金融庁(제출·성립일) / 契約ウォッチ(공포일·법률번호·시행기한) / PwC Japan(성립일·개정 골자)
tier: T1 / T4 / T3
confidence: A (성립일) · C (공포일·법률번호·세부 시행일)
retrieved: 2026-10-21
quote: FSA: "令和８年４月10日提出" "令和８年７月15日成立" / 契約ウォッチ: "公布日：2026年7月23日" "公布の日から起算して1年を超えない範囲内において政令で定める日"
note: wave1 F-016(2026-07-15 성립, 시행일 미확정)의 후속. e-Gov 법령검색·관보 원문은 수집기로 열리지 않아 공포일·번호는 T4 단일 → §5 C-05. 개정 골자: 발행자·거래업자 정보공표 의무, 업규제 재편(暗号資産取引業), 불공정거래(인사이더) 규제. 2026-06-01 시행된 令和7年 개정 자금결제법(중개업 신설, wave1 F-019)과는 별개 법.
```

```
F-043
claim: 일본 범죄수익이전방지법(트래블룰 근거, 제10조의5)의 2026-07-30 이후 개정은 이번 조사에서 확인되지 않았다.
entity: reg:jp-aptcp
source_url: https://www.pwc.com/jp/ja/knowledge/news/legal-news/legal-20260728-4.html
publisher: PwC Japan
tier: T3
confidence: B (부재 증거)
retrieved: 2026-10-21
quote: (PwC 페이지의 개정 항목 목차에 犯罪収益移転防止法 항목 없음)
note: 금상법 이관 시 범수법상 "암호자산교환업자" 지정 문구의 연동 개정(整備法) 가능성은 정령·내각부령 단계에서 확인 필요(§8).
```

```
F-044
claim: MAS는 2026-09-01 「Consultation Paper on Proposed Amendments to the Payment Services Act 2019 for Stablecoins Regulation」을 발표하고 2026-10-16 의견수렴을 마감했다. 제안: 신규 "stablecoin issuance" 라이선스 클래스(MAS-regulated stablecoin 표방은 라이선스 보유자만), 준비자산 ≥ 유통량 액면, 페그통화 상환 기한, 발행자의 추적·동결·소각 기술능력, 전 보유자 신원확인 요구 여부 의견수렴, 역외 발행 스테이블코인의 사례별 인정(Part 2B "MAS-recognised"), 시스템적 스테이블코인 지정 체계, 비규제 스테이블코인은 DPT 체계 잔류, 은행은 별도 비은행 법인으로 발행.
entity: reg:sg-psa-stablecoin-amendments
source_url: https://www.allenandgledhill.com/sg/perspectives/articles/33474/sgkh-mas-consults-on-amendments-to-payment-services-act-2019-to-implement-stablecoin-regulatory-framework ; https://www.bakermckenzie.com/en/insight/publications/2026/09/singapore-mas-introduces-stablecoins-framework-under-payments-legislation
publisher: Allen & Gledhill / Baker McKenzie
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "On 1 September 2026, the Monetary Authority of Singapore (MAS) published a Consultation Paper" / "The consultation closes on 16 October 2026." / "technical capability to trace, freeze, and/or burn their stablecoin"
note: MAS 원문 페이지는 307 리다이렉트로 미열람. 상태 proposed(의견수렴 종료, 법안 미제출). 2023-08 MAS 단일통화 스테이블코인 체계(wave1 F-008)의 법제화 단계. DTSP(FSMA Part 9, 2025-06-30 시행) 관련 2026년 변경은 발견되지 않음.
```

```
F-045
claim: 싱가포르 MAS Notice PSN02(DPT 서비스 AML/CFT, 최종개정 2025-06-30)의 2026-07-30 이후 추가 개정은 이번 조사에서 확인되지 않았다 — 부재 진술이며, 2026-09-01 스테이블코인 PSA 개정 의견수렴(F-044)이 향후 PSN02 적용범위에 영향을 줄 수 있다.
entity: reg:sg-psn02
source_url: https://www.allenandgledhill.com/sg/perspectives/articles/33474/sgkh-mas-consults-on-amendments-to-payment-services-act-2019-to-implement-stablecoin-regulatory-framework
publisher: Allen & Gledhill (PSN02 개정 언급 없음)
tier: T3
confidence: D
retrieved: 2026-10-21
quote: "Stablecoins that are not MAS-regulated stay in the DPT regime, for which all intermediation services are subject to regulation" (수집기 요약)
note: 검색 쿼터 소진으로 MAS 고시 페이지(mas.gov.sg) 직접 재확인 불가. §8 재검증 과제.
```

```
F-046
claim: SFC 공식 명단(2026-10-16 갱신) 기준 홍콩 VATP 인가 운영자는 13개(최신: Victory Fintech/VDX 2026-02-13, NewBX/Bixin.com 2026-05-18)이고, 심사 중 5개(그중 deemed-to-be-licensed 2개: Foris DAX HK, Whalefin Markets), 신청 철회 16·반려 2·거부 0으로 명단에서 제외된 신청자는 18개다.
entity: data:hk-sfc-vatp-list
source_url: https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/Virtual-assets/Virtual-asset-trading-platforms-operators/Lists-of-virtual-asset-trading-platforms
publisher: Securities and Futures Commission (HK)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Last updated: 16 Oct 2026" / 13번째 "NewBX Limited | Bixin.com | 18/05/2026"
note: wave1 F-013/F-014(2026-05-29: 13개·심사 6·deemed 3·탈락 누적 23)와 비교하면 인가 수는 동일, 심사 중 6→5, deemed 3→2. 탈락 누적 23→18의 차이는 집계 범위(과거 제외 신청자 포함 여부)에 기인할 수 있음 → §5 C-06. 일부 2차 보도의 "12개"는 2026-02 시점 수치.
```

```
F-047
claim: HKMA 「Register of Licensed Stablecoin Issuers」(최종 갱신 2026-04-23)에는 Anchorpoint Financial Limited(FRS01)와 The Hongkong and Shanghai Banking Corporation Limited(FRS02) 2개가 2026-04-10 효력으로 등재되어 있으며, 2026-10-21까지 추가 인가는 없다.
entity: data:hk-hkma-stablecoin-register
source_url: https://www.hkma.gov.hk/eng/regulatory-resources/registers/register-of-licensed-stablecoin-issuers/
publisher: Hong Kong Monetary Authority
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Anchorpoint Financial Limited | FRS01 | 10/04/2026" / "The Hongkong and Shanghai Banking Corporation Limited | FRS02 | 10/04/2026" / "Last revision date : 23 April 2026"
note: 발행 스테이블코인 명칭·통화는 등록부에 미기재. 안내 페이지(stablecoin-issuers/) 최종 수정 2026-07-13이나 인가 추가 없음. wave1 F-011과 동일.
```

```
F-048
claim: UAE에서는 연방 CMA(옛 SCA)가 2026-04 가상자산 체계를 발표해 규제활동을 3개에서 8개 범주로 확대했고(일반요건·영업행위·대체거래시스템·AML/CFT·건전성 5모듈), VARA는 Exchange Services Rulebook v2.1을 2026-03-31 시행했으며(거래소 상장 가상자산 파생상품 상시 허용), DFSA는 2026-04 컴플라이언스 점검 결과를 공표했다. VARA의 AML/CFT 서큘러는 온보딩 및 AED 3,500 초과 거래에 CDD를 요구한다.
entity: reg:ae-cma-va-framework-2026
source_url: https://www.clydeco.com/en/insights/2026/05/uae-virtual-assets-update-q2-2026
publisher: Clyde & Co (2026-05-07)
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "expanding regulated activities from three to eight categories" / "Version 2.1 of its Exchange Services Rulebook (effective 31 March 2026)"
note: 2026-07-30 이후 VARA·CBUAE 신규 조치는 확인 못함. "연방 AML Decree-Law 10/2025(2025-10 시행, VASP에 은행 동등 기준)" 주장은 T5 단일 출처(facephi.com, 2026-08-11)로 confidence D → §5 C-07, §8.
```

```
F-048b
claim: 호주에서는 2026-06-30 AUSTRAC VASP 등록부가 공개되고 2026-07-01부터 가상자산 이전에 트래블룰 의무가 적용되었으며, 미검증 자기수탁 지갑 관련 보고 의무는 2029-03-31까지 유예된다.
entity: reg:au-amlctf
source_url: https://sumsub.com/media/news/australia-launches-public-vasp-register-as-travel-rule-to-take-effect/
publisher: Sumsub (2026-06-30; AUSTRAC 원문 링크 인용)
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "Travel Rule obligations apply to newly regulated virtual asset services from July 1" / "remains deferred until March 31, 2029"
note: AUSTRAC 원문(virtual-asset-service-provider-register-goes-public, amlctf-transitional-rules-2026)은 3회 연속 타임아웃으로 미확인. 2026-07-30 이후 AUSTRAC 가상자산 집행 사례는 발견되지 않음. wave1 F-024/F-025(VASP 의무 2026-03-31, 트래블룰 2026-07-01)와 정합.
```

```
F-049
claim: 인도 FIU-IND는 2026-09-09 PMLA 2002 미준수를 이유로 역외 VDA 서비스제공자 15곳(Bitunix, DigiFinex, Pionex, WhiteBIT, FixedFloat, Toobit 등)에 통지를 발부하고 불법 운영 서비스의 앱·URL 공개접근 차단을 요구했다. 의무는 활동 기준으로 인도 내 물리적 소재와 무관하다.
entity: case:in-fiu-ind-15-vda-notices
source_url: https://newsonair.gov.in/fiu-ind-cracks-down-on-15-vda-service-providers-over-pmla-non-compliance/
publisher: News on AIR (인도 공영방송, 재무부 발표 전재)
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "are activity-based and are not contingent on physical presence of the entity in India" / "to take down applications and URLs providing public access to services found to be operating illegally in the Country"
note: 2026-01-08 FIU-IND VDA AML/CFT 가이드라인 개정(wave1 F-033)의 집행 국면. 정부 디지털자산 토론보고서·COINS Act(민간 모델법)는 법적 효력 없음 — 상태 변화 없음.
```

### 4.6 정량 지형(2026년 발간 연례 보고서)

```
F-050
claim: Chainalysis(2026-01-08 공개)에 따르면 2025년 불법 주소 수취액은 최소 USD 1,540억으로 2024년 수정치 USD 572억(당초 발표 409억) 대비 162% 증가했고, 전체 온체인 거래량 대비 불법 비중은 1% 미만, 스테이블코인이 불법 거래량의 84%를 차지했다. 제재 대상 주체 수취액은 694% 증가, 북한 연계 해커 탈취액은 USD 20억(Bybit 약 15억 포함), 러시아 A7A5는 1년 미만에 USD 933억 이상 거래됐다.
entity: doc:chainalysis-ccr-2026
source_url: https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/
publisher: Chainalysis
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "at least $154 billion" / "our updated estimate for 2024 is substantially higher at $57.2 billion" / "Stablecoins accounted for 84% of all illicit transaction volume in 2025" / "a dramatic 694% increase in the value received by sanctioned entities"
note: 방법론: 식별된 불법 주소 기반 하한 추정치(향후 상향 전망), 비(非)크립토 네이티브 범죄 제외, 분모는 알려진 서비스 유입 총액(서비스 내부 이전 제외). $154B/$57.2B는 산술상 +169%이나 보고서는 162%로 표기(반올림·수정치 차이, §5 C-08). 제재 관련 절대액은 서문에 미기재(2차 보도의 "$104B"는 미검증).
```

```
F-051
claim: TRM Labs(2026-01-28)에 따르면 2025년 불법 지갑 수취액은 사상 최대 USD 1,580억으로 2024년 USD 645억 대비 약 145% 증가했으나, 전체 가상자산 거래량 대비 비중은 1.3%(2024)→1.2%(2025)로 하락했고 VASP 유입 기준으로는 2.9%→2.7%다. 해킹·익스플로잇 약 150건 USD 28.7억(Bybit 14.6억), 북한 연계 USD 19.2억, 제재 주체·관할 유입 USD 930억(그중 A7A5 약 720억, 95%가 스테이블코인), 사기 유입 약 USD 350억(검증 230억+신고 120억; 검증 사기의 84%가 스테이블코인).
entity: doc:trm-ccr-2026
source_url: https://www.trmlabs.com/reports-and-whitepapers/2026-crypto-crime-report
publisher: TRM Labs
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "Illicit crypto volume reached an all-time high of USD 158 billion in 2025, up nearly 145% from 2024." / "from 1.3% in 2024 to 1.2% in 2025" / "TRM Labs attributes USD 1.92 billion to North Korea-linked actors (DPRK) in 2025." / "Nearly 95% of inflows to sanctioned entities and jurisdictions in 2025 were through stablecoins."
note: 방법론: "conservative baseline — a minimum, or 'floor'", 법정화폐 기원 수익·미귀속 주소·세탁 체인 제외(이중계산 방지), 분모를 알려진 서비스·지갑으로 축소, VASP 유출 유동성 지표 추가. 수치는 "dynamic baseline"으로 상향 수정 예정.
```

```
F-052
claim: Elliptic은 2025-10-06 기준 북한 연계 해커가 2025년에 이미 USD 20억 이상을 탈취해 연간 최대 기록을 세웠고(이전 최고 2022년 13.5억, 2024년 대비 약 3배), 누적 알려진 탈취액은 USD 60억 이상이라고 밝혔다. 이번 조사에서 Elliptic의 2026년 연례 범죄 보고서는 확인되지 않았다.
entity: act:dprk-cyber
source_url: https://www.elliptic.co/blog/north-korea-linked-hackers-have-already-stolen-over-2-billion-in-2025
publisher: Elliptic
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "have already stolen over $2 billion in cryptoassets in 2025" / "Attributing cyber thefts to North Korea is not an exact science."
note: 연말 확정치 아님(10월 초 시점). Elliptic 2026 Typologies Report 존재 여부는 §8.
```

```
F-053
claim: TRM Labs(2026-04-30 보도)에 따르면 2026년 1~4월 북한 연계 행위자는 약 USD 5.77억을 탈취해 같은 기간 전 세계 해킹 손실의 76%를 차지했고(KelpDAO 2.92억·Drift Protocol 2.85억), 2025년 북한 비중은 64%(2024년 39%), 2017년 이후 누적 귀속 탈취액은 USD 60억을 넘었다.
entity: act:dprk-cyber
source_url: https://www.theblock.co/post/399569/north-korea-accounts-for-76-of-2026-crypto-hack-losses-with-theft-since-2017-topping-6-billion-trm-labs
publisher: The Block (TRM 자료 인용, 2026-04-30)
tier: T4
confidence: C
retrieved: 2026-10-21
quote: "North Korean actors extracted approximately $577 million through the first four months of 2026" / "a sum representing 76% of all global cryptocurrency hack losses during the period"
note: TRM H1 2026 보고(2026-07-01: 총 손실 USD 9.72억, 북한 66.2%)는 검색 스니펫만 확보해 원문 미확인 → §8. 2026년 YTD 수치는 기간이 달라 2025년 연간치와 직접 비교 불가.
```

---

## 5. 상충·의문점

| ID | 쟁점 | 출처 A 주장 | 출처 B 주장 | 판단 | 재검증 방법 |
|---|---|---|---|---|---|
| C-01 | 트래블룰 입법국 중 미집행 비율 | FATF TU7 요약: "almost half" | FATF TU7 본문 §25: 60%(55/91) | 본문 수치 채택, 요약 표현 병기. 2차 보도는 요약문을 옮겨 "절반 가까이"로 보도 | 원문 PDF p.16 재확인(완료) — 인용 시 본문 우선 |
| C-02 | CVC 믹싱 철회 공고의 RIN | 원 NPRM(2023) RIN 1506-AB64 | 철회 공고(2026-10-06) RIN 1506-AB47 | 공고 표기 오류 또는 비수탁지갑 RIN 재사용 가능. 식별은 FR 인용(88 FR 72701)으로 | reginfo.gov RIN 1506-AB64·AB47 이력 조회 |
| C-03 | 비수탁지갑 NPRM 철회 시점 | wave1 F-007: 통합의제상 2024-04-12 철회, 관보 공고 없음 | FR 2026-20430: 2026-10-06 관보 철회 공고 | 양립 — 의제상 종결(2024)과 공식 관보 철회(2026)는 다른 행정행위. KB는 두 날짜를 분리 기록 | reginfo 이력 + FR 공고(확보) |
| C-04 | 해외 VASP·개인지갑 1,000만원 이상 거래의 의무 성격 | wave1 F-011(입법예고): "위험도 무관 의심거래 보고" | 금융위 2026-08-11 보도자료: "자체 의심거래 관리체계를 구축·운영" | 최종안 문구가 더 완화·구조적. STR 자동의무로 서술하면 오류 | 공포 시행령 제10조의20 원문 대조 |
| C-05 | 일본 개정법 공포일·법률번호 | 契約ウォッチ: 2026-07-23, 令和8年法律第64号 | FSA·PwC: 성립 2026-07-15만 확인, 공포·번호 미기재 | 공포일·번호는 T4 단일 → confidence C | e-Gov 法令検索(508AC0000000064) 또는 官報 2026-07-23호 |
| C-06 | 홍콩 VATP 탈락 누적 수 | wave1 F-014(2026-05-29): 철회·반려·거부 23 | SFC 명단(2026-10-16): 18(철회 16·반려 2) | SFC 명단은 "최신 상태 미반영 가능" 고지. 집계 범위(명단 삭제 후 미표시) 차이로 추정 | SFC 명단 과거 스냅샷 비교 |
| C-07 | UAE 연방 AML Decree-Law 10/2025 | facephi(T5): 2025-10 시행, VASP에 은행 동등 기준 | Clyde & Co·Tamimi 등 T3에서 미확인(Tamimi 404) | confidence D. 본문 인용 보류 | UAE 관보/CBUAE·MoE 공식 페이지 |
| C-08 | Chainalysis YoY 증가율 | 보고서: +162% | $154B/$57.2B 산술치 ≈ +169% | 반올림·수정치 시점 차이. 보고서 표기 그대로 인용하고 산술 괴리 주석 | Chainalysis 본문 표 확인 |
| C-09 | 2025 불법 규모·북한 탈취액 | Chainalysis: $154B / DPRK $2.0B / 2024 $57.2B | TRM: $158B / DPRK $1.92B / 2024 $64.5B | 방법론·분모·귀속 기준 상이 — 병기 원칙. 두 수치 모두 "하한(floor)" | 두 보고서 방법론 부록 비교(별도 도시에) |
| C-10 | 재신고 기한 2026-11-20 | MTN(2026-09-14, 단독) 및 다른 T4 보도 | 금융위 보도자료 2건(08-11, 08-13)에는 기한 미기재 | 시행일+3개월 추정과 일치하나 1차 미확인 → C | 법률 제21358호 부칙 원문(law.go.kr) |
| C-11 | FCA 인가창 "개설" 확인 | FCA 페이지: "Application period starts 30 September 2026" | FCA 뉴스 목록(10-08~19)에 개설 보도자료 없음 | 일정상 개설된 것으로 보되 명시 확인은 없음 → B | FCA Connect 공지 또는 10월 초 FCA 뉴스 아카이브 |

---

## 6. 출처 레지스트리

| source_id | 기관 | URL | tier | 갱신주기 | 접근 | 비고 |
|---|---|---|---|---|---|---|
| S-01 | FATF | https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-june-2026.html | T2 | 총회별 | 공개 | 자동수집기 403 — 브라우저 접근 필요 |
| S-02 | FATF (FIAU Malta 미러) | https://fiaumalta.org/app/uploads/2026/07/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf | T2 | 연 1회 | 공개 | 7차 TU 전문 PDF |
| S-03 | FATF | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-updated-virtualassets-vasps-2026.html | T2 | — | 공개 | 공표 페이지(403) |
| S-04 | The Tribune/ANI | https://www.tribuneindia.com/news/world/first-fatf-plenary-under-uk-presidency-to-take-place-from-october-28-30/ | T4 | — | 공개 | 10월 총회 일정 |
| S-05 | AML UAE | https://amluae.com/fatf-grey-list-countries-update-19th-june-2026/ | T4 | 총회별 | 공개 | 22개 명단 |
| S-06 | ComplyAdvantage | https://complyadvantage.com/insights/fatf-plenary-june-2026-outcomes/ | T4 | — | 공개 | 흑색명단·UK 의장국 |
| S-07 | A&O Shearman | https://finreg.aoshearman.com/fatf-consults-on-guidance-to-increase-payment-transparency | T3 | — | 공개 | R.16 가이던스 의견수렴 |
| S-08 | EBA | https://www.eba.europa.eu/regulation-and-policy/anti-money-laundering-and-countering-financing-terrorism | T2 | 수시 | 공개 | AMLA 이관 |
| S-09 | AMLA | https://www.amla.europa.eu/press-release-amla-finalises-key-standards-private-sector_en | T2 | — | 공개 | RTS 3건 제출 |
| S-10 | AMLA | https://www.amla.europa.eu/amla-identifies-amlcft-priorities-review-mica_en | T2 | — | 공개 | MiCA 재검토 의견 |
| S-11 | AMLA | https://www.amla.europa.eu/index_en | T2 | 수시 | 공개 | 홈페이지 뉴스 티커 |
| S-12 | ESMA | https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv | T1 | 주간 | 공개 | CASP 등록부 CSV |
| S-13 | ESMA | https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica | T2 | 수시 | 공개 | 등록부 안내·갱신일 |
| S-14 | FCA | https://www.fca.org.uk/firms/cryptoassets-information | T2 | 수시 | 공개 | 인가 신청기간 |
| S-15 | EisnerAmper | https://www.eisneramper.com/insights/cryptocurrency-insights/fca-cryptoasset-authorization-0926/ | T3 | — | 공개 | MLR 통계·활동 9종 |
| S-16 | Federal Register (PI) | https://public-inspection.federalregister.gov/2026-16796.pdf | T1 | — | 공개 | GENIUS §3 NPRM |
| S-17 | Jones Day | https://www.jonesday.com/en/insights/2026/08/us-treasury-proposes-genius-act-rules-for-stablecoin-issuance-offer-and-sale | T3 | — | 공개 | NPRM 해설 |
| S-18 | Chapman and Cutler | https://www.chapman.com/assets/htmldocuments/Chapman-GENIUS-Act-Rulemaking-and-Reporting-Tracker-081126.pdf | T3 | 수시 | 공개 | GENIUS 트래커(2026-07-16) |
| S-19 | FinCEN | https://www.fincen.gov/news/news-releases/fincen-announces-withdrawals-proposed-digital-asset-related-rules | T2 | — | 공개 | 철회 보도자료 |
| S-20 | Federal Register (PI) | https://public-inspection.federalregister.gov/2026-20429.pdf | T1 | — | 공개 | 믹싱 철회 |
| S-21 | Federal Register (PI) | https://public-inspection.federalregister.gov/2026-20430.pdf | T1 | — | 공개 | 비수탁지갑 철회 |
| S-22 | Federal Register (PI) | https://public-inspection.federalregister.gov/2026-20371.pdf | T1 | — | 공개 | A7 특별조치 NPRM |
| S-23 | FinCEN | https://www.fincen.gov/resources/statutes-regulations/federal-register-notices | T2 | 수시 | 공개 | 관보 공고 목록 |
| S-24 | FinCEN | https://www.fincen.gov/news | T2 | 수시 | 공개 | 뉴스 목록 |
| S-25 | OFAC | https://ofac.treasury.gov/recent-actions/20260917 | T1 | 일별 | 공개 | BitBank 지정 |
| S-26 | U.S. Treasury | https://home.treasury.gov/news/press-releases/sb0632/ | T2 | — | 공개 | Economic Outcast/BitBank |
| S-27 | The Block | https://theblock.co/news/regulation/2026-09-17-us-sanctions-iranian-crypto-exchange-bitbank-alleged-bitcoin-transfers-to-irgc-415462 | T4 | — | 공개 | 선행 지정 맥락 |
| S-28 | The Defiant | https://thedefiant.io/news/regulation/senate-blocks-clarity-act-49-50-with-no-democratic-votes-to-proceed | T4 | — | 공개 | CLARITY 49-50 |
| S-29 | Bitcoin.com News | https://news.bitcoin.com/clarity-act-made-126-concessions-and-still-couldnt-get-60-votes/ | T4 | — | 공개 | 표결일 2026-09-15 |
| S-30 | Decrypt | https://decrypt.co/376577/roman-storms-tornado-cash-retrial-pushed-to-april-2027 | T4 | — | 공개 | Storm 재심 |
| S-31 | Cointelegraph | https://cointelegraph.com/news/fincen-crypto-mixing-rule-legitimate-activity | T4 | — | 공개 | 철회 보도 |
| S-32 | 금융위원회 | https://www.fsc.go.kr/no010101/87499 | T2 | — | 공개 | 시행령 국무회의(2026-08-11) |
| S-33 | 금융위원회 | https://www.fsc.go.kr/no010101/87521 | T2 | — | 공개 | 신고매뉴얼 개정(08-13) |
| S-34 | 금융위원회 | https://www.fsc.go.kr/no010101/87835 | T2 | 반기 | 공개 | '26 상반기 실태조사(10-01) |
| S-35 | 금융위원회 | https://www.fsc.go.kr/no010101/87916 | T2 | — | 공개 | 사이트 차단(10-13) |
| S-36 | 금융위원회 | https://www.fsc.go.kr/no010101/87783 | T2 | — | 공개 | 불공정거래 고발(09-23) |
| S-37 | 금융위원회 | https://www.fsc.go.kr/no010101?srchKey=sj&srchText=%EA%B0%80%EC%83%81%EC%9E%90%EC%82%B0 | T2 | 수시 | 공개 | 보도자료 검색 목록 |
| S-38 | KDI 경제정보센터 | https://eiec.kdi.re.kr/policy/materialView.do?num=285286 | T2 | — | 공개 | FIU 보도자료 전재 |
| S-39 | MTN | https://news.mtn.co.kr/news-detail/2026091415254495524 | T4 | — | 공개 | 재신고·현장점검 |
| S-40 | 쿠키뉴스 | https://www.kukinews.com/article/view/kuk202604130220 | T4 | — | 공개 | 두나무 1심·코인원 |
| S-41 | 블록미디어 | https://www.blockmedia.co.kr/archives/1149080 | T4 | — | 공개 | 2026-10-08 국감 |
| S-42 | SBS Biz | https://biz.sbs.co.kr/amp/article/20000325470 | T4 | — | 공개 | 2026-07-29 업무보고 |
| S-43 | 파이낸셜뉴스 | https://www.fnnews.com/news/202605191827097795 | T4 | — | 공개 | 법인 2단계 지연 |
| S-44 | 金融庁 | https://www.fsa.go.jp/common/diet/index.html | T1 | 국회별 | 공개 | 제출·성립일 |
| S-45 | 契約ウォッチ | https://keiyaku-watch.jp/media/hourei/2026-2027-kinsyohou/ | T4 | — | 공개(일부 유료) | 공포일·시행기한 |
| S-46 | PwC Japan | https://www.pwc.com/jp/ja/knowledge/news/legal-news/legal-20260728-4.html | T3 | — | 공개 | 개정 골자 |
| S-47 | Allen & Gledhill | https://www.allenandgledhill.com/sg/perspectives/articles/33474/sgkh-mas-consults-on-amendments-to-payment-services-act-2019-to-implement-stablecoin-regulatory-framework | T3 | — | 공개 | MAS CP 상세 |
| S-48 | Baker McKenzie | https://www.bakermckenzie.com/en/insight/publications/2026/09/singapore-mas-introduces-stablecoins-framework-under-payments-legislation | T3 | — | 공개 | MAS CP |
| S-49 | SFC | https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/Virtual-assets/Virtual-asset-trading-platforms-operators/Lists-of-virtual-asset-trading-platforms | T1 | 수시 | 공개 | VATP 명단 |
| S-50 | HKMA | https://www.hkma.gov.hk/eng/regulatory-resources/registers/register-of-licensed-stablecoin-issuers/ | T1 | 수시 | 공개 | 스테이블코인 발행자 등록부 |
| S-51 | Clyde & Co | https://www.clydeco.com/en/insights/2026/05/uae-virtual-assets-update-q2-2026 | T3 | 분기 | 공개 | UAE Q2 2026 |
| S-52 | Facephi | https://facephi.com/observatory/en/vara-regulacion-cripto-emiratos-2026/ | T5 | — | 공개 | Decree-Law 10/2025 주장(미검증) |
| S-53 | Sumsub | https://sumsub.com/media/news/australia-launches-public-vasp-register-as-travel-rule-to-take-effect/ | T4 | — | 공개 | AUSTRAC 등록부·트래블룰 |
| S-54 | News on AIR | https://newsonair.gov.in/fiu-ind-cracks-down-on-15-vda-service-providers-over-pmla-non-compliance/ | T2 | — | 공개 | FIU-IND 통지 |
| S-55 | Chainalysis | https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/ | T3 | 연 1회 | 공개 | 2026 CCR 서문 |
| S-56 | TRM Labs | https://www.trmlabs.com/reports-and-whitepapers/2026-crypto-crime-report | T3 | 연 1회 | 공개(등록 유도) | 2026 CCR |
| S-57 | Elliptic | https://www.elliptic.co/blog/north-korea-linked-hackers-have-already-stolen-over-2-billion-in-2025 | T3 | — | 공개 | DPRK 2025 |
| S-58 | The Block | https://www.theblock.co/post/399569/north-korea-accounts-for-76-of-2026-crypto-hack-losses-with-theft-since-2017-topping-6-billion-trm-labs | T4 | — | 공개 | TRM 2026 YTD |

---

## 7. 일일 수집 후보 (Ingestion Hooks)

| 명칭 | 방식 | 엔드포인트 | 포맷 | 갱신빈도 | 인증 | 라이선스/주의 | 검증 |
|---|---|---|---|---|---|---|---|
| ESMA 임시 CASP 등록부 | HTTP 파일 | https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv | CSV(UTF-8 BOM, 12열) | 주간 | 불필요 | ESMA 재이용 조건; 2026 중 IT 시스템 통합 예정으로 URL 변경 가능 | **검증**(2026-10-21 curl 200, 379행) |
| 금융위 보도자료 검색 | HTML | https://www.fsc.go.kr/no010101?srchKey=sj&srchText=가상자산 | HTML 목록(글번호·일자·제목) | 일별 | 불필요 | 공공누리 확인 필요 | **검증**(2026-10-21) |
| FinCEN 연방관보 공고 목록 | HTML | https://www.fincen.gov/resources/statutes-regulations/federal-register-notices | HTML 표 | 수시 | 불필요 | 공공 저작물 | **검증** |
| FinCEN 뉴스 | HTML | https://www.fincen.gov/news | HTML 목록 | 수시 | 불필요 | 공공 저작물 | **검증**(/news-room/news 는 404) |
| OFAC Recent Actions | HTML(일자 URL) | https://ofac.treasury.gov/recent-actions/YYYYMMDD | HTML | 일별 | 불필요 | 공공 저작물; 목록 페이지는 10건만 노출 | **검증**(20260917) |
| Federal Register Public Inspection | HTTP PDF | https://public-inspection.federalregister.gov/{docnum}.pdf | PDF | 일별 | 불필요 | federalregister.gov 본문 페이지는 봇 차단(unblock 리다이렉트) | **검증**(3건 다운로드) |
| SFC VATP 명단 | HTML | https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/Virtual-assets/Virtual-asset-trading-platforms-operators/Lists-of-virtual-asset-trading-platforms | HTML 표 | 수시 | 불필요 | SFC 이용약관 | **검증** |
| HKMA 스테이블코인 발행자 등록부 | HTML | https://www.hkma.gov.hk/eng/regulatory-resources/registers/register-of-licensed-stablecoin-issuers/ | HTML 표 | 수시 | 불필요 | HKMA 약관 | **검증** |
| AMLA 홈페이지 뉴스 티커 | HTML | https://www.amla.europa.eu/index_en | HTML | 수시 | 불필요 | EU 재이용 정책; /news_en 목록은 비어 있음, RSS 링크 존재하나 URL 미확인 | **검증**(홈페이지) / RSS **미검증** |
| EBA AML 정책 페이지 | HTML | https://www.eba.europa.eu/regulation-and-policy/anti-money-laundering-and-countering-financing-terrorism | HTML | 수시 | 불필요 | — | **검증** |
| FCA 뉴스 | HTML | https://www.fca.org.uk/news | HTML 목록(최근 10건) | 일별 | 불필요 | — | **검증** |
| 재무부 보도자료 | HTML | https://home.treasury.gov/news/press-releases | HTML(10건, 페이지 파라미터 무효) | 일별 | 불필요 | 공공 저작물 | **검증**(페이지네이션 비작동) |
| FATF 공표물·총회 결과 | HTML | https://www.fatf-gafi.org/en/publications/... | HTML | 총회별 | 불필요 | **자동수집기 403** — 헤드리스 브라우저 또는 수동 | **미검증(차단)** |
| KoFIU 보도자료 | HTML | https://www.kofiu.go.kr/kor/notification/press.do | HTML | 수시 | 불필요 | 2026-10-21 수집 시 오류 페이지 | **미검증(장애)** |
| AUSTRAC 가상자산 페이지 | HTML | https://www.austrac.gov.au/about-us/legislation/updates-legislation/amlctf-transitional-rules-2026 | HTML | 수시 | 불필요 | 3회 타임아웃 | **미검증** |
| 金融庁 국회제출법안 | HTML/PDF | https://www.fsa.go.jp/common/diet/index.html | HTML + PDF | 국회별 | 불필요 | — | **검증** |

---

## 8. 미확인·다음 단계

- [ ] **FATF 10월 총회 결과**(2026-10-30 공표 예정): 회색명단 변동, 개정 R.16 최종 가이던스 채택 여부, 멕시코·미국 MER, 7차 TU 후속. 확인처: fatf-gafi.org "Outcomes FATF Plenary, 28-30 October 2026"(브라우저 접근 필요).
- [ ] **개정 R.16 이행 가이던스 최종본** 발간 여부·일자 — FATF Recommendations 페이지.
- [ ] **한국 5차 상호평가 일정 재확인** — wave1(현장방문 2028-11·총회 2029-06 잠정; FIU 계획 '28.3월) 이후 공식 갱신 유무. 확인처: FIU 보도자료, FATF 평가 캘린더.
- [ ] **AMLA 직접감독 잠정 적격목록**(2026-09 말 확정 예정)의 공개 여부와 산업 구성(CASP 포함 여부) — AMLA News & Media, 각국 NCA 공지.
- [ ] **집행위 MiCA 재검토 표적 의견수렴**의 정식 명칭·기간·후속 일정 — finance.ec.europa.eu.
- [ ] **AMLD6 전환 현황**(2026-07-10 기한 조항) 및 집행위 침해절차 — Commission infringement database.
- [ ] **특금법 시행령 개정 공포일·대통령령 번호**, 그리고 "그 외 부분"(트래블룰 기준금액 폐지 등) 시행일(공포+6개월) — 법제처 law.go.kr(수집기 본문 미출력), 관보.
- [ ] **개정 감독규정(고시) 공포·시행일** 및 1년 유예 부칙 원문 — FIU 고시.
- [ ] **재신고 기한 2026-11-20의 1차 근거**(법률 제21358호 부칙) 및 재신고 결과(수리·불수리·탈락 수) — law.go.kr, FIU 보도자료(12월 전후).
- [ ] **FIU 2026-07~10월 제재·검사 발표**(FIU 사이트 장애로 미확인), 두나무 1심 항소 여부, 빗썸·코인원 행정소송 경과 — kofiu.go.kr, 법원 판결문.
- [ ] **법인 참여 2단계 시행 발표·실명계좌 가이드라인** — 금융위 보도자료, 가상자산위원회 회의 결과.
- [ ] **디지털자산기본법 정부안 국회 제출**(의안번호·발의일) 및 계류 10건 처리 상태 — 국회 의안정보시스템.
- [ ] **일본 개정법 공포일·법률번호·정령 시행일** 1차 확인 — e-Gov 法令検索(508AC0000000064), 官報; 암호자산 이관에 따른 범수법 정비(整備法) 여부.
- [ ] **MAS 스테이블코인 의견수렴 원문**(PSA 개정안 조문·DPT 사업자 의무) 및 법안 제출 일정; DTSP 라이선스 발급 건수 — mas.gov.sg.
- [ ] **AUSTRAC 1차 자료**(등록 VASP 수, 2026-07-01 이후 집행) — austrac.gov.au(타임아웃).
- [ ] **UAE Federal Decree-Law 10/2025(AML)** 존재·내용·시행일 — UAE 관보, CBUAE/MoE; VARA 2026 트래블룰 서큘러 원문.
- [ ] **홍콩**: HKMA 스테이블코인 2차 인가 일정, SFC 탈락 집계 기준(C-06).
- [ ] **인도 정부 디지털자산 토론보고서** 발간 여부 — DEA.
- [ ] **미국**: GENIUS 하위 최종규칙 발표 여부(OCC/FDIC/NCUA/Treasury/FinCEN), FinCEN AML/CFT 프로그램 최종규칙 시점, A7 특별조치 의견마감(관보 게재+30일=2026-11-04 추정) 및 최종화, CLARITY 재토론종결 일정과 공식 롤콜 번호(senate.gov 403), OFAC 2026-10-01 A7 지정 공고 원문, 2026-06 Nobitex 등·2026-08 Shelbit·Aban Tether 지정의 OFAC 원문.
- [ ] **정량**: Elliptic 2026 연례(Typologies) 보고서 존재 여부와 수치; Chainalysis 2026 중간 업데이트(H1 2026); TRM H1 2026 보고 원문(USD 9.72억·북한 66.2%); Chainalysis "제재 주체 수취 $104B" 2차 보도 수치의 원문 확인.
- [ ] **FSB 2026-10 디지털자산 산출물**(wave1 F-137 예정) 발간 여부.

---

## 9. 기존 저장소 내용과의 차이·정정 제안

> 기준: 2026-10-21. "무엇이 → 무엇으로". 근거 F-ID 병기. 상태 용어는 proposed / enacted-not-in-force / in-force / amended / superseded / withdrawn.

| # | 파일 | 현재 서술 | 정정 제안 | 근거 |
|---|---|---|---|---|
| 1 | `notes/2-regulations/fatf.md` (TL;DR, §5, §8) | "2026 후반에 가이던스 발표 예정" | "개정 R.16 이행 가이던스 초안 의견수렴 2026-06-24~08-21 종료, 최종본 **2026-10-21 기준 미발간**(10월 총회 의제 가능성)" | F-009 |
| 2 | `notes/2-regulations/fatf.md` §7 표 | Grey List 2026 예시 "케냐, 나미비아, 필리핀 등" | 나미비아는 2026-06-19 졸업, 필리핀은 현행 22개 명단에 없음 → 예시를 "케냐·베트남·BVI·불가리아(가상자산 지적 관할)"로 교체하고 2026-06-19 기준 22개 명시 | F-002 |
| 3 | `notes/2-regulations/fatf.md` §8 표 | "Targeted Update ... 가장 최근 2025" | "가장 최근 **7차(2026-07-16)**: 트래블룰 입법 83%(91/109), 미집행 60%(55/91), R.15 LC 34%" | F-004~F-006 |
| 4 | `notes/2-regulations/fatf.md` §6·§9 | "한국 5차 2027~2028 예상" | wave1 기준 "현장방문 2028-11·총회 2029-06(잠정), FIU 계획 '28.3월" — 재확인 과제 표기 | wave1 F-018/F-029, §8 |
| 5 | `notes/2-regulations/fatf.md` §9 | "AMLA는 2028년부터 EU 40개 고위험 VASP를 직접 감독" | "AMLA 직접감독 대상은 **6개 회원국 이상에서 영업하는 신용·금융기관(그룹) 약 40개**로 2027 선정·2028 개시; VASP 전용 목록이 아님" | wave1 F-017/F-018, F-012 |
| 6 | `notes/2-regulations/eu-mica-amlr.md` TL;DR·§5 | "AMLA 2025년부터 본격 운영" (EBA 역할 언급 없음) | "2025-07-01 운영 개시, **2026-01-01 EBA AML 권한 이관**, **2026-10-01 AMLR 최초 RTS 3건 집행위 제출**, 2026-10-07 MiCA 재검토 AML 우선과제 제출" 추가 | F-010, F-011, F-013 |
| 7 | `notes/2-regulations/eu-mica-amlr.md` §2 | "2024-12-30 전면 시행" | "발효(entry into force) 2023-06-29 / **적용개시** 2024-12-30"으로 용어 분리(kb eu-mica.yaml curator_note와 일치) | kb/eu-mica.yaml |
| 8 | `notes/2-regulations/eu-mica-amlr.md` §2 | CASP 인가 통계 없음 | "ESMA 임시 등록부 2026-10-19: 379행·376 LEI(DE 109·FR 36·NL 29…)" 추가 | F-014 |
| 9 | `notes/2-regulations/eu-mica-amlr.md` §5 | "AMLA의 직접 감독 대상 40개에 들어가는지 여부가 대형 CASP의 관심사" | 선정 기준(≥6 회원국 금융기관)을 명시하고 "CASP가 포함되는지는 2026-10-21 기준 미공개"로 수정 | F-012, §8 |
| 10 | `notes/2-regulations/us-bsa-fincen.md` TL;DR·§5 | "2026-04-08 FinCEN+OFAC 합동 제안 → 시행규정 2026-07-18 마감, 전면 시행 2027-01-18" | "PPSI AML/CFT·제재 NPRM 관보 2026-04-10, **의견마감 2026-06-09**; 2026-07-18은 **법정 규칙제정 기한(경과)**; 법 시행 예상 2027-01-18(법정 최종기한); 재무부 §3 NPRM 2026-08-18(의견 10-19)" | F-017~F-019 |
| 11 | `notes/2-regulations/us-bsa-fincen.md` §2 | "2024~2025: Mixer 관련 정보수집 명령" (CVC 믹싱 §311 NPRM 상태 불명) | "CVC 믹싱 §311 NPRM(2023-10-23)은 **2026-10-06 관보 철회(withdrawn)**; 비수탁지갑 NPRM(2020-12-23)도 동일자 철회" | F-021, F-022 |
| 12 | `notes/2-regulations/us-bsa-fincen.md` §3 OFAC | Tornado Cash 해제(2025-03)까지만 기술 | 2026 제재 축 추가: "Operation Economic Outcast(2026-08-24~) — BitBank 등 이란 거래소 지정(2026-09-17, E.O. 13902); A7 Network TCO 지정(2026-10-01) + FinCEN A7 하위대리인 자금이체 금지 NPRM(2026-10-05)" | F-024~F-026 |
| 13 | `notes/2-regulations/us-bsa-fincen.md` §4 집행 | "2025년 강력한 enforcement: OKX, Paxful" | 2026 추가: "Storm 재심 2027-04-26 연기; FinCEN AML 프로그램 규칙 미최종화; CLARITY 상원 토론종결 2026-09-15 49-50 부결" | F-020, F-027, F-028 |
| 14 | `notes/2-regulations/korea-fiu-act.md` TL;DR·§1 표 | "2026-01-29 개정안 국회 통과 ... 2026년 하반기 시행 예정" | "법률 제21358호 2026-02-19 공포, **2026-08-20 시행(in-force)**(신고제·퇴직자 제재통보); 시행령 개정안 2026-08-11 국무회의 의결; 신고매뉴얼 2026-08-13 전면 개정" | F-029~F-034 |
| 15 | `notes/2-regulations/korea-fiu-act.md` §3 Travel Rule | "임계금액: 100만원(시행령 §10의10, FIU 고시)" / "한국은 100만원 임계 유지" | "100만원 기준은 **2026-10-21 현재 유효**하나 개정 시행령으로 **폐지 확정(amended, 시행은 공포 후 6개월)**; 수취 VASP 정보확보 의무, 해외·개인지갑 위험도별 차등, 1천만원 이상 자체 의심거래 관리체계" | F-032, F-033 |
| 16 | `notes/2-regulations/korea-fiu-act.md` §2 신고 | 대주주 심사 개요만 | 신고매뉴얼 세부 추가: "AML 인력 4인 이상, 전산설비 국내 소재, 대주주·법령준수체계 변경 30일 전 사전신고, 부채비율 200%(예치금 차감), 기존 사업자 1년 유예, 재신고 기한 2026-11-20(보도)" | F-031, F-034, F-035 |
| 17 | `notes/2-regulations/korea-fiu-act.md` §6 FIU 보도자료 | "2025-12-02 FIU 보도자료 ... 미신고 외국 VASP 차단" | 최신화: "2026-10-13 사이트 27건 접속차단(방미심위 10-06~07), 수사기관 통보 누적 44개, 앱마켓 차단 병행" | F-040 |
| 18 | `notes/2-regulations/korea-fiu-act.md` §4 제재 | 제재 사례 나열 | "두나무 영업일부정지 처분 취소소송 **1심 원고승(2026-04-09, 보도)**, 빗썸 소송 진행" 추가 — 제재의 사법심사 국면 | F-041 |
| 19 | `notes/2-regulations/korea-fiu-act.md` FAQ | "'Travel Rule은 100만원 이상만 해당' — 실무에선 90만원대 반복 패턴도 EDD" | 기준금액 폐지 예정 사실을 전제로 재작성 | F-032 |
| 20 | `notes/2-regulations/korea-user-protection.md` TL;DR·§8 | "2단계 입법 진행 중" | "2026-10-21 기준 **정부안 미제출, 의원안 10건 계류(proposed)**; 2026-10-08 국감 '막바지 협의'; 원화 스테이블코인 발행주체 미결" | F-036, F-037 |
| 21 | `notes/2-regulations/korea-user-protection.md` §7 | 집행 성과 2024~2025만 | "2026-07-20 시행 2년 성과 발표, 2026-07-01·09-23 고발·통보(09-23: 4건, API 초단기 시세조종 3건)" 추가 | F-039b |
| 22 | `notes/2-regulations/asia-regs.md` §3.5 | "2026 개정 자금결제법 — 2026-04 시행 예정" | "令和7年 개정 자금결제법 **2026-06-01 시행**(wave1); **별개 법**으로 금상법 이관 개정법 2026-07-15 성립·07-23 공포(令和8年法律第64号), 이관 조항 시행 ≤2027-07-23(enacted-not-in-force)" | F-042 |
| 23 | `notes/2-regulations/asia-regs.md` §4 홍콩 | VATP 수·스테이블코인 조례 언급 없음 | "VATP 인가 13개(2026-10-16), Stablecoins Ordinance 2025-08-01 시행, 발행 인가 2개(2026-04-10)" 추가 | F-046, F-047 |
| 24 | `notes/2-regulations/asia-regs.md` §1 싱가포르 | DTSP 체제·스테이블코인 법제화 언급 없음 | "FSMA Part 9 DTSP 2025-06-30 시행(wave1); **MAS PSA 개정 스테이블코인 의견수렴 2026-09-01~10-16(proposed)**" 추가 | F-044 |
| 25 | `notes/2-regulations/asia-regs.md` §2 UAE | VARA Rulebook 7개 구조 | "VARA Exchange Services Rulebook v2.1 2026-03-31; 연방 CMA 가상자산 체계 2026-04(3→8 활동)" 추가 | F-048 |
| 26 | `notes/2-regulations/asia-regs.md` 범위 | 싱가포르·UAE·일본·홍콩만 | 호주(2026-03-31 VASP 의무, 07-01 트래블룰)·인도(FIU-IND 2026-01-08 가이드라인, 2026-09-09 15개사 통지) 절 신설 제안 | F-048b, F-049 |
| 27 | `notes/2-regulations/README.md` | "마지막 업데이트: 2026-04-17" + 2026 변경 미반영 | 위 1~26 반영 후 갱신일 수정 | — |
| 28 | `README.md` 트래블룰 요약 | "트래블룰 의무는 8개 관할(국제기준·EU·영국·일본·한국·미국·홍콩·싱가포르·호주)" | 열거는 9개 — 개수 또는 목록 정합화; 한국 100만원 기준의 '폐지 확정·미시행' 상태 주석 | F-032 |
| 29 | `kb/entities/regulations/kr-tfia.yaml` | citation "법률 제21358호 (2026-08-20 시행 예정)" | "법률 제21358호 (2026-08-20 시행; 그 외 부분 공포 후 6개월)" — STATE 레코드 in-force 전환 | F-029 |
| 30 | `kb/entities/regulations/kr-tfia-sd.yaml` curator_note | "AML 실체 규정 개정(트래블룰 기준금액 폐지 등)은 2026-07-30 기준 미공포" | "2026-08-11 국무회의 의결; 공포일·대통령령 번호 확인 필요; 트래블룰 조항 시행 = 공포+6개월(enacted-not-in-force)" | F-030~F-033, §8 |
| 31 | `kb/entities/regulations/us-bsa.yaml` curator_note | "CVC 믹싱 §311 규칙(RIN 1506-AB64) proposed, 최종조치 목표 2027-12" / "위 철회 2건 모두 연방관보 공고 없음" | "믹싱 NPRM **withdrawn**(관보 2026-10-06, 공고 RIN 1506-AB47 표기)"; "비수탁지갑 NPRM 관보 철회 공고 2026-10-06 게재(85 FR 83840)" — '관보 공고 없음' 삭제 | F-021, F-022, C-02, C-03 |
| 32 | `kb/entities/regulations/eu-amlr.yaml` | RTS 언급 없음 | "AMLA RTS 3건(Art. 28(1)·19(9)·16(4)/17(3)) 2026-10-01 집행위 제출" 엣지/노트 추가 | F-011 |
| 33 | `kb/entities/regulations/intl-fatf-r16.yaml` curator_note | 세 일자(개정·이행시한·방법론) | 네 번째 일자 "guidance_consultation 2026-06-24~08-21, final = 미발간(2026-10-21)" 추가 | F-009 |
| 34 | `kb/entities/regulations/eu-mica.yaml` | 등록부 통계 없음 | "CASP 등록부 379행(2026-10-19)" DATA 참조 추가; MiCA 재검토(AMLA 의견 2026-10-07) 노트 | F-013, F-014 |
| 35 | `kb/entities/regulations/jp-aptcp.yaml` | 금상법 이관과의 관계 없음 | "2026-07 금상법 이관법 성립 — 범수법 연동 개정 여부 확인 과제" 노트 | F-042, F-043 |
| 36 | `kb/entities/regulations/hk-amlo.yaml` | VATP·스테이블코인 수치 없음 | "VATP 13(2026-10-16), 스테이블코인 발행자 2(2026-04-10)" 참조 추가 | F-046, F-047 |
| 37 | `kb/entities/regulations/sg-psn02.yaml` | PSA 개정 의견수렴 미반영 | "2026-09-01 MAS 스테이블코인 PSA 개정 CP(proposed) — PSN02 영향 검토" 노트 | F-044 |
| 38 | `kb/entities/regulations/gb-mlr2017.yaml` | FSMA 인가창 미반영 | "FSMA 인가 신청 2026-09-30~2027-02-28, 신체계 2027-10-25; MLR 등록 자동전환 없음" 노트 | F-015 |
| 39 | `kb/entities/regulations/au-amlctf.yaml` | "가상자산 관련 개정은 2026-03-31 시행" | "트래블룰 적용 2026-07-01, VASP 등록부 공개 2026-06-30, 자기수탁 지갑 보고 2029-03-31 유예(T4)" 보강 | F-048b |

**정정 우선순위(영향 큰 순)**: #15·#19·#28·#30(한국 트래블룰 100만원 — "폐지 확정이나 아직 유효"라는 두 상태를 반드시 분리) → #11·#31(미국 믹싱·비수탁지갑 규칙 withdrawn) → #14·#29(특금법 in-force 전환) → #10(GENIUS 날짜 오귀속) → #1·#3(FATF 가이던스·7차 TU) → #22(일본 두 법 혼동) → 나머지.
