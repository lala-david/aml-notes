# 관할 크로스워크 — 송신인 정보 전달 의무

> 🤖 자동 생성 (`python scripts/build_crosswalk.py`). 직접 편집하지 마세요.
> 의무 노드: `OBL:x-travel-rule-originator` · 기준 시점: 전체

> 가상자산을 보낼 때, 보내는 쪽 사업자가 받는 쪽 사업자에게 "누가 보냈는지"를 이체와 동시에 또는 그 전에 알려야 하는 의무. 나라를 가리지 않는 공통 형태로 적어 둔 것이며, 이 의무를 실제로 정하는 조문은 나라마다 다르다. 기준금액이나 개인지갑 취급 같은 나라별 차이는 각 조문 쪽에 붙어 있다.

| 관할 | 근거 조문 | 임계값 | 통화 | 유효기간 | 확신도 |
|---|---|---:|---|---|---|
| 🌐 국제기준 | `INR.15 §7(b)` | 임계값 없음 | — | 2019-06 ~ 현재 | A |
| 🇦🇺 호주 | `section 66A` | 임계값 없음 | — | ? ~ 현재 | A |
| 🇪🇺 EU | `Article 14` | 임계값 없음 | — | 2024-12-30 ~ 현재 | A |
| 🇬🇧 영국 | `regulation 64C` | 임계값 없음 | — | ? ~ 현재 | A |
| 🇭🇰 홍콩 | `Schedule 2, section 13A` | 임계값 없음 | — | ? ~ 현재 | A |
| 🇯🇵 일본 | `第十条の五` | 임계값 없음 | — | ? ~ 현재 | A |
| 🇰🇷 한국 | `제5조의3` | 임계값 없음 | — | 2022-03-25 ~ 현재 | A |
| 🇰🇷 한국 | `제10조의10 제1호` | 1,000,000 | KRW | 2022-03-25 ~ 현재 | A |
| 🇸🇬 싱가포르 | `paragraph 13` | 임계값 없음 | — | ? ~ 현재 | A |
| 🇺🇸 미국 | `31 CFR 1010.410(f)` | 3,000 | USD | ? ~ 현재 | B |

## 등재된 조문

- `PROV:au-amlctf-s66a` — AML/CTF법 제66A조 (소속 규범 `REG:au-amlctf`)
- `PROV:eu-tfr-art14` — TFR 제14조 (소속 규범 `REG:eu-tfr`)
- `PROV:gb-mlr2017-reg64c` — MLR 2017 reg 64C (소속 규범 `REG:gb-mlr2017`)
- `PROV:hk-amlo-sch2-s13a` — AMLO 부칙2 §13A (소속 규범 `REG:hk-amlo`)
- `PROV:intl-fatf-inr15-p7b` — INR.15 §7(b) (소속 규범 `REG:intl-fatf-r15`)
- `PROV:jp-aptcp-art10-5` — 범수법 제10조의5 (소속 규범 `REG:jp-aptcp`)
- `PROV:kr-tfia-art5-3` — 특금법 제5조의3 (소속 규범 `REG:kr-tfia`)
- `PROV:kr-tfia-sd-art10-10` — 시행령 제10조의10 (소속 규범 `REG:kr-tfia-sd`)
- `PROV:sg-psn02-para13` — PSN02 §13 (소속 규범 `REG:sg-psn02`)
- `PROV:us-bsa-cfr1010-410f` — 31 CFR 1010.410(f) (소속 규범 `REG:us-bsa`)
