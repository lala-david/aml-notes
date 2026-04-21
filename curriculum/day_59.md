# Day 59 — 🎓 캡스톤: Mini AML Risk Engine 설계서

> 60일 학습을 통합해서 시스템 설계. ⏱️ ~150분 (사전 회고 30분 + 캡스톤 작성 120분).

<!-- MAP-START -->
## 🗺 오늘의 지도

```mermaid
flowchart TB
    D["📘 Design Doc"] --> P["문제 정의"]
    D --> R["규제 매핑 (특금법 §·이용자보호법 §)"]
    D --> A["아키텍처"]
    D --> RS["Risk Score 모델"]
    D --> RC["룰 카탈로그 10+"]
    D --> G["거버넌스 (5 Pillars · 3LoD)"]
    D --> L["단계적 도입 로드맵"]
    style D fill:#1a2e4a,color:#fff,stroke:#1a2e4a
```
<!-- MAP-END -->

## 🎯 캡스톤 목표

**Mini AML Risk Engine 설계서 작성** — 가상자산 거래소/수탁용 통합 위험엔진의 1차 설계 문서.

## 🛠️ 캡스톤 (~150분)

### 산출물
프로젝트: `aml/projects/06-capstone-risk-engine/DESIGN.md`

### 설계서 목차 (필수)

```markdown
# Mini AML Risk Engine — Design Document

## 1. 문제 정의
- 우리가 풀려는 문제 (시나리오)
- 사업유형 (거래소 / 수탁 / OTC ...)
- 성공 기준

## 2. 적용 규제 매핑
- 한국 특금법 § 매핑
- 가상자산이용자보호법 § 매핑
- (해외 영업 시) FATF / OFAC / TFR

## 3. 데이터 소스
- KYC: ___ 벤더 (또는 본인확인기관)
- KYT: ___ 벤더 또는 자체 + 외부 결합
- Sanctions: OFAC + UN + EU + 외교부
- PEP/Adverse Media: ___ 벤더
- Travel Rule: ___ 솔루션

## 4. 시스템 아키텍처
- 컴포넌트 다이어그램 (KYC → Risk Engine → KYT → Sanctions → Travel Rule → STR)
- 데이터 흐름 (실시간 / 배치)
- 인터페이스 (API)

## 5. Risk Score 모델
- 입력 변수 (KYC 위험 + KYT 노출 + 거래 패턴)
- 가중치
- 등급 매핑 (LOW/MED/HIGH)
- threshold + 자동 액션

## 6. 룰 카탈로그
- 최소 10개 룰 (Smurfing / Pass-through / Mixer 노출 / SDN / ...)

## 7. 운영 플로우
- Onboarding
- 거래 시
- 일일 배치
- STR 생성
- 검사 대응

## 8. 거버넌스
- 5 pillars 어떻게 충족
- 3LoD 매핑
- AMLO 권한
- 교육 + 감사

## 9. 단계적 도입 로드맵
- MVP (3개월)
- v1 (6개월)
- v2 (12개월)

## 10. 리스크와 한계
- False positive / negative 균형
- 비용
- 인력
- 미해결 영역 (DeFi / Privacy coin)

## 11. 참고 (인용)
- 이 60일에 사용한 모든 자료 인용
```

### 작성 팁
- 분량: 4~10 페이지 (마크다운 기준)
- 구체성 우선 (예: "KYT" → "Chainalysis KYT API + 자체 라벨 매칭")
- 다이어그램 1개 이상 (Mermaid 또는 ASCII)
- 자기 회사 사업유형 1개 가정

## ✅ 체크포인트
- [ ] DESIGN.md 11절 모두 작성
- [ ] 다이어그램 1개+
- [ ] 룰 10개+
- [ ] 60일 학습 자료 인용 5개+

## 💭 오늘의 한 줄
