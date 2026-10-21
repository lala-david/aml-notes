# 가상자산 감시, 입법에서 집행으로 넘어가다

> 기준일 2026-10-21. 근거는 `research/` 도시에 6편(2026-10-aml-landscape · kyt · fds · travel-rule · fatf-virtual-asset-reports · academic-literature)이다. 본문에는 1차 출처(T1/T2) 또는 원문 확인(confidence A, 일부 B)된 사실만 넣었다. B 등급은 문장 안에 "(B)"로 표시했다. 상태 용어는 proposed / enacted-not-in-force / in-force / withdrawn 네 가지만 쓴다. 특정 회사의 사업 전략은 다루지 않는다.

2026-10-21 기준으로 가상자산 AML의 쟁점은 "법을 만들었는가"에서 "법을 집행하는가"로 넘어갔다. FATF 7차 Targeted Update(2026-07-16)에 따르면 응답 관할의 **83%(91/109)가 트래블룰을 입법했지만, 그중 60%(55/91)는 트래블룰 관련 감독·집행 조치를 한 건도 하지 않았다**. 개정 기준에 따른 R.15 평가에서는 대부분준수(LC) 이상이 149개 관할 중 52개(C 1개 포함)뿐이다. 기술 쪽에서는 FATF가 처음으로 VASP에 "transactions monitoring and blockchain analytics tools"로 급속 이전을 탐지하라고 권고했다. 업계에서 쓰는 "KYT"라는 말은 FATF·MAS·한국 고시 어디에도 나오지 않는다. 한국에서는 "이상거래"라는 한 단어가 법적으로 서로 다른 세 제도를 가리킨다. 전자금융 FDS·보이스피싱 임시조치(2026-10-01부터 가상자산거래소에도 법정 의무), 가상자산이용자보호법 제12조의 불공정거래 상시감시, 특금법의 의심거래보고(STR)가 그것이다. 한국 트래블룰 100만원 기준 폐지는 대통령령 제36592호(공포 2026-08-18)로 **확정됐으나 아직 시행되지 않았다(enacted-not-in-force)**. 법제처 시행일 색인은 2027-02-19를 가리킨다. 미국은 2026-10-05 믹서·비수탁지갑 제안규칙 두 건을 철회했고, 같은 주에 A7 네트워크 같은 특정 네트워크를 차단하는 조치를 냈다. 거래 유형을 규제하던 방식이 네트워크 단위 제재로 바뀐 것이다. 학계는 노드 분류에서 서브그래프·크로스체인·프라이버시 누수 측정으로 옮겨 갔다. 반면 트래블룰이 실제로 어떤 효과를 냈는지 측정한 실증 연구는 2025~2026년에 한 편도 확인되지 않았다.

---

## 1989~2019년: 은행 규칙 30년이 가상자산으로 옮겨 오다

배경부터 짚는다. FATF는 1989년에 설립돼 1990년 40개 권고를 냈고, 비트코인 백서는 2008년에 나왔다. 이 세 사실은 이번 도시에들이 원문으로 검증한 범위 밖이어서 배경으로만 언급한다[^bg]. 원문으로 확인되는 가상자산 대응의 출발점은 FATF의 2014-06 보고서 「Virtual Currencies Key Definitions and Potential AML/CFT Risks」다. 2020년 Red Flag 보고서가 이 문서를 자료원으로 명시한다([FATF Red Flag Indicators PDF](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf)). 그 뒤 2015년 가상통화 가이던스가 나왔고, **2018-10 R.15 개정으로 VA·VASP 정의가 용어집에 신설됐으며, 2019-06 INR.15와 RBA 가이던스 초판이 채택됐다**. 2021 개정 가이던스는 2019년 초판을 "incorporates and supersedes"하고 2015 가이던스도 갱신한다고 밝힌다([FATF 2021 RBA 가이던스](https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf)).

