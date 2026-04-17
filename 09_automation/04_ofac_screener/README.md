# Project 04 — OFAC SDN Crypto Wallet Screener

> 입력 주소가 OFAC SDN에 매칭되는지 자동 체크. (D49 미니 프로젝트)

## 학습 목표

1. OFAC SDN crypto 주소 캐시 운영
2. 단일 / 벌크 스크리닝 함수
3. 매칭 결과 표준 응답
4. False positive disposition 흐름

## 사양

### 입력
- 가상자산 지갑주소 1개 또는 리스트

### 출력
```json
{
  "address": "0xABC...",
  "matched": true,
  "match_info": {
    "entity_name": "Lazarus Group",
    "sdn_id": "12345",
    "programs": ["DPRK", "CYBER"],
    "listed_date": "2020-08-15"
  }
}
```

## 인터페이스

```python
def fetch_ofac_crypto_addresses() -> dict[str, dict]:
    """OFAC SDN.xml → {address.lower(): metadata}"""

def screen(address: str) -> dict:
    """단일 주소 스크리닝"""

def bulk_screen(addresses: list[str]) -> list[dict]:
    """다수 주소 스크리닝"""

def refresh_cache() -> int:
    """캐시 강제 갱신, 신규 추가 수 반환"""
```

## 캐시 전략

- 최초 fetch → `cache/sdn_crypto.json`
- 일 1회 자동 갱신 (timestamp 기반)
- 메모리 dict로 O(1) lookup

## 테스트 케이스

1. 알려진 SDN 주소 (공개) → matched: true
2. 정상 wallet → matched: false
3. 대소문자 다양 (0xABC vs 0xabc) → matched (정규화)
4. 잘못된 형식 입력 → 에러 핸들링
5. 벌크 100개 → 빠른 응답

## 산출물

```
04_ofac_screener/
├── README.md
├── main.py
├── test.py
├── requirements.txt
├── cache/
│   └── sdn_crypto.json
└── .env.example
```

## 학습 자료

- [`../../04_compliance_ops/sanctions_screening.md`](../../04_compliance_ops/sanctions_screening.md)
- [`../../01_regulations/us_bsa_fincen.md`](../../01_regulations/us_bsa_fincen.md) — OFAC
- [OFAC SDN 검색](https://sanctionssearch.ofac.treas.gov/)
- [OFAC 데이터 포맷](https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-list-data-formats-data-schemas)

## 한계 / 주의

- 직접 매칭만 (cluster matching 별도)
- 새 SDN 등재 즉시 반영 안 됨 (캐시 갱신 필요)
- 한국 외교부 명단 별도 (추가 보너스)
- **법적 책임 회피**: 이 도구는 학습용, 실제 컴플라이언스 사용 시 별도 검증

## 보너스 챌린지

- Cluster matching (D35 tracer 결합)
- 한국 외교부 + UN + EU consolidated 통합
- Webhook 알림 (매칭 시)
- Disposition 워크플로 (TP/FP 코드 기록)
- API 서버화 (FastAPI)
