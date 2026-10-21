# 용어 사전 (Glossary)

> AML·가상자산 약어와 한국어·영어 용어. 이 사전의 목적은 **"어떤 용어를 봤을 때 30초 안에 핵심·실무 맥락을 잡는 것"** 입니다. 핵심 용어는 💡 **실무** 블록으로 "실무에서 언제·어떻게 쓰이나"를 1~2줄 추가. ABC 순. 마지막 업데이트: 2026-10-21.

## 이 사전 사용법

- 읽다가 모르는 약어가 나오면 **Ctrl+F**로 찾기. 전체를 암기할 필요 없음.
- 헷갈리는 짝(KYC vs KYT, CDD vs EDD 등)은 `1-foundations/key-concepts.md`의 **"자주 헷갈리는 짝" 표**에서 한 번에 대조.
- 용어마다 있는 💡 **실무** 블록은 정의를 넘어 "실제로 이 용어를 언제 쓰나"의 감각을 주기 위한 것.
- 상세 학습은 각 용어의 Deep 문서(링크는 맨 아래)로.

---

## A

- **AML** (Anti-Money Laundering) — 자금세탁방지.
  - 💡 **실무**: 회사 AML 프로그램 = 9대 의무(신고·KYC·EDD·KYT·제재·STR·Travel Rule·기록·내부통제)의 합. "AML 담당자"는 보통 이 9개 운영.
- **AMLA** (Anti-Money Laundering Authority) — EU AML 감독기구, 프랑크푸르트 본부. 2026-01-01 EBA로부터 AML/CFT 규칙제정·가이던스 권한을 넘겨받았다.
  - 💡 **실무**: 2026-10-01 AMLR 첫 RTS 3건 최종안을 집행위에 제출(채택 전). 직접감독 대상은 6개 이상 회원국에서 영업하는 금융기관(그룹) 약 40개로 VASP 전용이 아니며, CASP 포함 여부는 공개되지 않았다(B).
- **AMLD** (Anti-Money Laundering Directive) — EU AML 지침. AMLD5 → AMLD6 진행 중.
- **AMLO** (Anti-Money Laundering Officer) — AML 책임자.
  - 💡 **실무**: 한국 특금법은 **임원급** 요구. STR 결정권·CEO 직접 보고 채널이 핵심. Binance CZ 사례 이후 **개인 형사 책임** 가능성 명확해짐.
- **AMLR** (AML Regulation) — EU AML 규정 (2027-07-10 적용).
- **AML/CFT** — 자금세탁방지·테러자금조달방지 결합 표기.
  - 💡 **실무**: ML은 "출처 은닉"(사후), TF는 "목적지 차단"(사전). 룰 엔진 설계 시 **별도 그룹**으로 관리하는 게 분석 품질 ↑.
- **APG** (Asia-Pacific Group on Money Laundering) — FATF 지역 기구. 한국도 회원.
- **APT** (Advanced Persistent Threat) — 지속적 표적 공격 (Lazarus 등). 국가급 사이버 부대 지칭에 주로 사용.
- **ART** (Asset-Referenced Token) — MiCA 토큰 카테고리, 여러 자산 페그.
- **Attribution** — 지갑 클러스터를 알려진 엔티티에 매핑.
  - 💡 **실무**: Chainalysis·TRM·Elliptic의 **진짜 경쟁력**이 여기. 알고리즘(Clustering)은 복제 가능하지만 attribution DB는 수년 누적 필요.

## B

- **Beneficial Owner / BO** — 실소유자 (법인 25% 이상 자연인).
  - 💡 **실무**: 법인 고객 onboarding 시 재귀적으로 지분 추적. UBO 확인 불가면 **거래 거절**이 원칙 — 억지 수용 시 STR + 영업정지 리스크.
- **BSA** (Bank Secrecy Act, 1970) — 미국 AML 모법.
  - 💡 **실무**: FATF 권고의 원형이 이 법. 한국 특금법 많은 조항이 BSA 구조를 차용했으므로, 미국 법을 알면 한국 법 이해가 빨라짐.
