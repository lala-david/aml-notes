---
dossier_id: academic-literature-2026-10
title: 가상자산 AML·KYT·FDS·트래블룰 학술 문헌조사 (2025-01-01 ~ 2026-10-21) — 주제별 주석 서지
domain: technology
as_of: 2026-10-21
coverage: 가상자산 AML 탐지 ML/GNN · 주소 클러스터링·비익명화 · 거래 모니터링·LLM · 트래블룰·PET · 사기·FDS · 규제·법·경제학 · 데이터셋·서베이 · 기관 보고서 방법론 (관할 중립; 한국 문헌은 접근 가능 범위 내)
confidence_overall: B
sources_total: 72
---

> **읽기 전 주의**
> 1. 이 문서의 모든 수치는 **해당 논문의 arXiv 초록 페이지·출판사 초록 페이지·기관 보고서 원문을 2026-10-21에 직접 열어 확인한 것**만 적었다. 초록을 열지 못한 문헌은 §7에 제목만 둔다. 이 저장소는 과거 「인용 수치가 원논문에 없었다」(`kb/facts/contradictions.jsonl` CTR:00007) 오류를 겪었으므로, 본문·초록에 없는 수치는 한 건도 쓰지 않았다.
> 2. 초록에 수치가 없는 논문은 "초록에 수치 없음"이라고 명시했다. 이는 결과가 없다는 뜻이 아니라 **초록만으로는 확인 불가**라는 뜻이다.
> 3. 2025-01-01 이전 문헌은 **[맥락]** 표시를 붙였고, 비교·정정 목적(§8)으로만 포함했다.
> 4. 조사 도중 세션의 웹 검색 할당량이 소진되어(2026-10-21 중반) 이후는 직접 URL 열람(WebFetch)만으로 진행했다. 그 영향으로 **한국 법학 학술지 2025년 논문**과 **한국은행·KDI 보고서**는 접근 가능한 경로에서 확보하지 못했다(§3, §7 참조).
> 5. 특정 발주사·자사 언급 없음. 벤더·분석업체 명칭은 문헌 인용에 필요한 범위에서만 등장한다.

---

## 1. BLUF — 2025~2026 연구 동향 핵심

- **"노드 분류"에서 "서브그래프·경로·의도 추적"으로 문제 정의가 이동했다.** Elliptic2(2024, [맥락] P-063)가 자금세탁을 서브그래프 분류 문제로 재정의한 뒤, 2025~2026년에는 송·수신 종단을 추적하는 RevTrack(P-014), DeFi 거래의 의미 단위(DSU)를 LLM으로 해석해 자금을 좇는 AMLGuard(P-008), 라인그래프로 자금 흐름 자체를 노드화하는 LineMVGNN(P-003)이 등장했다. [P-003][P-008][P-014]
- **크로스체인 추적이 "휴리스틱"에서 "자동 매칭 시스템"으로 성숙했다.** 12개 브리지에서 양방향 추적 F1 91.75%(ABCTracer, P-006), 5개 브리지 약 50만 건에서 F1 0.9746(ConneX, P-007), Ethereum–Polygon 브리지에서 입금 93~99.65%·출금 67.55~92.78% 매칭(P-016)이 보고됐다. 단, 브리지 집합·정의가 달라 **수치 간 직접 비교는 불가**하다. [P-006][P-007][P-016]
- **프라이버시 프로토콜 평가의 단위가 "깨졌다/안전하다"에서 "익명성 집합 축소율·비트 손실"로 바뀌었다.** Railgun 출금 17.65%가 입금과 유일 연결, 중위 익명성 손실 3.42비트(P-017); Railgun·Hinkal 186,356건 분석에서 공개 토큰 제약만으로 평균 익명성 집합 40.1~59.0% 축소(P-018). Tornado Cash 클러스터링 논문(P-019)은 **저자 철회**됐으므로 수치 인용 금지. [P-017][P-018][P-019]
- **믹서 계정 연결(mixing address association)이 라벨 부족·노이즈 라벨 대응 기법과 결합됐다.** 10-shot 환경 F1 96.98%(StealthLink, P-022), 고·저주파 그래프 대조학습(HiLoMix, AAAI 2026, P-021), 그래프 구조 학습 기반 LASC(IEEE TDSC 2026, P-020). [P-020][P-021][P-022]
- **LLM의 AML 투입은 "STR 초안·알람 트리아지"에 집중되나, 평가는 전부 합성 데이터다.** 다중 에이전트 SAR 초안(P-025), 근거 인용·반사실 점검을 강제한 트리아지(인용 유효성 0.98 vs Escalate F1 0.62, P-026), 규제 조항 연결 설명(P-027), k-hop 서브그래프 텍스트화(P-028). 가상자산 원천 STR 코퍼스로 평가한 연구는 **없다**. [P-025][P-026][P-027][P-028]
- **트래블룰 연구는 암호학적 설계(PET·ZK·SSI)와 TRISA 보안성에 머물고, 실증 경제학은 공백이다.** PET 평가(P-032), 양자내성 TRISA(P-033), KYC 준수 dApp의 ZK 권한부여(P-031), 중앙은행 전문가 PET 분류(P-034). sunrise issue 경제학·트래블룰 효과 실증 논문은 2025~2026년에 **발견되지 않았다**. [P-031][P-032][P-033][P-034]
- **사기 연구의 중심은 address poisoning·rug pull·드레이너로 이동했고, 측정 규모가 급증했다.** Ethereum·BSC 2년간 2.7억 건 공격 시도·1,700만 피해자·6,633건 사고·8,380만 달러 손실(USENIX Security '25, P-036); Ethereum 비철회 상태불변 트랜잭션의 53%가 address poisoning(P-038); 53개 지갑 중 16개가 가짜 토큰 피싱 전송을 그대로 표시(P-037). [P-036][P-037][P-038]
- **rug pull은 "타입 분류학 → 누수 방지 평가"로 정교화됐다.** 35개 유형 분류·13개 도구가 25.7~62.9%만 커버(ISSTA 2025, P-040), 유동성 인출 전 피처만 사용하는 누수 저항 설계(P-043), Solana 3.69억 건에서 62,895개 의심 풀 데이터셋(P-044), TON DEX 거래 첫 5분 내 AUC 0.891(P-042). [P-040][P-042][P-043][P-044]
- **제재 집행의 온체인 한계가 정량화됐다.** Tornado Cash 제재 후 957일간 입금액 71.03% 감소에도 Ethereum 보안사고의 78.33%가 여전히 Tornado Cash 경유(WWW '26, P-049); USDT 제재 주소 7.3%·USDC 18.7%가 동결 발효 전 전액 인출(P-050). [P-049][P-050]
- **벤치마크 회의론이 명시적 연구 주제가 됐다.** 템플릿 기반 이상 주입 벤치마크가 모델 강건성을 과대평가한다는 TransXion(KDD '26, P-056); Elliptic에서 초기화·정규화 선택만으로 결과가 달라진다는 ablation(P-005); 운영 시 손실 기반 평가를 주장한 논문(P-012)은 철회됐다. [P-005][P-012][P-056]
- **기관 보고서는 "불법 규모"보다 "데이터 격차·방법론"을 전면에 세웠다.** 분석업체 두 곳의 2025년 불법 규모는 각각 1,540억 달러(하한, 전년 수치 409억→572억 달러로 상향 수정)와 1,580억 달러(온체인 거래량의 1.2%, VASP 유동성의 2.7%)로 **분모 정의가 다르다**(P-069, P-070). BIS는 스테이블코인이 "불법 온체인 활동의 상당 부분"이라며 permissioned 플랫폼에 AML 내장을 권고했고(P-067), ECB CAMEG는 MiCAR를 자연실험으로 쓰는 분석을 소개했다(P-066). [P-066][P-067][P-069][P-070]
- **저장소 기존 자료의 정정 필요 사항이 다수 확인됐다**(§8): Bellei 2024 제목 오기, Alarab 2020·Möser&Böhme 2017·Androulaki 2013 학회 오기, Elliptic++·Elliptic2 규모 오기, Weber 2019 성능 수치 불일치, 존재가 확인되지 않는 "Sun et al. 2023" 항목, `notes/4-technology/blockchain-analytics.md`에 잔존하는 CTR:00007 날조 표 3곳.

---

## 2. 주제별 주석 서지 (Annotated Bibliography)

### 2.1 가상자산 AML 탐지 — ML/GNN

### [P-001] Tian, Song, Qian, Wang, Sun, Jia (2025). DiT-SGCR: Directed Temporal Structural Representation with Global-Cluster Awareness for Ethereum Malicious Account Detection. arXiv:2506.20123. 발표일 2025-06-25.
- URL: https://arxiv.org/abs/2506.20123
- 유형: preprint (cs.CE)
- 데이터: Ethereum 악성 계정 데이터셋 3종 (초록에 데이터셋명·규모 미기재)
- 방법·결과: 방향성 시간 집계 + 미분가능 클러스터링 + 그래프 라플라시안 정규화를 결합한 **비지도 그래프 인코더**. 기존 방법이 연속적 거래 동역학·거래 방향·계정 군집을 놓친다고 지적. 3개 데이터셋에서 SOTA 대비 F1 **3.62~10.83%p 향상**을 보고하며, 전통적 그래프 전파를 피해 확장성이 좋다고 주장.
- 한계: 비교 대상·데이터셋 규모가 초록에 없음. 라벨 없는 계정 모델에서 "악성"의 정의가 데이터셋 라벨에 종속.
- 저장소 관련성: `notes/4-technology/blockchain-analytics.md` §3(Ethereum 계정 모델 분석 한계) 보강 — 계정 모델에서도 방향·시간 피처로 비지도 탐지가 가능함을 보여주는 2025 사례.
- tier/confidence: T3/A (초록 직접 확인). retrieved: 2026-10-21

### [P-002] Haider, Noreen, Salman (2025). Towards Quantum-Ready Blockchain Fraud Detection via Ensemble Graph Neural Networks. IEEE BCCA 2025 / arXiv:2509.23101. 발표일 2025-09-27.
- URL: https://arxiv.org/abs/2509.23101
- 유형: peer-reviewed (IEEE Conference on Blockchain Computing and Applications 2025 proceedings 게재 명시)
- 데이터: Elliptic 데이터셋
- 방법·결과: GCN·GAT·GIN 3종의 **소프트 보팅 앙상블**. 불법 거래 recall을 높게 유지하면서 **오탐률 1% 미만**을 달성했다고 보고. 양자 피처 매핑·하이브리드 양자-고전 모델 연결을 위한 훅을 포함.
- 한계: 초록에 recall·F1 절대값 없음. Elliptic 단일 데이터셋.
- 저장소 관련성: `curriculum/day_57.md` ML 한계 서술(라벨 부족·클래스 불균형)에서 "앙상블로 FPR 통제"의 2025 사례로 인용 가능.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-003] Poon, Kwok, Chow, Choi (2026). LineMVGNN: Anti-Money Laundering with Line-Graph-Assisted Multi-View Graph Neural Networks. AI (journal) 2025 / arXiv:2603.23584. 발표일 2026-03-24.
- URL: https://arxiv.org/abs/2603.23584
- 유형: peer-reviewed (Comments: "Published as a journal paper in AI 2025")
- 데이터: Ethereum 피싱 거래 데이터셋 1종 + 산업 파트너 제공 금융 결제 데이터셋 1종 (규모 미기재)
- 방법·결과: 다차원 엣지 피처를 다루기 어려운 스펙트럴 GNN과 자금 흐름을 포착하지 못하는 공간 GNN의 한계를 지적하고, **라인그래프 뷰**(거래를 노드로)와 양방향 메시지 전달을 결합한 경량 멀티뷰 모델 제안. 두 데이터셋에서 SOTA를 상회한다고 보고(초록에 수치 없음). 확장성·적대적 강건성·규제 고려사항 논의 포함.
- 한계: 초록에 수치 없음. 산업 데이터셋은 비공개.
- 저장소 관련성: `notes/4-technology/blockchain-analytics.md` §8(ML/AI) — "거래(엣지)를 1급 객체로 보는 설계"가 2026년 흐름임을 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-004] D'Amico, De Rosso, Dixit, Salles de Padua, Palmer, Mugel, Orús, Eble, Abedi (2025). Blockchain Network Analysis using Quantum Inspired Graph Neural Networks & Ensemble Models. arXiv:2508.09237. 발표일 2025-08-12.
- URL: https://arxiv.org/abs/2508.09237
- 유형: preprint (cs.LG, quant-ph)
- 데이터: 블록체인 거래 네트워크 (초록에 데이터셋명 미기재)
- 방법·결과: GNN에 **Canonical Polyadic(CP) 분해 층**을 추가한 양자영감 GNN + QBoost 또는 Random Forest 앙상블. 사기 거래 탐지에서 **F2 74.8%** 보고.
- 한계: F2 지표 단독 보고(F1·PR-AUC 없음), 데이터셋 불명. 양자영감 기법의 AML 실무 효용은 미검증.
- 저장소 관련성: 참고 수준. `curriculum/day_57.md` "ML 한계" 서술에 "지표 선택(F2 등)이 결과 해석을 좌우"한다는 주의로 활용.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-005] Dang, Nguyen, Dev, Nijsse (2026). Normalisation and Initialisation Strategies for Graph Neural Networks in Blockchain Anomaly Detection. Engineering Applications of Neural Networks 2026 (Springer), pp. 313–326 / arXiv:2602.23599. 발표일 2026-02-27.
- URL: https://arxiv.org/abs/2602.23599
- 유형: peer-reviewed (Springer Nature 학회 proceedings)
- 데이터: Elliptic Bitcoin 데이터셋
- 방법·결과: GCN·GAT·GraphSAGE 3종에 대해 가중치 초기화·정규화 전략의 **체계적 ablation**. GraphSAGE는 Xavier 초기화 단독이 최적, GAT는 GraphNorm+Xavier 조합이 최대 이득, GCN은 변화에 거의 민감하지 않음. 재현 가능한 실험 프레임워크 공개.
- 한계: 초록에 성능 절대값 없음. Elliptic 단일.
- 저장소 관련성: §5 상충 항목 — Elliptic 벤치마크 수치는 **구현 세부(초기화·정규화)에 따라 달라지므로** 논문 간 F1 비교표를 만드는 것 자체가 위험하다는 근거.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-006] Lin, Zheng, Wu, Yang, Lin, Xiao, Song, Zheng (2025). Track and Trace: Automatically Uncovering Cross-chain Transactions in the Multi-blockchain Ecosystems. arXiv:2504.01822. 발표일 2025-04-02.
- URL: https://arxiv.org/abs/2504.01822
- 유형: preprint (cs.SE, cs.CR; 검색 결과는 IEEE TSC 게재를 언급하나 arXiv 페이지에 venue 미기재)
- 데이터: 주류 크로스체인 브리지 12개
- 방법·결과: 이벤트 로그 마이닝 + 개체명 인식(명시적 단서) + 정보검색(암묵적 단서)으로 **양방향 크로스체인 거래 추적 도구 ABCTracer** 구축. 12개 브리지에서 **양방향 추적 F1 91.75%**. 실제 크로스체인 공격·자금세탁 사건에 적용.
- 한계: 브리지별 성능 분포·실패 유형이 초록에 없음. 유동성 풀 기반 브리지(1:1 매칭 불가)의 처리 여부 불명.
- 저장소 관련성: `notes/4-technology/blockchain-analytics.md` §5.5 "정확도 벤치마크(공개+추정)" 표(97~99% 등 출처 없는 수치)를 **이 논문과 P-007·P-016의 실측치로 대체**해야 함(§8-14).
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-007] Liang, Duan, Su, Li, Liu, Tian, Xu, Zhong (2025). ConneX: Automatically Resolving Transaction Opacity of Cross-Chain Bridges for Security Analysis. arXiv:2511.01393. 발표일 2025-11-03.
- URL: https://arxiv.org/abs/2511.01393
- 유형: preprint (cs.CR)
- 데이터: 5개 주요 브리지 플랫폼, 약 50만 건 거래
- 방법·결과: LLM으로 의미 탐색 공간을 **1e10에서 100 미만**으로 축소한 뒤, 검사기 모듈이 거래 금액으로 후보를 검증해 양측 거래 쌍을 자동 매칭. **평균 F1 0.9746**, 기준선 대비 최소 20.05%p 상회. 실제 해킹 사건의 불법 자금 추적(100만 달러 규모 전송 사례) 시연.
- 한계: 5개 플랫폼 한정. LLM 의존 단계의 재현성·비용 미기재.
- 저장소 관련성: P-006과 함께 §5.5 대체 근거. "브리지 쌍 매칭 실패가 자금 추적 실패의 주원인"이라는 문제 정의는 `notes/3-crypto-aml/onchain-typology.md` 체인호핑 서술 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-008] Wu, Wang, Li, Wu, Fan, Liu, Luo (2026). Tracing the Shadows: Automatic Tracking and Analysis of Crypto Money Laundering via Transaction Semantic Analysis. arXiv:2607.18869. 발표일 2026-07-21.
- URL: https://arxiv.org/abs/2607.18869
- 유형: preprint (cs.CR)
- 데이터: 실제 자금세탁 사건 82건(불법 자산 10억 달러 초과), 단일체인·크로스체인 데이터셋
- 방법·결과: 계정 기반 체인용 **의미 인식 AML 프레임워크 AMLGuard**. 규칙 기반 정적 분석 + RAG 기반 LLM 추론으로 복잡한 DeFi 거래의 의도를 추론하고 각 거래를 "DeFi Semantic Unit(DSU)"로 추상화해 체인 간 자금을 추적. 목적지 정밀도 **94.4%/87.6%**, 주소 recall **98.4%/95.8%**, 목적지 recall **94.1%/93.8%**(단일/크로스체인).
- 한계: 82건은 알려진 사건이므로 선택 편향. LLM 추론 단계의 오류 전파 분석은 초록에 없음.
- 저장소 관련성: `notes/3-crypto-aml/onchain-typology.md`·`defi-nft-risks.md` — "DeFi 거래 의미 해석"이 추적의 병목이라는 2026년 문제 설정.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-009] Jia, Tian, Zhang, Wang, Sun, Song (2025). KGBERT4Eth: A Feature-Complete Transformer Powered by Knowledge Graph for Multi-Task Ethereum Fraud Detection. arXiv:2509.03860. 발표일 2025-09-04.
- URL: https://arxiv.org/abs/2509.03860
- 유형: preprint (Comments: IEEE 투고 중)
- 데이터: 피싱 계정 탐지 벤치마크 3종 + 비익명화 데이터셋 4종 (명칭 미기재)
- 방법·결과: 거래 기록의 의미 표현을 학습하는 Transaction Language Model + 자금 흐름 패턴·전문가 피처를 담은 Transaction Knowledge Graph를 결합한 사전학습 인코더. 희귀 이상 거래를 강조하는 편향 마스킹 과제 포함. 피싱 탐지 F1 **8~16%p**, 비익명화 **6~26%p** 개선 보고.
- 한계: 개선폭만 보고(절대값 없음). 벤치마크 명칭 미기재.
- 저장소 관련성: `notes/4-technology/blockchain-analytics.md` §3 — 계정 모델에서 "거래 텍스트화 + 지식그래프"라는 2025년 접근 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-010] Wu, Chen, Lin, Li, Zhao (2026). Phishing Detection in Ethereum via Temporal Graph Contrastive Learning. arXiv:2605.01207. 발표일 2026-05-02.
- URL: https://arxiv.org/abs/2605.01207
- 유형: preprint (16p, 11 fig, 13 tables)
- 데이터: 161,658개 주소·416,541건 거래; 실배포 2023-05-01~2024-07-31
- 방법·결과: 이기종 시간 속성 멀티그래프 + 시간 그래프 대조학습으로 **완전 동적·자기지도** 피싱 탐지 시스템 PhishEye. 피싱 거래 탐지 F1 87.23%/AUC 98.43%, 피싱 계정 탐지 F1 94.19%/AUC 98.03%. 실배포에서 **미지의 피싱 주소 1,803개** 식별, 손실 예방 20억 달러(저자 주장).
- 한계: "손실 예방 20억 달러"는 반사실 추정이며 산정 방법은 초록에 없음.
- 저장소 관련성: `curriculum/day_57.md` "Scam 사전 탐지 실용도 하~중" 평가를 **재검토**할 근거(자기지도 실배포 사례).
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-011] Heidrich, Heidemann, Buchkremer, Wandosell Fernández de Bobadilla (2026). A Systematic Evaluation Protocol of Graph-Derived Signals for Tabular Machine Learning. Applied Sciences (DOI 10.3390/app16052624) / arXiv:2603.13998. 발표일 2026-03-14.
- URL: https://arxiv.org/abs/2603.13998
- 유형: peer-reviewed (MDPI Applied Sciences DOI 연결)
- 데이터: "대규모 불균형 가상자산 사기 탐지 데이터셋"(초록에 명칭 없음 — Elliptic으로 단정 금지)
- 방법·결과: 그래프 파생 피처 범주별로 통계적으로 유의하고 강건한 이득이 있는지 검증하는 **재현 가능한 평가 프로토콜**(자동 하이퍼파라미터 튜닝·다중 시드·유의성 검정·그래프 섭동 강건성). 일부 신호 범주는 일관된 이득, 결손·오염 관계 데이터에서의 거동은 범주별로 상이.
- 한계: 초록에 수치 없음.
- 저장소 관련성: §5 — "그래프 피처가 항상 이득"이라는 가정에 대한 검정 프로토콜. `curriculum/day_57.md` ML 한계에 "통계적 유의성 검정 부재" 추가 근거.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-012] Bhatt, Sharma (2026). Algorithmic Compliance and Regulatory Loss in Digital Assets. arXiv:2603.04328. 발표일 2026-03-04 — **2026-04-24 v2로 저자 철회(withdrawn)**.
- URL: https://arxiv.org/abs/2603.04328
- 유형: preprint — **철회됨** ("requires substantial revision")
- 데이터: Bitcoin 거래 데이터(상세 미기재)
- 방법·결과: 전향적·롤링 평가로 배포 후 ML AML 시스템의 효과를 측정. 정적 분류 지표가 실제 규제 효과를 과대평가하며, 원인은 예측력 저하보다 **의사결정 임계값의 보정 실패**라는 주장. 분포 변화로 비용 민감 임계값이 불안정해져 동적 최적 벤치마크 대비 초과 규제 손실 발생.
- 한계: **철회 상태이므로 결과 인용 불가.** 문제 설정(개념 표류 → 임계값 불안정)만 참고.
- 저장소 관련성: Weber 2019의 "암시장 폐쇄 후 성능 붕괴"(`_research/wave1/analytics-technology.md` F-035)와 같은 문제를 2026년에 재제기했다는 점만 기록. 수치 인용 금지.
- tier/confidence: T3/D (철회). retrieved: 2026-10-21

