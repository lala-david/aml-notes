# Good First Issues — 처음 기여하실 때 추천

> 이 저장소의 첫 PR을 위한 **구체적이고 작은** 작업들. 각 Issue는 GitHub에 `good-first-issue` 라벨로 등록되어 있습니다.
> 마지막 갱신: 2026-04-21

---

## 한 눈에

| # | 카테고리 | 제목 | 난이도 | 예상 시간 |
|---|---|---|---|---|
| 1 | 사실 체크 | Bybit 탈취액 수치 통일 ($1.5B → $1.46B) | ★ | 30분 |
| 2 | 사실 체크 | FATF R.16 2025-06 개정일 표기 통일 | ★ | 30분 |
| 3 | 사실 체크 | 특금법 조항 번호 재검증 | ★★ | 2시간 |
| 4 | 사실 체크 | 한국 VASP 통계 갱신 (DAXA 2026-Q1) | ★★ | 1시간 |
| 5 | 사실 체크 | Chainalysis 누적 라벨 수 확인 | ★ | 30분 |
| 6 | 링크·차트 | 외부 URL 깨짐 수정 | ★ | 1시간 |
| 7 | 링크·차트 | Mermaid 다이어그램 가독성 개선 | ★★ | 2시간 |
| 8 | 링크·차트 | 규제 타임라인 차트 2026-Q3 이벤트 추가 | ★★ | 1시간 |
| 9 | 링크·차트 | Lazarus 탈취 누적 그래프 업데이트 | ★★ | 1시간 |
| 10 | 링크·차트 | Vendor 시장 점유율 차트 추가 | ★★★ | 3시간 |
| 11 | 번역·용어 | Glossary 한→영 10 용어 추가 | ★ | 1시간 |
| 12 | 번역·용어 | "고객확인" vs "실명확인" 혼용 정리 | ★★ | 1시간 |
| 13 | 번역·용어 | 금액 표기 통일 | ★ | 30분 |
| 14 | 번역·용어 | en/ 영문 에디션 어색한 구문 다듬기 | ★★ | 2시간 |
| 15 | 번역·용어 | 새 용어 5개 glossary 추가 | ★ | 1시간 |

---

## Issues 상세

### 카테고리 A: 사실 체크 (5개)

#### 1. Bybit 탈취액 수치 통일

- **문제**: 저장소 전체에서 Bybit 2025-02 탈취액이 `$1.5B`·`$1.46B` 혼용
- **액션**: 모든 파일에서 `$1.5B` → `$1.46B` 교체 (Chainalysis 공식 집계 기준)
- **검색**: `grep -r "1.5B\|\$1.5B" notes/ curriculum/ deep/`
- **검증**: Chainalysis 2025 Crypto Crime Report 인용 추가
- **라벨**: `good-first-issue`, `fact-check`

#### 2. FATF R.16 2025-06 개정일 표기 통일

- **문제**: "2025-06" · "2025.06" · "June 2025" · "2025년 6월" 혼용
- **액션**: 규칙 — 문장 본문은 `2025년 6월`, 표·메타데이터는 `2025-06`
- **영향 파일**: `notes/2-regulations/fatf-r16.md` 등 10+ 파일
- **라벨**: `good-first-issue`, `fact-check`, `style`

#### 3. 특금법 조항 번호 재검증

- **문제**: 특금법 §5-2·§5-3 등 조항 참조 정확성 확인 필요
- **액션**: 법령정보센터 (law.go.kr) 원문 대조
- **영향 파일**: `notes/2-regulations/korea-fiu-act.md`
- **산출**: 조항별 링크 + 확인 일자 테이블
- **라벨**: `good-first-issue`, `fact-check`, `legal`

#### 4. 한국 VASP 통계 갱신

- **문제**: VASP 수·이용자 수·거래량 수치가 2025 기준
- **액션**: DAXA 2026-Q1 공개 통계 반영
- **영향 파일**: `notes/3-crypto-aml/korea-vasp-landscape.md`
- **라벨**: `good-first-issue`, `fact-check`, `stats`

#### 5. Chainalysis 누적 라벨 수 확인

- **문제**: "Chainalysis 10억+ 라벨"식 표현 근거 확인
- **액션**: Chainalysis 공식 발표 자료 기준 최신 수치로
- **라벨**: `good-first-issue`, `fact-check`

---

### 카테고리 B: 링크·Mermaid (5개)

#### 6. 외부 URL 깨짐 수정

- **액션**: `scripts/check_external_urls.py` 실행 → 출력된 4xx/5xx URL 수정
- **실행**: `python scripts/check_external_urls.py > url-check.txt`
- **라벨**: `good-first-issue`, `link-rot`

#### 7. Mermaid 다이어그램 가독성 개선

