# Day 27 — VASP Discovery + DTI / GLEIF LEI

> 지갑 주소 → 어느 VASP인가? 라우팅의 핵심. ⏱️ ~75분.

## 📖 오늘 뭘 배우나

Travel Rule의 숨은 난제 — **지갑주소만으로는 카운터파티 VASP를 식별할 수 없다**. 이를 해결하기 위한 5가지 접근(Attribution DB·Directory·DTI·LEI·직접 등록)을 오늘 정리. **DTI**(ISO 24165 토큰 식별자)와 **GLEIF LEI**(법인 식별 글로벌 표준)가 어떻게 Travel Rule 라우팅의 기반이 되는지 알아둡니다.

## 🎯 핵심 질문
1. 지갑주소만 보고 카운터파티 VASP를 어떻게 식별?
2. DTI = 무엇? (ISO 24165)
3. GLEIF LEI = 무엇?

## 📖 읽기 (~50분)
- 메인: [`../notes/4-technology/travel-rule-protocols.md`](../notes/4-technology/travel-rule-protocols.md) — 5절
- 보조: [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) — 3절 (Attribution)

## 🌐 외부 자료 (~20분)
- [DTI Foundation](https://dtif.org/)
- [GLEIF LEI 공식](https://www.gleif.org/en/about-lei/introducing-the-legal-entity-identifier-lei)

## 🛠️ 미니 챌린지 (~5분)
- VASP Discovery 5가지 방법 (Attribution DB / VASP Directory / DTI / LEI / 직접 등록) 각 한 줄 정리

## ✅ 체크포인트
- [ ] 주소 → VASP 식별이 별도 인프라 문제임을 안다
- [ ] DTI = 토큰 식별 표준 안다
- [ ] LEI = 법인 식별 글로벌 표준 안다
- [ ] Chainalysis 등 attribution DB의 역할 안다

## 💭 오늘의 한 줄
