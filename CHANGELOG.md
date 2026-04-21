# Changelog

> 본 저장소의 주요 변경 이력. [Keep a Changelog](https://keepachangelog.com/) 형식을 따르며, 날짜는 KST 기준입니다.

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
