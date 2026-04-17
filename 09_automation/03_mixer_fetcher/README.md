# Project 03 — Mixer 주소 공개소스 Fetcher

> 위험 wallet 데이터셋을 공개 소스에서 자동 수집. (D42 미니 프로젝트)

## 학습 목표

1. OFAC SDN XML 파싱
2. Etherscan label 데이터 활용
3. 표준 형식으로 저장 (JSON + CSV)
4. 일일 업데이트 + diff 추적

## 사양

### 입력
- 없음 (자동 fetch)

### 출력
- `data/mixer_addresses.json`
- `data/mixer_addresses.csv`
- 매 fetch 시 diff 로그

## 인터페이스

```python
def fetch_ofac_sdn() -> list[dict]:
    """OFAC SDN.xml → 가상자산 주소만 추출"""

def fetch_etherscan_label(label: str) -> list[str]:
    """Etherscan 라벨 페이지 (예: tornado-cash)"""

def normalize(addr: str, source: str, label: str) -> dict:
    return {
        "address": addr.lower(),
        "label": label,
        "source": source,
        "fetched_at": datetime.utcnow().isoformat(),
    }

def save_json(records: list[dict], path: str): ...
def save_csv(records: list[dict], path: str): ...

def diff_with_previous(current: list, prev: list) -> dict:
    """{added: [...], removed: [...]}"""
```

## 데이터 소스

### 1. OFAC SDN
- URL: https://www.treasury.gov/ofac/downloads/sdn.xml
- 가상자산 주소: `<feature><type>Digital Currency Address</type>...` 형태
- 무료, 공개

### 2. Etherscan Label DB
- 페이지 스크래핑 (rate limit 주의)
- 예: `https://etherscan.io/accounts/label/tornado-cash`
- 공개 정보, robots.txt 준수

### 3. (선택) 추가 OSINT
- GitHub 라벨 저장소 (예: `0xVisor/labels`)
- Slowmist / 분석회사 공개 자료

## 산출물

```
03_mixer_fetcher/
├── README.md
├── main.py
├── requirements.txt
├── data/
│   ├── mixer_addresses.json
│   ├── mixer_addresses.csv
│   └── history/
│       └── YYYY-MM-DD.json  # 일별 스냅샷
└── .env.example
```

## 학습 자료

- [`../../04_compliance_ops/sanctions_screening.md`](../../04_compliance_ops/sanctions_screening.md) — 제재 스크리닝
- [`../../02_crypto_aml/onchain_typology.md`](../../02_crypto_aml/onchain_typology.md) — Mixer
- [OFAC SDN 다운로드](https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-list-data-formats-data-schemas)

## 한계 / 주의

- OFAC SDN은 정기 업데이트 (보통 주 1~2회)
- Etherscan 스크래핑은 약관 준수 필수
- 라벨 정확도는 출처에 따라 변동
- 가상자산 주소가 SDN에 포함되는 형식이 시간에 따라 변할 수 있음

## 보너스 챌린지

- 일일 cron job (GitHub Actions)
- Slack/Discord 알림 (신규 추가 시)
- 한국 외교부 제재명단 추가
- UN Consolidated List 추가 (이름 + 가상자산 매핑)
