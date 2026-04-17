# Day 30 — UTXO + Common Input Ownership Heuristic

> 비트코인 분석의 가장 중요한 휴리스틱. ⏱️ ~80분.

## 🎯 핵심 질문
1. UTXO 모델이 뭔가? (vs Account 모델)
2. Common Input Ownership 휴리스틱의 논리?
3. CoinJoin이 이 휴리스틱을 무력화하는 방식?

## 📖 읽기 (~50분)
- 메인: [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) — 1~2절

## 🌐 외부 자료 (~20분)
- [Heuristic-Based Address Clustering in Bitcoin (논문)](https://www.researchgate.net/publication/347083664_Heuristic-Based_Address_Clustering_in_Bitcoin)
- [Elementus — Data Science Heuristics](https://www.elementus.io/blog-post/decoding-the-chain-how-data-science-based-heuristics-reveal-blockchain-networks)

## 🛠️ 미니 챌린지 (~10분)
- 트랜잭션 1개에 input 3개 (A, B, C) → output 2개 (D, E) 예시 그리기
- Common Input Ownership 적용 → 어느 주소들이 같은 클러스터?
- CoinJoin 시나리오를 추가하면 어떻게 깨지는지 메모

## ✅ 체크포인트
- [ ] UTXO 모델 이해
- [ ] Common Input Ownership 직접 설명 가능
- [ ] CoinJoin이 무력화하는 이유 안다
- [ ] 비트코인이 ETH보다 클러스터링이 강한 이유 안다

## 💭 오늘의 한 줄
