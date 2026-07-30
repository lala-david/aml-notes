# 검증 규칙

## 금칙어 목록 (I-12)

`quality/rules/forbidden_terms.local.txt` 는 **gitignore 대상**이며 저장소에 커밋되지 않는다.
한 줄에 하나의 금칙 문자열을 적는다. `#` 로 시작하는 줄은 주석.

```
# 예시 형식 — 실제 파일은 커밋되지 않음
<조직명 한글>
<조직명 영문>
<제품명>
```

파일이 없으면 검증기는 조직명 검사를 **생략하고 경고**를 남긴다. 조직 고유명 없이도 다음 일반 패턴은 항상 검사한다.

- `진입 전략`, `경쟁 우위`, `사업 계획`, `수익 모델`
- `우리 회사`, `우리 서비스`, `우리 제품`
- `go-to-market`

### 왜 목록을 커밋하지 않는가

금칙어 목록 자체가 커밋되면 "무엇을 숨기려 했는지"가 공개 이력에 남는다. 목록은 로컬과 CI 시크릿에만 둔다.

CI 에서는 시크릿을 파일로 풀어놓고 검증기를 실행한다.

```yaml
- name: 금칙어 목록 복원
  run: printf '%s\n' "${{ secrets.FORBIDDEN_TERMS }}" > quality/rules/forbidden_terms.local.txt
- name: 검증
  run: python quality/validate_kb.py
```

## 규칙 출처

| 규칙군 | 정의 문서 |
|---|---|
| I-1 ~ I-12 | [`../../docs/ontology/04-node-edge-spec.md §8`](../../docs/ontology/04-node-edge-spec.md) |
| ID-1 ~ ID-8 | [`../../docs/ontology/05-identifier-scheme.md §7`](../../docs/ontology/05-identifier-scheme.md) |
| T-1 ~ T-7 | [`../../docs/ontology/06-timeline-model.md §8`](../../docs/ontology/06-timeline-model.md) |
| Q-1 ~ Q-8 | [`../../docs/governance/01-data-quality.md §4`](../../docs/governance/01-data-quality.md) |
| ONT-1 ~ ONT-3 | 술어 정의역·치역 — `kb/schema/ontology.yaml` 의 `predicates` |
