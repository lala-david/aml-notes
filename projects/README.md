# 🛠️ projects — 자동화 미니 프로젝트

> 60일 챌린지의 **6개 미니 프로젝트** 코드 + 사양. 이 프로젝트들은 주별로 배운 개념을 **손으로 실행 가능한 코드**로 바꿔보고, 최종적으로 Capstone Risk Engine 설계서로 통합하기 위한 점진적 빌딩 블록입니다. 마지막 업데이트: 2026-04-17.

## 왜 코드까지 작성하나

법·규제·운영을 문서로 읽는 것과, **실제 OFAC SDN XML을 파싱해보고 Etherscan API로 2-hop 추적을 직접 해보는 것**은 이해의 깊이가 다릅니다. 6개 프로젝트는 난이도를 낮게 유지하되, Week 4~8 동안의 지식을 **손에 익도록** 반복시키는 것이 목적. 마지막 Capstone에서 이 6개가 하나의 시스템 설계도로 묶입니다.

## 프로젝트 목록

| 번호 | 폴더 | 주차 | 주제 |
|---|---|---|---|
| 01 | [`01-ivms101-builder/`](01-ivms101-builder/README.md) | W4 (D28) | IVMS101 메시지 빌더 + 검증 |
| 02 | [`02-onchain-tracer/`](02-onchain-tracer/README.md) | W5 (D35) | Etherscan API 2-hop tracer |
| 03 | [`03-mixer-fetcher/`](03-mixer-fetcher/README.md) | W6 (D42) | Mixer 주소 공개소스 fetcher |
| 04 | [`04-ofac-screener/`](04-ofac-screener/README.md) | W7 (D49) | OFAC SDN crypto wallet 스크리너 |
| 05 | [`05-kyt-wrapper/`](05-kyt-wrapper/README.md) | W8 (D56) | KYT API 호출 wrapper |
| 06 | [`06-capstone-risk-engine/`](06-capstone-risk-engine/DESIGN.md) | Capstone (D59) | Mini AML Risk Engine 설계서 |

## 연결 구조 — 6개가 어떻게 합쳐지나

```
01 IVMS101 Builder  ─┐
02 Onchain Tracer   ─┤
03 Mixer Fetcher    ─┼──► 05 KYT Wrapper ──► 06 Capstone Risk Engine
04 OFAC Screener    ─┘          (통합)           (전체 설계서)
```

- **01~04**는 각기 **독립된 학습용 기능**을 구현합니다.
- **05 KYT Wrapper**에서 03(mixer)·04(OFAC)·02(tracer)를 조합해 `kyt_check(address)`라는 **통합 함수**를 만듭니다.
- **06 Capstone**은 여기까지 만든 코드 모듈을 엮어 **하나의 AML Risk Engine 설계서**로 결산합니다.

## 활용 가이드

### 학습 목적
- 코드 = 학습 도구. **프로덕션 코드 아님**
- 작동하는 데모 + 한계 인지가 목표
- 회사 컴플라이언스에 직접 사용 금지 (별도 검증 필수)

### 공통 환경
권장:
- Python 3.10+
- requests / pydantic / python-dotenv
- (선택) pandas / matplotlib / mermaid-py

```bash
pip install requests pydantic python-dotenv
```

### .env 패턴
모든 프로젝트는 API 키를 `.env`로 관리:

```bash
# .env (gitignore에 포함됨)
ETHERSCAN_API_KEY=your_key
OFAC_API_BASE=https://www.treasury.gov/ofac/downloads
```

### 폴더 구조 (공통)
```
0X_project/
├── README.md         # 사양 + 사용법
├── main.py           # 핵심 로직
├── test.py           # 테스트
├── requirements.txt  # 의존성
├── data/             # 산출물
├── sample_outputs/   # 예시
└── .env.example      # 환경변수 예시
```

## 안전 / 윤리

- **공개 데이터만 사용** — OFAC, 공개 블록체인, 공개 라벨 DB
- **API 호출 rate limit 준수**
- **PII 절대 저장 금지**
- **GitHub 푸시 전 .env 확인**

## 다음 단계 (60일 후)

