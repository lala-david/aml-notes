/* eslint-disable */
// 🤖 자동 생성 — 직접 편집하지 마세요.
// 원본: kb/schema/{node,edge}.schema.json
// 재생성: npm run gen:types

/**
 * 지식베이스 노드 공통 스키마. 클래스별 확장 필드는 kb/schema/types/{TYPE}.schema.json 에서 allOf 로 결합한다. 규범적 정의는 docs/ontology/04-node-edge-spec.md.
 */
export type KBNode = KBNode1 & KBNode2 & KBNode3 & KBNode4 & KBNode5;
/**
 * {TYPE}:{namespace}-{slug} · 불변
 */
export type KBNode6 = string;
export type KBNode7 =
  | 'JUR'
  | 'ORG'
  | 'REG'
  | 'PROV'
  | 'OBL'
  | 'CTL'
  | 'CONCEPT'
  | 'RISK'
  | 'TYP'
  | 'TEC'
  | 'IND'
  | 'ASSET'
  | 'CHAIN'
  | 'PROTO'
  | 'VASP'
  | 'VEND'
  | 'CAP'
  | 'ACT'
  | 'SRC'
  | 'DOC'
  | 'ERA'
  | 'EVT'
  | 'ENF'
  | 'INC'
  | 'CASE'
  | 'ACTION'
  | 'FUNC'
  | 'ROLE'
  | 'FEED'
  | 'PROD';
/**
 * funnel 은 온톨로지 계층이 아니라 이를 채우는 인프라 (ADR-0004)
 */
export type KBNode8 = 'semantic' | 'dynamic' | 'kinetic' | 'funnel';
export type KBNode10 = string;
export type KBNode11 = string;
export type KBNode12 = string;
/**
 * 원어 명칭 (일본어·중국어 등)
 */
export type KBNode13 = string;
export type KBNode15 = string;
export type KBNode14 = KBNode15[];
/**
 * 2~3문장. 이 노드가 무엇인지.
 */
export type KBNode16 = string;
export type KBNode18 = string;
export type KBNode17 = KBNode18[];
export type KBNode19 = 'active' | 'deprecated' | 'merged' | 'disputed';
export type KBNode20 = string;
export type KBNode21 = string;
export type KBNode23 = string;
/**
 * @minItems 1
 */
export type KBNode24 = [KBNode25, ...KBNode25[]];
export type KBNode26 = string;
/**
 * A=T1/T2 원문 확인, B=T3 복수 일치, C=T4 단일, D=미검증
 */
export type KBNode27 = 'A' | 'B' | 'C' | 'D';
/**
 * 페이지·조문·섹션 등 문서 내 위치
 */
export type KBNode28 = string;
/**
 * 원어 원문 인용. 번역본 인용 금지.
 */
export type KBNode29 = string;
export type KBNode30 = string;
export type KBNode33 = string;
export type KBNode34 = string;
export type KBNode36 = KBNode37 | KBNode38;
export type KBNode37 = string;
export type KBNode38 = null;
export type KBNode39 = KBNode40 | KBNode41;
export type KBNode40 = string;
export type KBNode41 = null;
export type KBNode42 = string;
export type KBNode43 = KBNode25[];
export type KBNode31 = KBNode32[];
export type KBNode44 = string;
export type KBNode45 = string;
/**
 * 신선도 SLA 만료일. 초과 시 sla_expiry 신호 발생.
 */
export type KBNode46 = string;
/**
 * 판단 근거·주의사항. 사람이 읽는 메모.
 */
export type KBNode47 = string;

export interface KBNode1 {
  [k: string]: unknown;
}
/**
 * Funnel 클래스는 semantic 계층에 올 수 없다
 */
export interface KBNode2 {
  [k: string]: unknown;
}
/**
 * 운용 액션은 이행하는 의무를 명시해야 한다 (조문→의무→통제→액션 사슬)
 */
export interface KBNode3 {
  [k: string]: unknown;
}
/**
 * 에이전트 역할은 어떤 액션도 직접 실행할 수 없다
 */
