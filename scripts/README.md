# scripts/ — 빌드·파생물 생성 도구

지식 그래프(SSOT)에서 **파생물을 생성**하는 도구를 둡니다. 수집기는 `ingest/`, 검증기는 `quality/` 에 있습니다.

---

## 도구

### `build_crosswalk.py` — 관할 크로스워크 생성

추상 의무(`OBL`) 하나에 걸린 각국 조문(`PROV`)의 `IMPOSES` 한정자를 모아 관할 비교표를 만듭니다.
손으로 유지하던 비교표를 **질의 결과로 대체**하는 것이 목적입니다.

```bash
python scripts/build_crosswalk.py                              # 전체 의무 → kb/derived/crosswalk/
python scripts/build_crosswalk.py --stdout                     # 파일 대신 표준출력
python scripts/build_crosswalk.py --obl OBL:x-travel-rule-originator
python scripts/build_crosswalk.py --stdout --as-of 2020-01-01   # 시점 질의
```

`--as-of` 는 엣지의 `valid_from`/`valid_to` 를 기준으로 해당 시점에 유효했던 관계만 반환합니다.
2020-01-01 로 돌리면 한국 트래블룰 조문이 정확히 빠집니다(시행 2022-03-25).

설계 근거 → [`docs/ontology/01-semantic-layer.md`](../docs/ontology/01-semantic-layer.md) §2.1

---

## 다른 디렉터리의 도구

이 저장소는 **역할별로 도구를 분리**합니다. 찾는 것이 여기 없으면 아래를 보세요.

| 도구 | 위치 | 용도 |
|---|---|---|
| `validate_kb.py` | [`quality/`](../quality/README.md) | 지식 그래프 무결성 검증 (불변식 강제 · CI 차단) |
| `validate_links.py` | [`quality/`](../quality/README.md) | 산문 내부 상대 링크 검증 |
| `validate_mermaid.py` | [`quality/`](../quality/README.md) | Mermaid 블록 mmdc 컴파일 검증 |
| `check_external_urls.py` | [`quality/`](../quality/README.md) | 외부 URL 생존 확인 |
| `regulatory_rss.py` | [`ingest/legacy/`](../ingest/legacy/README.md) | ⚠️ 전환 대상 구 주간 워처 |
| `generator.py` | [`print/`](../print/README.md) | A4·모바일 HTML 패킷 생성 |
| `generate.py`, `fix_urls.py` 등 | `charts/` | 차트·다이어그램 생성 |

> 검증 스크립트는 2026-07-30 구조 개편에서 `charts/` → `quality/` 로 이동했습니다.
> `validate_mermaid.py` 는 mmdc 툴체인·설정·캐시를 여전히 `charts/` 에서 참조합니다.

---

## 파생물 규율

`kb/derived/` 는 **생성물이며 직접 편집하지 않습니다.** CI 가 재생성 결과와 커밋된 내용을 대조하며,
불일치는 "누군가 생성물을 손으로 고쳤다"는 신호로 취급해 실패시킵니다 ([ADR-0003](../docs/adr/0003-file-ssot-defer-engine.md)).

빌드는 **재현 가능**해야 합니다 — 외부 네트워크 호출을 넣지 마세요. 필요한 데이터는 전부 저장소 안에 있어야 합니다.

```
git clone → build → 동일한 산출물
```

---

## 의존성

```bash
pip install -r quality/requirements.txt   # PyYAML, jsonschema
```