### [P-013] Grama (2025). Money Laundering Detection Using Graph Neural Networks Enhanced with Autoencoder Components. Studia Universitatis Babeș-Bolyai Informatica 70(1-2). DOI 10.24193/subbi.2025.06. 발표일 2025-11-27.
- URL: https://studia.reviste.ubbcluj.ro/index.php/subbinformatica/article/view/9735
- 유형: peer-reviewed (대학 학술지)
- 데이터: 동종 그래프로 표현된 거래 데이터(데이터셋명 초록 미기재; 참고문헌에 AMLSim·합성 거래 데이터셋 포함)
- 방법·결과: GNN 엣지 분류에 **오토인코더 재구성 단계**를 결합, 재구성 오차로 성능 개선. Shapley 값으로 정상/사기 분리에 기여한 피처 식별.
- 한계: 초록에 수치 없음. 합성 데이터 가능성 높음.
- 저장소 관련성: `curriculum/day_57.md` "설명가능성" — SHAP 결합 GNN의 2025 학술 사례.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-014] [맥락·2024] Song, Dhraief, Xu, Cai, Chen, Arvind, Chen (2024). Identifying Money Laundering Subgraphs on the Blockchain. ICAIF 2024 / arXiv:2410.08394. 발표일 2024-10-10.
- URL: https://arxiv.org/abs/2410.08394
- 유형: peer-reviewed (ICAIF 2024). 코드 공개: GitHub MITIBMxGraph/RevTrack
- 데이터: Elliptic2
- 방법·결과: 자금의 **최초 송신자·최종 수신자**를 추적하는 RevTrack 프레임워크. 서브그래프 분류기 RevClassify, 후보 서브그래프가 없을 때 합법 거래를 반복 제거해 새 의심 서브그래프를 찾는 RevFilter. Elliptic2에서 비용·정확도 양면에서 기존 서브그래프 분류법 상회(초록에 수치 없음).
- 한계: Elliptic2 라벨("의심")의 정의에 종속.
- 저장소 관련성: `deep/papers.md` §4 Bellei 2024 항목 뒤에 **후속 연구**로 추가.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-015] Alteneiji, Shaalan, Yerima, Butt (2025). Systematic Review: Machine Learning Approaches for Detecting Illicit Activities in Bitcoin Transactions. IEEE ICCR 2025 (Dubai, 2025-07-03~04). DOI 10.1109/ICCR67387.2025.11291938.
- URL: https://research.ajman.ac.ae/en/publications/systematic-review-machine-learning-approaches-for-detecting-illic/
- 유형: peer-reviewed (학회)
- 데이터: 2015~2025년 문헌
- 방법·결과: 지도학습·비지도 클러스터링·그래프 신경망 연구를 체계적으로 검토. 클래스 불균형·미라벨 데이터·고도화된 세탁 기법이 탐지를 어렵게 한다고 정리. **그래프 어텐션 모델이 규칙 기반 대비 40% 이상 성능 우위**라고 요약(리뷰 저자의 종합치).
- 한계: "40% 이상"은 리뷰의 2차 종합이며 지표·기준선이 초록에 없음 — 저장소에 수치로 옮기지 말 것.
- 저장소 관련성: `deep/papers.md` §4 ML 섹션 — 2025년 체계적 리뷰로 안내.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-016] Yan, Huang, Tessone (2025). Ethereum–Polygon 브리지 거래 매칭 (arXiv:2504.15449). 발표일 2025-04-22. — `_research/wave1/analytics-technology.md` F-038·F-039에서 2026-07-30 검증 완료, 본 조사에서는 재열람하지 않음.
- URL: https://arxiv.org/abs/2504.15449
- 유형: preprint
- 데이터: 2020-08-28~2023-08-28 Ethereum–Polygon 브리지 거래
- 방법·결과: 수취인·시간창·토큰·금액 4기준 매칭. 입금 매칭률 Ether 94.97%, ERC20 93.04%, ERC721 99.65%; 출금 Ether 81.74%, ERC20 67.55%, ERC721 92.78%. 출금 시간창(약 6.4일)이 입금(약 24분)의 약 380배.
- 한계: 단일 브리지. ERC20 출금이 최약점.
- 저장소 관련성: P-006·P-007과 함께 `blockchain-analytics.md` §5.5 대체. 자산 유형별 신뢰도 차등 설계 근거.
- tier/confidence: T3/B (저장소 wave1 검증 인용). retrieved: 2026-07-30 (wave1)

### 2.2 주소 클러스터링·비익명화·프라이버시 프로토콜

### [P-017] Huseynov, Shahzaib, Seres, Tapolcai (2026). A Tattered Cloak of Invisibility: Measuring Anonymity Loss in Railgun on Ethereum. arXiv:2606.25926. 발표일 2026-06-24.
- URL: https://arxiv.org/abs/2606.25926
- 유형: preprint (Comments: Pre-print)
- 데이터: Ethereum 상 Railgun 전체 shield/unshield 거래
- 방법·결과: 타이밍·주소 재사용·거래그래프 근접성·금액 지문·배낭식 금액 매칭 **5가지 누수원**으로 입금–출금 동일 사용자 확률 추정. **출금 거래의 17.65%가 입금과 유일 연결**, 출금의 **중위 익명성 손실 3.42비트**. 암호학적으로 강한 시스템도 사용자 행태가 익명성을 크게 줄인다는 결론.
- 한계: Ethereum 배포만 측정(P-018이 6개 체인으로 확장). PPOI(Private Proofs of Innocence)의 효과는 초록에 없음.
- 저장소 관련성: `_research/wave1/analytics-technology.md` F-030(동일 논문)·`notes/4-technology/blockchain-analytics.md` §7 프라이버시 프로토콜 — "Railgun 17.65%" 수치의 1차 출처 재확인.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-018] Guo, Chaliasos, Feng, Xu (2026). The Anonymity Gap: Understanding Real Privacy in Shielded UTXO-based Protocols for DeFi. arXiv:2608.22987. 발표일 2026-08-24.
- URL: https://arxiv.org/abs/2608.22987
- 유형: preprint (cs.CR)
- 데이터: Railgun 프로덕션 배포 4개 + Hinkal 독립 풀 5개, EVM 체인 6개, **unshielding 거래 186,356건** 전 이력
- 방법·결과: 익명성이 풀 크기가 아니라 **자산 출처(provenance)**에 좌우된다는 계층 모델 + 공개 제약·과거 은닉 상태 전이를 추적하는 분석 파이프라인. 공개 토큰 제약이 가장 일관된 가지치기 요인 — **평균 익명성 집합 40.1~59.0% 축소**. 후보 주소 10개 이하로 좁혀진 거래 **3,679건**(이 중 단일 후보 1,228건).
- 한계: "익명성 집합 크기"가 실제 비익명화 확률과 직결되지는 않음(저자도 해석 가능 패턴 제시에 중점).
- 저장소 관련성: `kb/entities/protocols` railgun 항목·`notes/4-technology/blockchain-analytics.md` §7 — Hinkal 포함 다중 체인 측정으로 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-019] Cristodaro, Kraner, Tessone (2025). Clustering Deposit and Withdrawal Activity in Tornado Cash: A Cross-Chain Analysis. arXiv:2510.09433. 발표일 2025-10-10 — **2025-11-18 v3로 저자 철회**("mistakes in the references. A corrected version will be prepared").
- URL: https://arxiv.org/abs/2510.09433
- 유형: preprint — **철회됨**
- 데이터: Ethereum·BNB Smart Chain·Polygon의 Tornado Cash
- 방법·결과(철회 전 초록): 주소 재사용·거래 연결·FIFO 시간 매칭 3휴리스틱. 재사용+연결로 출금 5.1~12.6% 추적, FIFO가 15~22%p 추가, 연결된 출금 총 23억 달러.
- 한계: **철회 상태 — 수치 인용 금지.** 정정판 게시 여부를 추적할 것.
- 저장소 관련성: `_research/wave1/analytics-technology.md` F-028·§5에 이미 철회 기록. 본 조사에서 2025-11-18 철회 사유 문구를 확인.
- tier/confidence: T3/D (철회). retrieved: 2026-10-21

