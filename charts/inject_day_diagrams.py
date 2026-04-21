#!/usr/bin/env python3
"""
Inject a Mermaid "🗺 오늘의 지도" block into each curriculum/day_NN.md,
right before the '## 🎯 핵심 질문' / '회고 질문' section.

Usage:
    python charts/inject_day_diagrams.py            # inject all 60
    python charts/inject_day_diagrams.py --remove   # undo: remove blocks
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CUR = ROOT / "curriculum"

MARKER_START = "<!-- MAP-START -->"
MARKER_END = "<!-- MAP-END -->"

DIAGRAMS: dict[int, str] = {}

# ================================================================
# Week 1 — 기초
# ================================================================
DIAGRAMS[1] = """\
```mermaid
flowchart LR
    A["💰 범죄수익"] --> P["Placement<br/>배치"]
    P --> L["Layering<br/>은닉"]
    L --> I["Integration<br/>통합"]
    I --> C["✅ 합법 자산"]
    style A fill:#f7f5ef,stroke:#c9a646
    style C fill:#d1fae5,stroke:#10b981
    style P fill:#e5eaf2,stroke:#1a2e4a
    style L fill:#e5eaf2,stroke:#1a2e4a
    style I fill:#e5eaf2,stroke:#1a2e4a
```"""

DIAGRAMS[2] = """\
```mermaid
flowchart LR
    T["🏦 전통 금융"] -->|비공개·T+1·국경 有·동결 가능| V1["AML 표준"]
    C["⛓️ 가상자산"] -->|공개·24/7·국경 X·가명| V2["KYT + KYC 결합"]
    V2 --> P["🎯 실시간 Pre-tx<br/>차단 필수"]
    style T fill:#e5eaf2,stroke:#1a2e4a
    style C fill:#fff7d6,stroke:#c9a646
    style P fill:#fed7aa,stroke:#ea580c
```"""

DIAGRAMS[3] = """\
```mermaid
flowchart TB
    KYC["🌂 KYC"] --> CDD["📋 CDD (모든 고객)"]
    CDD --> EDD["🔒 EDD<br/>PEP · 고위험국 · 비대면+위험"]
    CDD --> SDD["🟢 SDD<br/>정부·상장사 (한국 X)"]
    style KYC fill:#fff,stroke:#1a2e4a,stroke-width:2px
    style CDD fill:#f7f5ef,stroke:#c9a646
    style EDD fill:#fed7aa,stroke:#ea580c
    style SDD fill:#d1fae5,stroke:#10b981
```"""

DIAGRAMS[4] = """\
```mermaid
flowchart LR
    subgraph KYC["👤 KYC — 사람"]
        KID["신분증·실명·PEP"]
    end
    subgraph KYT["⛓️ KYT — 거래·지갑"]
        KEX["exposure·cluster·SDN"]
    end
    KYC & KYT --> RE["🎯 Risk Score"]
    RE -->|threshold 초과| STR["📝 STR (금액 무관)"]
    STR -.Tipping-off 금지.-> FIU["🏛 KoFIU"]
    style KYC fill:#e5eaf2,stroke:#1a2e4a
    style KYT fill:#fff7d6,stroke:#c9a646
    style STR fill:#fed7aa,stroke:#ea580c
```"""

DIAGRAMS[5] = """\
```mermaid
flowchart TB
    F["🌍 FATF 권고"] --> K["🇰🇷 특금법"]
    F --> U["🇺🇸 BSA"]
    F --> E["🇪🇺 AMLR + MiCA"]
    F -.평가.-> M["⚠️ Grey/Black List"]
    K --> KFIU["FIU · FSC"]
    U --> UFIN["FinCEN · OFAC"]
    E --> EAMLA["AMLA · NCA"]
    style F fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style M fill:#fff7d6,stroke:#c9a646
```"""

DIAGRAMS[6] = """\
```mermaid
flowchart TB
    V["🏢 VASP"] --> R["1. 신고/라이선스"]
    V --> K["2~3. KYC/CDD · EDD"]
    V --> T["4~5. KYT · 제재"]
    V --> S["6~7. STR/CTR · Travel Rule"]
    V --> G["8~9. 기록·내부통제"]
    style V fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style R fill:#e5eaf2,stroke:#1a2e4a
    style K fill:#e5eaf2,stroke:#1a2e4a
    style T fill:#e5eaf2,stroke:#1a2e4a
    style S fill:#e5eaf2,stroke:#1a2e4a
    style G fill:#e5eaf2,stroke:#1a2e4a
```"""

DIAGRAMS[7] = """\
```mermaid
mindmap
  root((Week 1<br/>가상자산 AML))
    AML 기초
      3단계 Placement·Layering·Integration
      AML vs CFT
    가상자산 특수성
      투명성의 역설
      Layering 도구 6종
    핵심 용어
      KYC CDD EDD SDD
      KYT STR CTR PEP BO
    거버넌스
      FATF 권고
      한국·미국·EU
    VASP 의무
      9 의무 + Travel Rule
```"""

# ================================================================
# Week 2 — 한국 규제
# ================================================================
DIAGRAMS[8] = """\
```mermaid
flowchart LR
    A["🏢 신규 VASP"] --> B["ISMS 인증"]
    A --> C["실명확인 계좌<br/>(거래소)"]
    A --> D["AML 내부통제"]
    A --> E["AMLO 임명 (임원)"]
    A --> F["대주주 자격심사<br/>(2026-01)"]
    B & C & D & E & F --> G["📋 FIU 신고 → 수리"]
    G -.3년.-> H["갱신"]
    style A fill:#fff7d6,stroke:#c9a646
    style G fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[9] = """\
```mermaid
flowchart LR
    S["특금법"] --> K["§5의2 KYC"]
    S --> STR["§4 STR (금액無)"]
    S --> CTR["§4의2 CTR 1천만원"]
    S --> TR["§5의2+시행령<br/>Travel Rule 100만원"]
    S --> R["§5의4 기록 5년"]
    S --> T["§9 Tipping-off 금지"]
    S --> P["§17 처벌"]
    style S fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style T fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[10] = """\
```mermaid
flowchart TB
    U["👤 이용자"] -->|원화 예치금| B["🏦 제휴 은행 분리보관<br/>+ 이용료 지급"]
    U -->|가상자산 예치| C["📦 자기자산과 분리 보관"]
    C --> CW["❄️ 콜드월렛 80%+"]
    C --> HW["🔥 핫월렛 20% (보험·준비금)"]
    B -.파산 시.-> UV["✅ 우선변제권"]
    style U fill:#fff7d6,stroke:#c9a646
    style B fill:#e5eaf2,stroke:#1a2e4a
    style C fill:#e5eaf2,stroke:#1a2e4a
```"""

