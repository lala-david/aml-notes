# 60-Day AML Daily Challenge

> 가상자산 AML을 60일(2개월) 데일리 챌린지로 마스터. 마지막 업데이트: 2026-04-17.

## 한 장 요약

- **기간**: 60일 (8주 + 캡스톤 4일)
- **하루 투자**: 60~120분 (평일 60~90, 주말 90~120 권장)
- **구조**: 매일 1개 토픽 + 매주 1개 미니 프로젝트 + 마지막 캡스톤
- **결과물**: 60개 체크된 일일 노트 + 8개 동작하는 미니 프로젝트 + 1개 캡스톤 + 다음 90일 로드맵

## 8주 테마

| 주차 | 일자 | 테마 | 미니 프로젝트 |
|---|---|---|---|
| **Week 1** | D1~D7 | AML 기초 + 가상자산 특수성 | 마인드맵 + 퀴즈 |
| **Week 2** | D8~D14 | 한국 규제 (특금법 + 이용자보호법) deep | 한국법 §단위 정리표 |
| **Week 3** | D15~D21 | FATF + 글로벌 규제 (US/EU) | 한·미·EU Travel Rule 비교표 |
| **Week 4** | D22~D28 | Travel Rule + IVMS101 + 프로토콜 | **🛠️ IVMS101 메시지 빌더 (Python)** |
| **Week 5** | D29~D35 | 온체인 분석 + KYT 기술 | **🛠️ Etherscan API 2-hop tracer** |
| **Week 6** | D36~D42 | 자금세탁 유형 + DeFi/Mixer | **🛠️ Mixer 주소 라벨 fetcher** |
| **Week 7** | D43~D49 | 컴플라이언스 운영 + 거버넌스 | **🛠️ OFAC SDN 가상자산 wallet 스크리너** |
| **Week 8** | D50~D56 | 사례 + 최신 리서치 + AI/ML | **🛠️ KYT API 호출 wrapper** |
| **Capstone** | D57~D60 | 통합 + 미래 + 다음 단계 | **🎓 Mini AML Risk Engine 설계서** |

## 일일 파일 구조

각 `day_NN.md`는 다음 섹션:

```
# Day NN — Topic

🎯 핵심 질문 (3개)
📖 읽기 (~50분, 기존 노트 링크)
🌐 외부 자료 (선택, 링크)
🛠️ 미니 챌린지 (~20분, 구체 과제)
✅ 체크포인트 (3~5개 박스)
💭 오늘의 한 줄 (직접 작성)
```

**완료 기준**: 체크포인트 모두 체크 + 한 줄 작성 + (해당 시) 미니 챌린지 산출물 저장.

## 사용 방법

1. 매일 그날의 `day_NN.md` 열기
2. 읽기 → 외부자료 → 미니 챌린지 → 체크포인트 순으로 진행
3. 끝나면 [`progress.md`](progress.md) 에 체크 + 그날의 한 줄 옮기기
4. 미니 프로젝트 결과물은 [`../09_automation/`](../09_automation/) 에 저장

## 학습 페이스 가이드

- **하루 빠짐 OK** — 다음날 따라잡으면 됨
- **2일 연속 빠짐** — 그날(들) 핵심 질문만 답변하고 패스
- **1주 빠짐** — 주차 미니 프로젝트만 하고 다음 주로
- **완벽주의 금지** — 80% 이해 + 진도 우선

## 빠른 인덱스

### Week 1 — 기초
| Day | 토픽 |
|---|---|
| [D1](day_01.md) | AML이 뭔가 + ML 3단계 |
| [D2](day_02.md) | 왜 가상자산 AML은 다른가 |
| [D3](day_03.md) | 핵심 용어 1 (KYC/CDD/EDD/SDD) |
| [D4](day_04.md) | 핵심 용어 2 (KYT/STR/CTR/PEP/BO) |
| [D5](day_05.md) | AML 글로벌 거버넌스 지도 |
| [D6](day_06.md) | VASP 정의 + 9 의무 |
| [D7](day_07.md) | 🔁 Week 1 리뷰 + 마인드맵 |

### Week 2 — 한국 규제 deep
| Day | 토픽 |
|---|---|
| [D8](day_08.md) | 특금법 1 — VASP 신고제 |
| [D9](day_09.md) | 특금법 2 — 의무 + 2026 개정 |
| [D10](day_10.md) | 이용자보호법 1 — 자산 분리 |
| [D11](day_11.md) | 이용자보호법 2 — 시세조종 + 2단계 입법 |
| [D12](day_12.md) | KoFIU 시스템 + 보고 절차 |
| [D13](day_13.md) | 한국 가이드라인 정독 (RBA, 신고매뉴얼) |
| [D14](day_14.md) | 🛠️ 한국법 §단위 정리표 + 1주 리뷰 |