### [P-020] Wu, Wu, Feng, Li, Zhang, Li, Sun, Zhang, An, Liu, Guan, Zhu (2026). Unveiling Ethereum Mixing Services Using Enhanced Graph Structure Learning. IEEE TDSC 23(2), 3845–3863. DOI 10.1109/TDSC.2025.3640941. 발표연도 2026(월일 미기재).
- URL: https://pure.bit.edu.cn/en/publications/unveiling-ethereum-mixing-services-using-enhanced-graph-structure/
- 유형: peer-reviewed (IEEE Transactions)
- 데이터: 실제 Ethereum 거래 (규모 미기재)
- 방법·결과: 스마트컨트랙트 기반 믹서를 형식적으로 정의하고, 그래프 구조 학습 기반 **연결성 공격 LASC**로 Tornado Cash 믹싱 계정을 연결. 실현 가능성의 수학적 증명 주장. 기존 SOTA 대비 성능·효율 우위(초록에 수치 없음).
- 한계: 초록에 수치 없음. 라벨 출처 미기재.
- 저장소 관련성: `notes/6-cases/tornado-cash.md` — "제재 후에도 학술적 비익명화 연구가 지속"의 2026 사례.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-021] Tu, Duan, Miao, Zhang, Sun (2025). HiLoMix: Robust High- and Low-Frequency Graph Learning Framework for Mixing Address Association. AAAI 2026 / arXiv:2511.07759. 발표일 2025-11-11.
- URL: https://arxiv.org/abs/2511.07759
- 유형: peer-reviewed (Comments: AAAI 2026)
- 데이터: 믹싱 서비스 상호작용 그래프 (명칭·규모 미기재)
- 방법·결과: 노이즈 라벨·희소 라벨 두 난제에 대해 이기종 속성 믹싱 상호작용 그래프 + **고·저주파 뷰 주파수 인식 대조학습** + 신뢰도 기반 노이즈 라벨 가중. 고역·저역 GNN 공동 학습 후 스태킹. 기존 방법 상회(초록에 수치 없음).
- 한계: 초록에 수치·데이터셋 없음.
- 저장소 관련성: `curriculum/day_57.md` "새 mixer 식별" 영역 — 2025~26년 학술 접근의 핵심이 **라벨 품질 대응**임을 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-022] Che, Li, Shen, Du, Zhu (2025). Correlating Account on Ethereum Mixing Service via Domain-Invariant Feature Learning. arXiv:2505.09892. 발표일 2025-05-15.
- URL: https://arxiv.org/abs/2505.09892
- 유형: preprint
- 데이터: 실제 믹싱 데이터셋(Tornado Cash 포함; 규모 미기재)
- 방법·결과: 블록체인 이상탐지 도메인의 지식을 믹싱 거래 추적으로 전이하는 **StealthLink**. 믹싱 서브그래프 인코더 MixFusion + 도메인 간 적대적 피처 정렬. **F1 96.98%**, **10-shot** 환경에서도 지도학습 대비 일반화 우위.
- 한계: 라벨 출처·클래스 비율 미기재.
- 저장소 관련성: P-021과 함께 "라벨 10개 수준에서도 동작"하는 전이학습 사례 — `notes/4-technology/blockchain-analytics.md` §8.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-023] [맥락·2024] Hammad, Victor (2024). Monero Traceability Heuristics: Wallet Application Bugs and the Mordinal-P2Pool Perspective. IEEE ICBC 2024 (저자판) / arXiv:2408.05332. 발표일 2024-08-09.
- URL: https://arxiv.org/abs/2408.05332
- 유형: peer-reviewed (IEEE International Conference on Blockchain and Cryptocurrency 2024)
- 데이터: Monero 체인 2019~2023
- 방법·결과: 지갑 버그("10 Block Decoy Bug", "Differ-by-one"), P2Pool 출력 병합, Mordinal 유래 휴리스틱을 ground truth 및 쌍별 비교로 평가. **대부분 고정밀**이며 10 Block Decoy Bug와 Coinbase decoy 식별이 2019~2023년 가장 큰 영향. 제거 가능 decoy 수·잔여 유효 링 크기 추정.
- 한계: 2023년 초 패치된 버그 기반 휴리스틱은 신규 거래에 무효.
- 저장소 관련성: `notes/4-technology/blockchain-analytics.md` 535행 "Monero 거의 분석 불가"·605행 "완전 추적 불가는 지속" 서술을 **"구세대 거래는 버그 기반 휴리스틱으로 부분 추적 가능, 패치 이후 거래는 아니다"**로 정밀화(§8-15).
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-024] (저자 미확인 — TU Dresden Privacy and Security 그룹) (2026). Network-level Side-channel Attacks in the Lightning Network. ACM Transactions on Internet Technology (게재 확정, DOI 10.1145/3810239). 공지일 2026-04-30.
- URL: https://tu-dresden.de/ing/informatik/sya/ps/chair/news/publikation-in-acm-transactions-on-internet-technology (ACM DL 페이지는 접근 거부)
- 유형: peer-reviewed (저널 accepted)
- 데이터: 라이브 Lightning 네트워크 실험 + 메인넷 스냅샷 시뮬레이션
- 방법·결과: 악성 AS 같은 **네트워크 수준 관찰자**가 종단 암호화에도 패킷 헤더만으로 Lightning 메시지를 식별, 결제 검열·채널 혼잡 유발 가능. 타이밍·흐름 방향·메시지 유형으로 경로 내 노드 역할 추론. 대응책: 고정 메시지 크기·더미 트래픽.
- 한계: 초록에 수치 없음. **저자 명단을 1차 페이지에서 확인 못 함**(AFT 2024 선행 논문 저자 Ndolo·Tschorsch의 후속으로 추정되나 미확인).
- 저장소 관련성: `notes/4-technology/blockchain-analytics.md` — Lightning 분석은 온체인 휴리스틱이 아닌 네트워크 계층 공격이 주류임을 명시.
- tier/confidence: T3/C (초록은 기관 공지로 확인, 저자 미확인). retrieved: 2026-10-21

### 2.3 거래 모니터링·알람 분류·LLM 활용

### [P-025] Naik, Dintakurthi, Hu, Wang, Qiu (2025). Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives. arXiv:2509.08380. 발표일 2025-09-10 (v2 2025-09-17).
- URL: https://arxiv.org/abs/2509.08380
- 유형: preprint (cs.AI, cs.LG)
- 데이터: 초록에 데이터셋·평가 수치 없음
- 방법·결과: SAR 서술 생성이 고비용·저확장 병목이며 단순 LLM은 사실 환각·범죄 유형론 불일치·설명력 부족이라고 진단. 계획·범죄유형 탐지·외부 정보 수집·컴플라이언스 검증 **전문 에이전트** + 동적 메모리 + 프라이버시 보호층 + Agent-as-a-Judge 실시간 검증 에이전트, 사람 검토자가 최종 수정.
- 한계: **정량 평가 없음.** 아키텍처 제안 논문.
- 저장소 관련성: `curriculum/day_57.md` "LLM in AML — STR 초안 자동 작성" 항목의 학술 참조(단, 수치 인용 불가).
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-026] Torres, Cheng, Hu (2026). Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks. arXiv:2604.19755. 발표일 2026-03-22 (v2 2026-06-06).
- URL: https://arxiv.org/abs/2604.19755
- 유형: preprint (cs.AI, cs.LG)
- 데이터: **공개 합성 AML 벤치마크**
- 방법·결과: 트리아지를 증거 제약 의사결정으로 정식화. RAG 증거 번들 + 명시적 인용을 강제하는 구조화 출력 계약 + 최소 섭동 반사실 점검. 규칙·표형·그래프 ML, LLM-only, RAG-only와 비교. **PR-AUC 0.75, Escalate F1 0.62, 인용 유효성 0.98, 증거 지지 0.88, 반사실 충실도 0.76**. 결론: 거버넌스된 검증 가능 LLM은 트리아지 의사결정 지원에 실용적.
- 한계: 합성 데이터. **인용 유효성 0.98과 Escalate F1 0.62의 괴리** — "근거를 잘 인용한다"가 "에스컬레이션 판단이 맞다"를 보장하지 않음.
- 저장소 관련성: `curriculum/day_57.md` "Alert triage"·"설명가능성" — 감독 질의("왜 STR인가")에 대한 LLM 답변의 신뢰 한계 근거.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-027] Khanvilkar, Kommuru (2025). Regulatory Graphs and GenAI for Real-Time Transaction Monitoring and Compliance Explanation in Banking. arXiv:2506.01093. 발표일 2025-06-01.
- URL: https://arxiv.org/abs/2506.01093
- 유형: preprint (CC BY 4.0)
- 데이터: **시뮬레이션 금융 데이터 스트림**
- 방법·결과: 동적 거래 그래프 + GNN 분류 + 서술 필드 임베딩 + RAG로 **규제 조항에 연결된 자연어 설명** 생성. 시뮬레이션에서 F1 98.2%, precision 97.8%, recall 97.0%. 전문가 평가로 설명 품질 확인.
- 한계: 시뮬레이션 데이터의 98% F1은 실데이터로 이전 불가. 은행 결제 맥락.
- 저장소 관련성: 가상자산 전이 가능 요소는 "설명을 규제 조항(예: 특금법 조문)에 앵커링"하는 설계. `notes/5-compliance/str-ctr.md` 보강 아이디어.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-028] Pirmorad (2025). Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs. IEEE ICDMW 2025 (AI4FCF-ICDM 2025) / arXiv:2507.14785. 발표일 2025-07-20 (v2 2025-10-29).
- URL: https://arxiv.org/abs/2507.14785
- 유형: peer-reviewed (워크숍)
- 데이터: 합성 AML 시나리오
- 방법·결과: 금융 지식그래프에서 관심 개체의 **k-hop 이웃을 구조화 텍스트로 변환**, few-shot 프롬프트로 의심도 평가·설명 생성. LLM이 분석가식 추론·레드플래그 식별·일관된 정당화를 모방. 저자 스스로 "탐색적 연구"로 규정.
- 한계: 정량 평가 없음, 합성 데이터.
- 저장소 관련성: `curriculum/day_57.md` LLM 시나리오 — "그래프→텍스트 직렬화"가 LLM 활용의 공통 패턴임을 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-029] Cheng, Wang (2025). Design and Implementation of a Suspicious Activity Report Generation System Driven by Large Language Models. Advances in Transdisciplinary Engineering vol. 74 (MIDA 2025), pp. 79–87. DOI 10.3233/ATDE250594.
- URL: https://ebooks.iospress.nl/doi/10.3233/ATDE250594
- 유형: peer-reviewed (IOS Press 학회 proceedings; 페이지에 발행일 미기재, 저작권 2026)
- 데이터: 프로덕션 운영 데이터(상세 미기재)
- 방법·결과: 문서 요약·개체 연결·보고서 생성 3기능 마이크로서비스. GNN-CL 프레임워크 기반 다중 헤드 어텐션·GCN 피처 추출. **평균 처리시간 45분→8초, 정확도 90% 초과, 운영비용 전통 방식의 15%**(저자 자체 보고).
- 한계: 자체 보고 수치, 평가 프로토콜 미기재, "정확도"의 정의 불명.
- 저장소 관련성: `curriculum/day_57.md` "STR 초안 30% 시간 단축 보고" 같은 **출처 없는 수치**를 이 논문의 자체 보고치로 교체하되 "자체 보고"임을 명시.
- tier/confidence: T3/B (자체 보고 수치). retrieved: 2026-10-21

### [P-030] Ding, Ding, Jiang, Pang, Xiao, Liu, Chen, Zhong, Yuan, Guan, Cheng, Xu (2025). Beyond Knowledge to Agency: Evaluating Expertise, Autonomy, and Integrity in Finance with CNFinBench. KDD 2026 / arXiv:2512.09506. 발표일 2025-12-10 (v6 2026-06-08).
- URL: https://arxiv.org/abs/2512.09506
- 유형: peer-reviewed (Proceedings of KDD 2026 명시)
- 데이터: 29개 하위과제 벤치마크, 22개 모델 평가
- 방법·결과: 규제 코퍼스 기반 전문지식·엔드투엔드 에이전트 워크플로·다중 턴 적대적 공격을 평가. Harmful Instruction Compliance Score(HICS) 제안. LLM은 응용 과제에 강하나 **규칙 이해가 약하고**, 단일 모듈→전체 실행 체인에서 **15.4 하락**, 다중 턴 공격 2라운드에서 **평균 위반 159.05% 급증**.
- 한계: **AML 명시 과제 없음**(규제 준수 일반). 중국어 금융 맥락.
- 저장소 관련성: "규제 문서 QA에 LLM 사용"(`curriculum/day_57.md`)의 한계 근거 — 규칙 이해·다중 턴 공격 취약.
- tier/confidence: T3/A. retrieved: 2026-10-21

### 2.4 트래블룰·프라이버시 보존 컴플라이언스

