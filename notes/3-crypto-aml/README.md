# 3️⃣ Crypto AML — 가상자산 특화 의무·패턴

> 전통 AML이 **가상자산 특수성**과 만나는 층. VASP가 실제로 떠안는 의무·Travel Rule·자금세탁 패턴을 정리합니다. 마지막 업데이트: 2026-10-21.

## 누가 먼저 읽어야 하나

- 🏢 가상자산 거래소·수탁·지갑 서비스에서 AML 업무를 맡은 실무자
- 🔗 Travel Rule·KYT 연동 엔지니어 (IVMS 101.2023 메시지가 뭔지 코드 레벨에서 필요)
- 🕵️ 조사·수사·법률 자문에서 **가상자산 특유 패턴**(mixer·peel chain·cross-chain)을 이해해야 하는 사람

## 읽는 순서

```mermaid
flowchart LR
    A[vasp-obligations.md<br/>9대 의무] --> B[travel-rule.md<br/>INR.15 §7b 운영]
    B --> C[onchain-typology.md<br/>자금세탁 7유형]
    C --> D[defi-nft-risks.md<br/>회색지대]
    D --> Next[▶ 4-technology/로]

    style A fill:#fef3c7
    style B fill:#fce7f3
    style C fill:#dbeafe
    style D fill:#ede9fe
    style Next fill:#d1fae5
```

## 파일 인덱스

| # | 파일 | 핵심 질문 | 배우고 나면 |
|---|---|---|---|
| 1 | [`vasp-obligations.md`](vasp-obligations.md) | VASP가 해야 할 일 9가지가 뭔가? | "AML 프로그램 있다"는 주장을 체크리스트로 검증 |
| 2 | [`travel-rule.md`](travel-rule.md) | 송수신인 정보를 왜·어떻게 동반해야 하나? | A·B·C 금액 유형, 한국 100만원(~2027-02-18)→전건(2027-02-19~) 전환, Sunrise 대응 설명 가능 |
| 3 | [`onchain-typology.md`](onchain-typology.md) | 실제로 어떻게 세탁하는가? | KYT가 탐지하려는 7~9패턴의 원리·탐지 난이도 설명 |
| 4 | [`defi-nft-risks.md`](defi-nft-risks.md) | 사업자 없는 영역은 누가 책임지나? | DeFi·NFT·Privacy coin 규제가 왜 지연되는지 이해 |

## 핵심 출구

- VASP 9대 의무를 7개 이상 외운다
- Travel Rule 금액 구조 차이 설명 — 한국 100만원 이상(A형, ~2027-02-18; 2027-02-19~ 전건, enacted-not-in-force) · EU TFR(정보는 전건, EUR 1,000 은 자기수탁 검증) · 영국(1,000 euros 2023-09-01~2026-06-29 → £800 2026-06-30~, 정보 심화 기준) · 미국 31 CFR 1010.410(f) USD 3,000 이상($250 하향안은 2025-04-16 철회)
- Peel chain·Smurfing·Chain hopping·Mixer·Privacy coin·NFT wash trading·Flash loan abuse 각각 **1문장 정의**
- Tornado Cash·북한 Lazarus와 이 문서의 유형이 어떻게 대응되는지

## 트래블룰 한눈에 — 2027-02-19 한국 전환

```mermaid
flowchart LR
    N["2026-10-21 기준<br/>시행령 §10-10 ①호<br/>100만원 이상만 정보제공"] -->|대통령령 제36592호<br/>2026-08-18 공포| T["2027-02-19 시행 예정<br/>enacted-not-in-force"]
    T --> F["정보제공: 모든 이전"]
    T --> Q["추가정보: 요청 시 3영업일"]
    T --> W["자기수탁 지갑: 동일인만 허용"]
    T --> M["1천만원 이상: 자체 의심거래 감시체계"]
```

근거: [법제처 시행예정 판본](https://www.law.go.kr/DRF/lawService.do?OC=test&target=eflaw&MST=288765&efYd=20270219&type=XML), [감독규정 FIU 고시 제2026-2호](https://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=2100000285986&type=XML). 상세는 [`travel-rule.md`](travel-rule.md) §7.

## 다음 단계

- 기술 스택 → [`../4-technology/README.md`](../4-technology/README.md)
- 운영 절차 → [`../5-compliance/README.md`](../5-compliance/README.md)
- 실제 사건 → [`../6-cases/README.md`](../6-cases/README.md)
- 상위 인덱스 → [`../README.md`](../README.md)
