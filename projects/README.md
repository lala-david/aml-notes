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

## 참고

- 60일 커리큘럼: [`../curriculum/README.md`](../curriculum/README.md)
- 기술 기반: [`../notes/4-technology/`](../notes/4-technology/)
- 솔루션 시장: [`../notes/7-vendors/`](../notes/7-vendors/)
