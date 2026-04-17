# Day 40 — NFT Wash Trading

> 가격을 임의로 만드는 자금세탁. ⏱️ ~70분.

## 🎯 핵심 질문
1. NFT가 자금세탁에 매력적인 이유?
2. Wash trading 패턴 3가지?
3. FATF의 NFT 분류 기준?

## 📖 읽기 (~45분)
- 메인: [`../notes/3-crypto-aml/defi-nft-risks.md`](../notes/3-crypto-aml/defi-nft-risks.md) — 2절 (NFT)

## 🌐 외부 자료 (~15분)
- [Chainalysis — NFT 관련 Crypto Crime](https://www.chainalysis.com/) (사이트 내 검색)

## 🛠️ 미니 챌린지 (~10분)
- Self-trading 시나리오 직접 그리기 (A→B→A 같은 NFT)
- Loop trading 시나리오 (3자 순환)
- 탐지 룰 의사코드:
  ```
  IF (same_NFT_traded ≥3 times in 7d 
      AND price_change > 5x
      AND addresses share cluster)
    THEN flag as wash trade
  ```

## ✅ 체크포인트
- [ ] NFT 자금세탁 매력 (가격 자율 + 글로벌 즉시) 안다
- [ ] Wash trading 3패턴 (Self/Loop/Pump) 안다
- [ ] 한국 2024-06 FSC NFT 가이드라인 인지
- [ ] FATF NFT VA 분류 기준 안다

## 💭 오늘의 한 줄
