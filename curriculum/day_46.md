# Day 46 — 제재 스크리닝 (이름 + Wallet)

> OFAC/UN/EU/외교부 + 가상자산 SDN. ⏱️ ~80분.

## 🎯 핵심 질문
1. 핵심 제재 리스트 5개?
2. 이름 fuzzy 매칭의 함정?
3. Wallet 주소 매칭 3가지 (Direct/Cluster/Hop)?

## 📖 읽기 (~55분)
- 메인: [`../notes/5-compliance/sanctions-screening.md`](../notes/5-compliance/sanctions-screening.md) — 1~7절

## 🌐 외부 자료 (~15분)
- [OFAC SDN 검색](https://sanctionssearch.ofac.treas.gov/)
- [UN Consolidated List](https://www.un.org/securitycouncil/content/un-sc-consolidated-list)

## 🛠️ 미니 챌린지 (~10분)
- "Kim Min-soo" 같은 흔한 이름 → false positive 처리 흐름 메모
- Disposition 코드 3개 정의 (TP-Confirmed / FP-Different DOB / Pending)

## ✅ 체크포인트
- [ ] OFAC SDN + UN + EU + 외교부 5대 리스트 안다
- [ ] Wallet 매칭 3종 (Direct/Cluster/Hop) 안다
- [ ] False Positive disposition 흐름 안다
- [ ] OFAC 2차 제재의 글로벌 영향 안다

## 💭 오늘의 한 줄