DIAGRAMS[11] = """\
```mermaid
flowchart LR
    M["⚠️ 불공정거래 4종"] --> MM["시세조종"]
    M --> IT["내부자 거래"]
    M --> F["부정거래"]
    M --> SL["자기발행 상장 제한"]
    MM & IT & F --> P["💣 1년+ 징역<br/>부당이득 3~5배"]
    style M fill:#fed7aa,stroke:#ea580c
    style P fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[12] = """\
```mermaid
flowchart LR
    V["🏢 VASP"] -->|STR 전자보고| K["🏛 KoFIU"]
    K --> P["🚓 경찰·검찰"]
    K --> N["🏢 국세청·관세청"]
    K --> I["🕶 국정원"]
    K --> F["📊 금감원"]
    style V fill:#e5eaf2,stroke:#1a2e4a
    style K fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[13] = """\
```mermaid
flowchart TB
    L["📜 특금법"] --> E["시행령"]
    E --> S["감독규정 (FIU 고시)"]
    E --> B["업무규정"]
    S & B --> G["📖 신고매뉴얼 · RBA 가이드"]
    G --> O["🛠 실무 운영"]
    style L fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style G fill:#fff7d6,stroke:#c9a646
    style O fill:#d1fae5,stroke:#10b981
```"""

DIAGRAMS[14] = """\
```mermaid
flowchart LR
    K["🇰🇷 한국 AML 양대 법"] --> S["특금법<br/>(AML)"]
    K --> U["이용자보호법<br/>(자산보호·시장)"]
    S --> S1["KYC · STR · Travel Rule"]
    S --> S2["AML 기록 5년"]
    U --> U1["자산 분리보관"]
    U --> U2["시세조종 금지"]
    U --> U3["거래정보 15년"]
    style K fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