### [P-031] Piper, Wolf, Heiss (2025). Privacy-Preserving On-chain Permissioning for KYC-Compliant Decentralized Applications. arXiv:2510.05807. 발표일 2025-10-07.
- URL: https://arxiv.org/abs/2510.05807
- 유형: preprint (cs.CR)
- 데이터: KYC 준수 DeFi 구현체 실험(수치 초록 미기재)
- 방법·결과: 자기주권신원(SSI) + ZKP + 속성기반 접근제어(ABAC)로 분산 정책 결정에 기반한 **프라이버시 보존 온체인 권한부여**. 등호·범위·멤버십·시간 의존 증명 지원. 자격증명 진위 검증을 ZKP 회로 밖으로 빼는 commit-and-prove로 증명 생성 가속. 기준선 대비 성능 개선 주장.
- 한계: 초록에 수치 없음. 트래블룰 자체가 아닌 KYC 게이팅.
- 저장소 관련성: `notes/4-technology/travel-rule-protocols.md`·`_research/wave1/analytics-technology.md` F-040(Privacy Pools) 옆에 "KYC 게이팅형 ZK" 계열로 배치.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-032] Shevchuk, Adamyk, Benson, Kovalchuk (2025). Privacy-enhancing technologies for FATF crypto Travel Rule: balancing compliance and data protection. In: Sztuczna Inteligencja i Cyberbezpieczeństwo – 2025 (eds. Rysiński, Więcek), ch. 5, pp. 45–56. DOI 10.53052/9788367652520. 발표일 2025-12-05.
- URL: https://research.aston.ac.uk/en/publications/technologie-wspieraj%C4%85ce-prywatno%C5%9B%C4%87-dla-regu%C5%82y-podr%C3%B3%C5%BCy-fatf-w-kryp/
- 유형: peer-reviewed (편저 단행본 챕터; 폴란드 Bielsko-Biała)
- 데이터: 문헌·구현체 검토
- 방법·결과: GDPR·MiCA·AMLR·CCPA 하에서 트래블룰 PII 보호 과제를 정리하고 토큰화·MPC·동형암호·ZKP·TEE·SSI를 평가, TRISA·OpenVASP/TRP·TAP 등 구현체 검토. 결론: **중앙집중형 컴플라이언스 아키텍처에서 연합형·암호학적 검증 가능 모델로 이동**.
- 한계: 초록에 수치 없음. 평가 기준의 정량화 없음.
- 저장소 관련성: `deep/papers.md` §3 Travel Rule(화이트페이퍼만 있음)에 **첫 동료심사 문헌**으로 추가. `notes/4-technology/travel-rule-protocols.md` 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-033] Shevchuk, Adamyk, Benson (2025). Post-Quantum Security Enhancements for the TRISA Framework: A Technical Perspective. IEEE ACIT 2025 (Šibenik, 2025-09-17~19), pp. 553–558. DOI 10.1109/ACIT65614.2025.11185711. 발표일 2025-10-09.
- URL: https://research.aston.ac.uk/en/publications/post-quantum-security-enhancements-for-the-trisa-framework-a-tech/
- 유형: peer-reviewed (IEEE 학회)
- 데이터: TRISA 프레임워크 암호 구성 분석
- 방법·결과: TRISA가 의존하는 RSA·ECDSA의 양자 취약성을 지적하고 **CRYSTALS-Kyber(키 캡슐화)·CRYSTALS-Dilithium(서명)**로의 마이그레이션 경로 제안.
- 한계: 구현·성능 측정 없음(기술 관점 제안).
- 저장소 관련성: `kb/entities/protocols` trisa 항목 — 장기 리스크(양자) 항목 추가.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-034] Helal, Talout Zitan (Banque de France), Koutrouli (Bank of Greece), Nogueira, Pinto (Banco de Portugal) (2025). Privacy-enhancing mechanisms. — ECB Occasional Paper No. 382 §2.10.2 수록 초록 (CAMEG 2025 Conference, 2025-10-30~31). 공개 2026-03-23.
- URL: https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op382.en.pdf (p. 35)
- 유형: working paper 초록 (중앙은행 전문가 개인 견해)
- 데이터: 기법 분류·오남용·집행 사례 검토
- 방법·결과: permissionless 네트워크의 기밀성 강화 기법 **분류체계** — 커스터디 믹서·CoinJoin형 조정, ZK 증명, MPC, 완전동형암호, 스텔스 주소 — 를 신뢰 가정·검증 가능성·성능·운영 복잡성·**AML/CFT 준수** 관점에서 평가. BIS Innovation Hub **Mandala** 프로젝트(MPC 제어 + ZK)를 예시. 결론: 적절한 조합으로 사용자 프라이버시와 충분한 감독을 동시 달성 가능.
- 한계: 초록만 수록(본문 미공개). 같은 OP §2.10.3(Nardelli, Banca d'Italia)은 e-cash→CBDC 프로토타입까지 PET 통합 분류를 arXiv 기술보고서로 발표 예정이라 밝힘(ID 미기재).
- 저장소 관련성: `notes/4-technology/travel-rule-protocols.md` — 규제당국 측 PET 인식의 1차 자료.
- tier/confidence: T2/A. retrieved: 2026-10-21

### [P-035] (산업) 분석업체 T 백서 (2026). On-chain Privacy and Financial Compliance. 발표일 2026-02-19.
- URL: https://www.trmlabs.com/reports-and-whitepapers/on-chain-privacy-and-financial-compliance
- 유형: industry white paper
- 데이터: 사례 연구(Ronin 브리지 해킹, 가상 스테이블코인 "RUSD", 더스팅)
- 방법·결과: 거래 뷰키·주소 뷰키·집합 멤버십 증명·자산 뷰키·허용목록 **5개 프라이버시 체제**를 이해관계자 요구·위협모델로 비교, 단일 체제로는 부족하며 하이브리드 설계를 권고. Proof of Innocence의 한계(미지 주소는 통과, 선입금 오염은 비가역), ASP 설계의 rage-quit. 백만 주소 더스팅 비용을 "수백 달러"로 추정.
- 한계: 벤더 관점. 수치 대부분이 예시(RUSD 티어 등).
- 저장소 관련성: `_research/wave1/analytics-technology.md` F-040·F-041(Privacy Pools·PPOI) 보강 — 업계 측 설계 평가.
- tier/confidence: T3/B. retrieved: 2026-10-21

### 2.5 사기·FDS

### [P-036] Tsuchiya, Dong, Soska, Christin (2025). Blockchain Address Poisoning. USENIX Security 2025 / arXiv:2501.16681. 발표일 2025-01-28 (v3 2025-07-02).
- URL: https://arxiv.org/abs/2501.16681
- 유형: peer-reviewed (USENIX Security '25 게재 명시)
- 데이터: Ethereum·BSC **2년간** 측정
- 방법·결과: 피해자 거래 이력에 유사 주소를 주입하는 address poisoning에 대한 탐지 시스템 구축·대규모 측정. 선행 연구 대비 **13배 많은 공격 시도** — **온체인 공격 2.7억 건, 피해자 1,700만, 사고 6,633건, 손실 8,380만 달러**. 대형 공격자 집단 수익성, 표적·성공 요인, 크로스체인 공격, 소프트웨어·하드웨어별 유사주소 생성 시뮬레이션, 대응책 논의.
- 한계: v1(2025-01)과 v3(2025-07) 수치가 다를 수 있음(§5-7 참조 — 2차 요약에서 1,700만 시도·130만 피해자·7,930만 달러가 유통).
- 저장소 관련성: `notes/3-crypto-aml/onchain-typology.md`에 address poisoning 유형 신설 근거. `kb/entities/typologies` 추가 후보.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-037] Guan, Li (2025). Ethereum Crypto Wallets under Address Poisoning: How Usable and Secure Are They? arXiv:2508.12107. 발표일 2025-08-16.
- URL: https://arxiv.org/abs/2508.12107
- 유형: preprint (15p)
- 데이터: 인기 Ethereum 지갑 **53종** 대상 공격 시뮬레이션
- 방법·결과: 12개 지갑은 거래 활동 제공자와의 통신 실패로 이력 자체를 못 내려받았고, **16개 지갑은 가짜 토큰 피싱 전송을 그대로 표시**(고위험). 대부분 제공자 필터링에 의존하며 품질 편차 큼. 피싱 주소로 송금 시 **명시적 경고를 띄운 지갑은 3개**. 개발자 커뮤니티가 버그 리포트를 인정하고 완화 작업 중. 누적 손실은 "1억 달러 초과"로 기술.
- 한계: 스냅숏 시점 평가, 지갑 업데이트로 변동.
- 저장소 관련성: `notes/4-technology/kyc-kyt.md` — 지갑 단 통제의 실태(VASP 출금 전 경고의 필요성).
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-038] Pahari, Messias, Ferreira Torres (2026). There Will Be Spam: Characterizing State-Invariant Transactions and Speculative MEV. arXiv:2607.24172. 발표일 2026-07-27.
- URL: https://arxiv.org/abs/2607.24172
- 유형: preprint (cs.CR)
- 데이터: Ethereum·Optimism·Base
- 방법·결과: 수수료 외 상태 변화가 없는 "상태불변 트랜잭션"을 정의, **약 14억 건** 식별. Ethereum 거래의 2.6%, Optimism 24%, Base 37%. L2에서는 투기적 MEV가 주원인(Optimism 57%, Base 68%). **Ethereum의 비철회 상태불변 트랜잭션 중 53%가 address poisoning**. 감축 시 자원·수수료 절감과 피싱 억제 효과.
- 한계: address poisoning 식별은 선행 데이터셋(P-036)의 주소 쌍에 의존(선행 데이터셋의 블록 20,208,026~21,565,106 공백을 지적).
- 저장소 관련성: P-036 보강 — address poisoning이 L1 스팸의 과반이라는 2026 측정.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-039] Jiang, Zhang, Li, Li, Zhou, Wu, Hou, Zhang, Li (Tsinghua·Baidu·Nankai·Zhongguancun Lab) (2026). CtPhishCapture: Uncovering Credential-Theft-Based Phishing Scams Targeting Cryptocurrency Wallets. NDSS 2026.
- URL: https://www.ndss-symposium.org/wp-content/uploads/2026-f2854-paper.pdf (PDF 1면 직접 추출)
- 유형: peer-reviewed (NDSS 2026)
- 데이터: 6개월 배포; **CtPhish 웹사이트 5,138개·앱 10,612개**
- 방법·결과: 의심 사이트를 능동 방문 → **LLM 기반 분류** → 앱 다운로드·분석. 웹사이트 17%·앱 21%만 기존 커뮤니티 보고와 중복 → **83%/79%가 신규 발견**. 전형적 3단계(블랙햇 SEO → 정품 모방 → 자격증명 입력 유도). 기존 도구 CES의 한계: 5,138개 사이트 중 43%는 타이포스쿼팅으로 생성 불가, 앱 10,612개 중 28%는 정품과 다른 이름. 배포 후 주간 사용자 민원 **5.8배 감소**.
- 한계: 중국어권 검색엔진 협업 배포 — 지역 편향. 드레이너(승인 서명형)와 구분되는 "자격증명 탈취형"에 한정.
- 저장소 관련성: `notes/3-crypto-aml/onchain-typology.md` 피싱 유형 세분화(자격증명 탈취 vs 승인 드레이너).
- tier/confidence: T3/A (논문 PDF 1면 직접 확인). retrieved: 2026-10-21

### [P-040] Sun, Ma, Nie, Liu (2025). SoK: A Taxonomic Analysis of DeFi Rug Pulls — Types, Dataset, and Tool Assessment. ISSTA 2025 (Trondheim, 2025-06-25~28).
- URL: https://conf.researchr.org/details/issta-2025/issta-2025-papers/25/SoK-A-Taxonomic-Analysis-of-DeFi-Rug-Pulls-Types-Dataset-and-Tool-Assessment
- 유형: peer-reviewed (ACM ISSTA 2025 Research Papers)
- 데이터: 학술 논문 31편·산업 자료 27건 검토; 신규 데이터셋 2,391건
- 방법·결과: **35개 rug pull 유형**(이 중 9개 신규) 분류체계. 기존 데이터셋은 알려진 유형의 20%만 커버 → 신규 데이터셋으로 82.9%까지 확대. **13개 탐지 도구** 평가 결과 커버리지 **25.7~62.9%**, 어떤 도구도 못 잡는 유형 9개. 복합 기법 rug pull에서 성능 급락(55.6%→31.3%).
- 한계: 도구 평가 시점 고정.
- 저장소 관련성: `notes/3-crypto-aml/defi-nft-risks.md` rug pull 서술에 유형 수·도구 커버리지 수치 반영.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-041] Wu, Cao, Chen, Yan, Xu, Zhao, Liu, Jiang (2025). RugScreener: Leveraging Temporal Graph Neural Network for Rugpull Detection in DeFi. IEEE TIFS 20, 11120–11133. DOI 10.1109/TIFS.2025.3620669. 온라인 2025-10-14.
- URL: https://scholars.cityu.edu.hk/en/publications/rugscreener-leveraging-temporal-graph-neural-network-for-rugpull-/
- 유형: peer-reviewed (IEEE Transactions)
- 데이터: 신규 Ethereum 데이터셋 — 비라벨 1,882,114건 거래/29,595 토큰; 라벨 128,819건/1,000 토큰(rug pull 500, 정상 500)
- 방법·결과: 메모리·어텐션 메커니즘을 갖춘 **시간 그래프 신경망**으로 급변하는 거래 패턴 포착. **균형 정확도 95.7%**, SOTA 그래프 모델 상회.
- 한계: 라벨 500/500 균형 구성 — 실제 불균형 환경 성능은 별도.
- 저장소 관련성: §4 데이터셋 표. `defi-nft-risks.md` 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-042] Yaremus, Li, Kalacheva, Vodolazov, Yanovich (2025). Detecting Rug Pulls in Decentralized Exchanges: Machine Learning Evidence from the TON Blockchain. arXiv:2509.01168. 발표일 2025-09-01.
- URL: https://arxiv.org/abs/2509.01168
- 유형: preprint (cs.DC, cs.LG)
- 데이터: TON 최대 DEX 2곳(STON.fi, DeDust) 결합
- 방법·결과: TVL 급감 기반과 거래 유휴 기반 **두 가지 rug pull 정의** 비교. Gradient Boosting으로 **거래 개시 첫 5분 내** 식별, TVL 기반 **AUC 최대 0.891**(유휴 기반은 recall 우위). 피처 집합은 거래소 간 일관되나 분포가 달라 **플랫폼 인식 모델** 필요.
- 한계: TON 생태계 한정.
- 저장소 관련성: "rug pull 정의 자체가 복수"라는 점 — `defi-nft-risks.md`에 정의 주의 추가.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-043] Shoaei, Pishdar, Bag-Mohammadi, Karami (2026). LROO Rug Pull Detector: A Leakage-Resistant Framework Based on On-Chain and OSINT Signals. arXiv:2603.11324. 발표일 2026-03-11.
- URL: https://arxiv.org/abs/2603.11324
- 유형: preprint (cs.CR)
- 데이터: 수작업 라벨 토큰 프로젝트 **1,000개**
- 방법·결과: 기존 탐지기의 **시간적 데이터 누수**(유동성 인출 후 신호 사용)를 지적, 유동성 인출 **이전** 피처만 추출. 온체인 지표 + 시간 정렬 OSINT(소셜·검색 트렌드). 코어 모델 TabPFN. 고전 기준선 대비 판별력·확률 보정 우위, 낮은 미탐.
- 한계: 초록에 수치 없음(1,000 외).
- 저장소 관련성: §5 상충 — **벤치마크 데이터 누수**가 rug pull 탐지 성능을 부풀린다는 명시적 지적.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-044] Alhaidari, Kalal, Palanisamy, Sural (2025). SolRPDS: A Dataset for Analyzing Rug Pulls in Solana Decentralized Finance. ACM CODASPY 2025 / arXiv:2504.07132. 발표일 2025-04-06.
- URL: https://arxiv.org/abs/2504.07132
- 유형: peer-reviewed (CODASPY 2025 게재 명시)
- 데이터: Solana 2021~2024(약 4년) **36.9억 건 거래** 스캔 → 의심 유동성 풀 **62,895개**, rug pull 패턴 토큰 **22,195개**
- 방법·결과: Solana 거래 기반 **최초 공개 rug pull 데이터셋**. 비활성 상태·유동성 추가/제거 주석. 예비 분석으로 정상/사기 풀 구분.
- 한계: 라벨은 패턴 기반 주석(법적 확정 아님).
- 저장소 관련성: §4 데이터셋 표. Solana 커버리지가 거의 없는 `notes/3-crypto-aml/defi-nft-risks.md` 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-045] Cai, Bai, Lu, Xu, Yang, Zhou, Lu (2026). GenDetect: Generalizing Reactive Detection for Resilience Against Imitative DeFi Attack Cascade. ICSE 2026 (Rio de Janeiro, 2026-04-12~18) / arXiv:2604.26094. 발표일 2026-04-28.
- URL: https://arxiv.org/abs/2604.26094
- 유형: peer-reviewed (ICSE 2026 게재 명시, 13p)
- 데이터: 과거 3년 DeFi 공격 거래
- 방법·결과: 초기 익스플로잇 논리를 재사용하는 **모방 공격 캐스케이드** 개념화 — **DeFi 공격의 69% 이상이 선행 사고와 유사**. 단일 관측 공격을 일반화 탐지 규칙으로 변환(함수 시그니처 의미·노이즈 트레이스 처리). **정확도 98%, FPR 1%, FNR 3%**, 미공개 공격 **56건** 신규 발견.
- 한계: 모방형에 특화 — 신규 유형에는 반응형 한계 그대로.
- 저장소 관련성: `defi-nft-risks.md` — 익스플로잇 탐지가 "사후 규칙화 속도" 경쟁임을 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-046] Alhaidari, Palanisamy, Krishnamurthy (2025). On-Chain Decentralized Learning and Cost-Effective Inference for DeFi Attack Mitigation. AFT 2025 / arXiv:2510.16024. 발표일 2025-10-15.
- URL: https://arxiv.org/abs/2510.16024
- 유형: peer-reviewed (AFT 2025 게재 명시; LIPIcs vol. 354)
- 데이터: 2020~2025 실제 익스플로잇 **298건·402건 거래·EVM 8체인·손실 37.4억 달러** 큐레이션
- 방법·결과: 프라이빗 릴레이·동일 블록 내 실행 익스플로잇을 놓치는 오프체인 모니터의 한계를 지적, **완전 온체인** 학습·추론 프레임워크. L2에서 학습, 검증된 업데이트를 L1에 전파, 가스 한도 내 추론. Proof-of-Improvement 프로토콜. 양자화·루프 언롤링으로 LR·SVM·MLP·CNN·RNN·결정트리를 Ethereum 블록 가스 한도 내 실행(Z3로 동치 증명).
- 한계: 초록에 F1 등 수치 없음(검색 요약의 "97%/82%"는 미확인 — §7).
- 저장소 관련성: `defi-nft-risks.md` — "온체인 인라인 차단"이라는 새 통제 지점.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-047] [맥락·2024-12] Acharya, Holz (2024). An Explorative Study of Pig Butchering Scams. arXiv:2412.15423. 발표일 2024-12-19.
- URL: https://arxiv.org/abs/2412.15423
- 유형: preprint (cs.CR)
- 데이터: 2024-03~10, 소셜미디어 4개 플랫폼 계정 43만·게시물 77만, 공개 악용 신고 3,200건, 뉴스 1,000건; 피해자 146명 사례·신고 서술 2,570건·사례연구 50건(834명); 크라우드소싱 설문 584명
- 방법·결과: 다중 관점 최초 종합 연구. **추정 손실 5.21억 달러**(저자 추정). 정책·수사·교육 협력 필요.
- 한계: 온체인 네트워크 분석 아님(소셜·신고 데이터). 손실 추정 방법은 초록에 없음.
- 저장소 관련성: `notes/3-crypto-aml/onchain-typology.md` pig butchering — 오프체인 측 실증.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-048] Botha, Singh, Leenen (2025). Analysis of a Cryptocurrency Investment Scam: Pig Butchering. Proceedings of the 24th European Conference on Cyber Warfare and Security 24(1). DOI 10.34190/eccws.24.1.3558. 발표일 2025-06-25.
- URL: https://papers.academic-conferences.org/index.php/eccws/article/view/3558
- 유형: peer-reviewed (학회)
- 데이터: 단일 플랫폼(Elite-Bit) 피해자 인터뷰·서신, 온·오프체인 분석, Maltego 링크 분석
- 방법·결과: 데이팅 플랫폼 접촉 → 투자 유도 → 출금 시 수수료·허위 비용 부과의 전형적 경로를 사례로 해부. 사회공학·허위 긴급성.
- 한계: 단일 사례, 수치 없음.
- 저장소 관련성: `onchain-typology.md` pig butchering 사례 참고.
- tier/confidence: T3/A. retrieved: 2026-10-21

