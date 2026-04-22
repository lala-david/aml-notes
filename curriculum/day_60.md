# Day 60 — 🎓 다음 90일 로드맵

> 60일 끝, 90일 시작. ⏱️ ~120분.

## 📖 오늘 뭘 배우나

60일의 마지막 날. 오늘은 **"앞으로 90일"** 의 구체 로드맵을 작성합니다. 4개 전공 트랙(기술·법·컴플라이언스·솔루션) 중 자신의 관심과 경력에 맞는 1개를 선택해 월별 마일스톤을 세우면, 60일 챌린지가 **지속 성장 궤도**로 이어집니다.


<!-- MAP-START -->
## 🗺 오늘의 지도

```mermaid
flowchart LR
    C["🎓 60일 완주"] --> TA["Track A<br/>기술·KYT"]
    C --> TB["Track B<br/>법·규제"]
    C --> TC["Track C<br/>컴플 운영"]
    C --> TD["Track D<br/>솔루션·제품"]
    TA & TB & TC & TD --> M["🗓 M1·M2·M3 마일스톤"]
    M --> G["🎯 90일 후 도달"]
    style C fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style G fill:#d1fae5,stroke:#10b981
```
<!-- MAP-END -->

## 🎯 회고 질문 (60일 통합)

1. 가장 큰 변화 (Day 1과 Day 60의 나):
2. 가장 의외였던 영역:
3. 가장 약한 영역 (보강 필요):
4. 가장 흥미 있는 전공 영역:

## 🛠️ 90일 로드맵 작성 (~90분)

### 산출물
파일: `aml/curriculum/_artifacts/d60_90_day_roadmap.md`

### 4개 전공 트랙 중 선택

#### 트랙 A — 기술 (KYT/Analytics)
- 자체 attribution DB 구축
- ML 기반 클러스터링 실험
- Cross-chain tracing 깊이
- 산출물: 작동하는 KYT 프로토타입

#### 트랙 B — 법/규제
- 특금법 + 이용자보호법 § 단위 마스터
- FATF/EU/US 깊이 비교
- 한국 가상자산 변호사 자료 + 컨퍼런스 참석
- 산출물: 한국 VASP 컴플라이언스 핸드북

#### 트랙 C — 컴플라이언스 운영
- AMLO 실무 (정책/룰/감사 사이클)
- STR 분석가 트레이닝 자료
- ERA 작성
- 산출물: AMLO 운영 매뉴얼 + 룰 카탈로그

#### 트랙 D — 솔루션/제품
- KYT/Travel Rule 솔루션 시장 깊이
- 신규 제품 아이디어 (한국 특화 + 글로벌)
- 비즈니스 모델
- 산출물: 신규 솔루션 1-pager + MVP 사양

### 90일 플랜 템플릿

```markdown
# 90-day Roadmap — Track [A/B/C/D]

## 핵심 목표
- 90일 후 도달 상태 (구체):

## 월별 마일스톤
- M1 (1~30일): _______
- M2 (31~60일): _______
- M3 (61~90일): _______

## 주간 학습 페이스
- 평일: __h
- 주말: __h

## 산출물 (3개)
- 1. _______
- 2. _______
- 3. _______

## 리뷰 시점
- D30: 1차 리뷰
- D60: 2차 리뷰 + 조정
- D90: 최종 평가 + 다음 단계
```

## ✅ 체크포인트
- [ ] 60일 회고 작성
- [ ] 트랙 1개 선택
- [ ] 90일 로드맵 작성
- [ ] [`progress.md`](progress.md) Capstone 4일 모두 체크
- [ ] 60일 챌린지 git tag (예: `v1.0-60day-completed`)

## 💭 60일 마지막 한 줄

> 이 60일이 나에게 가르쳐준 것:
> 다음 90일에 시도할 한 가지:

---

🎉 **60일 챌린지 완주 축하!** 🎉

이제 [`../README.md`](../README.md) 우선순위 Top 5 를 다시 보면 — 시작할 때와 완전히 다른 눈으로 보일 거임.

## 💼 실무 현장 (Industry Reality)

### 한국 AML 커리어 지도 (2026 기준)

4개 트랙은 실제 업계의 4가지 직군과 대응:

| 트랙 | 실제 포지션 | 주요 채용사 | 연봉(한국) |
|---|---|---|---|
| A 기술·KYT | KYT Engineer · Data Scientist | Upbit·람다256·Bithumb·Chainalysis Korea | 주니어 5,500~8,000만 / 시니어 1~1.8억 |
| B 법·규제 | AML Legal · Compliance Counsel | 김앤장·광장·세종·VASP 법무팀 | 변호사 1~3년차 1~1.5억 |
| C 컴플 운영 | AML Analyst · AMLO · MLRO | 전 VASP · 은행 컴플실 | 주니어 4,500~6,500만 / AMLO 1.5~3억 |
| D 솔루션·제품 | Product Manager · Solutions Engineer | VerifyVASP·CODE·Chainalysis | 시니어 1~2억 |

### 글로벌 진출 시 참고 (2026)

- **Singapore MAS**: 아시아 허브 1순위 · 한국 출신 AML 수요 많음
- **Dubai VARA**: 대형 거래소 AMLO hub · Binance·OKX·Crypto.com 소재
- **London FCA**: 유럽 규제 중심 · MiCA 확산
- **New York DFS**: 미국 진입 게이트 · BitLicense 보유 기관 제한적
- **한국 출신의 국제 이동**: **Chainalysis·TRM·Elliptic Korea** 또는 글로벌 HQ 직이동이 가장 흔한 경로

### 90일 로드맵 실제 샘플 (트랙 C 예시)

```
M1 (1~30일):
- Chainalysis Certified Investigator (CCI) 자격 취득
- FIU-TIS 포털 UI·STR 양식 3번 작성 연습
- 한국 VASP 실제 STR 공개 사례 10건 분석

M2 (31~60일):
- 현 회사/희망 회사의 ERA 문서 접근·정독
- Alert 큐 실제 shadowing 2주 (멘토 붙여)
- 룰 카탈로그 10개 직접 작성·위원회 발표

M3 (61~90일):
- 연례 AML 교육 자료 1편 제작 (사내 배포)
- FIU 검사 Q&A 스크립트 작성·훈련
- AMLO 후보군 진입 (임원 멘토링)
```

### 자격증·컨퍼런스 지도 (2026)

- **ACAMS CAMS**: 글로벌 표준 AML 자격 · 한국 응시자 증가 추세
- **ACAMS CCAS (Crypto Asset Specialist)**: 가상자산 특화
- **Chainalysis CCI / CEI**: 블록체인 조사·이더 특화
- **한국 자격**: 금융투자협회 AMLO 교육(3일 집합), FIU 정례 교육
- **컨퍼런스**: ACAMS Las Vegas (10월) · Links Chainalysis (5월) · Korea Blockchain Week (9월) · DAXA 공동세미나

### 자주 나오는 오해

- **"AMLO = 법무 출신"** — 2020년 이전은 맞지만 2026 현재 **데이터·엔지니어링 배경 AMLO 증가**. Upbit·코빗의 차기 AMLO 후보군에 엔지니어 백그라운드 다수.
- **"자격증이 있어야 채용"** — 한국은 **실무 경험·코드·STR 품질**이 자격보다 무게. CAMS는 있으면 유리하지만 필수 아님.
- **"60일로 충분"** — 60일은 **입문 완료**. 실무 역량은 **최소 2~3년 누적**. 그러나 60일을 한 사람과 안 한 사람의 출발선은 다름.

