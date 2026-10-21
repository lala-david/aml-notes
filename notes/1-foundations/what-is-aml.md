# What is AML? — 자금세탁방지 기초

> 자금세탁(Money Laundering)이란 무엇이고, AML(Anti-Money Laundering)이 왜 존재하는가. 이 글을 읽고 나면 "자금세탁 3단계"가 머릿속 그림으로 남고, 왜 AML이 단순 금융규제가 아니라 **범죄 억제 인프라**인지 설명할 수 있게 됩니다. 마지막 업데이트: 2026-10-21.

## TL;DR
- **자금세탁(ML, Money Laundering)**: 범죄로 얻은 돈의 출처를 숨겨 합법적인 자금처럼 보이게 하는 행위
- **AML(Anti-Money Laundering)**: 그걸 막기 위한 법·제도·기술·운영의 총합. 짝꿍 개념으로 **CFT**(테러자금조달방지)가 있음
- 자금세탁은 전통적으로 **3단계 모델**: Placement → Layering → Integration
- 가상자산은 이 3단계가 다 **온체인에서** 일어날 수 있어서 추적은 쉬워졌지만 속도·규모가 폭증
- AML 의무의 큰 줄기: **고객을 알고(KYC) → 거래를 모니터링하고(KYT/TM) → 의심되면 신고(STR)**
- 가상자산 국제 기준의 뼈대는 **FATF R.15·INR.15**(2018-10 정의 신설, 2019-06 INR.15 채택). 가상자산 트래블룰의 원천은 R.16 본문이 아니라 **INR.15 §7(b)** 다

---

## 1. 자금세탁이 뭔가 — "왜 굳이 세탁하나"부터

### 핵심 아이디어

범죄로 번 돈은 당장 써도 문제입니다. 현금 다발을 들고 부동산을 계약하면 공인중개사가 의심 신고를 하고, 은행에 한 번에 10억을 입금하면 은행이 FIU(금융정보분석원)에 보고합니다. 그래서 범죄조직은 **"이 돈이 어디서 왔는지 모르게 만든 뒤, 합법적인 소득처럼 보이도록 포장하는 일"** 에 시간과 수수료를 쓰게 됩니다. 이게 자금세탁입니다.

용어 정의:
- **ML (Money Laundering)** — 자금세탁. 범죄수익의 출처를 은닉하고 합법성을 가장하는 일련의 과정.
- **AML (Anti-Money Laundering)** — 자금세탁방지. 그걸 탐지·차단하기 위한 법·제도·기술·운영 전체.
- **Predicate Offense (전제범죄)** — 자금세탁의 대상이 된 원범죄. 마약, 뇌물, 탈세, 해킹 등이 대표. 전제범죄가 없으면 자금세탁죄도 성립하지 않음.

### 자금세탁의 3가지 목적

범죄조직 관점에서 자금세탁의 목적은 단순합니다.

1. **출처(origin)를 숨긴다** — 돈이 마약 판매금인지 랜섬웨어 몸값인지 알 수 없게 한다.
2. **추적(trail)을 끊는다** — 자금 흐름이 수사기관 눈에 안 보이게 만든다.
3. **합법 경제에 통합(integration)한다** — 부동산·사업체·럭셔리 자산 형태로 "정상 소득"이 된다.

이 셋이 달성되면 범죄자는 번 돈을 마음대로 쓸 수 있고, 수사기관이 뒤늦게 발견해도 **몰수(asset forfeiture)가 어려워집니다**. 그래서 AML은 단순한 "금융 규제"가 아니라 **마약·조직범죄·테러·사이버범죄·대량살상무기 확산 그 자체를 억제하는 수단**으로 다뤄집니다. 이게 AML이 금융위·FSC가 아닌 **FIU**(Financial Intelligence Unit, 금융정보분석원) 같은 전담기구와 국가정보기관이 관여하는 이유입니다.

### 실무 포인트