- **Bridge** — 체인 간 자산 이동 인프라.
  - 💡 **실무**: 출금 주소가 브리지 컨트랙트면 단순 휴리스틱으로는 다음 홉 추적이 어렵다. 크로스체인 자동 매칭 연구(ABCTracer·ConneX)가 있으나 브리지 집합이 달라 정확도를 직접 비교할 수 없다. 브리지 노출은 STR 자동 대상이 아니라 **검토 큐**의 입력이다.

## C

- **CASP** (Crypto-Asset Service Provider) — EU MiCA 용어, ≈ VASP.
- **CCO** (Chief Compliance Officer) — 컴플라이언스 총괄.
- **CDD** (Customer Due Diligence) — 고객실사 (표준).
  - 💡 **실무**: 4단계(식별·BO·목적·모니터링). onboarding 1회로 끝 아니고 **지속 모니터링**이 핵심. 재실사 주기는 위험등급별로 사내 기준을 정한다.
- **CFT** (Combating the Financing of Terrorism) — 테러자금조달방지.
- **Chain Hopping** — BTC → ETH → Tron → BNB 같은 체인 점프 layering.
- **Chainalysis** — 미국 블록체인 분석 회사 (시장 표준).
  - 💡 **실무**: FIU는 2026-02-05 업무계획에 "체이널리시스(가상자산 분석도구) 도입"을 넣었다. 거래소별 도입 현황은 공개 근거가 없어 적지 않는다.
- **Cluster / Clustering** — 같은 엔티티 추정 주소 묶음.
  - 💡 **실무**: UTXO(BTC) 모델이 Account(ETH) 모델보다 클러스터링 정확도 높음. Ethereum은 Attribution DB 의존도 ↑.
- **CMLN** (Chinese Money Laundering Network) — 중국어 자금세탁 네트워크.
  - 💡 **실무**: 텔레그램·위챗 OTC + **Laundering-as-a-Service**. 처리 규모 추정치는 분석업체마다 정의가 달라 여기서는 인용하지 않는다.
- **CODE** — 한국 Travel Rule 컨소시엄 (빗썸·코빗·코인원 합작).
- **Cold Wallet** — 오프라인 지갑 (콜드월렛).
  - 💡 **실무**: 가상자산이용자보호법 시행령은 **이용자 가상자산의 80% 이상** 콜드월렛 보관 의무.
- **CPF** (Counter-Proliferation Financing) — 대량살상무기 확산금융 차단.
- **CTR** (Currency Transaction Report) — 임계금액 초과 현금거래 보고.
  - 💡 **실무**: 한국 1천만원, 미국 $10K. VASP는 현금 취급 드물어 실제 트리거 거의 없음(OTC desk 예외).
- **CVC** (Convertible Virtual Currency) — FinCEN 용어, 환전 가능 가상통화.

## D

- **DAO** (Decentralized Autonomous Organization) — 탈중앙 자율 조직.
- **DAXA** — 디지털자산거래소공동협의체 (한국 4대 거래소).
  - 💡 **실무**: 법적 강제력 없지만 **자율 규제**(상장 심사 기준 등)가 사실상 산업 표준. 신규 프로젝트 상장 시 1차 관문.
- **DeFi** (Decentralized Finance) — 탈중앙 금융.
- **DEX** (Decentralized Exchange) — 탈중앙 거래소.
  - 💡 **실무**: KYC 없는 swap 환경이라 layering에 자주 악용. DEX 컨트랙트 노출은 KYT 룰의 단골 트리거.