# ================================================================
# Week 3 — FATF + 글로벌
# ================================================================
DIAGRAMS[15] = """\
```mermaid
flowchart TB
    F["🌍 FATF (1989)<br/>39+2 회원국"] --> R["40 권고"]
    R --> R15["R.15 — VASP AML/CFT"]
    R --> R16["R.16 — Travel Rule"]
    R --> RO["R.1 RBA · R.10 CDD · R.20 STR"]
    F -->|평가| ME["상호평가<br/>C/LC/PC/NC"]
    ME -->|미흡| BL["⚠️ Grey · Black List"]
    style F fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style BL fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[16] = """\
```mermaid
flowchart LR
    R15["🌍 FATF R.15<br/>(2018 개정)"] --> KR["🇰🇷 특금법 §2"]
    R15 --> US["🇺🇸 MSB"]
    R15 --> EU["🇪🇺 MiCA CASP"]
    R15 -.정의.-> D["매수도 · 교환 · 이전<br/>보관 · 금융서비스"]
    style R15 fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[17] = """\
```mermaid
timeline
    title R.16 Travel Rule 진화
    2019 : 가상자산 확장
    2022~2025 : 현재 글로벌 운영<br/>USD/EUR 1,000 권고
    2025-06-18 : 개정 발표<br/>VASP tailored framework
    2026 후반 : 가이던스 발표 예정
    2030 말 : 발효
```"""

DIAGRAMS[18] = """\
```mermaid
flowchart LR
    BSA["🇺🇸 BSA (1970)"] -->|2001 강화| P["PATRIOT Act"]
    BSA --> M["MSB 등록<br/>(가상자산 2013~)"]
    M --> R["AML 프로그램<br/>SAR · CTR $10K"]
    M --> TR["Travel Rule $3,000"]
    style BSA fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[19] = """\
```mermaid
flowchart TB
    O["🇺🇸 OFAC"] --> S["SDN List"]
    S --> SC["🪙 가상자산 지갑주소 등재"]
    O --> SEC["2차 제재<br/>외국인도 미국 시장 차단"]
    SEC -.한국 VASP.-> K["USD·스테이블코인·클라우드 의존"]
    O --> G["GENIUS Act (2025-07)<br/>스테이블코인 BSA"]
    style O fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style SEC fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[20] = """\
```mermaid
flowchart TB
    EU["🇪🇺 EU 가상자산<br/>3종 세트"] --> M["MiCA (2024-12-30)<br/>시장·라이선스"]
    EU --> T["TFR (2024-12-30)<br/>Travel Rule 임계 0"]
    EU --> A["AMLR+AMLD6 (2027-07-10)<br/>27개국 단일 규칙"]
    M --> MG["grandfathering<br/>2026-07-01 종료"]
    A --> AMLA["AMLA 감독기구<br/>(프랑크푸르트)"]
    style EU fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[21] = """\
```mermaid
flowchart LR
    KR["🇰🇷 100만원"] & US["🇺🇸 $3,000"] & EU["🇪🇺 임계 無"] --> TR["Travel Rule 대상"]
    KR -.특이.-> UW["외부지갑 등록제"]
    US -.특이.-> UM["unhosted 룰 부재"]
    EU -.특이.-> UE["unhosted 1,000€+ 신원검증"]
    style KR fill:#e5eaf2,stroke:#1a2e4a
    style US fill:#fff7d6,stroke:#c9a646
    style EU fill:#fed7aa,stroke:#ea580c
