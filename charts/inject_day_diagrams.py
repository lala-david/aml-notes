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
    V2 --> P["🎯 사전 스크리닝<br/>+ 사람 검토"]
    style T fill:#e5eaf2,stroke:#1a2e4a
    style C fill:#fff7d6,stroke:#c9a646
    style P fill:#fed7aa,stroke:#ea580c
```"""

DIAGRAMS[3] = """\
```mermaid
flowchart TB
    KYC["🌂 KYC"] --> CDD["📋 CDD (모든 고객)"]
    CDD --> EDD["🔒 EDD<br/>PEP · 고위험국 · 비대면+위험"]
    CDD --> SDD["🟢 SDD<br/>정부·상장사 등 저위험<br/>VASP에선 드묾"]
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
    RE -->|알람 후 분석가가 의심 판단| STR["📝 STR (금액 무관)"]
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
    A --> E["AML 인력 4인 이상<br/>보고책임자 지정"]
    A --> F["대주주 심사<br/>(2026-08-20 시행)"]
    B & C & D & E & F --> G["📋 FIU 신고 → 수리"]
    G -.유효기간.-> H["갱신"]
    style A fill:#fff7d6,stroke:#c9a646
    style G fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[9] = """\
```mermaid
flowchart LR
    S["특금법"] --> K["§5의2 KYC"]
    S --> STR["§4 STR (금액無)"]
    S --> CTR["§4의2 CTR 1천만원"]
    S --> TR["§5의3 + 시행령 §10의10<br/>트래블룰 100만원 이상<br/>2027-02-19~ 전건"]
    S --> R["기록 보존 5년"]
    S --> T["누설 Tipping-off 금지"]
    S --> P["벌칙 · 과태료"]
    style S fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style T fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[10] = """\
```mermaid
flowchart TB
    U["👤 이용자"] -->|원화 예치금| B["🏦 은행에 분리보관"]
    U -->|가상자산 예치| C["📦 자기자산과 분리 보관"]
    C --> CW["❄️ 콜드월렛 보관<br/>비율은 하위규범 소관"]
    C --> HW["🔥 핫월렛<br/>보험 또는 준비금"]
    B -.사업자 사고 시.-> UV["✅ 고유재산과 분리"]
    style U fill:#fff7d6,stroke:#c9a646
    style B fill:#e5eaf2,stroke:#1a2e4a
    style C fill:#e5eaf2,stroke:#1a2e4a
```"""

DIAGRAMS[11] = """\
```mermaid
flowchart LR
    M["⚠️ 불공정거래 금지 §10"] --> IT["① 미공개중요정보 이용"]
    M --> MM["②③ 시세조종"]
    M --> F["④ 부정거래"]
    M --> SL["⑤ 자기·특수관계인 발행<br/>가상자산 거래"]
    IT & MM & F --> P["💣 1년 이상 유기징역 또는<br/>이익의 3~5배 벌금 §19"]
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
    F["🌍 FATF<br/>정부간 작업반 · soft law"] --> R["40 권고"]
    R --> R15["R.15 + INR.15 §7b<br/>VASP AML/CFT · 트래블룰 원천"]
    R --> R16["R.16 2025-06 개정<br/>VASP는 R.15 경유"]
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
    title 가상자산 트래블룰 국제 기준 - 2026-10-21 기준
    2019-06 : INR.15 §7b 신설 - 금액 기준 없음
    2021-10-28 : RBA 가이던스 - R.16을 amended way로 적용
    2025-06 : R.16 개정 - VASP는 R.15 경유 - de minimis USD/EUR 1,000 이하
    2026-06-24~08-21 : R.16 이행 가이던스 초안 의견수렴
    2026-10-21 : 최종본 미발간
    2030 말 : 개정 R.16 이행 기대시한
```"""

DIAGRAMS[18] = """\
```mermaid
flowchart LR
    BSA["🇺🇸 BSA<br/>31 U.S.C. 5311 et seq."] -->|배경: 2001 강화| P["PATRIOT Act"]
    BSA --> M["MSB 정의로 포섭<br/>other value that<br/>substitutes for currency"]
    M --> R["AML 프로그램 · SAR"]
    M --> TR["트래블룰<br/>$3,000 or more"]
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
    EU["🇪🇺 EU 가상자산<br/>3종 세트"] --> M["MiCA 발효 2023-06-29<br/>CASP 적용 2024-12-30"]
    EU --> T["TFR 2024-12-30 적용<br/>금액 기준 없이 전건"]
    EU --> A["AMLR 2027-07-10 적용 예정<br/>27개국 단일 규칙"]
    M --> MG["회원국별 경과기간<br/>최장 2026-07-01 종료"]
    A --> AMLA["AMLA 프랑크푸르트<br/>2026-01-01 EBA 권한 이관"]
    style EU fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[21] = """\
```mermaid
flowchart LR
    KR["🇰🇷 100만원 이상 ~2027-02-18<br/>전건 2027-02-19~"] & US["🇺🇸 USD 3,000 이상"] & EU["🇪🇺 금액 기준 없음 - 전건"] --> TR["Travel Rule 대상"]
    KR -.특이.-> UW["외부지갑: 거래소 자율<br/>2027-02-19~ 동일인만 허용"]
    US -.특이.-> UM["비수탁지갑 NPRM<br/>2026-10-06 withdrawn"]
    EU -.특이.-> UE["자기수탁 EUR 1,000 이상<br/>소유·통제 평가"]
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
    A->>U: 출금 요청 - 100만원 이상 ~2027-02-18 / 전건 2027-02-19~
    U->>K: 주소 위험도 체크
    K-->>U: OK
    U->>V: IVMS 101.2023 메시지
    V->>B: 라우팅
    B-->>V: Accept
    U->>A: 온체인 송금 실행
