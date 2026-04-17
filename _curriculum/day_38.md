# Day 38 — Peel Chain + Smurfing

> 분할로 추적 회피. ⏱️ ~70분.

## 🎯 핵심 질문
1. Peel chain의 시각적 패턴?
2. Smurfing(structuring)과 peel chain의 차이?
3. 두 패턴의 탐지 휴리스틱은?

## 📖 읽기 (~45분)
- 메인: [`../02_crypto_aml/onchain_typology.md`](../02_crypto_aml/onchain_typology.md) — 1절 D (Peel chain)
- 보조: [`../00_overview/what_is_aml.md`](../00_overview/what_is_aml.md) — 2절 (Smurfing 언급)

## 🛠️ 미니 챌린지 (~20분)
- Peel chain 그림 그리기 (10단계)
- Smurfing 시나리오 그리기 (10명 → 1 wallet 합산)
- 두 패턴의 탐지 룰 의사코드 작성:
  ```
  IF (in_degree > 5 AND each_amount < threshold AND time_window < 24h)
    THEN flag as smurfing
  ```

## ✅ 체크포인트
- [ ] Peel chain 패턴 시각적으로 구별 가능
- [ ] Smurfing = 분할 입금 = KYC 회피 안다
- [ ] 그래프 분석 (in-degree/out-degree) 개념 안다
- [ ] 룰 기반 탐지의 한계 (adversarial) 인지

## 💭 오늘의 한 줄