```"""

# ================================================================
# Week 4 — Travel Rule + IVMS101
# ================================================================
DIAGRAMS[22] = """\
```mermaid
sequenceDiagram
    participant A as 👤 고객
    participant U as 🏦 VASP A
    participant K as 🔍 KYT
    participant V as 🌐 Travel Rule
    participant B as 🏦 VASP B
    A->>U: 출금 요청 (≥100만원)
    U->>K: 주소 위험도 체크
    K-->>U: OK
    U->>V: IVMS101 메시지
    V->>B: 라우팅
    B-->>V: Accept
    U->>A: 온체인 송금 실행
```"""

DIAGRAMS[23] = """\
```mermaid
flowchart TB
    I["📝 IVMS101 Message"] --> O["Originator"]
    I --> B["Beneficiary"]
    I --> OV["OriginatingVASP"]
    I --> BV["BeneficiaryVASP"]
    O --> NP["NaturalPerson / LegalPerson"]
    NP --> N["name.nameIdentifier"]
    NP --> G["geographicAddress"]
    NP --> NID["nationalIdentification"]
    NP --> DOB["dateAndPlaceOfBirth"]
    style I fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[24] = """\
```mermaid
flowchart LR
    S["📨 IVMS101 Payload"] --> T["TRISA<br/>gRPC + PKI"]
    S --> P["TRP<br/>REST API"]
    S --> O["OpenVASP<br/>Ethereum 기반"]
    T -.분산형.-> D["누구나 참여<br/>(VASP Discovery 별도)"]
    P -.분산형.-> D
    style S fill:#e5eaf2,stroke:#1a2e4a
```"""

DIAGRAMS[25] = """\
```mermaid
flowchart LR
    VV["🔐 VerifyVASP<br/>(람다256 + Chainalysis)"] <--> UP["🏦 Upbit"]
    CD["🔐 CODE<br/>(3사 합작법인)"] <--> B["🏦 빗썸"]
    CD <--> KB["🏦 코빗"]
    CD <--> CO["🏦 코인원"]
    VV <-.연동.-> CD
    style VV fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style CD fill:#c9a646,color:#fff,stroke:#c9a646
```"""

DIAGRAMS[26] = """\
```mermaid
flowchart LR
    V1["🏦 VASP A<br/>(TRISA)"] --> N["🌐 Notabene<br/>Gateway"]
    V2["🏦 VASP B<br/>(VerifyVASP)"] --> N
    V3["🏦 VASP C<br/>(CODE)"] --> N
    V4["🏦 VASP D<br/>(TRP)"] --> N
    N -.1,500+ VASP.-> S["✅ 단일 연결로<br/>Sunrise 해결"]
    style N fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style S fill:#d1fae5,stroke:#10b981
```"""

DIAGRAMS[27] = """\
```mermaid
flowchart TB
    Q["❓ 지갑주소 0xABC...<br/>어느 VASP?"] --> A["Attribution DB<br/>Chainalysis · TRM"]
    Q --> D["VASP Directory<br/>Notabene · TRISA"]
    Q --> T["DTI (ISO 24165)"]
    Q --> L["GLEIF LEI"]
    Q --> R["직접 등록<br/>(화이트리스트)"]
    style Q fill:#fff7d6,stroke:#c9a646
```"""

DIAGRAMS[28] = """\
```mermaid
flowchart LR
    I["📥 Input<br/>송수신 정보"] --> B["🔨 Builder"]
    B --> M["📝 IVMS101 JSON"]
    M --> V["🔍 Validator"]
    V --> O["✅ 성공"]
    V --> E["⚠️ 필드 누락<br/>포맷 오류"]
    style B fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style O fill:#d1fae5,stroke:#10b981
    style E fill:#fee2e2,stroke:#dc2626
```"""