```"""

DIAGRAMS[23] = """\
```mermaid
flowchart TB
    I["📝 IVMS 101.2023 Message"] --> O["Originator"]
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
    S["📨 IVMS 101.2023 Payload"] --> T["TRISA<br/>gRPC/protobuf + GDS"]
    S --> P["TRP<br/>양자 간 암호화 교환"]
    O["OpenVASP Association<br/>Zug - TRP 관리 협회"] -.관리.-> P
    T -.오픈 표준.-> D["사양 공개·각자 구현<br/>상대 식별은 별도"]
    P -.오픈 표준.-> D
    style S fill:#e5eaf2,stroke:#1a2e4a
```"""

DIAGRAMS[25] = """\
```mermaid
flowchart LR
    VV["🔐 VerifyVASP<br/>운영 주체 홈페이지 미명시"] --> P1["TravelRule API<br/>VerifyName API · VerifyWallet"]
    CD["🔐 CODE<br/>CODE Inc."] --> P2["상호운용 표시 목록<br/>VerifyVASP · GTR · Sumsub<br/>Sygna · Notabene · CryptoSwift"]
    CD -.홈페이지에 상호운용 표시.-> VV
    style VV fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style CD fill:#c9a646,color:#fff,stroke:#c9a646
```"""

DIAGRAMS[26] = """\
```mermaid
flowchart LR
    V1["🏦 VASP A<br/>TRISA"] --> N["🌐 멀티프로토콜<br/>연동 솔루션"]
    V2["🏦 VASP B<br/>솔루션 네트워크"] --> N
    V3["🏦 VASP C<br/>TRP"] --> N
    N -.연동 표시 ≠ 커버리지 보장.-> S["미연결 상대방은 남는다<br/>→ Sunrise 정책 필요"]
    style N fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style S fill:#fef3c7,stroke:#d97706