### 2.6 규제·법·경제학

### [P-049] Liu, Ryan, Zhou, Berrang (2025). Evasion Under Blockchain Sanctions. ACM Web Conference 2026 (WWW '26) / arXiv:2507.11721. 발표일 2025-07-15 (camera-ready v2 2026-05-19).
- URL: https://arxiv.org/abs/2507.11721
- 유형: peer-reviewed (WWW '26 게재 명시)
- 데이터: **957일**, Ethereum 블록 679만 개, 거래 10.7억 건
- 방법·결과: OFAC의 Tornado Cash 제재가 사용을 줄였는지 측정. 입금액 **71.03% 감소**(제재 후 약 20억 달러)했으나 Ethereum 관련 보안사고의 **78.33%**에서 여전히 Tornado Cash 사용 → 지속적 회피. 구조적 한계 3가지: 합의층·응용층에 걸친 **단편적 검열**, 난독화 서비스의 복잡성, **이진 제재 목록의 더스팅 공격 취약성**.
- 한계: Ethereum 단일 체인. "보안사고"의 정의·출처는 초록에 없음.
- 저장소 관련성: `notes/6-cases/tornado-cash.md` — 제재 효과의 정량 평가(감소는 했으나 범죄 자금 경유는 지속)로 서술 갱신.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-050] Wu, Bai, Ren, Zhang, Cao, Wang, Wen, Liu (2026). Ordering Power is Sanctioning Power: Sanction Evasion-MEV and the Limits of On-Chain Enforcement. arXiv:2603.27739. 발표일 2026-03-29 (v2 2026-05-03).
- URL: https://arxiv.org/abs/2603.27739
- 유형: preprint (cs.CR)
- 데이터: Ethereum USDT·USDC 집행·회피 종단 데이터 2017-11~2025-08, 동결 가치 15억 달러 초과
- 방법·결과: 동결은 일반 트랜잭션이므로 제재 대상의 전송과 블록 우선순위를 경쟁 → **Sanction-Evasion MEV(SE-MEV)**. **USDT 제재 주소의 7.3%, USDC의 18.7%가 동결 발효 전 전액 인출**. 게임이론 모델: 준수 발행자도 순서 시장 참여가 합리적, 회피는 MEV 전문 행위자에 집중, 암묵적 MEV 세는 벌칙과 함께 상승. 비상 정지·사법 동결 등 모든 특권적 온체인 행위에 일반화.
- 한계: Ethereum 한정(Tron 등 미포함). 인출 선행이 모두 회피 의도인지는 식별 불가.
- 저장소 관련성: `notes/6-cases/circle-stablecoin-freeze.md`·`notes/5-compliance/sanctions-screening.md` — 발행자 동결의 **실효성 한계** 정량 근거.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-051] 신미진·유민정·정윤영·김성민 (2025). 암호화폐 트랜잭션의 실증적 분석을 통한 자금세탁 탐지 기술 (Money Laundering Detection Technology through Empirical Analysis of Cryptocurrency Transactions). 융합보안논문지 25(1), 105–116. DOI 10.33778/kcsa.2025.25.1.105. 발표일 2025-03-31.
- URL: https://www.koreascience.kr/article/JAKO202512754005711.page
- 유형: peer-reviewed (한국융합보안학회 학술지; KCI 등재 여부는 미확인)
- 데이터: 상용 분석 도구(Reactor)로 분석한 실제 사건·수사 중 주소
- 방법·결과: 기존 GNN 기반 탐지 연구가 **ground truth 부재**로 경험적 분석에 머물고, 이미 불법으로 식별된 지갑만 탐지 가능하다고 지적. 실제 데이터 기반 복합 세탁 패턴과 수사 중 주소의 세탁 기법을 분석.
- 한계: 초록에 수치 없음. 상용 도구 의존.
- 저장소 관련성: `deep/papers.md` §7 "한국 기술 논문은 드뭅니다" 서술에 **반례**로 추가. 한국 법학 논문(특금법·이용자보호법)은 본 조사에서 확보 실패(§3, §7).
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-052] Kelly, Rosset (Central Bank of Ireland), Wolff (ECB) (2025). Electronic money tokens in Europe: the changing landscape of US dollar-denominated and euro-denominated stablecoins in the EU. — ECB OP 382 §2.1.2 수록 초록. 공개 2026-03-23.
- URL: https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op382.en.pdf (p. 8)
- 유형: working paper 초록
- 데이터: 2023-01~2025-09 EU 스테이블코인 시장; 지리 귀속 온체인 흐름 + 시가총액·거래량
- 방법·결과: **MiCAR 도입·시행을 자연적 체제 변화**로 삼아 회원국 귀속 시장 활동 변화를 분석. 누적 순유입을 보유 변화의 대리변수로 사용. 비준수 토큰 상장폐지, 준수 USD 스테이블코인으로의 온·오프체인 재배분, 일시적 거래량 압축 속 EU 거주자의 USD 스테이블코인 순축적 지속을 기록.
- 한계: 초록에 수치 없음. 지리 귀속 방법론 상세 미공개.
- 저장소 관련성: `notes/2-regulations/eu-mica-amlr.md` — MiCAR 효과의 **첫 중앙은행 실증 설계**.
- tier/confidence: T2/A. retrieved: 2026-10-21

### [P-053] Saggese, Sigmund, Raunig, Segalla, Haslhofer, Makridis (2025). Digital asset integration in the financial system: evidence from Austria. — ECB OP 382 §2.7.2 수록 초록. 공개 2026-03-23.
- URL: https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op382.en.pdf (p. 24)
- 유형: working paper 초록 (OeNB·Complexity Science Hub·IMT Lucca·Stanford)
- 데이터: 오스트리아 CASP 생태계 2020~2025
- 방법·결과: CASP가 일 1,000억 달러 이상 거래량을 처리하나 **가명 주소·지리 식별자 부재**로 단일 관할 내 온체인 활동 측정이 어렵다는 문제 설정. 고빈도 변동·거시 충격을 활용한 이벤트 스터디, **주소 내 변동 분리**로 구성 효과 극복. flight-to-quality 동학, 커스터디/비커스터디 간 재배분 추적.
- 한계: 초록에 수치 없음.
- 저장소 관련성: `notes/4-technology/blockchain-analytics.md` — "관할 귀속" 분석의 방법론적 난점에 대한 중앙은행 측 1차 서술.
- tier/confidence: T2/A. retrieved: 2026-10-21

### [P-054] Feder (Národná banka Slovenska) (2025). What can we learn from a major crypto-asset scam? A Slovak case study from 2025. — ECB OP 382 §2.7.3 수록 초록. 공개 2026-03-23.
- URL: https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op382.en.pdf (p. 25)
- 유형: working paper 초록 (감독기관)
- 데이터: 국가 당국 신고 사고 데이터·소비자 민원·내부 분석
- 방법·결과: 2025년 상반기 슬로바키아 소매 대상 대형 스캠(손실 "수백만 유로", 피해자 "수만 명") 해부 — 전문적 외양의 허위 플랫폼 + 공격적 대면 마케팅. 디지털 문해력 부족·심리 조작이 확산 요인. **전통적 투자자 경고는 행동적 공명이 부족**하다는 결론, NCA의 시나리오 기반 캠페인 권고.
- 한계: 정확한 손실·피해자 수 미공개.
- 저장소 관련성: `notes/2-regulations/korea-user-protection.md` — 이용자 보호 커뮤니케이션 설계의 유럽 감독기관 사례.
- tier/confidence: T2/A. retrieved: 2026-10-21

### [P-055] [맥락·2020] Feinstein, Werbach (2020). The Impact of Cryptocurrency Regulation on Trading Markets. SSRN. DOI 10.2139/ssrn.3649475.
- URL: https://doi.org/10.2139/ssrn.3649475
- 유형: working paper (Crossref로 서지 확인; 초록 미열람 — 저널 게재판 서지는 미확인)
- 데이터: (검색 요약) 56개 거래소 이벤트 스터디
- 방법·결과: 본 조사에서 초록을 직접 열지 못했으므로 결과 서술 생략. 2025~2026년 트래블룰·VASP 규제의 **거래량·불법 비중 효과를 인과 추정한 동료심사 논문은 발견되지 않았고**, 이 2020년 연구가 여전히 가장 가까운 선행 연구임을 기록하기 위해 포함.
- 한계: 초록 미열람.
- 저장소 관련성: §3 연구 공백의 기준점.
- tier/confidence: T3/C. retrieved: 2026-10-21

### 2.7 데이터셋·벤치마크·서베이

### [P-056] Chen, Jiang, Zhao, Li, Chen, Luo, Li, Liu, Jing, Ye, Wu, Chai (2026). TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering. KDD '26 V.2, pp. 8707–8718. DOI 10.1145/3770855.3817550 / arXiv:2604.17420. 발표일 2026-04-19 (v2 2026-06-25).
- URL: https://arxiv.org/abs/2604.17420
- 유형: peer-reviewed (KDD 2026 게재 명시). 코드·데이터 공개
- 데이터: 합성 **거래 300만 건·개체 5만**
- 방법·결과: 기존 거래그래프 벤치마크가 노드 맥락이 빈약하고 **템플릿 기반 이상 주입**이라 모델 강건성을 과대평가한다고 지적. 프로파일 인식 정상 활동 시뮬레이션 + 확률적 비템플릿 불법 서브그래프 생성. 지속적 개체 프로파일·조건부 거래 행태로 "사회경제적 맥락과 충돌하는 활동" 검정 가능. **기존 모델들이 널리 쓰이는 벤치마크보다 현저히 낮은 점수**.
- 한계: 결제 네트워크 모사(가상자산 특화 아님).
- 저장소 관련성: §5 — 벤치마크 과대평가 문제의 2026 근거. `curriculum/day_57.md` 라벨 부족 서술 보강.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-057] Kumar, Thing (2025). A Survey of Transaction Tracing Techniques for Blockchain Systems. arXiv:2510.09624. 발표일 2025-09-23.
- URL: https://arxiv.org/abs/2510.09624
- 유형: preprint (서베이)
- 데이터: 문헌
- 방법·결과: 단일 원장 내 추적뿐 아니라 **원장 간 자산 이동** 추적 기법을 추적 접근·목표 객체 기준으로 분류·비교, 한계와 향후 방향 제시.
- 한계: 초록에 수치 없음.
- 저장소 관련성: `deep/papers.md` §5 Cross-chain 섹션 서베이로 추가.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-058] Castelao López, Corzo Santamaría, Lagoa Varela (2025). Analysis of the main techniques and tools to combat money laundering: a review of the literature. Journal of Money Laundering Control (DOI 10.1108/JMLC-10-2024-0159). 발표일 2025-08-08.
- URL: https://repositorio.comillas.edu/jspui/handle/11531/102983
- 유형: peer-reviewed (저널명은 DOI 접두어로 추정 — 리포지터리 페이지에 미기재)
- 데이터: 2017~2024년 **45편** (PRISMA, Google Scholar)
- 방법·결과: 통계적 방법 → ML·네트워크 분석으로의 패러다임 전환, 혼합 방법 증가. 과제: 가상자산, 탐지–프라이버시 균형, 해석가능성·확장성. **방법 간 효과를 직접 비교한 연구가 드물다.** 권고: 계층적 분석·데이터 공유 프레임워크·해석가능성(금융기관), 단계적 컴플라이언스·샌드박스·결과 지표(규제기관).
- 한계: Google Scholar 단일 DB.
- 저장소 관련성: `deep/papers.md` §8 저널 안내(JMLC) 갱신.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-059] Liu, Li, Lan, Cheng, Chen, Li, Cao, Han, Zhang, Chai (2025). A Survey on Anti-Money Laundering Techniques in Blockchain Systems. Strategic Study of CAE 27(2), 287–303. DOI 10.15302/J-SSCAE-2024.11.025. 온라인 2025-03-25.
- URL: https://www.engineering.org.cn/sscae/EN/10.15302/J-SSCAE-2024.11.025
- 유형: peer-reviewed (중국공정원 전략연구 저널; 중문/영문 초록)
- 데이터: 문헌
- 방법·결과: 규칙 기반(임계값·주소-개체 연계·크로스체인 연계), ML(SVM·LR·DT·RF·k-means·오프체인 정보), DL(CNN·RNN·GNN·Transformer) 3분류. 향후 과제: **불균형·주석 불확실성에 대응하는 데이터셋**, 신뢰 가능 알고리즘, 은닉 금융활동 탐지, 규제 준수 프라이버시 보존.
- 한계: 초록에 수치 없음.
- 저장소 관련성: `deep/papers.md` 서베이 안내.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-060] Wang (2025). xfraud — PDHG(Ethereum phishing detection via heterogeneous graph transformer) 보조 데이터셋. Mendeley Data v1. DOI 10.17632/xgm4dn7ggs.1. 공개 2025-09-10. CC BY 4.0.
- URL: https://data.mendeley.com/datasets/xgm4dn7ggs/1
- 유형: dataset (연계 논문은 Expert Systems with Applications 투고로 기재; 게재 확인 안 됨)
- 데이터: 구성(계정 수·피싱 라벨 수·거래 수) **페이지에 미기재**
- 방법·결과: 데이터셋 설명 자체가 논문 참조로만 되어 있음.
- 한계: 규모 미확인 — §4 표에는 "구성 미확인"으로만 기재.
- 저장소 관련성: 추적 대상(논문 게재 후 재확인).
- tier/confidence: T3/C. retrieved: 2026-10-21