가상자산 트래블룰의 법적 원천은 R.16 본문이 아니다. **2019-06 신설된 INR.15 §7(b)**가 원천이다. 송신 VASP가 "required and accurate originator information and required beneficiary information"을 확보·보유하고 수신 VASP에 "immediately and securely" 제출하라는 문언에는 금액 기준이 없다. USD/EUR 1,000은 바로 앞 §7(a)의 임시거래 CDD 기준이다. 각주는 "It is not necessary for this information to be attached directly to the virtual asset transfers"라고 해 오프체인 메시징의 근거를 놓았다([저장소 KB의 INR.15 §7(b) 원문, 2026-07-30 확인](https://www.fatf-gafi.org/content/fatf-gafi/en/publications/Fatfrecommendations/Fatf-recommendations.html)). 2021 가이던스 para 178은 이를 "Recommendation 16 applies in an amended way to VAs as set out in paragraph 7(b) of INR.15"라고 정리한다([FATF 2021 RBA 가이던스](https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf)).

국가 단위에서 가장 먼저 이를 적용한 사례는 스위스다. FINMA 감독공시 02/2019(2019-08-26)는 Art. 10 GwV-FINMA를 블록체인 지급에 기술중립적으로 적용했다. 그리고 **외부지갑 이전은 자기 고객 소유를 "suitable technical means"로 증명한 경우에만 허용**했다. FINMA는 "Unlike the FATF standards, Article 10 AMLO-FINMA does not provide for any exception for payments involving unregulated wallet providers"라고 밝혀 FATF보다 엄격한 출발점을 택했다([FINMA 02/2019](https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/4dokumentation/finma-aufsichtsmitteilungen/20190826-finma-aufsichtsmitteilung-02-2019.pdf)).

같은 시기에 FDS와 학술 연구는 각자의 계보를 시작했다. 한국 금융감독원은 2014-12-10 「금융권 이상금융거래탐지시스템(FDS) 고도화 1.0」을 발표했다. 여기서 FDS는 "전자금융거래 접속정보·거래내역 등을 분석하여 이상거래를 탐지·차단하는 시스템"으로 정의됐다([금감원 2014-12-10](https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=11361&menuNo=200218)). 처음부터 AML이 아니라 전자금융사고 예방 제도로 출발한 것이다. 학계에서는 Weber 외(2019)가 **Elliptic 데이터셋(거래 노드 203,769개·엣지 234,355개·피처 166개, 불법 라벨 2%)**을 공개했다. 이 논문에서 랜덤포레스트(F1 0.796)는 GCN(F1 0.628)보다 나았고, 시점 43의 다크마켓 폐쇄 이후에는 모든 모델의 성능이 급락했다(본문 수치는 B)([Weber et al. 2019](https://arxiv.org/abs/1908.02591)). 이 데이터셋은 이후 7년간 가상자산 AML 연구의 기본 벤치마크로 쓰였다.

## 2020-09: FATF가 58개 위험징후로 "무엇을 볼지"를 처음 정했다

2020년은 FATF가 기준 이행 점검과 유형론을 처음 묶어 낸 해다. 6월에 12개월 검토가 나왔고, **2020-09-14 「Virtual Assets — Red Flag Indicators of ML/TF」**가 발간됐다. 보고서는 2017~2020년 관할이 제출한 100건 이상의 사례를 바탕으로 6개 범주(거래·거래패턴·익명성·송수신인·자금원/재산원·지리)와 상위 지표 58개(5·8·14·19·8·4), 번호 사례 13건을 담았다([FATF Red Flag 공식 페이지](https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets-red-flag-indicators.html)). 지표 다수는 온체인 구조보다 고객·행위·KYC 쪽 신호다. 송수신인 범주만 19개다. 보고서는 이 지표를 감독 체크리스트로 쓰지 말라고 명시한다("should not be intended for use as a regulatory tool for compliance and examination purposes, or as a checklist", para 20). 지표 하나만으로 의심의 근거가 되지는 않는다는 단서도 붙어 있다(para 8). 그래도 이후 KYT 룰의 원형이 대부분 여기서 나왔다. "입금 후 즉시 개인지갑 출금은 거래소를 사실상 믹서로 만든다(This effectively turns the exchange/VASP into an ML mixer)", "24시간 내 다수 고액", "랜섬웨어형 규칙 간격 송금" 같은 표현이 대표적이다([Red Flag PDF](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf)).

한국은 이 보고서에 사례 제공국으로 등장한다. Case Study 2는 **피싱 피해금 약 4억원이 3종 가상자산으로 바뀐 뒤 국내 VASP 48개 계정을 거쳐 55회 이전되고 해외 지갑으로 빠져나간 사건**이다([Red Flag PDF p.7](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-Assets-Red-Flag-Indicators.pdf)). 같은 해 2020-04-16 공개된 FATF 한국 4차 상호평가 보고서(2020-02 총회 채택)는 R.15를 **"C"(Compliant)**, R.16을 "LC"로 매겼다. 다만 이 등급은 2019-06 가상자산 개정 이전 기준에 따른 것이다([FATF 한국 MER 2020](https://www.fatf-gafi.org/en/publications/Mutualevaluations/Mer-korea-2020.html))[^kr-mer].

미국은 이해에 트래블룰 강화안을 두 건 냈다. 둘 다 시행되지 못했다. 2020-10-27 FinCEN·FRB의 국경 간 임계 $3,000→$250 하향 NPRM(RIN 1506-AB41)은 Spring 2025 통합의제에서 **2025-04-16 withdrawn**으로 정리됐다([reginfo.gov](https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202504&RIN=1506-AB41)). 2020-12-23 비수탁지갑 NPRM(85 FR 83840)은 **2026-10-06 연방관보 철회 공고로 withdrawn**이 확정됐다([Federal Register 2026-20430](https://public-inspection.federalregister.gov/2026-20430.pdf)). 그 결과 2026-10-21 현재 미국 트래블룰은 여전히 31 CFR 1010.410(f)의 "$3,000 or more" 하나다([31 CFR 1010.410](https://www.law.cornell.edu/cfr/text/31/1010.410)).

## 2021-10: RBA 가이던스가 트래블룰의 작동 방식을 단락 단위로 고정했다

**2021-10-28 「Updated Guidance for a Risk-Based Approach to VAs and VASPs」**(PDF 111쪽, 단락 1–357)는 여섯 영역을 손봤다. VA/VASP 정의 확장, 스테이블코인 적용, P2P 위험과 대응 도구, 라이선스·등록, 트래블룰 이행, 감독기관 간 정보공유 원칙이다([FATF 2021 RBA 가이던스](https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf)). 트래블룰에 관해서는 이 문서가 사실상 "운영 매뉴얼" 역할을 했다. 모든 VA 이전은 국경 간 전신송금으로 취급된다(para 179). "즉시"는 이전 이전·동시·병행 전송을 뜻하며 "Post facto submission … should not be permitted"다(para 185, 187). USD/EUR 1,000 de minimis는 국가가 선택할 수 있는 기준이다. 그 미만 이전에도 송수신인 성명과 지갑주소(또는 거래참조번호)는 모아야 한다(para 191–192). 상대 VASP 실사는 3단계로 이뤄진다(para 196–199). sunrise 문제에는 계약·사업관행으로 상대에게 준수를 요구하고, 내부이전 한정이나 확인된 본인(first-party) 이전만 허용하는 식으로 대응할 수 있다(para 200–201). 같은 문서 para 197(a)는 "the FATF is not aware of any technically proven means of identifying the VASP that manages the beneficiary wallet exhaustively, precisely, and accurately … from the VA address alone"라고 인정한다. 주소만으로 상대 VASP를 식별할 수 없다는 이 한계는 이후 모든 트래블룰 프로토콜이 풀어야 할 과제가 됐다.

KYT의 규범적 뼈대도 이 문서에서 나왔다. para 275~276은 지속 모니터링을 고객 프로파일 대비 거래 일관성 검증으로 정의한다. 그리고 "automated systems may be the only realistic method of monitoring transactions, and flagged transactions should go through human/expert analysis"라고 해 자동화와 사람의 검토를 함께 요구한다. 운영 룰의 무결성은 "regular basis"로 검증해야 한다. para 277~278은 고위험 상황에서 모니터링을 "extend beyond the immediate transaction"하라고 요구하는데, 이것이 간접 노출 추적의 근거가 된다. para 273은 블랙리스트 주소와 대조하라고 하고, para 234는 분석도구의 비용·자산 커버리지 한계와 프라이버시 영향을 지적한다([FATF 2021 가이던스 미러](https://www.onpcsb.ro/2022/01042022/Updated-Guidance-VA-VASP.pdf)). DeFi에 대해서는 "A DeFi application (i.e. the software program) is not a VASP"이지만 통제력·영향력을 가진 사람은 VASP가 될 수 있다는 원칙을 세웠다(para 66–69). P2P는 para 40에서 "the FATF has not observed a distinct trend towards increased usage of P2P transactions so far"라고 판단했다. 대신 para 105(c)에서 P2P 시장지표를 모으라고 권고했다. 5년 뒤 7차 TU에서 이 권고를 이행한 관할은 23%에 그친다. FATF 공식 페이지는 2026-10-21 현재 이 가이던스가 "does not reflect … the 2025 revisions to Recommendation 1"이라고 경고한다([FATF 공식 페이지](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html)). 따라서 이 가이던스는 in-force이지만 2025년 이후 기준 개정은 반영하지 않은 상태다.

같은 해 캐나다는 PCMLTFR s.124.1을 통해 가상통화 이전에 요청인·수익자 정보 동반 의무를 2021-06-01 시행했다. 조문에 금액 기준은 없다([Justice Laws Canada](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/section-124.1.html)).

## 2022~2024년: 트래블룰은 관할마다 다른 금액 구조로 시행됐다

이 시기의 핵심은 같은 FATF 문언이 관할마다 서로 다른 금액 구조로 바뀌었다는 점이다. 의무 자체에 금액이 붙어 그 미만이면 대상이 아닌 구조가 있고(A형), 의무는 모든 이전에 적용하되 금액은 정보의 깊이만 가르는 구조가 있으며(B형), 금액이 전혀 없는 구조도 있다(C형). **한국은 2022-03-25 시행령 제10조의10으로 "1백만원 이상"에 의무를 건 A형으로 출발했다**([법제처 DRF 현행 판본](https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20260820&type=XML)). 일본은 2023-06-01 시행 범수법 제10조의5로 금액 조건 없는 C형을 택했다. 10만엔은 시행령의 CDD 기준일 뿐이다([e-Gov 法令API](https://laws.e-gov.go.jp/api/1/articles;lawId=419AC0000000022;article=10%E3%81%AE5); [金融庁 2023-05-26](https://www.fsa.go.jp/news/r4/sonota/20230526/20230526.html)). 홍콩은 같은 날 AMLO 개정·VATP 체제를 시행하며 HK$8,000 이상에서 정보를 늘리는 B형을 택했다. 즉시전송 요건은 2024-01-01까지 유예됐다(B)([Clyde & Co 2023-06-07](https://www.clydeco.com/en/insights/2023/06/hong-kong-virtual-assets-regulatory-update))[^hk]. **영국은 2023-09-01 MLR 2017 Part 7A를 시행했고, 심화정보 기준은 처음에 "1,000 euros"였다**([legislation.gov.uk 64C 2023-09-01 판](https://www.legislation.gov.uk/uksi/2017/692/regulation/64C/2023-09-01)). FCA는 시행 직전인 2023-08-17 성명에서 트래블룰을 아직 시행하지 않은 관할로 보낼 때는 정보를 수집·검증·보관한 뒤 이전할 수 있다고 안내했다([FCA 성명](https://www.fca.org.uk/news/statements/fca-sets-out-expectations-uk-cryptoasset-businesses-complying-travel-rule)). 싱가포르 PSN02 현행 판본은 2024-04-04 효력이 생겼고, S$1,500 초과 시 신원확인·검증을 추가한다([MAS PSN02](https://www.mas.gov.sg/-/media/amld-amendments---30-june-2025/mas-notice-psn02-amendment--new.pdf)). 메시지 표준 쪽에서는 2023-08 「IVMS 101.2023」이 나왔고 interVASP ISWG가 2024-06-04 갱신을 공표했다. 이것이 현행판이며, 흔히 말하는 "IVMS101 v2"는 존재하지 않는다([interVASP](https://intervasp.org/)).

EU는 한 번에 가장 촘촘한 체제를 만들었다. **TFR(2023/1113)과 EBA 트래블룰 가이드라인(EBA/GL/2024/11, 2024-07-04)은 2024-12-30 적용됐다**. EBA는 TFR 전문 30항을 근거로 "all crypto-asset transfers are subject to the same requirements regardless of their amount"라고 해석한다. EUR 1,000은 정보의 깊이가 아니라 자기수탁 주소의 소유·통제를 평가하는 발동 기준이다. 평가 방법은 원격 온보딩 검증, 소액 송금(Satoshi test), 메시지 서명, 기타 기술적 수단 가운데 **최소 1종**이고, 확인된 주소는 화이트리스트에 올릴 수 있다(¶83, ¶86). 기술적 한계를 이유로 한 유예는 2025-07-31 끝났다(¶24)([EBA/GL/2024/11](https://www.eba.europa.eu/sites/default/files/2024-07/6de6e9b9-0ed9-49cd-985d-c0834b5b4356/Travel%20Rule%20Guidelines.pdf)). EU는 sunrise 상대에게 거래를 금지하지 않는다. 대신 "고위험 요소"로 분류하고, 반복해서 정보를 누락하는 기관은 3개월 안에 당국에 보고하게 한다(§4.5, §4.7). AMLR(2024/1624)은 2024-06-19 관보에 실렸다. 제79조의 익명성강화코인 취급 금지를 포함해 **2027-07-10 적용 예정(enacted-not-in-force)**이다([EUR-Lex OJ L 2024/1624](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401624)). EBA는 2024-01-16 ML/TF 위험요소 가이드라인에 CASP를 편입하면서 "transaction monitoring tools and advanced analytics tools"를 요구했다(B)([CMS 요약](https://cms.law/en/bih/legal-updates/new-eba-guidelines-to-manage-aml-risks-as-part-of-the-activities-of-crypto-asset-service-providers)).

감독기관이 KYT를 명시적으로 다룬 첫 문서는 뉴욕주 금융감독청(NYDFS)의 2022-04-28 산업서한이다. 지원하는 자산마다 거래 추적 절차를 두고, 외주 분석도구와 자체 도구를 모두 허용하며, 분석도구가 "may not be able to identify underlying owners"라는 귀속의 한계도 인정했다([NYDFS](https://www.dfs.ny.gov/industry_guidance/industry_letters/il20220428_guidance_use_blockchain_analytics)). 사기 쪽에서는 FinCEN이 2023-09-08 주의보 FIN-2023-Alert005로 pig butchering의 기술 적신호를 제시했다. 예를 들면 "고유 IP·기기 ID·지역이 과거 접속 패턴과 불일치", "ETH를 받은 뒤 수수료가 낮은 TRX로 전환해 급출금" 같은 것으로, 거래소 FDS 룰로 바로 옮길 수 있는 서술이다([FinCEN Alert](https://www.fincen.gov/sites/default/files/shared/FinCEN_Alert_Pig_Butchering_FINAL_508c.pdf)).

한국에서는 이 시기에 "이상거래"의 두 축이 따로 섰다. 하나는 전자금융 FDS다. 금감원·금융보안원이 2023-10-05 「FDS 운영 가이드라인」을 발표했다([금감원 2023-10-05](https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=130709&menuNo=200218)). 그러나 현행 「전자금융감독규정」(고시 제2026-29호) 전문에는 "이상금융거래"나 "FDS"라는 용어가 아예 없다. 전자금융 FDS는 고시 의무가 아니라 가이드라인과 자율배상의 영역이다([전자금융감독규정](https://www.law.go.kr/LSW/admRulInfoR.do?admRulSeq=2100000282622&chrClsCd=010201)). 다른 하나는 **2024-07-19 시행된 「가상자산 이용자 보호 등에 관한 법률」 제12조 "이상거래에 대한 감시"**다. 시행령 제18조는 이상거래를 "불공정거래행위 등의 금지의무를 위반할 우려가 있는 거래 또는 행위"로 정의한다. 따라서 보이스피싱이나 계정탈취는 이 조문의 범위 밖이다. 산출물도 차단이 아니라 금융위·금감원 통보(혐의가 충분하면 수사기관 신고)이고, 위반하면 과태료 1억원 이하가 부과된다(제22조①6·7호)([가상자산이용자보호법](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290735&efYd=20261002&ancYnChk=0&chrClsCd=010202&urlMode=lsInfoR); [시행령](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290171&efYd=20261002&ancYnChk=0&chrClsCd=010202&urlMode=lsInfoR)). 금융위는 2024-07-08 "거래소 적출·심리 → 통보 → 조사 → 가상자산조사심의위원회 → 고발·통보·과징금·경고·주의 5단계" 조사체계를 공표했다([금융위 2024-07-08](https://www.fsc.go.kr/no010101/82625)). 2024-08-22 현장점검에서 확인된 거래소 감시시스템은 가격상승률·거래량증가율 같은 변수가 임계값을 넘으면 적출하는 **룰 기반 자체 개발 시스템**이었다([금융위·금감원 2024-08-22](https://fsc.go.kr/po010101/82943)).

이 시기 학계는 데이터셋을 키웠다. **Elliptic++(2023, KDD)**는 지갑 주소 822k+·시간 상호작용 1.27M을 더했다([arXiv 2306.06108](https://arxiv.org/abs/2306.06108)). **Elliptic2(2024)**는 라벨 서브그래프 122K·노드 클러스터 49M·엣지 196M으로 자금세탁을 서브그래프 분류 문제로 다시 정의했다([arXiv 2404.19109](https://arxiv.org/abs/2404.19109)). Elliptic2의 GLASS 모델은 F1 0.933이지만 PR-AUC는 0.208이다(본문 수치는 B). 극단적 불균형 데이터에서 F1만 보면 성능을 오독한다는 점이 이후 벤치마크 회의론의 출발점이 됐다.

## 2025년: 기준은 다시 쓰이고, 제재 대상은 "유형"에서 "네트워크"로 옮겨 갔다

**FATF는 2025-06 총회에서 R.16("Payment transparency")을 개정했다.** 설명서는 "FATF has agreed not to bring VASPs directly into the scope of R.16 but to apply the updated requirements indirectly through R.15"라고 밝힌다(para 54). de minimis는 "no higher than USD/EUR 1,000"으로 유지했고(para 33), 이행시한은 **2030년 말**이다("The FATF will expect that most, or all of the new requirements are in effect by that date", para 59)([R.16 개정 설명서](https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Explanatory%20note%20for%20revised%20R.16.pdf.coredownload.pdf)). 따라서 개정 R.16은 기준으로는 채택됐지만 VASP에 대한 실체적 변경은 R.15를 거쳐 간접적으로만 들어온다. 2025-06-26 6차 Targeted Update는 **DPRK의 Bybit USD 14.6억 탈취(회수율 3.8%)**를 헤드라인으로 올렸다. 「Best Practices on Travel Rule Supervision」도 함께 발간됐다(존재만 확인)([6차 TU](https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2025-Targeted-Upate-VA-VASPs.pdf.coredownload.pdf)).

미국에서는 정책 방향이 크게 바뀌었다. 재무부는 **2025-03-21 Tornado Cash를 SDN에서 삭제했다**(엔티티 1개·ETH 주소 90개)([OFAC 2025-03-21](https://ofac.treasury.gov/recent-actions/20250321)). 그러나 형사 쪽은 별도로 진행됐다. 2025-08-06 배심은 Roman Storm에게 무면허 송금업 공모 유죄를 평결했고, 자금세탁·IEEPA 위반 공모 혐의는 배심 불일치로 끝났다(B)([Willkie 2025-08-08](https://complianceconcourse.willkie.com/articles/tornado-cash-cofounder-convicted-for-conspiring-to-operate-an-unlicensed-money-transmitting-business/)). **GENIUS Act는 2025-07-18 서명됐다**([재무부 2026-03 의회보고서](https://home.treasury.gov/system/files/246/GENIUS-Act-Illicit-Finance-Innovation-Congressional-Report-March-2026.pdf)). 집행의 무게중심은 특정 조직으로 옮겨 갔다. 2025-10-14 OFAC는 캄보디아 Prince Group을 초국가범죄조직으로 지정했고(146개 대상), FinCEN은 같은 날 Huione Group을 미국 금융시스템에서 끊는 §311 최종규칙을 발동했다([재무부 sb0278](https://home.treasury.gov/news/press-releases/sb0278)). 2025-12-09 FinCEN은 Paxful에 $3.5M 민사벌금을 부과했다. 사유는 MSB 미등록·AML 프로그램 미비·SAR 미제출이었고 트래블룰 위반은 없었다([FinCEN](https://www.fincen.gov/news/news-releases/fincen-assesses-35-million-penalty-against-paxful-facilitating-suspicious)).

2024-01-01~2026-10-21 사이에 **트래블룰 위반을 독립 제재 사유로 명시한 사건은 어느 관할에서도 확인되지 않았다**. 가장 가까운 사례는 2025-10-22 캐나다 FINTRAC이 Xeltox(Cryptomus)에 부과한 C$176,960,190 행정벌이다. 여기서도 "Travel rule"은 컴플라이언스 정책 결함 목록의 한 항목으로만 등장한다([FINTRAC](https://fintrac-canafe.canada.ca/pen/amps/pen-2025-10-22-eng)). 한국의 대형 제재도 마찬가지다. FIU는 2025-11-06 두나무에 과태료 352억원을 결정했는데, 사유는 고객확인·거래제한·의심거래보고 등의 위반이었고 트래블룰(특금법 제5조의3)은 포함되지 않았다([FIU 보도자료 KDI 미러](https://eiec.kdi.re.kr/policy/materialView.do?num=273166)).

한국은 2025년에 세 갈래 "이상거래" 제도를 모두 손봤다. 시장감시 쪽에서는 2025-09-03 가상자산이용자보호법 첫 과징금이 나왔다. 테더마켓 자전거래로 비트코인 가격을 올려 다른 코인의 원화환산가를 왜곡한 사건이다([금융위 2025-09-03](https://www.fsc.go.kr/po010101/85233)). FDS 쪽에서는 2025-05 출금지연제도가 도입됐고, 금감원은 2025-05-29 책임분담기준 개선안에서 "FDS 고도화 등 사고 예방노력"을 금융회사 책임 판단에 반영했다. 은행권의 2024-01~2025-04 배상은 41건·1억6,891만원으로 피해금액의 약 18%였다([금감원 2025-05-29](https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=194420&menuNo=200218)). 2025-10-29에는 금융보안원 ASAP가 출범했다. 약 130개 금융회사가 9개 유형·90개 항목을 실시간 공유하는데, 가상자산거래소는 참여기관으로 명시되지 않았다([금융위 2025-10-29](https://www.fsc.go.kr/no010101/85526)). AML 쪽에서는 FIU 고시 제2025-2호 「자금세탁방지 업무규정」이 2025-10-22 발령돼 2026-01-22 시행됐다. 제76~81조가 "거래모니터링체계"를 규정하는데, 본문에 "가상자산"이라는 단어는 한 번도 나오지 않는다([법제처 DRF](https://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=2100000267264&type=XML)). 한국 KYT의 법적 근거가 가상자산 전용 조문이 아니라 금융권 공통 규정이라는 뜻이다.

다른 관할도 움직였다. 싱가포르는 PSN02를 2025-06-30 개정해 2025-07-01 시행했다. ¶6.27은 FATF 기준 감독을 받지 않는 상대와 DPT를 이전할 때 강화조치를 요구한다([MAS PSN02](https://www.mas.gov.sg/-/media/amld-amendments---30-june-2025/mas-notice-psn02-amendment--new.pdf)). 인도네시아는 2025-07-03 SEOJK 16/2025로 USD 1,000 이상/미만 2단 정보 구조를 도입했다([OJK](https://ojk.go.id/id/regulasi/Pages/SEOJK-16-SEOJK07-2025-Penerapan-Program-APU-PPT-dan-Pencegahan-Pendanaan-Proliferasi-Senjata-Pemusnah-Massal-Pedagang-AKD.aspx)). 브라질 Res. BCB 520(2025-11-10)은 금액 조건 없는 정보 전달 의무를 2026-02-02 발효하고 2028-02-02 전면 의무화하는 단계 일정을 정했다([Res. BCB 520 미러](https://www.migalhas.com.br/arquivos/2025/11/23462FAD2E8205_Resolucao520.pdf)). 사기 피해 환급 제도는 관할마다 모델이 달랐다. 호주 Scams Prevention Framework Act 2025(2025-02-20 재가)는 장관이 섹터를 지정하는 방식이고 가상자산은 법문에 없다([Federal Register of Legislation](https://www.legislation.gov.au/C2025A00015/asmade/2025-02-20/text/original/pdf)). 싱가포르 SRF(2024-12-16)는 금융회사에 실시간 사기감시 의무를 지웠다([MAS](https://www.mas.gov.sg/news/media-releases/2024/mas-and-imda-announce-implementation-of-shared-responsibility-framework-from-16-december-2024)). 영국 PSR 의무환급(2024-10-07)은 FPS·CHAPS 계좌 간 송금만 대상으로 한다(B)([PSR](https://www.psr.org.uk/our-work/app-scams/)).

2025년 학계는 측정 규모와 문제 정의를 함께 바꿨다. **Address poisoning 연구(USENIX Security '25)는 Ethereum·BSC 2년간 공격 시도 2.7억 건, 피해 대상 1,700만 명, 사고 6,633건, 최소 8,380만 달러 손실을 측정했다**([arXiv 2501.16681](https://arxiv.org/abs/2501.16681)). 후속 연구에서는 인기 지갑 53종 중 3종만 피싱 주소로 송금할 때 경고를 띄웠다([arXiv 2508.12107](https://arxiv.org/abs/2508.12107)). 크로스체인 추적은 휴리스틱에서 자동 매칭으로 넘어갔다. 12개 브리지 양방향 F1 91.75%(ABCTracer), 5개 브리지 약 50만 건 F1 0.9746(ConneX)이 보고됐다. 다만 브리지 집합이 달라 두 수치를 직접 비교할 수는 없다([arXiv 2504.01822](https://arxiv.org/abs/2504.01822); [arXiv 2511.01393](https://arxiv.org/abs/2511.01393)). 제재의 효과도 정량화됐다. Tornado Cash 제재 후 957일 동안 입금액은 71.03% 줄었지만, Ethereum 보안사고의 78.33%는 여전히 Tornado Cash를 거쳤다(WWW '26)([arXiv 2507.11721](https://arxiv.org/abs/2507.11721)). 트래블룰 연구는 이해에 처음으로 동료심사 문헌이 나왔다. 하지만 PET 평가(토큰화·MPC·동형암호·ZKP·TEE·SSI; "중앙집중형 → 연합형·암호학적 검증 모델로 이동")와 양자내성 TRISA(Kyber·Dilithium 이행 경로) 같은 설계 연구에 머물렀다([Shevchuk 외 2025](https://research.aston.ac.uk/en/publications/technologie-wspieraj%C4%85ce-prywatno%C5%9B%C4%87-dla-regu%C5%82y-podr%C3%B3%C5%BCy-fatf-w-kryp/); [TRISA PQ](https://research.aston.ac.uk/en/publications/post-quantum-security-enhancements-for-the-trisa-framework-a-tech/)). rug pull 분야에서는 35개 유형을 정리하고 13개 탐지 도구의 커버리지가 25.7~62.9%에 그친다는 SoK가 나왔다(ISSTA 2025)([researchr](https://conf.researchr.org/details/issta-2025/issta-2025-papers/25/SoK-A-Taxonomic-Analysis-of-DeFi-Rug-Pulls-Types-Dataset-and-Tool-Assessment)).

## 2026-01~10-21: 입법 83%, 집행 공백 60% — 7차 TU가 드러낸 간극

### 상반기: 권한 이전, 연례 범죄 통계, FATF 타겟보고서

2026-01-01 EU의 AML/CFT 규칙제정·가이던스 권한이 EBA에서 AMLA로 넘어갔다. 기존 EBA 가이드라인은 AMLA가 대체할 때까지 유효하다([EBA](https://www.eba.europa.eu/regulation-and-policy/anti-money-laundering-and-countering-financing-terrorism)). 연례 범죄 통계는 두 분석업체가 1월에 냈다. 두 수치는 정의가 달라 나란히 읽어야 한다. **Chainalysis(2026-01-08)는 2025년 불법 주소 수취액을 "최소 1,540억 달러"로 추정했다**. 2024년 수치는 409억에서 572억 달러로 올려 잡았고, 불법 비중은 알려진 서비스 유입 대비 1% 미만, 스테이블코인 비중은 84%다(B)([Chainalysis](https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/)). **TRM(2026-01-28)은 1,580억 달러로 추정했다**. 2024년은 645억 달러였고, 비중은 전체 온체인 거래량의 1.2%, VASP 유동성 대비 2.7%다(B)([TRM](https://www.trmlabs.com/reports-and-whitepapers/2026-crypto-crime-report)). 두 회사 모두 하한(floor) 추정이고 계속 상향 수정한다고 밝힌다. 분모가 각각 "서비스 유입"과 "온체인 거래량"으로 다르므로 비중을 비교하면 안 된다[^crime]. 미국 FBI IC3의 2025 연례보고서는 신고 기반 통계로, 가상자산 관련 피해 113.66억 달러(+22%), 가상자산 투자사기 72.28억 달러, 60세 이상 피해 44.32억 달러를 기록했다([FBI IC3 2025](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf)).

FATF는 6차 TU가 약속한 타겟보고서 세 편을 모두 냈다. 2026-03-03 스테이블코인·비수탁지갑 보고서는 스테이블코인 250종 이상·시총 3,000억 달러 초과를 보고하며 발행자의 동결·소각·회수와 환매 시 CDD를 모범사례로 들었다. 동시에 "FATF Standards do not require jurisdictions to adopt regulatory frameworks for stablecoin arrangements beyond those already applicable to VASPs"라고 선을 그었다([FATF 2026-03-03](https://www.fatf-gafi.org/en/publications/Virtualassets/targeted-report-stablecoins-unhosted-wallets.html)). 2026-03-11 역외 VASP 보고서는 활동기반 접근을 채택한 관할이 46%라고 밝혔다([FATF 2026-03-11](https://www.fatf-gafi.org/en/publications/Virtualassets/Understanding-Mitigating-Risks-Offshore-VASPs.html)). 2026-07-21 DeFi 보고서는 2021 가이던스의 DeFi 분석을 "updates and complements"하면서 통제 존재를 기능적으로 판정하라고 권고했다([FATF 2026-07-21](https://www.fatf-gafi.org/en/publications/Virtualassets/targeted-report-decentralised-finance-2026.html)). 미국에서는 FinCEN·OFAC가 2026-04-10 GENIUS 법상 허가 결제스테이블코인 발행자(PPSI)를 BSA 금융기관으로 편입하는 AML/CFT·제재 NPRM을, 2026-06-22 CIP NPRM을 공고했다(둘 다 proposed)([Federal Register API](https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=%221010.410%22&conditions%5Bagencies%5D%5B%5D=financial-crimes-enforcement-network&order=newest&per_page=20)). 재무부의 2026-03 의회보고서는 DASP에 "$3,000 or more"의 트래블룰이 적용된다고 다시 확인했다([재무부 보고서](https://home.treasury.gov/system/files/246/GENIUS-Act-Illicit-Finance-Innovation-Congressional-Report-March-2026.pdf)).

한국은 2026년 상반기에 FDS를 법으로 끌어올렸다. **법률 제21503호(2026-03-31 공포)로 「통신사기피해환급법」상 "금융회사등"에 가상자산거래소가 포함됐다. 법 이름도 "피해자산 환급"으로 바뀌었고, 2026-10-01 시행됐다**. 제2조의5는 금융회사등이 "자체점검을 상시적으로 실시"해 피해의심거래계좌등으로 추정되면 이체·출금 또는 **가상자산 이전**을 지연·일시정지하도록 의무화한다([법제처 통신사기피해환급법](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290245&efYd=20261002&ancYnChk=0&chrClsCd=010202&urlMode=lsInfoR); [금융위 2026-03-13](https://www.fsc.go.kr/no010101/86446)). 한국 전자금융 FDS의 실질적 법정 근거는 전자금융감독규정이 아니라 이 법이다. 금융위는 의심정보 공유 근거를 담은 법률 제21320호(2026-02-03 공포, 2026-08-04 시행)의 입법 배경으로 개별 FDS가 "자체 패턴분석에 의존해 사전 차단 효과가 제한적"이라는 점을 들었다([금융위 2026-01-15](https://www.fsc.go.kr/no010101/86063)). 2026-08-04 금융보안원이 법정 정보공유분석기관으로 지정됐다([금융위 2026-08-04](https://www.fsc.go.kr/no010101/87474)). 2026-04-07 「강화된 출금지연제도」 표준 내규도 시행됐다. 근거가 된 집계는 2025-06~09 거래소 사기이용계좌 2,526개 중 1,490개(59%)가 출금지연 예외계좌였고 피해금의 75.5%가 예외계좌에서 빠져나갔다는 것이다(B)([금융위 2026-04](https://www.fsc.go.kr/po010102/86656)).

AML 쪽 한국 일정은 다음과 같다. FIU는 2026-02-05 업무계획에 "체이널리시스(가상자산 분석도구) 도입", 심사분석 AI 도입, 트래블룰을 100만원 미만 거래와 수신거래소로 확대하는 방안을 넣었다([금융위 2026-02-05](https://fsc.go.kr/no010101/86209)). 2026-02-19 특금법 개정 법률 제21358호가 공포됐다. 2026-03-30 시행령·감독규정 개정안 입법예고에는 해외 VASP·개인지갑 대상 1,000만원 이상 거래를 "위험도와 관계없이 의심거래로 보아 FIU에 보고"하는 안이 들어 있었다([금융위 2026-03-30](https://www.fsc.go.kr/no010101/86589)). 이 안은 최종본에서 바뀌었다(아래)[^1000].

### 7차 TU(2026-07-16): FATF가 처음으로 블록체인 분석을 VASP 권고에 넣었다

**FATF 7차 Targeted Update는 2026-07-16 발간됐다(PDF 34쪽).** 설문은 2026-02~06에 했고 147개 관할(FATF 38 + FSRB 109)이 응답했다. 응답하지 않은 58/205개 관할은 진전이 없는 것으로 추정 처리됐다([7차 TU PDF](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf)). 2026-04 기준 R.15 평가 149개 관할의 등급은 **C 1 · LC 51(34%) · PC 64(43%) · NC 33(22%)**이다. 2025년(138개)의 LC 29%·PC 50%보다 나아졌지만 모집단이 늘었으므로 백분율만 비교하면 안 된다. **트래블룰 입법은 83%(91/109)로 2025년 73%(85/117)보다 올랐다. 그러나 입법 관할의 60%(55/91)는 트래블룰 관련 지적·지시·집행·감독조치가 전혀 없었다(2025년 59%)**. 같은 보고서 요약문은 이 수치를 "almost half"로 표현해 본문과 어긋난다[^half]. 라이선스를 요구하는 관할은 73%(95/130)이지만 실제로 인가·등록을 내준 관할은 58%(76/130)로 2025년 65%보다 비율이 떨어졌다. 역외 VASP에도 인가를 요구하는 관할은 34%(39/114)다. 금지 접근은 2023년 11%에서 23%(33/144)로 늘었다. P2P를 고위험으로 평가한 관할은 88%(58/66)인데 시장지표를 모으는 관할은 23%(31/133)뿐이다. DeFi 위험평가를 마친 관할은 18%(26/142), 자국 내 VASP 해당 DeFi를 식별하지 못한 관할은 93%, 실제로 인가한 관할은 2개, 집행한 관할은 1개다([7차 TU PDF](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf)).

7차 TU가 다룬 위험의 축도 바뀌었다. 6차의 헤드라인이 Bybit였다면, 7차는 **캄보디아 소재 금융 복합체가 2021-08~2025-01 최소 USD 40억을 세탁한 사건(그중 최소 USD 3,700만이 DPRK 탈취자금)**을 들었다(para 29–30). 제3자 발행자가 USD 2,900만 이상을 동결하자 이 조직이 "immune to asset freezing"을 내세운 자체 스테이블코인을 발행했다는 사례도 실렸다. FATF는 여기서 VASP가 "issuer-level asset freeze/burn mechanisms"를 준수 안전장치로 믿을 수 없을 수도 있다고 결론 내렸다(para 35). AI도 위험요인으로 등장했다. 딥페이크 면접을 이용한 채용사기로 USD 100만 이상이 탈취됐고, AI 코딩 도구·에이전트가 스마트컨트랙트 익스플로잇을 만들 수 있다는 것이다(para 34). DPRK가 RPC 노드·멀티시그 공급자 같은 제3자 인프라를 공격한다는 점도 지적됐다(para 33). 민간에 대한 권고에는 KYT 언어가 처음 등장한다. VASP는 "identify suspicious patterns … and detect rapid transfer of VAs using transactions monitoring and blockchain analytics tools"해야 한다(권고 6-ii). 통제 요소로는 "KYC, wallet screening, blacklisting, and, where appropriate, whitelisting mechanisms as well as freezing and blocking capabilities"가 열거됐다(권고 5-ii). 소매 사용자로 위장한 역외 VASP 계정 탐지와 브리지·믹서·크로스체인 노출 평가도 요구됐다(권고 6-iii·iv). 한국은 Annex A 표에서 위험평가·입법·검사·집행·트래블룰은 모두 "Yes"였고, **스테이블코인 발행자 등록·인가 요구는 "No", R.15 등급은 "N/A"(개정 기준 미평가)**였다.

이 시기 FATF의 다른 일정도 정리해 둔다. 2026-06-17~19 총회에서 보스니아헤르체고비나·이라크가 회색명단에 들어가고 알제리·나미비아가 빠졌다([FATF 2026-06 총회 결과](https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-june-2026.html)). 그 결과 현행 회색명단은 22개 관할이다(B). 2026-06-24 개정 R.16 이행 가이던스 초안 공개의견수렴이 시작돼 2026-08-21 마감됐는데, 최종본은 2026-10-21 현재 발간 흔적이 없다(proposed, B)([FIAU Malta 요약](https://fiaumalta.org/news/latest-updates-from-the-fatf/)).

### 하반기: 한국 시행령 공포, 영국 금액 치환, 미국 철회

**한국: 2026-08-11 국무회의 의결 → 2026-08-18 대통령령 제36592호 공포 → 2026-08-20 본칙 시행.** 부칙 제1조 단서는 "제10조의2, 제10조의5제6항, 제10조의10, 제10조의20 및 제16조의2제1호ㆍ제4호의 개정규정은 공포 후 6개월이 경과한 날부터 시행한다"고 정한다([법제처 DRF 시행예정 판본](https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20270219&type=XML)). 법제처 시행일 색인의 시행예정 판본은 **2027-02-19**를 표시한다. 그래서 2026-10-21 현재 효력 있는 제10조의10 제1호는 여전히 "1백만원 이상"이다[^krdate]. 2027-02-19부터 이 조항은 "다른 가상자산사업자에게 가상자산을 이전하는 모든 경우"로 바뀐다. 성명·주소는 이전과 동시에 제공해야 하고, 주민등록번호 등은 요청을 받은 날부터 3영업일 이내에 제공해야 한다. 제10조의20 제7·8호와 FIU 고시 제2026-2호(2026-08-20) 제28조의2는 해외 VASP를 세 등급으로 나눈다. 저위험은 허용, 그 외는 고객과 상대방이 동일인일 때만 허용, FATF 고위험국 소재나 무인허가는 제한이다. "독점적인 관리 권한을 가지지 않은 가상자산주소"(자기수탁 지갑)와의 이전은 동일인일 때만 허용된다. **입법예고안의 "1,000만원 이상 일률 STR"은 최종본에서 "1천만원 이상 자체 의심거래 감시체계 구축·운영"으로 바뀌었다**(고시 §28-2③)([감독규정 FIU 고시 제2026-2호](https://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=2100000285986&type=XML); [금융위 2026-08-11](https://www.fsc.go.kr/no010101/87499)). 고시의 "공포 후 6개월" 기산점에 따라 제28조의2 시행일은 시행령과 이틀 차이가 날 수 있어 확정되지 않았다[^sup]. 특금법 법률 제21358호의 신고제·퇴직자 제재통보 부분은 2026-08-20 시행됐고(in-force), 법률 제21857호(2026-08-04 공포, 타법개정)가 2026-10-02부터 현행본이다([금융위 2026-08-11](https://www.fsc.go.kr/no010101/87499); [법제처 DRF 법령 검색](https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=law&type=JSON&query=특정금융거래정보의보고및이용등에관한법률)). 2026-08-13 전면 개정된 신고매뉴얼은 AML 인력 4인 이상, 전산설비 국내 소재(클라우드 국내 리전 인정), 대주주 변경 "30일 전 사전신고"를 정했다([금융위 2026-08-13](https://www.fsc.go.kr/no010101/87521)). 2026-10-01 상반기 실태조사에서는 **총 출고 62.8조원 가운데 트래블룰이 적용된 것은 9.5조원(약 15%)**이었다([금융위 2026-10-01](https://www.fsc.go.kr/no010101/87835)). 100만원 기준과 국내 VASP 간 이전으로 한정된 현행 제도가 실제로 얼마나 덮는지를 보여 주는 수치이고, 2027년 이후 비교할 기준선이 된다. 시장감시 쪽에서는 금융위가 2026-07-20 법 시행 2년 성과로 조사 완료 40여 건, 고발·통보 30여 건, 평균 부당이득 14억원, 과징금 2건(부당이득의 125~165%)을 공표했다([금융위 2026-07-20](https://fsc.go.kr/po010106/87357)). 2026-09-23에는 API 초단기 시세조종과 90% 이상 가장매매 등 4건을 고발·통보했다([금융위 2026-09-23](https://www.fsc.go.kr/no010101/87783)). 2026-10-13 FIU는 미신고 사업자 사이트 27건 접속차단을 공표했다(수사기관 통보 누적 44개)([금융위 2026-10-13](https://www.fsc.go.kr/no010101/87916)).

**영국은 S.I. 2026/621(2026-06-30 시행)로 reg 64C(4)와 64G(1)(b)의 "1,000 euros"를 "£800"으로 바꿨다**. 같은 개정령이 신설한 암호자산 코레스 관계 강화 CDD(reg 34A)는 **2027-02-01 시행 예정(enacted-not-in-force)**이다([legislation.gov.uk S.I. 2026/621](https://www.legislation.gov.uk/uksi/2026/621/made)). 비호스팅 지갑에 대해서는 소유 증명 의무를 두지 않는다. 사업자가 고객에게 정보를 요청할 수 있고, 받지 못하면 "must not make the cryptoasset available to the beneficiary"하는 구조다([reg 64G](https://www.legislation.gov.uk/uksi/2017/692/regulation/64G)). FCA의 2026 과징금 목록(2026-09-30까지 17건)에 Part 7A 위반 건은 없다([FCA 2026 fines](https://www.fca.org.uk/news/news-stories/2026-fines)). FSMA 가상자산 인가 신청기간은 2026-09-30~2027-02-28이고, 신체계는 2027-10-25 시행 예정이다([FCA](https://www.fca.org.uk/firms/cryptoassets-information)).

**미국은 2026-10-05 FinCEN이 CVC 믹싱 §311 NPRM(88 FR 72701)과 비수탁지갑 NPRM(85 FR 83840)을 철회했다(관보 2026-10-06, withdrawn)**. 사유는 "chilling effect on legitimate activity"와 "deregulatory agenda"였다([Federal Register 2026-20429](https://public-inspection.federalregister.gov/2026-20429.pdf); [FinCEN](https://www.fincen.gov/news/news-releases/fincen-announces-withdrawals-proposed-digital-asset-related-rules))[^rin]. 같은 날 관보에는 러시아 연계 A7 네트워크의 역외 하위대리인과의 자금이체를 금지하는 특별조치 NPRM(RIN 1506-AB77, proposed)이 실렸다. 근거는 §311이 아니라 Combating Russian Money Laundering Act §9714다([Federal Register 2026-20371](https://public-inspection.federalregister.gov/2026-20371.pdf)). OFAC는 2026-08-24 시작한 "Operation Economic Outcast"의 일환으로 2026-09-17 이란 거래소 BitBank 등을 E.O. 13902로 지정했다([OFAC 2026-09-17](https://ofac.treasury.gov/recent-actions/20260917); [재무부 sb0632](https://home.treasury.gov/news/press-releases/sb0632/)). 2026-10-01에는 A7 네트워크를 초국가범죄조직으로 지정했다(B, FinCEN NPRM 각주 인용). 믹서라는 "유형"을 규제하던 계획은 접고, 특정 "네트워크"를 차단하는 수단을 강화한 셈이다. GENIUS §3 NPRM(RIN 1505-AC95)은 2026-08-18 관보에 실렸고 의견은 2026-10-19 마감됐다([Federal Register 2026-16796](https://public-inspection.federalregister.gov/2026-16796.pdf)). GENIUS 법은 최종규칙이 늦어져 법정 최종기한인 **2027-01-18 시행이 예상된다**(B)([Jones Day](https://www.jonesday.com/en/insights/2026/08/us-treasury-proposes-genius-act-rules-for-stablecoin-issuance-offer-and-sale)).

EU·아시아의 하반기 움직임은 다음과 같다. 2026-10-01 AMLA가 AMLR 첫 RTS 3건(CDD Art. 28(1), 거래관계 기준 Art. 19(9), 그룹 요건 Art. 16(4)/17(3))의 최종안을 집행위에 제출했다(아직 채택 전)([AMLA](https://www.amla.europa.eu/press-release-amla-finalises-key-standards-private-sector_en)). 2026-10-07에는 MiCA 재검토와 관련해 스테이킹·대출, DeFi 통제자 정의, 무인가 스테이블코인 등 AML 우선과제 5개를 제출했다([AMLA](https://www.amla.europa.eu/amla-identifies-amlcft-priorities-review-mica_en)). ESMA 임시 CASP 등록부(2026-10-19)는 379행·고유 LEI 376개다([ESMA CASPS.csv](https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv)). 일본은 암호자산을 금상법으로 옮기는 개정법이 2026-07-15 성립했지만 시행일은 정해지지 않았다(enacted-not-in-force)([金融庁](https://www.fsa.go.jp/common/diet/index.html)). 홍콩 VATP 인가는 13개(2026-10-16), 스테이블코인 발행 인가는 2개(2026-04-10)다([SFC](https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/Virtual-assets/Virtual-asset-trading-platforms-operators/Lists-of-virtual-asset-trading-platforms); [HKMA](https://www.hkma.gov.hk/eng/regulatory-resources/registers/register-of-licensed-stablecoin-issuers/)). 싱가포르 MAS는 2026-09-01~10-16 PSA 개정 스테이블코인 체계 의견수렴을 했다(proposed, B)([Allen & Gledhill](https://www.allenandgledhill.com/sg/perspectives/articles/33474/sgkh-mas-consults-on-amendments-to-payment-services-act-2019-to-implement-stablecoin-regulatory-framework)). 인도 FIU-IND는 2026-09-09 역외 VDA 사업자 15곳에 PMLA 위반을 통지했다([News on AIR](https://newsonair.gov.in/fiu-ind-cracks-down-on-15-vda-service-providers-over-pmla-non-compliance/)). 대만은 2026-08-04 트래블룰 2단계 시행 계획을, 태국은 2026-09-02 최종안(준수기한 2027-02-27, 자기수탁 지갑 소유·통제 검증 의무)을 발표했다(둘 다 B)([Notabene Taiwan](https://notabene.id/world/taiwan); [Sumsub Thailand](https://sumsub.com/media/news/thailand-introduces-new-crypto-travel-rule-compliance-requirements/)).

### 2026년 학술·정책 문헌: 측정은 정교해졌지만 실증은 비어 있다

2026년 학계는 "깨졌다/안전하다"라는 이분법 대신 수치로 측정하는 쪽으로 갔다. Railgun 측정에서는 **출금의 17.65%가 입금과 하나로 연결됐고 중위 익명성 손실은 3.42비트**였다([arXiv 2606.25926](https://arxiv.org/abs/2606.25926)). Railgun·Hinkal의 unshield 186,356건 분석에서는 공개 토큰 제약만으로 평균 익명성 집합이 40.1~59.0% 줄었다([arXiv 2608.22987](https://arxiv.org/abs/2608.22987)). 스테이블코인 동결의 한계도 정량화됐다. **USDT 제재 주소의 7.3%, USDC의 18.7%가 동결 발효 전에 전액 인출됐다**("Sanction-Evasion MEV")([arXiv 2603.27739](https://arxiv.org/abs/2603.27739)). FATF 7차 TU가 말한 "issuer-level freeze 의존 불가"를 학계가 수치로 뒷받침한 것이다. 벤치마크 회의론도 본격적인 연구 주제가 됐다. TransXion(KDD '26)은 템플릿 기반 이상 주입 벤치마크가 모델의 강건성을 과대평가한다고 보였다([arXiv 2604.17420](https://arxiv.org/abs/2604.17420)). Elliptic 시계열 분할에서는 Extra Trees(AUPRC 0.570)가 GraphSAGE(0.311)를 크게 앞섰다(B)([Akter 외 2026](https://publications.eai.eu/index.php/airo/article/download/13658/4313/36724)). LLM 분야에서는 근거 인용을 강제한 알람 트리아지 연구가 **인용 유효성 0.98, 에스컬레이션 F1 0.62**를 보고했다. 근거를 잘 인용한다고 판단이 맞는 것은 아니라는 뜻이다. 이 연구를 포함해 LLM 평가는 전부 합성 데이터로 이뤄졌다([arXiv 2604.19755](https://arxiv.org/abs/2604.19755)). 실배포 사례로는 자기지도 피싱 탐지기 PhishEye가 미지의 피싱 주소 1,803개를 찾았다([arXiv 2605.01207](https://arxiv.org/abs/2605.01207)). CtPhishCapture(NDSS 2026)는 자격증명 탈취형 피싱 사이트 5,138개·앱 10,612개 가운데 83%·79%가 커뮤니티에 보고되지 않은 신규였다([NDSS 2026](https://www.ndss-symposium.org/wp-content/uploads/2026-f2854-paper.pdf)). 정책 기관도 같은 방향을 가리켰다. BIS 연차경제보고서(2026-06-23)는 "stablecoins account for a significant share of illicit on-chain activity"라며 발행자 동결과 분석업체 지원이 "cannot replace routine, large-scale AML/CFT controls"라고 했다([BIS AER 2026](https://www.bis.org/publ/arpdf/ar2026e3.htm)). ECB OP 382(2026-03-23)는 MiCAR를 자연실험으로 삼는 분석 설계를 소개했다([ECB OP 382](https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op382.en.pdf)). 그러나 **트래블룰·VASP 등록이 거래량·불법 비중·sunrise 지연에 미친 인과 효과를 추정한 2025~2026 동료심사 논문은 확인되지 않았다**. 자기수탁 지갑 소유 검증 방식(서명·소액송금)을 학술적으로 평가한 논문도 없다.

## 2026-10-22 이후: 이미 날짜가 정해진 일정들

가장 가까운 일정은 FATF 일정표상 **2026-10-26~30 파리 총회(영국 의장국 첫 총회)**다([FATF 일정표](https://www.fatf-gafi.org/en/calendars/events.html))[^plen]. 회색명단 갱신과 R.16 가이던스 최종본 여부가 여기서 확인된다. 2026-10-30에는 브라질 Res. BCB 520 Art. 91의 무허가 상대방 거래 금지가 발효된다. 2026-12-14는 EU PSD3의 유럽의회 본회의 지표 일정이다(proposed, B)([EP OEIL 2023/0209](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0209%28COD%29)). 7차 TU는 국가위험평가 가이던스의 VA/VASP 부속서가 "later in 2026" 나온다고 예고했다. 2027년 1분기에는 일정이 몰려 있다. GENIUS 예상 시행(2027-01-18, B), 영국 reg 34A(2027-02-01), **한국 트래블룰 기준금액 폐지와 해외 VASP·자기수탁 지갑 차등 규율(2027-02-19)**, 태국 준수기한(2027-02-27, B), 영국 FSMA 인가 신청 마감(2027-02-28)이다. 2027-07-10 EU AMLR이 적용되고 익명성강화코인 취급 금지가 함께 시작된다. 2027-10-25 영국 가상자산 신체계가 시행된다. 2028-01-01 미국 투자자문업자 AML 규칙의 준수기한이 온다([31 CFR 1010.410 LII 주석](https://www.law.cornell.edu/cfr/text/31/1010.410)). 2028-02-02 브라질 트래블룰이 전면 의무화되고, 2028-07-18 GENIUS의 DASP 비허가 스테이블코인 취급 금지가 시작된다(B). 마지막으로 2030-12-31이 개정 R.16 이행 기대시한이다.

---

## 연대기 표

| 일자 | 사건 | 관할 | 영역 | 상태(2026-10-21) |
|---|---|---|---|---|
| 2014-06 | FATF 「Virtual Currencies Key Definitions」 | INTL | AML | 발간 |
| 2014-12-10 | 금감원 「FDS 고도화 1.0」 | KR | FDS | 계보상 선행 |
| 2018-10 | R.15 개정 — VA·VASP 정의 | INTL | AML | in-force |
| 2019-06 | INR.15 §7(b) 채택(가상자산 트래블룰) + RBA 가이던스 초판 | INTL | 트래블룰 | in-force(초판은 2021판으로 대체) |
| 2019-07-31 | Weber 외 Elliptic 데이터셋 공개 | 학술 | KYT | — |
| 2019-08-26 | FINMA 02/2019(외부지갑 소유 증명) | CH | 트래블룰 | in-force |
| 2020-04-16 | FATF 한국 4차 MER 공개(R.15 "C", 개정 전 기준) | KR | AML | 발간 |
| 2020-09-14 | **FATF Red Flag Indicators** | INTL | KYT·AML | in-force(현행 유일판) |
| 2020-10-27 | 미국 $3,000→$250 NPRM | US | 트래블룰 | **withdrawn**(2025-04-16) |
| 2020-12-23 | 미국 비수탁지갑 NPRM | US | 트래블룰 | **withdrawn**(관보 2026-10-06) |
| 2021-06-01 | 캐나다 PCMLTFR s.124.1 | CA | 트래블룰 | in-force |
| 2021-10-28 | **FATF 개정 RBA 가이던스** | INTL | AML·KYT·트래블룰 | in-force(2025 R.1 개정 미반영) |
| 2022-03-25 | 한국 트래블룰(100만원 이상) | KR | 트래블룰 | in-force → 2027-02-18까지 |
| 2022-04-28 | NYDFS 블록체인 분석 가이던스 | US-NY | KYT | in-force |
| 2023-06-01 | 일본 범수법 §10-5 / 홍콩 AMLO·VATP(B) | JP·HK | 트래블룰 | in-force |
| 2023-08 | IVMS 101.2023 | INTL | 트래블룰 | 현행 표준 |
| 2023-09-01 | 영국 MLR Part 7A(€1,000) | GB | 트래블룰 | in-force(2026-06-30 £800로 개정) |
| 2023-09-08 | FinCEN pig butchering 주의보 | US | FDS | in-force |
| 2023-10-05 | 금감원·금보원 FDS 운영 가이드라인 | KR | FDS | in-force(자율) |
| 2024-04-04 | 싱가포르 PSN02 현행 판본 효력 | SG | 트래블룰 | in-force |
| 2024-06-19 | EU AMLR 관보 게재 | EU | AML | enacted-not-in-force(2027-07-10) |
| 2024-07-04 | EBA/GL/2024/11 | EU | 트래블룰 | in-force(2024-12-30 적용) |
| 2024-07-19 | **한국 가상자산이용자보호법 시행(§12 이상거래 감시)** | KR | 시장감시 | in-force |
| 2024-12-30 | EU TFR·MiCA 적용 | EU | 트래블룰·AML | in-force |
| 2025-03-21 | Tornado Cash SDN 삭제 | US | KYT·제재 | 해제 완료 |
| 2025-06(총회) | **R.16 개정(VASP는 R.15 경유, 2030년 말)** | INTL | 트래블룰 | 기준 채택, 이행 진행 |
| 2025-06-26 | FATF 6차 TU | INTL | AML | 발간 |
| 2025-07-18 | GENIUS Act 서명 | US | AML | enacted-not-in-force |
| 2025-09-03 | 가상자산이용자보호법 첫 과징금 | KR | 시장감시 | 확정 |
| 2025-10-14 | Prince Group TCO 지정·Huione §311 최종규칙 | US | 제재 | in-force |
| 2025-10-22 | 한국 AML 업무규정(FIU 고시 2025-2호) 발령 | KR | KYT | in-force(2026-01-22) |
| 2025-10-29 | 금융보안원 ASAP 출범 | KR | FDS | 운영 중 |
| 2025-11-06 | 두나무 과태료 352억원 결정(트래블룰 사유 아님) | KR | AML | 결정 |
| 2026-01-01 | EU AML 권한 EBA→AMLA | EU | AML | in-force |
| 2026-03-31 | 통신사기피해환급법 제21503호 공포(거래소 편입) | KR | FDS | in-force(2026-10-01) |
| 2026-06-30 | 영국 S.I. 2026/621(£800) | GB | 트래블룰 | in-force |
| 2026-07-16 | **FATF 7차 TU** | INTL | AML·KYT·트래블룰 | 발간 |
| 2026-08-18 | 대통령령 제36592호 공포 | KR | 트래블룰 | 본칙 in-force / 제10조의10·20 enacted-not-in-force |
| 2026-08-20 | 특금법 제21358호 시행·감독규정 제2026-2호 | KR | AML | in-force(§28-2 등 유예) |
| 2026-10-01 | 거래소 보이스피싱 임시조치 의무 시행 / AMLA RTS 제출 | KR·EU | FDS·AML | in-force / 집행위 제출(채택 전) |
| 2026-10-05~06 | **FinCEN 믹싱·비수탁지갑 NPRM 철회**, A7 특별조치 NPRM | US | KYT·제재 | withdrawn / proposed |
| 2026-10-26~30 | FATF 총회 | INTL | AML | 예정 |
| 2027-01-18 | GENIUS 법정 최종 시행기한(예상, B) | US | AML | enacted-not-in-force |
| 2027-02-01 | 영국 reg 34A | GB | 트래블룰 | enacted-not-in-force |
| **2027-02-19** | **한국 100만원 기준 폐지·해외 VASP/자기수탁 차등** | KR | 트래블룰 | enacted-not-in-force |
| 2027-07-10 | EU AMLR 적용(익명성강화코인 금지 포함) | EU | AML·KYT | enacted-not-in-force |
| 2027-10-25 | 영국 FSMA 가상자산 신체계 | GB | AML | enacted-not-in-force |
| 2028-02-02 | 브라질 트래블룰 전면 의무화 | BR | 트래블룰 | in-force(단계) |
| 2030-12-31 | 개정 R.16 이행 기대시한 | INTL | 트래블룰 | — |

---

## 2026-10-21 현재 단면

### 관할별 AML 규제는 대부분 "다음 단계가 이미 법에 들어가 있는" 상태다

| 관할 | 현행 핵심 근거(in-force) | 확정됐으나 미시행 | 제안 단계(proposed) / 철회 |
|---|---|---|---|
| FATF | R.15/INR.15, 2021 RBA 가이던스 | 개정 R.16(이행시한 2030-12-31) | R.16 이행 가이던스 초안(의견수렴 종료, 최종본 미발간) |
| 한국 | 특금법(법률 제21857호), 시행령 본칙, 감독규정 제2026-3호, 가상자산이용자보호법 §12, 통신사기피해환급법(거래소 2026-10-01~) | 시행령 제10조의10·제10조의20, 감독규정 §28-2(2027-02 중) | — |
| EU | MiCA, TFR, EBA/GL/2024/11 | AMLR(2027-07-10) | AMLA RTS 3건(집행위 제출), MiCA 재검토, PSD3/PSR |
| 영국 | MLR 2017 Part 7A(£800, 2026-06-30~) | reg 34A(2027-02-01), FSMA 신체계(2027-10-25) | — |
| 미국 | BSA 31 CFR 1010.410(f) $3,000 | GENIUS Act(예상 2027-01-18, B) | GENIUS 하위 NPRM 다수, A7 특별조치 / **철회**: 믹싱 §311·비수탁지갑(2026-10-06), $250 안(2025-04-16) |
| 일본 | 범수법 §10-5 | 금상법 이관 개정법(2026-07-15 성립, 시행일 미정) | — |
| 싱가포르 | PSN02(2025-07-01 개정분) | — | PSA 스테이블코인 개정(B) |
| 홍콩 | AMLO Sch.2 s.13A, VATP 13개, 스테이블코인 발행 인가 2개 | — | — |
| UAE(두바이) | VARA Rulebook III.G(AED 3,500 초과) | — | — |
| 브라질 | Res. BCB 520(단계 시행) | 전면 의무(2028-02-02) | — |

### KYT·FDS·시장감시는 같은 "이상" 신호를 서로 다른 법적 산출물로 보낸다

| 구분 | ① FDS / 보이스피싱 임시조치 | ② 시장감시(가상자산이용자보호법 §12) | ③ AML·KYT → STR |
|---|---|---|---|
| 한국 법적 근거 | 통신사기피해환급법 §2의5·§2의6·§4(거래소 2026-10-01~), 전자금융거래법 §21 + 금감원 가이드라인(자율) | 법 §12, 시행령 §18, 가상자산시장조사업무규정 §3·§4 | 특금법 §4, AML 업무규정 제76~81조, 시행령 §10-20 ⑦나(2027-02-19~) |
| 목적 | 이용자 자산 보호(계정탈취·보이스피싱) | 시세조종·미공개정보 이용 적발 | 자금세탁·테러자금 차단 |
| 1차 데이터 | 접속·기기·세션, 입출금 패턴, ASAP 공유정보 | 호가·체결 원장, 계정 집중도 | 온체인 주소·노출도, KYC 프로필 |
| 산출물 | 지연·일시정지·지급정지·환급 | 금융위·금감원 통보(혐의 충분 시 수사기관 신고), 거래유의·거래중지 | STR, 거래거절, EDD |
| 위반 시 | 지급정지 미이행 손해배상(§4③) | 과태료 1억원 이하(§22①6·7) | 특금법 과태료·영업정지 |
| 국제 기준의 언어 | SRF "real-time fraud surveillance", FinCEN 적신호 | — | FATF "transactions monitoring and blockchain analytics tools"(7차 TU), "ongoing monitoring"(2021 para 275) — **"KYT"는 0회** |

KYT에 대해 확정적으로 말할 수 있는 것은 많지 않다. 원문으로 확인되는 것은 규범(FATF 2021 para 273–278, 7차 TU 권고 5·6, NYDFS 2022, MAS PSN02 ¶6.27, 한국 업무규정 제76~81조)뿐이다. 벤더가 공개한 커버리지·노출도 산정 방식·지연 시간은 모두 자사 주장(T5)이라 이 보고서에서는 뺐다. 거래모니터링의 알람→SAR 전환율에 대한 공개 벤치마크도 은행권 자료(EY 2018, 리테일 평균 14%)만 있다. **가상자산 전용 alert-to-STR 벤치마크는 존재하지 않는다**(B)([EY 2018](https://ey.com/content/dam/ey-unified-site/ey-com/en-uk/industries/financial-services/documents/ey-anti-money-laundering-transaction-monitoring-2018-emeia-survey.pdf)).

### 트래블룰 관할 비교 — 금액 조문과 의무 조문은 따로 읽어야 한다

유형: **A** 의무 자체에 금액(미만이면 대상 아님) · **B** 의무는 전건, 금액은 정보 깊이만 · **C** 금액 없음.

| 관할 | 의무 조문 | 유형 | 금액(경계 문언) | 자기수탁 지갑 | 시행 | 상태 |
|---|---|---|---|---|---|---|
| FATF | INR.15 §7(b) | C | 없음(USD/EUR 1,000 de minimis는 선택) | 위험기반(2021 para 203–204, 295–297) | 2019-06 | in-force(soft law) |
| 한국(현행) | 특금법 §5-3, 시행령 §10-10 ①호 | A | KRW 1,000,000 이상 | 법령 미규율 | 2022-03-25 | in-force(~2027-02-18) |
| 한국(2027) | 시행령 §10-10·§10-20, 감독규정 §28-2 | 전건 + 요청 시 추가정보 | 정보제공 없음 / 1천만원 이상은 감시체계 | **동일인 간에만 허용**, 현저한 고위험은 제한 | 2027-02-19 | enacted-not-in-force |
| EU | TFR Art 14·16 | B′ | 정보는 전건 동일 / EUR 1,000 "amounts to or exceeds"면 자기수탁 검증 | 검증 방법 1종 이상, 화이트리스트 | 2024-12-30 | in-force |
| 영국 | MLR reg 64C | B | £800 "equals or exceeds"(2026-06-30~; 이전 €1,000) | 정보 요청 재량, 미수령 시 지급 금지 | 2023-09-01 | in-force |
| 미국 | 31 CFR 1010.410(f) | A | USD 3,000 "or more" | 명시 규정 없음 | — | in-force |
| 일본 | 범수법 §10-5 | C | 없음 | 1차 문언 미확보 | 2023-06-01 | in-force |
| 싱가포르 | PSN02 ¶13 | B | S$1,500 "exceeds"면 신원 검증 추가 | 전용 조항 없음 | 2024-04-04 | in-force |
| 홍콩 | AMLO Sch.2 s.13A | B | HK$8,000 "not less than" | 정보 수집·위험평가(B) | 2023-06-01(B) | in-force |
| 호주 | AML/CTF Act s 66A | C(법률) | 법률상 없음, Rules 금액 미확인 | s 66A(2)(d) 실사 분류 | 시행일 상충[^au] | in-force |
| UAE(VARA) | Rulebook III.G ¶2 | A | AED 3,500 "exceeding" | 위험 고려 의무 | 2025-05-19 판 | in-force |
| 스위스 | Art. 10 GwV-FINMA | C | 없음 | 고객 소유 기술적 증명 시만 허용 | 2019-08-26 | in-force |
| 캐나다 | PCMLTFR s.124.1 | C | 조문상 없음 | 언급 없음 | 2021-06-01 | in-force |
| 브라질 | Res. BCB 520 Art. 44 | C | 없음 | 위험 고지 의무(Art. 59 §2) | 2026-02-02(전면 2028-02-02) | in-force(단계) |
| 인도네시아 | SEOJK 16/2025 | B | USD 1,000 "atau lebih" | FAQ에 명시 없음 | 2025-07-03 | in-force |
| 대만 | VASP AML 辦法 第7條 | B(B) | NT$30,000 초과(B) | 미규정 | 별도 지정일 | enacted-not-in-force |
| 태국 | SEC 고시(2026-09-02) | 미확인 | 미확인 | 소유·통제 검증 의무 | 2027-02-27(B) | enacted-not-in-force |

같은 "자기수탁 지갑"이라도 관할마다 규율이 전혀 다르다. EU는 검증 방법을 열거하고, 스위스는 증명을 필수로 하되 방법을 정하지 않는다. 영국은 정보 요청과 지급 보류 구조이고, 한국(2027)은 동일인 요건만 두고 방법은 정하지 않는다. 미국은 규정이 없다. 한국은 2027-02-19부터 한 행에 세 가지 수치·발동 조건(정보제공 전건, 추가정보는 요청 시, 1천만원은 감시체계)이 겹친다. 이를 한 칸에 적으면 틀린다.

### FATF 3개 문서가 말하는 것

| 문서 | 성격·분량 | 핵심 메시지 | 2026-10-21 현재 읽는 법 |
|---|---|---|---|
| **Red Flag Indicators (2020-09-14)** | 비구속 유형론, PDF 24쪽, 6범주·상위 지표 58개·사례 13건(+무번호 1건), 2017~2020 사례 100+ | "무엇이 의심스러운가"의 목록. 송수신인(19)·익명성(14) 범주가 가장 크고, 지표 하나만으로는 의심 근거가 아니며, 감독 체크리스트로 쓰면 안 된다. 한국 사례(4억원·48계정·55회) 수록 | 현행 유일판. 2021년 이후 유형(브리지·DeFi 유동성·드레이너·동결저항 스테이블코인)은 없다. 7차 TU와 2026 타겟보고서로 보완해야 한다 |
| **RBA 가이던스 (2021-10-28)** | 가이던스, PDF 111쪽, 단락 1–357 + 정보공유 원칙 20개, 2019판 대체 | 트래블룰 운영 규칙(국경 간 취급, 즉시·사후 금지, de minimis 선택, 상대 VASP 3단계 실사, sunrise 대응, 주소만으로 VASP 식별 불가 인정), 지속 모니터링(자동화 + 인간 분석, 룰 무결성 정기 검증, 즉시 거래 너머 추적), DeFi 통제자 원칙 | in-force. 다만 FATF가 스스로 2025 R.1 개정이 반영되지 않았다고 고지한다. R.16 부분은 2025 개정 설명서와, DeFi는 2026-07-21 보고서와 함께 읽어야 한다 |
| **7차 Targeted Update (2026-07-16)** | 이행 점검 보고서, PDF 34쪽, 147개 관할 응답 | 입법은 늘었지만(트래블룰 83%) 집행은 비어 있다(60%가 조치 없음). R.15 LC 34%. 실제 인가 비율은 하락(58%). DeFi 인가 2개·집행 1개. 처음으로 "blockchain analytics tools"로 급속 이전 탐지를 권고. 발행자 동결에 기댈 수 없다고 경고. AI·제3자 인프라 공격 | 차기 판은 2027년. 요약문의 "almost half"가 아니라 본문 para 25의 60%(55/91)를 인용해야 한다 |

### 2025~2026 논문 동향 — 다섯 가지 이동과 세 가지 공백

| 흐름 | 대표 근거(초록 직접 확인) | 의미 |
|---|---|---|
| 노드 분류 → 서브그래프·경로·의도 추적 | Elliptic2(2024), AMLGuard(2026, 82건 사건 목적지 정밀도 94.4%) | 탐지 단위가 "거래 하나"에서 "자금 흐름 전체"로 바뀜 |
| 크로스체인 자동 매칭 | ABCTracer F1 91.75%(12 브리지), ConneX 0.9746(5 브리지) | 정의가 달라 수치 비교 불가. 공통 벤치마크 부재 |
| 프라이버시 프로토콜의 정량 측정 | Railgun 17.65%·3.42비트, 익명성 집합 40.1~59.0% 축소 | "추적 불가/가능" 이분법 폐기 |
| 사기 측정 규모 확대 | address poisoning 2.7억 건(USENIX '25), 지갑 53종 중 3종만 경고 | FDS 쪽 공백(지갑 단 경고 부재)을 수치로 확인 |
| 벤치마크 회의론 | TransXion(KDD '26), 트리 앙상블 > GNN(Akter 2026, B), Elliptic2 F1 0.933 vs PR-AUC 0.208 | 그래프 모델의 실무 우위는 공개 근거로 확인되지 않음 |
| **공백 1** 트래블룰 효과 실증 | 2025~2026 동료심사 논문 없음 | 7차 TU의 관할별 시행일을 패널 데이터로 쓸 수 있는 시점 |
| **공백 2** LLM 실데이터 평가 | 전부 합성 데이터(인용 유효성 0.98 vs F1 0.62) | 감독 질의 대응 시 "그럴듯한 근거"의 위험 |
| **공백 3** 자기수탁 소유 검증 | 학술 평가 논문 없음(벤더 문서만) | 서명은 "통제"를 증명할 뿐 "수익적 소유"는 증명하지 못함 |

---

## 결론

이번 정리로 분명해진 것은, 2026년의 병목이 기준이 없어서가 아니라 기준이 겹쳐 있어서 생긴다는 점이다. FATF는 R.16을 개정했지만 VASP에는 R.15를 거쳐 간접 적용한다. 한국은 2027-02-19 하루에 정보제공 전건화, 요청 기반 추가정보, 1천만원 감시체계, 해외 VASP 3등급, 자기수탁 동일인 요건을 한꺼번에 시작한다. 같은 "이상거래" 신호가 FDS·시장감시·STR이라는 세 개의 법적 출구로 갈라진다는 점까지 겹치면, 실무에서 가장 위험한 것은 탐지 실패보다 분류 실패다. 탐지한 신호를 틀린 출구로 보내는 오류다. 반대로 집행 쪽은 비어 있다. 트래블룰 위반만으로 제재된 사례는 어느 관할에도 없고, 입법 관할의 60%는 감독 조치가 전혀 없다. 따라서 "트래블룰 미준수 리스크"는 2026-10-21 현재 제재 리스크라기보다 상대방 실사와 거래 허용 여부의 문제다. 한국 2027 규율이 sunrise 대응을 처음으로 허용 요건으로 법령화했다는 점이 이를 보여 준다.

앞으로 두 가지를 지켜봐야 한다. 첫째, 발행자 동결은 7차 TU의 경고, BIS의 평가, 동결 전 인출 7.3%/18.7%라는 학계 측정이 같은 방향을 가리킨다. 그런데 미국은 믹서 유형 규제를 철회하고 네트워크 단위 차단으로 갔다. 이 조합은 거래소 측 거래모니터링과 상대방 위험평가의 몫을 줄이는 것이 아니라 늘린다. 둘째, 2027년 1분기 한국·영국·태국·미국의 시행이 겹치므로 트래블룰 효과를 실증할 자연실험 조건이 처음으로 갖춰진다. 2026-10-21 현재 그 실증 연구는 비어 있고, 한국의 "총 출고 대비 트래블룰 적용 15%"는 그 비교의 첫 기준선으로 쓸 수 있다.

---

## 부록 A. 저장소 정정 필요 사항

> 각 도시에의 §9(정정 제안)를 합치고, 도시에 사이의 상충은 T1 원문 쪽으로 정리했다. 이 보고서는 해당 파일들을 수정하지 않았다.

| # | 파일 경로 | 현재 서술 → 정정 | 근거 |
|---|---|---|---|
| A-1 | `notes/2-regulations/korea-fiu-act.md` §3·FAQ, `notes/3-crypto-aml/travel-rule.md` TL;DR·§3 | "100만원 임계 유지" → "~2027-02-18 100만원 이상(A형) / 2027-02-19~ 전건 + 요청 시 추가정보(3영업일), 1천만원 이상 자체 감시체계" 두 행으로 분리, 상태 enacted-not-in-force | 대통령령 제36592호 부칙, 법제처 eflaw 20270219 |
| A-2 | `kb/entities/regulations/kr-tfia-sd/provisions/kr-tfia-sd-art10-10.yaml` | threshold 단일값 → IMPOSES 엣지 분할(valid_to 2027-02-18 / valid_from 2027-02-19, threshold null), "개정령안 미공포" 삭제 | 동상 |
| A-3 | `kb/entities/regulations/kr-tfia-sd.yaml` | citation 대통령령 제35947호 → 제36592호(2026-08-18) 및 제36728호(2026-09-29, 현행) | 법제처 DRF |
| A-4 | `kb/entities/regulations/kr-tfia.yaml` | "제19563호(현행)/제21358호(시행 예정)" → "제21358호(2026-02-19 공포·2026-08-20 시행) → 제21857호(2026-08-04 공포·2026-10-02 시행, 현행)" | 법제처 DRF, 금융위 2026-08-11 |
| A-5 | (신설) `kr-tfia-sd/provisions/kr-tfia-sd-art10-20.yaml`, `REG:kr-fiu-supervisory-rule` + §28-2 PROV | 누락 → 해외 VASP 3등급·자기수탁 동일인·1천만원 감시체계, 고시 제2026-2호·제2026-3호 등재, §28-2 시행일 "미확정" 표기 | FIU 고시 제2026-2호 |
| A-6 | `kb/facts/contradictions.jsonl` CTR:00004 | "공포 전까지 proposed" → 공포 2026-08-18, 시행 2027-02-19(언론 02-20 상충 기록), 입법예고 "1,000만원 일률 STR" → 최종 "자체 감시체계" | 동상, 금융위 2026-03-30 |
| A-7 | `_research/wave2/korea-verify.md` §0 #8·#9 | "2027-01-01", "1,000만원 STR 간주" → 공포본 기준 정정 메모 추가(원문 보존) | 동상 |
| A-8 | `research/2026-10-kyt.md` BLUF·엔티티·F-031·F-032·§9 #6(c) | "트래블룰 기준금액 폐지 2027-01-01", "§28-2③ 1천만원 위험도 무관 STR(2027-08-20)", "공포 미확인" → 2026-08-18 공포, 2027-02-19 시행, "1천만원 이상 자체 의심거래 감시체계"(STR 자동의무 아님). §9 #6(c)의 "자동 STR" 추가 제안은 폐기 | travel-rule F-011~F-020 |
| A-9 | `research/2026-10-aml-landscape.md` F-029·F-032·F-033·타임라인 | "공포일 미확인", "~2027-02(추정 불가)" → 공포 2026-08-18, 시행 2027-02-19 | 동상 |
| A-10 | `research/2026-10-travel-rule.md` §1·F-001~F-006 | FATF 수치 T4/B, "R.16 1차 문언 미확인" → 7차 TU 공식 PDF(T1/A)·R.16 개정 설명서 para 33·54·59로 확인 완료 | fatf-reports F-030·F-031·F-040~F-049 |
| A-11 | `research/2026-10-kyt.md` F-001 | "FIAU 미러, 발간일 미확인" → 2026-07-16(FATF 공식 페이지·PDF 메타) | fatf-reports F-040 |
| A-12 | `notes/2-regulations/fatf.md` §6 | "4차 ME에서 가상자산 영역 PC" → "2020 MER R.15 'C'(개정 전 기준), 7차 TU 개정 기준 'N/A'" | FATF 한국 MER 페이지, 7차 TU Annex A |
| A-13 | `notes/2-regulations/fatf.md` §4 | "임계값 €1~$3,000 재량", "분기별 FIU 보고", "Protocol Interop 의무", "PII 보관기간" → 삭제. "de minimis no higher than USD/EUR 1,000, VASP는 R.15 경유, 2030년 말" | R.16 설명서 para 33·54·59 |
| A-14 | `notes/2-regulations/fatf.md` TL;DR·§2 | "2019년 R.16 개정(VA 확장)" → "2019-06 INR.15 §7(b) 신설" | 2021 가이던스 para 178 |
| A-15 | `notes/2-regulations/fatf.md` TL;DR·§5·§8·§9, `notes/3-crypto-aml/travel-rule.md` §9 | "2026 후반 가이던스 발표 예정", "TU 최근 2025" → "R.16 가이던스 초안 의견수렴 2026-06-24~08-21, 최종본 미발간", "7차 TU 2026-07-16"; Red Flag 2020·스테이블코인(03-03)·oVASP(03-11)·DeFi(07-21) 보고서 추가 | 7차 TU, FIAU |
| A-16 | `notes/2-regulations/fatf.md` §7 | 회색명단 예시 "케냐, 나미비아, 필리핀" → 나미비아 2026-06-19 해제, 필리핀 현행 명단 없음, "2026-06-19 기준 22개" | FATF 2026-06 총회 결과 |
| A-17 | `notes/2-regulations/fatf.md` §9 | "AMLA 2028년부터 EU 40개 고위험 VASP 직접감독" → "6개 이상 회원국 영업 금융기관(그룹) 약 40개, VASP 전용 아님, CASP 포함 여부 미공개"(wave1 근거, B) | aml-landscape §9 #5 |
| A-18 | `_research/wave1/fatf-intl-standards.md` F-013·F-035 | "35 PDF쪽, 인쇄 p.1~33" → "34쪽, 인쇄 pp.1–31"; "147개 관할 응답(38+109), 무응답 58/205" 추가 | 7차 TU PDF |
| A-19 | `notes/2-regulations/us-bsa-fincen.md` TL;DR·§5 | "시행규정 2026-07-18 마감" → "2026-07-18은 법정 규칙제정 기한(경과); PPSI NPRM 의견 마감 2026-06-09; 법 시행 예상 2027-01-18; §3 NPRM 2026-08-18" | Federal Register, Jones Day(B) |
| A-20 | `notes/2-regulations/us-bsa-fincen.md` §2·§3, `kb/entities/regulations/us-bsa.yaml` curator_note | 믹싱 §311 "proposed" / 비수탁지갑 "관보 공고 없음" → 둘 다 **withdrawn**(관보 2026-10-06; 믹싱 철회 공고의 RIN 표기 1506-AB47 병기); OFAC 2026 축(Operation Economic Outcast, BitBank 2026-09-17, A7) 추가 | FR 2026-20429·20430·20371 |
| A-21 | `kb/entities/regulations/us-bsa/provisions/us-bsa-cfr1010-410f.yaml` | "89 FR 72274 개정 내용 미확인" → 투자자문업자 규칙의 (e)(6) 제외목록 수정, 2028-01-01 연기, 가상자산 트래블룰 무관; $250 안 철회일 2025-04-16; 재무부 2026-03 보고서 각주 63을 적용 근거로 추가 | LII, reginfo, 재무부 보고서 |
| A-22 | `kb/entities/regulations/gb-mlr2017/provisions/gb-mlr2017-reg64c.yaml`, `gb-mlr2017.yaml`, `notes/3-crypto-aml/travel-rule.md` §3 | "£800" 단일값 → "1,000 euros(2023-09-01~2026-06-29) / £800(2026-06-30~, S.I. 2026/621 reg 32)"; valid_from 2023-09-01; S.I. 2022/860 확정; reg 64G·reg 34A(2027-02-01) PROV 신설 | legislation.gov.uk |
| A-23 | `notes/3-crypto-aml/travel-rule.md` §6 | "외부지갑 등록제 — 법령 미요구" → "2027-02-19부터 고시 의무(동일인만 허용, 방법 미지정)" | 시행령 §10-20 ⑧, 고시 §28-2④ |
| A-24 | `notes/3-crypto-aml/travel-rule.md` 💼·§7-C·§8, `notes/4-technology/travel-rule-protocols.md` §N.4·§M | "Sunrise 미연결 5~15%", "자동 성공 85%", 오류 분포 35/22/18/12/8%, SLA, "보존 한국 15년·EU 5년" → 출처 없음, 삭제 또는 "미검증" | travel-rule F-073 |
| A-25 | `notes/4-technology/travel-rule-protocols.md` §2·§N.1 | "DateAndPlaceOfBirth(선택)", "EU 모든 필드 필수", "US 2025 개정 제안 $1,000" → IVMS 101.2023 제약 C1 "택1 이상", TFR §14(1)(d) 주소 또는 생년월일·출생지, $1,000 제안은 존재 확인 안 됨($250 안은 철회) | IVMS 101.2023, TFR, reginfo |
| A-26 | `notes/4-technology/travel-rule-protocols.md` §3-C·§3-H, `notes/7-vendors/travel-rule-vendors.md` §2-F·§8 | "OpenVASP: Ethereum·ENS·Whisper", "GTR: BitGo 등 컨소시엄", "IVMS101 v2" → OpenVASP Association은 TRP 관리 협회, GTR 운영 주체는 Infozone Technologies(싱가포르), "IVMS 101.2023(현행)"; 가격·우열 평가 삭제 | travel-rule F-059·F-065·F-067 |
| A-27 | `notes/2-regulations/eu-mica-amlr.md` TL;DR·§2·§5 | "2024-12-30 전면 시행" → "발효 2023-06-29 / 적용개시 2024-12-30" 분리; AMLA 2026-01-01 권한 이관·2026-10-01 RTS 3건 제출·2026-10-07 MiCA 재검토 의견, ESMA 등록부 379행(2026-10-19) 추가 | EBA, AMLA, ESMA |
| A-28 | `kb/entities/regulations/eu-amlr.yaml`, `intl-fatf-r16.yaml`, `eu-mica.yaml` | RTS 제출, 가이던스 의견수렴(2026-06-24~08-21, 최종 미발간), 등록부 통계 노트 추가 | AMLA, FIAU |
| A-29 | `notes/2-regulations/asia-regs.md` §3.5 | "2026 개정 자금결제법 2026-04 시행 예정" → "令和7年 개정 자금결제법 2026-06-01 시행(wave1)과 별개로 금상법 이관 개정법 2026-07-15 성립, 시행일 미정" | 金融庁 |
| A-30 | `notes/2-regulations/asia-regs.md` §1·§2·§4, `hk-amlo-sch2-s13a.yaml`, `sg-psn02-para13.yaml` | 홍콩 VATP 13·스테이블코인 발행자 2, 트래블룰 valid_from 2023-06-01(B), 싱가포르 PSN02 ¶13.8 해소·2025-07-01 개정, MAS 스테이블코인 의견수렴(proposed), VARA III.G AED 3,500 "exceeding" 추가 | SFC, HKMA, MAS, VARA |
| A-31 | 과제 지시문·업계 서술의 "홍콩 트래블룰 2024-06-01" | → 2023-06-01 시행(즉시전송 2024-01-01). 2024-06-01은 과도기간 종료와 혼동된 것 | Clyde & Co, 21 Analytics(B) |
| A-32 | `README.md` 트래블룰 요약 | "8개 관할" + 9개 열거 → 개수 정합화, 한국 100만원 "폐지 확정·미시행" 주석 | aml-landscape §9 #28 |
| A-33 | `notes/2-regulations/korea-user-protection.md` §3-C·§7·💼·전반 | §12 누락 → "§12 상시감시, 시행령 §18, 조사업무규정 §3·§4" 소절 신설; "분리보관 위반 5년 이하 징역·5천만원 벌금" → 현행 §22① 과태료 1억원 이하로 재작성; 출처 없는 벤더명·시점 삭제; 통신사기피해환급법 거래소 적용(2026-10-01)·출금지연(2025-05→2026-04-07) 추가 | 법제처 법령 원문, 금융위 |
| A-34 | `kb/entities/regulations/kr-vaupa.yaml` | §12 PROV 분리, 현행 법률 제21857호·시행 2026-10-02 반영 | 법제처 |
| A-35 | (신설) `kb/entities/regulations/kr-tsf-act.yaml`, `kb/entities/orgs/kr-fsi-asap.yaml` | 통신사기피해환급법(제21503·21320·20368호), ASAP(2025-10-29 출범, 2026-08-04 법정 지정) | 법제처, 금융위 |
| A-36 | `notes/4-technology/kyc-kyt.md` §3·§6·§8 | Risk Engine 출력(ALLOW/EDD/STR/BLOCK) 단일 축 → 산출물 3축(차단/통보/STR) 분리; "의심되면 차단 먼저" → 임시조치 절차(통지·본인확인·해제·기록 보존)와 이용자보호법 §11 입출금 차단 제한 명시; 한국 법적 근거로 업무규정 제76~81조 추가 | fds §1-A, kyt F-022 |
| A-37 | `notes/4-technology/kyc-kyt.md` §4·§7·💼, `notes/7-vendors/analytics-vendors.md`, `notes/7-vendors/vendor-benchmark.md` | 노출도 공식·"5-hop"·λ 표·4대 거래소 KYT 일괄 표기·가격·점유율·FP 70~85%·"Lynx GNN"·"룰 80% + ML 20%" → 공개 근거 없음, "가설 모델/미검증"으로 격하 또는 삭제 | kyt §9 |
| A-38 | `notes/4-technology/blockchain-analytics.md` §2.A·§2.B·§11.2(76~83·112~118·643~651행) | CTR:00007 계열 날조 P/R/F1 표 3곳 잔존 → 삭제, "표준화된 정확도 수치 부재"로 대체 | academic §8 #9 |
| A-39 | `notes/4-technology/blockchain-analytics.md` 648~649·634~635·535·605행, §5.5 | Weber 2019 "RF 0.93/0.77/0.84, GCN 0.92/0.83/0.87" → RF 0.971/0.675/0.796, GCN 0.812/0.512/0.628; Elliptic++ "2022·840K tx·1.6M 주소" → 2023·822k+ 주소·1.27M; Elliptic2 "~122M txs" → 라벨 서브그래프 122K; 브리지 정확도 표 → ABCTracer·ConneX·Ethereum–Polygon 실측; Monero "완전 추적 불가" → 2023 패치 전 구간 부분 추적 가능 | academic P-061~P-063, P-006·P-007·P-016, P-023 |
| A-40 | `deep/papers.md` | Bellei 2024 제목 오기 → "The Shape of Money Laundering…"; Alarab 2020 ICDM → ACM ICMLT 2020(수치 미검증); Möser&Böhme ESORICS → IEEE EuroS&PW 2017; Androulaki ESORICS → FC 2013; Harlev HICSS 2018 추가; "Sun et al. 2023" 삭제(존재 미확인); Lorenz 2020 제목 보완; BABD IEEE TIFS 2024; 트래블룰 동료심사 문헌(P-031~P-034)·2025~2026 섹션 신설 | Crossref, arXiv |
| A-41 | `deep/reports.md` §1·§2·§3·§7 | Chainalysis "$82B·$17B" → 서론에 없음, "출처 확인 필요"; 하한·2024 수치 상향 수정·분모 정의 추가; TRM 보고서명 "2026 Crypto Crime Report"; BIS AER 2026·ECB OP 382·FSB(2026-10-12) 항목 신설; Elliptic 2025 Typologies | academic P-065~P-070 |
| A-42 | `curriculum/day_57.md` | "STR 초안 30% 시간 단축", "4대 거래소 XGBoost 2023~2025 도입", "Binance 2024 Sardine", "Kraken Featurespace" → 출처 없음, 삭제 또는 "미검증"; "이상거래 탐지"를 FDS/시장감시/의심거래 탐지로 분리; "Scam 사전 탐지 실용도 하~중" 재검토(PhishEye·CtPhishCapture) | fds §9, academic §8 |
| A-43 | `notes/3-crypto-aml/onchain-typology.md` | 체크리스트에 Red Flag RF-ID 병기, "Bybit 48시간 내 $160M layering" 출처 없음 → 삭제 또는 보강; 동결저항 자체 스테이블코인·RPC/멀티시그 공격·AI 딥페이크 채용사기·address poisoning 유형 추가; "이상거래 자동 탐지" → "온체인 이상 패턴(anomaly) 탐지" | 7차 TU para 33–35, P-036 |
| A-44 | `kb/entities/indicators/`(63건) | curator_note "Red Flag 원문 미확보, T3 의존" → `DOC:intl-fatf-va-red-flags-2020` evidence 추가, 완전 매핑 17건 confidence A·RF-ID locator; 공백 지표 17건(RF-P7·A9·A10·S5·S6·S10~S14·S16·S18·F7 등) 신규 후보; ATM 단독·하드웨어 지갑 지표 fp_risk 상향 | fatf-reports §3A-3, §9-3 |
| A-45 | `en/quick-start-guide.md`, `notes/glossary.md`, `notes/5-compliance/str-ctr.md`, `notes/5-compliance/inspection-response.md` | "이상거래보고 → STR" → "의심거래보고(STR)"; FDS·이상거래(§12)·이상금융거래·임시조치·시장감시 용어 신설; STR 입력원에 FDS 알림·시장감시 적출 추가; 검사 대비 체크리스트를 FIU/금감원(§12)/금융안전과 3분할 | fds §9.1 |
| A-46 | `_research/wave1/analytics-technology.md` F-028 | Tornado Cash 클러스터링 논문 철회 사유 "mistakes in the references"(2025-11-18 v3) 추가 | arXiv 2510.09433 |

## 부록 B. 확인하지 못해 본문에서 뺀 것

1. FATF 설립(1989)·40개 권고(1990)·비트코인 백서(2008) — 배경으로만 언급, 도시에 검증 범위 밖
2. FATF 흑색명단 구성(북한·이란·미얀마) — 단일 T4
3. 회색명단 22개 개별 국가명 — FATF 원문 403, T4 재구성(개수만 B로 사용)
4. FATF 2026-10 총회 결과, R.16 이행 가이던스 최종본 — 2026-10-21 기준 미개최·미발간
5. 개정 R.16 평가방법론(Annex IV) 발효 상태, 확대 정보항목, "ISO 20022·구조화 데이터" — 재확인 안 됨
6. 미국 CLARITY Act 상원 토론종결 49-50 부결(2026-09-15) — T4, C
7. Roman Storm 재심 2027-04-26 연기 — T4, C
8. 두나무 영업일부정지 처분 1심 취소(2026-04-09)·FIU 항소, 빗썸·코인원·코빗 제재 세부 — T4, C
9. 한국 기존 사업자 재신고 기한 2026-11-20 — T4 단독, 부칙 원문 미확인
10. 디지털자산기본법·원화 스테이블코인 진행, 법인 실명계좌 2단계 — T4, C
11. 한국 감독규정 §28-2 정확한 시행일(2027-02-19 vs 02-21) — 기산점 미확정
12. 일본 개정법 공포일·법률번호(令和8年法律第64号)·시행 기한 — T4 단독
13. 호주 AML/CTF Rules 2025의 트래블룰 시행일(2026-03-31 vs 2026-07-01)과 Rules 금액 구분, 자기수탁 보고 2029-03-31 유예 — 도시에 간 상충, AUSTRAC 원문 미열람
14. UAE 연방 Decree-Law 10/2025 — T5, D
15. 태국 고시번호·THB 30,000 기준, 캐나다 CAD 1,000 기록 임계 — 미확인
16. 일본 FSA "対象外ウォレット" 정보 보존 요구 — 원문 미추출
17. Chainalysis 스캠 챕터(140억~170억 달러, 사칭 +1,400%), "제재 주체 수취 $104B", `deep/reports.md`의 $82B·$17B — T4 또는 원문 부재
18. TRM 2026 YTD 북한 76%·5.77억 달러, H1 2026 수치 — T4, C
19. Chainalysis 서문의 +162%와 산술상 +169% 차이 — 각주로만 처리, 원인 미확인
20. 벤더 제품 페이지 수치(커버리지, 노출도 홉 정의, 지연 ms, 라벨 주소 수, 고객 수) — T5
21. 벤더 인수·투자 금액(Hexagate, Alterya, Nash, TRM 기업가치, Elliptic 라운드) — T4, C
22. ICE–TRM 단독계약·Chainalysis 입찰이의 — 판결 미확인, 벤더 간 분쟁
23. Chainalysis AI 에이전트 정식 출시 여부, T3 FCU 누적 동결 4.5억 달러, Tether–Crystal 투자 — T4/T5
24. 경찰청 분석도구 예산 36.57억원, 업비트·코인원 KYT 도입 연도, 2022-09 FIU 검사 "추출 0건" 사례 — T4, C
25. 트래블룰 프로토콜·솔루션 네트워크 규모(Notabene·Sumsub·CODE·VerifyVASP·GTR·TRUST 등) — 자사 주장, Shyft Veriscope 중단은 T3 단일
26. 거래소 FDS "누적 1,500억 원 예방" — 회사 자체 발표
27. 출금지연제도 집계표의 피해 절대액(2,257억·1,705억) — 단위 미확정(비율만 사용)
28. 제2금융권 자율배상 1.6% 등 국회 제출자료 — T4, C
29. 영국 PSR 환급 상한 £85,000 인하 — 원문 미확인
30. Elliptic "Tornado 100 ETH 풀 예치 1/3 불법 출처", Flash Mixer MCP — T4 단일
31. 철회 논문 arXiv 2510.09433(Tornado Cash 클러스터링), arXiv 2603.04328(규제 손실) — 수치 인용 금지
32. 리뷰 2차 종합치 "그래프 어텐션 40% 우위"(P-015), P-029 자체 보고 "45분→8초", P-046 "97%/82%", Cengiz "F1 92.3%", SaTML 2026 논문(초록 미열람), Lightning TOIT 논문(저자 미확인), xfraud 데이터셋 구성 — 초록 부재 또는 C
33. Feinstein & Werbach 2020 이벤트 스터디 결과 — 초록 미열람
34. 한국 법학 학술지 2025 논문, 한국은행·KDI·자본시장연구원 보고서 — 접근 실패(부재 결론 아님)
35. 한국 5차 상호평가 일정, AMLA 직접감독 잠정목록, MiCA 경과규정 종료 등 wave1 의존 항목 — 이번에 재확인 안 됨

---

[^bg]: 1989·1990·2008 사실은 6개 도시에 어디에도 원자적 사실(F-ID)로 수록되지 않았다. 연대기 맥락을 위해서만 쓰며 인용 근거로 삼지 않는다.
[^kr-mer]: 저장소 `notes/2-regulations/fatf.md`는 "4차 ME 가상자산 영역 PC"라고 적었지만 FATF 한국 MER 페이지 등급표는 "R.15 - New technologies C"다(fatf-reports F-058, T1/A). 7차 TU Annex A는 한국을 "N/A(개정 기준 미평가)"로 표시한다(F-056). 개정 기준 등급은 2026-04 기준 아직 없다.
[^hk]: 과제 예시와 일부 업계 서술의 "홍콩 2024-06-01"은 어느 출처에서도 트래블룰 일자로 확인되지 않는다. 복수의 T3(Clyde & Co, 21 Analytics)가 2023-06-01 시행·2024-01-01 즉시전송으로 일치한다(travel-rule F-048, B). 2024-06-01은 기존 SFO 인가 VATP의 12개월 과도기간 종료와 혼동된 것으로 보인다. eLegislation 원문은 미확보다.
[^crime]: Chainalysis는 "all inflows to known services" 대비 1% 미만이라고 하고 비크립토 원천 범죄는 뺀다. TRM은 "conservative baseline — a minimum, or 'floor'"로서 전체 귀속 온체인 거래량 대비 1.2%, VASP 유동성 대비 2.7%라고 한다. TRM 보고서는 유동성 지표의 분모를 방법론에서는 "VASP outflows", 본문에서는 "incoming VASP flows"로 달리 적는다(academic §5-5). Chainalysis의 +162%는 $154B/$57.2B의 산술값(약 +169%)과 다르다(aml-landscape C-08). 두 회사 모두 추후 상향 수정을 예고했다.
[^1000]: 입법예고안(금융위 2026-03-30)은 "1,000만원 이상 거래에 대해서는 위험도와 관계없이 의심거래로 보아 금융정보분석원에 보고"였다. 공포본 시행령 §10-20 ⑦나는 "자체적인 의심거래 감시체계를 구축ㆍ운영할 것"이고, 고시 §28-2③이 그 금액을 1천만원으로 정한다(travel-rule F-015·F-018·F-020, T1/A). kyt 도시에의 "위험도 무관 STR, 2027-08-20 시행"(F-032, T3 법무법인 요약의 입법예고 기준)은 공포본과 달라 채택하지 않았다.
[^half]: 7차 TU 본문 para 25는 "Slightly more than half of the 91 jurisdictions (60%; 55 of 91)…"이고, 요약(Key Findings p.3)은 "almost half"다. 1차 문서 내부의 불일치로, 본문 수치를 채택했다(fatf-reports F-044, aml-landscape C-01).
[^krdate]: 채택: 대통령령 제36592호 공포 2026-08-18, 부칙 제1조 단서 "공포 후 6개월이 경과한 날", 법제처 eflaw 시행예정 판본 시행일자 20270219(travel-rule F-011·F-012, T1/A). 기각: 언론(이데일리·쟁글)의 2027-02-20(공포일을 08-19로 가정한 계산으로 보임), kyt 도시에와 입법예고 부칙의 2027-01-01. 법제처 조문 단위 메타데이터에는 조문시행일자 20260820이 찍혀 있는데, 이는 부칙·헤더와 충돌하는 레코드 결함이다(travel-rule §5).
[^sup]: FIU 고시 제2026-2호 부칙은 제26조·제28조의2·제31조제3호를 "공포 후 6개월이 경과한 날"부터 시행한다고 한다. 발령일 2026-08-20을 기산점으로 하면 2027-02-21이 되어 시행령 §10-20(2027-02-19)과 이틀 어긋날 수 있다. 법제처 행정규칙 시행일 색인으로 확정해야 한다(travel-rule F-019).
[^rin]: 믹싱 NPRM의 원래 RIN은 1506-AB64인데, 2026-10-06 철회 공고에는 1506-AB47(비수탁지갑 규칙과 같은 번호)이 적혀 있다. 공고의 오기로 보인다. 식별은 88 FR 72701 인용으로 한다(aml-landscape C-02).
[^plen]: FATF 일정표는 총회·작업반 주간을 2026-10-26~30으로 적는다(T1). 보도(ANI, T4)의 10-28~30은 본회의 일정이다(fatf-reports §5).
[^au]: AML/CTF Act s 66A는 금액 조건이 없다(T1/A). Rules 2025의 시행일은 travel-rule 도시에가 2026-03-31(T3, B), aml-landscape 도시에가 2026-07-01(T4, C, "newly regulated virtual asset services")로 적어 상충한다. AUSTRAC 원문을 열지 못해 해소되지 않았으므로 표에 날짜를 넣지 않았다.
