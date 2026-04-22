# Day 51 — 케이스: Tornado Cash + DeFi 제재의 한계

> 코드를 제재할 수 있는가? ⏱️ ~80분.

## 📖 오늘 뭘 배우나

Tornado Cash 사건은 "**코드 자체를 제재할 수 있는가**"라는 질문의 사법적 답을 처음 보여준 판례입니다. 2022 OFAC 제재 → 2024 5th Circuit Van Loon 판결 → 2025-03 해제라는 3년 흐름과, 동시에 진행 중인 **Roman Storm 개발자 형사재판**(별개)을 정리합니다. "코드는 제재 못 해도 개발자는 책임질 수 있다"는 결론이 DeFi 규제의 뉴노멀.


<!-- MAP-START -->
## 🗺 오늘의 지도

```mermaid
timeline
    title Tornado Cash
    2022-08 : OFAC 제재
    2024-11 : 5th Cir. Van Loon 판결
    2025-03-21 : 지정 해제
    2025~ : Roman Storm 형사재판
```
<!-- MAP-END -->

## 🎯 핵심 질문
1. Tornado Cash 제재 timeline (2022-08 → 2024-11 → 2025-03)?
2. 5th Circuit 판결의 핵심 논리?
3. Roman Storm 형사 재판이 별개인 이유?

## 📖 읽기 (~55분)
- 메인: [`../notes/6-cases/tornado-cash.md`](../notes/6-cases/tornado-cash.md)

## 🌐 외부 자료 (~20분)
- [Venable — Treasury Lifts Tornado Sanctions](https://www.venable.com/insights/publications/2025/04/a-legal-whirlwind-settles-treasury-lifts-sanctions)
- [Steptoe — DeFi AML implications](https://www.steptoe.com/en/news-publications/critical-tornado-cash-developments-have-significant-implications-for-defi-aml-and-sanctions-compliance.html)

## 🛠️ 미니 챌린지 (~5분)
- "Tornado 노출 wallet → 회사 정책" 의사결정 트리 메모 (2025-03 해제 후에도 차단 유지)
- 다른 mixer 운명 5개 (Blender/Sinbad/Wasabi/Samourai/JoinMarket) 정리

## ✅ 체크포인트
- [ ] Tornado Cash 전체 타임라인: 2022-08 OFAC 제재 → 2024-11 5th Cir. Van Loon 판결 → 2025-03-21 지정 해제
- [ ] 5th Circuit "코드는 property 아니다" 안다
- [ ] 개발자 형사책임 가능성 안다 (Storm 재판)
- [ ] 회사 정책: mixer = 위험 카테고리 유지 안다

## 💭 오늘의 한 줄

## 💼 실무 현장 (Industry Reality)

### 한국 VASP에서는

**Tornado Cash 지정 해제(2025-03) 이후에도 한국 4대 거래소는 전원 "mixer 노출 주소" 내부 블랙리스트 유지**. Chainalysis의 "Mixing" 카테고리 노출 >1%면 EDD 트리거, >5%면 freeze가 표준. 이유는 **특금법 §5의2(의심거래 보고)**는 OFAC 지정과 무관하게 "자금세탁 의심"을 독립 판단 대상으로 두기 때문. DAXA 가이드라인도 "mixer는 제재 유무와 무관하게 고위험 카테고리"로 명시.

### 글로벌에서는

**Coinbase·Kraken**은 2025-03 해제 직후 Tornado Cash 주소 **복원(unblock)**이 아니라 **카테고리를 "Sanctioned"에서 "High-Risk Mixer"로 재분류**. **Circle**은 USDC의 Tornado Cash 관련 blacklist를 **일부** 풀었지만 신규 유입은 계속 모니터링. **Roman Storm 재판(2025)**에서 유죄가 나오면 **"mixer 개발자 = 무등록 MSB"** 선례가 되어 프라이버시 도구 산업 전반에 충격.

### "코드 제재"의 법적 결론 (Van Loon 판결)

```
5th Circuit 핵심 논리:
1. Immutable smart contract = "property"가 아님
2. OFAC IEEPA(1977)은 "property" 지정 권한만 부여
3. 따라서 OFAC이 code 자체를 제재할 권한 없음

→ 그러나 개발자 개인(Roman Storm)의 
   무등록 MSB 운영·제재 회피 방조는 별개 형사 문제
```

### 회사 정책 의사결정 트리 (실무)

```
IF wallet has Tornado Cash direct exposure:
    IF exposure occurred BEFORE 2022-08-08 (지정 전):
        → LOW risk (증빙 보관)
    IF exposure occurred 2022-08 ~ 2025-03 (지정 기간):
        → BLOCK + STR (OFAC 위반 소급)
    IF exposure AFTER 2025-03-21 (해제 후):
        → HIGH risk (mixer 노출) + EDD
```

### 자주 나오는 오해

- **"제재 해제됐으니 지워도 된다"** — 한국·EU VASP 대다수는 **"mixer = 위험 카테고리"**로 별도 유지. 제재 해제 ≠ AML 위험 해제.
- **"코드는 법적 책임 없다"** — Van Loon은 **정부의 제재 권한**을 제한했을 뿐, **개발자의 형사 책임**은 별개(Storm 재판). "익명성 도구 제공 = 무등록 MSB"라는 해석이 살아있음.
