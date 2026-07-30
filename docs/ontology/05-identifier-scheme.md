# 식별자 체계 (Identifier Scheme)

> **역할**: 노드·엣지·레코드의 전역 유일 식별 규칙 · **강제**: `quality/rules/id_rules.py`

---

## 1. 형식

```
{TYPE}:{namespace}-{slug}
```

정규식:
```regex
^[A-Z]{3,7}:[a-z0-9]{1,4}(-[a-z0-9][a-z0-9-]*)?$
```

| 부분 | 규칙 |
|---|---|
| `TYPE` | 대문자 3~7자. [`04-node-edge-spec.md §3`](04-node-edge-spec.md) 의 클래스 코드만 허용 |
| `namespace` | ISO 3166-1 alpha-2 소문자 / `eu` / `intl` / `x` |
| `slug` | 소문자·숫자·하이픈. 연속 하이픈 금지, 하이픈으로 시작·종료 금지 |

### 1.0 slug 생략 (JUR 전용)

관할 노드는 **namespace 자체가 식별자**이므로 slug 를 생략한다 — `JUR:kr`, `JUR:eu`.
그 외 모든 클래스는 slug 가 필수이며, 누락 시 validator 규칙 **ID-9** 가 차단한다.
허용 목록은 `kb/schema/ontology.yaml` 의 `slug_optional_classes` 에서 관리한다.

> 이 예외는 최초 규격에 누락되어 있었고, 씨앗 노드 검증에서 `JUR:kr` 이
> 자기 규격을 위반하며 드러났다. 정규식을 완화하고 클래스별 강제를 validator 로
> 옮긴 것이 수정 내용이다.

### 1.1 namespace 선택

| 값 | 사용 | 예 |
|---|---|---|
| ISO 국가코드 | 특정 국가 귀속 | `kr`, `us`, `jp`, `sg`, `hk`, `ae`, `kp` |
| `eu` | EU 차원 | `REG:eu-mica` |
| `intl` | 국제기구·다자기준 | `ORG:intl-fatf` |
| `x` | 무국적·기술·추상 | `TEC:x-chain-hopping`, `OBL:x-travel-rule-originator` |

**판단 기준**: "이것이 특정 관할의 산물인가?" 아니면 `x`.
위협행위자의 namespace 는 **귀속된 국가**를 쓴다 (`ACT:kp-lazarus`) — 귀속이 미확정이면 `x`.

---

## 2. slug 작성 규칙

| 대상 | 규칙 | 예 |
|---|---|---|
| 법률 | 통용 약칭의 로마자 | `REG:kr-tfia`, `REG:eu-mica` |
| 조문 | `{법률slug}-{조문경로}` | `PROV:kr-tfia-art5-3`, `PROV:us-31cfr-1010-410f` |
| 기관 | 통용 약어 | `ORG:kr-kofiu`, `ORG:us-fincen` |
| 사업자·벤더 | 브랜드명 | `VASP:kr-upbit`, `VEND:us-chainalysis` |
| 집행조치 | `{대상}-{연도}` | `ENF:us-binance-2023` |
| 사고 | `{대상}-{연도}` 또는 `{사건명}-{연도}` | `INC:x-bybit-2025` |
| 사건(EVT) | `{주체}-{사건}-{연도}` | `EVT:eu-mica-casp-application-2024` |
| 기법 | 통용 영문 기법명 | `TEC:x-peel-chain` |

### 2.1 조문 경로 표기

| 관할 | 원 표기 | slug |
|---|---|---|
| 한국 | 제5조의3 제1항 | `art5-3-p1` |
| 한국 | 시행령 제10조의10 | `sd-art10-10` |
| 미국 | 31 CFR §1010.410(f) | `31cfr-1010-410f` |
| EU | Regulation Art. 14(2) | `art14-2` |
| 일본 | 第63条の11 | `art63-11` |

한글 조문 번호의 "의"는 하이픈으로 (`제5조의3` → `art5-3`). 항·호는 `p`(項)·`i`(號) 접두어.

---

## 3. 불변성 (Immutability)