# ================================================================
# Week 5 — 온체인 분석 + KYT
# ================================================================
DIAGRAMS[29] = """\
```mermaid
flowchart LR
    subgraph KYC["👤 KYC"]
        K1["신분증·PEP<br/>onboarding"]
    end
    subgraph KYT["⛓️ KYT"]
        T1["주소·클러스터<br/>실시간"]
    end
    KYC & KYT --> RE["Risk Engine"]
    RE --> A["Allow · Review · Block"]
    style KYC fill:#e5eaf2,stroke:#1a2e4a
    style KYT fill:#fff7d6,stroke:#c9a646
```"""

DIAGRAMS[30] = """\
```mermaid
flowchart LR
    I1["Input A"] --> TX["📦 TX"]
    I2["Input B"] --> TX
    I3["Input C"] --> TX
    TX --> O1["Output D"]
    TX --> O2["Output E (change)"]
    TX -.CIOH.-> CL["A·B·C = 같은 클러스터"]
    style CL fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[31] = """\
```mermaid
flowchart LR
    U1["👤 사용자 1"] --> D1["deposit 주소"]
    U2["👤 사용자 2"] --> D2["deposit 주소"]
    U3["👤 사용자 N"] --> DN["deposit 주소"]
    D1 & D2 & DN --> C["🏦 consolidation"]
    C --> H["🔥 hot wallet"]
    C --> CW["❄️ cold wallet"]
    C -.Deposit Heuristic.-> EX["✅ 거래소 클러스터"]
    style EX fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[32] = """\
```mermaid
flowchart LR
    CL["📦 Cluster"] --> A["🏷 Attribution"]
    A --> E["Exchange"]
    A --> M["Mixer"]
    A --> S["Sanctions (OFAC SDN)"]
    A --> D["Darknet"]
    A --> R["Ransomware"]
    A -.벤더.-> V["Chainalysis · TRM<br/>Elliptic · Crystal"]
    style A fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[33] = """\
```mermaid
flowchart LR
    W["🪪 주소"] --> D["Direct (1-hop)"]
    W --> I["Indirect (N-hop)"]
    D --> W1["× 금액 가중"]
    I --> W2["× 시간 거리"]
    W1 & W2 --> C["× 카테고리<br/>(SDN > Mixer > HR Exchange)"]
    C --> S["🎯 Risk Score 0~100"]
    S --> A["Threshold<br/>차단 · 검토 · 통과"]
    style S fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[34] = """\
```mermaid
sequenceDiagram
    participant A as ⛓️ Chain A (ETH)
    participant B as 🌉 Bridge
    participant C as ⛓️ Chain B (Tron)
    A->>B: deposit (lock)
    B->>C: mint wrapped
    Note over A,C: 추적 단절 위험
    A-->>C: time·amount 매칭<br/>(Chainalysis Crosschain · TRM Multichain)
```"""

DIAGRAMS[35] = """\
```mermaid
flowchart LR
    T["🎯 주소 X"] --> H1["1-hop<br/>카운터파티"]
    H1 --> H2["2-hop<br/>(fan-out 최대 10,000)"]
    H2 --> L["🏷 라벨 매칭"]
    L --> G["📊 Mermaid 그래프"]
    style T fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

# ================================================================
# Week 6 — 자금세탁 유형
# ================================================================
DIAGRAMS[36] = """\
```mermaid
flowchart LR
    L["🔀 Layering"] --> M["Mixer"]
    L --> CH["Chain Hopping"]
    L --> BR["Bridge"]
    L --> PC["Peel Chain"]
    L --> DX["DEX Swap"]
    L --> DF["DeFi L/LP"]
    L --> PR["Privacy Coin"]
    L --> NFT["NFT Wash"]
    L --> OTC["OTC 환전"]
    style L fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[37] = """\
```mermaid
flowchart LR
    subgraph Mixer["🔀 Mixer"]
        TC["Tornado Cash<br/>(zk-SNARK)"]
        W["Wasabi CoinJoin"]
        S["Samourai (폐쇄)"]
    end
    subgraph Privacy["🔒 Privacy Coin"]
        XMR["Monero<br/>Ring Sig + Stealth + RingCT"]
        ZEC["Zcash<br/>zk-SNARK shielded"]
    end
    Mixer --> HR["거래소 차단 카테고리"]
    Privacy --> D["한국·일본 상장폐지"]
    style HR fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[38] = """\
