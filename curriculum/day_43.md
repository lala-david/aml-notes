# Day 43 — CDD 4단계 운영

> 표준 실사 프로세스 deep. ⏱️ ~70분.

## 📖 오늘 뭘 배우나

Week 7은 컴플라이언스 운영 주간. 먼저 모든 고객에게 적용되는 **CDD 4단계**(식별·BO·목적·모니터링)를 운영 관점에서 깊이 봅니다. 특히 **지속 모니터링**이 onboarding 1회로 끝나지 않는다는 원칙, 그리고 한국 RBA 가이드라인의 재실사 주기(저5/중3/고1년)를 정리.

## 🎯 핵심 질문
1. CDD 4단계 (식별/BO/목적/모니터링) 각 핵심 과제?
2. 한국 가이드라인의 RBA 4 차원?
3. 지속 모니터링 재실사 주기 (저5/중3/고1)?

## 📖 읽기 (~50분)
- 메인: [`../notes/5-compliance/cdd-edd.md`](../notes/5-compliance/cdd-edd.md) — 1, 3절

## 🛠️ 미니 챌린지 (~15분)
- 가상 신규 고객 1명 시나리오 → CDD 4단계 모두 적용 메모
- "재실사 주기 알림 시스템" 가벼운 SQL 의사코드:
  ```sql
  SELECT customer_id FROM customers
  WHERE risk_level = 'HIGH' AND last_kyc_date < NOW() - INTERVAL '1 year'
  ```

## ✅ 체크포인트
- [ ] CDD 4단계 외운다
- [ ] BO 25% 기준 안다
- [ ] 한국 RBA 4차원 + 등급별 통제 차이 안다
- [ ] 지속 모니터링 ≠ onboarding 1회 안다

## 💭 오늘의 한 줄