**발급된 ID 는 어떤 경우에도 변경하지 않는다.** 외부 문서·산문·과거 브리프가 ID 를 참조하고 있기 때문이다.

| 상황 | 처리 |
|---|---|
| 오타로 만든 ID | 새 ID 생성 + 구 ID `status: merged` + `MERGED_INTO` 엣지 |
| 중복 노드 발견 | 정본 하나 선택, 나머지 `MERGED_INTO` |
| 대상이 개명 (기관·기업) | ID 유지, `label` 만 갱신, 구 명칭은 `aliases` 로 |
| 대상이 소멸 | ID 유지, `status: deprecated`, `valid_to` 설정 |
| 클래스 오분류 | 새 ID(올바른 TYPE) + `MERGED_INTO` |

```yaml
# 폐기된 노드도 파일로 영구 보존
id: "VEND:us-typo-chainalisys"
type: "VEND"
status: "merged"
merged_into: "VEND:us-chainalysis"
merged_at: "2026-08-01"
merge_reason: "철자 오류로 생성된 중복"
```

---

## 4. 순번 기반 ID (L2/L3)

`FACT`, `STATE`, `EVT`(일부), `SIG`, `TASK`, `RUN`, `ITEM` 은 대량 생성되므로 순번을 쓴다.

| 클래스 | 형식 | 예 |
|---|---|---|
| `FACT` | `FACT:{7자리}` | `FACT:0001842` |
| `STATE` | `STATE:{5자리}` | `STATE:00412` |
| `SIG` | `SIG:{YYYYMMDD}-{4자리}` | `SIG:20260730-0113` |
| `TASK` | `TASK:{YYYYMMDD}-{4자리}` | `TASK:20260730-0042` |
| `RUN` | `RUN:{YYYYMMDD}-{feed_slug}` | `RUN:20260730-us-fincen-news` |
| `ITEM` | `ITEM:{YYYYMMDD}-{feed_slug}-{5자리}` | `ITEM:20260730-us-fincen-news-00007` |

순번은 `kb/.counters.json` 에서 중앙 발급하며, 동시 발급 충돌은 빌드 시 검출한다.

**`EVT` 는 예외** — 역사적으로 중요한 사건은 사람이 읽는 slug 를 쓴다 (`EVT:jp-mtgox-collapse-2014`). 자동 생성 사건만 순번.

---

## 5. 엣지 ID

엣지는 `(from, predicate, to, valid_from)` 4튜플로 자연 식별되므로 별도 ID 를 부여하지 않는다. 참조가 필요한 경우에만 결정적 해시를 쓴다.

```
E:{sha256(from|predicate|to|valid_from)[:12]}
```

---

## 6. 외부 식별자 매핑

내부 ID 와 별개로 외부 표준 식별자를 `external_ids` 에 보관한다. 상호운용과 검증에 쓴다.

```yaml
external_ids:
  celex: "32023R1114"              # EU 법령
  law_go_kr: "001234"              # 국가법령정보센터 법령ID
  ecfr: "31 CFR 1010.410"
  lei: "..."                       # 법인 식별
  cik: "..."                       # SEC
  corp_reg_kr: "..."               # 법인등록번호
  wikidata: "Q..."
  mitre_attack: "T1234"            # 기법 매핑 (해당 시)
```

`external_ids` 는 **중복 검출의 1차 수단**이다. 같은 CELEX 번호를 가진 노드가 둘이면 병합 대상이다.

---

## 7. 검증 규칙

| # | 규칙 |
|---|---|
| ID-1 | 정규식 일치 |
| ID-2 | `TYPE` 이 온톨로지에 정의된 클래스 |
| ID-3 | 전역 유일 (파일 전체 스캔) |
| ID-4 | `namespace` 가 허용 목록에 존재 |
| ID-5 | 파일 경로가 ID 와 정합 (`kb/entities/{복수형}/{namespace}-{slug}.yaml`) |
| ID-6 | `MERGED_INTO` 대상이 실존하고 `status != merged` (병합 체인 금지) |
| ID-7 | 참조된 모든 ID 가 실존 (댕글링 참조 0) |
| ID-8 | 동일 `external_ids` 값을 가진 노드가 2개 이상이면 경고 |