```mermaid
flowchart LR
    B["💰 큰 금액"] -->|peel| A1["소액"] -->|peel| A2["소액"] -->|peel| A3["소액 ···"]
    B --> R["나머지"]
    R -->|peel| R2["소액"]
    R2 --> R3["···"]
    style B fill:#fff7d6,stroke:#c9a646
```"""

DIAGRAMS[39] = """\
```mermaid
flowchart LR
    F["💰 자금"] --> S["DEX Swap<br/>ETH→USDT→DAI"]
    F --> LP["LP 입금<br/>→ 다른 자산 인출"]
    F --> FL["Flash Loan<br/>+ 가격 조작"]
    S & LP & FL --> C["👤 frontend 운영자<br/>책임 검토"]
    style C fill:#fed7aa,stroke:#ea580c
```"""

DIAGRAMS[40] = """\
```mermaid
flowchart LR
    W["👥 자금세탁자들"] --> S["Self-trading<br/>A ↔ B (same owner)"]
    W --> L["Loop trading<br/>A → B → C → A"]
    W --> P["Pump<br/>고가 만들어 외부 매도"]
    S & L & P --> G["📈 가짜 가격/거래량"]
    style G fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[41] = """\
```mermaid
flowchart TB
    C["💼 CMLN<br/>(중국어 자금세탁 네트워크)"] -.Laundering-as-a-Service.-> F["💰 Lazarus · 범죄조직"]
    C --> T["📱 텔레그램·위챗 OTC"]
    C --> U["USDT(Tron) 기반<br/>5~15% 수수료"]
    C -.2025.-> N["$16.1B · 1,800+ wallet"]
    style C fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style N fill:#fed7aa,stroke:#ea580c
```"""

DIAGRAMS[42] = """\
```mermaid
flowchart LR
    O["OFAC SDN.xml"] --> P["🔨 Parser"]
    E["Etherscan Labels"] --> P
    G["GitHub OSINT"] --> P
    P --> N["🏷 Normalize"]
    N --> J["📄 JSON · CSV"]
    N --> D["🔄 일별 diff"]
    style P fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

# ================================================================
# Week 7 — 컴플라이언스 운영
# ================================================================
DIAGRAMS[43] = """\
```mermaid
flowchart LR
    C["CDD"] --> S1["1. 신원확인"]
    C --> S2["2. 실소유자 (25%)"]
    C --> S3["3. 거래목적·자금원천"]
    C --> S4["4. 지속 모니터링"]
    S4 -.주기.-> R["저5·중3·고1년 재실사"]
    style C fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[44] = """\
```mermaid
flowchart TB
    T["⚠️ EDD 트리거"] --> P["PEP"]
    T --> H["고위험국"]
    T --> NF["비대면+위험"]
    T --> LG["거액거래"]
    T --> CX["복잡한 구조"]
    T --> CI["현금집약업"]
    T --> Action
    Action["🔒 EDD 절차"] --> SoF["자금출처(SoF) 증빙"]
    Action --> SoW["자산출처(SoW)"]
    Action --> App["임원 승인"]
    style T fill:#fed7aa,stroke:#ea580c
    style Action fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[45] = """\
```mermaid
flowchart LR
    A["🚨 1선 알람"] --> B["🔍 2선 분석"]
    B --> C["📝 STR 작성<br/>(사실·사유·증빙·유관)"]
    C --> D["✍️ AMLO 결재"]
    D --> K["🏛 KoFIU"]
    C -.Tipping-off 금지.-> X["고객 누설 ❌"]
    K --> E["경찰·검찰·국세청"]
    style K fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style X fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[46] = """\
```mermaid
flowchart TB
    S["🔍 Sanctions Screening"] --> O["OFAC SDN"]
    S --> U["UN Consolidated"]
    S --> E["EU CFSP"]
    S --> H["HM Treasury"]
    S --> K["🇰🇷 외교부"]
    S --> W["🪪 Wallet (Direct·Cluster·N-hop)"]
    W -.2차 제재.-> G["🇺🇸 글로벌 강제력"]
    style S fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style G fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[47] = """\