### [P-061] [맥락·2019] Weber, Domeniconi, Chen, Weidele, Bellei, Robinson, Leiserson (2019). Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics. KDD 2019 Anomaly Detection in Finance Workshop / arXiv:1908.02591. 발표일 2019-07-31.
- URL: https://arxiv.org/abs/1908.02591
- 유형: workshop paper. Elliptic 데이터셋 공개 논문
- 데이터: 초록 — 200K+ 거래(노드)·234K 방향성 결제 흐름(엣지)·노드 피처 166개. 본문(`_research/wave1` F-033) — 203,769노드·234,355엣지·시점 49·불법 4,545(2%)·합법 42,019(21%)
- 방법·결과(본문, wave1 F-034·F-035): RF(AF+NE) precision 0.971/recall 0.675/F1 0.796이 최고, GCN 0.812/0.512/0.628. 시점 43 암시장 폐쇄 후 전 모델 성능 급락.
- 한계: 라벨 77% 미공개.
- 저장소 관련성: §8-8 — `blockchain-analytics.md` §11.2의 "RF 0.93/0.77/0.84, GCN 0.92/0.83/0.87 (Weber 2019)"는 논문 수치와 불일치.
- tier/confidence: T3/A (초록) + B (본문 수치는 wave1 검증). retrieved: 2026-10-21

### [P-062] [맥락·2023] Elmougy, Liu (2023). Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics. KDD 2023 (DOI 10.1145/3580305.3599803) / arXiv:2306.06108. 발표일 2023-05-25. — "Elliptic++" 데이터셋
- URL: https://arxiv.org/abs/2306.06108
- 유형: peer-reviewed
- 데이터: 초록 — **822k+ 지갑 주소(노드)·노드당 56 피처·1.27M 시간적 상호작용**, 4종 그래프
- 방법·결과: 거래 수준(Elliptic)에 주소 수준을 결합한 확장 데이터셋.
- 한계: —
- 저장소 관련성: §8-6 — `deep/papers.md`·`blockchain-analytics.md`의 "Elliptic++ (2022) ~840K txs, 1.6M addresses"는 **연도·규모 모두 불일치**.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-063] [맥락·2024] Bellei, Xu, Phillips, Robinson, Weber, Kaler, Leiserson, Arvind, Chen (2024). The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset. KDD MLF Workshop 2024 / arXiv:2404.19109. 발표일 2024-04-29 (v3 2024-07-29).
- URL: https://arxiv.org/abs/2404.19109
- 유형: workshop paper. Elliptic2 공개 논문
- 데이터: 초록 — **라벨 서브그래프 122K, 노드 클러스터 49M, 엣지 거래 196M**. 본문(wave1 F-036·F-037) — 라벨 서브그래프 121,810(합법 119,047/의심 2,763); GLASS F1 0.933·PR-AUC 0.208·ROC-AUC 0.889, 혼동행렬 TP 245/FN 46/FP 765/TN 11,125
- 방법·결과: AML을 서브그래프 분류로 재정의.
- 한계: F1 0.933과 PR-AUC 0.208의 괴리(§5-1).
- 저장소 관련성: §8-1·§8-7 — 제목 오기("Shape vs. Structure…")와 규모 오기("~122M txs") 정정.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-064] [맥락·2022/2024] Xiang, Lei, Bao, Ren, Li, Yang, Liu, Zhu, Choo (2022→2024). BABD: A Bitcoin Address Behavior Dataset for Pattern Analysis. IEEE TIFS 19, 2171–2185 (DOI 10.1109/TIFS.2023.3347894) / arXiv:2204.05746. arXiv 2022-04-10, 저널 2024.
- URL: https://arxiv.org/abs/2204.05746
- 유형: peer-reviewed
- 데이터: 2019-07-12~2021-05-26 Bitcoin 거래; **주소 유형 13종, 지표 5범주·피처 148개, 라벨 544,462건**
- 방법·결과: k-hop 서브그래프 알고리즘. kNN·DT·RF·MLP·XGBoost 5모델로 다중 분류 정확도 **93.24~97.13%**.
- 한계: 2021-05 이후 데이터 없음.
- 저장소 관련성: `deep/papers.md` "BABD-13 (Xiang 2022)" 항목에 저널·규모 추가.
- tier/confidence: T3/A. retrieved: 2026-10-21

### 2.8 기관 보고서 (방법론 비중)

### [P-065] European Central Bank (2026). Crypto-Asset Monitoring Expert Group (CAMEG) 2025 Conference — Book of abstracts. ECB Occasional Paper Series No. 382 (coord. Kochanska). 발표일 2026-03-23.
- URL: https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op382.en.pdf
- 유형: T2 (중앙은행 Occasional Paper; 개별 초록은 저자 개인 견해)
- 데이터: 2025-10-30~31 컨퍼런스 발표 초록 30여 편
- 방법·결과: 전체 판단 — "현재 크립토자산 위험과 중앙은행 영역에 대한 함의는 **제한적이거나 관리 가능**"(기존 규제·감독 틀 전제). 수록 초록 중 본 조사 관련: §2.1.2 MiCAR 자연실험(P-052), §2.7.2 오스트리아 CASP(P-053), §2.7.3 슬로바키아 스캠(P-054), §2.10.2 PET 분류(P-034), §2.10.3 PET 통합 분류(Nardelli), §2.5.1 **MIDAS — EU 수준 크립토 시장 감시**, §2.6.3 크립토 데이터 신뢰성. 2026년 계획: 온·오프체인 데이터 공동 탐색, **지리적 위치 식별 방법론·지표 개발**, 공동 데이터셋·대시보드. 다음 컨퍼런스 2026-10 말.
- 한계: 초록집 — 본문·수치 없음.
- 저장소 관련성: `deep/reports.md` §7 BIS·IMF 섹션에 ECB 항목 신설. `notes/2-regulations/eu-mica-amlr.md`에 "MiCAR 효과 실증은 ECB CAMEG에서 진행 중" 추가.
- tier/confidence: T2/A. retrieved: 2026-10-21

### [P-066] Bank for International Settlements (2026). Annual Economic Report 2026, Chapter III: Anchoring trust in money: innovation beyond stablecoins. 발표일 2026-06-23.
- URL: https://www.bis.org/publ/arpdf/ar2026e3.htm
- 유형: T2
- 데이터: 시가총액 2026-05 말 기준, 거래량 2025년 추정
- 방법·결과: 스테이블코인은 토큰화의 잠재력을 보이나 "화폐의 기초 속성"에 미달하고 **금융 무결성을 위협**. 인용: "Experience to date suggests that stablecoins account for a significant share of illicit on-chain activity." 공개 permissionless 체인의 "pseudonymity and the use of unhosted wallets can undermine KYC and AML/CFT compliance"; 믹서·크로스체인 브리지가 흐름을 가림. 발행자 동결·분석업체 지원은 "cannot replace routine, large-scale AML/CFT controls in everyday payments." 권고: permissioned 플랫폼에 AML/CFT·제재 스크리닝 내장("Integrity by design"), 규제차익 방지를 위한 국제 정합성. 수치: 법정화폐 담보 스테이블코인의 **99.4%가 USD 페그**, 시가총액 **3,200억 달러**(2026-05 말), 2025년 거래량 **28조 달러**(동일 주체 지갑 간 이전 포함 총액 — 순액은 "훨씬 낮음"). Box C: EU 비은행 발행자 자기자본 최소 35만 유로, 싱가포르 S$100만 또는 연 운영비 50% 중 큰 값·5영업일 내 환매, 홍콩 1영업일 내 환매, 영국 제안 40% 이상 무이자 중앙은행 예치·최대 60% 단기 국채.
- 한계: "상당 부분"의 출처·정량치 미기재(분석업체 수치 인용 추정). 정책 보고서.
- 저장소 관련성: `deep/reports.md` §7 갱신. `notes/2-regulations/fatf.md`·`korea-fiu-act.md`의 스테이블코인 발행자 AML 의무 논의와 연결.
- tier/confidence: T2/A. retrieved: 2026-10-21

### [P-067] Financial Stability Board (2026). Global Stablecoin Arrangements: Cross-border vulnerabilities and financial stability monitoring (Report to the G20). 발표일 2026-10-12. — 관련: FSB Thematic Review on the Global Regulatory Framework for Crypto-asset Activities (2025-10-16, 페이지 내 언급); Promoting Global Financial Stability: 2025 FSB Annual Report (2026-03-24).
- URL: https://www.fsb.org/2026/10/global-stablecoin-arrangements-cross-border-vulnerabilities-and-financial-stability-monitoring/ ; https://www.fsb.org/2026/03/promoting-global-financial-stability-2025-fsb-annual-report/
- 유형: T2
- 데이터: 현행 데이터 소스의 편익·한계 평가(PDF 본문 미열람)
- 방법·결과: 글로벌 스테이블코인을 "inherently cross-border and cross-sectoral issue"로 규정, 취약성 전파 경로·**모니터링 지표·가용 데이터 소스와 한계**를 정리. 단일 관할이 전체를 평가·대응하기 어렵다는 점 명시. 2025-10-16 주제별 검토는 "진전은 환영하나 격차·불일치 잔존". 2025 연차보고서 페이지는 크립토 프레임워크·GSC의 "full and consistent implementation"을 2025년 중점으로만 언급.
- 한계: 웹페이지 요약만 확인, PDF 본문 수치 미확인. AML 언급 없음.
- 저장소 관련성: `deep/reports.md` — FSB 항목 신설(현재 없음).
- tier/confidence: T2/B (웹 요약). retrieved: 2026-10-21

### [P-068] 분석업체 C (2026). 2026 Crypto Crime Report — 서론 포스트 "Crypto Crime Reaches Record High in 2025 as Nation-State Sanctions Evasion Moves On-Chain at Scale". 발표일 2026-01-08.
- URL: https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/
- 유형: T3 (industry)
- 데이터: 자사 귀속 주소 데이터
- 방법·결과(방법론 중심): 2025년 불법 주소 수취액 **최소 1,540억 달러**(전년 대비 162%↑); 귀속 거래량의 **1% 미만**; **2024년 수치를 409억→572억 달러로 상향 수정**; 스테이블코인이 불법 거래량의 84%; 제재 대상 수취액 694%↑, 특정 루블 연동 토큰 1년 미만 933억 달러; DPRK 탈취 20억 달러. 방법론 인용: "we must caveat that this figure represents a lower-bound estimate"; "A year from now, these totals will be higher as we continue to identify more illicit addresses"; 비크립토 원천 범죄 제외("Such transactions are virtually indistinguishable from licit transactions in on-chain data"); 비중 분모 = "all inflows to known services across all the assets that we track"(내부 이전 제외).
- 한계: 서론 페이지에는 **스캠 총액·자금세탁 총액 없음**(`deep/reports.md`의 "$17B", "$82B"는 본문 확인 필요 — §8-19). 귀속 기준 비공개.
- 저장소 관련성: `deep/reports.md` §1 — 하한·수정 관행·분모 정의를 명시해야 함.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-069] 분석업체 T (2026). 2026 Crypto Crime Report. 발표일 2026-01-28.
- URL: https://www.trmlabs.com/reports-and-whitepapers/2026-crypto-crime-report
- 유형: T3 (industry)
- 데이터: 자사 귀속 데이터
- 방법·결과(방법론 중심): 2025년 불법 흐름 **1,580억 달러**(전년 대비 약 145%↑), 온체인 거래량의 **1.2%**(2024년 1.3%), 신설 지표 **가용 유동성의 2.7%**(VASP 유출입 대비). 범주별 증가: 제재 >400%, 블록리스트 32%, 해킹·탈취 31%, 다크넷 20%, 불법 재화·서비스 12%. 해킹 28.7억 달러·약 150건(단일 사건 14.6억 달러), 사기 약 350억 달러, 마약 34억 달러 이상. 방법론 인용: "We treat this estimate as a conservative baseline — a minimum, or 'floor'"; "The illicit volume metric is intended to capture the revenue generated by illicit actors"; "Illicit activity on blockchains is frequently identified with delay"; "a dynamic baseline rather than a fixed measurement."
- 한계: 유동성 지표의 분모가 본문("incoming VASP flows")과 방법론("VASP outflows") 간 **불일치**(§5-5). 사기 350억 vs 타사 추정 차이는 정의 차.
- 저장소 관련성: `deep/reports.md` §2 — 보고서명("Annual Crypto Threats Report"가 아님)과 수치 갱신.
- tier/confidence: T3/A. retrieved: 2026-10-21

### [P-070] 분석업체 E (2025). Typologies Report 2025 — "Innovating to fight financial crime in an age of rapid change". 발표일 2025-09-30.
- URL: https://www.elliptic.co/insights/elliptics-typologies-report-innovating-to-fight-financial-crime-in-an-age-of-rapid-change/
- 유형: T3 (industry)
- 데이터: 자사 조사 사례(방법론 미기재)
- 방법·결과: 2018-10부터 연간 발간. 2025년판 5개 트렌드 — AI 활용 스캠(AI 생성 신분증으로 KYC 우회·딥페이크), 산업화된 pig butchering(중국어 보증 마켓플레이스, 자기수탁 지갑 풀링·peeling chain), 제재 회피의 스테이블코인, 카르텔(현금→크립토, 크립토 ATM), 크로스체인 범죄(브리지·DEX·스왑). 인용: "most major stablecoins today are designed to contain a freezing functionality".
- 한계: **유형론 도출 방법론(표본·선정 기준) 미기재.** 2026년판은 조사 시점에 미확인.
- 저장소 관련성: `deep/reports.md` §3 갱신; `onchain-typology.md` AI 스캠 유형 추가 근거.
- tier/confidence: T3/B. retrieved: 2026-10-21

---

## 3. 연구 공백·미해결 질문