```"""

DIAGRAMS[27] = """\
```mermaid
flowchart TB
    Q["❓ 지갑주소 0xABC...<br/>어느 VASP?"] --> A["블록체인 분석 라벨<br/>Attribution DB"]
    Q --> D["네트워크 디렉터리<br/>TRISA GDS · 솔루션 네트워크 회원"]
    Q --> L["LEI ISO 17442<br/>법인 식별"]
    Q --> C["고객에게 직접 확인<br/>EBA GL ¶77~78"]
    T["DTI ISO 24165<br/>토큰 식별 - VASP 식별자 아님"] -.보조.-> Q
    style Q fill:#fff7d6,stroke:#c9a646
```"""

DIAGRAMS[28] = """\
```mermaid
flowchart LR
    I["📥 Input<br/>송수신 정보 + 실행일"] --> B["🔨 Builder"]
    B --> M["📝 IVMS 101.2023 페이로드"]
    M --> V["🔍 Validator<br/>C1·C9 + 관할·시점 규칙"]
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
    subgraph KYT["⛓️ KYT - 거래모니터링"]
        T1["주소·클러스터<br/>노출도"]
    end
    KYC & KYT --> RE["Risk Engine"]
    RE --> A["사람 검토 → STR · EDD·거래거절 · 종결"]
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
    C -.Deposit Heuristic.-> EX["✅ 거래소 클러스터 후보"]
    style EX fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[32] = """\
```mermaid
flowchart LR
    CL["📦 Cluster"] --> A["🏷 Attribution"]
    A --> E["Exchange"]
    A --> M["Mixer"]
    A --> S["Sanctions - OFAC SDN 등"]
    A --> D["Darknet"]
    A --> R["Ransomware"]
    SRC["라벨 원천<br/>자체 거래 · 공개 주소 · 법집행<br/>제재목록 · OSINT"] -.-> A
    style A fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[33] = """\
```mermaid
flowchart LR
    W["🪪 주소"] --> D["Direct"]
    W --> I["Indirect - N-hop"]
    D --> W1["금액"]
    I --> W2["경과 시간"]
    W1 & W2 --> C["카테고리<br/>제재 · 믹서 · 다크넷 등"]
    C --> S["🎯 노출도 점수<br/>계수 비공개 - 블랙박스"]
    S --> A["사람 검토 → STR · EDD·거래거절 · 종결"]
    style S fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[34] = """\
```mermaid
sequenceDiagram
    participant A as ⛓️ Chain A
    participant B as 🌉 Bridge
    participant C as ⛓️ Chain B
    A->>B: deposit - lock 또는 burn
    B->>C: mint 또는 release
    Note over A,C: 추적 단절 위험
    A-->>C: 순번·수취인·시간·금액 매칭
```"""

DIAGRAMS[35] = """\
```mermaid
flowchart LR
    T["🎯 주소 X"] --> H1["1-hop<br/>카운터파티"]
    H1 --> H2["2-hop<br/>fan-out 상한은 직접 설정"]
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
        TC["Tornado Cash<br/>zk-SNARK 고정 액면 풀"]
        W["CoinJoin<br/>Wasabi · Samourai · JoinMarket"]
        RG["Railgun 등 차폐 풀"]
    end
    subgraph Privacy["🔒 Privacy Coin"]
        XMR["Monero<br/>Ring Sig + Stealth + RingCT"]
        ZEC["Zcash<br/>zk-SNARK shielded"]
    end
    Mixer --> HR["노출도·행태 기반 위험평가"]
    Privacy --> D["EU AMLR 제79조<br/>2027-07-10 취급 금지 예정"]
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
    F["💰 자금"] --> S["DEX Swap<br/>연쇄 교환"]
    F --> LP["LP 입금<br/>→ 다른 자산 인출"]
    F --> FL["Flash Loan<br/>+ 가격 조작"]
    S & LP & FL --> C["👤 통제자 판정<br/>FATF 2021 para 67·93"]
    style C fill:#fed7aa,stroke:#ea580c
