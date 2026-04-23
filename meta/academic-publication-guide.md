# 학술·산업 발표 경로 — Academic & Industry Publication Guide

> 본 저장소의 콘텐츠를 **학술 논문·산업 발표·콘퍼런스**로 확장해 국제 신뢰도를 확보하는 가이드. 마지막 갱신: 2026-04-23.

## TL;DR

- **arXiv**: 기술 논문 (Exposure Score·CIOH·Korean Fuzzy 알고리즘)
- **SSRN**: 법·정책 논문 (특금법 해석·감독 검사 체계)
- **ACAMS**: Annual Conference 발표·Today 매거진 기고
- **학회**: 한국상사법학회·경제법학회·정보보호학회
- **컨퍼런스**: Chainalysis Links·Consensus·Korea Blockchain Week

## 1. arXiv 제출 가이드 (기술 논문)

### 적합한 주제 (저장소에서 파생 가능)

1. **"Korean Fuzzy Matching for OFAC Screening: FP 90% → 12% via Surname Filtering"**
   - 출처: notes/5-compliance/sanctions-screening.md §N
   - 카테고리: cs.CR (cryptography and security) + cs.DB
   - 분량: 8~12 페이지

2. **"Exposure Score Formula for Crypto AML: A Vendor-Generalized Model"**
   - 출처: notes/4-technology/blockchain-analytics.md §4
   - 카테고리: cs.CR
   - 분량: 10~15 페이지

3. **"CoinJoin Fingerprint Detection: Benchmarking on Elliptic2"**
   - 출처: 동 §2
   - 카테고리: cs.CR + cs.LG
   - 분량: 8~10 페이지

4. **"Cross-Chain Bridge Matching Algorithm with Nonce Prioritization"**
   - 출처: 동 §5
   - 카테고리: cs.CR + cs.DC
   - 분량: 10~14 페이지

### arXiv 제출 절차

1. **LaTeX 템플릿 선택** — Springer·IEEE 등 자유 (arXiv 양식 요구 없음)
2. **저자 등록** — arxiv.org/login (무료, 약 3일 검증)
3. **endorsement 필요** — cs.CR 카테고리는 기존 저자 1명의 endorsement 필요
   - 업계 연구자 (Chainalysis·Elliptic 연구팀) 연락
   - 대학 가상자산 연구실 지도교수 접촉
4. **제출** — PDF + source files
5. **검토** — 1~3일 자동 검토 후 공개

### 체크리스트

- [ ] 저자·소속 정확히
- [ ] abstract 200 단어 이내
- [ ] reference 15+ (본 저장소 deep/papers.md 활용)
- [ ] code·data 공개 의사 표시 (GitHub link)
- [ ] Korean keywords + English keywords

## 2. SSRN 제출 (법·정책 논문)

### 적합한 주제

1. **"Korean Tukgeumbeop §5 and Crypto VASPs: Interpretive Analysis"**
2. **"Regulatory Inspection Response for Korean VASPs: A Practical Framework"**
3. **"Comparative Analysis of Travel Rule: Korea, US, EU, Asia"**

### SSRN 절차

