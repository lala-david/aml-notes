# 2️⃣ Regulations — 규제 맵

> 가상자산 AML 관련 규제의 전체 지도. 마지막 업데이트: 2026-04-17.

## 한 장으로 보는 계층

```
                    ┌─────────────────────────┐
                    │   FATF (국제 표준)        │
                    │   Recommendation 15, 16  │
                    └────────────┬─────────────┘
                                 │ 권고 → 회원국 도입
            ┌────────────────────┼─────────────────────┐
            ▼                    ▼                     ▼
    ┌──────────────┐    ┌──────────────┐    ┌────────────────┐
    │   한국         │    │   미국         │    │      EU        │
    │ 특금법 + 이용자  │    │ BSA + USAPA   │    │ MiCA + AMLR +  │
    │ 보호법         │    │ FinCEN/OFAC   │    │ AMLD6 + TFR    │
    │ 감독: FIU/FSC  │    │              │    │ 감독: AMLA/NCA  │
    └──────────────┘    └──────────────┘    └────────────────┘
```

## 영역별 문서

| 파일 | 다루는 내용 |
|---|---|
| [`global_fatf.md`](global_fatf.md) | FATF 권고안 (R.15, R.16), Travel Rule, 상호평가 |
| [`korea_fiu_act.md`](korea_fiu_act.md) | 한국 특정금융정보법 (특금법) — VASP 신고제 |
| [`korea_user_protection.md`](korea_user_protection.md) | 가상자산이용자보호법 (2024.7.19 시행) |
| [`us_bsa_fincen.md`](us_bsa_fincen.md) | 미국 BSA, FinCEN, OFAC, GENIUS Act (스테이블코인) |
| [`eu_mica_amlr.md`](eu_mica_amlr.md) | EU MiCA, AMLR/AMLD6, TFR (Travel Rule) |

## 적용 우선순위 (한국 법인 / 한국 신고 VASP 기준)

1. **🔴 1순위 (직접 적용)** — 한국 특금법 + 가상자산이용자보호법 + FIU 고시
2. **🟠 2순위 (글로벌 거래/해외고객)** — FATF 표준, 외국 VASP와의 Travel Rule 호환
3. **🟡 3순위 (해외 진출/자회사 시)** — EU MiCA, US BSA
4. **⚪ 항시 의식** — OFAC/UN 제재 (전 세계 적용)

## 핵심 일정 (2026~2027)

| 시점 | 사건 |
|---|---|
| 2024-07-19 | 한국 가상자산이용자보호법 시행 |
| 2024-12-30 | EU MiCA 전면 시행 |
| 2025-03-21 | OFAC, Tornado Cash 제재 해제 |
| 2025-06-18 | FATF Recommendation 16 개정 |
| 2025-07 | 미국 GENIUS Act 통과 (스테이블코인 BSA 적용) |
| 2026-01-29 | 한국 특금법 개정안 통과 (대주주 자격심사 강화) |
| 2026-07-01 | EU MiCA grandfathering 종료 (CASP 라이센스 의무) |
| 2026-07-18 | 미국 GENIUS Act 시행규정 마감 |
| 2026 후반 | FATF Travel Rule 가이던스 발표 예정 |
| 2027-01-18 | 미국 GENIUS Act 전면 시행 |
| 2027-07-10 | EU AMLR + AMLD6 적용 |
| 2030년 말 | FATF R.16 개정 발효 |