1. **트래블룰 효과 실증의 부재.** 2025~2026년에 트래블룰·VASP 등록 의무가 거래량·불법 비중·sunrise 지연에 미친 인과 효과를 추정한 동료심사 논문을 찾지 못했다. 가장 가까운 선행은 2020년 이벤트 스터디(P-055). ECB CAMEG의 MiCAR 자연실험(P-052)이 중앙은행 측 최초 설계이나 초록만 공개. → FATF 6차 타겟업데이트(2025-06-26, 99개 관할 입법)의 관할별 시행일을 패널 데이터로 삼는 연구가 가능한 시점이다.
2. **한국 법학 문헌 미확보.** 특정금융정보법·가상자산이용자보호법 관련 2025년 법학 학술지 논문을 RISS(서버 오류)·DBpia(검색 0건)·KCI(접근 불가)에서 확보하지 못했다. 세션 웹 검색 할당량 소진이 직접 원인이며, 문헌이 없다는 결론은 **아니다**. 다음 단계: KCI·DBpia에서 「가상자산 이전 시 정보제공」「가상자산사업자 자금세탁방지」「시세조종 가상자산」 키워드로 2025~2026 필터 재검색.
3. **개념 표류(concept drift) 운영 연구.** 배포 후 성능 저하를 다룬 유일한 2026 논문(P-012)이 철회됐다. Weber 2019의 암시장 폐쇄 결과(P-061)가 여전히 핵심 근거. 가상자산 특유의 이벤트(믹서 제재·브리지 해킹·스테이블코인 동결)를 트리거로 하는 재학습 프로토콜 연구가 없다.
4. **적대적 회피.** IEEE SaTML 2026 채택 논문 "The Feature-Space Illusion"(§7-1)이 유일하게 확인된 2026 문헌이나 초록 미열람. GNN AML 탐지기에 대한 경제적 동기 공격자 모델링은 사실상 공백.
5. **자기수탁 지갑 소유 검증.** 서명·마이크로트랜잭션·셀프디클레어 방식의 **학술 평가 논문 없음**(벤더 문서만 존재). 서명이 "통제"는 증명하나 "수익적 소유"는 증명 못 한다는 문제의 형식화가 필요.
6. **거래소 핫월렛 식별의 2025 실측.** 입금주소 재사용·스윕 패턴 기반 식별의 정밀도를 공개 ground truth로 평가한 2025~2026 논문을 찾지 못했다.
7. **Lightning 2025.** 온체인 휴리스틱형 논문은 없고 네트워크 계층 사이드채널(P-024)만 확인. 저자 명단조차 1차 페이지에서 미확인.
8. **LLM AML 평가의 합성 데이터 의존.** P-025~P-028 전부 합성·시뮬레이션. 가상자산 원천 STR·알람 코퍼스로 평가한 연구 없음. 인용 유효성(0.98)과 판단 정확도(F1 0.62)의 괴리(P-026)가 시사하는 "그럴듯한 근거 제시" 위험은 감독 대응에서 중대.
9. **사기 피해 규모 추정 방법론.** 업계 추정(사기 350억 달러, P-069)과 신고 기반 추정의 승수(underreporting multiplier) 선택 문제를 다룬 학술 논문은 미발견. P-047(5.21억 달러)의 추정법도 초록에 없음.
10. **크로스체인 벤치마크 통일.** P-006(12개 브리지, F1 91.75%), P-007(5개, 0.9746), P-016(1개, 67.55~99.65%)은 브리지 집합·정의·지표가 달라 비교 불가. 공통 ground truth 벤치마크 부재.
11. **가상자산 네이티브 공개 라벨 데이터셋의 정체.** 2025~2026 신규 공개 데이터셋은 rug pull(P-044, P-041), 피싱(P-010), 합성 결제(P-056) 위주. Elliptic·Elliptic2 이후 **자금세탁 라벨** 비트코인/이더리움 데이터셋 신규 공개 없음.

---

## 4. 데이터셋·코드 공개 현황

| 데이터셋/코드 | 연도 | 체인 | 규모 (초록·공개 페이지 확인치) | 라벨 | 공개 | 근거 |
|---|---|---|---|---|---|---|
| Elliptic | 2019 | BTC | 거래 203,769 노드·234,355 엣지·피처 166·시점 49 | 불법 4,545(2%)·합법 42,019(21%) | 공개 | P-061 |
| Elliptic++ | 2023 | BTC | 주소 822k+·피처 56·시간 상호작용 1.27M (+Elliptic 거래) | 거래·주소 양 수준 | 공개(논문 기준; 저장소 URL 미확인) | P-062 |
| Elliptic2 | 2024 | BTC | 라벨 서브그래프 122K(121,810)·노드 클러스터 49M·엣지 196M | 합법 119,047 / 의심 2,763 | 공개 | P-063 |
| BABD-13 | 2022/24 | BTC | 라벨 544,462·피처 148·13 유형 (2019-07-12~2021-05-26) | 13 행태 유형 | 공개 | P-064 |
| RevTrack 코드 | 2024 | (Elliptic2) | — | — | GitHub MITIBMxGraph/RevTrack | P-014 |
| GNN 초기화·정규화 프레임워크 | 2026 | (Elliptic) | — | — | 공개(초록 명시) | P-005 |
| SolRPDS | 2025 | Solana | 스캔 36.9억 건 → 의심 풀 62,895·토큰 22,195 (2021~2024) | 비활성·유동성 주석 | 공개 | P-044 |
| RugScreener 데이터셋 | 2025 | ETH | 비라벨 1,882,114 tx/29,595 토큰; 라벨 128,819 tx/1,000 토큰 | rug pull 500 / 정상 500 | 논문 기준 신규 구축(공개 여부 미확인) | P-041 |
| LROO 라벨셋 | 2026 | 다수 | 토큰 프로젝트 1,000 | 수작업 | 미확인 | P-043 |
| SoK rug pull 데이터셋 | 2025 | DeFi | 2,391건, 35 유형 중 82.9% 커버 | 유형 라벨 | 미확인 | P-040 |
| PhishEye | 2026 | ETH | 주소 161,658·거래 416,541 | 피싱 | 미확인 | P-010 |
| xfraud (PDHG) | 2025 | ETH | **구성 미기재** | 피싱 | Mendeley CC BY 4.0 | P-060 |
| TransXion | 2026 | 합성 결제 | 거래 300만·개체 5만 | 비템플릿 불법 서브그래프 | 코드·데이터 공개 | P-056 |
| Address poisoning 탐지 | 2025 | ETH·BSC | 공격 2.7억·피해자 1,700만·사고 6,633 | 공격/피해 | 미확인 | P-036 |
| 상태불변 트랜잭션 | 2026 | ETH·OP·Base | 약 14억 건 | 분류 | 미확인 | P-038 |
| CtPhish | 2026 | 오프체인 | 사이트 5,138·앱 10,612 | 피싱 | 미확인 | P-039 |
| DeFi 익스플로잇 큐레이션 | 2025 | EVM 8체인 | 298 익스플로잇·402 거래·37.4억 달러 (2020~2025) | 공격 | 미확인 | P-046 |
| AMLGuard 사건셋 | 2026 | 다중 | 세탁 사건 82건·>10억 달러 | 사건 | 미확인 | P-008 |
| ConneX 매칭셋 | 2025 | 5 브리지 | 약 50만 건 | 매칭 쌍 | 미확인 | P-007 |
| Railgun·Hinkal 분석 | 2026 | 6 EVM | unshield 186,356건 | — | 미확인 | P-018 |
| Tornado Cash 제재 측정 | 2025 | ETH | 957일·블록 679만·거래 10.7억 | — | 미확인 | P-049 |
| USDT·USDC 동결 데이터 | 2026 | ETH | 2017-11~2025-08, 동결 >15억 달러 | 동결·인출 | 미확인 | P-050 |

> "미확인"은 초록·공개 페이지에 저장소 URL이 없었다는 뜻이며, 비공개 단정이 아니다.

---

## 5. 상충·주의 사항

| # | 쟁점 | 근거 A | 근거 B | 판단·주의 |
|---|---|---|---|---|
| 1 | **F1과 PR-AUC의 괴리** | Elliptic2 GLASS F1 0.933 (P-063) | 동일 모델 PR-AUC 0.208, 정밀도 245/(245+765)≈24% | 극단 불균형에서 F1 산출 방식에 따라 숫자가 다수 클래스에 지배됨. 저장소 비교표에 F1만 적는 관행 중단 |
| 2 | **시뮬레이션 성능의 실데이터 이전** | P-027 F1 98.2% (시뮬레이션) | P-056: 현실적 벤치마크에서 기존 모델 점수 급락 | 합성·템플릿 벤치마크 수치는 실무 성능 지표로 인용 금지 |
| 3 | **철회 논문** | P-012 (2026-04-24 철회), P-019 (2025-11-18 철회) | — | 수치 인용 금지. 정정판 추적 |
| 4 | **불법 규모 총액의 분모** | 1,540억 달러, 귀속 서비스 유입 대비 <1% (P-068) | 1,580억 달러, 온체인 거래량 1.2%, VASP 유동성 2.7% (P-069) | 두 보고서 모두 "하한·동적 기준선". 분모 정의가 달라 비중 비교 불가 |
| 5 | **유동성 지표 분모 불일치** | P-069 방법론: VASP outflows | P-069 본문: incoming VASP flows | 보고서 내부 불일치. 인용 시 "정의 불명확" 병기 |
| 6 | **크로스체인 추적 정확도** | ABCTracer F1 91.75%/12 브리지 (P-006) | ConneX 0.9746/5 브리지 (P-007); 단일 브리지 67.55~99.65% (P-016) | 브리지 집합·매칭 정의 상이 → 단일 표로 합치지 말 것 |
| 7 | **Address poisoning 수치 버전 차** | P-036 v3 초록: 공격 2.7억·피해자 1,700만·손실 8,380만 달러 | 2차 요약(검색 스니펫)의 1,700만 시도·130만 사용자·7,930만 달러 | 본 조사는 v3 초록만 확인. v1 수치는 미확인 — 인용 시 버전 명시 |
| 8 | **자동 생성 벤더 "corpus" 페이지** | 검색 결과에 다수 노출된 `…/corpus/gen-NNNN/…` 페이지 | 비문·반복 서술 다수 | 연구 출처로 사용 금지(T5). 본 문서는 한 건도 인용하지 않음 |
| 9 | **리뷰의 2차 종합치** | P-015 "그래프 어텐션이 규칙 기반 대비 40% 이상 우위" | 지표·기준선 미기재 | 저장소 수치로 전사 금지 |
| 10 | **자체 보고 운영 수치** | P-029 "45분→8초, 정확도 >90%" | 평가 프로토콜 미기재 | "저자 자체 보고"로만 인용 |
| 11 | **Monero 추적 가능성 서술** | P-023: 버그 기반 휴리스틱은 고정밀, 2023 패치로 신규 거래 무효 | 저장소: "거의 분석 불가/완전 추적 불가 지속" | 시기 구분 필요(§8-15) |
| 12 | **제재 효과의 양면성** | P-049: 입금 71.03% 감소 | P-049: 보안사고 78.33%가 여전히 경유 | "효과 있음/없음" 이분법 금지 |

---

## 6. 출처 레지스트리

| source_id | 기관/DB | URL | tier | 접근 | 본 조사 결과 |
|---|---|---|---|---|---|
| src:arxiv | arXiv (cs.CR, cs.LG, cs.CE) | https://arxiv.org | T3 | 공개 | 초록 페이지 42건 직접 확인 |
| src:crossref | Crossref API | https://api.crossref.org | T3(서지) | 공개 | Alarab 2020·Möser&Böhme 2017·Lorenz 2020·Androulaki 2013·Harlev 2018·Feinstein&Werbach 서지 확인; 간헐적 429 |
| src:acm-dl | ACM Digital Library | https://dl.acm.org | T3 | 등록/유료 | **403** (Alarab 2020·TOIT Lightning 초록 미열람) |
| src:ieee-xplore | IEEE Xplore | https://ieeexplore.ieee.org | T3 | 유료 | 미접근(기관 리포지터리로 대체) |
| src:ios-press | IOS Press ebooks (ATDE) | https://ebooks.iospress.nl | T3 | 공개 초록 | P-029 확인 |
| src:springer-eann | Springer EANN 2026 | (arXiv 경유) | T3 | — | P-005 |
| src:jucs | JUCS | https://lib.jucs.org | T3 | 공개 | 서지만 확인, 초록 미렌더링 (§7-2) |
| src:doaj | DOAJ | https://doaj.org | T3 | 공개 | **403** |
| src:koreascience | KoreaScience | https://www.koreascience.kr | T3 | 공개 | P-051 확인; 검색 URL 404 |
| src:kci | KCI | https://www.kci.go.kr | T3 | 공개 | 미접근(검색 할당량 소진) |
| src:riss | RISS | https://www.riss.kr | T3 | 공개 | 검색 **500** |
| src:dbpia | DBpia | https://www.dbpia.co.kr | T3 | 등록 | "가상자산 트래블룰" **0건** |
| src:aston-pure | Aston Research Explorer | https://research.aston.ac.uk | T3 | 공개 | P-032·P-033 |
| src:bit-pure | BIT Pure | https://pure.bit.edu.cn | T3 | 공개 | P-020 |
| src:cityu | CityU Scholars | https://scholars.cityu.edu.hk | T3 | 공개 | P-041 |
| src:ajman | Ajman Univ. Research | https://research.ajman.ac.ae | T3 | 공개 | P-015 |
| src:comillas | Comillas Repositorio | https://repositorio.comillas.edu | T3 | 공개 | P-058 |
| src:ubb | Studia UBB Informatica | https://studia.reviste.ubbcluj.ro | T3 | 공개 | P-013 |
| src:cae | Strategic Study of CAE | https://www.engineering.org.cn | T3 | 공개 | P-059 |
| src:ndss | NDSS Symposium | https://www.ndss-symposium.org | T3 | 공개 PDF | P-039 (PDF 1면 로컬 추출) |
| src:issta | ISSTA 2025 (researchr) | https://conf.researchr.org | T3 | 공개 | P-040 |
| src:eccws | ECCWS proceedings | https://papers.academic-conferences.org | T3 | 공개 | P-048 |
| src:satml | IEEE SaTML 2026 accepted list | https://satml.org/2026/accepted-papers/ | T3 | 공개 | §7-1 제목·저자 확인 |
| src:tud | TU Dresden 공지 | https://tu-dresden.de | T3 | 공개 | P-024 |
| src:mendeley | Mendeley Data | https://data.mendeley.com | T3 | 공개 | P-060 |
| src:ecb-op | ECB Occasional Papers | https://www.ecb.europa.eu/pub/pdf/scpops/ | T2 | 공개 PDF | P-065 (로컬 텍스트 추출) |
| src:bis-aer | BIS Annual Economic Report | https://www.bis.org/publ/arpdf/ | T2 | 공개 | P-066 |
| src:fsb | FSB publications | https://www.fsb.org/publications/ | T2 | 공개 | P-067 |
| src:imf | IMF Publications | https://www.imf.org | T2 | 공개 | 검색 URL 404 — 2차 추적기로 제목만 (§7-7) |
| src:kcmi | 자본시장연구원 보고서 | https://www.kcmi.re.kr/report/report_list | T3 | 공개 | 최근 4건만 노출; AML 관련 없음 (§7-8) |
| src:bok | 한국은행 간행물 | https://www.bok.or.kr | T2 | 공개 | 검색 URL 오류 페이지 (§7-9) |
| src:vendor-c | 분석업체 C 블로그 | https://www.chainalysis.com/blog/ | T3 | 공개 | P-068 |
| src:vendor-t | 분석업체 T 보고서 | https://www.trmlabs.com/reports-and-whitepapers | T3 | 등록 | P-069·P-035 |
| src:vendor-e | 분석업체 E 인사이트 | https://www.elliptic.co/insights/ | T3 | 공개 | P-070 (corpus 페이지는 제외) |

