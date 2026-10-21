---
dossier_id: 2026-10-travel-rule
title: 가상자산 트래블룰 관할별 현황 — 2026-10-21 기준 전면 재검증
domain: regulation
as_of: 2026-10-21
coverage: FATF(R.16 2025-06 개정·INR.15 §7(b)·7차 Targeted Update 2026-07) / 핵심 9관할(한국·EU·영국·미국·일본·싱가포르·홍콩·호주 + FATF) / 보조 8관할(UAE·스위스·캐나다·인도·브라질·대만·태국·인도네시아) / 프로토콜·솔루션 11종 + IVMS101 / 집행 2024~2026 / 개인정보·스테이블코인·DeFi·데이터품질
confidence_overall: B
sources_total: 101
baseline: notes/3-crypto-aml/travel-rule.md(2026-08-04) · notes/4-technology/travel-rule-protocols.md(2026-04-17) · notes/7-vendors/travel-rule-vendors.md(2026-04-17) · kb/entities/regulations/*/provisions/*.yaml(트래블룰 10건) · kb/facts/contradictions.jsonl(CTR:00002·00004·00006)
---

> **수집 조건 메모(2026-10-21)**: ① fatf-gafi.org 는 모든 경로에서 HTTP 403 을 반환해 FATF 1차 문서(R.16 개정문·7차 Targeted Update PDF·Annex IV)를 직접 열지 못했다. FATF 관련 수치는 T2(CSSF·FIAU Malta·OJK)와 T3/T4 요약의 교차일치로만 확정했고 확신도를 B 이하로 두었다. ② EUR-Lex 는 본문 없는 응답만 반환했다. TFR 조문은 저장소가 2026-07-31 CELLAR 로 확보한 T1 문언을 그대로 쓰고, 2026-10-21 재확인 불가로 표기했다. ③ 법제처 DRF API(`OC=test`)로 한국 시행령·감독규정의 **현행본과 시행예정본을 조문 단위로 직접 확보**했다. ④ 세션 WebSearch 한도 소진 후에는 알고 있는 URL 의 직접 열람과 공공 API(법제처 DRF·e-Gov·Federal Register·reginfo·Crossref·arXiv)만 사용했다.

## 1. BLUF — 핵심 결론

- **한국 트래블룰 기준금액(100만원) 폐지는 `enacted-not-in-force` 다.** 대통령령 제36592호(공포 2026-08-18)가 제10조의10 제1호를 「가상자산을 이전하는 **모든 경우**」로 개정했고, 부칙 제1조 단서가 이 조문을 「공포 후 6개월이 경과한 날」로 유예했다. 법제처 시행일 색인의 시행예정 판본은 **2027-02-19** 를 가리킨다 — 언론의 「2027-02-20」과 하루 다르다. 2026-10-21 현재 효력 있는 제10조의10 제1호는 여전히 「1백만원 이상」이다 [F-011][F-012][F-013][F-014]
- **한국은 2027-02-19 부터 '이전 상대방 유형별 허용 규율'을 갖는다.** 시행령 제10조의20 제7호·제8호와 감독규정(FIU 고시 제2026-2호) 제28조의2 가 해외 가상자산사업자를 저위험(FATF 이행국·동등 AML·인허가 → 허용, 단 제10조의10 제2호 정보 확보)/중간(고객과 상대방이 **동일인**일 때만 허용)/고위험(FATF 고위험국·무인허가 → 제한)으로 가르고, 「독점적 관리 권한이 없는 가상자산주소」(= 자기수탁 지갑)는 **동일인 이전만 허용**한다. 입법예고안의 「1,000만원 이상 일률 의심거래보고」는 최종안에서 「1천만원 이상 자체 의심거래 감시체계」로 바뀌었다 [F-015][F-017][F-018][F-020]
- **영국은 2026-06-30 에 정보 심화 기준을 「1,000 euros」에서 「£800」으로 바꿨다.** S.I. 2026/621 규정 32·33 이 reg 64C(4)와 reg 64G(1)(b)의 금액을 치환했다. 저장소 산문·KB 의 「£800」은 결과적으로 맞지만, 2023-09-01 원문은 유로였고 개정 연혁이 KB 에 없다. 같은 개정령이 암호자산 사업자 간 코레스 관계 강화 CDD(reg 34A)를 신설했고 이는 **2027-02-01 시행 예정**이다 [F-030][F-031][F-034]
- **FATF 7차 Targeted Update(2026-07-16)**: 조사대상 109 관할 중 **91(83%)** 이 트래블룰 입법 완료(6차 2025 대비 73%→83%), 11 관할 입법 진행 중, 입법 완료 관할의 **55(60%)** 는 감독·집행 조치가 한 건도 없음. FATF 는 「persistent gaps in Travel Rule implementation remain a serious concern」(¶26)이라 썼다. Sunrise 쟁점은 '입법 격차'에서 '집행 격차'로 이동했다 [F-005][F-008]
- **FATF R.16 개정(2025-06 총회 채택)의 1차 문언은 재확인하지 못했다.** T2 요약(CSSF·FIAU·OJK)으로 확인되는 것은: ① 지급 사슬상 책임 명확화 ② 국경 간 P2P 지급 USD/EUR 1,000 초과 표준화 정보 ③ 사기·오류 방지 기술(수취인 계좌 확인) ④ 상품·서비스 구매의 카드결제 제외 ⑤ 2030년 말 이행. 가상자산 관련 변경은 INR.15 §7 각주의 참조 갱신(결과적 개정)뿐이다. 「구조화 데이터·ISO 20022 정합」 서술은 미확인으로 남겼다. 이행 가이던스 초안은 2026-06-24 공개협의(마감 2026-08-21) [F-001][F-002][F-003][F-004]
- **미국은 변동 없음이 확정이다.** 31 CFR 1010.410(f) $3,000 현행, $250 하향안(RIN 1506-AB41)은 2025-04-16 철회(Spring 2025 Unified Agenda), 1010.410 에 걸린 미시행 개정(89 FR 72274)은 투자자문업자 AML 규칙의 (e)(6) 제외목록 수정이며 2028-01-01 로 연기 — 가상자산 트래블룰과 무관. GENIUS 법 하위 NPRM(2026-04-10)은 허가 스테이블코인 발행자를 BSA 금융기관으로 편입하며, 재무부 2026-03 보고서는 DASP 에 Travel Rule 이 $3,000 이상에서 적용됨을 재확인 [F-036][F-037][F-038][F-039][F-040]
- **집행: 2024-01-01~2026-10-21 사이 트래블룰 위반을 독립 제재사유로 명시한 사건을 어느 관할에서도 찾지 못했다.** 한국 4대 거래소 제재(두나무 과태료 352억 등)는 미신고 사업자 거래·고객확인·거래제한·STR 위반이 사유다. 가장 근접한 사례는 캐나다 FINTRAC 의 Xeltox(Cryptomus) C$176,960,190 (2025-10-22) — 「Travel rule」이 컴플라이언스 정책 결함 항목 중 하나로 언급됨 [F-022][F-053][F-041]
- **EBA 트래블룰 가이드라인(EBA/GL/2024/11, 2024-07-04, 적용 2024-12-30)이 자기수탁 검증 방법을 열거한다**: 원격 온보딩 검증·소액 송금(Satoshi test)·메시지 서명·기타 기술적 수단 중 **최소 1종**, 불충분하면 조합, 확인 후 화이트리스트 허용. EUR 1,000 판정은 수수료 제외·이전 시점 환율. 기술적 한계 보완 유예는 2025-07-31 종료 [F-024][F-025][F-026][F-027]
- **IVMS101 현행판은 「IVMS 101.2023」(2023-08 발행, Issue 1 FINAL; ISWG 가 2024-06-04 갱신 공표)** 이다. 저장소 산문의 「IVMS101 v2」 전망은 근거가 없다. 2023판은 PayloadVersionCode(101 / 101.2023), LEI 제약(C9~C11), 주소유형 GEOG, 자연인 originator 필수항목 제약 C1 을 정식화한다 [F-059][F-060]
- **프로토콜 지형 2026-10**: Notabene(2,000+ VASP 주장, 2026-07-23 Ripple 전략투자)·Sumsub(5개 프로토콜)·CODE(350+ VASP, VerifyVASP·GTR·Sumsub·Sygna·Notabene·CryptoSwift 연동)·VerifyVASP(150+)·GTR(Infozone, Singapore)·TRISA(Envoy 노드로 TRP 겸용; trisa.io 접속불가)·OpenVASP TRP(활동 중)·TRUST(125+, 폐쇄형)·Sygna(운영 중)·Shyft Veriscope(**중단**, T3 단일출처)·21 Analytics(도메인 .co 이전). Notabene 은 TRP **1.0** 엔드포인트만 지원한다고 자인 [F-061]~[F-071]
- **보조 관할 중 기준일 직전 변동 2건**: 대만 금관회 2026-08-04 트래블룰 2단계 시행 계획 발표(국내 VASP 간 2026-10 → 국경 간 2027년 말), 태국 SEC 2026-09-02 최종안 발표(준수기한 2027-02-27, 자기수탁 지갑 소유·통제 검증 의무). 브라질 Res. BCB 520(2026-02-02 발효)은 2028-02-02 전면 의무화, 인도네시아 SEOJK 16/2025 는 USD 1,000 이상/미만 2단 정보 [F-056][F-057][F-055][F-058]
- **저장소 정정 필요 항목(§9 상세)**: 산문 §9 「2026 후반 가이던스 발표 예정」→ 초안은 2026-06-24 공개; KB `REG:kr-tfia` citation(현행 법률 제21857호 누락) · `REG:kr-tfia-sd`(제36592호·제36728호 누락) · `PROV:gb-mlr2017-reg64c`(S.I. 2026/621 연혁) · `PROV:us-bsa-cfr1010-410f`(89 FR 72274 의 실체) · 산문 §6 「외부지갑 등록제 = 법령 미요구」(2027-02-19 부터 틀림) · 벤더 산문의 가격·점유율·SLA 수치(출처 없음)

## 2. 엔티티 목록

| entity_id | 명칭(원어/한글) | 유형 | 관할 | 상태 | 발효/최신일 | 근거 |
|---|---|---|---|---|---|---|
| reg:intl-fatf-r16-2025 | FATF Recommendation 16 (Payment transparency) 2025 개정 | 국제기준 | INTL | amended(standard) / 이행시한 2030-12-31 | 2025-06 총회 채택 | F-001, F-002 |
| reg:intl-fatf-inr15-p7b | INR.15 §7(b) 가상자산 이체 정보요건 | 국제기준 | INTL | in-force(soft law) | 2019-06 / 각주 결과적 개정 2025-06 | F-003, F-009 |
| doc:intl-fatf-7th-targeted-update | 7th Targeted Update on VA/VASPs | 보고서 | INTL | published | 2026-07-16 | F-005~F-008 |
| doc:intl-fatf-r16-guidance-draft | R.16 이행 가이던스 초안(공개협의) | 가이던스 | INTL | proposed(consultation closed 2026-08-21) | 2026-06-24 | F-004 |
| reg:kr-tfia | 특정 금융거래정보의 보고 및 이용 등에 관한 법률 | 법률 | KR | in-force(법률 제21857호, 타법개정) | 2026-10-02 | F-021 |
| reg:kr-tfia-sd-36592 | 특금법 시행령 일부개정(대통령령 제36592호) | 시행령 | KR | in-force(본칙) / **enacted-not-in-force**(제10조의10·제10조의20 → 2027-02-19) | 공포 2026-08-18 | F-011~F-015 |
| reg:kr-tfia-sd-36728 | 특금법 시행령 타법개정(대통령령 제36728호) | 시행령 | KR | in-force | 2026-10-02 | F-012 |
| reg:kr-fiu-supervisory-rule-2026-2 | 특정 금융거래정보 보고 및 감독규정(FIU 고시 제2026-2호) | 고시 | KR | in-force(본칙) / enacted-not-in-force(제26조·제28조의2·제31조제3호) | 2026-08-20 | F-016~F-019 |
| reg:kr-fiu-supervisory-rule-2026-3 | 동 감독규정 일부개정(FIU 고시 제2026-3호) | 고시 | KR | in-force | 2026-10-02 | F-016 |
| reg:eu-tfr-2023-1113 | Regulation (EU) 2023/1113 (TFR) | 규정 | EU | in-force | 적용 2024-12-30 | F-023 |
| reg:eu-eba-gl-2024-11 | EBA Travel Rule Guidelines EBA/GL/2024/11 | 가이드라인 | EU | in-force | 2024-12-30 (유예 종료 2025-07-31) | F-024~F-029 |
| reg:gb-mlr2017-part7a | MLR 2017 Part 7A (regs 64A–64H) | 규정 | GB | in-force / amended 2026-06-30 | 2023-09-01 | F-030~F-033 |
| reg:gb-si-2026-621 | Money Laundering and Terrorist Financing (Amendment) Regulations 2026 (S.I. 2026/621) | 개정령 | GB | in-force(대부분) / enacted-not-in-force(reg 34A → 2027-02-01) | 2026-06-30 | F-031, F-034 |
| reg:us-bsa-1010-410f | 31 CFR 1010.410(f) | 규정 | US | in-force | — | F-036 |
| reg:us-rin-1506-ab41 | FinCEN/FRB $250 임계 하향 NPRM | 제안 | US | **withdrawn** 2025-04-16 | NPRM 2020-10-27 | F-037 |
| reg:us-genius-ppsi-nprm | PPSI AML/CFT·제재 NPRM (FR 2026-06963) | 제안 | US | proposed | 2026-04-10 | F-039 |
| reg:jp-aptcp-art10-5 | 犯罪収益移転防止法 第十条の五 | 법률 | JP | in-force | 2023-06-01 | F-042, F-043 |
| reg:sg-psn02 | MAS Notice PSN02 (2025-06-30 개정판) | 고시 | SG | in-force / amended 2025-07-01 | 2024-04-04 | F-045~F-047 |
| reg:hk-amlo-sch2-s13a | AMLO Cap.615 Sch.2 s.13A | 법률 | HK | in-force | 2023-06-01 (즉시전송 2024-01-01) | F-048, F-049 |
| reg:au-amlctf-s66a + Rules 2025 | AML/CTF Act s 66A · AML/CTF Rules 2025 Part 8 | 법률·규칙 | AU | in-force | 2026-03-31 | F-050 |
| reg:ae-vara-rulebook-iii-g | VARA Compliance & Risk Management Rulebook Part III.G | 규칙 | AE(Dubai) | in-force | 판본 2025-05-19 | F-051 |
| reg:ch-gwv-finma-art10 | Art. 10 GwV-FINMA + FINMA Aufsichtsmitteilung 02/2019 | 규정·가이던스 | CH | in-force | 2019-08-26 | F-052 |
| reg:ca-pcmltfr-s124-1 | PCMLTFR s. 124.1 | 규정 | CA | in-force | 2021-06-01 | F-053 |
| reg:in-fiu-vda-guidelines | FIU-IND AML/CFT Guidelines for VDA SPs | 가이드라인 | IN | in-force / updated 2026-01-08(T3) | 2023-03-10 | F-054 |
| reg:br-res-bcb-520 | Resolução BCB nº 520/2025 | 규정 | BR | in-force(단계 이행; 전면 2028-02-02) | 2026-02-02 | F-055 |
| reg:tw-vasp-aml-reg-art7 | 提供虛擬資產服務之事業或人員防制洗錢及打擊資恐辦法 第7條 | 규칙 | TW | enacted-not-in-force(시행일 별도 지정) | 2024-11-30(본칙) | F-056 |
| reg:th-sec-travel-rule-2026 | SEC Thailand 트래블룰 고시(2026-09-02 발표) | 고시 | TH | enacted-not-in-force(준수기한 2027-02-27) | 2026-09-02 | F-057 |
| reg:id-seojk-16-2025 | SEOJK No. 16/SEOJK.07/2025 | 회람 | ID | in-force | 2025-07-03 | F-058 |
| std:ivms101-2023 | IVMS 101.2023 (interVASP ISWG) | 표준 | INTL | current | 2023-08 / 2024-06-04 갱신 | F-059, F-060 |
| vnd:notabene · vnd:sumsub · vnd:verifyvasp · vnd:code · vnd:gtr · vnd:trisa · vnd:openvasp-trp · vnd:shyft-veriscope · vnd:sygna · vnd:21analytics · vnd:trust | 솔루션·프로토콜 11종 | 벤더/프로토콜 | 다수 | §4 참조 | — | F-061~F-071 |

## 2A. 관할 비교표 — 의무 조문 · 수치 조문 · 유형 · 금액 · 자기수탁 · 시행일 · 확신도 (2026-10-21 기준)

유형 범례 — **A**: 의무 자체에 금액이 붙음(미만이면 대상 아님) / **B**: 의무는 전건, 금액은 정보 항목(또는 신원확인)의 깊이만 가름 / **C**: 어떤 금액도 없음. 경계값 문언을 괄호에 적었다. 상태는 BRIEF §0-5 용어.

| 관할 | 의무 부과 조문 | 수치 조문 | 유형 | 금액·통화(경계 문언) | 자기수탁(unhosted) 취급 | 시행일 | 상태 | 2026-08-04 이후 변경 | 확신도 |
|---|---|---|---|---|---|---|---|---|---|
| FATF | INR.15 §7(b) | — (§7(a) USD/EUR 1,000 은 CDD) | C | 없음 | R.15 가이던스(2021) 위험기반; 7차 Update 「higher-risk unhosted wallet activity」 모니터링 권고 | 2019-06 | in-force(soft law) | 7차 Update 2026-07-16; R.16 가이던스 초안 2026-06-24 | A(문언)/B(2026 사안) |
| 한국 (현행) | 특금법 §5-3 (+§6③ 위임) | 시행령 §10-10 ①호 「1백만원 이상」 | **A** | KRW 1,000,000 이상 | 법령 미규율(거래소 자율 등록제) | 2022-03-25 | in-force → **2027-02-18 까지** | 대통령령 제36592호 공포 2026-08-18 | **A** |
| 한국 (2027-02-19~) | 특금법 §5-3 | 시행령 §10-10 ①호 「모든 경우」 / §10-20 ⑦나·감독규정 §28-2③ 「1천만원」(감시체계) | **B→C 전환**(의무 전건; 1천만원은 감시체계 발동) | 정보제공: 없음 / 자체 의심거래 감시체계: KRW 10,000,000 이상 | §10-20 ⑧ + 감독규정 §28-2④: **고객과 상대방 동일인일 때만 허용**, 현저한 고위험은 제한 | 2027-02-19 | **enacted-not-in-force** | 신설 | **A** |
| EU | TFR Art 14(1)·15·16 | — (Art 14(5)·16(2) EUR 1 000 은 자기수탁 소유 평가 발동) | **B'**(전건 동일 정보; 금액은 자기수탁 검증만) | 정보: 없음 / 자기수탁 검증: EUR 1 000 「amounts to or exceeds」 | Art 14(5)·16(2) + EBA GL §81~89: 검증 5방법 중 1 이상, 화이트리스트 | 2024-12-30 (유예 2025-07-31) | in-force | 없음(확인 범위) | A(EBA)/B(TFR 재확인 불가) |
| 영국 | MLR 2017 reg 64C(1) | reg 64C(4) 「equals or exceeds … **£800**」(연결 이전 합산) | B | 기본: 없음 / 심화: GBP 800 이상 | reg 64G: 수익자 측이 정보 요청 가능(£800 이상 시 심화정보), 미수령 시 지급 불가 | 2023-09-01 | in-force / amended 2026-06-30 | S.I. 2026/621 (€1,000→£800; reg 34A 2027-02-01) | **A** |
| 미국 | 31 CFR 1010.410(f) (MSB 정의 경유) | 동 조문 「$3,000 or more」 | **A** | USD 3,000 이상 | 명시 규정 없음(2020-12 NPRM 미채택) | — | in-force | 없음; $250 안 철회 2025-04-16 확정 | A |
| 일본 | 犯収法 §10-5 | — (施行規則 §31-7 항목만; 「十万円を超える」는 CDD) | C | 없음 | 법령상 통지 대상 외; FSA 2025-06 「対象外ウォレット」 정보 보존 요구는 **미확인** | 2023-06-01 | in-force | 없음(확인 범위) | A(조문)/B(시행일) |
| 싱가포르 | PSN02 ¶13.3~13.11 | ¶13.4 「below or equal to S$1,500」 / ¶13.6 「exceeds S$1,500」 | B(+신원확인·검증) | 기본: 없음 / 심화+검증: SGD 1,500 초과 | ¶13 에 unhosted 명시 조항 없음(확인 범위) | 2024-04-04 (개정 2025-07-01) | in-force | 없음 | **A** |
| 홍콩 | AMLO Sch.2 s.13A(1)·(4) | s.13A(2)·(3) 「not less than $8,000」 | B | 기본: 없음 / 심화: HKD 8,000 이상 | SFC 지침: 자기수탁 이전도 정보 수집·위험평가(21 Analytics 요약) | 2023-06-01 (즉시전송 2024-01-01) | in-force | 없음 | A(KB)/B(2차) |
| 호주 | AML/CTF Act s 66A(3) (→ s 64(3)) | AML/CTF Rules 2025 Part 8 (항목 위임; 금액 기준 **미확인**) | C(법률) / Rules 미확인 | 법률상 없음 | s 66A(2)(d) 「self-hosted wallet controlled by the payee」 실사 분류 | 2026-03-31 | in-force | 없음(확인 범위) | A(법률)/C(Rules) |
| UAE(VARA) | Rulebook Part III.G ¶2·¶3 | 동 ¶2 「exceeding AED 3,500」 | **A** | AED 3,500 초과 | ¶7 「non-obliged entities (i.e. unhosted VA Wallets)」 위험 고려 의무만 | 판본 2025-05-19 | in-force | 없음(확인 범위) | A(VARA)/CBUAE·ADGM 미확인 |
| 스위스 | Art. 10 GwV-FINMA + FINMA 02/2019 | — (Art. 51a CHF 1,000 은 CDD) | C | 없음 | 외부지갑: 자기 고객 소유 기술적 증명 시만 허용, 제3자 지갑은 신원확인+증명 | 2019-08-26 | in-force | 없음 | A |
| 캐나다 | PCMLTFR s. 124.1 | 기록의무 발동(CAD 1,000 설은 T3, **미확인**) | C(조문)/연계 | 조문상 없음 | FINTRAC 지침 미언급 | 2021-06-01 | in-force(2026-09-30 통합본) | 없음 | A(조문)/C(기록 임계) |
| 인도 | PMLA + FIU-IND VDA 가이드라인 | 임계 없음(T3) | C(T3) | 없음 | 비호스팅 지갑 = 고위험 범주 | 2023-03-10 (갱신 2026-01-08, T3) | in-force | 없음(확인 범위) | B/C |
| 브라질 | Res. BCB 520 Art. 44 §único | 없음 | C | 없음 | Art. 59 §2 고지의무; Res. 521 외환 규율(T3) | 2026-02-02 (국내 ≈2027-02 / 전면 2028-02-02) | in-force(단계) | Art. 91 (2026-10-30 무허가 상대방 금지) 임박 | A |
| 대만 | VASP AML 辦法 第7條 | NT$30,000 초과 심화(T3) | B(T3) | 기본 없음 / 심화 TWD 30,000 초과 | 미규정(T3) | 미시행(FSC 별도 지정) | enacted-not-in-force | FSC 2026-08-04 2단계 계획 | B |
| 태국 | SEC 고시(2026-09-02 발표) | THB 30,000 설(T4, **미확인**) | B(미확인) | 미확인 | 자기수탁 지갑 소유·통제 검증 의무 | 준수기한 2027-02-27 | enacted-not-in-force | 신설 | B/D |
| 인도네시아 | SEOJK 16/SEOJK.07/2025 | 동 회람·FAQ 「USD1.000 atau lebih」 | B | 기본 없음 / 전체정보 USD 1,000 이상 | FAQ 에 명시 의무 없음 | 2025-07-03 | in-force | 없음 | A |

**경계값 재확인**: 영국 £800 「equals or exceeds」(상위) · 홍콩 HK$8,000 「not less than」(상위) · 싱가포르 S$1,500 「exceeds」(정확히 1,500 은 하위) · UAE AED 3,500 「exceeding」(정확히 3,500 은 대상 외) · 인도네시아 USD 1,000 「atau lebih」(상위) · EU EUR 1 000 「amounts to or exceeds」(상위, 자기수탁 검증) · 일본 十万円 「超える」(CDD; 정확히 10만엔 제외).

## 3. 타임라인

| 일자 | 사건 | 관할 | 중요도 | 근거 |
|---|---|---|---|---|
| 2019-08-26 | FINMA Aufsichtsmitteilung 02/2019 — Art.10 GwV-FINMA 블록체인 지급 적용, 외부지갑 소유 증명 요구 | CH | M | F-052 |
| 2020-10-27 | FinCEN·FRB $3,000→$250 임계 하향 NPRM (85 FR 68005) | US | M | F-037 |
| 2021-06-01 | PCMLTFR s.124.1 가상통화 트래블룰 시행 | CA | M | F-053 |
| 2022-03-25 | 한국 트래블룰(시행령 §10-10, 100만원) 시행 | KR | H | F-014 |
| 2023-06-01 | 일본 犯収法 §10-5 시행 / 홍콩 AMLO 개정·VATP 체제 시행(즉시전송 유예 2024-01-01 까지) | JP·HK | H | F-043, F-048 |
| 2023-08 | IVMS 101.2023 발행 | INTL | M | F-059 |
| 2023-09-01 | 영국 MLR 2017 Part 7A 시행(S.I. 2022/860) — reg 64C(4) 「1,000 euros」 | GB | H | F-030 |
| 2024-04-04 | MAS PSN02(2024-04-02 판) 효력 | SG | M | F-045 |
| 2024-07-04 | EBA/GL/2024/11 발표 | EU | H | F-024 |
| 2024-12-30 | TFR 2023/1113 적용 개시 · EBA GL 적용 | EU | H | F-023, F-024 |
| 2025-04-16 | RIN 1506-AB41($250 안) 철회 | US | M | F-037 |
| 2025-06 (총회) | FATF R.16 「Payment transparency」 개정 채택(이행 2030 말) | INTL | H | F-001 |
| 2025-07-03 | 인도네시아 SEOJK 16/2025 발효 | ID | M | F-058 |
| 2025-07-31 | EBA GL ¶24 기술적 한계 보완 유예 종료 | EU | M | F-025 |
| 2025-10-22 | FINTRAC, Xeltox(Cryptomus) C$176.96M AMP 공표 | CA | M | F-053 |
| 2025-11-06 | 두나무 과태료 352억원 결정 발표 | KR | M | F-022 |
| 2026-01-29 | 특금법 개정안 국회 본회의 통과(대주주 심사) | KR | M | F-021 |
| 2026-02-02 | Res. BCB 520 발효 | BR | M | F-055 |
| 2026-02-19 | 특금법 법률 제21358호 공포(시행 2026-08-20) | KR | H | F-021 |
| 2026-03-30 | 특금법 시행령·감독규정 개정안 입법예고(~05-11) — 1,000만원 일률 STR 안 | KR | M | F-020 |
| 2026-03-31 | 호주 AML/CTF Rules 2025 시행(s 66A 가상자산 이전) | AU | H | F-050 |
| 2026-04-10 | FinCEN·OFAC PPSI AML/CFT NPRM (FR 2026-06963) | US | M | F-039 |
| 2026-06-09 / 06-30 | S.I. 2026/621 제정 / 시행 — reg 64C(4)·64G(1)(b) €1,000→£800 | GB | H | F-031 |
| 2026-06-24 | FATF R.16 가이던스 초안 공개협의 개시(마감 08-21) | INTL | H | F-004 |
| 2026-07-16 | FATF 7차 Targeted Update 발표 | INTL | H | F-005 |
| 2026-08-04 | 대만 FSC 트래블룰 2단계 시행 계획 발표 / 특금법 법률 제21857호(타법개정) 공포 | TW·KR | M | F-056, F-021 |
| 2026-08-11 | 특금법 시행령 개정안 국무회의 의결 | KR | H | F-010 |
| 2026-08-18 | 대통령령 제36592호 공포 | KR | H | F-011 |
| 2026-08-20 | 시행령 본칙·감독규정 제2026-2호 시행 (제10조의10 등은 유예) | KR | H | F-011, F-016 |
| 2026-09-02 | 태국 SEC 트래블룰 최종안 발표(준수 2027-02-27) | TH | M | F-057 |
| **2026-10-30** | 브라질 Art. 91 — 무허가 상대방과의 가상자산 거래 금지 발효 | BR | M | F-055 |
| **2027-02-01** | 영국 reg 34A(암호자산 코레스 관계 강화 CDD) 시행 | GB | M | F-034 |
| **2027-02-19** | 한국 시행령 §10-10(기준금액 폐지)·§10-20 시행 (감독규정 §28-2 는 「공포 후 6개월」 — 별도 산정 필요) | KR | H | F-012, F-019 |
| **2027-02-27** | 태국 준수기한 | TH | M | F-057 |
| **2028-02-02** | 브라질 Art. 44 전면 의무화 | BR | M | F-055 |
| **2030-12-31** | FATF R.16 개정 이행 기대시한 | INTL | H | F-001 |

## 4. 원자적 사실 (Atomic Facts)

### 4.1 FATF
```
F-001
claim: FATF 는 2025-06 총회에서 R.16 개정(표제 「Payment transparency」)에 합의했고, 변경은 2030년 말까지 전면 이행되어야 하며, 가상자산 맥락에서 「Travel Rule」로도 불린다.
entity: reg:intl-fatf-r16-2025
source_url: https://www.cssf.lu/en/Document/fatf-enhances-transparency-in-payments-through-the-modification-to-the-recommendation-16-of-its-standard/ ; https://ojk.go.id/apu-ppt/id/berita-dan-kegiatan/publikasi/Pages/FATF-Recommendation-Updated-Juni-2025.aspx
publisher: CSSF(룩셈부르크) 2025-06-18 ; OJK(인도네시아) 2025-06-18
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "The changes to Recommendation 16 of the FATF standard … were agreed by members at the FATF's June 2025 Plenary meeting." / "also referred to as the 'Travel Rule' in the context of virtual assets."
note: FATF 원문 페이지(update-Recommendation-16-payment-transparency-june-2025.html)는 2026-10-21 HTTP 403. CSSF 문언은 「ensure consistency of information required in payment messages」까지만 — 「구조화 데이터·ISO 20022」 명시는 미확인.
F-002
claim: FIAU Malta 요약(2025-06-26)에 따르면 R.16 개정은 ① 지급 사슬상 정보 포함·불변 유지 책임 주체 명확화 ② USD/EUR 1,000 초과 국경 간 P2P 지급의 표준화 정보요건 ③ 사기·오류 방지 신기술 채택 의무 ④ 「purchase of goods and services」 정의 명확화를 담고, OJK 요약은 수취인 계좌 확인(payee account verification)과 카드결제 제외 조건을 덧붙인다.
entity: reg:intl-fatf-r16-2025
source_url: https://fiaumalta.org/?p=14978 ; https://ojk.go.id/apu-ppt/id/berita-dan-kegiatan/publikasi/Pages/FATF-Recommendation-Updated-Juni-2025.aspx
publisher: FIAU Malta ; OJK
tier: T2
confidence: B
retrieved: 2026-10-21
quote: "The changes will come into effect by the end of 2030." (FIAU)
note: 두 FIU 의 2차 요약이며 INR.16 조문 번호·필드 목록(이름·주소·생년월일 등)은 확보하지 못했다. 저장소 산문 §9 의 「VASP 는 별도 tailored framework」 서술을 뒷받침하는 1차 문언도 미확보.
F-003
claim: 2025-06 개정의 가상자산 관련 변경은 INR.15 제7항 각주(OJK 표기 「footnote 46」)가 R.16 의 해당 단락을 참조하도록 바꾼 결과적 개정에 그친다.
entity: reg:intl-fatf-inr15-p7b
source_url: https://ojk.go.id/apu-ppt/id/berita-dan-kegiatan/publikasi/Pages/FATF-Recommendation-Updated-Juni-2025.aspx
publisher: OJK
tier: T2
confidence: B
retrieved: 2026-10-21
quote: (OJK 요약) footnote 46 to paragraph 7 of the INR.15 Interpretive Note now refers to the relevant paragraphs of R.16.
note: 저장소 KB(PROV:intl-fatf-inr15-p7b)는 같은 각주를 「[48] As defined in INR. 16, paragraph 9」로 등재(2026-07-30 PDF p.80). 각주 번호 46 vs 48 은 판본 차이이거나 OJK 오기 — 1차 PDF 재확인 필요(§5·§8).
F-004
claim: FATF 는 2026-06-24 R.16 이행 가이던스 초안 공개협의를 개시했고(마감 2026-08-21), 질의 주제는 ① 오지급 탐지·방지(개정 기준의 「three options for alignment checks」) ② 저역량 관할의 금융포용 ③ 디지털 월렛·모바일머니 적용 ④ 데이터보호·프라이버시와의 조화다. 가상자산·VASP 는 협의문 요약에 언급되지 않는다.
entity: doc:intl-fatf-r16-guidance-draft
source_url: https://finreg.aoshearman.com/fatf-consults-on-guidance-to-increase-payment-transparency ; https://fiaumalta.org/news/latest-updates-from-the-fatf/ ; https://www.neopay.co.uk/fatf-launches-public-consultation-on-guidance-to-increase-payment-transparency/
publisher: A&O Shearman(2026-06-24) ; FIAU Malta(2026-07-01) ; Neopay(2026-07-23)
tier: T3 / T2 / T4
confidence: B
retrieved: 2026-10-21
quote: "Please send your response by Friday 21 August 2026" (FIAU/Neopay 인용) ; "three options for alignment checks foreseen in the revised Standard"
note: 저장소 산문 §9 「2026 후반 가이던스 발표 예정」은 초안 공개 시점(2026-06-24) 기준으로 낡았다. 최종 가이던스 채택 여부는 2026-10-21 기준 미확인.
F-005
claim: FATF 7차 Targeted Update(2026-07-16 발표)는 R.15 기술적 준수 평가 149 관할·트래블룰 설문 109 관할을 다루며, 109 중 91(83%)이 트래블룰 입법 완료(2025 년 73% 대비), 11 관할이 입법 진행 중, 입법 완료 91 중 55(60%)는 트래블룰 관련 지적·지시·감독·집행 조치가 전무하다.
entity: doc:intl-fatf-7th-targeted-update
source_url: https://vaspnet.com/articles/from-rules-to-results-fatfs-seventh-targeted-update-on-virtual-assets-and-vasps ; https://notabene.id/post/fatfs-seventh-targeted-update-on-virtual-assets ; https://financialcrime.lu/2026/07/16/FATF-Virtual-Assets-7th-Targeted-Update/
publisher: VASPnet ; Notabene(2026-07-17) ; financialcrime.lu(2026-07-16)
tier: T4 / T3 / T4
confidence: B
retrieved: 2026-10-21
quote: "The persistent gaps in Travel Rule implementation remain a serious concern." (FATF ¶26, VASPnet 전재) ; "83% (91 of 109) of surveyed jurisdictions have Travel Rule legislation in force" (Notabene)
note: FATF 페이지·PDF 403. 발표일은 FATF 검색 색인·VASPnet·financialcrime.lu 가 07-16, Notabene 본문은 07-15, CMS 페이지 날짜 07-20 — 07-16 채택. financialcrime.lu 는 「almost half … no supervisory or enforcement action」로 표현해 55/91(60%)과 어긋남 → §5.
F-006
claim: 같은 보고서에서 인허가·등록을 요구하는 관할은 응답자의 73% 이나 실제로 VASP 를 인허가·등록한 관할은 58% 이고, R.15 인허가 기준을 충족한 관할은 40%, 금지(prohibition) 접근 관할은 2023 년 11% → 2026 년 23% 로 증가했으며, 국내 소재 VASP 만 인허가 대상으로 삼는 관할이 50/114(44%), 일부 역외 VASP 까지 확장한 관할이 39(34%)다.
entity: doc:intl-fatf-7th-targeted-update
source_url: https://vaspnet.com/articles/from-rules-to-results-fatfs-seventh-targeted-update-on-virtual-assets-and-vasps
publisher: VASPnet
tier: T4
confidence: C
retrieved: 2026-10-21
quote: none captured (수치 전재)
note: 단일 T4 출처. R.15 등급: 완전준수 1, 대부분준수 29%→34%, 부분준수 43%, 미준수 22% (동 출처).
F-007
claim: 7차 Update 는 스테이블코인 발행자 동결 기능을 보편 안전장치로 삼지 말 것을 명시하고(「the deliberate issuance of proprietary stablecoins specifically designed to circumvent law enforcement intervention」 ¶35), 11 관할이 스테이블코인 발행자 인허가를 요구하지 않으며 그중 8 은 트래블룰 시행 관할이고, DeFi 위험평가를 마친 관할은 18%(진행 9%), DeFi 에 인허가를 부과한 관할 4, 실제 인허가 2 라고 보고한다.
entity: doc:intl-fatf-7th-targeted-update
source_url: https://notabene.id/post/fatfs-seventh-targeted-update-on-virtual-assets ; https://vaspnet.com/articles/from-rules-to-results-fatfs-seventh-targeted-update-on-virtual-assets-and-vasps
publisher: Notabene ; VASPnet
tier: T3 / T4
confidence: B
retrieved: 2026-10-21
quote: "Eleven jurisdictions report that they do not require stablecoin issuers to be licensed or registered" (Notabene 전재)
note: 비호스팅 지갑에 관한 새 통계는 없고 「strengthen monitoring of higher-risk unhosted wallet activity」 권고만 있음(Notabene).
F-008
claim: 7차 Update 의 권고 조치: 입법 완료 관할은 감독·집행을 신속히 운영화할 것, 감독기관은 FATF 2025 「Best Practices in Travel Rule Supervision」 참조, 민간은 역외 VASP 강화 CDD·소매고객으로 위장한 역외 VASP 계정 탐지·고위험 관계 제한, 상대방 VASP 식별은 「completely and accurately」 수행.
entity: doc:intl-fatf-7th-targeted-update
source_url: https://notabene.id/post/fatfs-seventh-targeted-update-on-virtual-assets ; https://vaspnet.com/articles/from-rules-to-results-fatfs-seventh-targeted-update-on-virtual-assets-and-vasps
publisher: Notabene ; VASPnet
tier: T3 / T4
confidence: B
retrieved: 2026-10-21
quote: "should rapidly operationalize supervision and enforcement" (Notabene 전재)
note: 「Best Practices in Travel Rule Supervision」(2025) 문서 자체는 FATF 403 으로 미열람 — 존재·일자 §8.
F-009
claim: INR.15 §7(b) 현행 문언은 송신 VASP 가 「required and accurate originator information and required beneficiary information」을 확보·보유하고 수신 VASP 에 「immediately and securely」 제출하도록 요구하며 금액 기준이 없다(USD/EUR 1,000 은 §7(a) CDD 임시거래 기준). 2026-10-21 fatf-gafi.org 는 403 으로 재확인 불가.
entity: reg:intl-fatf-inr15-p7b
source_url: https://www.fatf-gafi.org/content/fatf-gafi/en/publications/Fatfrecommendations/Fatf-recommendations.html (403) ; 저장소 KB PROV:intl-fatf-inr15-p7b (DOC:intl-fatf-recommendations, PDF p.80, retrieved 2026-07-30)
publisher: FATF
tier: T1
confidence: A(2026-07-30 문언) / 재확인 불가(2026-10-21)
retrieved: 2026-07-30 (KB) ; 2026-10-21 (403 관측)
quote: "Countries should ensure that originating VASPs obtain and hold required and accurate originator information and required beneficiary information on virtual asset transfers, submit the above information to the beneficiary VASP or financial institution (if any) immediately and securely"
note: 각주 49 「It is not necessary for this information to be attached directly to the virtual asset transfers.」가 오프체인 메시징 허용 근거. OJK 가 말한 각주 번호 변경(F-003) 외에 §7(b) 본문 변경 보도는 없음.
```
### 4.2 한국
```
F-010
claim: 금융위원회·FIU 는 2026-08-11 「특정금융정보법 시행령」 개정안 국무회의 의결을 발표했다. 내용: 신고 VASP 간 정보제공 의무를 「현행 100만원 이상에서 전체 거래로 확대」, 해외거래소·개인지갑 이전은 위험도별로 저위험 해외거래소 허용/그 외 해외거래소·개인지갑은 송·수신인 동일 시만 허용/고위험 금지, 1,000만원 이상 거래 자체 의심거래 관리체계 의무, 신고제·퇴직자 제재통보 부분 2026-08-20 시행, 「그 외 부분은 공포 후 6개월이 경과한 날부터 시행」.
entity: reg:kr-tfia-sd-36592
source_url: https://www.fsc.go.kr/no010101/87499
publisher: 금융위원회 보도자료
tier: T2
confidence: A
retrieved: 2026-10-21
quote: "트래블룰 기준금액(100만원) 폐지" ; "그 외 부분은 공포 후 6개월이 경과한 날부터 시행"
note: 보도자료 본문에 공포일·구체 시행일 없음. 「특정 금융거래정보 보고 및 감독규정」·신고매뉴얼 개정안 동반, 2026-08-13 설명회.
F-011
claim: 대통령령 제36592호(특금법 시행령 일부개정)는 2026-08-18 공포, 2026-08-20 시행이며 부칙 제1조 단서가 「제10조의2, 제10조의5제6항, 제10조의10, 제10조의20 및 제16조의2제1호ㆍ제4호의 개정규정은 공포 후 6개월이 경과한 날부터 시행한다」고 정한다.
entity: reg:kr-tfia-sd-36592
source_url: https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20270219&type=XML
publisher: 법제처 국가법령정보센터(DRF)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "이 영은 2026년 8월 20일부터 시행한다. 다만, 제10조의2, 제10조의5제6항, 제10조의10, 제10조의20 및 제16조의2제1호ㆍ제4호의 개정규정은 공포 후 6개월이 경과한 날부터 시행한다."
note: KB CTR:00004 가 「공포 전까지 proposed」로 둔 사안이 공포로 전환됨. 입법예고안 부칙의 「2027년 1월 1일」은 최종 공포본에서 「공포 후 6개월」로 바뀌었다.
F-012
claim: 법제처 시행일 색인(eflaw)은 특금법 시행령에 대해 MST 288765(공포 2026-08-18, 제36592호) 「시행예정」 판본의 시행일자를 **20270219** 로, 같은 공포번호의 「연혁」 판본을 20260820 으로, 현행 판본을 MST 290511(공포 2026-09-29, 대통령령 제36728호, 타법개정, 시행 2026-10-02)로 표시한다. 언론(이데일리 2026-08-10, 쟁글 2026-08-11)은 기준금액 폐지 적용일을 「2027년 2월 20일」로 보도했다.
entity: reg:kr-tfia-sd-36592 ; reg:kr-tfia-sd-36728
source_url: https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=eflaw&type=JSON&query=특정금융거래정보의보고및이용등에관한법률시행령 ; https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02420646645546008 ; https://xangle.io/insight/events/6a7a759f962c5f6693cff437
publisher: 법제처 DRF ; 이데일리 ; 쟁글
tier: T1 / T4
confidence: A(법제처) — 언론 일자와 상충(§5)
retrieved: 2026-10-21
quote: eflaw 레코드 「공포일자 20260818 / 공포번호 36592 / 시행일자 20270219 / 현행연혁코드 시행예정」 ; "다만 트래블룰 금액 기준 폐지 조항은 공포 후 6개월의 유예기간을 거쳐 내년 2월 20일부터 적용된다." (이데일리)
note: 공포 08-18 → 익일 기산 → 6개월 만료 2027-02-18 → 「경과한 날」 2027-02-19. 언론의 02-20 은 공포일을 08-19 로 가정한 계산으로 보임. 저장소는 법제처 색인값 2027-02-19 를 채택할 것.
F-013
claim: 2027-02-19 시행 판본의 시행령 제10조의10 은 ① 「정보제공은 가상자산사업자가 다른 가상자산사업자에게 가상자산을 이전하는 모든 경우에 할 것」 ② 송·수신 고객의 성명(법인은 명칭·대표자 성명)과 가상자산주소 제공 ③ FIU 원장 또는 수취 VASP 요청 시 송신 고객의 주민등록번호(법인등록번호)·여권번호·외국인등록번호 제공 ④ 제2호 정보는 이전 시 동시 제공, 제3호 정보는 요청일부터 3영업일 이내 제공을 규정한다.
entity: reg:kr-tfia-sd-36592
source_url: https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20270219&type=XML
publisher: 법제처 DRF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "정보제공은 가상자산사업자가 다른 가상자산사업자에게 가상자산을 이전하는 모든 경우에 할 것" ; "제3호에 따른 정보는 정보제공을 요청받은 날부터 3영업일 이내에 제공할 것"
note: 한국은 2027-02-19 부터 유형 A(의무에 금액) → 「의무 전건 + 요청 시 추가정보」 구조로 바뀐다. 추가정보(주민등록번호 등)는 금액이 아니라 **요청**으로 발동되므로 비교표의 B 형과도 다르다.
F-014
claim: 2026-10-21 현재 효력 있는(2026-08-20 판) 시행령 제10조의10 제1호는 「정보제공은 금융정보분석원장이 정하여 고시하는 환산 기준에 따라 가상자산사업자가 다른 가상자산사업자에게 1백만원 이상에 상당하는 가상자산을 이전하는 경우에 할 것」이다.
entity: reg:kr-tfia-sd-36592
source_url: https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20260820&type=XML
publisher: 법제처 DRF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "1백만원 이상에 상당하는 가상자산을 이전하는 경우에 할 것"
note: 같은 응답의 조문 단위 메타데이터 「조문시행일자 20260820」은 헤더의 「20270219:제10조의10」·부칙과 충돌 — 법제처 레코드 오류로 보이나 §5 에 기록. 현행 MST 290511 XML 은 이미 「모든 경우」 문언을 보여주어 혼동 유발.
F-015
claim: 시행령 제10조의20(2027-02-19 시행) 제7호는 외국 가상자산사업자와 이전거래 시 FIU 고시 방법으로 AML 조치를 평가하고 고시 기준에 맞게 거래할 것(가목), 「1천만원 이상의 범위에서 금융정보분석원장이 정하여 고시하는 금액 이상」 거래에 자체 의심거래 감시체계 구축·운영(나목)을, 제8호는 「독점적인 관리 권한을 가지지 않은 가상자산주소를 이용하는 거래 상대방」과의 이전거래에 고시 기준 준수(가목)와 제7호나목 이행(나목)을 요구한다.
entity: reg:kr-tfia-sd-36592
source_url: https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20270219&type=XML
publisher: 법제처 DRF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "가상자산사업자가 독점적인 관리 권한을 가지지 않은 가상자산주소를 이용하는 거래 상대방과 가상자산 이전거래를 하는 경우에는 다음 각 목의 사항을 이행할 것"
note: 「개인지갑」이라는 용어는 법령에 없고 「독점적인 관리 권한을 가지지 않은 가상자산주소」가 자기수탁 지갑의 법령상 표현이다. 수취 VASP 측 정보 확보 의무(제10조의5제6항)는 본 조사에서 문언 미확보.
F-016
claim: 특정 금융거래정보 보고 및 감독규정은 FIU 고시 제2026-2호(발령·시행 2026-08-20, 일부개정)에 이어 제2026-3호(발령·시행 2026-10-02, 일부개정)로 개정되어, 2026-10-21 기준 현행본은 제2026-3호다. 저장소가 2026-07-30 확인한 최신본은 제2024-1호였다.
entity: reg:kr-fiu-supervisory-rule-2026-2 ; reg:kr-fiu-supervisory-rule-2026-3
source_url: https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=admrul&type=JSON&query=특정 금융거래정보 보고 및 감독규정 ; https://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=2100000285986&type=XML
publisher: 법제처 DRF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: 「행정규칙일련번호 2100000285986 / 발령일자 20261002 / 발령번호 2026-3 / 시행일자 20261002 / 제개정구분 일부개정」 ; 부칙 "이 고시는 2026년 10월 2일부터 시행한다." (제2026-3호)
note: 제2026-3호의 개정 내용은 XML 에 개정이유가 없어 미확인(타법개정 반영 추정 — 추정이므로 §8).
F-017
claim: 감독규정 제28조의2 제1항은 외국 가상자산사업자와 거래관계 수립 전 신원확인·AML 조치 평가 및 주기적 재평가를, 제2항은 ① FATF 권고 이행국 소재·국내 유사 수준 AML 의무 이행·인허가 이행을 모두 충족하고 저위험이면 이전 허용(단 영 제10조의10제2호 정보 확보) ② 그 외는 「고객과 가상자산 이전거래의 상대방이 동일한 경우에 한해」 허용 ③ FATF 고위험국 소재 또는 인허가 의무 미이행이거나 고위험 평가 시 「거래를 제한하여야 한다」를 정한다.
entity: reg:kr-fiu-supervisory-rule-2026-2
source_url: https://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=2100000285986&type=XML
publisher: 법제처 DRF(금융정보분석원 고시)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "제1호 및 제3호에 해당하지 않는 경우에는 고객과 가상자산 이전거래의 상대방이 동일한 경우에 한해 가상자산 이전거래를 허용하여야 한다." ; "외국 가상자산사업자가 FATF가 지정하는 조치를 요하는 고위험 국가에 소재할 것"
note: 저위험 기준 나목은 「가상자산 이전 시 정보제공의무 등 자금세탁방지의무를 이행하고 있을 것」을 포함 — 상대 관할의 트래블룰 시행 여부가 허용 요건(sunrise 대응의 법령화).
F-018
claim: 감독규정 제28조의2 제3항은 영 제10조의20제7호나목의 고시 금액을 「1천만원」으로, 제4항은 영 제10조의20제8호가목(독점적 관리 권한 없는 주소)의 기준을 ① 고객 특성·거래양태상 위험이 현저히 높으면 해소 전까지 거래 제한 ② 그 외는 「고객과 가상자산 이전거래의 상대방이 동일한 경우에 한해 가상자산 이전거래를 허용할 것」(법령상 의무 이행·국가기관 권한 행사 이전은 예외)으로 정한다.
entity: reg:kr-fiu-supervisory-rule-2026-2
source_url: https://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=2100000285986&type=XML
publisher: 법제처 DRF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "영 제10조의20제7호나목에서 \"금융정보분석원장이 정하여 고시하는 금액\"이란 1천만원을 말한다." ; "제1호에 해당하지 않는 경우에는 고객과 가상자산 이전거래의 상대방이 동일한 경우에 한해 가상자산 이전거래를 허용할 것. 다만, 법령에 따른 의무의 이행 또는 국가기관의 적법한 권한 행사에 따라 가상자산을 이전하는 경우에는 그러하지 아니하다."
note: 자기수탁 지갑 「본인 지갑만 허용」 원칙이 거래소 자율규제(DAXA 외부지갑 등록제)에서 **고시 의무**로 격상된다. 소유 증명 방법은 고시가 정하지 않음.
F-019
claim: FIU 고시 제2026-2호 부칙은 「이 규정은 2026년 8월 20일부터 시행한다」고 하되 제26조·제28조의2·제31조제3호 개정규정은 공포 후 6개월이 경과한 날부터 시행하고, 시행 전 신고 사업자에 대해 별표2 제1호가목(부채비율)·별표3 은 「이 규정 시행 이후 1년이 경과한 날부터 적용」한다.
entity: reg:kr-fiu-supervisory-rule-2026-2
source_url: https://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=2100000285986&type=XML
publisher: 법제처 DRF
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "이 규정은 2026년 8월 20일부터 시행한다." ; (별표2·3) "이 규정 시행 이후 1년이 경과한 날부터 적용한다."
note: 고시 「공포 후 6개월」의 기산점이 발령일(08-20)이면 제28조의2 시행일은 2027-02-21 로 산정되어 시행령 제10조의20(2027-02-19)과 2일 어긋날 수 있음 — 법제처 행정규칙 시행일 색인으로 확정 필요(§8). 제26조(가격 산정)는 환산 기준 조문.
F-020
claim: 2026-03-30 입법예고(2026-03-30~05-11) 단계의 안은 해외 VASP·개인지갑 「1,000만원 이상 거래에 대해서는 위험도와 관계없이 의심거래로 보아 금융정보분석원에 보고」였으나, 최종 시행령은 「1천만원 이상 범위에서 FIU 고시 금액 이상 거래에 자체 의심거래 감시체계 구축·운영」으로 바뀌었다.
entity: reg:kr-tfia-sd-36592
source_url: https://www.fsc.go.kr/no010101/86589 ; https://www.etoday.co.kr/news/view/2613380
publisher: 금융위원회 보도자료(2026-03-30) ; 이투데이(2026-08-11)
tier: T2 / T4
confidence: A(변경 사실 — 두 T1/T2 문언 대조)
retrieved: 2026-10-21
quote: "1,000만원 이상 거래에 대해서는 위험도와 관계없이 의심거래로 보아 금융정보분석원에 보고하도록 한다." (입법예고) ; "자체적인 의심거래 감시체계를 구축ㆍ운영할 것" (공포본 §10-20 ⑦나)
note: 저장소 korea-verify §0 #9 「1,000만원 이상 STR 간주(위험도 판단 불요)」는 입법예고안 기준 — 공포본으로 정정 필요(§9).
F-021
claim: 특금법은 법률 제21358호(공포 2026-02-19, 시행 2026-08-20; 대주주 심사·신고 조건부 수리·퇴직자 제재통보)에 이어 법률 제21857호(공포 2026-08-04, 시행 2026-10-02, 타법개정)가 현행본이다. 2026-01-29 본회의 통과 보도자료는 제5조의3(가상자산 이전 시 정보제공) 개정을 언급하지 않는다.
entity: reg:kr-tfia
source_url: https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=law&type=JSON&query=특정금융거래정보의보고및이용등에관한법률 ; https://www.fsc.go.kr/no010101/86168 ; 저장소 _research/wave2/korea-verify.md F-101~F-104
publisher: 법제처 DRF ; 금융위원회
tier: T1 / T2
confidence: A
retrieved: 2026-10-21
quote: 「법령ID 009244 / 법령일련번호 290725 / 공포일자 20260804 / 공포번호 21857 / 시행일자 20261002 / 제개정구분명 타법개정」
note: KB REG:kr-tfia 의 citation 「법률 제19563호(현행) / 제21358호(시행 예정)」은 2026-10-21 기준 둘 다 낡음(§9).
F-022
claim: 한국 2025~2026 VASP 제재에서 트래블룰(제5조의3) 위반은 사유로 공표되지 않았다. 두나무: 2025-11-06 FIU 발표 과태료 총 352억원(약 860만건; 고객확인·거래제한·의심거래보고 의무 위반 등), 2025-02-25 영업 일부정지 3개월(미신고 VASP 거래 금지 위반). 코인원: 2026-04 영업 일부정지 3개월·과태료 52억원(미신고 해외 VASP 16개사와 10,113건 이전 등). 빗썸: 영업 일부정지 6개월·과태료(금액 미확인). 코빗: 2026-01 기관경고·과태료 약 27억3,200만원.
entity: case:kr-fiu-dunamu-2025
source_url: https://eiec.kdi.re.kr/policy/materialView.do?num=273166 ; https://www.tfmedia.co.kr/news/article.html?no=203703 ; https://www.blockmedia.co.kr/archives/1089395
publisher: 금융위원회·FIU 보도자료(KDI 경제정보센터 미러) ; 조세금융신문(2026-04-14) ; 블록미디어(2026-05-10)
tier: T2 / T4 / T4
confidence: A(두나무) / C(코인원·빗썸·코빗)
retrieved: 2026-10-21
quote: "총 352억원의 과태료 처분을 결정함" ; "약 860만건" ; "영업 일부정지 3개월과 과태료 52억원 부과를 결정했다."
note: KoFIU 제재공시 페이지는 2026-10-21 404. 두나무 과태료 확정액 35,215,600,000원(FIU 제재공시 2025-12-09)은 저장소 korea-verify F-117 과 일치. 블록미디어는 코인원 제재 효력이 소송으로 일부 정지 중이라 보도(미검증).
```
### 4.3 EU
```
F-023
claim: TFR(Regulation (EU) 2023/1113) 제14조 제1항은 송신 CASP 에 송신인 성명·DLT 주소·계정번호·주소(또는 생년월일·출생지)·LEI 동반을 요구하며 금액 기준이 없다. EBA 의견수렴 결과표는 「Recital 30 … all crypto-asset transfers are subject to the same requirements regardless of their amount and of whether they are domestic or cross-border transfers」를 근거로 CASP 에 EUR 1 000 간소화 조항이 없다고 설명한다.
entity: reg:eu-tfr-2023-1113
source_url: https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf ; 저장소 KB PROV:eu-tfr-art14 (CELLAR, retrieved 2026-07-31) ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R1113 (2026-10-21 본문 없음)
publisher: EBA ; EUR-Lex
tier: T1
confidence: A(제14조 문언은 KB 2026-07-31 확인; EBA 결과표는 2026-10-21 직접 확인)
retrieved: 2026-10-21
quote: "Recital 30 of Regulation (EU) 2023/1113 is clear that all crypto-asset transfers are subject to the same requirements regardless of their amount and of whether they are domestic or cross-border transfers."
note: 적용개시 2024-12-30 은 EBA GL 본문 「Like MiCAR, Regulation (EU) 2023/1113 will apply from 30 December 2024」로 확인. EUR-Lex 는 세 경로(ELI/HTML/PDF) 모두 빈 응답.
F-024
claim: EBA Travel Rule Guidelines(EBA/GL/2024/11)는 표지 일자 2024-07-04, 적용일 2024-12-30 이며 JC/GL/2017/16 을 대체한다.
entity: reg:eu-eba-gl-2024-11
source_url: https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf ; https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/anti-money-laundering-and-countering-financing-terrorism/guidelines-preventing-abuse-funds-and-certain-crypto-assets-transfers-money-laundering-and-terrorist
publisher: EBA
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "EBA/GL/2024/11 04/07/2024" ; "10. These Guidelines apply from 30 December 2024."
note: EBA 페이지의 compliance-table 날짜 2024-11-27 은 당국 준수통보 기한이며 적용일과 다름. 준수표 엑셀 최종 갱신 2026-03-17.
F-025
claim: EBA GL ¶21~¶23 은 정보 전송 인프라가 「without gaps or errors」 전송·수신 가능해야 하고 불가하면 시스템을 바꾸라고 하며, ¶24 는 CASP·ICASP 에 한해 2025-07-31 까지 기술적 한계를 추가 절차로 보완하는 예외를 허용했다.
entity: reg:eu-eba-gl-2024-11
source_url: https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf
publisher: EBA
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "24. CASPs and ICASPs may, by way of derogation from paragraph 21 and until 31 July 2025, exceptionally use infrastructures or services where technical limitations in relation to the completeness of data need to be compensated by additional technical steps or fixes to fully comply with these Guidelines."
note: 데이터 품질 요구의 1차 근거. 유예 종료 후(2025-08-01~) 필드 누락을 기술적 한계로 정당화할 수 없다.
F-026
claim: EBA GL §4.8.4 ¶81~¶83: EUR 1 000 도달 여부는 송신 CASP 는 주문·개시 시점, 수신 CASP 는 수취 시점에 이전 시점 환율로 수수료 제외 판정하고, 자기수탁 주소 소유·통제 평가에는 ⒜ 비대면 원격온보딩 무인검증(주소 표시) ⒝ 유인검증 ⒞ CASP 가 정한 소액(가급적 최소단위)을 해당 주소와 CASP 계정 간 송금 ⒟ 해당 키로 특정 메시지 전자서명 ⒠ 기타 적합한 기술적 수단 중 **최소 1종**을 사용한다.
entity: reg:eu-eba-gl-2024-11
source_url: https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf
publisher: EBA
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "83. In order to assess whether the self-hosted address is owned or controlled by the originator or beneficiary, respectively, CASPs should use at least one of the following verification methods: … c) sending of a predefined amount (preferably the smallest denomination of a given crypto-asset), set by the CASP, from and to the self-hosted address to the CASP's account; d) requesting the customer to digitally sign a specific message into the account and wallet software with the key corresponding to that address;"
note: ⒞=Satoshi test, ⒟=메시지 서명. AOPP 는 명시되지 않으나 ⒟/⒠에 포섭. 협의안의 「2종 이상」 요구는 최종안에서 삭제(EBA 결과표 §4.8.4).
F-027
claim: EBA GL ¶77~¶78 은 상대 주소가 자기수탁인지 판단에 블록체인 분석·제3자 데이터·메시징 식별자를 쓰고 불가하면 고객에게 직접 확인하되 상대가 CASP 로 판명되면 상대 CASP 를 정확히 식별할 것을, ¶85 는 단일 방법이 불충분하면 조합을, ¶86 은 확인 완료 주소의 화이트리스트(위험 변화 시 제거)를, ¶89 는 제3자 소유로 판명 시 블록체인 분석·공개 데이터로 신원 검증을 갈음할 수 있음을 규정한다.
entity: reg:eu-eba-gl-2024-11
source_url: https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf
publisher: EBA
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "86. Where the CASP is fully satisfied that the self-hosted address is owned or controlled by its customer, the CASP should document this in its systems and may not need to re-apply the measures above to subsequent transactions from/to the same address ('whitelisting')."
note: 저장소 산문의 「Satoshi test」 언급을 EU 규범 근거로 보강 가능.
F-028
claim: EBA GL 위험요소 목록(§4.5)은 (d) 당사자 PSP/CASP 가 「publicly available information」상 트래블룰 미이행 국가에 소재, (e) PSP/CASP 활동을 인허가·규제하지 않는 제3국 소재 기관과의 이전, (f) 자기수탁 주소와의 이전, (i) 정당한 이유 없이 반복적으로 정보를 누락하는 기관을 고위험 요소로 들고, §4.7 은 「repeatedly failing」 판정 기준(정성·정량)과 식별 후 3개월 내 당국 보고를 요구한다.
entity: reg:eu-eba-gl-2024-11
source_url: https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf
publisher: EBA
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "d) transfers where the payer's PSP, originator's CASP, IPSP, ICASP, payee's PSP or beneficiary's CASP are located in a country that, based on publicly available information, has not yet implemented the obligation to obtain, hold and transmit information on the originator and beneficiary when conducting wire and virtual asset transfers;"
note: EU 의 sunrise 대응은 「거래 금지」가 아니라 「고위험 요소 + 반복 누락 기관 보고」 구조. 의견수렴에서 업계가 「sunrise period and interoperability limitations」로 완화를 요청했으나 EBA 는 「No change」.
F-029
claim: EBA 는 GDPR 지침 요청에 대해 TFR Recital 19(「the processing of personal data under this Regulation should take place in full compliance with Regulation (EU) 2016/679」, 제3국 이전은 GDPR 제5장)와 제25조 제4항의 별도 위임을 들어 가이드라인에 추가하지 않았고, guideline 14 에서 정보 전송은 블록체인 거래 개시 이전·동시에 「immediately … and securely」 이뤄져야 하며 자기수탁 지갑에도 동일 시점이 적용된다고 밝혔다.
entity: reg:eu-eba-gl-2024-11
source_url: https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf
publisher: EBA
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "'the processing of personal data under this Regulation should take place in full compliance with Regulation (EU) 2016/679 (...)' and, equally, that 'the transfer of personal data to a third country is required to be carried out in accordance with Chapter V of Regulation (EU) 2016/679'"
note: EDPB 의 TFR 관련 의견서는 본 조사에서 미확인(§8).
```
### 4.4 영국
```
F-030
claim: MLR 2017 Part 7A(regs 64A~64H)는 S.I. 2022/860 으로 신설되어 2023-09-01 시행됐고, 2023-09-01 시점 reg 64C(4)의 심화정보 발동 문언은 「equal to or exceeds the equivalent in cryptoassets of 1,000 euros」였다. reg 64C(1)의 기본 의무에는 금액이 없다.
entity: reg:gb-mlr2017-part7a
source_url: https://www.legislation.gov.uk/uksi/2017/692/regulation/64C/2023-09-01 ; https://www.legislation.gov.uk/uksi/2017/692/regulation/64C
publisher: legislation.gov.uk (The National Archives)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Where paragraph (3) does not apply and the transfer is equal to or exceeds the equivalent in cryptoassets of 1,000 euros in value (taken together with any other cryptoasset transfer which appears to be linked), the cryptoasset business of the originator must ensure that the inter-cryptoasset business transfer is also accompanied by the information specified in paragraph (6)." (2023-09-01 판)
note: 주석 F1 「Pt. 7A inserted (1.9.2023) by S.I. 2022/860」. KB PROV:gb-mlr2017-reg64c 의 valid_from 공란을 2023-09-01 로 채울 수 있다.
F-031
claim: The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 (S.I. 2026/621; 2026-06-09 제정, 2026-06-30 시행)의 regulation 32 는 reg 64C(4)의 「1,000 euros」를 「£800」으로, regulation 33 은 reg 64G(1)(b)의 같은 금액을 「£800」으로 치환했다. 같은 개정령은 reg 15(3)(b)를 £1,000, reg 27(1)(b)·(7E)를 £800 으로 바꿨다.
entity: reg:gb-si-2026-621
source_url: https://www.legislation.gov.uk/uksi/2026/621/made
publisher: legislation.gov.uk
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "In regulation 64C(4), for \"1,000 euros\" substitute \"£800\"." ; "In regulation 64G(1)(b), for \"1,000 euros\" substitute \"£800\"."
note: 저장소 산문·KB 의 「£800」은 2026-08-04 조회 시점의 현행 문언이라 맞지만, 2026-06-30 이전 사안(예: 2024~2025 거래)에는 €1,000 이 적용된다. 시점 질의를 위해 KB 에 valid_from/valid_to 분리 필요(§9).
F-032
claim: 현행 reg 64C 는 (5) 송·수신인 성명(법인은 등록명/상호)·계좌번호 또는 고유거래식별자, (6) 법인: 고객식별번호 또는 등록사무소·주영업소 주소 / 개인: 고객식별번호·주소·출생증명서/여권/신분증 번호·생년월일+출생지 중 하나, (8) 송신인 정보는 독립 신뢰 출처로 검증, (9) 완전 준수 전 이전 금지를 규정하고, (7) 은 수익자 사업자가 영국 외에서만 영업하는 배치 이전 특례다.
entity: reg:gb-mlr2017-part7a
source_url: https://www.legislation.gov.uk/uksi/2017/692/regulation/64C
publisher: legislation.gov.uk (changes to 2026-10-20 반영)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: (9) 요지 — originator's business must not make the transfer until it has fully complied with this regulation (125자 제한으로 축약 인용)
note: (3)·(4)의 발동 조건은 「every cryptoasset business in the transfer chain … carries on business in the UK」면 (3) 적용(요청 시 3영업일 내 제공), 아니면 (4)(£800 이상 시 동반) — KB 가 미확정으로 남긴 조건을 이번에 확인.
F-033
claim: reg 64G(비호스팅 지갑 이전)는 암호자산 사업자가 고객(송신인 또는 수익자)에게 누락 정보를 요청할 수 있고, 고객이 수익자이며 연결 이전 합산 £800 이상이면 송신인 심화정보도 요청할 수 있으며, 요청 여부는 위험평가(관계·이전의 목적·성격, 금액·빈도, 관계 지속기간)에 따르고, 요청 정보를 받지 못하면 「must not make the cryptoasset available to the beneficiary」다.
entity: reg:gb-mlr2017-part7a
source_url: https://www.legislation.gov.uk/uksi/2017/692/regulation/64G
publisher: legislation.gov.uk (2026-06-30 판)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "may request from its customer (whether the originator or the beneficiary)" ; "it must not make the cryptoasset available to the beneficiary"
note: 영국은 자기수탁 지갑에 소유 증명 의무를 두지 않고 「요청 재량 + 미수령 시 지급 금지」 구조. 소유 검증 방법은 JMLSG 가이던스 영역(미확인).
F-034
claim: S.I. 2026/621 regulation 20 은 MLR 2017 에 reg 34A(암호자산 교환·수탁지갑 사업자가 제3국 유사 사업자와 「correspondent relationship」을 맺을 때 강화 CDD: 사업 성격 정보 수집·고위경영진 승인 등; 셸 사업자 금지)를 신설하며, reg 1(4)에 따라 2027-02-01 시행된다.
entity: reg:gb-si-2026-621
source_url: https://www.legislation.gov.uk/uksi/2026/621/regulation/20/made ; https://www.legislation.gov.uk/uksi/2026/621/made
publisher: legislation.gov.uk
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "\"correspondent relationship\" means the relationship between and among cryptoasset exchange providers, … including relationships established for transactions in, or transfers of, cryptoassets;"
note: 상태 enacted-not-in-force. 비호스팅 지갑·고위험 제3국 문언은 없음. 상대 VASP 실사(FATF 「counterparty VASP due diligence」)의 영국판으로 트래블룰 운영과 직결.
F-035
claim: FCA 는 2023-08-17 성명에서 2023-09-01 트래블룰 시행을 안내하며, 트래블룰 미시행 관할로 송금 시 상대가 정보를 수신할 수 있는지 합리적 조치로 확인하고 불가하면 정보를 수집·검증·보관한 뒤 이전할 수 있으며, 그런 관할에서 수신한 정보 누락 이전은 위험기반으로 지급 여부를 결정하라고 했다. FCA 2026 과징금 목록(17건, 2026-09-30 까지)에는 암호자산·Part 7A 위반 건이 없다.
entity: reg:gb-mlr2017-part7a
source_url: https://www.fca.org.uk/news/statements/fca-sets-out-expectations-uk-cryptoasset-businesses-complying-travel-rule ; https://www.fca.org.uk/news/news-stories/2026-fines
publisher: FCA
tier: T2 / T1
confidence: A
retrieved: 2026-10-21
quote: "From 1 September 2023, cryptoasset businesses in the UK will be required to collect, verify and share information"
note: FCA 2024·2025 과징금 목록은 미점검(§8).
```
### 4.5 미국
```
F-036
claim: 31 CFR 1010.410(f)는 미국 내 송신·중개 금융기관에 「transmittal of funds in the amount of $3,000 or more」의 이체지시에 송신인 성명·계좌번호·주소·금액·실행일·수취 금융기관 정보를 포함하도록 요구한다(법적 근거 75 FR 65812, 2010-10-26; 81 FR 76864, 2016-11-04).
entity: reg:us-bsa-1010-410f
source_url: https://www.law.cornell.edu/cfr/text/31/1010.410
publisher: Cornell LII (eCFR 미러; ecfr.gov 는 2026-10-21 unblock 리다이렉트)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "shall include in any transmittal order for a transmittal of funds in the amount of $3,000 or more, information as required in this paragraph (f)"
note: 가상자산 적용은 MSB 정의 경유(KB curator_note 동일). 재무부 2026-03 보고서(F-040)가 DASP 적용을 명시.
F-037
claim: FinCEN·FRB 의 국경 간 임계 $3,000→$250 하향 및 CVC 명확화 NPRM(RIN 1506-AB41; 85 FR 68005, 2020-10-27)은 Spring 2025 Unified Agenda 에 「Completed Actions — Withdrawn 04/16/2025」로 기재됐다. Federal Register 에는 별도 철회 고시 문서가 없다(FinCEN 1010.410 관련 34건 중 2024~2026 문서에 철회 없음).
entity: reg:us-rin-1506-ab41
source_url: https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202504&RIN=1506-AB41 ; https://www.federalregister.gov/api/v1/documents.json?conditions[term]=%221010.410%22&conditions[agencies][]=financial-crimes-enforcement-network&order=newest&per_page=20
publisher: OIRA reginfo.gov ; Federal Register API
tier: T1
confidence: A
retrieved: 2026-10-21
quote: 「Timetable: NPRM 10/27/2020 (85 FR 68005) / NPRM Comment Period End 11/27/2020 / Withdrawn 04/16/2025」
note: 저장소 KB curator_note 「2025-04 철회(FACT 기록 있음)」와 일치, 일자 04-16 로 확정. 같은 시기 2020-12-23 비호스팅 지갑 NPRM(2020-28437)의 상태는 미확인(§8).
F-038
claim: 1010.410 에 걸린 미시행 개정 「89 FR 72274 (2024-09-04)」는 투자자문업자 AML/CFT 규칙(FR 2024-19260)이 1010.410(e)(6) 제외목록에 투자자문업자를 추가한 것이며, 91 FR 36(2026-01-02)으로 시행이 2028-01-01 로 연기됐다. 가상자산 트래블룰 요건과 무관하다.
entity: reg:us-bsa-1010-410f
source_url: https://www.law.cornell.edu/cfr/text/31/1010.410 ; https://www.federalregister.gov/documents/2024/09/04/2024-19260/financial-crimes-enforcement-network-anti-money-launderingcountering-the-financing-of-terrorism
publisher: Cornell LII ; Federal Register
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "This amendment was delayed until Jan. 1, 2028, at 91 FR 36, Jan. 2, 2026." (LII) ; FR API 요약: "Amends 1010.410(e)(6) to add investment advisers to the exclusion list."
note: KB PROV:us-bsa-cfr1010-410f curator_note 「개정 내용은 … 연방관보 원문을 따로 확보해야 한다」 → 본 사실로 해소(§9).
F-039
claim: FinCEN·OFAC 는 GENIUS 법(2025-07-18 서명) 이행을 위해 허가 결제스테이블코인 발행자(PPSI)를 BSA 금융기관으로 편입하는 AML/CFT·제재 프로그램 NPRM 을 2026-04-10 (FR 2026-06963), 고객확인프로그램 NPRM 을 2026-06-22 (FR 2026-12460) 공고했다. DLA Piper 분석은 PPSI 가 비은행 기록보존규칙(≥$3,000)과 Travel Rule 을 준수해야 하되 NPRM 이 유통시장 거래 적용 여부를 다루지 않는다고 본다.
entity: reg:us-genius-ppsi-nprm
source_url: https://www.federalregister.gov/api/v1/documents.json?conditions[term]=%221010.410%22&conditions[agencies][]=financial-crimes-enforcement-network&order=newest&per_page=20 ; https://www.dlapiper.com/en/insights/publications/2026/04/treasury-proposes-aml-cft-and-sanctions-compliance-rules-for-stablecoin-issuers-under-the-genius-act
publisher: Federal Register API ; DLA Piper(2026-04-22)
tier: T1 / T3
confidence: A(공고 사실) / B(트래블룰 적용 서술)
retrieved: 2026-10-21
quote: "The PPSI NPRM does not address whether these rules apply to secondary market transactions." (DLA Piper)
note: 2026-10-21 기준 최종규칙 미확인. FR 문서 본문은 unblock 리다이렉트로 직접 열람 불가.
F-040
claim: 미 재무부 「Report to Congress … on Innovative Technologies to Counter Illicit Finance Involving Digital Assets」(2026-03, GENIUS 법 이행)는 각주 63 에서 송금업자인 DASP 는 「Funds Transfer Rule」/「Travel Rule」을 준수해야 하며 $3,000 이상 자금 이체가 요건을 발동할 수 있다고 적는다.
entity: reg:us-bsa-1010-410f
source_url: https://home.treasury.gov/system/files/246/GENIUS-Act-Illicit-Finance-Innovation-Congressional-Report-March-2026.pdf
publisher: U.S. Department of the Treasury
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "To the extent that any money transmitter's transactions constitute a \"transmittal of funds\" under FinCEN's regulations, then the money transmitter must comply with the \"Funds Transfer Rule\" or \"Travel Rule.\" Under the rule, a transmittal of funds of $3,000 or more may trigger certain requirements on a DASP such as an exchange"
note: PDF 34쪽, 로컬 텍스트 추출로 확인. Notabene 블로그(2026-05-18)의 인용과 일치.
F-041
claim: FinCEN 은 2025-12-09 Paxful, Inc.·Paxful USA, Inc. 에 $3,500,000 민사벌금(Consent Order 2025-02)을 부과했다. 사유는 MSB 미등록·AML 프로그램 미비·SAR 미제출이며 보도자료에 트래블룰(1010.410(f)) 위반은 없다. DOJ 합의의 「Travel Act」(18 U.S.C. §1952)는 트래블룰과 다른 법이다.
entity: case:us-fincen-paxful-2025
source_url: https://www.fincen.gov/news/news-releases/fincen-assesses-35-million-penalty-against-paxful-facilitating-suspicious
publisher: FinCEN
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Paxful admits that it willfully violated the BSA, including failing to:"
note: 2024~2026 FinCEN·OCC·NYDFS 가상자산 집행에서 트래블룰 명시 사례는 발견되지 않음(FinCEN 집행 색인 전수 미점검 — §8).
```
### 4.6 일본
```
F-042
claim: 犯罪による収益の移転防止に関する法律 第十条の五(暗号資産の移転に係る通知義務)는 「暗号資産交換業者は、顧客から依頼を受けて暗号資産の移転を行う場合において、当該移転を受取顧客に対して行うとき」 송·수취 고객 식별정보를 상대 교환업자에 통지하도록 하고(제1항), 수탁·재위탁 이전 시 통지 전달(제2항)을 정하며 금액 조건이 없다.
entity: reg:jp-aptcp-art10-5
source_url: https://laws.e-gov.go.jp/api/1/articles;lawId=419AC0000000022;article=10%E3%81%AE5
publisher: e-Gov 法令検索 API (デジタル庁)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "暗号資産交換業者は、顧客から依頼を受けて暗号資産の移転を行う場合において、当該移転を受取顧客に対して行うとき"
note: KB PROV:jp-aptcp-art10-5·CTR:00006 과 일치. 10만엔은 施行令 제7조(特定取引=CDD) 수치.
F-043
claim: 금융청 「令和4年資金決済法等改正に係る政令・内閣府令案等に関するパブリックコメントの結果等について」(2023-05-26, 2023-09-15 갱신)는 관련 政令이 「令和５年６月１日（木曜）から施行」되고 内閣府令등·告示도 같은 날 시행·적용되며, 별지에 「犯罪による収益の移転防止に関する法律施行規則の一部を改正する命令」(FATF勧告対応法 관련)이 포함된다고 밝힌다.
entity: reg:jp-aptcp-art10-5
source_url: https://www.fsa.go.jp/news/r4/sonota/20230526/20230526.html
publisher: 金融庁
tier: T2
confidence: A(政令·府令 시행일) / B(제10조의5 자체 시행일 — 개정법 부칙 미열람)
retrieved: 2026-10-21
quote: "令和５年６月１日（木曜）から施行されます" ; "FATF勧告対応法に係る犯罪収益移転防止法関連の政令・施行規則等の改正も含まれております"
note: KB REG:jp-aptcp curator_note 가 「FSA 2023-05-26 의견공모 결과에 근거한 2차 정보」라 한 바로 그 문서를 직접 확인. 트래블룰 자체의 임계·비호스팅 지갑 언급은 이 페이지에 없음.
F-044
claim: 범수법 施行規則 제31조의7 은 통지 항목(의뢰고객 성명·주소 또는 식별번호·고객번호, 이전 식별부호; 수취고객 성명·식별부호)만 정하고 금액 기준이 없으며, 「十万円を超える」는 施行令 제7조 제1항 제1호의 特定取引(CDD) 정의다. FSA 2025-06-25 문서가 통지 대상 외 지갑(対象外ウォレット) 정보 보존을 요구한다는 보도는 미확인이다.
entity: reg:jp-aptcp-art10-5
source_url: 저장소 KB PROV:jp-aptcp-mo-art31-7 (e-Gov, retrieved 2026-08-04) ; https://www.fsa.go.jp/news/r6/sonota/20250625/01.pdf (2026-10-21 바이너리 — 미열람)
publisher: e-Gov ; 金融庁
tier: T1 / 미확인
confidence: A(KB) / D(2025-06-25 문서)
retrieved: 2026-08-04 (KB) ; 2026-10-21 (시도)
quote: (KB) 「この条文にも金額基準がない」 요지 — 원문 축조 문언은 KB 도 미확보
note: 일본의 비호스팅 지갑 취급은 1차 문언 미확보 상태로 유지(§8).
```
### 4.7 싱가포르
```
F-045
claim: MAS Notice PSN02(2024-04-02 발행, 「This Notice shall take effect from 4 April 2024」)는 2025-06-30 최종개정되어 개정분이 2025-07-01 효력을 가진다.
entity: reg:sg-psn02
source_url: https://www.mas.gov.sg/-/media/amld-amendments---30-june-2025/mas-notice-psn02-amendment--new.pdf
publisher: MAS
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "1.2 This Notice shall take effect from 4 April 2024." ; "3. The amendments reflected in this document shall take effect on 1 July 2025." ; "Last revised on 30 June 2025"
note: 변경추적판(reference only)이며 Published Version 이 우선한다는 고지 포함. 2026 년 추가 개정은 발견되지 않음.
F-046
claim: PSN02 ¶13.4 는 S$1,500 이하 가치이전에 송·수신인 성명·계좌번호(또는 고유거래참조번호) 4항목을, ¶13.6 은 S$1,500 초과 시 송신인 신원확인·검증 의무와 함께 주소·고유식별번호·생년월일 중 하나를 추가로 요구한다. 의무 자체에는 금액 조건이 없다.
entity: reg:sg-psn02
source_url: https://www.mas.gov.sg/-/media/amld-amendments---30-june-2025/mas-notice-psn02-amendment--new.pdf
publisher: MAS
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "13.4 Subject to paragraph 13.5, in a value transfer where the amount to be transferred or arranged to be transferred is below or equal to S$1,500, every payment service provider which is an ordering institution shall include in the message or payment instruction that accompanies or relates to the value transfer the following:" ; "13.6 … exceeds S$1,500, every payment service provider which is an ordering institution shall identify the value transfer originator and verify the value transfer originator's identity"
note: KB PROV:sg-psn02-para13 와 완전 일치(2025-06-30 판 기준). ¶13.5·¶13.8 은 싱가포르 내 중개기관 앞 완화.
F-047
claim: PSN02 ¶13.9 는 수집 정보의 「immediately and securely」 제출을, ¶13.11 은 ¶13.3~13.10 미준수 시 「shall not execute or arrange for the value transfer」를, ¶13.12·¶13.14 는 수익기관의 누락정보 탐지(실시간 또는 사후 모니터링)와 집행·거절·보류 정책을 요구한다. ¶13 에 비호스팅 지갑 전용 조항은 없다. MAS 집행조치 색인(2026-05-25~2026-10-14 구간)에 PSN02 ¶13 관련 건은 없다.
entity: reg:sg-psn02
source_url: https://www.mas.gov.sg/-/media/amld-amendments---30-june-2025/mas-notice-psn02-amendment--new.pdf ; https://www.mas.gov.sg/regulation/enforcement/enforcement-actions
publisher: MAS
tier: T1
confidence: A(조문) / B(집행 — 색인 1쪽만 점검)
retrieved: 2026-10-21
quote: "13.11 Where the ordering institution is unable to comply with the requirements in paragraphs 13.3 to 13.10, it shall not execute or arrange for the value transfer."
note: KB 가 미확인으로 남긴 ¶13.8 은 S$1,500 초과 이전의 싱가포르 내 중개기관 앞 완화(고유거래참조번호+수익자 정보만, 3영업일 내 제공 조건) — 확인 완료.
```
### 4.8 홍콩
```
F-048
claim: 홍콩 AMLO 개정·VATP 체제와 SFC AML 지침 개정 요건은 2023-06-01 시행됐고, SFC 는 가상자산 이전 정보의 「as soon as practicable after the virtual asset transfer」 제출을 2024-01-01 까지 과도조치로 수용했다. 기존 SFO 인가 VATP 는 12개월 과도기간을 가졌다.
entity: reg:hk-amlo-sch2-s13a
source_url: https://www.clydeco.com/en/insights/2023/06/hong-kong-virtual-assets-regulatory-update ; https://21analytics.co/travel-rule-regulations/hong-kong-travel-rule-regulation
publisher: Clyde & Co(2023-06-07) ; 21 Analytics
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "have become effective on 1 June 2023" ; "as soon as practicable after the virtual asset transfer to be acceptable as an interim measure until 1 January 2024" (Clyde & Co) ; "The Travel Rule went live on 1 June 2023." (21 Analytics)
note: 과제 지시문의 「2024-06-01」은 어느 출처에서도 트래블룰 일자로 나오지 않는다. 2023-06-01 개시 12개월 과도기간의 종료(2024-05-31/06-01)와 혼동된 것으로 보인다 — §5·§9. eLegislation 조문 원문은 미확보(KB 와 동일).
F-049
claim: AMLO Sch.2 s.13A 는 금액 무관 전건 의무이며, HK$8,000 「not less than」이면 송신인 주소·고객식별번호·신분증번호 또는 생년월일·출생지가 추가되고 미만이면 성명·계좌번호 4항목이다. 21 Analytics 는 자기수탁 지갑 이전에도 정보 수집·위험평가가 필요하다고 요약한다.
entity: reg:hk-amlo-sch2-s13a
source_url: 저장소 KB PROV:hk-amlo-sch2-s13a (SFC AML Guideline ¶12.11, retrieved 2026-08-04) ; https://21analytics.co/travel-rule-regulations/hong-kong-travel-rule-regulation
publisher: SFC ; 21 Analytics
tier: T1 / T3
confidence: A(구조) / B(자기수탁)
retrieved: 2026-08-04 (KB) ; 2026-10-21
quote: "Irrespective of the transaction value, Travel Rule information is required." ; "less information is required for transactions under HKD 8000" (21 Analytics)
note: SFC 집행 뉴스 게이트웨이는 2026-10-21 빈 응답 — s.13A 인용 제재 건 미확인.
```
### 4.9 호주
```
F-050
claim: AML/CTF Act s 66A(3)(2024년 법률 제110호 신설)는 주문기관이 「the information specified in the AML/CTF Rules for the purposes of subsection 64(3)」을 수익기관에 전달하도록 하며 금액 조건이 없고, s 66A(2)(d)는 상대 지갑이 「a self-hosted wallet controlled by the payee」인지 실사로 판정하게 한다. AML/CTF Rules 2025 는 2025-08-31 의회 제출, 기존 보고기업에 2026-03-31 시행되며 Part 8 이 가치이전(payer·payee 정보 동반, 3영업일 내 정보요청 응답)을 정한다.
entity: reg:au-amlctf-s66a + Rules 2025
source_url: 저장소 KB PROV:au-amlctf-s66a (legislation.gov.au, retrieved 2026-08-04) ; https://www.nortonrosefulbright.com/en-sg/knowledge/publications/4bdd08b3/australia-amlctf-reforms-a-new-era-in-financial-crime-prevention ; https://vinciworks.com/blog/australias-tranche-2-aml-ctf-reforms-whats-changed-whos-in-scope-and-what-to-do-now/
publisher: Federal Register of Legislation(KB) ; Norton Rose Fulbright(2025-12) ; VinciWorks(2025-09-08)
tier: T1 / T3 / T4
confidence: A(법률) / B(Rules 시행일) / C(Rules 내용)
retrieved: 2026-10-21
quote: (NRF) Part 8 of the Rules "introduces detailed requirements for value transfers" ; "information about both the payer and payee must accompany transfers" ; (VinciWorks) "The Rules commence on 31 March 2026."
note: AUSTRAC 페이지 2곳(new-amlctf-rules, travel-rule-reform)은 2026-10-21 3회 타임아웃. Rules 2025 의 금액별 항목 구분·자기수탁 검증 요건은 **미확인**(KB 가 남긴 과제 그대로). Notabene AU 페이지는 3월·7월 시행일을 혼재 표기.
```
### 4.10 보조 관할
```
F-051
claim: VARA(두바이) Compliance and Risk Management Rulebook Part III.G 「FATF Travel Rule」 ¶2 는 「Prior to initiating any transfer of Virtual Assets with an equivalent value exceeding AED 3,500」 송·수신인 정보 확보·보유·당국 제공을, ¶3 은 수익 VASP 의 대칭 의무를, ¶4·5 는 최소 항목(송신인 성명·계좌/지갑주소·주거/사업장 주소; 수익자 성명·계좌/지갑주소)을, ¶7 은 「non-obliged entities (i.e. unhosted VA Wallets)」 위험 고려를, ¶9 는 임계 회피 구조화 모니터링을 정한다.
entity: reg:ae-vara-rulebook-iii-g
source_url: https://rulebooks.vara.ae/node/146
publisher: VARA
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Prior to initiating any transfer of Virtual Assets with an equivalent value exceeding AED 3,500,"
note: 유형 A(초과). 21 Analytics FAQ(2024-07-03)의 「equal to or exceeding AED 3500」은 룰북 문언과 상충 — T1 우선(§5). 연방(CBUAE)·ADGM FSRA 규정은 미확인(§8).
F-052
claim: 스위스 Art. 10 GwV-FINMA(2023-01-01 통합본)는 지급지시에 송신인 성명·계좌번호·주소(또는 생년월일·출생지/고객번호/국가식별번호)와 수익자 성명·계좌번호 전달을 요구하며 금액 기준이 없고, FINMA Aufsichtsmitteilung 02/2019(2019-08-26)는 이를 블록체인 지급에 기술중립적으로 적용하되 외부지갑 이전은 자기 고객 소유를 「suitable technical means」로 증명한 경우(제3자 지갑은 신원확인·실소유자 확인·소유 증명)에만 허용하고 「Unlike the FATF standards, Article 10 AMLO-FINMA does not provide for any exception for payments involving unregulated wallet providers」라 밝힌다. Art. 51a 의 CHF 1,000 「erreichen oder übersteigen」은 CDD 기준이다.
entity: reg:ch-gwv-finma-art10
source_url: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2015/390/20230101/de/html/fedlex-data-admin-ch-eli-cc-2015-390-20230101-de-html-4.html ; https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/4dokumentation/finma-aufsichtsmitteilungen/20190826-finma-aufsichtsmitteilung-02-2019.pdf
publisher: Fedlex ; FINMA
tier: T1 / T2
confidence: A
retrieved: 2026-10-21
quote: "such transactions are only permitted from and to external wallets if these belong to one of the institution's own customers. Their ownership of the external wallet must be proven using suitable technical means."
note: 2023-01-01 이후 통합본 존재 여부·FINMA 02/2019 대체 여부는 미확인.
F-053
claim: 캐나다 PCMLTFR s. 124.1(1)은 가상통화 이전 기록의무가 있는 금융기관·MSB·외국 MSB 에 요청인·수익자의 성명·주소·계좌/참조번호 동반(a)과 수신 시 확보 합리적 조치(b)를, (2)는 누락 시 보류·거절 서면정책을 요구하며(통합본 2026-09-30 현재 2025~2026 개정 없음), FINTRAC 지침은 2021-06-01 발효다. FINTRAC 은 2025-10-22 Xeltox Enterprises Ltd.(Cryptomus)에 C$176,960,190 AMP 를 공표했고, 위반 3(PCMLTFR 156(1)(b) 서면정책 미비)의 결함 영역 목록에 「Travel rule」이 포함된다 — 독립 트래블룰 위반·별도 벌금은 아니다.
entity: reg:ca-pcmltfr-s124-1 ; case:ca-fintrac-xeltox-2025
source_url: https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/section-124.1.html ; https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/travel-acheminement/1-eng ; https://fintrac-canafe.canada.ca/pen/amps/pen-2025-10-22-eng
publisher: Justice Laws Canada ; FINTRAC
tier: T1 / T2 / T1
confidence: A
retrieved: 2026-10-21
quote: "the name, address and, if any, the account number or other reference number" ; "FEs, MSBs and FMSBs must include the travel rule information when they send VC transfers."
note: s. 124.1 발동 기록의무의 금액(CAD 1,000 설)은 T3 단일출처로 미확인(§8). 2024~2026 조사 범위에서 트래블룰이 제재문서에 명시된 유일 사례.
F-054
claim: 인도는 2023-03-07 S.O. 1072(E)로 VDA 서비스업을 PMLA 보고기관에 편입하고 FIU-IND AML/CFT 가이드라인을 2023-03-10 발효시켰으며, 가이드라인은 VDA 이전을 전신송금에 준해 「required and accurate originator information and required beneficiary information」 확보·즉시 전송을 요구하고 금액 기준을 두지 않으며, 비호스팅 지갑 이전을 고위험으로 분류한다. 2026-01-08 갱신판이 보도된다.
entity: reg:in-fiu-vda-guidelines
source_url: https://cryptoslate.com/crypto-laws/india-fiu-ind-aml-cft-guidelines-vda-service-providers/
publisher: CryptoSlate(법령 프로필, 「Last verified Jun 5, 2026」)
tier: T3
confidence: B(일자) / C(갱신판)
retrieved: 2026-10-21
quote: "either the originator or beneficiary wallet is not hosted"
note: FIU-IND 1차 PDF 는 홈페이지에서 링크를 찾지 못함(§8).
F-055
claim: 브라질 Resolução BCB nº 520(2025-11-10)은 Art. 44 §único 로 PSAV 에 송신인(성명·계좌·주소·CPF/CNPJ·지갑)·수익자(성명·계좌·지갑) 정보 전달을 금액 조건 없이 요구하고, Art. 92 로 2026-02-02 발효, Art. 89 로 국내 1단계(발효 후 365일)·국경 간 2단계(추가 365일)를 두며 「a partir de 2 de fevereiro de 2028」 전면 의무화하고, Art. 91 로 2026-10-30 부터 무허가 상대방과의 가상자산 거래를 금지한다. Art. 59 §2 는 자기수탁 선택 고객에 위험 고지 의무다.
entity: reg:br-res-bcb-520
source_url: https://www.migalhas.com.br/arquivos/2025/11/23462FAD2E8205_Resolucao520.pdf (BCB 원문 미러)
publisher: Banco Central do Brasil(미러: Migalhas)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "Art. 92. Esta Resolução entra em vigor em 2 de fevereiro de 2026." ; "§ 3º O cumprimento das regras estabelecidas no art. 44 é obrigatório para todas as sociedades prestadoras de serviços de ativos virtuais autorizadas a funcionar no país a partir de 2 de fevereiro de 2028."
note: 기준일 9일 후(2026-10-30) Art. 91 발효 — 감시 항목. Res. BCB 521 의 자기수탁 외환 규율은 T3(Chambers) 미검증.
F-056
claim: 대만 「提供虛擬資產服務之事業或人員防制洗錢及打擊資恐辦法」(2024-11-26 개정, 2024-11-30 시행) 第7條(트래블룰)는 第18條에 따라 금관회가 별도 지정하는 날 시행되며, 전건 의무에 NT$30,000 초과 시 심화정보(T3)이고 자기수탁 지갑 요건은 미규정이다. 금관회는 2026-08-04 2단계 시행(국내 VASP 간 2026-10 → 국경 간 2027년 말)을 발표했고 經濟日報(2026-09-03)가 이를 보도했다. 《虛擬資產服務法》은 2026-06-30 입법원 통과(시행일 미정).
entity: reg:tw-vasp-aml-reg-art7
source_url: https://notabene.id/world/taiwan ; https://money.udn.com/money/story/5613/9732991 ; https://news.cnyes.com/news/id/6557030
publisher: Notabene(2026-08-10 갱신) ; 經濟日報 ; 鉅亨網
tier: T3 / T4 / T4
confidence: B
retrieved: 2026-10-21
quote: "except for Article 7, which shall enter into force from a date to be separately specified by the FSC." (Notabene) ; "金管會規劃的FATF「轉帳規則」（Travel Rule）也將於2026年10月起分兩階段推行" (經濟日報)
note: 2026-10-21 기준 第7條 시행일 고시 여부 미확인. law.moj.gov.tw 원문 미열람(§8).
F-057
claim: 태국 SEC 는 AMLO 와 협의해 2026-09-02 디지털자산 사업자에 송·수신인 식별·정보 전송·상대 VASP 실사·자기수탁 지갑 소유·통제 검증을 요구하는 과도 규칙을 확정 발표했고 준수기한은 2027-02-27 이다. 고시번호(Sor Thor. 9/2026 설)·THB 30,000 심화 기준은 미확인이다.
entity: reg:th-sec-travel-rule-2026
source_url: https://sumsub.com/media/news/thailand-introduces-new-crypto-travel-rule-compliance-requirements/ ; https://fintechnews.sg/136660/thailand/thailand-crypto-travel-rule/
publisher: Sumsub(2026-09-04) ; Fintech News Singapore(2026-09-03)
tier: T3 / T4
confidence: B(발표·기한) / D(고시번호·임계)
retrieved: 2026-10-21
quote: "have until February 27, 2027, to introduce new checks identifying the parties behind digital asset transfers." ; "Operators must also verify who owns or controls self-hosted wallets used to send or receive digital assets."
note: sec.or.th 는 403. 상태 enacted-not-in-force.
F-058
claim: 인도네시아 OJK SEOJK No. 16/SEOJK.07/2025(2025-07-03 제정·발효; POJK 27/2024·POJK 8/2023 근거)는 디지털금융자산(AKD) 이전에 트래블룰을 의무화하며, 공식 FAQ 에 따르면 USD 1,000 이상은 송·수신인 전체 정보(성명·지갑주소·주소·신분증), 미만은 성명·지갑주소만 요구한다.
entity: reg:id-seojk-16-2025
source_url: https://ojk.go.id/id/regulasi/Pages/SEOJK-16-SEOJK07-2025-Penerapan-Program-APU-PPT-dan-Pencegahan-Pendanaan-Proliferasi-Senjata-Pemusnah-Massal-Pedagang-AKD.aspx ; (FAQ PDF) https://ojk.go.id/id/regulasi/Documents/Pages/SEOJK-16-SEOJK07-2025-Penerapan-Program-APU-PPT-dan-Pencegahan-Pendanaan-Proliferasi-Senjata-Pemusnah-Massal-Pedagang-AKD/FAQ%20SEOJK%2016-SEOJK07-2025%20Penerapan%20Program%20APU%20PPT%20dan%20Pencegahan%20Pendanaan%20Proliferasi%20Senjata%20Pemusnah%20Massal%20bagi%20Pedagang%20AKD.pdf
publisher: OJK
tier: T1 / T2
confidence: A
retrieved: 2026-10-21
quote: "ii. Transfer AKD dengan nilai USD1.000 atau lebih: informasi lengkap pengirim dan penerima (nama, alamat wallet, alamat, dokumen identitas). iii. Transfer AKD dengan nilai kurang dari USD1.000: nama pengirim dan alamat wallet pengirim, nama penerima dan alamat wallet penerima."
note: 유형 B, 통화 USD(IDR 아님), 경계 「atau lebih」(이상). SEOJK 본문 PDF 는 타임아웃 — 조항 번호 미확인.
```
### 4.11 메시지 표준·프로토콜·솔루션 (벤더 간 우열 평가 없음 — 공개 사실만)
```
F-059
claim: IVMS101 의 현행판은 「IVMS 101.2023, interVASP data model standard Issue 1 FINAL」(PayloadVersionCode 「101.2023」, 「Published August 2023」)이며, 2020-05 원판은 JWG 가, 2023 판은 GDF·OpenVASP·VASPnet 이 2023-04 결성한 interVASP Standards Working Group(ISWG; GDF Open Standards Council 산하)이 유지하고, ISWG 는 2024-06-04 갱신을 공표했다. 표준 문서에는 JSON/XML 스키마가 포함되지 않는다(구현체가 별도 관리).
entity: std:ivms101-2023
source_url: https://intervasp.org/ ; https://cdn.jsdelivr.net/npm/ivms101@2.0.0/specs/ivms101-2023.pdf
publisher: interVASP ISWG (표준 PDF 는 21 Analytics npm 패키지 미러)
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "The ISWG released an update to IVMS 101 on 4 June 2024." ; "This standard, IVMS 101.2023, was developed under the auspices of the interVASP Standards Working Group (ISWG). It is an update to, and derived from, the original IVMS 101 interVASP data model standard, developed in 2020"
note: 저장소 산문의 「IVMS101 v2 등 표준 발전」 전망은 근거 없음 — 현행 명칭은 101.2023. 2020→2023 변경 목록(errata/enhancements)은 협의안 문서 미열람으로 미확정.
F-060
claim: IVMS 101.2023 은 LEIText(ISO 17442, 20자) 데이터형과 NationalIdentifierTypeCode(ISO 20022 TypeOfIdentification4Code 제한; LEIX 포함)를 정의하고, 제약 C7(법인은 RAID/MISC/LEIX/TXID), C9(LEIX 면 registrationAuthority 금지, 비LEIX 면 필수), C10(GLEIF RA 목록), C11(validLEI), 자연인 originator 필수항목 C1(geographicAddress[GEOG/HOME/BIZZ] 또는 customerIdentification 또는 nationalIdentification 또는 dateAndPlaceOfBirth 중 1 이상), 주소유형 GEOG(IVMS 고유 추가)를 둔다.
entity: std:ivms101-2023
source_url: https://cdn.jsdelivr.net/npm/ivms101@2.0.0/specs/ivms101-2023.pdf
publisher: interVASP ISWG
tier: T1
confidence: A
retrieved: 2026-10-21
quote: "C1 OriginatorInformationNaturalPerson If the originator is a NaturalPerson either (geographicAddress with an addressType value of 'GEOG' or 'HOME' or 'BIZZ') and/or customerIdentification and/or nationalIdentification and/or dateAndPlaceOfBirth is required."
note: 산문 travel-rule-protocols.md §2 의 「DateAndPlaceOfBirth (선택)」·「EU TFR: 모든 필드 필수」는 C1 의 「택1 이상」 구조와 TFR 제14조(주소 **또는** 생년월일·출생지)를 반영해 정정 대상(§9).
F-061
claim: Notabene(2020 설립; 제품 SafeTransact·Notabene Flow·TAP)은 2026-10-21 자사 페이지에서 「2,000+ VASPs in Network / 280+ Notabene Customers / 100+ Jurisdictions / $2T+ Transaction Volume」을, 2026-07-23 보도자료에서 Ripple 의 비공개 금액 전략투자와 「more than 2,300 connected institutions」를 밝혔다. 자사 TRP 페이지는 「Every Notabene customer has a live TRP 1.0 endpoint」라며 OpenVASP 회원임을 밝힌다. 기준일 이전 M&A·폐업 없음.
entity: vnd:notabene
source_url: https://notabene.id/about-us ; https://notabene.id/post/notabene-announces-strategic-investment-from-ripple ; https://notabene.id/travel-rule-messaging-protocols/trp
publisher: Notabene
tier: T3
confidence: B(자사 주장)
retrieved: 2026-10-21
quote: "The network spans more than 2,300 connected institutions" ; "Every Notabene customer has a live TRP 1.0 endpoint."
note: 자사 페이지 간 수치 불일치(2,000+ vs 2,300+; $1T vs $2T). 산문의 「1,500+ VASP」는 낡은 수치. 2024 Series B($14.5M 설)는 1차 미확인. Notabene 페이지의 「TRP 채택 감소」 주장은 이해관계자 단일 서술(D).
F-062
claim: Sumsub Travel Rule 은 2026-10-21 자사 프로토콜 페이지에서 Sumsub(자체)·GTR·CODE(CodeVASP)·TRP(「Limited」)·Sygna 5개 프로토콜 연동과 「2,100+ VASPs」, 10대 VASP 중 7 포함을 주장하며, 비호스팅 지갑은 자체 프로토콜과 블록체인 분석 파트너를 통한 「multiple verification methods」로 검증한다고 적는다.
entity: vnd:sumsub
source_url: https://sumsub.com/protocols/
publisher: Sumsub
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "Sumsub provides the broadest Travel Rule protocol coverage, enabling VASPs"
note: Sygna 연동(2024-09 설)·CODE 연동 일자는 스니펫 수준(C). 저장소 산문의 「본사 영국」은 본 조사에서 미확인.
F-063
claim: VerifyVASP 는 2026-10-21 홈페이지(저작권 2025)에서 「150+ Member VASPs / 30+ Jurisdiction Coverage」와 TravelRule API·VerifyName API·VerifyWallet 제품을 표시하며 운영 주체(람다256·두나무·Chainalysis)를 홈페이지에 명시하지 않는다. CODE 홈페이지는 VerifyVASP 를 「Interoperability」 목록과 파트너 로고에 올려 양 네트워크 연동이 유지되고 있음을 보여준다(VerifyVASP 측 페이지는 CODE 미언급).
entity: vnd:verifyvasp ; vnd:code
source_url: https://www.verifyvasp.com/ ; https://www.codevasp.com/
publisher: VerifyVASP ; CODE Inc.
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "150+ verified VASPs across 30+ jurisdictions with full counterparty information." (VerifyVASP) ; "Connect across protocols with a single integration." (CODE — 연동 목록: CodeVASP, VerifyVASP, GTR, Sumsub, Sygna, Notabene, CryptoSwift)
note: 산문 「VerifyVASP ↔ CODE 연동 2022-05 완성」·「3개월 공백」 서술의 1차 근거(2022 보도)는 이번에 재열람하지 못함(C). Chainalysis 합작 지분 구조도 홈페이지에서 미확인.
F-064
claim: CODE(CODE Inc., 대표 이성미, 사업자등록 824-87-02026, LEI 988400S6ZLJS1V0AOC43)는 2026-10-21 홈페이지에 「350+ VASPs / 60 jurisdictions / 9.75M+ transactions / $289B+ volume」과 2025-12-10 Transaction Visualizer, 2025-12-23 CryptoSwift 연동, 2026-01-19 FIXT 가입, 2026-01-29 VEAT 법무법인 파트너 회원, 2026-03-25 신규 비호스팅 지갑 식별 솔루션, 2026-05-22 안랩블록체인컴퍼니 VASP 신고 완료·CodeVASP 채택 소식을 게시했다. 파트너 로고에 Bithumb·Coinone·Digital-X·Bybit·OKX 가 있고 Korbit 로고는 캡처되지 않았다.
entity: vnd:code
source_url: https://www.codevasp.com/
publisher: CODE Inc.
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "Your infrastructure. Your keys. Your security policy. Your customer data."
note: 산문의 「빗썸·코빗·코인원 3사 균등 출자」 지분 구조는 홈페이지에서 확인 불가 — 2022 보도 기반(C). 일부 「Lifetime」 카운터가 「0.00M+」 자리표시자로 표시됨.
F-065
claim: GTR(Global Travel Rule)은 Infozone Technologies Pte. Ltd.(싱가포르, 317 Outram Road) 가 운영하며 2026-10-21 홈페이지에 얼라이언스 회원 13(Binance·BingX·Bitget·Bybit·Ceffu·Circle·CoinSwitch·CoinTR·DTC Pay·Gate.io·HashKey Exchange·OKX·Paymonade), 지원 프로토콜 Code·Sumsub·Sygna·Fireblocks, 제품(API·Manual·Wallet Verification·Out-Of-Network), 최신 게시물 2026-08-09 를 표시한다. 21 Analytics 용어집은 Infozone 을 「a Binance company」라 적는다.
entity: vnd:gtr
source_url: https://www.globaltravelrule.com/ ; https://21analytics.co/glossary/gtr-binance-travel-rule
publisher: Infozone Technologies (GTR) ; 21 Analytics
tier: T3
confidence: B(회원·프로토콜) / C(Binance 소유)
retrieved: 2026-10-21
quote: "We offer an easy, one-time integration with the largest exchange in the world (Binance)." (GTR) ; "GTR is run by Infozone Technologies PTE, a Binance company." (21 Analytics)
note: 산문의 「GTR = BitGo 등 컨소시엄, 일부 미국·중남미」 서술은 근거 없음 — 정정 대상(§9). GTR 사이트의 VASP 수 카운터는 「0」 자리표시자.
F-066
claim: TRISA 는 2026-10-21 trisa.dev 에서 gRPC/protobuf 기반 오픈소스 프로토콜과 Global Directory Service 를 설명하고 오픈소스 노드 「Envoy」가 TRISA 와 TRP 를 모두 지원한다고 밝히며, GitHub trisacrypto/trisa 는 공개·비보관(232 커밋) 상태다. 같은 날 trisa.io 는 응답하지 않았고 github.com/trisacorp/trisa 는 404 였다.
entity: vnd:trisa
source_url: https://trisa.dev/ ; https://github.com/trisacrypto/trisa ; https://trisa.io/ (무응답)
publisher: TRISA
tier: T3 / A(관측)
confidence: B
retrieved: 2026-10-21
quote: "TRISA has released an open source node called \"Envoy\"." ; (Envoy) "may help your organization quickly get up and running with both the TRISA and TRP protocols."
note: 산문의 「CipherTrace 시작 → Mastercard 인수」는 역사적 사실로 Sygna 페이지(「CipherTrace's TRISA」)가 간접 뒷받침. GDS 운영 상태·회원 수·TRISA–TRP 상호운용(2023-11 설)은 미확인. 접속 불가만으로 폐업 추정 금지.
F-067
claim: OpenVASP Association(Zug, c/o MME Legal AG)은 TRP 를 「Bilateral exchange of encrypted data (VASP-to-VASP). No data or metadata is ever exchanged with any third party」로 설명하고 ISO 24165(DTI)·IVMS101 호환, 주간 TRP Working Group, GitLab(CC BY-SA 4.0, 2020-05-06 생성, 116 커밋, 태그 0) 공개 사양을 유지하며, 벤더로 21 Analytics·Blockchain Intelligence Group·ospree 를 든다. 현행 TRP 버전 번호는 사이트에 표시되지 않는다.
entity: vnd:openvasp-trp
source_url: https://www.openvasp.org/ ; https://www.openvasp.org/trp ; https://gitlab.com/OpenVASP/travel-rule-protocol
publisher: OpenVASP Association
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "Travel Rule Protocol (TRP) is a protocol standard for the FATF Travel Rule (Recommendation 16)."
note: 산문의 「OpenVASP: Ethereum·ENS·Whisper 기반, 활용도 낮음」은 2020년 이전 설계 서술 — 2026-10-21 기준 OpenVASP 는 TRP 의 모체 협회(§9). TRP↔Notabene: Notabene 측 TRP 1.0 지원(F-061).
F-068
claim: Shyft Veriscope 는 Notabene 프로토콜 페이지에서 「No longer actively developed … the protocol seems to have been discontinued」로 기재된다(2022-02-21 기준 2,321 건 지갑 증명 거래). Shyft 측 1차 공지·중단 일자는 확보되지 않았다.
entity: vnd:shyft-veriscope
source_url: https://notabene.id/travel-rule-messaging-protocols/shyft-network
publisher: Notabene(제3자)
tier: T3
confidence: C
retrieved: 2026-10-21
quote: "Please note that this document is for historical purposes only, as the protocol seems to have been discontinued."
note: Sygna 홈페이지는 여전히 「Veriscope on Shyft」 상호운용을 표기 — 낡은 서술로 보임(§5).
F-069
claim: Sygna(CoolBitX)는 2026-10-21 sygna.io(저작권 2026)에서 Sygna Bridge 2.0·IVMS101 지원, 3,000+ 자산, TRISA·Veriscope 상호운용, 분석 파트너(Chainalysis·Elliptic·Merkle Science·Coinfirm·Dow Jones·ComplyAdvantage)를 표시하며 Sumsub(「Live」)·GTR·CODE 가 지원 프로토콜로 올린다. 2024~2026 일자 뉴스는 홈페이지에 없다.
entity: vnd:sygna
source_url: https://www.sygna.io/ ; https://sumsub.com/protocols/ ; https://www.globaltravelrule.com/
publisher: Sygna ; Sumsub ; GTR
tier: T3
confidence: B
retrieved: 2026-10-21
quote: "interoperability enabled with other protocols like CipherTrace's TRISA & Veriscope on Shyft"
note: VASP 수·대만 CoolBitX 소유 구조는 페이지에서 미확인.
F-070
claim: 21 Analytics 는 2026-10-21 기준 도메인을 21analytics.ch → 21analytics.co 로 이전(301)했고, AOPP 용어집에서 540+ 지갑·2,800+ 자산 지원과 수동 서명 대비 자동화를 주장하며, OpenVASP 가 TRP 벤더·도구(Travel Address Encoder/Decoder) 호스트로 든다. aopp.group 은 같은 날 접속 거부였다.
entity: vnd:21analytics
source_url: https://21analytics.co/glossary/address-ownership-proof-protocol-aopp ; https://www.openvasp.org/trp ; https://aopp.group/ (ECONNREFUSED)
publisher: 21 Analytics ; OpenVASP
tier: T3 / A(관측)
confidence: B
retrieved: 2026-10-21
quote: "supports over 540 different wallets and 2800+ digital assets" ; "Unlike the traditional manual signing method, AOPP is completely automated, fast and user-friendly."
note: AOPP 의 스위스 은행 기원·2021-01 지갑 개발사 반발(Trezor·BlueWallet·Sparrow 지원 철회) 역사는 1차 출처 404 로 미검증(§8).
F-071
claim: TRUST(Travel Rule Universal Solution Technology)는 Coinbase 가 운영하는 비영리 연합 폐쇄형 네트워크로 2021-12 출범, 2022-05 글로벌 확장, 「as of early 2025 … over 125 VASPs」, 20+ 관할이며, 해시 주소 게시판+암호화 P2P 채널 구조로 외부 벤더 직접 연결을 허용하지 않는다(Notabene 서술). coinbase.com/travelrule 은 2026-10-21 HTTP 403.
entity: vnd:trust
source_url: https://notabene.id/travel-rule-messaging-protocols/ustrwg
publisher: Notabene(제3자·경쟁사)
tier: T3
confidence: C
retrieved: 2026-10-21
quote: "TRUST is a network operated by Coinbase that (as of early 2025) comprises over 125 VASPs" ; "Coinbase does not allow external vendors to interact directly with TRUST, Notabene cannot connect directly with it today."
note: 저장소 산문 3편 어디에도 TRUST 가 없다 — 미국 주요 VASP 경로 누락(§9). 2026 회원 수는 1차 미확인.
F-072
claim: 자기수탁 지갑 소유 검증 4방법 — AOPP(포털 링크로 자동 암호서명, 온체인 거래 불필요, 호환 지갑 한정), 수동 메시지 서명(모든 지갑이 지원하지 않음), Satoshi test(지정 소액 송금; 수수료·확인 지연·주소 재사용 프라이버시 비용), 시각적 증명(스크린샷·영상; 위조 가능, 키 통제 미증명) — 는 21 Analytics 개요(2026-10-19)로 정리되며, 규제 수용은 EU EBA GL ¶83(⒞ 소액송금 ⒟ 서명 ⒠ 기타 기술수단; 1종 이상)·스위스 FINMA 02/2019(「suitable technical means」, 방법 미지정)·한국 감독규정 §28-2④(동일인 요건만, 방법 미지정)·태국 SEC(소유·통제 검증 의무, 방법 미지정)로 확인된다. 영국 reg 64G 는 소유 증명 의무 대신 정보요청·지급보류 구조다.
entity: vnd:21analytics ; reg:eu-eba-gl-2024-11 ; reg:ch-gwv-finma-art10 ; reg:kr-fiu-supervisory-rule-2026-2
source_url: https://www.21analytics.co/blog/unhosted-wallet-verification-methods-an-overview ; (규제 근거) F-026 · F-052 · F-018 · F-057 · F-033 의 URL
publisher: 21 Analytics ; EBA ; FINMA ; 금융정보분석원 ; SEC Thailand(2차) ; legislation.gov.uk
tier: T3(방법 개요) / T1·T2(규제)
confidence: B
retrieved: 2026-10-21
quote: "A convincing screenshot does not, by itself, establish that the customer controls the private key" (21 Analytics) ; "e) other suitable technical means as long as they allow for reliable and secure assessment and the CASP is fully satisfied that it knows who owns or controls the address." (EBA ¶83)
note: 벤더별 채택 방법은 CODE(비호스팅 지갑 화이트리스트·2026-03-25 식별 솔루션), GTR(Wallet Verification; 2026-07-27 「Wallet Verify」 게시물), VerifyVASP(VerifyWallet), 21 Analytics(AOPP)만 확인. 서명 표준(EIP-191/BIP-137) 사용 여부·네덜란드 DNB·영국 JMLSG 문언은 미확인(§8).
```
### 4.12 데이터 품질·쟁점·문헌
```
F-073
claim: Notabene 「State of Crypto Travel Rule 2025」(2025-04-23; VASP 91·규제기관 10 설문)는 100% 가 2025 년 말까지 준수 계획, 수익자 정보 확인 전 출금 차단 VASP 비중 2.9%(2024)→15.4%, 송신인 정보 누락 입금 반환 VASP 19.8%, EU CASP 발 거래량 200배 증가(비EU 8배), 「71% of EU Crypto Asset Service Providers missed this deadline」, 반복 미준수 상대방을 규제기관에 보고하는 절차 보유 1/3 을 보고한다. 거절률·필드 누락률·이름 불일치율 통계는 없다. 2026 판은 발견되지 않았다.
entity: vnd:notabene
source_url: https://notabene.id/post/state-of-crypto-travel-rule-2025report
publisher: Notabene
tier: T3(벤더 설문)
confidence: B
retrieved: 2026-10-21
quote: "the report shows that 100% of firms plan to be Travel Rule compliant by the end of 2025." ; "Transaction volumes originating from EU Crypto Asset Service Providers increased by 200x"
note: 저장소 산문 travel-rule-protocols.md §N.4 「오류 분포 Top 5(35%/22%/18%/12%/8%)」와 §M.6 SLA·Sunrise 비율(5~15%)은 어떤 공개 출처로도 확인되지 않음 — 「추정」 표기가 있더라도 수치 삭제 또는 출처 명시 필요(§9). Sumsub·21 Analytics 데이터품질 통계는 미확보.
F-074
claim: 2025~2026 트래블룰 관련 학술·정책 문헌(메타데이터만 확인, 초록·본문 미열람): ① Shevchuk, Adamyk, Kovalchuk 외, 「Privacy-Enhancing Technologies for FATF Crypto Travel Rule: Balancing Compliance and Data Protection」, Informatyka Techniczna i Sztuczna Inteligencja, 2025-12, DOI 10.53052/9788367652520.05 ② Gaisina & Finger, 「Anti-money laundering (AML) effectiveness and cryptocurrency regulations: an empirical analysis of the introduction of VASPs licensing and AML crypto laws」, Journal of Financial Regulation and Compliance, 2026-02-27, DOI 10.1108/jfrc-10-2025-0319 ③ World Bank, 「AML/CFT National Risk Assessment on Virtual Assets and VASPs: Guidance Manual」, 2025-10-18, DOI 10.1596/43905 ④ Li, Feng, Ding, Ma, 「Balancing Privacy and Compliance in DeFi: A Zero-Knowledge-Based Auditable Cross-Chain Framework」, arXiv:2608.15276, 2026-08-15(트래블룰을 감사 접근의 법적 트리거로 인용) ⑤ Commey 외, Ghana 2025 VASP Act 비교, Journal of Money Laundering Control, 2026-07-02, DOI 10.1108/jmlc-12-2025-0247.
entity: —
source_url: https://api.crossref.org/works?query=%22travel%20rule%22%20virtual%20asset%20service%20providers%20FATF&filter=from-pub-date:2025-01-01&rows=15 ; http://export.arxiv.org/api/query?search_query=all:%22travel%20rule%22%20AND%20(all:crypto%20OR%20all:%22virtual%20asset%22%20OR%20all:blockchain)&max_results=15
publisher: Crossref ; arXiv
tier: T3(서지 메타데이터)
confidence: C
retrieved: 2026-10-21
quote: none captured (서지만)
note: 상세 문헌조사는 별도 도시에 위임. 여기 목록은 존재·서지 확인용이며 각 논문의 결론은 인용하지 않는다. SSRN·BIS·IMF·ECB 는 미조회.
```

## 5. 상충·의문점

| 쟁점 | 출처 A 주장 | 출처 B 주장 | 판단 | 재검증 방법 |
|---|---|---|---|---|
| 한국 기준금액 폐지 시행일 | 법제처 eflaw 색인: 시행예정 판본 시행일자 **20270219** (F-012) | 이데일리·쟁글: 「2027년 2월 20일」 (F-012) | A 채택. 공포 08-18 → 「공포 후 6개월이 경과한 날」= 02-19. 언론은 공포일을 08-19 로 가정한 듯 | 2027-02 법제처 「현행」 전환 시 재확인; 금융위 시행 보도자료 |
| 시행령 제10조의10 조문 단위 시행일 메타데이터 | 헤더 「20270219:제10조의10」·부칙 단서 | 조문 단위 `<조문시행일자>` 20260820 / 현행본(MST 290511) XML 은 「모든 경우」 문언 표시 (F-014) | 부칙·헤더 우선. 법제처 레코드 결함으로 봄. **현행 조문을 API 로 자동 추출하는 파이프라인은 이 사례에서 틀린 답을 낸다** | DRF `efYd` 지정 호출로 시점별 문언 비교를 정례화 |
| 감독규정 제28조의2 시행일 | 고시 부칙 「공포 후 6개월」, 발령 2026-08-20 → 2027-02-21 산정 (F-019) | 시행령 §10-20 은 2027-02-19 (F-012) | 2일 어긋날 가능성. 고시의 「공포」가 관보 게재일이면 또 달라짐 | 법제처 행정규칙 시행일 색인·FIU 고시 관보 확인 |
| FATF 7차 Update 발표일 | FATF 색인·VASPnet·financialcrime.lu·Comsure: 2026-07-16 | Notabene: 「July 15, 2026」; CMS 페이지 날짜 07-20 | 07-16 채택 | FATF 페이지 접근 가능 시 확정 |
| 7차 Update 집행 격차 수치 | Notabene·VASPnet: 입법 91 중 **55(60%)** 조치 없음 | financialcrime.lu: 「almost half」; Comsure: 「Only 40% … have taken action」(=36/91, 산술 일치) | 55/91 채택(두 출처 수치 일치; 「almost half」는 부정확 요약) | FATF PDF ¶26 전후 원문 |
| INR.15 §7 각주 번호 | KB(2026-07-30 PDF): 각주 **48** 「As defined in INR. 16, paragraph 9」 | OJK: 「footnote 46 to paragraph 7 of INR.15」 참조 갱신 (F-003) | 판본 간 번호 재배열 또는 OJK 오기. 본문 변경 없음은 양측 일치 | 2025-06 판 PDF p.80 재열람 |
| FATF R.16 「구조화 데이터·ISO 20022」 | 저장소 산문 §9 「메시징 표준 명확화」; 업계 통설 | 본 조사 T2 요약은 「consistency of information」·「standardised requirements … above USD/EUR 1,000」까지만 (F-001, F-002) | 미확정. 산문 서술을 A 로 격상할 근거 없음 | INR.16 2025 판 ¶ 원문 |
| 영국 £800 의 시점 | 저장소(2026-08-04): 「£800 이상」 | 2023-09-01 원문 「1,000 euros」; 2026-06-30 치환 (F-030, F-031) | 둘 다 맞되 **시점이 다름**. KB 에 valid_from/valid_to 분리 필요 | 완료(legislation.gov.uk 두 시점 판본) |
| 홍콩 「2024-06-01」 | 과제 지시문·업계 일부 | 모든 출처: 2023-06-01 시행, 2024-01-01 즉시전송 (F-048) | 2024-06-01 은 트래블룰 일자가 아님(12개월 과도기간 종료와 혼동 추정) | SFC 2023-05 회람·AMLO 개정령 부칙 |
| UAE VARA 경계값 | 룰북 ¶2 「exceeding AED 3,500」 (F-051) | 21 Analytics FAQ: 「equal to or exceeding AED 3500」 | T1 우선 — 정확히 3,500 은 대상 외 | VARA 룰북 최신 판본(2025-05-19 이후) |
| 호주 트래블룰 시행일 | AML/CTF Rules 2025: 2026-03-31 (F-050) | Notabene AU 페이지 본문: 「July 2026 effective date」 | 03-31 채택(Tranche 2 신규 기업 의무 개시 07-01 과 혼동) | AUSTRAC 페이지(타임아웃) 재시도 |
| Shyft Veriscope 상태 | Notabene: 중단 (F-068) | Sygna 홈페이지: 「Veriscope on Shyft」 상호운용 표기 | 중단 쪽 유력(Sygna 표기는 미갱신) | Shyft 공식 채널 |
| 캐나다 기록의무 발동 금액 | CryptoSlate: CAD 1,000 이상 VC 이전 기록 | PCMLTFR s.30 열람 범위에는 CAD 10,000 수취 기록만 (F-053) | 미확정 — 비교표에 「조문상 없음/연계 미확인」 | PCMLTFR s.12·s.30·s.33.x 전수 |
| 한국 제재와 트래블룰 | 업계 일부 「트래블룰 위반 제재」 통념 | 두나무·코인원·빗썸·코빗 제재 사유에 제5조의3 없음 (F-022) | 트래블룰 독립 제재 사례 없음 | KoFIU 제재공시(404 복구 후) 전수 |

## 6. 출처 레지스트리

| source_id | 기관 | URL | tier | 갱신주기 | 접근 | 비고 |
|---|---|---|---|---|---|---|
| SRC-kr-law-drf | 법제처 국가법령정보센터 DRF | https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=law&type=JSON&query=… | T1 | 수시 | 공개(OC=test 동작) | `target=eflaw` 로 시행예정 판본, `target=admrul` 로 고시; `lsHistory` 는 미신청 오류 |
| SRC-kr-fsc-press | 금융위원회 보도자료 | https://www.fsc.go.kr/no010101 | T2 | 일 | 공개 | 2026-08-11 #87499, 2026-03-30 #86589, 2026-01-29 #86168 |
| SRC-kr-kofiu-sanction | 금융정보분석원 제재공시 | https://www.kofiu.go.kr/ | T1 | 수시 | 공개 | 2026-10-21 하위경로 404 — 경로 재확인 필요 |
| SRC-eu-eba-gl | EBA Travel Rule Guidelines PDF | https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf | T1 | 정적 | 공개 | 24개 언어판·준수표(2026-03-17) 동일 페이지 |
| SRC-eu-eurlex-tfr | EUR-Lex CELEX 32023R1113 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R1113 | T1 | 정적 | 공개 | 2026-10-21 fetcher 에 빈 응답 — CELLAR 내용협상 경로 유지 |
| SRC-gb-legislation | legislation.gov.uk | https://www.legislation.gov.uk/uksi/2017/692/regulation/64C ; https://www.legislation.gov.uk/uksi/2026/621/made | T1 | 수시 | 공개 | 시점 URL(`/2023-09-01`) 지원 |
| SRC-gb-fca | FCA 성명·과징금 | https://www.fca.org.uk/news/news-stories/2026-fines | T1/T2 | 수시 | 공개 | 2024·2025 연도 페이지 미점검 |
| SRC-us-lii-cfr | Cornell LII 31 CFR 1010.410 | https://www.law.cornell.edu/cfr/text/31/1010.410 | T1(미러) | eCFR 동기 | 공개 | ecfr.gov·federalregister.gov 본문은 unblock 리다이렉트 |
| SRC-us-fr-api | Federal Register API | https://www.federalregister.gov/api/v1/documents.json?conditions[term]=%221010.410%22&conditions[agencies][]=financial-crimes-enforcement-network | T1 | 일 | 공개 | 본문 페이지는 차단되나 API 는 정상 |
| SRC-us-reginfo | OIRA Unified Agenda | https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202504&RIN=1506-AB41 | T1 | 반기 | 공개 | 철회 일자 원천 |
| SRC-us-treasury-genius | 재무부 GENIUS 보고서 | https://home.treasury.gov/system/files/246/GENIUS-Act-Illicit-Finance-Innovation-Congressional-Report-March-2026.pdf | T1 | 정적 | 공개 | 34쪽 PDF |
| SRC-us-fincen-news | FinCEN 보도자료 | https://www.fincen.gov/news/news-releases/fincen-assesses-35-million-penalty-against-paxful-facilitating-suspicious | T1 | 수시 | 공개 | — |
| SRC-jp-egov-api | e-Gov 法令API | https://laws.e-gov.go.jp/api/1/articles;lawId=419AC0000000022;article=10%E3%81%AE5 | T1 | 수시 | 공개 | 枝番 URL 인코딩 필요 |
| SRC-jp-fsa | 金融庁 公表資料 | https://www.fsa.go.jp/news/r4/sonota/20230526/20230526.html | T2 | 수시 | 공개 | 2025-06-25 PDF 는 바이너리 미추출 |
| SRC-sg-mas-psn02 | MAS PSN02 개정 대조판 | https://www.mas.gov.sg/-/media/amld-amendments---30-june-2025/mas-notice-psn02-amendment--new.pdf | T1 | 개정 시 | 공개 | Published Version 우선 고지 |
| SRC-sg-mas-enf | MAS Enforcement Actions | https://www.mas.gov.sg/regulation/enforcement/enforcement-actions | T1 | 수시 | 공개 | 1쪽만 점검 |
| SRC-lawfirm-hk-au | Clyde & Co(HK 2023-06-07) · Norton Rose Fulbright(AU 2025-12) | https://www.clydeco.com/en/insights/2023/06/hong-kong-virtual-assets-regulatory-update ; https://www.nortonrosefulbright.com/en-sg/knowledge/publications/4bdd08b3/australia-amlctf-reforms-a-new-era-in-financial-crime-prevention | T3 | 정적 | 공개 | AUSTRAC·eLegislation 원문 대체 |
| SRC-ae-vara | VARA Rulebooks | https://rulebooks.vara.ae/node/146 | T1 | 개정 시 | 공개 | Part III.G |
| SRC-ch-fedlex | Fedlex SR 955.033.0 | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2015/390/20230101/de/html/fedlex-data-admin-ch-eli-cc-2015-390-20230101-de-html-4.html | T1 | 개정 시 | 공개 | 2023-01-01 통합본 |
| SRC-ch-finma | FINMA 02/2019 PDF | https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/4dokumentation/finma-aufsichtsmitteilungen/20190826-finma-aufsichtsmitteilung-02-2019.pdf | T2 | 정적 | 공개 | — |
| SRC-ca-justice | Justice Laws PCMLTFR | https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/section-124.1.html | T1 | 수시 | 공개 | 통합본 2026-09-30 |
| SRC-ca-fintrac | FINTRAC 지침·AMP | https://fintrac-canafe.canada.ca/pen/amps/pen-2025-10-22-eng | T1/T2 | 수시 | 공개 | — |
| SRC-br-bcb-520 | Res. BCB 520 (미러) | https://www.migalhas.com.br/arquivos/2025/11/23462FAD2E8205_Resolucao520.pdf | T1(미러) | 정적 | 공개 | 원본 normativos.bcb.gov.br 미열람 |
| SRC-id-ojk | OJK SEOJK 16/2025 + FAQ | https://ojk.go.id/id/regulasi/Pages/SEOJK-16-SEOJK07-2025-… | T1/T2 | 개정 시 | 공개 | 본문 PDF 타임아웃 |
| SRC-tw-th-secondary | Notabene Taiwan · Sumsub Thailand | https://notabene.id/world/taiwan ; https://sumsub.com/media/news/thailand-introduces-new-crypto-travel-rule-compliance-requirements/ | T3 | 수시 | 공개 | 1차(FSC·SEC) 미열람 |
| SRC-intl-fiu-summaries | CSSF · FIAU Malta · OJK (FATF 2차 요약) | https://www.cssf.lu/en/Document/fatf-enhances-transparency-in-payments-through-the-modification-to-the-recommendation-16-of-its-standard/ ; https://fiaumalta.org/news/latest-updates-from-the-fatf/ ; https://ojk.go.id/apu-ppt/id/berita-dan-kegiatan/publikasi/Pages/FATF-Recommendation-Updated-Juni-2025.aspx | T2 | 월 | 공개 | FATF 403 시 1차 대체 |
| SRC-intl-7th-update-summaries | VASPnet · Notabene (7차 Update 요약) | https://vaspnet.com/articles/from-rules-to-results-fatfs-seventh-targeted-update-on-virtual-assets-and-vasps ; https://notabene.id/post/fatfs-seventh-targeted-update-on-virtual-assets | T4/T3 | 수시 | 공개 | FATF 403 대체 |
| SRC-std-intervasp | interVASP ISWG | https://intervasp.org/ ; https://cdn.jsdelivr.net/npm/ivms101@2.0.0/specs/ivms101-2023.pdf | T1 | 수시 | 공개 | — |
| SRC-vnd-* | Notabene·Sumsub·VerifyVASP·CODE·GTR·TRISA·OpenVASP·Sygna·21 Analytics 홈페이지 | §4.11 각 URL | T3 | 수시 | 공개 | trisa.io·aopp.group·coinbase.com/travelrule 접속 불가(2026-10-21) |
| SRC-biblio | Crossref / arXiv API | https://api.crossref.org/works?query=… ; http://export.arxiv.org/api/query?… | T3 | 일 | 공개 | 서지만 |

## 7. 일일 수집 후보 (Ingestion Hooks) — 2026-10-21 실제 접속 확인분

| 명칭 | 방식 | 엔드포인트 | 포맷 | 갱신빈도 | 인증 | 라이선스/약관 주의 |
|---|---|---|---|---|---|---|
| 법제처 DRF 시행일 법령(특금법 시행령) | API | `https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=eflaw&type=JSON&query=특정금융거래정보의보고및이용등에관한법률시행령` | JSON | 일 1회 | OC(test 동작; 정식 발급 권장) | 공공데이터 이용약관; 2027-02-19 「현행」 전환 감시 |
| 법제처 DRF 행정규칙(감독규정) | API | `https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=admrul&type=JSON&query=특정 금융거래정보 보고 및 감독규정` | JSON | 일 1회 | 동일 | 고시 번호 변경 감시(2026-10-21 기준 제2026-3호) |
| 법제처 DRF 조문 XML(시점 지정) | API | `https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20270219&type=XML` | XML | 변경 시 | 동일 | 조문 단위 시행일 메타데이터 결함 주의(§5) |
| 금융위 보도자료 검색 | HTML | `https://www.fsc.go.kr/no010101?srchKey=sj&srchText=특정금융정보법` | HTML | 일 1회 | 없음 | 저작권 KOGL 확인 |
| Federal Register API (FinCEN, 1010.410) | API | `https://www.federalregister.gov/api/v1/documents.json?conditions[term]=%221010.410%22&conditions[agencies][]=financial-crimes-enforcement-network&order=newest` | JSON | 일 1회 | 없음 | 공공저작물 |
| reginfo Unified Agenda RIN | HTML | `https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202504&RIN=1506-AB41` | HTML | 반기 | 없음 | pubId 를 매 Agenda 마다 갱신 |
| legislation.gov.uk reg 64C (latest) | HTML | `https://www.legislation.gov.uk/uksi/2017/692/regulation/64C` | HTML(+XML `/data.xml`) | 일 1회 | 없음 | OGL v3 |
| e-Gov 法令API 第十条の五 | API | `https://laws.e-gov.go.jp/api/1/articles;lawId=419AC0000000022;article=10%E3%81%AE5` | XML | 주 1회 | 없음 | 利用規約(공개) |
| Justice Laws PCMLTFR s.124.1 | HTML | `https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/section-124.1.html` | HTML | 주 1회 | 없음 | 「current to」 일자 파싱 |
| EBA 준수표(xlsx) | 파일 | `https://www.eba.europa.eu/sites/default/files/2024-10/a0a4c6e5-505f-4c32-b6e8-135e58c35f37/EBA%20GL%202024%2011%20-%20%20Guidelines%20on%20information%20requirements%20in%20relation%20to%20transfers%20of%20funds%20and%20certain%20crypto-assets%20transfers.xlsx` | XLSX | 월 1회 | 없음 | 당국별 준수 선언 변동 감시 |
| VARA Rulebook Part III.G | HTML | `https://rulebooks.vara.ae/node/146` | HTML | 월 1회 | 없음 | 판본 문자열(VER2025…) 파싱 |
| OJK SEOJK 16/2025 페이지 | HTML | `https://ojk.go.id/id/regulasi/Pages/SEOJK-16-SEOJK07-2025-Penerapan-Program-APU-PPT-dan-Pencegahan-Pendanaan-Proliferasi-Senjata-Pemusnah-Massal-Pedagang-AKD.aspx` | HTML | 월 1회 | 없음 | — |
| Crossref works (travel rule) | API | `https://api.crossref.org/works?query=%22travel%20rule%22%20virtual%20asset%20service%20providers%20FATF&filter=from-pub-date:2025-01-01&rows=15` | JSON | 주 1회 | 없음(polite pool 권장) | — |
| FATF 7차 Update 페이지 | HTML | `https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-updated-virtualassets-vasps-2026.html` | HTML | — | 없음 | **미검증(403)** — 브라우저 UA 또는 수동 열람 필요 |
| AUSTRAC 트래블룰 리폼 페이지 | HTML | `https://www.austrac.gov.au/about-us/amlctf-reform/reforms-guidance/other-guidance/travel-rule-reform` | HTML | — | 없음 | **미검증(타임아웃 3회)** |
| KoFIU 제재공시 | HTML | `https://www.kofiu.go.kr/` 하위 | HTML | — | 없음 | **미검증(404)** — 실제 경로 재탐색 |

## 8. 미확인·다음 단계

- [ ] **FATF 1차 문서 재열람(403 해소)**: ① INR.16 2025 판 원문 — 「구조화 데이터」·필드 목록·「three options for alignment checks」 문언 ② INR.15 §7 각주 번호(46 vs 48) ③ 7차 Targeted Update PDF ¶26 전후·부속표(69 관할) ④ 2025-10-28 Annex IV(개정 R.16 평가 방법론) 공표 사실 ⑤ 2025 「Best Practices in Travel Rule Supervision」 존재·일자 ⑥ 6차 Update(2025-06) 기준선 수치. — fatf-gafi.org 를 브라우저로 수동 열람하거나 UA 변경 fetcher 사용.
- [ ] **한국 감독규정 제28조의2 시행일 확정**: 고시 「공포 후 6개월」 기산점(발령일 2026-08-20 vs 관보 게재일) → 법제처 행정규칙 시행일 색인 또는 FIU 질의. 시행령 §10-20(2027-02-19)과의 2일 격차 여부.
- [ ] **감독규정 제2026-3호(2026-10-02) 개정 내용** — 개정이유서 확보(법제처 행정규칙 상세 또는 FIU 공고).
- [ ] **시행령 제10조의5 제6항(수취 VASP 정보 확보 의무)** 문언 — DRF XML 재호출(offset 100000 이후 구간).
- [ ] **KoFIU 제재공시 경로 복구** 후 빗썸(과태료 금액·일자)·코인원·코빗·고팍스 제재문서에서 제5조의3 적시 여부 전수 확인.
- [ ] **EU TFR 조문 직접 재확인**: Art 14(5)·16(2)·21·40 — CELLAR 내용협상(`Accept: application/xhtml+xml`) 경로; EDPB 의 TFR 관련 의견서 존재 여부.
- [ ] **영국**: JMLSG Part II Sector 22 의 비호스팅 지갑 소유 검증 서술; FCA 2024·2025 과징금 목록의 암호자산 건; reg 64C(3)·(4) 영국 외 소재 조건 원문 축조 인용(125자 제한으로 이번에 부분 인용).
- [ ] **미국**: 2020-12-23 비호스팅 지갑 NPRM(FR 2020-28437) 의 Unified Agenda 상태; PPSI NPRM 본문의 1010.410(e)·(f) 적용 문언; FinCEN 2024~2026 집행 색인 전수.
- [ ] **일본**: 개정법 부칙으로 제10조의5 시행일 2023-06-01 확정; FSA 2025-06-25 「対象外ウォレット」 문서 텍스트 추출; 施行規則 제31조의7 원문 축조 문언; JVCEA 2025-10-03 자율규칙 개정 내용.
- [ ] **홍콩**: eLegislation Cap.615 Sch.2 s.13A 조문 원문; AMLO 개정령 시행 부칙(2023-06-01); SFC 집행 뉴스에서 s.13A 인용 건.
- [ ] **호주**: AML/CTF Rules 2025 Part 8 원문(legislation.gov.au 등록 ID) — 금액별 항목 구분·자기수탁 지갑 검증 요건; AUSTRAC 가이던스 페이지.
- [ ] **UAE**: CBUAE 연방 규정(Decree-Law 20/2018·Cabinet Decision 10/2019 전신송금 조항, LFI 가상자산 가이던스)·ADGM FSRA AML Rulebook 의 VA 이전 조항·임계.
- [ ] **캐나다**: s.124.1 발동 기록의무의 정확한 조항·금액(CAD 1,000 설).
- [ ] **인도**: FIU-IND 가이드라인 2023-03 / 2026-01-08 판 PDF 원문.
- [ ] **대만**: 全國法規資料庫에서 辦法 원문(第7條 NT$30,000 문언)·금관회 2026-08-04 보도자료·第7條 시행일 고시 여부.
- [ ] **태국**: SEC 고시 번호(Sor Thor. 9/2026 설)·일자·THB 30,000 문언; AMLO 규정 초안.
- [ ] **인도네시아**: SEOJK 16/2025 본문 조항 번호·자기수탁 지갑 조항.
- [ ] **프로토콜**: TRISA GDS 운영 상태·회원 수; TRP 현행 버전 번호; GTR·TRUST 네트워크 규모 1차 출처; Shyft 공식 중단 공지; VerifyVASP–Chainalysis 합작 구조 현황; Notabene 2024 Series B; IVMS101 2020→2023 변경 목록; AOPP 역사(2021 지갑 반발) 1차 출처; TRM Labs·Chainalysis·Elliptic·Crystal 트래블룰 제품.
- [ ] **데이터 품질 통계**: Sumsub·21 Analytics 공개 통계; Notabene 2026 판 발간 여부; FATF 7차 Update 의 「quality of information」 원문.
- [ ] **개인정보**: 한국 개인정보보호위원회의 국외이전·트래블룰 관련 의결·안내 존재 여부; 일본·싱가포르 데이터보호 당국 입장.
- [ ] **문헌**: F-074 목록의 초록·결론 열람 및 SSRN·BIS·IMF·ECB 조회(별도 문헌 도시에).

## 9. 기존 저장소 내용과의 차이·정정 제안

### 9.1 `notes/3-crypto-aml/travel-rule.md` (2026-08-04)

| 위치 | 현재 서술 | 2026-10-21 기준 판정 | 정정 제안 | 근거 |
|---|---|---|---|---|
| TL;DR·§3 표 「한국 A형 100만원 이상」 | 현행 기준으로만 서술 | **부분 낡음** — 2027-02-19 부터 「모든 경우」 | 행을 둘로 나눠 「~2027-02-18: 100만원 이상(A)」 / 「2027-02-19~: 전건 + 요청 시 추가정보(제3호)」 표기; 상태 enacted-not-in-force | F-011~F-014 |
| §3 표 「영국 B £800 이상」 | 시점 무표기 | **시점 결함** — 2023-09-01~2026-06-29 는 「1,000 euros」 | 「£800 (2026-06-30~; 그 전 1,000 euros, S.I. 2026/621)」 | F-030, F-031 |
| §3 표 「호주 B (Rules 위임)」 | Rules 내용 미확인 | 변동 없음(여전히 미확인) | 「Rules 2025 Part 8 시행 2026-03-31; 금액 구분 미확인」으로 갱신 | F-050 |
| §3 표 전체 | FATF·8관할 | 보조 관할 없음 | §2A 비교표를 이식(UAE·CH·CA·IN·BR·TW·TH·ID 추가; 경계값 문언 포함) | §2A |
| §6 「외부지갑 등록제 — 법령이 명시 요구한 건 아니다」, 「자주 나오는 오해: 외부지갑 등록은 규제 요구사항 아님」 | 거래소 자율 | **2027-02-19 부터 틀림** — 시행령 §10-20 ⑧·감독규정 §28-2④ 가 「독점적 관리 권한 없는 주소」 이전을 동일인에 한정 | 「2027-02-19 부터 고시 의무(본인 지갑만 허용; 고위험 제한). 소유 증명 방법은 미지정」 추가 | F-015, F-018 |
| §7-C 「보존 기간 한국 15년, EU 5년」 | 출처 없음 | 미검증 | 출처 붙이거나 삭제(본 조사 범위 외) | — |
| §9 「2026 후반 가이던스 발표 예정」 | 예정형 | **낡음** — 초안 2026-06-24 공개, 협의 마감 2026-08-21 | 일자·상태(proposed) 갱신; 최종 채택은 미확인 | F-004 |
| §9 「VASP 는 별도 tailored framework」, 「메시징 표준 명확화」 | 근거 미제시 | 1차 미확인 | 확신도 표시 또는 「INR.15 각주 참조 갱신(결과적 개정)」으로 축소 | F-001~F-003 |
| §9 「2030년 말 발효」 | 단일 일자 | CTR:00003 과 동일 결론 — 「이행 기대시한」으로 용어 통일 | 「2030-12-31 이행 기대시한(standard 는 2025-06 채택)」 | F-001 |
| 💼 「Binance 가 한국 미신고… 차단」, 「Crypto.com API 타임아웃 빈번」, 「DAXA 24h 홀드」 | 출처 없음 | 미검증(고유명 서술) | 출처 없으면 삭제 또는 「업계 관행(미검증)」 라벨 | BRIEF §0-2 |
| 💼 「Sunrise 미연결 5~15%」, 「Travel Rule 필요 30~40%」, 「자동 성공 85%」 | 추정치 | 어떤 공개 출처로도 확인 불가 | 삭제 또는 출처 명시; Notabene 2025 설문의 15.4%·19.8% 등 공개 수치로 대체 | F-073 |
| §8 다이어그램 「메시지 15년 보관(양사)」 | — | 미검증 | 위와 동일 | — |

### 9.2 `kb/entities/regulations/*/provisions/*.yaml` 및 REG 노드

| 파일 | 현재 | 판정 | 정정 제안 | 근거 |
|---|---|---|---|---|
| `kr-tfia-sd/provisions/kr-tfia-sd-art10-10.yaml` | threshold 1,000,000 KRW; curator_note 「개정령안 미공포」 | **낡음** | IMPOSES 엣지 분할: ① threshold 1,000,000 / valid_from 2022-03-25 / **valid_to 2027-02-18** ② threshold null / scope_note 「모든 경우; 요청 시 주민등록번호 등 3영업일」 / valid_from **2027-02-19** / 상태 enacted-not-in-force. text_orig 채움(F-013·F-014 문언). review_due 를 2027-02-19 직후로 | F-011~F-014 |
| `kr-tfia-sd.yaml` | citation 대통령령 제35947호 | **낡음** | 제36592호(2026-08-18 공포, 일부개정) 및 제36728호(2026-09-29, 타법개정, 현행) 등재; 「AML 실체 개정 미공포」 서술 삭제 | F-011, F-012 |
| `kr-tfia.yaml` | citation 「제19563호(현행)/제21358호(시행 예정)」 | **낡음** | 「제21358호(공포 2026-02-19·시행 2026-08-20) → 제21857호(공포 2026-08-04·시행 2026-10-02, 타법개정, 현행)」 | F-021 |
| (신설) `kr-tfia-sd/provisions/kr-tfia-sd-art10-20.yaml` | 없음 | 누락 | 제7호(해외 VASP 평가·1천만원 범위 감시체계)·제8호(독점적 관리권한 없는 주소) PROV 신설; DELEGATES_TO → 감독규정 §28-2 | F-015 |
| (신설) `REG:kr-fiu-supervisory-rule` + `PROV:…-art28-2` | FIU고시 제2024-1호가 최신이라 기록 | **낡음** | 고시 제2026-2호(2026-08-20)·제2026-3호(2026-10-02) 등재; §28-2 ①~④ PROV 신설(저위험/동일인/고위험/1천만원/개인지갑 기준), 시행일 「공포 후 6개월」 미확정 표기 | F-016~F-019 |
| `gb-mlr2017/provisions/gb-mlr2017-reg64c.yaml` | scope_note 「£800」; valid_from null; (4)항 조건 미확정 | **연혁 누락** | valid_from 2023-09-01(S.I. 2022/860); 심화 기준 속성을 「1,000 euros (2023-09-01~2026-06-29)」/「£800 (2026-06-30~, S.I. 2026/621 reg 32)」로 분리; (3)·(4) 조건 「every cryptoasset business in the chain carries on business in the UK」 반영; (5)(6)(8)(9) 요지 채움 | F-030~F-032 |
| (신설) `gb-mlr2017/provisions/gb-mlr2017-reg64g.yaml`, `…-reg34a.yaml` | 없음 | 누락 | reg 64G(비호스팅 지갑; £800 2026-06-30~) 및 reg 34A(2027-02-01 시행, enacted-not-in-force) 신설 | F-033, F-034 |
| `gb-mlr2017.yaml` | 「제7A편 신설 개정령(SI 2022/860 으로 추정)」 | 확정 가능 | S.I. 2022/860 확정(주석 F1) + S.I. 2026/621 추가 | F-030, F-031 |
| `us-bsa/provisions/us-bsa-cfr1010-410f.yaml` | 「89 FR 72274 개정 내용 미확인」; 「$250 안 2025-04 철회」 | 보강 가능 | 89 FR 72274 = 투자자문업자 규칙의 (e)(6) 수정(2028-01-01); 철회일 2025-04-16(reginfo) 명시; 재무부 2026-03 보고서 각주 63 을 「가상자산 적용」 근거(IMPOSES 확신도 B→A 검토)로 추가 | F-037, F-038, F-040 |
| `intl-fatf-inr15-p7b.yaml` | 각주 48 | 판본 확인 필요 | OJK 「각주 46 참조 갱신」과 대조 과제 등록; 2026-10-21 403 관측 기록 | F-003, F-009 |
| `intl-fatf-r16.yaml` | 세 일자 분리(CTR:00003) | 유지 | 가이던스 초안 2026-06-24·협의 마감 2026-08-21 을 STATE 로 추가 | F-004 |
| `hk-amlo/provisions/hk-amlo-sch2-s13a.yaml` | valid_from null | 채움 가능(B) | valid_from 2023-06-01 (즉시전송 요건 2024-01-01) — T3 복수 일치; 1차 확인 전 confidence B | F-048 |
| `jp-aptcp.yaml`, `jp-aptcp/provisions/jp-aptcp-art10-5.yaml` | valid_from null(FSA 2차) | 보강 | FSA 2023-05-26 공표자료 URL 을 evidence 로 등재(政令·府令 2023-06-01), 법률 부칙은 과제 유지 | F-043 |
| `sg-psn02/provisions/sg-psn02-para13.yaml` | ¶13.8 미확인 | 해소 | ¶13.8 내용(싱가포르 내 중개기관 완화) 반영; 발효 2024-04-04·개정 2025-07-01 기록 | F-045~F-047 |
| `au-amlctf/provisions/au-amlctf-s66a.yaml` | valid_from null | 보강(B) | Rules 2025 시행 2026-03-31(T3) 기록; Rules Part 8 PROV 신설 과제 | F-050 |
| (신설) 보조 관할 REG/PROV | 없음 | 누락 | VARA Part III.G(A형 AED 3,500 초과), Art.10 GwV-FINMA(C), PCMLTFR s.124.1(C), Res. BCB 520 Art.44(C, 단계 시행), SEOJK 16/2025(B, USD 1,000), 대만 辦法 第7條(enacted-not-in-force), 태국 SEC 고시(enacted-not-in-force) | F-051~F-058 |
| `kb/facts/contradictions.jsonl` CTR:00004 | 「공포 전까지 proposed」 | 상태 전환 | 후속 레코드: 공포 2026-08-18 확정; 시행일 2027-02-19 (언론 02-20 상충 기록); 입법예고안 「1,000만원 일률 STR」→ 「자체 감시체계」 변경 | F-011, F-012, F-020 |
| `_research/wave2/korea-verify.md` §0 #8·#9 | 「2027-01-01」, 「1,000만원 STR 간주」 | 공포본과 상이 | 정정 메모 추가(원 도시에는 보존) | F-011, F-020 |

### 9.3 `notes/4-technology/travel-rule-protocols.md` (2026-04-17)

| 위치 | 현재 | 판정 | 정정 제안 | 근거 |
|---|---|---|---|---|
| §2 「DateAndPlaceOfBirth (선택)」·「EU TFR: 모든 필드 필수」 | — | **부정확** | IVMS 101.2023 C1 「택1 이상」; TFR 제14조(1)(d) 「주소… **or, alternatively**, 생년월일·출생지」 | F-060, F-023 |
| §N.1 `JURISDICTION_RULES` 「US: 2025 개정 제안 $1,000」 | — | **오류** | $1,000 제안은 존재 확인 안 됨; $250 안은 2025-04-16 철회 | F-037 |
| §N.1 「EU: 1 EUR부터 전체 / dateOfBirth·placeOfBirth REQUIRED」 | — | 부정확 | 주소 또는 생년월일·출생지 택일 | F-023 |
| §N.1 「KR: nationalIdentification HASHED」 | 추정 | 미검증 — 2027 판 제3호는 요청 시 **원문** 주민등록번호 제공 | 삭제 또는 출처 | F-013 |
| §N.4 오류 분포 표(35/22/18/12/8%) | 「추정」 | 출처 없음 | 삭제 또는 공개 출처로 대체 | F-073 |
| §M.1 지연·§M.6 SLA 수치 | 추정 | 출처 없음 | 「예시 가정」으로 명시 또는 삭제 | — |
| §3-C 「OpenVASP: Ethereum·ENS·Whisper, 활용도 낮음」 | 2020 이전 설계 | **낡음** | OpenVASP Association = TRP 표준 관리 협회(Zug), TRP 활동 중; Notabene 는 TRP 1.0 지원 | F-067, F-061 |
| §3-H 「GTR: BitGo 등 일부」 | — | **오류** | Infozone Technologies(싱가포르) 운영, 13 회원, Code·Sumsub·Sygna·Fireblocks 지원 | F-065 |
| §3-F·💼 「Notabene 1,500+ VASP」 | — | 낡음 | 2,000+/2,300+ (자사 주장, 2026-10) | F-061 |
| 💼 「Notabene 가격 $5K~$50K+/월」 | — | 출처 없음 | 삭제 | — |
| 전체 | TRUST·Shyft Veriscope·IVMS 101.2023·2026 M&A 부재 | 누락 | 추가(TRUST 폐쇄형 125+; Veriscope 중단; IVMS 101.2023; Ripple→Notabene 투자 2026-07-23) | F-059, F-068, F-071 |
| §9 체크리스트 「메시지 보관 한국 15년, EU 5년」 | — | 미검증 | 출처 | — |

### 9.4 `notes/7-vendors/travel-rule-vendors.md` (2026-04-17)

| 위치 | 현재 | 판정 | 정정 제안 | 근거 |
|---|---|---|---|---|
| §2-A 「Notabene 1,500+ VASP」 | — | 낡음 | 2,000+(자사) | F-061 |
| §2-D 「Sumsub 본사 영국」 | — | 미검증 | 출처 또는 삭제; 프로토콜 5종·2,100+ 추가 | F-062 |
| §2-F 「GTR: BitGo 등 컨소시엄, 일부 미국·중남미」 | — | **오류** | F-065 로 교체 | F-065 |
| §2-G 「TRISA 사용: 일부 LATAM, 신흥시장」 | — | 출처 없음 | Envoy(TRISA+TRP) 사실로 대체; trisa.io 접속 불가 관측 기록 | F-066 |
| §3 벤더 선택 매트릭스·§7 가격·💼 가입 프로세스/협상 팁 | 추천·우열·가격 | **BRIEF §0-1 위반 소지**(우열 평가·가격 추정) | 중립 사실(연동 목록·공개 네트워크 수)로 축소 | — |
| §4 「Chainalysis: VerifyVASP 합작 통해 제공」 | — | 미검증(홈페이지 미기재) | 확신도 표시 | F-063 |
| §8 「IVMS101 v2」 | — | 근거 없음 | 「IVMS 101.2023(현행)」 | F-059 |
| 💼 「Korbit 보수적 운영」 등 거래소별 평가 | — | 우열 평가 | 삭제 | BRIEF §0-1 |
| 전체 | TRUST·Shyft·CryptoSwift·FIXT 등 2025~2026 변동 부재 | 누락 | F-064·F-071 반영 | — |

### 9.5 교차 정정 원칙(이번 조사에서 재확인)

1. **「의무 조문」과 「수치 조문」 분리**는 한국 2027 판에서 한 층 더 복잡해진다 — 정보제공 의무(§10-10, 금액 없음), 추가정보(제3호, **요청**으로 발동), 감시체계(§10-20 ⑦나 + 고시 §28-2③, 1천만원). 세 수치·발동조건을 한 칸에 적으면 전부 틀린다.
2. **시점 축을 KB 에 넣어야 하는 사례가 2건 추가됐다**: 영국 €1,000→£800(2026-06-30), 한국 100만원→전건(2027-02-19). 산문의 단일값 표기는 모두 「~일자」를 달아야 한다.
3. **자기수탁 지갑은 관할별로 전혀 다른 규율**이다 — EU(검증 방법 열거, 1종 이상), 스위스(소유 증명 필수, 방법 미지정), 영국(요청 재량·미수령 시 지급 금지), 한국 2027(동일인만 허용, 방법 미지정), 홍콩(정보 수집·위험평가), 미국(규정 없음), 태국(검증 의무 예정). 비교표에 「자기수탁」 열을 상설할 것.
4. **FATF 수치는 1차 문서 접근이 막힌 상태에서 수집됐다**(403). §4.1 의 B 확신도는 FATF 사이트 복구 후 A 로 올리거나 정정해야 한다.