캡스톤(D59) 후 90일 트랙 (D60) 에서 실제 프로토타입으로 발전 가능:
- 트랙 A (기술): 프로젝트 묶어서 통합 시스템
- 트랙 D (솔루션): MVP 기반 비즈니스 모델

## 💼 실무 현장 (Industry Reality)

### 6개 프로젝트가 실제 회사에서 맡는 역할

각 미니 프로젝트는 VASP 컴플 조직의 **한 기능 유닛**에 대응합니다. "이 기능만 떼어내 스타트업 만들 수도 있는" 단위.

| 프로젝트 | 담당 실무 팀 | 실제 벤더 대체재 |
|---|---|---|
| 01 IVMS101 Builder | Travel Rule 엔지니어링 | Notabene · VerifyVASP · CODE · TRISA |
| 02 Onchain Tracer | Investigation(수사) · FCI | Chainalysis Reactor · TRM Forensics · Elliptic Investigator |
| 03 Mixer Fetcher | Threat Intel · Label Ops | Chainalysis Labels · Elliptic · 자체 OSINT팀 |
| 04 OFAC Screener | Sanctions Operations | NICE Actimize · Verafin · ComplyAdvantage |
| 05 KYT Wrapper | KYT 엔지니어링 · AML Monitoring | Chainalysis KYT · Elliptic Navigator · TRM API |
| 06 Capstone Risk Engine | Chief Compliance Office 전체 | Hummingbird · Unit21 (Case Management) 조합 |

### 한국 VASP는 6개 중 몇 개를 자체 구축하나

**Upbit 기준 실제 구성** (2026 추정):

- **자체 구축**: Risk Engine 중 룰 엔진 · KYT wrapper · 자체 라벨 DB (한국 거래소 hot wallet 등)
- **벤더 의존**: IVMS101(람다256 VerifyVASP) · KYT(Chainalysis) · KYC(ARGOS+PASS) · Sanctions(Chainalysis 내장+자체 외교부 매핑)
- **하이브리드**: OFAC SDN crypto 스크리닝은 Chainalysis + 자체 일일 diff 동시 운영

즉 **6개 중 4개는 "자체 구축 + 벤더 보완"**, **나머지 2개(IVMS101·KYT 원천 데이터)는 벤더 의존**이 한국 업계 표준. 완전 자체 구축은 현실적으로 Chainalysis 10년·수백 명·수억 달러 R&D를 혼자 따라잡는 일이라 **ROI가 맞지 않음**.

### 프로덕션과 이 프로젝트의 결정적 차이

| 항목 | 이 프로젝트 | 실제 프로덕션 |
|---|---|---|
| 데이터 규모 | 수천 건 JSON | Kafka 초당 수천 건 · 연 수십억 건 |
| 지연시간(latency) | 응답 수 초 OK | p95 200ms 이하 (거래 블로킹 SLA) |
| 라벨 DB | OFAC + 자체 수집 수백 개 | Chainalysis 10억+ 주소 매핑 |
| 감사(Audit) | 없음 | 모든 판단 결과 5~15년 보관 + 근거 추적 |
| 다중 체인 | ETH 단독 | BTC·ETH·Tron·Solana·BSC 등 20+ |
| 장애대응 | 로컬 재실행 | PagerDuty · SRE on-call |

이 갭을 인지하고 Capstone 설계 시 **"어디까지 자체, 어디부터 벤더"**를 명확히 경계 짓는 연습이 핵심.

### 이 프로젝트 6개를 포트폴리오로 쓸 때

채용 관점에서 6개 모두 실행해 GitHub에 공개하면 **주니어 AML Analyst·KYT 엔지니어 지원 시 실무감각 어필**이 가능합니다. 단, README에 "학습용이며 실제 컴플 도구 아님"을 명시하고, **OFAC SDN 데이터 사용은 학습 목적 공개**임을 분명히 할 것. 한국 VASP AML 조직은 **"법·금융 + 데이터/엔지니어링"** 하이브리드 인재를 선호해 이 조합이 강점이 됩니다.

## 참고

- 60일 커리큘럼: [`../curriculum/README.md`](../curriculum/README.md)
- 기술 기반: [`../notes/4-technology/`](../notes/4-technology/)
- 솔루션 시장: [`../notes/7-vendors/`](../notes/7-vendors/)
