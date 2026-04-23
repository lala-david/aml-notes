# Regulatory Watch — 규제 변화 추적 시스템

> AML·가상자산 규제는 분기별로 바뀐다. 이 저장소는 **자동·반자동 추적 체계**로 stale 콘텐츠를 방지한다. 마지막 갱신: 2026-04-23.

## 배포 상태 (2026-04-23 기준)

- [x] **`scripts/regulatory_rss.py`** — 13개 피드 수집, 키워드 필터, JSON+Markdown 출력
- [x] **GitHub Actions 자동화** — `.github/workflows/regulatory-watch.yml`, 매주 월요일 UTC 00:00 (KST 09:00) 실행
- [x] **자동 Issue 생성** — 변화 감지 시 `regulatory-update` · `automated` 라벨로 Issue
- [x] **수동 실행 지원** — `workflow_dispatch` 트리거로 on-demand 실행
- [x] **산출물 보관** — GitHub Actions artifacts 90 일 (`regulatory-changes.json`, `.md`)
- [x] **검증 CI** — `.github/workflows/validate.yml` 로 링크·Mermaid PR 자동 검증
- [ ] **한국 기관 RSS** — FSC/KoFIU/FSS 공식 RSS 미제공 → 웹 스크레이핑 별도 이슈

## TL;DR

- **추적 대상**: FATF · 한국 (FSC·KoFIU·FSS·DAXA) · 미국 (FinCEN·OFAC·SEC) · EU (AMLA·ESMA) · 아시아 (MAS·VARA·FSA·SFC)
- **추적 방법**: RSS·email subscription·웹 모니터링·분기 수동 리뷰
- **반영 주기**: Major 변화 1주 내 / Minor 변화 분기별
- **검증**: 모든 콘텐츠는 1차 자료 링크 보유 → 깨진 링크는 `validate_links.py` 자동 탐지

---

## 1. 추적 채널 매트릭스

### 1.1 한국 채널 (필수 일일 모니터)

| 기관 | 채널 | 주기 | URL |
|---|---|---|---|
| FSC (금융위) | 보도자료 | 일별 | https://www.fsc.go.kr/no010101 |
| FSC | 정책 발표 | 주별 | https://www.fsc.go.kr/no010102 |
| KoFIU | 보도자료 | 주별 | https://www.kofiu.go.kr/kor/notice/news.do |
| FSS (금감원) | 보도자료 | 일별 | https://www.fss.or.kr/fss/bbs/B0000188/list.do |
| DAXA | 공식 발표 | 부정기 | https://www.daxa.or.kr/ |
| 법제처 | 법령 개정 알림 | 주별 | https://www.law.go.kr/ |

### 1.2 글로벌 채널 (주별 모니터)

| 기관 | 채널 | URL |
|---|---|---|
| FATF | News·Reports | https://www.fatf-gafi.org/en/publications.html |
| FATF | Mutual Evaluation | https://www.fatf-gafi.org/en/topics/mutual-evaluations.html |
| FinCEN | News Releases | https://www.fincen.gov/news/news-releases |
| OFAC | Recent Actions | https://ofac.treasury.gov/recent-actions |
| SEC | Press Releases | https://www.sec.gov/news/pressreleases |
| EU AMLA | News | https://amla.europa.eu/news |
| MAS (Singapore) | Media Room | https://www.mas.gov.sg/news |
| VARA (UAE) | News | https://www.vara.ae/en/news |
| FSA (Japan) | Press Releases | https://www.fsa.go.jp/en/news/index.html |
| SFC (Hong Kong) | News | https://www.sfc.hk/en/News-and-announcements |

### 1.3 산업 채널 (월별)

| 채널 | 종류 |
|---|---|
| Chainalysis Blog | 사건·리포트 1차 분석 |
| TRM Labs Insights | 사건 신속 분석 |
| Elliptic Resources | EU 중심 리포트 |
| ACAMS Today | 자격 분야 트렌드 |
| Coin Center | 미국 정책·법원 분석 |

### 1.4 학술·연구 (분기)

- arXiv (cs.CR) "money laundering" "AML" filter
- Google Scholar Alerts: "blockchain" "AML" "KYT"
- IEEE/ACM Digital Library 새 논문

---

## 2. 자동 모니터링 인프라 (배포됨)

### 2.1 RSS aggregator — `scripts/regulatory_rss.py`

배포 상태: **운영 중** · 13 개 피드 수집 · 키워드 필터 · 에러 격리 (피드 하나 다운 ≠ 전체 실패).

수집 대상:

| 권역 | 피드 |
|---|---|
| 국제 | FATF, BIS |
| 미국 | SEC Press, FinCEN News, OFAC Recent Actions, DOJ News, CFTC Press |
| EU | ESMA News |
| 아시아 | MAS News, HK SFC News |
| 업계 | Chainalysis Blog, Elliptic Blog, TRM Labs Blog |

> 한국 기관 (FSC/KoFIU/FSS) 은 공식 RSS 미제공 → 추후 HTML 스크레이핑 추가 예정.

실행:

```bash
pip install -r scripts/requirements.txt
python scripts/regulatory_rss.py --days 7 --verbose
# → regulatory-changes.json + regulatory-changes.md 생성
# → exit code 1 이면 신규 항목 있음 (CI 에서 Issue 생성)
```

자세한 사용법은 [`scripts/README.md`](../scripts/README.md) 참조.

### 2.2 GitHub Actions — `.github/workflows/regulatory-watch.yml`

배포 상태: **운영 중** · 매주 월요일 UTC 00:00 (KST 09:00) 자동 실행.

잡 흐름:

1. `actions/checkout@v4` · `actions/setup-python@v5` (3.11, pip 캐시)
2. `pip install -r scripts/requirements.txt`
3. `python scripts/regulatory_rss.py --days 7 --verbose` → 산출물 2 개 생성
4. **신규 항목 있으면** `peter-evans/create-issue-from-file@v5` 로 Issue 자동 생성 (`regulatory-update` · `automated` 라벨)
5. `actions/upload-artifact@v4` 로 JSON+MD 90 일 보관

수동 실행: GitHub UI → Actions → Regulatory Watch → `Run workflow`.

### 2.3 검증 CI — `.github/workflows/validate.yml`

배포 상태: **운영 중** · PR 마다 자동 검증.

- **PR / push → main**: `validate_links.py` · `validate_mermaid.py` 실행 (빠른 피드백)
- **분기 스케줄 · 수동**: `check_external_urls.py` 도 추가 실행 (rate-limit · flaky 대응 `continue-on-error: true`)

---

## 3. 분기 리뷰 체크리스트

### Q별 표준 절차 (4시간 작업)

- [ ] **Step 1: RSS 수집 결과 검토** (`regulatory-changes.json`)
- [ ] **Step 2: 우선순위 분류**
  - **Critical**: 한국 특금법·이용자보호법 개정 / FATF 권고 개정 / OFAC 가상자산 관련 → 1주 내 반영
  - **Major**: 미국·EU·아시아 주요 규제 변화 / 대형 enforcement 사건 → 1개월 내 반영
  - **Minor**: 가이드라인·FAQ 갱신·통계 → 다음 분기 리뷰
- [ ] **Step 3: 영향 받는 파일 식별**
  - `grep -r` 키워드 검색
  - CHANGELOG 참조
- [ ] **Step 4: 콘텐츠 업데이트**
  - 1차 자료 링크 갱신
  - 날짜·금액·조항 정확성 검증
  - "마지막 업데이트" 타임스탬프
- [ ] **Step 5: 자동 검증**
  - `python charts/validate_mermaid.py`
  - `python charts/validate_links.py`
  - `python charts/check_external_urls.py`
- [ ] **Step 6: CHANGELOG 추가**
- [ ] **Step 7: GitHub release tag** (분기별 v0.X.Y)

### 분기 일정 (KST)

- **Q1 (1~3월)**: 신년 규제 대응 (특금법·MiCA·FATF 연초 변경)
- **Q2 (4~6월)**: 중간 점검 (FATF Plenary 주로 6월)
- **Q3 (7~9월)**: 미국 정책 변화 추적 (대선 영향)
- **Q4 (10~12월)**: 연말 정리 + 다음해 예정 변화

---

## 4. Major 변화 알림 워크플로

새 Critical 변화 발견 시:

1. **GitHub Issue 생성** (`regulatory-update` 라벨)
2. **CHANGELOG 임시 추가** (Unreleased)
3. **24시간 내 1차 패치** (이슈 본문에 1차 자료 링크)
4. **1주일 내 정식 반영** (관련 파일 업데이트)
5. **Discussion 게시** (대형 변화 시 사용자 알림)

---

## 5. 외부 자료 링크 health check

자동:
```bash
python charts/check_external_urls.py
```

수동 (분기별):
- 깨진 URL 발견 시 → 신규 URL 검색 → `python charts/fix_urls.py` REPLACEMENTS dict 갱신 → 재실행

---

## 6. 추적 누락 시 신고

규제 변화를 발견했는데 교재에 미반영이면 [GitHub Issue 04-regulatory-update](https://github.com/lala-david/aml-notes/issues/new?template=04-regulatory-update.yml) 사용.