---

## 7. 미확인·다음 단계

1. [ ] **Frankart, Simonetto, Cordy, Papageorgiou, Pocher, Fridgen (2026). The Feature-Space Illusion: Exposing Practical Vulnerabilities in Blockchain GNN Fraud Detection. IEEE SaTML 2026** — 채택 목록(Group 2, 2026-03-24 세션)에서 제목·저자 확인. **초록 미열람**(ORBilu 인증서 오류). → ORBilu 10993/68067 또는 IEEE Xplore 확인 후 §2.1에 승격.
2. [ ] **Cengiz, Gök (2025). Anti Money Laundering in Bitcoin Network Using Chaotic Time Series and Graph Convolution Network. JUCS 31(11), 1175–1195, DOI 10.3897/jucs.135907 (2025-09-28)** — 서지 확인, 초록 미렌더링. 검색 스니펫의 "F1 92.3%"는 **미확인**.
3. [ ] **P-024 저자 명단** — ACM DL 10.1145/3810239 접근 필요.
4. [ ] **Ordekian et al., eCrime 2024 (UCL Discovery 10197431)** — 403. 사기 플랫폼 유형(거래소 사칭 33건·허위 거래 플랫폼 124건은 스니펫 기준 미확인).
5. [ ] **DFRWS EU 2026 paper 116** (Focal Loss·LSTM·PageRank 기반 비트코인 불법 탐지) — 403.
6. [ ] **P-046 검색 요약의 "탐지 정확도 97%·미지 공격 F1 82.0%"** — 초록에 없음, 본문 확인 필요.
7. [ ] **IMF 2026 스테이블코인 문헌** — 2차 추적기 기준 제목만: "From Par to Pressure: Liquidity, Redemptions, and Fire Sales with a Systemic Stablecoin"(WP, 2026-01-16), "Stablecoins in Nigeria: A Growing Cross-Border Channel"(2026-06-16), "Stablecoins – Promise, risks, and policy choices for emerging markets"(2026-08-07), "international stablecoin flows"(2025-07-11), "understanding stablecoins"(2025-12-04). imf.org 원문 미확인 — AML 관련성 평가 보류.
8. [ ] **자본시장연구원** — 목록 최근 4건 중 「K-자본시장 정책시리즈 2: 자본시장 토큰화의 확산」(정화영, 2026-10-06)만 확인(AML 아님). 2025~2026 가상자산·스테이블코인 AML 관련 보고서는 사이트 내 검색 필요.
9. [ ] **한국은행 2025~2026 스테이블코인·가상자산 보고서** — 간행물 검색 URL이 오류 페이지로 리다이렉트. 이슈노트 목록 직접 열람 필요.
10. [ ] **한국 법학 학술지 2025 논문(특금법·이용자보호법·트래블룰)** — 미확보(§3-2).
11. [ ] **분석업체 C 2026 보고서 본문** — 스캠 총액·자금세탁 총액(`deep/reports.md`의 $17B·$82B) 서론 페이지에 없음. 본문 PDF 확인 필요.
12. [ ] **분석업체 E 2026 Typologies Report / 2025 Cross-chain Crime Report** — 미열람.
13. [ ] **Garantex 사례 연구(University of Tartu)** — 접속 거부. 학위논문 여부 미확인.
14. [ ] **소비자단체의 2025 미국 크립토 사기 손실 추정(승수 7.1)** — 검색 스니펫만, 원문 미열람. §3-9 방법론 비판에 활용하려면 원문 필요.
15. [ ] 2차 요약으로만 접한 2025 논문: Srifa et al. (Blockchain: Research and Applications, 2025-09, Uniswap rug pull 시계열), HNN4RP (JEIT 2025-10), PDHG 본 논문(ESWA 투고), Fan et al. arXiv:2503.10058(모바일 AML DL 리뷰), Prosolov et al. 2025(Ethereum 계정) — 초록 미열람.
16. [ ] 2024년 맥락 문헌 중 미열람: Dekhil et al. (IEEE BCCA 2024, CoinJoin ML), JoinDetect (GoodIT '24), CENSor (IEEE Access 2024), MixBroker (2024).

---

## 8. 기존 저장소 내용과의 차이·정정 제안

> 대상: `deep/papers.md`, `deep/reports.md`, `notes/4-technology/blockchain-analytics.md`, `curriculum/day_57.md`. 본 문서는 **제안**이며 해당 파일은 수정하지 않았다.

| # | 파일·위치 | 현재 서술 | 확인 결과 | 제안 |
|---|---|---|---|---|
| 1 | `deep/papers.md` "AML·온체인 분석 핵심 논문 > GNN" ; `blockchain-analytics.md` 123·661·685행 | Bellei et al. (2024) *Shape vs. Structure: Topology-Aware Self-Supervised Learning for AML on Elliptic2* | 해당 제목의 논문은 arXiv에 없음. 실제 제목: *The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset* (arXiv 2404.19109, KDD MLF Workshop 2024). `deep/papers.md` §4에는 바른 제목이 있어 **같은 파일 안에서 이중 표기** | 제목 통일. "Self-supervised"·"topology-aware" 서술 삭제(원논문은 지도학습 서브그래프 분류) |
| 2 | `deep/papers.md` "Alarab et al. (2020) … (ICDM) … F1 0.84→0.90" ; `blockchain-analytics.md` 650행 "GAT 0.94/0.86/0.90 Alarab 2020" | ICDM 게재, GAT 성능 | Crossref: *Competence of Graph Convolutional Networks for Anti-Money Laundering in Bitcoin Blockchain*, **ACM ICMLT 2020** (DOI 10.1145/3409073.3409080). 초록은 ACM 403으로 미열람 → F1·GAT 수치 **미검증**(CTR:00007도 "미검증"으로 남김) | 학회명 정정. 수치는 원문 확인 전까지 삭제 또는 "미검증" 표기 |
| 3 | `deep/papers.md` "Möser & Böhme (2017) … (ESORICS)" ; `blockchain-analytics.md` 658행 | ESORICS | Crossref: **IEEE EuroS&PW 2017** (DOI 10.1109/eurospw.2017.48) | 학회명 정정 |
| 4 | `deep/papers.md` §1 "Androulaki et al. (2013) … ESORICS 2013" | ESORICS | Crossref: **FC 2013** (LNCS, DOI 10.1007/978-3-642-39884-1_4). 같은 파일 아래 섹션은 FC로 바르게 표기 | ESORICS → FC 통일 |
| 5 | `deep/papers.md` "Harlev et al. (2018)" (학회 미기재) | — | **HICSS 2018** (DOI 10.24251/hicss.2018.443) | 학회·DOI 추가 |
| 6 | `deep/papers.md` "Elliptic++ (2022) — 840K tx, 1.6M addresses" ; `blockchain-analytics.md` 634행 | 2022, 840K tx, 1.6M 주소 | arXiv 2306.06108 (2023-05-25; KDD 2023): **주소 822k+, 피처 56, 시간 상호작용 1.27M** | 연도 2023, 규모 정정 (P-062) |
| 7 | `blockchain-analytics.md` 635행 "Elliptic2 … ~122M txs, 196M transactions" ; `deep/papers.md` "122M txs" | 1.22억 거래 | 초록: **라벨 서브그래프 122K**, 노드 클러스터 49M, 엣지 거래 196M | "122K labeled subgraphs" 로 정정 (P-063) |
| 8 | `blockchain-analytics.md` 648~649행 "Random Forest 0.93/0.77/0.84, GCN 0.92/0.83/0.87 — Weber 2019" | 해당 수치 | 논문(wave1 F-034): RF(AF+NE) **0.971/0.675/0.796**, GCN **0.812/0.512/0.628** | 수치 교체. "Elliptic/Elliptic2 기준 Bitcoin clustering" 표 제목도 오류(Weber는 클러스터링 아님) |
| 9 | `blockchain-analytics.md` 76~83행(§2.A 실증 정확도 표), 112~118행(§2.B 결합 정확도 표), 643~651행(§11.2 표) | CIOH 0.95~0.98/0.99/0.97(Meiklejohn 2013), CoinJoin 샘플 0.75/0.98/0.85(Möser&Böhme 2017), Elliptic2+Fingerprint 0.95/0.92/0.93(Bellei 2024), "CIOH+Change 0.91/0.95/0.93 Androulaki 2013", "Shape-based SSL 0.96/0.89/0.92" | **CTR:00007(2026-08-04)이 확정한 날조 수치와 동일 계열.** CTR은 `onchain-typology.md`·`day_30.md`만 정정했고 이 파일 3곳은 잔존. Meiklejohn 2013·Möser&Böhme 2017·Androulaki 2013·Bellei 2024 어느 논문도 해당 P/R/F1을 보고하지 않음 | 3개 표 삭제. 대체: Möser & Narayanan FC 2022의 "개별 휴리스틱 TPR 10~30%, RF ROC-AUC 0.999·FPR 0.1%에서 TPR 82%"(wave1 F-006·F-007) 및 "표준화된 정확도 수치 부재"라는 분야 입장 |
| 10 | `blockchain-analytics.md` 118행 "ML 기반 CoinJoin 분류기(GNN) 0.97/0.94 — Chainalysis Behavior 추정", 652행 "Chainalysis Behavior ~0.97 claim" | 벤더 추정치 | 출처 없음 | 삭제 |
| 11 | `deep/papers.md` §5 "Sun et al. (2023) — Analysis of Cross-Chain Bridges: Security and Efficiency" | 존재하는 논문으로 기재 | Crossref 서지 검색에서 해당 제목·저자·연도 일치 결과 **없음** | 삭제 후 P-006·P-007·P-016·P-057로 교체 |
| 12 | `deep/papers.md` §4 "Lorenz et al. (2020) — Machine learning methods to detect money laundering in the Bitcoin blockchain" | 제목 일부 | 정식 제목은 "… **in the presence of label scarcity**" (ACM ICAIF 2020, DOI 10.1145/3383455.3422549) — 라벨 희소성이 논문의 핵심 | 제목 보완 |
| 13 | `deep/papers.md` "BABD-13 (Xiang 2022) — 13 behavior classes" | 연도·규모 간략 | arXiv 2022-04, **IEEE TIFS 19 (2024)**; 라벨 544,462·피처 148·정확도 93.24~97.13% | 저널·규모 추가 (P-064) |
| 14 | `blockchain-analytics.md` §5.5 "정확도 벤치마크(공개+추정)" 표 (Polygon 97~99%, LayerZero Generic 40~60% 등) | 출처 없는 브리지별 정확도 | 동료심사·프리프린트 실측치: 12 브리지 F1 91.75%(P-006), 5 브리지 F1 0.9746(P-007), Ethereum–Polygon 입금 93.04~99.65%/출금 67.55~92.78%(P-016) | 표를 실측치 3건으로 교체하고 "비교 불가" 주석(§5-6) |
| 15 | `blockchain-analytics.md` 535행 "Privacy coin (Monero) 거의 분석 불가", 605행 "완전 추적 불가는 지속" | 전면 불가 | P-023: 2019~2023 지갑 버그·P2Pool·Mordinal 휴리스틱은 **고정밀**, 10 Block Decoy Bug는 2023 초 패치로 신규 거래 무효 | "패치 이전 구간은 부분 추적 가능, 이후는 아니다"로 시기 구분 |
| 16 | `deep/papers.md` §3 Travel Rule — 화이트페이퍼·Wolfsberg만 | 학술 문헌 없음 | P-031~P-034 (2025) | 동료심사 문헌 4건 추가 |
| 17 | `deep/papers.md` §7 "한국 … 기술 중심 논문은 드뭅니다" | 단정 | P-051(융합보안논문지 2025)이 반례 | "드물다"는 유지 가능하나 사례 1건 추가. 법학 논문은 본 조사에서 미확보임을 명시 |
| 18 | `deep/papers.md` §4 ML 섹션 전체 | 2024 Bellei에서 종료 | 2025~2026 문헌 P-001~P-015, 서베이 P-015·P-058·P-059 | 섹션 신설 "2025~2026" |
| 19 | `deep/reports.md` §1 "2026: $154B, 162%, 84% stablecoin … Money Laundering ($82B) … Scams ($17B)" | 수치 나열 | $154B·162%·84%·$93.3B·DPRK $2B는 서론 포스트(2026-01-08)와 일치. **$82B·$17B는 서론에 없음**. 하한 추정·2024년 $40.9B→$57.2B 상향 수정·분모 정의가 누락 | 미확인 2건은 본문 확인 전 "출처 확인 필요" 표기; 방법론 3문장 추가 (P-068) |
| 20 | `deep/reports.md` §2 "TRM — Annual Crypto Threats Report" | 보고서명 | 2026년판 정식 명칭 "2026 Crypto Crime Report"(2026-01-28); $158B·1.2%·유동성 2.7%·사기 ~$35B | 명칭·수치·"dynamic baseline" 방법론 추가 (P-069); 유동성 지표 분모 불일치 주석 |
| 21 | `deep/reports.md` §7 BIS·IMF | 일반 안내만 | BIS AER 2026 Ch. III(2026-06-23), ECB OP 382(2026-03-23), FSB GSC note(2026-10-12)·주제별 검토(2025-10-16) | 항목 신설 (P-065~P-067). FSB·ECB 섹션 추가 |
| 22 | `deep/reports.md` §3 Elliptic | "Crypto Crime Reports" 일반 | 2025 Typologies Report(2025-09-30) 5개 트렌드 | 갱신 (P-070) |
| 23 | `curriculum/day_57.md` "LLM in AML … STR 초안 … 30% 시간 단축 보고" | 출처 없는 수치 | 학술 문헌의 자체 보고치는 P-029(45분→8초)만 존재; P-025는 수치 없음 | 출처 없는 30%는 삭제하거나 P-029 "자체 보고"로 교체. P-026의 인용 유효성 0.98 vs Escalate F1 0.62를 "설명가능성" 절에 추가 |
| 24 | `curriculum/day_57.md` "Scam 사전 탐지 실용도 하~중" | 평가 | P-010(실배포 1,803 주소), P-039(5,138 사이트), P-041(균형정확도 95.7%) | "중" 이상으로 재평가 검토, 근거 병기 |
| 25 | `curriculum/day_57.md` "Adversarial adaptation … 지속 이슈" | 일반 서술 | SaTML 2026 논문(§7-1) 존재; P-012 철회 | 문헌 포인터 추가(초록 확인 후) |
| 26 | `curriculum/day_57.md` "Elliptic 공개셋도 20만 노드 수준" | 203,769 노드 | 일치 (P-061) | 유지. Elliptic2(49M 클러스터)·TransXion 추가 가능 |
| 27 | `_research/wave1/analytics-technology.md` F-028·§5 Tornado Cash 철회 기록 | 철회 | 2025-11-18 v3 철회 사유 "mistakes in the references" 확인 | 사유 문구 추가 (P-019) |
