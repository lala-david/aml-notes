# 레거시 수집기

> ⚠️ **전환 대상**. 새 파이프라인이 안정화되면 제거한다.

## `regulatory_rss.py`

주간 RSS 집계 → GitHub 이슈 생성. 신 파이프라인([`docs/ingestion/02-daily-pipeline.md`](../../docs/ingestion/02-daily-pipeline.md))의 원형이다.

| 항목 | 현행 (레거시) | 전환 후 |
|---|---|---|
| 소스 정의 | 코드 내 `FEEDS` 딕셔너리 (하드코딩) | [`ingest/config/sources.yaml`](../config/sources.yaml) 선언적 |
| 소스 검증 | 없음 (추측 URL 포함) | 실측 `probe` 필수, 미검증은 `enabled: false` |
| 관련성 판정 | 키워드 단순 매칭 | 관련성 점수 + KB 노드 매칭 |
| 실행 주기 | 주 1회 (월요일) | 일 1회 + 제재 명단 2회 |
| 결과 | 이슈 생성 후 종료 | SIGNAL → TASK → L2 승격 |
| 보존 | artifact 90일 | `data/` 영구 + 계보 기록 |

### 알려진 문제

레거시 `FEEDS` 에는 **실측되지 않은 URL**이 섞여 있다. 2026-07-30 실측 결과 다음이 확인되었다.

| 소스 | 실측 결과 |
|---|---|
| FinCEN, OFAC, DOJ, FATF | 403 / timeout — 조용히 0건 수집 |
| `esma.europa.eu/news.rss` | 현행 경로는 `/rss.xml` |
| OFSI Consolidated List | **2026-01-28 철회** — 갱신되지 않는 파일을 계속 받고 있었음 |

즉 레거시 워처는 **일부 소스가 죽은 것을 알려주지 않는다**. 신 파이프라인이 침묵 탐지(`feed_silence`)를 넣은 이유다.

### 전환 절차

1. 신 파이프라인 구현 후 **병행 운영**
2. 레거시가 잡던 항목을 신 파이프라인이 전부 재현하는지 확인
3. 확인 후 이 디렉터리와 `.github/workflows/regulatory-watch.yml` 제거

### 실행

```bash
pip install -r ingest/legacy/requirements.txt
python ingest/legacy/regulatory_rss.py --days 7 --verbose
```