export interface KBNode4 {
  [k: string]: unknown;
}
export interface KBNode5 {
  id: KBNode6;
  type: KBNode7;
  layer: KBNode8;
  label: KBNode9;
  aliases?: KBNode14;
  summary?: KBNode16;
  tags?: KBNode17;
  status?: KBNode19;
  merged_into?: KBNode20;
  merge_reason?: KBNode21;
  external_ids?: KBNode22;
  evidence?: KBNode24;
  edges?: KBNode31;
  created_at: KBNode44;
  updated_at: KBNode45;
  review_due?: KBNode46;
  curator_note?: KBNode47;
  [k: string]: unknown;
}
export interface KBNode9 {
  ko: KBNode10;
  en?: KBNode11;
  short?: KBNode12;
  orig?: KBNode13;
}
/**
 * celex, law_go_kr, ecfr, lei, cik, wikidata, mitre_attack 등
 */
export interface KBNode22 {
  [k: string]: KBNode23;
}
export interface KBNode25 {
  doc: KBNode26;
  confidence: KBNode27;
  locator?: KBNode28;
  quote?: KBNode29;
  retrieved?: KBNode30;
}
export interface KBNode32 {
  predicate: KBNode33;
  to: KBNode34;
  qualifiers?: KBNode35;
  valid_from?: KBNode36;
  valid_to?: KBNode39;
  recorded_at?: KBNode42;
  evidence?: KBNode43;
}
/**
 * 술어별 추가 속성. 허용 키는 ontology.yaml 의 predicates[].qualifiers 로 검증.
 */
export interface KBNode35 {}

/**
 * 지식베이스 엣지 스키마. 저장은 각 노드 파일의 edges[] 블록(출발점 기준)이며, 빌드 단계에서 이 형태로 정규화된다. 역엣지는 자동 생성한다.
 */
export type KBEdge = KBEdge1 & KBEdge2 & KBEdge3 & KBEdge4;
/**
 * sha256(from|predicate|to|valid_from)[:12] · 참조가 필요한 경우에만 발급
 */
export type KBEdge5 = string;
/**
 * ontology.yaml 의 predicates 에 정의된 것만 허용
 */
export type KBEdge6 = string;
export type KBEdge7 = string;
export type KBEdge8 = string;
export type KBEdge10 = KBEdge11 | KBEdge12;
export type KBEdge11 = number;
export type KBEdge12 = null;
export type KBEdge13 = string;
export type KBEdge14 = string;
export type KBEdge15 = 'full' | 'partial' | 'divergent';
export type KBEdge16 = 'sufficient' | 'partial';
export type KBEdge17 = 'strict' | 'broad' | 'narrow';
export type KBEdge18 = 'high' | 'medium' | 'low';
export type KBEdge19 = number;
export type KBEdge20 = number;
export type KBEdge21 = string;
export type KBEdge22 = string;
export type KBEdge23 = string;
export type KBEdge24 = string;
export type KBEdge25 = KBEdge26 | KBEdge27;
export type KBEdge26 = string;
export type KBEdge27 = null;
export type KBEdge28 = string;
export type KBEdge29 =
  | 'explicit_legislative'
  | 'official_statement'
  | 'contemporaneous_record'
  | 'expert_consensus'
  | 'forensic'
  | 'temporal_only';
export type KBEdge30 = string;
export type KBEdge31 = number;
export type KBEdge32 = 'A' | 'B' | 'C' | 'D';
export type KBEdge33 = number;
export type KBEdge34 = number;
export type KBEdge35 = string;
export type KBEdge36 = unknown;
export type KBEdge37 = unknown;
export type KBEdge38 = string;
export type KBEdge39 = KBEdge40 | KBEdge41;
export type KBEdge40 = string;
export type KBEdge41 = null;
export type KBEdge42 = string;
export type KBEdge43 = string;
export type KBEdge44 = string;
export type KBEdge46 = string;
export type KBEdge45 = KBEdge46[];
export type KBEdge47 = number;
export type KBEdge48 = string;
export type KBEdge49 = 'official-doc' | 'procurement' | 'press' | 'vendor-claim';
export type KBEdge50 = number;
export type KBEdge51 = string;
export type KBEdge52 = string;
export type KBEdge53 = string;
export type KBEdge54 = string;
/**
 * 이 관계가 성립하기 시작한 날. null = 시점 불명 또는 항구적.
 */