```mermaid
flowchart TB
    B["🏢 AML Program"] --> P1["1. 정책·절차"]
    B --> P2["2. AMLO 임명"]
    B --> P3["3. 교육"]
    B --> P4["4. 독립 감사"]
    B --> P5["5. CDD + BO"]
    B --> L["3LoD<br/>1선 영업 · 2선 컴플 · 3선 감사"]
    style B fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[48] = """\
```mermaid
flowchart TB
    CEO["👔 CEO"] -->|직접 보고| A["🎖 AMLO (임원급)"]
    A -->|STR 결정권| K["🏛 KoFIU"]
    A -->|감독 대응| F["FIU · 금감원"]
    A -->|전 거래 접근| D["Data"]
    A -.개인 형사책임.-> CZ["Binance CZ 4개월 징역 교훈"]
    style A fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style CZ fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[49] = """\
```mermaid
flowchart LR
    A["🔍 주소 입력"] --> S["OFAC SDN<br/>캐시 (일 1회 갱신)"]
    S --> M{"매칭?"}
    M -->|YES| B["⛔ 차단 + STR"]
    M -->|NO| P["✅ 통과"]
    M -->|모호| R["👀 수동 검토<br/>(FP disposition)"]
    style S fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style B fill:#fee2e2,stroke:#dc2626
```"""

# ================================================================
# Week 8 — 사례·리서치·AI
# ================================================================
DIAGRAMS[50] = """\
```mermaid
flowchart LR
    A["⚔️ 공급망 공격"] --> B["🏦 Bybit cold wallet"]
    B -->|$1.46B 탈취| L["🕵️ Lazarus"]
    L -->|48h playbook| P1["peel chain"]
    P1 --> P2["bridge (THORChain)"]
    P2 --> P3["DEX swap"]
    P3 --> P4["CMLN OTC 환전"]
    P4 --> K["💰 북한 자금화"]
    style L fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style K fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[51] = """\
```mermaid
timeline
    title Tornado Cash
    2022-08 : OFAC 제재
    2024-11 : 5th Cir. Van Loon 판결
    2025-03-21 : 지정 해제
    2025~ : Roman Storm 형사재판
```"""

DIAGRAMS[52] = """\
```mermaid
flowchart LR
    BM["BitMEX<br/>2020 $100M"] --> BT["Bittrex<br/>2022 $29M"]
    BT --> BN["Binance<br/>2023 $4.3B<br/>CZ 4개월 징역"]
    BN --> OK["OKX<br/>2025 $500M+"]
    OK --> PX["Paxful<br/>2025 $3.5M"]
    style BN fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[53] = """\
```mermaid
flowchart LR
    F["🇰🇷 FIU"] --> U["미신고 VASP<br/>단속 강화 (2025-12)"]
    F --> V["VASP 정기 검사"]
    L["🏛 법원"] --> E["시세조종 1호 사건"]
    L --> M["무신고 영업 기소<br/>(특금법 §17)"]
    style F fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[54] = """\
```mermaid
flowchart LR
    M["📄 Meiklejohn 2013<br/>A Fistful of Bitcoins"] --> W["Weber 2019<br/>Elliptic GCN"]
    W --> B["Bellei 2024<br/>Elliptic2 GNN"]
    B --> F["🔮 Future<br/>ZKP + AI"]
    style M fill:#e5eaf2,stroke:#1a2e4a
    style F fill:#fff7d6,stroke:#c9a646
```"""

DIAGRAMS[55] = """\
```mermaid
flowchart TB
    R["📊 Chainalysis 2026"] --> N1["$154B 불법거래"]
    R --> N2["84% 스테이블코인"]
    R --> N3["$2B DPRK"]
    R --> N4["$16.1B CMLN"]
    R --> N5["$17B Scams"]
    R --> N6["+162% YoY"]
    style R fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[56] = """\
