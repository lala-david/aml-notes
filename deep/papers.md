# 학술 논문 큐레이션

> AML·온체인 분석의 **학술 기반**. 이 글은 "어떤 논문을 읽어야 하나"의 큐레이션이며, 각 논문이 왜 **산업 표준에 영향**을 미쳤는지까지 설명합니다. 마지막 업데이트: 2026-04-17.

## 이 큐레이션을 읽기 전에

Chainalysis·Elliptic·TRM 같은 회사의 알고리즘은 대부분 **학계에서 시작**됐습니다. 2013~2019년의 Bitcoin clustering 논문들이 먼저 나왔고, 이후 산업이 이를 **상용화·확장**한 구조. 그래서 "왜 이 알고리즘이 이렇게 설계됐나"를 이해하려면 학술 논문을 읽는 게 지름길. 이 페이지는 그중 **실무 임팩트가 컸던 논문**만 추렸습니다.

---

## 1. Bitcoin Clustering / De-anonymization (필독)

### Meiklejohn et al. (2013) — "A Fistful of Bitcoins"

- 비트코인 클러스터링의 **고전**
- Common Input Ownership 휴리스틱 + 거래소 attribution 첫 학술적 검증
- 검색: ACM IMC 2013

**왜 중요한가**: 이 논문이 CIOH를 학계 차원에서 입증하면서 블록체인 분석이라는 산업의 **지적 기반**이 됐습니다. Chainalysis의 창업 철학이 이 논문의 연장선.

### Reid & Harrigan (2013) — "An Analysis of Anonymity in the Bitcoin System"

- 비트코인 익명성의 한계 첫 분석
- WikiLeaks·실크로드 사례 분석

**왜 중요한가**: "공개 원장에서의 프라이버시 한계"를 실제 사례로 처음 보여줌. 현대 KYT 산업이 "pseudonymity는 anonymity가 아니다"라는 공통 전제를 이 논문에서 얻었습니다.

### Androulaki et al. (2013) — "Evaluating User Privacy in Bitcoin"

- 사용자 행동 분석으로 식별 가능성 측정
- ESORICS 2013

### Heuristic-Based Address Clustering in Bitcoin (2020)