AML 부서에서 일한다는 건 결국 "범죄수익이 우리 회사를 통과하지 못하게 막는 일"입니다. 그래서 AML 실무자는 금융지식 + 규제지식 + 수사적 감(조금 낯선 패턴을 놓치지 않는 본능)을 동시에 요구받습니다. 이 감각이 **거래 모니터링 룰을 설계**하는 출발점이 됩니다.

---

## 2. 고전적 3단계 모델 (Placement → Layering → Integration)

```mermaid
flowchart LR
    Dirty["💰 범죄수익<br/>(현금·가상자산)"] -->|Stage 1| P["📥 Placement<br/>금융시스템 진입"]
    P -->|Stage 2| L["🔀 Layering<br/>흐름 복잡화"]
    L -->|Stage 3| I["🏢 Integration<br/>합법 자산화"]

    P -.예시.-> PEX["smurfing · 카지노 · 거래소 입금"]
    L -.예시.-> LEX["mixer · bridge · peel chain · DEX"]
    I -.예시.-> IEX["부동산 · 사업체 · OTC 환전"]

    style Dirty fill:#f7f5ef,stroke:#c9a646
    style P fill:#e5eaf2,stroke:#1a2e4a
    style L fill:#e5eaf2,stroke:#1a2e4a
    style I fill:#e5eaf2,stroke:#1a2e4a
    style PEX fill:none,stroke:none
    style LEX fill:none,stroke:none
    style IEX fill:none,stroke:none
```

### 왜 3단계인가

AML 교육에서 관용적으로 쓰는 설명 틀입니다(모델의 최초 제안자·연도는 이 저장소 근거 자료로 확인하지 않았습니다 — 공개 근거 미확인). 실제 자금세탁은 단계가 뚜렷이 구분되지 않고 섞여 돌아가지만, 이 모델은 **"어디에 방어선을 칠지"** 설계하는 데 유용합니다.

