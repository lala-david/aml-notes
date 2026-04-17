# 🛠️ projects — 자동화 미니 프로젝트

> 60일 챌린지의 6개 미니 프로젝트 코드 + 사양. 마지막 업데이트: 2026-04-17.

## 프로젝트 목록

| 번호 | 폴더 | 주차 | 주제 |
|---|---|---|---|
| 01 | [`01_ivms101_builder/`](01_ivms101_builder/README.md) | W4 (D28) | IVMS101 메시지 빌더 + 검증 |
| 02 | [`02_onchain_tracer/`](02_onchain_tracer/README.md) | W5 (D35) | Etherscan API 2-hop tracer |
| 03 | [`03_mixer_fetcher/`](03_mixer_fetcher/README.md) | W6 (D42) | Mixer 주소 공개소스 fetcher |
| 04 | [`04_ofac_screener/`](04_ofac_screener/README.md) | W7 (D49) | OFAC SDN crypto wallet 스크리너 |
| 05 | [`05_kyt_wrapper/`](05_kyt_wrapper/README.md) | W8 (D56) | KYT API 호출 wrapper |
| 06 | [`06_capstone_risk_engine/`](06_capstone_risk_engine/DESIGN.md) | Capstone (D59) | Mini AML Risk Engine 설계서 |

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
