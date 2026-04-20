# Day 39 — DeFi 자금세탁 (DEX / LP / Flash Loan)

> 무중개 금융이 layering 인프라가 되는 방식. ⏱️ ~80분.

## 📖 오늘 뭘 배우나

DeFi는 원래 AML 목적을 위해 설계된 게 아니지만, **운영자 없음 + KYC 없음 + 전역 접근**이라는 속성 때문에 자연스럽게 layering 인프라가 됐습니다. DEX swap·LP 입출금·Flash loan의 layering 메커니즘, 그리고 **frontend 운영자**에게 규제가 집중되는 이유(Uniswap Labs 사례)까지.

## 🎯 핵심 질문
1. DEX swap이 layering에 효과적인 이유?
2. Liquidity Pool 입출금이 출처 단절시키는 메커니즘?
3. Flash loan attack + 자금세탁 결합 방식?

## 📖 읽기 (~55분)
- 메인: [`../notes/3-crypto-aml/defi-nft-risks.md`](../notes/3-crypto-aml/defi-nft-risks.md) — 1절 (DeFi)
- 보조: [`../notes/3-crypto-aml/onchain-typology.md`](../notes/3-crypto-aml/onchain-typology.md) — 1절 E, F

## 🌐 외부 자료 (~15분)
- [Transnet — DeFi Compliance 2026 Guide](https://transnetinc.com/navigating-compliance-challenges-in-defi-a-2026-guide)

## 🛠️ 미니 챌린지 (~10분)
- DEX → Lending → LP token → 다른 자산 인출 흐름 한 그림
- "DeFi가 fully decentralized면 AML은 누가 책임?" 자기 답변 3줄

## ✅ 체크포인트
- [ ] DEX swap 노출 차단 정책 이해
- [ ] LP 입금 layering 효과 안다
- [ ] Flash loan 기본 메커니즘 안다
- [ ] DeFi의 frontend 운영자 책임 가능성 안다 (Uniswap Labs)

## 💭 오늘의 한 줄