```mermaid
flowchart LR
    D42["🔨 D42 Mixer fetcher"] --> W["🛠 KYT Wrapper"]
    D49["🔨 D49 OFAC screener"] --> W
    D35["🔨 D35 2-hop tracer"] --> W
    W --> API["kyt_check(address)"]
    API --> A["ALLOW · REVIEW · BLOCK"]
    style W fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

# ================================================================
# Capstone (57~60)
# ================================================================
DIAGRAMS[57] = """\
```mermaid
flowchart LR
    ML["🤖 AI·ML"] --> C["클러스터링 보조"]
    ML --> I["이상 탐지"]
    ML --> W["NFT wash trading"]
    ML --> N["새 mixer 식별"]
    ML --> S["Scam 사전 탐지"]
    ML -.한계.-> L["라벨 부족 · Adversarial · 설명가능성"]
    style ML fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style L fill:#fed7aa,stroke:#ea580c
```"""

DIAGRAMS[58] = """\
```mermaid
flowchart LR
    P["🔒 Privacy"] & C["⚖️ Compliance"] --> ZK["🔐 ZKP"]
    ZK --> Z1["zk-KYC"]
    ZK --> Z2["Selective Disclosure"]
    ZK --> Z3["Polygon ID · Worldcoin"]
    style ZK fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[59] = """\
```mermaid
flowchart TB
    D["📘 Design Doc"] --> P["문제 정의"]
    D --> R["규제 매핑 (특금법 §·이용자보호법 §)"]
    D --> A["아키텍처"]
    D --> RS["Risk Score 모델"]
    D --> RC["룰 카탈로그 10+"]
    D --> G["거버넌스 (5 Pillars · 3LoD)"]
    D --> L["단계적 도입 로드맵"]
    style D fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[60] = """\
```mermaid
flowchart LR
    C["🎓 60일 완주"] --> TA["Track A<br/>기술·KYT"]
    C --> TB["Track B<br/>법·규제"]
    C --> TC["Track C<br/>컴플 운영"]
    C --> TD["Track D<br/>솔루션·제품"]
    TA & TB & TC & TD --> M["🗓 M1·M2·M3 마일스톤"]
    M --> G["🎯 90일 후 도달"]
    style C fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style G fill:#d1fae5,stroke:#10b981
```"""


# ================================================================
# Injection logic
# ================================================================

SECTION_HEAD_RE = re.compile(r"^##\s+🎯\s+(?:핵심|회고)\s+질문", re.MULTILINE)

def inject(day: int):
    path = CUR / f"day_{day:02d}.md"
    if not path.exists():
        print(f"[SKIP] day_{day:02d}.md not found")
        return
    text = path.read_text(encoding="utf-8")

    # Remove existing block if any
    text = re.sub(
        rf"\n{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}\n",
        "\n",
        text,
        flags=re.DOTALL,
    )

    diagram = DIAGRAMS.get(day)
    if not diagram:
        print(f"[NO DIAGRAM] day_{day:02d}")
        return

    block = f"\n{MARKER_START}\n## 🗺 오늘의 지도\n\n{diagram}\n{MARKER_END}\n"

    m = SECTION_HEAD_RE.search(text)
    if not m:
        print(f"[NO HEAD] day_{day:02d}: no '## 🎯 ...질문' found")
        return

    new_text = text[: m.start()] + block + "\n" + text[m.start():]
    path.write_text(new_text, encoding="utf-8")
    print(f"[OK]  day_{day:02d}.md")


def remove_all():
    for d in range(1, 61):
        path = CUR / f"day_{d:02d}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = re.sub(
            rf"\n{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}\n",
            "\n",
            text,
            flags=re.DOTALL,
        )
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"[REMOVED] day_{d:02d}.md")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if "--remove" in sys.argv:
        remove_all()
        return

    for d in range(1, 61):
        inject(d)


if __name__ == "__main__":
    main()