용어:
- **FATF (Financial Action Task Force)** — 국제자금세탁방지기구. 권고안(Recommendation)을 발표하는 정부간 기구(1989년 설립은 배경 사실로만 언급 — 보고서 부록 B #1).
- **UNODC (UN Office on Drugs and Crime)** — UN 마약범죄국. 자금세탁 관련 통계·연구 발간.

### 한 줄 서사로 보는 3단계

마약상 A가 길거리에서 번 현금 10억을 부동산으로 바꿔 은퇴하려 합니다.

- **Stage 1 Placement (배치)** — A가 현금 10억을 100개 계좌에 100만원씩 나눠 입금(**structuring/smurfing**). 또는 현금→카지노칩→환전 전표로 바꾸기. 또는 현금→가상자산 거래소 입금.
- **Stage 2 Layering (은닉)** — A가 100개 계좌의 돈을 해외법인(쉘컴퍼니)으로 송금, 다시 3국을 거쳐 다른 법인으로 재송금. 가상자산이라면 mixer(믹서)를 거쳐 chain hopping(체인호핑)으로 Tron-USDT로 변환.
- **Stage 3 Integration (통합)** — A가 해외법인 명의로 서울 아파트를 매입. 이 아파트에서 나오는 임대소득은 이제 **"합법적 부동산 임대수익"** 으로 보입니다.

### Stage 1. Placement (배치)

**정의**: 더러운 돈을 금융 시스템에 **처음 집어넣는** 단계.

예:
- 현금다발을 여러 계좌에 분할 입금(**structuring/smurfing** — "스머프"들이 각자 소액씩 입금한다고 해서 붙은 이름)
- 카지노에서 현금 → 칩 → 체크 환전
- 현금 → 가상자산 거래소 입금 (P2P 또는 OTC)
- 실물 자산(금, 고가 시계, 미술품) 구매

이 단계가 **가장 위험하고 가장 탐지하기 쉬운** 구간입니다. 현금이 금융 시스템에 들어오는 순간 은행·거래소의 KYC(Know Your Customer, 고객확인)와 CTR(Currency Transaction Report, 고액현금거래보고) 규제와 맞닥뜨리기 때문. 그래서 AML 1차 방어선이 여기에 집중됩니다. 즉 "Placement를 포기시키면 나머지 단계는 의미가 없다"는 게 규제의 설계 철학입니다.

### Stage 2. Layering (은닉)

**정의**: 여러 번의 거래를 통해 돈의 흐름을 복잡하게 만들어 **추적을 끊는** 단계.

예:
- 여러 계좌·국가·법인 간 반복 송금
- 가상자산: **mixer**(Tornado Cash 등), **chain hopping**(BTC→ETH→Tron→BNB), **peel chain**(큰 금액을 계속 조금씩 떼어내 이전), DeFi swap, NFT wash trading

용어:
- **Mixer** — 여러 사용자의 자금을 섞어서 입출금 관계를 끊는 서비스.
- **Chain Hopping** — 서로 다른 블록체인 사이를 점프해 흔적을 흐리는 기법.
- **Peel Chain** — 큰 금액에서 소액을 떼어내(peel) 다른 주소로 보내고 나머지는 또 다른 주소로, 긴 사슬 패턴.

이 단계가 **가장 길고 창의적**입니다. 가상자산 환경에서는 layering 도구가 계속 바뀝니다. 연도별 "유행" 순위는 공개 근거가 없지만, 학계 측정은 몇 가지를 보여 줍니다. 크로스체인 추적은 휴리스틱에서 자동 매칭으로 넘어갔고(ABCTracer 12개 브리지 F1 91.75%, ConneX 5개 브리지 F1 0.9746 — 브리지 집합이 달라 직접 비교 불가)([arXiv 2504.01822](https://arxiv.org/abs/2504.01822); [arXiv 2511.01393](https://arxiv.org/abs/2511.01393)), Tornado Cash 제재 후 957일 동안 입금액은 71.03% 줄었지만 Ethereum 보안사고의 78.33%는 여전히 Tornado Cash를 거쳤습니다([arXiv 2507.11721](https://arxiv.org/abs/2507.11721)). **온체인 분석(blockchain analytics)** 도구가 주로 겨냥하는 구간이 바로 여기입니다.

### Stage 3. Integration (통합)

**정의**: 세탁된 돈이 **합법 자산으로 다시 등장**하는 단계.

예:
- 부동산 매입 (자금출처 증빙 모호하게)
- 럭셔리 자산 (요트, 시계, 미술품) 구매
- 합법 사업체 인수 → 매출 부풀리기
- 대출 상환 (가장한 대출 계약)
- 가상자산 → OTC desk → 법정화폐 → 사업 투자

이 시점에 잡히면 자산몰수가 **극도로 어렵습니다**. 왜냐하면 돈이 이미 "정당한 계약"과 "정당한 소유권" 옆에 붙어 있어서, 수사기관이 이를 몰수하려면 민사상 제3자 권리(선의취득자, 담보권자 등)를 건드려야 하기 때문. 그래서 AML 설계는 **"그 전 단계에서 막는다"** 에 집중합니다.

### 이 표를 어떻게 읽어야 하나

아래 표는 3단계를 **전통 금융 vs 가상자산** 관점에서 같은 행위가 어떻게 다른 도구로 나타나는지 대조합니다. 왼쪽이 익숙한 형태, 오른쪽이 가상자산 산업에서 보게 될 형태.

| 단계 | 전통 금융 도구 | 가상자산 도구 |
|---|---|---|
| Placement | 현금 분할입금, 카지노, 전신환, 차명계좌 | P2P/OTC 거래, 현금→거래소 입금, 선불카드→거래소 |
| Layering | 해외법인 송금, shell company, back-to-back loan | Mixer, cross-chain bridge, DEX swap, peel chain, NFT wash trade |
| Integration | 부동산, 사업체 인수, 가공매출 | OTC → 법정화폐 → 부동산, 스테이블코인 보유 후 글로벌 결제 |

### 실무 포인트

가상자산에서는 이 3단계가 **짧은 시간 안에 압축**될 수 있습니다. FATF 6차 Targeted Update(2025-06-26)는 DPRK의 **Bybit USD 14.6억 탈취(회수율 3.8%)** 를 헤드라인으로 올렸고([6차 TU](https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2025-Targeted-Upate-VA-VASPs.pdf.coredownload.pdf)), 7차 TU(2026-07-16)는 VASP가 "detect rapid transfer of VAs using transactions monitoring and blockchain analytics tools"해야 한다고 처음 권고했습니다(권고 6-ii)([7차 TU PDF](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf)). 이전 판의 "Bybit 48시간 내 $160M layering"은 출처가 없어 삭제했습니다. 업계가 쓰는 "KYT"라는 말 자체는 FATF·MAS·한국 고시 어디에도 나오지 않고, 규범 용어는 거래모니터링(transaction monitoring)입니다.

---

## 3. AML과 CFT의 관계 — 왜 짝꿍인가

### 세 약어의 차이

- **AML (Anti-Money Laundering)** — 자금세탁방지. **범죄수익 → 합법자산** 전환을 막는다.
- **CFT (Combating the Financing of Terrorism)** — 테러자금조달방지. **자금(합법이든 불법이든) → 테러조직**으로의 이동을 막는다.
- **CPF (Counter-Proliferation Financing)** — 대량살상무기 확산금융 차단. 주로 북한·이란 관련.

### ML과 TF는 방향이 정반대

여기가 혼동 지점입니다. ML은 "더러운 돈이 합법이 되는 과정"을 다루고 TF는 "합법 자금이 테러에 쓰이는 과정"을 다룹니다.

- **ML**: 더러운 돈 → (세탁) → 깨끗한 돈. 관심은 **출처**.
- **TF**: 깨끗한 돈이어도 → (이동) → 테러 자금. 관심은 **수취인/용도**.

그래서 TF는 **자금출처가 합법이어도** 차단 대상이 될 수 있습니다. 예를 들어 이슬라믹 스테이트(IS)가 자선단체를 가장해 정당한 기부금을 모은 뒤 무기 구매에 쓴다면, 그 기부금 자체는 범죄수익이 아니지만 CFT 위반이 됩니다. 이 차이가 **제재(sanctions) 스크리닝**을 실무의 핵심 통제로 만든 이유입니다 — 수취인 쪽 명단을 보는 일이기 때문.

용어:
- **Sanctions Screening (제재 스크리닝)** — 거래 당사자·지갑주소가 UN·미국 OFAC·EU·국내 제재대상자 명단에 해당하는지 대조.
- **OFAC (Office of Foreign Assets Control)** — 미국 재무부 해외자산통제국. 제재 대상을 지정·집행하는 권한 보유.
- **SDN List (Specially Designated Nationals List)** — OFAC가 발표하는 제재대상자 목록. 가상자산 주소가 실리는 경우도 있지만(예: 2025-03-21 삭제 전 Tornado Cash의 ETH 주소 90개), 2026-09-17 이란 거래소 BitBank 지정처럼 **주소 없이 지정되는 경우도 있다**([OFAC 2025-03-21](https://ofac.treasury.gov/recent-actions/20250321); [OFAC 2026-09-17](https://ofac.treasury.gov/recent-actions/20260917)).

### 실무 포인트

회사 AML 문서가 흔히 "AML/CFT" 또는 "AML/CFT/CPF"로 한 덩어리로 표기되는데, **운영 관점에서는 둘의 통제 지점이 다릅니다**. ML 통제는 "의심거래 탐지(STR)"에 집중하고, TF·CPF 통제는 "제재 명단 매칭(Sanctions Screening)"에 집중합니다. 거래 모니터링 룰을 설계할 때 이 둘을 섞지 말고, 별도 룰 세트로 관리하는 게 분석 품질에 유리합니다.

---

## 4. AML 의무의 큰 줄기 (어떤 회사든 비슷함)

### 개요

가상자산사업자(VASP, Virtual Asset Service Provider — 거래소·수탁·OTC 등)든 은행이든 결제사든, AML 의무의 뼈대는 거의 동일합니다. 관할(한국·미국·EU)에 따라 세부 조항과 금액 기준이 달라집니다. 이 9개는 어떤 AML 교재에서도 반복 등장하므로 순서째로 암기해두면 이후 규제 문서를 읽을 때 뼈대가 됩니다.

### 9개 의무 (가상자산 기준 Travel Rule 포함 시 10개)

1. **신고·등록(Licensing)** — 당국에 사업자 등록. 한국은 FIU 신고, 미국은 FinCEN MSB 등록, EU는 MiCA CASP 라이선스.
2. **고객확인(KYC/CDD)** — 누구와 거래하는지 확인. 신분증, 주소, 거래목적. 한국 근거는 특금법 §5의2.
3. **위험기반접근(RBA, Risk-Based Approach)** — 고객·상품·지역별 위험등급을 매기고 그에 비례해 통제 강도 조정. 저위험은 간소하게, 고위험은 두껍게.
4. **강화실사(EDD, Enhanced Due Diligence)** — 고위험(PEP, 고위험국, 비대면+기타 위험요소) 고객에 추가 확인. 자금원천 증빙이 핵심.
5. **거래모니터링(TM/KYT)** — 비정상 거래 패턴 탐지. 전통 금융은 TM(Transaction Monitoring), 가상자산은 KYT(Know Your Transaction)로 부름.
6. **제재 스크리닝(Sanctions Screening)** — 고객·카운터파티·지갑주소가 제재 대상인지 실시간 대조.
7. **의심거래보고(STR/SAR)** — 의심되면 FIU에 보고. STR(Suspicious Transaction Report, 한국·FATF 용어), SAR(Suspicious Activity Report, 미국 FinCEN 용어). 한국 근거는 특금법 §4(금액 기준 없음), 고액현금거래보고(CTR)는 §4의2.
8. **기록보관(Record Keeping)** — 한국은 특금법상 고객확인 자료·거래 기록 보존과 별도로, 가상자산이용자보호법 시행령 §13이 상시감시·조치 결과와 통보·신고·보고 기록을 보존 대상 가상자산거래기록에 넣습니다. 두 법의 대상·기간이 다르므로 각 기간은 법령 원문으로 확인하고, 겹치면 긴 쪽을 따릅니다([`../2-regulations/korea-fiu-act.md`](../2-regulations/korea-fiu-act.md) §4).
9. **내부통제(Internal Controls)** — AML 책임자(AMLO/MLRO) 임명, 정책·절차 문서화, 임직원 교육, 내부감사.

**가상자산 추가 10번째**:

10. **Travel Rule (FATF INR.15 §7(b))** — VASP 간 이전 시 송수신인 정보 동반. 관할마다 금액 구조가 다릅니다. 한국은 특금법 §5의3·시행령 §10의10 「100만원 이상」(2027-02-18까지) → **2027-02-19부터 기준금액 없이 전건**(대통령령 제36592호 2026-08-18 공포, enacted-not-in-force), 미국은 31 CFR 1010.410(f) "$3,000 or more", EU TFR은 **금액 기준 없이 전건**(EUR 1,000 이상 자기수탁 이전에는 소유·통제 검증)입니다. 상세는 [`../3-crypto-aml/travel-rule.md`](../3-crypto-aml/travel-rule.md).

용어:
- **PEP (Politically Exposed Person)** — 정치적 주요인물. 고위 공직자·그 가족·측근. 부패 위험이 구조적으로 높아 강화된 고객확인(EDD) 대상.
- **Travel Rule** — 전신송금 정보 동반 원칙(R.16)을 VASP에 적용한 것. 법적 원천은 2019-06 신설된 INR.15 §7(b)이고, 2021 가이던스 para 178은 "Recommendation 16 applies in an amended way to VAs as set out in paragraph 7(b) of INR.15"라고 정리합니다([FATF 2021 RBA 가이던스](https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf.coredownload.pdf)).

### 실무 포인트

AML 프로그램이 갖춰졌는지 점검할 때는 이 10개를 체크리스트로 만들어 각각에 **담당자·시스템·근거 조문·증빙**이 있는지 본다. 이 중 어느 하나라도 "사람만 있고 시스템이 없다"면 규제 검사에서 지적 대상입니다.

---

## 5. 누가 만든 룰을 따르는가 — 글로벌 거버넌스 지도

### FATF → 국내법의 구조

```mermaid
flowchart TB
    F["🌍 FATF<br/>40 Recommendations<br/>(국제 표준)"]
    F -->|권고 → 국내법화| KR["🇰🇷 한국<br/>특금법 · 이용자보호법<br/>통신사기피해환급법"]
    F -->|권고 → 국내법화| US["🇺🇸 미국<br/>BSA · PATRIOT Act"]
    F -->|권고 → 국내법화| EU["🇪🇺 EU<br/>MiCA · AMLR · TFR"]
    F -->|권고 → 국내법화| JP["🇯🇵 일본 · 싱가포르 · 홍콩"]

    KR --> KRS["감독: FIU · FSC · FSS"]
    US --> USS["감독·집행: FinCEN · OFAC"]
    EU --> EUS["AMLA · EBA · ESMA · 회원국 당국"]

    F -.평가.-> ME["Mutual Evaluation<br/>Grey/Black List"]

    style F fill:#1a2e4a,stroke:#1a2e4a,color:#fff
    style ME fill:#fff7d6,stroke:#c9a646
    style KR fill:#e5eaf2,stroke:#1a2e4a
    style US fill:#e5eaf2,stroke:#1a2e4a
    style EU fill:#e5eaf2,stroke:#1a2e4a
    style JP fill:#e5eaf2,stroke:#1a2e4a
```

### FATF는 법을 만들지 않는다

중요한 오해 하나를 먼저 풀면, **FATF는 국제법을 만드는 기구가 아닙니다**. FATF가 하는 일은 권고안(Recommendation, 40개)을 발표하고, 회원국이 이를 국내법으로 얼마나 잘 이행했는지 주기적으로 **상호평가(Mutual Evaluation, ME)** 하는 것입니다.

그러면 왜 각국이 FATF 권고를 열심히 따르는가? **제재보다 무서운 게 평판이기 때문**입니다. 상호평가에서 낮은 점수를 받으면 FATF는 그 나라를 **Grey List**(강화 모니터링) 또는 **Black List**(Call for Action)에 올릴 수 있고, 그러면:

- 외국 은행이 그 나라 금융기관과의 **코르레스(correspondent) 관계**를 끊거나 제한
- 국가 신용등급 강등, 자본 유출
- 외국인 투자 기피

등재가 특정 국가 경제에 준 영향의 수치는 이 저장소 근거 범위 밖입니다. 다만 각국 금융기관이 명단을 위험평가 입력으로 쓰기 때문에 해당 관할과의 거래에 강화 실사가 붙습니다. 2026-06-17~19 총회에서 보스니아헤르체고비나·이라크가 회색명단에 들어가고 알제리·나미비아가 빠져, 2026-10-21 기준 회색명단은 22개 관할입니다(B)([FATF 2026-06 총회 결과](https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-june-2026.html)). 다음 총회는 2026-10-26~30 예정입니다([FATF 일정표](https://www.fatf-gafi.org/en/calendars/events.html)).

### 가상자산에 대한 결정적 권고 2개

가상자산 산업이 FATF 권고를 체감하는 지점은 거의 이 둘로 압축됩니다.

- **FATF Recommendation 15(New technologies) + INR.15 — VASP에 AML/CFT 의무 부과.** 2018-10 R.15 개정으로 VA·VASP 정의가 용어집에 신설됐고, 2019-06 INR.15와 RBA 가이던스 초판이 채택됐습니다. 2021-10-28 개정 가이던스가 2019 초판을 대체합니다.
- **트래블룰 — INR.15 §7(b).** VASP 간 이전 시 송수신인 정보 동반 의무. 문언에 금액 기준이 없고, USD/EUR 1,000은 바로 앞 §7(a)의 임시거래 CDD 기준입니다. **R.16은 2025-06 개정**됐지만 FATF는 VASP를 R.16에 직접 넣지 않고 R.15를 거쳐 간접 적용하며(설명서 para 54), 이행 기대시한은 2030년 말입니다(para 59)([R.16 개정 설명서](https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Explanatory%20note%20for%20revised%20R.16.pdf.coredownload.pdf)).

이 기준은 한국 특금법 개정(2020-03-24 개정, 2021-03-25 시행)과 EU MiCA·TFR(2024-12-30 적용)의 배경이 됐습니다. 두 권고의 정확한 문언을 아는 것은 이후 모든 국가별 규제 학습의 출발점입니다. 자세한 내용은 [`../2-regulations/fatf.md`](../2-regulations/fatf.md) 참조.

### 실무 포인트

AML 정책 문서 맨 앞에 "본 정책은 FATF R.10·R.15(INR.15)·R.16 및 특금법 §4(STR)·§4의2(CTR)·§5의2(고객확인)·§5의3(트래블룰)에 근거한다"고 명시하면, 규제 검사관이 문서 구조를 이해하기 쉬워지고 내부 교육 자료에서도 "이 룰이 왜 있는가"를 거슬러 올라가 설명할 수 있습니다. 법적 근거 추적성(traceability)을 문서에 내재화하는 게 성숙한 AML 프로그램의 표식입니다.

---

## 요약 부록 — 빠른 참조용

**3단계 모델**: Placement → Layering → Integration (전통·가상자산 공통 틀)
**AML 9대 의무**: 신고 · KYC/CDD · RBA · EDD · TM/KYT · 제재 스크리닝 · STR · 기록보관 · 내부통제 (+ 가상자산 Travel Rule)
**글로벌 구조**: FATF 권고 → 각국 국내법 → 감독기관 집행 → Mutual Evaluation 피드백 루프

### 가상자산 AML 국제 기준 연대기

```mermaid
timeline
    title FATF 가상자산 기준 — 원문으로 확인되는 이정표
    2014-06 : Virtual Currencies Key Definitions 보고서
    2018-10 : R.15 개정 — VA·VASP 정의 신설
    2019-06 : INR.15 채택 — §7b 가상자산 트래블룰
    2020-09-14 : Red Flag Indicators 58개 지표
    2021-10-28 : 개정 RBA 가이던스
    2025-06 : R.16 개정 — VASP는 R.15 경유
    2026-07-16 : 7차 Targeted Update
```

출처: [보고서 연대기 표](../../reports/가상자산%20AML%20KYT%20FDS%20트래블룰%20흐름.md), [FATF Red Flag](https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets-red-flag-indicators.html), [7차 TU PDF](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/7th-targeted-update-on-implementation-fatf-standards-vas-vasps-2026.pdf.coredownload.pdf).

## 💼 실무 현장 (Industry Reality)

> 이전 판의 거래소별 조직 인원·컴플라이언스 비율, 연봉, 분석가 1인당 처리량, 거래소별 벤더·사내 시스템명(예: "Lynx", "Sombrero"), Binance·OKX 합의 금액과 모니터십 조건, DAXA 공동 블랙리스트, 본인확인기관 점유 서술은 이 저장소 근거 자료로 확인되지 않아 삭제했습니다(공개 근거 미확인 — [`../6-cases/major-enforcement.md`](../6-cases/major-enforcement.md) 기준과 같음).

### 조직 — 법이 요구하는 것과 확인되지 않는 것

- **보고책임자(AMLO)**: 특금법상 VASP는 보고책임자를 두고, 변경 시 신고합니다. 2026-08-20 이후 대주주 변경은 "30일 전 사전신고" 대상입니다([금융위 2026-08-13 신고매뉴얼](https://www.fsc.go.kr/no010101/87521)).
- **AML 인력**: 2026-08-13 전면 개정된 신고매뉴얼은 **AML 인력 4인 이상**과 전산설비 국내 소재(클라우드 국내 리전 인정)를 정했습니다([금융위 2026-08-13](https://www.fsc.go.kr/no010101/87521)). 개별 거래소의 실제 인원·조직 구조는 공개 근거가 없습니다.
- **글로벌 거래소 조직·보수 수준**: 공개 근거 미확인.

### AML 실무에서 매일 다루는 워크플로

```mermaid
flowchart LR
    U[사용자 거래] --> K["거래모니터링<br/>룰 + 블록체인 분석도구"]
    K -->|알림| Q[알림 큐]
    Q --> A[분석가 1차 검토]
    A -->|오탐| C["종결 · 사유 기록"]
    A -->|의심| I[조사]
    I --> E[EDD · 자금원천 확인]
    E -->|의심 해소 안 됨| S[STR 작성]
    S --> L[보고책임자 결재]
    L --> F["FIU 제출<br/>특금법 §4"]
    style K fill:#dbeafe
    style S fill:#fee2e2
    style F fill:#d1fae5
```

FATF 2021 가이던스 para 275~276은 "automated systems may be the only realistic method of monitoring transactions, and flagged transactions should go through human/expert analysis"라고 해 자동화와 사람의 검토를 함께 요구합니다([FATF 2021 가이던스 미러](https://www.onpcsb.ro/2022/01042022/Updated-Guidance-VA-VASP.pdf)). 알림 중 오탐 비율이나 STR 전환율에 대한 **가상자산 전용 공개 벤치마크는 없습니다**. 은행권 자료(EY 2018, 리테일 평균 14%)만 있습니다(B)([EY 2018](https://ey.com/content/dam/ey-unified-site/ey-com/en-uk/industries/financial-services/documents/ey-anti-money-laundering-transaction-monitoring-2018-emeia-survey.pdf)). 이전 판의 "80% 오탐, STR 전환 1~5%"는 근거가 없어 삭제했습니다.

### 한국 "이상거래"는 세 갈래다

같은 "이상" 신호라도 법적 출구가 다릅니다. ① 전자금융 FDS·보이스피싱 임시조치(통신사기피해환급법, 거래소 2026-10-01~) ② 가상자산이용자보호법 §12 불공정거래 상시감시 ③ 특금법 §4 의심거래보고(STR). 셋을 섞으면 탐지는 했는데 틀린 출구로 보내는 "분류 실패"가 생깁니다([`../4-technology/fds.md`](../4-technology/fds.md)).

### 자주 나오는 오해

- **"AML은 법무 업무"** — 법적 지식과 데이터 엔지니어링 역량이 동시에 필요합니다. 조직상 위치는 회사마다 다릅니다.
- **"룰만 많이 쌓으면 된다"** — FATF 2021 가이던스는 운영 룰의 무결성을 "regular basis"로 검증하라고 합니다. 룰 수보다 검증된 룰이 중요합니다.
- **"STR 많이 내면 잘하는 것"** — STR은 "의심되는" 경우의 보고이고, 판단 근거가 기록돼 있어야 합니다. 상세는 [`../5-compliance/str-ctr.md`](../5-compliance/str-ctr.md).
- **"트래블룰 위반으로 거래소가 제재받았다"** — 2024-01-01~2026-10-21 어느 관할에서도 트래블룰 위반을 독립 제재 사유로 명시한 사건은 확인되지 않았습니다. 두나무 과태료 352억원(2025-11-06)의 사유도 고객확인·거래제한·의심거래보고 위반이었습니다([FIU 보도자료 KDI 미러](https://eiec.kdi.re.kr/policy/materialView.do?num=273166)).

---

## 더 읽을거리
- [`why-crypto-different.md`](why-crypto-different.md) — 왜 가상자산 AML은 다른가
- [`key-concepts.md`](key-concepts.md) — KYC/KYT/CDD/EDD/STR/CTR 정의 상세
- [`../2-regulations/fatf.md`](../2-regulations/fatf.md) — FATF 권고안 R.15/R.16 deep
- [FATF — Money Laundering](https://www.fatf-gafi.org/en/topics/money-laundering)
- [UNODC — Money Laundering Overview](https://www.unodc.org/unodc/en/money-laundering/overview.html)