```"""

DIAGRAMS[40] = """\
```mermaid
flowchart LR
    W["👥 자금세탁자들"] --> S["Self-trading<br/>A ↔ B same owner"]
    W --> L["Loop trading<br/>A → B → C → A"]
    W --> P["Pump<br/>고가 만들어 외부 매도"]
    S & L & P --> G["📈 가짜 가격/거래량"]
    style G fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[41] = """\
```mermaid
flowchart TB
    C["💼 전문 세탁 네트워크<br/>CMLN · OTC 환전망"] -.Laundering-as-a-Service.-> F["💰 DPRK · 사기조직"]
    C --> T["📱 메신저 기반 OTC"]
    C --> U["스테이블코인 경유<br/>2025 불법 거래량의 84%, B"]
    C -.FATF 7차 TU.-> N["캄보디아 복합체<br/>최소 USD 40억 · 2021-08~2025-01"]
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
    C --> S2["2. 실소유자 BO<br/>지분 + 실질 지배"]
    C --> S3["3. 거래목적·자금원천"]
    C --> S4["4. 지속 모니터링"]
    S4 -.근거.-> R["업무규정 제76~81조<br/>거래모니터링체계"]
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
    A["🚨 1선 알람<br/>KYT·CS·FDS·시장감시"] --> B["🔍 2선 분석"]
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
    CEO["👔 CEO · 이사회"] -->|보고 채널| A["🎖 AMLO 보고책임자"]
    A -->|STR 결재| K["🏛 KoFIU"]
    A -->|감독 대응| F["FIU · 금감원 검사수탁"]
    A -->|데이터 접근| D["거래·고객 Data"]
    A -.개인 제재 가능.-> P["임직원 제재·퇴직자 제재통보<br/>2026-08-18 시행령"]
    style A fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style P fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[49] = """\
```mermaid
flowchart LR
    A["🔍 주소 입력"] --> S["OFAC SDN<br/>캐시 · 정기 갱신 + diff"]
    S --> M{"매칭?"}
    M -->|YES| B["⛔ 거래 거절·동결<br/>+ STR 검토"]
    M -->|NO| P["✅ 목록상 통과<br/>위험평가는 별도"]
    M -->|모호| R["👀 수동 검토<br/>FP disposition"]
    style S fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style B fill:#fee2e2,stroke:#dc2626
```"""

# ================================================================
# Week 8 — 사례·리서치·AI
# ================================================================
DIAGRAMS[50] = """\
```mermaid
flowchart LR
    A["⚔️ 제3자 인프라 공격<br/>RPC 노드·멀티시그 공급자"] --> B["🏦 VASP · DeFi"]
    B -->|"Bybit USD 14.6억"| L["🕵️ DPRK"]
    L --> P1["분산<br/>BTC 35 · ETH 125,000 지갑"]
    P1 --> P2["브리지"]
    P1 --> P3["비수탁 지갑"]
    P1 --> P4["OTC 네트워크"]
    P2 --> K["세탁 노드<br/>동남아 금융 복합체 등"]
    P3 --> K
    P4 --> K
    K --> R["회수 3.8%"]
    style L fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style R fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[51] = """\
```mermaid
timeline
    title Tornado Cash와 믹서 규제
    2022 : OFAC 최초 지정 · 세부는 원 공고로 확인
    2025-03-21 : SDN 삭제 · 엔티티 1 · ETH 주소 90
    2025-08-06 : Storm 배심 평결 B
    2026-10-06 : FinCEN 믹싱 311조 NPRM 철회
    2027-07-10 : EU AMLR 익명성강화 수단 금지
