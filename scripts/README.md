# Scripts — 자동화 도구

이 폴더는 저장소 유지보수용 자동화 스크립트를 담습니다.

## regulatory_rss.py

주요 AML 규제기관의 RSS 피드를 수집해 최근 변화를 탐지합니다.

### 로컬 실행

```bash
pip install -r scripts/requirements.txt
python scripts/regulatory_rss.py --days 7 --verbose
```

### 플래그

- `--days N` — 최근 N 일 이내 항목만 (기본 7)
- `--output-dir DIR` — 출력 디렉터리 (기본 현재 디렉터리)
- `--verbose`, `-v` — 피드별 진행 상황 stderr 출력

### 출력

- `regulatory-changes.json` — 기계 판독용 전체 데이터
- `regulatory-changes.md` — GitHub Issue 붙이기 용 사람 친화 리포트

### Exit code

- `0` — 신규 항목 없음
- `1` — 신규 항목 있음 (CI 에서 Issue 생성 트리거)
- `2` — 의존성 누락 등 실행 오류

### 추적 피드

국제 (FATF·BIS) · 미국 (SEC·FinCEN·OFAC·DOJ·CFTC) · EU (ESMA) · 아시아 (MAS·SFC HK) · 업계 (Chainalysis·Elliptic·TRM). 한국 규제기관 (FSC·KoFIU·FSS) 은 공식 RSS 미제공 → 별도 스크레이핑 작업 예정.

### CI 자동화

`.github/workflows/regulatory-watch.yml` 참조. 매주 월요일 UTC 00:00 (KST 09:00) 자동 실행.

---

## 기타 스크립트

이미 저장소에 있는 검증 도구는 `charts/` 폴더에 있습니다:

- `charts/validate_mermaid.py` — Mermaid 문법 검증
- `charts/validate_links.py` — 내부 링크 검증
- `charts/check_external_urls.py` — 외부 URL 400/404 탐지
- `charts/fix_urls.py` — 알려진 깨진 URL 일괄 교체

이들은 `.github/workflows/validate.yml` 에서 PR 시 자동 실행됩니다.