1. [ssrn.com](https://www.ssrn.com) 저자 등록 (무료)
2. 관련 Network 선택 (Cyber Security, Financial Regulation, Comparative Law)
3. PDF 업로드
4. 즉시 공개

### 유리한 점
- Endorsement 불필요
- 즉시 공개
- DOI 자동 발급

## 3. ACAMS (Certified AML Specialists) 발표

### Annual Conference

- 매년 9월 (미국 Las Vegas 또는 Hollywood FL)
- **Call for Proposals**: 매년 2~3월
- 제안서 양식: acams.org/events
- 분량: 50분 발표 + 10분 Q&A
- **한국 관련 세션 수요 증가** — "Korean VASP Compliance" 카테고리

### 제안 가능한 발표

1. "How Korean VASPs Prepare for FIU Inspections — 4-Week Playbook"
2. "Tukgeumbeop 2026 Amendment: Major Shareholder Review for Crypto Exchanges"
3. "Korean Fuzzy Matching: Lessons from OFAC Screening of 5M Korean Names"

### ACAMS Today 매거진

- 분기별 출간
- **2000 단어** 기고 (peer-reviewed)
- 원고료 지급 (~$500)
- 제출: acamstoday.org/contribute

## 4. 한국 학회 발표

### 한국상사법학회
- **학술대회**: 연 2회 (춘·추)
- **Call for Papers**: 2~3개월 전
- **분량**: 15~25 페이지 한국어
- **심사**: peer review
- **논문지 등재**: 상사법연구

### 한국경제법학회
- 규제 경제·소비자 보호 관점
- **학술대회**: 연 3~4회

### 한국정보보호학회
- 기술 보안·블록체인 관점
- **정보보호학회지** 학술 논문

### 제안 주제 (한국 맥락)
1. "특금법 §5-3 Travel Rule의 실무 적용 — 한국 4대 거래소 현황"
2. "가상자산 감독 검사 체계 — KoFIU·FSS·FSC 3-tier 구조"
3. "DAXA 자율규제의 법적 지위와 실효성"

## 5. 산업 콘퍼런스

### Chainalysis Links (글로벌)
- **일정**: 매년 4월 (뉴욕)
- **발표 기회**: 초청 + 제안
- **주제**: Crypto Crime·AML Tools·Industry Trends
- **한국 참여**: 람다256·Upbit 대표 발표 선례 있음

### Korea Blockchain Week (KBW)
- **일정**: 매년 9월 (서울)
- **AML 트랙**: 있음 (DAXA·FIU 초청 연사)
- **제안**: koreanblockchainweek.com/speakers

### Consensus (Coindesk)
- **일정**: 매년 5월 (덴버·LA)
- **Track**: Regulation·Compliance
- **한국 세션**: 드물지만 기회 있음

## 6. 출판 전 체크리스트

- [ ] 본 저장소 원본을 저자 명시 인용 (CC BY 4.0 의무)
- [ ] 발표 원고가 저장소 원본과 일치 (사실 관계)
- [ ] 영문 원고 — native speaker 검토
- [ ] 한글 원고 — 학회 양식·인용 스타일 준수
- [ ] 발표 슬라이드는 별도 오픈소스 (slideshare 등)
- [ ] 피드백은 저장소 Issue로 수집 (`academic-feedback` 라벨)

## 7. 제출 추적 시트

| 제목 | 플랫폼 | 제출일 | 상태 | 비고 |
|---|---|---|---|---|
| (예시) Korean Fuzzy Matching | arXiv cs.CR | 2026-Q3 | 계획 | endorsement 필요 |
| (예시) Tukgeumbeop §5 | SSRN | 2026-Q3 | 계획 | |
| (예시) Inspection Playbook | ACAMS 2026 | 2026-02 (CFP) | 미제출 | |

## 8. 저작권·인용 정책

본 저장소 CC BY 4.0 → 학술 논문에서 사용 시:
- **인용 형식**: "AML Notes (2026). lala-david. GitHub: https://github.com/lala-david/aml-notes"
- **공동 저자 불가** — 원본 저자 명시만
- **수정·확장 OK** — 학술 원고는 더 rigor 할 수 있음
- **상업적 사용 OK** — 인용만 하면

## 9. 파트너십 기회

학술 발표 + 공동 저술 시:
- **대학 연구실 (KAIST·연세·서울·POSTECH)** — 공동 저자 가능
- **법학회** — 특별 세션·공동 심포지엄
- **벤더 (Chainalysis·Elliptic)** — 데이터 협력 연구

## 10. 추적 & 결과 반영

발표·출간 후 저장소에 반영:
- [`deep/papers.md`](../deep/papers.md)에 추가
- [`CHANGELOG.md`](../CHANGELOG.md)에 academic 태그
- README badge: "arXiv" 또는 "Conference Presented"

학술 활동이 저장소의 장기 신뢰성을 결정짓습니다.