- **DMLRO** — Deputy MLRO, 부책임자.
- **DPRK** (Democratic People's Republic of Korea) — 북한.
- **DTI** (Digital Token Identifier, ISO 24165) — 토큰 식별 표준.

## E

- **EDD** (Enhanced Due Diligence) — 강화된 고객실사.
  - 💡 **실무**: CDD 위에 **자금원천 증빙 + 임원 승인**을 덧붙이는 강화. "추가 신분증"이 아니라 **SoF·SoW 문서 요구**가 핵심.
- **EMT** (E-Money Token) — MiCA 토큰 카테고리, fiat 페그 stablecoin.
- **EOA** (Externally Owned Account) — Ethereum 외부 소유 계정 (사용자).
- **ERA** (Enterprise-wide Risk Assessment) — 회사 전체 위험 평가.
  - 💡 **실무**: 한국 RBA 가이드라인 연 1회 이상 수행 요구. 감독 검사에서 **가장 먼저 요구되는 문서**.
- **ESMA** (European Securities and Markets Authority) — EU 증권 감독.
- **Exposure** — 한 주소가 위험 주소에 직간접 노출된 정도.
  - 💡 **실무**: KYT 시스템의 핵심 출력. Direct vs Indirect 구분이 일반적이나, 노출도 산정 공식·홉 정의는 벤더별 자사 주장이며 공개 표준은 없다.

## F

- **FDS** (Fraud Detection System) — 이상금융거래탐지시스템. 금감원(2014-12-10)은 "전자금융거래 접속정보·거래내역 등을 분석하여 이상거래를 탐지·차단하는 시스템"으로 정의.
  - 💡 **실무**: AML의 하위가 아니라 **병렬 제도**. 목적은 이용자 자산 보호(계정탈취·보이스피싱), 1차 산출물은 **임시조치**(지연·일시정지)·지급정지. 전자금융감독규정에는 FDS라는 용어가 없고, 실질적 법정 근거는 통신사기피해환급법 §2의5(가상자산거래소 2026-10-01~). → [`4-technology/fds.md`](4-technology/fds.md)
- **FATF** (Financial Action Task Force) — 국제자금세탁방지기구.
  - 💡 **실무**: 법 아닌 권고 발표. 한국 규제의 모태. Grey/Black List가 사실상 경제 제재처럼 작동.
- **FinCEN** (Financial Crimes Enforcement Network) — 미국 FIU.
- **FIU** (Financial Intelligence Unit) — 금융정보분석원.
  - 💡 **실무**: 한국은 KoFIU. STR 수신·분석·배분(경찰·검찰·국세청·관세청 등)의 허브.
- **Freezing / Freeze** — 자산 동결.

## G

- **GENIUS Act** — 미국 stablecoin 입법 (2025-07-18 서명). 2026-10-21 기준 enacted-not-in-force — 법정 최종 시행기한 2027-01-18 시행이 예상된다(B).
- **GLEIF LEI** (Legal Entity Identifier) — 법인 식별 글로벌 표준.
- **Grandfathering** — 기존 사업자 전환기간. MiCA는 2026-07-01 종료.
- **Grey List** — FATF 강화 모니터링 국가 목록.

## H

- **HSM** (Hardware Security Module) — 하드웨어 보안 모듈.

## I

- **IEEPA** (International Emergency Economic Powers Act) — 미국 OFAC 권한 근거.
  - 💡 **실무**: 2024 Tornado Cash 5th Cir. 판결에서 "immutable smart contract는 IEEPA의 property로 볼 수 없다"며 OFAC 패소한 핵심 법.
- **Integration** — 자금세탁 3단계 마지막 (합법 자산화).
- **IVMS101** (InterVASP Messaging Standard 101) — Travel Rule 메시지 표준.
  - 💡 **실무**: 모든 프로토콜(TRISA·TRP·VerifyVASP·CODE·Notabene)이 페이로드로 사용하는 JSON 스키마. 관할별 필수 필드 차이가 validator 구현의 난제.

## J

- **JWG** (Joint Working Group) — IVMS101 합의 그룹.

## K

- **KISA** — 한국인터넷진흥원. **ISMS 인증** 발급.
- **KoFIU** — 한국 FIU (금융정보분석원).
- **KYC** (Know Your Customer) — 고객확인.
  - 💡 **실무**: "고객을 안다"는 광범위 개념. 한국 VASP는 PASS·NICE 등 본인확인기관 + ARGOS 같은 SDK + PEP 스크리닝 조합.
- **KYT** (Know Your Transaction) — 거래·지갑 확인 (가상자산 특화). **업계 용어**다 — FATF·MAS·한국 고시 어디에도 "KYT"라는 말은 나오지 않는다. 규범 문언은 "ongoing monitoring"(FATF 2021 가이던스 para 275), "transactions monitoring and blockchain analytics tools"(FATF 7차 TU, 2026-07-16), 한국은 「자금세탁방지 업무규정」 제76~81조 "거래모니터링체계".
  - 💡 **실무**: KYC와 대체재가 아닌 보완재. KYT만으로는 "주소 위험"만 알 수 있고, STR 작성에는 KYC의 "누구" 정보가 반드시 결합돼야 함. KYT 알림의 법적 출구는 STR이다 — FDS의 임시조치, §12 시장감시의 통보와 섞지 않는다.

## L

- **Layering** — 자금세탁 3단계 중 둘째 (은닉).
- **Lazarus Group** — 북한 후원 사이버 부대.
  - 💡 **실무**: FATF 6차 TU(2025-06-26)는 DPRK의 Bybit USD 14.6억 탈취(회수율 3.8%)를 헤드라인으로 올렸고, 7차 TU(2026-07-16)는 RPC 노드·멀티시그 공급자 같은 제3자 인프라 공격과 딥페이크 채용사기를 위험요인으로 들었다.
- **LE** (Law Enforcement) — 법집행기관.
- **LEI** (Legal Entity Identifier) — 법인 식별자.
- **Liveness Check** — 살아있는 사람 vs 사진·영상 검증.
- **LST** (Liquid Staking Token) — Lido 등 유동 스테이킹 토큰.
- **LRT** (Liquid Restaking Token) — EigenLayer 등.

## M

- **Market Surveillance / 시장감시** — 가상자산이용자보호법 §12의 "이상거래에 대한 감시". 시세조종·미공개정보 이용 등 불공정거래(§10) 우려 거래를 상시 감시하고, 위반 의심 시 금융위·금감원에 **통보**(혐의가 충분히 증명된 경우 등은 수사기관 신고 후 보고).
  - 💡 **실무**: 의무 주체는 가상자산시장을 개설·운영하는 거래소. 조치는 「가상자산시장조사업무규정」 §3(거래유의 안내·조회공시·주문제한·거래중지). 위반 시 과태료 1억원 이하(§22①6·7호). 보이스피싱 탐지(FDS)와도, STR과도 다른 제도.
- **MEV** (Maximal Extractable Value) — 블록 순서 조작으로 추출하는 가치.
- **MiCA** (Markets in Crypto-Assets Regulation) — EU 가상자산 규제.
  - 💡 **실무**: 발효 2023-06-29, 적용개시 2024-12-30. EU passporting으로 한 회원국 인가로 역내 영업 가능. ESMA 임시 CASP 등록부는 2026-10-19 기준 379행.
- **Mixer / Tumbler** — 자금 섞기 서비스.
- **MLRO** (Money Laundering Reporting Officer) — 영국·EU AML 책임자.
- **ML/TF** — Money Laundering / Terrorism Financing.
- **MPC** (Multi-Party Computation) — 다자간 컴퓨팅 (수탁 키 관리).
- **MSB** (Money Services Business) — 미국 송금사업자.
  - 💡 **실무**: 미국 가상자산 회사가 속하는 카테고리. FinCEN 등록 + 주별 Money Transmitter License(MTL) 필수. 50개 주 면허 취득이 악명 높음.

## N

- **NCA** (National Competent Authority) — EU 회원국 감독기구.
- **NFT** (Non-Fungible Token) — 대체 불가 토큰.
- **NIST** (National Institute of Standards and Technology) — 미국 표준원.

## O

- **OCC** (Office of the Comptroller of the Currency) — 미국 은행 감독.
- **OFAC** (Office of Foreign Assets Control) — 미국 제재 집행.
  - 💡 **실무**: **2차 제재**로 인해 한국 VASP도 실질적으로 OFAC 준수 필수. 미국 고객 없어도 USD 결제망·스테이블코인·클라우드로 영향받음.
- **OpenVASP** — OpenVASP Association은 Travel Rule 프로토콜 TRP를 관리하는 협회.
- **Originator** — 송신인 (Travel Rule).
- **OSINT** (Open Source Intelligence) — 공개정보 첩보.
- **OTC** (Over-The-Counter) — 장외 거래.
  - 💡 **실무**: 거액·국경 간·특수 고객이 집중되는 영역이라 고위험으로 다룬다. STR 건수 비교 자료는 공개되지 않았다.

## P

- **PATRIOT Act** — 미국 2001 강화 AML/CFT 법.
- **Peel Chain** — 작게 떼어내는 자금세탁 패턴.
  - 💡 **실무**: 그래프 분석에서 시각적으로 일자형 사슬. in-degree/out-degree 패턴으로 탐지.
- **PEP** (Politically Exposed Person) — 정치적 주요인물.
  - 💡 **실무**: 범죄자라는 뜻 아님. 부패 리스크가 구조적으로 높아 **자동 EDD**. World-Check 등 상용 DB로 스크리닝.
- **PII** (Personally Identifiable Information) — 개인식별정보.
- **PIPA** (한국 개인정보 보호법).
  - 💡 **실무**: Travel Rule에서 PII가 VASP 간 전송되므로 PIPA와 긴장. 국외이전 영향평가(PIA) 정기 수행 필요.
- **Placement** — 자금세탁 3단계 중 첫째 (배치).
- **Privacy Coin** — 익명 코인 (Monero, Zcash 등).
  - 💡 **실무**: 한국·일본 주요 거래소 **상장 폐지**. 규제 부담이 매출보다 크다는 판단.
- **Proof of Reserves** — 준비금 증명. 수탁업의 신뢰 신호.

## R

- **R.15 / R.16** — FATF 권고안 15, 16 (가상자산, Travel Rule).
  - 💡 **실무**: 한국 특금법의 직접 모태. 글로벌 규제 변화가 이 두 권고 개정을 거쳐 각국으로 흘러내림.
- **RBA** (Risk-Based Approach) — 위험기반접근법.
  - 💡 **실무**: FATF 2012 개정으로 전 AML 의무의 운영 원칙. 회사 문서에 **Risk Score 산정 공식·가중치·임계값**이 명시돼야 "RBA를 한다"고 주장 가능.
- **RGB** (Reconnaissance General Bureau) — 북한 정찰총국. Lazarus의 상위 조직.

## S

- **SAR** (Suspicious Activity Report) — 미국 의심거래보고 (≈ STR).
- **SDD** (Simplified Due Diligence) — 간소화된 실사.
  - 💡 **실무**: 한국 가상자산 영역에서는 거의 적용 X. 감독당국이 "가상자산 = 고위험"을 기본 가정으로 함.
- **SDN List** (Specially Designated Nationals) — 미국 OFAC 제재 명단.
  - 💡 **실무**: **유일하게 가상자산 지갑주소를 명시**하는 제재 명단. SDN.XML의 `<feature><type>Digital Currency Address</type>` 구조.
- **SEC** (Securities and Exchange Commission) — 미국 증권거래위원회.
- **Smurfing / Structuring** — 분할 입금 (KYC 회피).
- **STR** (Suspicious Transaction Report) — **의심거래보고**(특금법 §4). "이상거래보고"라고 쓰지 않는다.
  - 💡 **실무**: 금액 무관·의심만 있으면 보고. Tipping-off(고객 누설)은 별도 처벌 대상. 입력원은 KYT·CS뿐 아니라 FDS 알림·§12 시장감시 적출도 포함되지만, 그 1차 산출물(임시조치·통보)은 STR이 아니다. 2027-02-19부터 해외 VASP·자기수탁 지갑 1천만원 이상 이전은 "자체 의심거래 감시체계" 대상 — 자동 STR이 아니다.
- **Sunrise Issue** — Travel Rule 관할별 시행 격차 문제.
  - 💡 **실무**: FATF 7차 TU(2026-07-16) 기준 트래블룰 입법 관할 83%(91/109) 중 60%(55/91)가 감독·집행 조치 없음. 상대 VASP 실사와 폴백 정책이 필요. 한국은 2027-02-19부터 해외 VASP를 위험 등급별로 차등 허용한다.

## T

- **Temporary Measure / 임시조치** — 통신사기피해환급법 §2의5. 금융회사등이 "자체점검을 상시적으로 실시"해 피해의심거래계좌등으로 추정되면 이체·송금·출금 또는 **가상자산 이전**을 지연·일시정지하고, 즉시 통지·본인확인 후 해당 없으면 해제하는 조치.
  - 💡 **실무**: 법률 제21503호로 2026-10-01부터 가상자산거래소에 적용(in-force). 통지·해제·본인확인 내역 보존 의무(§2의5④). FDS의 법정 산출물이며 AML의 거래거절과 다르다.
- **TF** (Terrorism Financing) — 테러자금조달.
- **TFR** (Transfer of Funds Regulation) — EU Travel Rule.
  - 💡 **실무**: **임계금액 0** (모든 거래). 전 세계에서 가장 엄격 → 글로벌 VASP의 설계 baseline.
- **Tipping-off** — STR 사실을 고객에게 알리는 행위 (금지).
  - 💡 **실무**: 특금법상 금지·처벌 대상(조문·형량은 원문 확인 — 이 사전의 이전 판은 조문 번호와 형량을 서로 다르게 적어 삭제했다). 계좌폐쇄 사유 안내 시 "내부 정책상" 같은 일반 표현으로.
- **TM** (Transaction Monitoring) — 거래 모니터링.
- **Tornado Cash** — 이더리움 mixer (2022-08 OFAC 제재 → 2024-11 Van Loon v. Treasury 5th Cir. 판결 → 2025-03-21 지정 해제).
  - 💡 **실무**: 제재 해제됐지만 **업계는 여전히 고위험 카테고리 유지**. "법적으로 허용 ≠ 실무 허용".
- **TraderTraitor** — FBI가 명명한 Lazarus sub-cluster. 가짜 채용 수법.
- **Travel Rule** — FATF R.16, 송수신인 정보 동반 의무.
- **TRISA** — Travel Rule 분산 프로토콜. CipherTrace 시작 (Mastercard 인수).
- **TRP** (Travel Rule Protocol) — REST 기반 프로토콜.
- **TRM Labs** — 미국 블록체인 분석 회사. cross-chain·실시간 강세.

## U

- **UBO** (Ultimate Beneficial Owner) — 최종 실소유자.
- **UNODC** (UN Office on Drugs and Crime) — UN 마약범죄국.
- **Unhosted Wallet** — 개인지갑 (거래소 외부).
  - 💡 **실무**: 2026-10-21 현재 한국 법령은 자기수탁 지갑 이전을 직접 규율하지 않는다. 2027-02-19부터는 "독점적인 관리 권한을 가지지 않은 가상자산주소"와의 이전이 **고객과 상대방이 동일인일 때만** 허용되며(시행령 §10-20 ⑧, 고시 §28-2④), 확인 방법은 정하지 않았다(enacted-not-in-force).
- **USAPA** — USA PATRIOT Act.
- **UTXO** (Unspent Transaction Output) — 비트코인 거래 모델.

## V

- **VA** (Virtual Asset) — 가상자산.
- **VASP** (Virtual Asset Service Provider) — 가상자산사업자.
  - 💡 **실무**: 거래소만이 아니라 **수탁·OTC·중개**도 포함. 한국 특금법 §2.1.하의 5가지 행위가 판단 기준.
- **VerifyVASP** — 한국 Travel Rule 솔루션 (람다256 + Chainalysis, Upbit 채택).

## W

- **Wash Trading** — 가짜 거래 (가격·거래량 부풀리기).
  - 💡 **실무**: 한국에서는 가상자산이용자보호법 §10 불공정거래이자 §12 시장감시의 탐지 대상. 금융위는 2026-09-23 사업자 임원이 마켓메이커를 고용해 거래량의 90% 이상을 가장매매한 사건을 고발·통보 의결했다.
- **Wolfsberg Group** — 글로벌 은행 AML 모범사례 그룹. HSBC·Citi·JPMorgan 등.

## Z

- **ZKP** (Zero-Knowledge Proof) — 영지식 증명.
  - 💡 **실무**: 프라이버시와 컴플라이언스 양립의 장기 열쇠. zk-KYC·Polygon ID·Worldcoin이 초기 실용화 시도.
- **zk-SNARK** — 영지식 증명 일종 (Tornado Cash, Zcash).

---

## 용어 짝 비교 — 자주 혼동되는 짝

한국 AML 실무에서 영문·국문·법령 용어가 뒤섞여 쓰입니다. 다음 짝은 **엄밀히는 의미가 다르거나, 같은 뜻이지만 출처 맥락이 다른 경우**.

### 고객확인 vs 실명확인 vs KYC

| 용어 | 출처·맥락 | 정의 |
|---|---|---|
| **고객확인(顧客確認)** | 특금법 §5의2 | 법정 용어. 법령상 VASP가 해야 할 "고객 실명 + 목적 + 자금원천" 확인 전체. 포괄 개념. |
| **실명확인(實名確認)** | 금융실명법·특금법 §5의2 ① | **고객확인의 한 부분** — 신분증·본인확인기관(PASS/NICE) 통한 본인 일치 검증만. 더 좁음. |
| **KYC (Know Your Customer)** | FATF·글로벌 | 국제 표준 용어. **한국 "고객확인"과 대체로 등가**이나, 각국 법 상세 조항 차이. |
| **CDD (Customer Due Diligence)** | FATF R.10 | KYC의 공식 법적 표현. "고객실사" 번역. |

**실무 사용**:
- 한국 법 문서 → "고객확인" 또는 "실명확인"
- 영문 회사 자료·FATF → "KYC" 또는 "CDD"
- **두 표기 혼용 허용**, 단 한 문서 내 일관성 유지

### STR vs SAR

| 용어 | 관할 | 의미 |
|---|---|---|
| **STR (Suspicious Transaction Report)** | FATF·한국·EU·싱가포르 | 의심거래 보고. 한국 특금법 §4. (§5의3은 트래블룰 조문) |
| **SAR (Suspicious Activity Report)** | 미국 FinCEN | 의심활동 보고. BSA 31 CFR 1020.320. 거래가 없어도 활동 의심 시 보고 가능 (더 넓음). |

### Travel Rule vs Wire Transfer Rule

| 용어 | 맥락 |
|---|---|
| **Travel Rule** | 가상자산 송수신 정보 동반. FATF R.16. 2019~. |
| **Wire Transfer Rule** | 전통 금융 전신환. BSA 1996~. Travel Rule의 기원. |

### AMLO vs MLRO vs Compliance Officer

| 용어 | 관할 |
|---|---|
| **AMLO (Anti-Money Laundering Officer)** | 한국·글로벌 일반 |
| **MLRO (Money Laundering Reporting Officer)** | 영국·EU 전통 |
| **Compliance Officer (CO)** | 더 넓은 준법 (AML 포함하거나 독립) |
| **CCO (Chief Compliance Officer)** | C-level, 임원급 |

### Tipping-off vs Disclosure

| 용어 | 의미 |
|---|---|
| **Tipping-off** | 의심거래 보고 사실을 **고객에게 누설** — 특금법상 금지(조문·형량은 원문 확인) |
| **Disclosure** | 일반적 "공개" — Tipping-off는 Disclosure의 한 형태 (특정 사실에 대한 금지) |

### 이상거래 vs 이상금융거래 vs 의심거래

한국에서 가장 자주 섞이는 짝. 세 용어는 **법적 근거·목적·산출물·수령 기관이 전부 다르다**. 상세는 [`4-technology/fds.md`](4-technology/fds.md).

| 용어 | 출처 | 목적 | 산출물 | 수령 기관 |
|---|---|---|---|---|
| **이상금융거래** (FDS) | 금감원·금보원 「FDS 운영 가이드라인」(2023-10-05), 통신사기피해환급법 "피해의심거래계좌등" | 이용자 자산 보호(계정탈취·보이스피싱) | 임시조치(지연·일시정지)·지급정지·피해환급 | 금융위 금융안전과·금감원 금융사기대응단, 금융보안원 |
| **이상거래** (§12) | 가상자산이용자보호법 §12, 시행령 §18 | 불공정거래 적발(시장 건전성) | 금융위·금감원 통보, 거래유의·주문제한·거래중지 | 금융위 가상자산과·금감원 가상자산조사국 |
| **의심거래** (STR) | 특금법 §4 | 자금세탁·테러자금 차단 | 의심거래보고(STR), 거래거절, EDD | KoFIU |

**실무 사용**: "이상거래보고"는 어느 법에도 없는 말이다. STR은 "의심거래보고", §12는 "이상거래 통보", FDS는 "임시조치"로 쓴다.

### PEP vs BO

| 용어 | 의미 |
|---|---|
| **PEP (Politically Exposed Person)** | 정치적 주요인물. 고위 공직자·가족·측근. 부패 위험 ↑ |
| **BO (Beneficial Owner)** | 실소유자. 법인 소유권의 실제 최종 수익자 (보통 25%+). |

### 동일 용어·다른 표기 (한 문서 내 일관성 필요)

- FATF R.15 / FATF Recommendation 15 — 같은 의미. **긴 형태가 공식**.
- 특금법 / 특정금융정보법 / 특정 금융거래정보의 보고 및 이용 등에 관한 법률 — 법정 풀네임은 마지막, **첫 등장 시 풀네임 + 약칭 병기**.
- 가상자산이용자보호법 / 이용자보호법 — 같음. 공식은 "가상자산 이용자 보호 등에 관한 법률".

### 실무 포인트

회사 AML 정책 문서는 **영문판·국문판**을 따로 작성하는 경우가 많고, 용어 짝을 서로 매핑하는 **용어 대조표**를 첨부하는 게 표준. 감독 검사 시 용어 혼용으로 오해가 생기는 경우를 줄임.

---

## 한국어 → 영어 빠른 매핑

| 한국어 | 영어 |
|---|---|
| 자금세탁방지 | Anti-Money Laundering (AML) |
| 테러자금조달방지 | CFT |
| 고객확인 | KYC |
| 고객실사 | CDD |
| 강화된 고객실사 | EDD |
| 의심거래보고 | STR (Suspicious Transaction Report) |
| 이상거래 (가상자산이용자보호법 §12) | abnormal trading — 시장감시 대상 |
| 이상거래에 대한 감시 / 시장감시 | market surveillance |
| 이상금융거래 (FDS) | abnormal financial transaction |
| 이상금융거래탐지시스템 | Fraud Detection System (FDS) |
| 임시조치 (통신사기피해환급법 §2의5) | temporary measure (payment delay·suspension) |
| 지급정지 | payment suspension |
| 거래모니터링체계 | transaction monitoring (업계 용어 KYT) |
| 고액현금거래보고 | CTR |
| 가상자산사업자 | VASP |
| 실소유자 | Beneficial Owner |
| 정치적 주요인물 | PEP |
| 위험기반접근법 | RBA |
| 자금세탁방지 보고책임자 | AMLO |
| 금융정보분석원 | FIU (KoFIU) |
| 특금법 | 특정금융정보법 |
| 가상자산이용자보호법 | Virtual Asset User Protection Act |
| 트래블룰 | Travel Rule |
| 외부지갑 등록 | Unhosted Wallet Registration |
| 콜드월렛 | Cold Wallet |
| 분리보관 | Segregated Storage |
| 시세조종 | Market Manipulation |
| 미공개정보이용 | Insider Trading |
| 부정거래 | Fraudulent Practices |
| 제재 | Sanctions |
| 자산동결 | Asset Freeze |

---

## Top 15 핵심 용어 우선순위 (신입자용)

AML이 처음이면 **이 15개만 먼저 외우세요**. 나머지는 맥락에서 자연스럽게 익힙니다.

1. **AML / CFT** — 짝꿍
2. **KYC / KYT** — 사람 vs 거래
3. **CDD / EDD** — 표준 vs 강화
4. **STR** — 의심거래 보고
5. **VASP** — 가상자산사업자
6. **FATF / FIU** — 국제 표준 vs 한국 집행
7. **특금법 / 이용자보호법** — 한국 양대 법
8. **Travel Rule / IVMS101** — 송수신인 정보 동반
9. **OFAC / SDN** — 미국 제재
10. **PEP** — 정치적 주요인물
11. **RBA** — 위험기반접근법
12. **AMLO** — 자금세탁방지 보고책임자
13. **Mixer / Tornado Cash** — 익명화 도구
14. **Lazarus / DPRK** — 1순위 위협
15. **Tipping-off** — 절대 금지

## 더 읽을거리

- [`1-foundations/key-concepts.md`](1-foundations/key-concepts.md) — 핵심 개념 정리 (동심원·짝 비교표)
- [`4-technology/fds.md`](4-technology/fds.md) — FDS·시장감시·STR 세 제도의 경계
- [`../README.md`](../README.md) — 전체 학습 로드맵