### Week 3 — FATF + 글로벌
| Day | 토픽 |
|---|---|
| [D15](day_15.md) | FATF 구조 + 40 권고안 |
| [D16](day_16.md) | R.15 (VASP에 AML 부과) |
| [D17](day_17.md) | R.16 + 2025-06 개정 |
| [D18](day_18.md) | US BSA + FinCEN |
| [D19](day_19.md) | US OFAC + 2차 제재 + GENIUS Act |
| [D20](day_20.md) | EU MiCA + AMLR/AMLD6 + TFR |
| [D21](day_21.md) | 🛠️ 한·미·EU Travel Rule 비교표 |

### Week 4 — Travel Rule + IVMS101
| Day | 토픽 |
|---|---|
| [D22](day_22.md) | Travel Rule 운영 흐름 |
| [D23](day_23.md) | IVMS101 표준 deep |
| [D24](day_24.md) | TRP, TRISA 프로토콜 |
| [D25](day_25.md) | VerifyVASP, CODE 한국 |
| [D26](day_26.md) | Notabene Gateway + Sunrise |
| [D27](day_27.md) | VASP Discovery + DTI/LEI |
| [D28](day_28.md) | 🛠️ IVMS101 메시지 빌더 (Python) |

### Week 5 — 온체인 분석
| Day | 토픽 |
|---|---|
| [D29](day_29.md) | KYC vs KYT 운영 |
| [D30](day_30.md) | UTXO + Common Input Ownership |
| [D31](day_31.md) | Change Detection + Deposit Heuristic |
| [D32](day_32.md) | Address Attribution + 라벨 DB |
| [D33](day_33.md) | Exposure Score (direct vs N-hop) |
| [D34](day_34.md) | Cross-chain tracing + bridge |
| [D35](day_35.md) | 🛠️ Etherscan API 2-hop tracer |

### Week 6 — 자금세탁 유형 + DeFi
| Day | 토픽 |
|---|---|
| [D36](day_36.md) | 자금세탁 7 typology 종합 |
| [D37](day_37.md) | Mixer + Privacy coin |
| [D38](day_38.md) | Peel chain + Smurfing |
| [D39](day_39.md) | DeFi 자금세탁 (DEX/LP/flash loan) |
| [D40](day_40.md) | NFT wash trading |
| [D41](day_41.md) | CMLN 중국어 자금세탁 네트워크 |
| [D42](day_42.md) | 🛠️ Mixer 주소 라벨 fetcher |

### Week 7 — 컴플라이언스 운영
| Day | 토픽 |
|---|---|
| [D43](day_43.md) | CDD 4단계 운영 |
| [D44](day_44.md) | EDD 트리거 + 자금원천 증빙 |
| [D45](day_45.md) | STR 작성 SOP |
| [D46](day_46.md) | 제재 스크리닝 (이름 + wallet) |
| [D47](day_47.md) | 내부통제 5 pillars + 3LoD |
| [D48](day_48.md) | AMLO 역할 + 거버넌스 |
| [D49](day_49.md) | 🛠️ OFAC SDN crypto wallet 스크리너 |

### Week 8 — 사례 + 리서치 + AI
| Day | 토픽 |
|---|---|
| [D50](day_50.md) | 케이스 — Lazarus DPRK + Bybit |
| [D51](day_51.md) | 케이스 — Tornado Cash + DeFi 제재 |
| [D52](day_52.md) | 케이스 — Binance/OKX/Paxful |
| [D53](day_53.md) | 케이스 — 한국 enforcement |
| [D54](day_54.md) | 학술 논문 — Bitcoin clustering |
| [D55](day_55.md) | 산업 리포트 — Chainalysis 2026 |
| [D56](day_56.md) | 🛠️ KYT API 호출 wrapper |

### Capstone (D57~D60)
| Day | 토픽 |
|---|---|
| [D57](day_57.md) | AI/ML in AML |
| [D58](day_58.md) | ZKP + 프라이버시-컴플라이언스 양립 미래 |
| [D59](day_59.md) | 🎓 Mini AML Risk Engine 설계서 |
| [D60](day_60.md) | 다음 90일 로드맵 |

## 산출물 체크

- [ ] 60일 일일 노트 모두 체크
- [ ] 8개 미니 프로젝트 모두 작동
- [ ] 1개 캡스톤 설계서
- [ ] 90일 로드맵 작성

진척 트래킹: [`progress.md`](progress.md)