- 5가지 휴리스틱 비교 평가
- [ResearchGate](https://www.researchgate.net/publication/347083664_Heuristic-Based_Address_Clustering_in_Bitcoin)

**왜 중요한가**: 2013년 이후 발전한 다양한 휴리스틱을 한 곳에서 비교 평가. 실무자가 "우리가 쓰는 휴리스틱이 얼마나 정확한가"를 판단할 때 참조 기준.

### Möser et al. — "An Inquiry into Money Laundering Tools in the Bitcoin Ecosystem"

- 다크넷 + mixer 자금세탁 측정
- eCrime 2013 (APWG)

---

## 2. CoinJoin / Privacy Tools

### Maxwell — "CoinJoin: Bitcoin privacy for the real world" (2013)

- CoinJoin **원형 제안** (Bitcointalk 글)

**왜 중요한가**: 학술 논문은 아니지만 Wasabi·Samourai·JoinMarket의 설계 원형. 개발자 포럼 글이 산업 표준이 된 희귀 사례.

### Möser & Böhme — "Anonymous Alone? Measuring Bitcoin's Second-Generation Anonymization Techniques" (2017)

- Wasabi·JoinMarket 효과성 측정

### Kappos et al. — "An Empirical Analysis of Anonymity in Zcash" (2018)

- Zcash shielded transaction 사용 패턴 분석
- USENIX Security 2018

**왜 중요한가**: 프라이버시 코인의 실제 익명성을 **실증 데이터**로 측정. "Zcash shielded는 쓰는 사람이 적어서 오히려 식별되기 쉽다"는 반직관적 결론이 대중 담론을 바꿈.

### Möser et al. — "An Empirical Analysis of Traceability in the Monero Blockchain" (2018)

- Monero가 100% 추적 불가능하지 않음 (ring signature 패턴 누설)

**왜 중요한가**: Monero도 **부분 추적 가능**하다는 것을 학술적으로 입증. Chainalysis의 2020 Monero 분석 도구의 학술적 근거.

---

## 3. Travel Rule / Compliance Tech

### Notabene · 21 Analytics 화이트페이퍼

- IVMS101 표준화 과정
- 검색: IVMS101 white paper

### Wolfsberg Group Crypto Statement

- 글로벌 은행 모범사례

**왜 중요한가**: Wolfsberg는 HSBC·Citi·JPMorgan 같은 글로벌 대형 은행이 AML 모범사례를 합의하는 그룹. 이들이 가상자산에 대해 내놓는 입장이 **은행이 VASP와 어떻게 관계 맺을지**를 결정합니다.

---

## 4. ML · AI in AML

### Weber et al. — "Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics" (2019)

- Elliptic 데이터셋 + GCN
- ML 기반 자금세탁 분류 **첫 영향력 논문**

**왜 중요한가**: **Elliptic dataset** (라벨된 20만+ 트랜잭션 그래프)을 학계에 공개하면서 ML 기반 AML 연구의 폭발적 확산을 촉발. 이후 대부분 AML ML 논문이 이 데이터셋을 벤치마크로 사용.

### Lorenz et al. — "Machine learning methods to detect money laundering in the Bitcoin blockchain" (2020)

- 다양한 ML 알고리즘 비교 (Random Forest, Neural Network 등)

### Bellei et al. — "The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset" (2024)

- 최신 GNN 접근

**왜 중요한가**: Elliptic2 데이터셋 (Elliptic의 후속) 공개 + Subgraph 기반 학습 기법. 2024년 이후 AML ML 연구의 state-of-the-art 기준점.

### Elliptic2 Dataset (2024)

- 최신 라벨 데이터셋 (학계 공유)
- ML 연구의 표준 벤치마크

---

## 5. Cross-chain · DeFi

### "Cross-chain bridges: Hacks, Vulnerabilities" (다수 보고서)

- 검색: cross-chain bridge security analysis

### "Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets" (St. Louis Fed, 2021)

- DeFi 전반 학술적 정리

**왜 중요한가**: **연준(Fed)이 DeFi를 학술적으로 분석**한 첫 주요 문헌. 규제당국의 DeFi 이해가 어떻게 시작됐는지 보여주는 사료.

### "An Empirical Study of DeFi Liquidations" (Qin et al., 2021)

- DeFi 청산 경제학

---

## 6. ZKP · Privacy-Preserving Identity

### Goldwasser et al. (1989) — "The Knowledge Complexity of Interactive Proof Systems"

- ZKP **원전**

**왜 중요한가**: Zero-Knowledge Proof 개념이 처음 제안된 논문. 1989년 이론이 2020년대 들어 Zcash·Tornado Cash·zk-KYC로 실용화되기까지의 긴 여정을 이해하는 출발점.

### Ben-Sasson et al. — "Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture"

- zk-SNARK

### Polygon ID, Worldcoin 등 산업 화이트페이퍼

**왜 중요한가**: 학술적 ZKP를 **identity·KYC에 응용**한 최초 대규모 시도들. "프라이버시 + 컴플라이언스 양립"이라는 장기 방향의 실무적 구현.

---

## 7. 한국 관련 학술

### 한국 가상자산 AML 관련 논문 (대학원 + 법학)

- 한국학술정보(KISS), DBpia, RISS 검색
- "특금법 가상자산", "Travel Rule 한국", "FATF Korea"
- 「한국법학회」「한국금융법학회」 저널

### 실무 포인트

한국 학술 논문은 **법학 중심**(특금법 해석·개정 방향 분석)이고 **기술 중심 논문은 드뭅니다**. 법무법인 인사이트와 결합해 읽으면 한국 규제 방향 예측에 유용.

---

## 8. 주요 컨퍼런스 · 저널

### 보안·시스템

- USENIX Security
- ACM CCS
- IEEE S&P (Oakland)
- NDSS
- Financial Cryptography (FC)

### 핀테크·AML 특화

- Journal of Money Laundering Control
- Crime, Law and Social Change
- Money Laundering Compliance

### 한국

- 한국법학회
- 한국금융법학회
- 디지털산업정책연구원

### 실무 포인트

보안·시스템 계열 Top 학회(USENIX·CCS·S&P)에 올라간 논문이 보통 **가장 임팩트 크고 산업 수용 빠름**. Financial Cryptography는 가상자산 특화 학회.

---

## 9. 검색 사이트

- [Google Scholar](https://scholar.google.com/)
- [arXiv (cs.CR)](https://arxiv.org/list/cs.CR/recent)
- [SSRN](https://www.ssrn.com/)
- [ResearchGate](https://www.researchgate.net/)
- [DBLP](https://dblp.org/)
- 한국: [RISS](http://www.riss.kr/), [DBpia](https://www.dbpia.co.kr/), [KISS](http://kiss.kstudy.com/)

### 실무 포인트

Google Scholar에서 논문을 찾을 때 **"Cited by"** 수치가 영향력의 가늠자. 1,000회 이상이면 산업 표준으로 수용된 논문일 가능성 높음.

---

## 10. 추천 읽기 순서 (입문자)

1. Meiklejohn 2013 (Bitcoin clustering 고전) — Day 54
2. Möser 2013 (mixer + 다크넷)
3. Weber 2019 (ML + Elliptic)
4. Bellei 2024 (최신 GNN)
5. ZKP 입문 1편

### 실무 포인트

위 5편을 월 1편씩 정독하면 **5개월**에 AML 분석 기술사 흐름이 머리에 잡힙니다. 각 논문의 저자·인용 논문을 따라가면 자연스럽게 관련 연구로 확장됩니다.

---

## 💼 실무 현장 (Industry Reality)

### 이 논문들을 실무에서 어떻게 쓰나

학술 논문이 **실제 프로덕션 코드로 이식되는 경로**는 세 가지입니다.

- **Meiklejohn 2013 → Chainalysis·TRM 클러스터링 엔진**: CIOH(Common Input Ownership Heuristic)는 현재 모든 KYT 벤더의 기본 휴리스틱. 자체 클러스터링을 시도하는 엔지니어는 이 논문 + Heuristic-Based Clustering(2020)을 반드시 읽고 시작.
- **Weber 2019 → Elliptic 데이터셋 기반 ML 모델**: Coinbase "Lynx"(2024) · TRM Labs 내부 ML · 한국 Upbit 자체 XGBoost 모델이 모두 이 논문 계보. Elliptic 데이터셋으로 벤치마크하는 게 **면접 실무 과제** 단골 주제.
- **Möser 2013 → mixer 탐지 룰**: CMLN(Crypto Money Laundering Network) 개념의 학술 원전. Chainalysis Reactor의 mixer 카테고리 설계가 이 연장선.

### 한국 VASP AMLO는 무엇을 보나

한국 AMLO는 학술 논문을 **일상적으로는 읽지 않습니다**. 다만 다음 시점에 특정 논문이 필요:

- **벤더 평가·RFP 작성**: Chainalysis·TRM·Elliptic 기술 검증 시 "CIOH·change address heuristic 구현 수준"을 질문해야 함. Meiklejohn 원전을 읽어본 AMLO가 유리.
- **금융위·FIU 질의 대응**: 감독당국이 "귀사는 mixer 노출을 어떻게 측정하는가"라고 물을 때, 학술 근거(Möser 2013 · Elliptic 2024 dataset)를 인용하면 설득력 급상승.
- **STR 이의제기 대응**: 고객이 "내 거래는 mixer와 무관"이라고 주장할 때, 학술 방법론(휴리스틱 신뢰도·통계적 유의성) 설명 가능 여부가 법적 방어력 차이를 만듦.

### 글로벌 컴플팀은 어떻게 소화하나

- **Coinbase Research**: 전담 리서치팀(~10명) 보유. Elliptic2 dataset · Bellei 2024 GNN 논문을 곧바로 자체 "Lynx" 엔진에 반영해 2024 블로그 발표
- **Chainalysis·TRM·Elliptic**: 주요 논문 저자가 자사 Chief Scientist·Research Head로 영입되는 경우 다수. Meiklejohn 본인이 UCL 교수지만 Chainalysis 고문 역할
- **ACAMS 커뮤니티**: 학술 논문을 **실무 언어로 번역**한 white paper·블로그 다수. 원전 읽기 어려우면 ACAMS Today Magazine 요약으로 대체 가능

### 자주 나오는 오해

- **"논문 = 학계 일"** — Chainalysis·TRM·Elliptic의 R&D 상당 부분이 학술 논문 출판 병행. 특히 USENIX Security·CCS 논문은 **벤더 영업 자료로 사용**됨.
- **"Monero는 완전 추적 불가"** — Möser 2018 논문이 **부분 추적 가능**을 실증. Chainalysis 2020부터 Monero 추적 도구 상용화. 프라이버시 코인 관련 "절대"라는 표현은 학술적으로 틀림.
- **"ML이 있으면 룰이 필요 없다"** — Weber 2019 이후 10년간 ML 기반 AML 연구가 활발했지만, 감독당국이 요구하는 **"해석 가능한 근거"** 때문에 여전히 **룰이 주, ML은 보조**. 학술 연구와 실무 배포 사이의 구조적 격차.

### 실무자가 이 영역을 따라잡는 루틴

- **월 1편 정독** — 위 추천 읽기 순서(10장) 5편을 5개월에 소화
- **Google Scholar Alert 등록** — "Bitcoin clustering", "cryptocurrency money laundering", "blockchain anti-money laundering" 키워드. 신규 논문 자동 이메일
- **컨퍼런스 논문집 훑기** — 매년 USENIX Security·CCS·Financial Cryptography proceedings의 abstract만 읽기(반일)
- **저자 Twitter 팔로우** — Meiklejohn(@sarahjamielewis 별개 인물 주의) · Narayanan · Böhme · Elliptic Research 계정
- **Notion·Zotero에 한줄 요약** — 읽은 논문 5단계 속독 결과(추상·결론·방법·관련연구·메모)를 축적. 2~3년 후 자체 지식 그래프가 됨

---

## 더 읽을거리

- [`reports.md`](reports.md) — 산업 리포트
- [`conferences.md`](conferences.md) — 컨퍼런스 영상
- [`links.md`](links.md) — 참고 링크 모음