```"""

DIAGRAMS[52] = """\
```mermaid
flowchart LR
    PH["Prince Group TCO 146개 대상<br/>Huione 311조 최종규칙<br/>2025-10-14"] --> XC["FINTRAC Xeltox<br/>C$176,960,190<br/>2025-10-22"]
    XC --> PX["FinCEN Paxful<br/>$3.5M<br/>2025-12-09"]
    PX --> BB["OFAC BitBank 등<br/>E.O. 13902<br/>2026-09-17"]
    BB --> A7["A7 네트워크 TCO B 2026-10-01<br/>9714조 특별조치 NPRM 2026-10-05"]
    style PH fill:#fee2e2,stroke:#dc2626
    style A7 fill:#fee2e2,stroke:#dc2626
```"""

DIAGRAMS[53] = """\
```mermaid
flowchart LR
    F["🇰🇷 FIU"] --> U["미신고 사업자 단속<br/>사이트 27건 접속차단 2026-10-13"]
    F --> V["VASP 검사<br/>두나무 과태료 352억원 2025-11-06"]
    G["금융위·금감원"] --> E["시장감시 집행<br/>첫 과징금 2025-09-03"]
    T["통신사기피해환급법"] --> M["거래소 임시조치 의무<br/>2026-10-01 시행"]
    style F fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[54] = """\
```mermaid
flowchart LR
    M["📄 Meiklejohn 2013<br/>A Fistful of Bitcoins · CIOH"] --> W["Weber 2019<br/>Elliptic 데이터셋 · RF > GCN"]
    W --> B["Bellei 2024<br/>Elliptic2 · 서브그래프 분류"]
    B --> F["🔮 2025~2026<br/>경로 추적 · 크로스체인 · 프라이버시 누수 측정"]
    style M fill:#e5eaf2,stroke:#1a2e4a
    style F fill:#fff7d6,stroke:#c9a646
```"""

DIAGRAMS[55] = """\
```mermaid
flowchart TB
    R["📊 Chainalysis 2026<br/>서론 2026-01-08"] --> N1["최소 $154B<br/>불법 주소 수취 · 하한"]
    R --> N2["스테이블코인 84% · B"]
    R --> N3["DPRK 탈취 $2B"]
    R --> N4["A7A5 1년 미만 $93.3B"]
    R --> N5["2024 수치 $40.9B → $57.2B<br/>상향 수정"]
    R --> N6["+162%로 서술<br/>산술값 약 +169%"]
    style R fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[56] = """\
```mermaid
flowchart LR
    D42["🔨 D42 Mixer fetcher"] --> W["🛠 KYT Wrapper"]
    D49["🔨 D49 OFAC screener"] --> W
    D35["🔨 D35 2-hop tracer"] --> W
    W --> API["kyt_check · address"]
    API --> A["PASS · REVIEW"]
    A --> H["👤 사람 검토<br/>FATF 2021 para 276"]
    H --> O["STR · EDD · 거래거절<br/>법적 산출물은 별도 축"]
    style W fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

# ================================================================
# Capstone (57~60)
# ================================================================
DIAGRAMS[57] = """\
```mermaid
flowchart LR
    ML["🤖 AI·ML"] --> C["클러스터링 보조"]
    ML --> A["온체인 이상 패턴<br/>anomaly 탐지"]
    ML --> P["피싱·rug pull·<br/>address poisoning"]
    ML --> N["새 mixer 식별"]
    A --> OUT{"어느 법적 출구?"}
    P --> OUT
    OUT --> F["FDS 임시조치<br/>통신사기피해환급법"]
    OUT --> M["시장감시 통보<br/>이용자보호법 §12"]
    OUT --> S["STR<br/>특금법 §4"]
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
    ZK --> Z3["SSI · 검증가능 자격증명<br/>설계 연구 단계"]
    style ZK fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```"""

DIAGRAMS[59] = """\
```mermaid
flowchart TB
    D["📘 Design Doc"] --> P["문제 정의"]
    D --> R["규제 매핑<br/>특금법 §4·§5의3 · 이용자보호법 §12 · 통신사기피해환급법"]
    D --> A["아키텍처"]
    D --> RS["Risk Score 모델<br/>산출물 3축 분리"]
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