- **문제**: 일부 차트 font-size 작음·색상 대비 낮음
- **액션**: Mermaid classDef 사용해 색상·굵기 개선
- **영향 파일**: `notes/3-crypto-aml/tx-flow.md`, `deep/` 내 6+ 파일
- **라벨**: `good-first-issue`, `mermaid`, `design`

#### 8. 규제 타임라인 차트 2026-Q3 이벤트 추가

- **액션**: 2026-Q3 예정 이벤트 3~5개 추가 (Pectra fork, EU MiCA 2차 등)
- **영향 파일**: `charts/regulation_timeline.svg` or `.mmd`
- **라벨**: `good-first-issue`, `chart`

#### 9. Lazarus 탈취 누적 그래프 업데이트

- **액션**: Chainalysis 2026 update 반영
- **영향 파일**: `charts/lazarus-cumulative.svg`
- **라벨**: `good-first-issue`, `chart`

#### 10. Vendor 시장 점유율 차트 추가

- **액션**: KYT 벤더 (Chainalysis·Elliptic·TRM·Merkle Science) 시장 점유율 차트 신규 작성
- **라벨**: `good-first-issue`, `chart`, `research`

---

### 카테고리 C: 번역·용어 (5개)

#### 11. Glossary 한국어→영어 10 용어 추가

- **액션**: `en/glossary.md` 에 한글 용어 10개 영문 정의 추가
  - 특금법, 이용자보호법, FIU, VASP, STR, CTR, EDD, RBA, PoR, 실명확인계좌
- **라벨**: `good-first-issue`, `translation`, `glossary`

#### 12. "고객확인" vs "실명확인" 혼용 정리

- **문제**: 동일 문서 내 두 용어 혼용
- **규칙**: 문서 1개에 1개 용어만 사용. `CONTRIBUTING.md` Style Guide에 추가
- **영향**: 전체 `notes/5-compliance/`
- **라벨**: `good-first-issue`, `style`, `terminology`

#### 13. 금액 표기 통일

- **규칙**: `100만원` (줄글) vs `1,000,000원` (표·숫자 강조) 중 택 1
- **액션**: `CONTRIBUTING.md` Style Guide 규정 + 기존 문서 통일
- **라벨**: `good-first-issue`, `style`

#### 14. en/ 영문 에디션 어색한 구문 다듬기

- **액션**: `en/` 폴더 내 1~2개 파일 native speaker 리뷰
- **추천 시작**: `en/day_01.md`
- **라벨**: `good-first-issue`, `translation`, `en-edition`

#### 15. 새 용어 5개 glossary 추가

- **액션**: `notes/glossary.md` 에 다음 5개 용어 추가
  - Restaking, MEV, LST (Liquid Staking Token), AVS (Actively Validated Service), ZK-KYC
- **각 용어**: 정의 + 예시 1개 + 관련 위험 1줄
- **라벨**: `good-first-issue`, `glossary`

---

## 기여 방법

1. 위 Issue 중 1개 선택 → GitHub Issue에 `/assign @me` 또는 "I'll take this" 댓글
2. Fork → 브랜치 생성 (`fix/issue-XX-short-desc`) → PR 제출
3. PR description에 `Closes #XXX` 표기
4. Maintainer 리뷰·승인 (1주일 내)
5. 머지 후 Hall of Fame 카운트 +1

처음이시라면 `CONTRIBUTING.md` 먼저 읽어주세요.

---

## 학습 경로 (기여자 온보딩)

- **1주차**: README · CONTRIBUTING · GOVERNANCE 읽기
- **2주차**: `curriculum/60-days/day_01.md` 훑기 + 관심 분야 select
- **3주차**: 첫 Good First Issue 시도 (위 #1·#5·#11·#13 중 택 1 추천)
- **4주차+**: 분야별 심화 기여

---

## 5+ PR 후 Trusted Contributor

- README Hall of Fame 등재
- 특정 폴더 review 권한 부여
- 공식 Contributor 표기 (LinkedIn·이력서 활용 가능)
- 분기 Contributor 미팅 초대 (온라인)

---

## Issue 라벨 체계

| 라벨 | 설명 |
|---|---|
| `good-first-issue` | 처음 기여 추천 |
| `fact-check` | 사실 확인 필요 |
| `link-rot` | 깨진 URL 수정 |
| `mermaid` | Mermaid 다이어그램 |
| `chart` | SVG/차트 |
| `translation` | 번역 |
| `style` | 스타일·용어 통일 |
| `glossary` | 용어집 |
| `en-edition` | 영문판 |
| `legal` | 법률 정확성 |
| `stats` | 통계·숫자 |
| `research` | 추가 조사 필요 |

---

## Maintainer 주석

이 파일의 15개 Issue가 모두 해결되면, 다음 배치 15개를 여기에 추가할 예정.
새 Issue 제안은 Discussion 또는 별도 Issue로.
