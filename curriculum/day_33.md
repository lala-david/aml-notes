# Day 33 — Exposure Score (Direct vs N-hop)

> 위험 노출도 계산법. ⏱️ ~70분.

## 🎯 핵심 질문
1. Direct vs Indirect (N-hop) exposure 차이?
2. 가중치 적용 3요소?
3. Exposure Score → 의사결정 흐름?

## 📖 읽기 (~50분)
- 메인: [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) — 4절
- 보조: [`../notes/4-technology/kyc-kyt.md`](../notes/4-technology/kyc-kyt.md) — 4절 (Exposure)

## 🛠️ 미니 챌린지 (~15분)
- 가상 주소 1개 시나리오:
  - Direct exposure to Tornado Cash: 50점
  - 2-hop to OFAC SDN: 30점
  - Direct to Binance (low): 0점
- 다른 시나리오 1개 자기 만들기 + 점수 계산

## ✅ 체크포인트
- [ ] Direct vs N-hop 차이 안다
- [ ] 가중치 3요소 (금액/시간거리/위험카테고리) 안다
- [ ] threshold 기반 자동 차단 메커니즘 이해
- [ ] False positive 처리 (disposition) 흐름 안다

## 💭 오늘의 한 줄