export type KBEdge55 = KBEdge56 | KBEdge57;
export type KBEdge56 = string;
export type KBEdge57 = null;
/**
 * null = 현재까지 유효
 */
export type KBEdge58 = KBEdge59 | KBEdge60;
export type KBEdge59 = string;
export type KBEdge60 = null;
/**
 * 우리가 이 관계를 기록한 날 (transaction time)
 */
export type KBEdge61 = string;
export type KBEdge62 = KBEdge63 | KBEdge64;
export type KBEdge63 = string;
export type KBEdge64 = null;
export type KBEdge65 = string;
/**
 * @minItems 1
 */
export type KBEdge66 = [KBEdge67, ...KBEdge67[]];
export type KBEdge68 = string;
export type KBEdge69 = 'A' | 'B' | 'C' | 'D';
export type KBEdge70 = string;
export type KBEdge71 = string;
export type KBEdge72 = string;
/**
 * 빌드가 생성한 역엣지·추론 엣지 여부. true 면 소스 파일에 저장하지 않는다.
 */
export type KBEdge73 = boolean;

/**
 * CAUSED 엣지는 근거 유형이 필수이며 temporal_only 를 허용하지 않는다
 */
export interface KBEdge1 {
  [k: string]: unknown;
}
/**
 * IMPOSES 에 임계값이 있으면 통화 단위가 필수
 */
export interface KBEdge2 {
  [k: string]: unknown;
}
/**
 * ATTRIBUTED_TO 는 귀속 주체와 근거가 필수
 */
export interface KBEdge3 {
  [k: string]: unknown;
}
export interface KBEdge4 {
  id?: KBEdge5;
  predicate: KBEdge6;
  from: KBEdge7;
  to: KBEdge8;
  qualifiers?: KBEdge9;
  valid_from?: KBEdge55;
  valid_to?: KBEdge58;
  recorded_at: KBEdge61;
  retracted_at?: KBEdge62;
  retraction_reason?: KBEdge65;
  evidence?: KBEdge66;
  derived?: KBEdge73;
}
/**
 * 술어별 한정자. 스키마는 ontology.yaml 참조.
 */
export interface KBEdge9 {
  threshold?: KBEdge10;
  currency?: KBEdge13;
  grace_until?: KBEdge14;
  fidelity?: KBEdge15;
  sufficiency?: KBEdge16;
  equivalence?: KBEdge17;
  effectiveness?: KBEdge18;
  precision_est?: KBEdge19;
  recall_est?: KBEdge20;
  license_kind?: KBEdge21;
  status?: KBEdge22;
  list?: KBEdge23;
  designated_on?: KBEdge24;
  delisted_on?: KBEdge25;
  attributor?: KBEdge28;
  basis?: KBEdge29;
  mechanism?: KBEdge30;
  lag_days?: KBEdge31;
  confidence?: KBEdge32;
  amount_usd?: KBEdge33;
  share?: KBEdge34;
  attribute?: KBEdge35;
  from_value?: KBEdge36;
  to_value?: KBEdge37;
  since?: KBEdge38;
  until?: KBEdge39;
  scope_note?: KBEdge42;
  segment?: KBEdge43;
  disclosed_by?: KBEdge44;
  articles?: KBEdge45;
  count?: KBEdge47;
  direction?: KBEdge48;
  evidence_kind?: KBEdge49;
  score?: KBEdge50;
  resolution?: KBEdge51;
  quote?: KBEdge52;
  locator?: KBEdge53;
  effective?: KBEdge54;
  [k: string]: unknown;
}
export interface KBEdge67 {
  doc: KBEdge68;
  confidence: KBEdge69;
  locator?: KBEdge70;
  quote?: KBEdge71;
  retrieved?: KBEdge72;
}
