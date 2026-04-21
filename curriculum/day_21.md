# Day 21 — 🛠️ 한·미·EU Travel Rule 비교표 + 3주 리뷰

> 글로벌 규제 정리 + 시각화. ⏱️ ~120분.

## 📖 오늘 뭘 배우나

한국·미국·EU 규제를 각각 배웠으니 이제 **한 장에 나란히** 놓고 차이를 정리합니다. Travel Rule 임계금액·stablecoin 접근·unhosted wallet 처리 등 실무에서 바로 판단이 필요한 6~8개 축을 표로 만듭니다. 이 표가 있으면 글로벌 거래 시나리오에서 "어느 나라 룰을 기준으로 설계할지" 결정이 빨라집니다.


<!-- MAP-START -->
## 🗺 오늘의 지도

```mermaid
flowchart LR
    KR["🇰🇷 100만원"] & US["🇺🇸 $3,000"] & EU["🇪🇺 임계 無"] --> TR["Travel Rule 대상"]
    KR -.특이.-> UW["외부지갑 등록제"]
    US -.특이.-> UM["unhosted 룰 부재"]
    EU -.특이.-> UE["unhosted 1,000€+ 신원검증"]
    style KR fill:#e5eaf2,stroke:#1a2e4a
    style US fill:#fff7d6,stroke:#c9a646
    style EU fill:#fed7aa,stroke:#ea580c
```
<!-- MAP-END -->

## 🎯 회고 질문
1. 한·미·EU 중 가장 빡빡한 임계금액은?
2. 미국과 EU의 stablecoin 접근 차이는?
3. 한국 사업자가 글로벌 영업 시 1순위 호환 이슈는?

## 🛠️ 메인 미니 프로젝트 (~90분)

**목표**: 한·미·EU Travel Rule + AML 핵심 항목 비교표 작성

### 형식 (예시)
| 항목 | 한국 | 미국 | EU |
|---|---|---|---|
| 모법 | 특금법 | BSA + USA PATRIOT | AMLR (2027-07~) |
| 가상자산 모법 | 가상자산이용자보호법 | GENIUS Act (stablecoin) | MiCA + TFR |
| 사업자 명칭 | VASP | MSB | CASP |
| 라이센스/신고 | FIU 신고 (3년) | FinCEN MSB + 주별 MTL | NCA 라이센스 (EU passporting) |
| Travel Rule 임계 | 100만원 | $3,000 | 없음 |
| TR 시행 | 2022-03-25 | 1996+ | 2024-12-30 |
| Unhosted wallet | 외부지갑 등록제 | 부재 | 1,000 EUR+ 신원검증 |
| KYC | 특금법 §5의2 | BSA CDD Rule | AMLR |
| EDD 트리거 | RBA 가이드 | BSA + OFAC | AMLR + 27개국 통합 |
| STR/SAR | 특금법 §4 | SAR (BSA) | STR (AMLR) |
| CTR/임계 | 1천만원 | $10,000 | EU 현금 €10K |
| 기록보관 | 5년 (특금법) / **15년 (이용자보호법)** | 5년 | 5년 |
| 제재기관 | 외교부 + FIU | OFAC | EU + AMLA |
| 미신고 처벌 | 5년/5천만원 | $250K+ + 형사 | 최대 €10M / 매출 5% |

→ 자기 손으로 다시 작성 (외운 척 하지 말고 노트 보면서 OK, 핵심은 구조 머릿속)

→ 결과물 저장: `aml/curriculum/_artifacts/d21_global_travel_rule_compare.md`

## ✅ 체크포인트
- [ ] 비교표 산출
- [ ] [`progress.md`](progress.md) Week 3 7개 모두 체크
- [ ] 한·미·EU 핵심 차이 5개 즉답 가능

## 💭 3주차 회고

가장 까다로운 관할:
가장 단순한 관할:
실무에서 1순위로 호환 봐야 할 것:
