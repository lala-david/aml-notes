# Changelog

> 본 저장소의 주요 변경 이력. [Keep a Changelog](https://keepachangelog.com/) 형식을 따르며, 날짜는 KST 기준입니다.

## [1.0.0] — 2026-07-30

**성격 전환: 학습 교재 → 질의 가능한 지식베이스**

산문 아래에 시점 질의가 되는 지식 그래프를 깔았습니다. 산문은 폐기하지 않고 그래프의 한 가지 투영으로 재정의했습니다.

### Added — 온톨로지

- `docs/ontology/` — **3계층 설계** (L1 의미 / L2 동적 / L3 운동), 33 클래스 · 50+ 술어
  - `04-node-edge-spec.md` — 노드·엣지 규범적 정의. 프로퍼티 그래프 채택
  - `02-dynamic-layer.md` — **이중시간(bitemporal)** 모델. 유효시간 + 기록시간
  - `06-timeline-model.md` — 3트랙 역사 타임라인 + `CAUSED` 인과 엣지 + 국면(ERA)
  - `05-identifier-scheme.md` — 식별자 불변성·병합 규칙
- `kb/schema/ontology.yaml` — 기계판 온톨로지 (클래스·술어·불변식·신선도 SLA)
- `kb/schema/node.schema.json` · `edge.schema.json` — JSON Schema
- `docs/adr/` — 아키텍처 결정 기록 3건 (프로퍼티 그래프 / 이중시간 / 파일 SSOT)

### Added — 거버넌스·품질

- `docs/governance/` — 품질 6차원 · 출처 등급 T1~T5 · 확신도 A~D · 검증 워크플로
- `quality/validate_kb.py` — 불변식 강제 검증기. 차단 위반 시 CI 차단
- `quality/README.md` — 검증 도구 사용법 · 미검증 부채 상한 5%
- `kb/facts/contradictions.jsonl` — **상충 레지스트리.** 출처가 엇갈리면 지우지 않고 기록
- `.github/workflows/kb-validate.yml` — 그래프 검증 + 파생물 재현성 확인

### Added — 수집

- `docs/ingestion/` — 소스 등재 기준 · 일일 파이프라인 운영 설계
- `ingest/config/sources.yaml` — **실측 검증된 소스 레지스트리.** 88개 후보 중 51개 OK 확인,
  가동 22개. 추측 URL 미등재, 미검증은 `enabled: false`

### Added — 도구

- `scripts/build_crosswalk.py` — 관할 비교표 생성 + `--as-of` 시점 질의
- `kb/derived/crosswalk/` — 생성된 관할 비교표

### Changed — 디렉터리 구조 개편

| 이동 | 이유 |
|---|---|
| `charts/validate_*.py`, `check_external_urls.py` → `quality/` | 검증기를 검증 계층으로 |
| `scripts/regulatory_rss.py` → `ingest/legacy/` | 수집기를 수집 계층으로. 전환 대상임을 위치로 표시 |
| `meta/regulatory-watch.md` → `intel/watchlist/` | 규제 추적은 분석 산출물 |
| `meta/outreach/`, `meta/submissions/`, 프로젝트 운영 문서 → `_private/` | 지식베이스 구성물이 아니며 공개 대상 아님 |

- `meta/` 디렉터리 제거. `scripts/` 를 **파생물 생성 전용**으로 재정의
- `README.md` 전면 개편 — 지식베이스 정체성 반영
- `.github/workflows/validate.yml`·`regulatory-watch.yml` 경로 갱신
- `CONTRIBUTING.md`·`deep/README.md`·이슈 템플릿 경로 참조 일괄 정정
- `quality/validate_mermaid.py` — `charts/` 툴체인 참조로 수정 (이동에 따른 파손 방지)
- `quality/validate_links.py` — `_research/`·`_private/` 검증 제외

### Fixed

- **식별자 규격 버그** — `JUR:kr` 이 자기 정규식(`namespace-slug` 필수)을 위반했다.
  씨앗 노드 검증에서 드러남. 정규식을 완화하고 클래스별 slug 강제를 validator 로 이관 (ID-9)
- **가상자산 트래블룰의 FATF 근거 정정** — R.16 Explanatory Note §54 원문 확인 결과,
  FATF 는 VASP 를 R.16 **직접 적용 대상에서 제외**했다. 근거는 INR.15 §7(b).
  R.16 을 직결 근거로 서술한 기존 내용은 정정 대상 (`CTR:00002`)
- **OFSI Consolidated List 폐기 반영** — 2026-01-28 철회. 구 워처가 갱신되지 않는 파일을
  계속 수집하고 있었다. UK Sanctions List 로 교체

### Known issues

- KB 노드 17개 — 구축 초기. 목표 1,200
- `CTR:00001` 미해소 — 특금법 개정 법률 제21358호의 공포일·시행일 상충 (재검증 진행 중)
- 개정 법률의 생애주기 모델링 미결 — 원법 속성 vs 독립 `REG` + `AMENDS`. ADR 필요

---

## [0.6.0] — 2026-04-20

**저장소 메타 정비**

### Added
- `LICENSE` — CC BY 4.0 (문서) + MIT (코드 샘플) 이중 라이선스 명시
- `CONTRIBUTING.md` — 기여 절차, PR 체크리스트, 스타일 가이드
- `CHANGELOG.md` — 본 파일
- `.github/ISSUE_TEMPLATE/` — 오류 보고·토픽 제안·링크 깨짐 3종 템플릿
- `notes/1-foundations/README.md` · `notes/3-crypto-aml/README.md` · `notes/4-technology/README.md` · `notes/5-compliance/README.md` · `notes/6-cases/README.md` · `notes/7-vendors/README.md` — 각 서브폴더에 "누가 먼저 읽을지 + 순서 + 핵심 출구" 가이드
- `curriculum/README.md` · `curriculum/progress.md` — **🗺 오늘의 지도** Mermaid 섹션을 일일 파일 구조에 공식 반영

### Changed
- `notes/README.md` — 서브폴더 파일 수 표기에 `+ README` 추가

---

## [0.5.0] — 2026-04-19

**시각 자료·검증 인프라 보강**

### Fixed
- `projects/04-ofac-screener/README.md` — Mermaid 파이프 레이블 `O(1)` 괄호가 mmdc 파서 오류 → `in-memory lookup`으로 교체
- seaborn 차트 PNG 한글 폰트 깨짐 (406 tofu warnings) — `sns.set_style("ticks")`가 `font.family`를 덮어써서 발생. Malgun Gothic을 스타일 적용 **후**에 설정하도록 순서 변경
- 국기 이모지(🇰🇷 🇺🇸 🇪🇺 🌍) Malgun Gothic에서 렌더 실패 → `KR`/`US`/`EU`/`FATF` 텍스트 뱃지 박스로 대체
- 외부 URL 14개 404/리다이렉트 — `charts/fix_urls.py` 추가, 길이 기준 내림차순 치환으로 prefix 오염 방지 (`/` 가 `/news/`를 망가뜨리던 버그)
- `charts/validate_links.py` — `node_modules`·`mermaid-cache`를 경로 세트 매칭으로 제외

### Added
- `charts/validate_mermaid.py` — 114개 Mermaid 블록 mmdc 컴파일 일괄 검증 (현재 114/114 PASS)
- `charts/validate_links.py` — 내부 상대 링크 검증 (378개 PASS, 0 broken)
- `charts/check_external_urls.py` — 외부 URL HEAD 체크 + 403/405 시 GET 폴백
- `charts/fix_urls.py` — 알려진 깨진 URL 일괄 교체 스크립트

### Changed
- `README.md` — 시각 자료·검증 인프라 섹션 추가, 뱃지 11개 재배치

---

## [0.4.0] — 2026-04-18

**Visual layer Phase 2 — 차트·아키텍처·프린트 사전 렌더**

### Added
- seaborn 차트 3개 추가 (총 8개)
- 6개 프로젝트에 아키텍처 Mermaid 다이어그램 각 1개 이상
- `print/generator.py` — mmdc subprocess 호출로 모든 Mermaid를 SVG로 사전 렌더 → 오프라인 프린트에서도 렌더 보장
- SHA1 해시 기반 mmdc 출력 캐시

### Changed
- `print/assets/print.css` — `.mermaid-wrap` · `.article-body` 클래스 추가, 페이지 나눔 규칙 정비

---

## [0.3.0] — 2026-04-17

**Visual layer Phase 1 — Mermaid + seaborn 도입**

### Added
- `charts/` — seaborn 기반 차트 생성 파이프라인 (`generate.py` + 5개 초기 차트)
- `charts/mermaid_config.json` — Pretendard 폰트 + 브랜드 액센트 `#1a2e4a` 테마
- 모든 notes (`notes/**/*.md`) + 60일 day 파일에 Mermaid 다이어그램 삽입
- `charts/inject_day_diagrams.py` — 60개 고유 **🗺 오늘의 지도** 다이어그램을 `<!-- MAP-START --> ... <!-- MAP-END -->` 마커로 삽입

---

## [0.2.0] — 2026-04-16

**A4 프린트 패킷 생성기 도입**

### Added
- `print/` — 60일 전체를 A4 최적화 HTML 패킷으로 생성
- `print/generator.py` — Task Sheet + 연결된 읽기 노트를 한 파일에 결합
- `print/assets/print.css` — A4 210×297mm, 18mm 여백, Pretendard + IBM Plex Mono
- `print/index.html` — 60개 패킷 목차

---

## [0.1.0] — 2026-04-14~15

**Prose Revamp — 치트시트에서 산문 교재로 전면 개편**

### Changed
- 22개 topic 노트(`notes/**/*.md`) · 60개 day 파일 · 6개 프로젝트 · 4개 deep 문서를 **산문 교재 스타일**로 재작성
- 모든 노트에 도입 blurb + TL;DR + 본문 + 실무 포인트 + 더 읽을거리 구조 적용
- 용어 첫 등장 시 한국어 괄호 병기 원칙 적용
- `glossary.md` — 실무 예시 보강

### Added
- `deep/` — 학술 논문 · 산업 리포트 · 컨퍼런스 · 외부 링크 4개 심화 문서

---

## [0.0.2] — 2026-04-01

**저장소 구조 재정비**

### Changed
- 11개 폴더 → 4개(`notes/ curriculum/ projects/ deep/`)로 축소
- README에 Mermaid 인덱스 다이어그램 추가

---

## [0.0.1] — 2026-03

**초기 커밋**

### Added
- 60일 커리큘럼 스켈레톤
- 토픽별 초기 노트
- 8개 자동화 미니 프로젝트 골격

---

[0.6.0]: https://github.com/lala-david/aml-notes/releases/tag/v0.6.0
[0.5.0]: https://github.com/lala-david/aml-notes/releases/tag/v0.5.0
[0.4.0]: https://github.com/lala-david/aml-notes/releases/tag/v0.4.0
[0.3.0]: https://github.com/lala-david/aml-notes/releases/tag/v0.3.0
[0.2.0]: https://github.com/lala-david/aml-notes/releases/tag/v0.2.0
[0.1.0]: https://github.com/lala-david/aml-notes/releases/tag/v0.1.0
