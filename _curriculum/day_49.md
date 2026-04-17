# Day 49 — 🛠️ 미니 프로젝트 4: OFAC SDN crypto wallet 스크리너 + 7주 리뷰

> 실제 OFAC 데이터로 스크리너 만들어보기. ⏱️ ~150분.

## 🎯 회고 질문
1. CDD/EDD/STR 중 가장 까다로운 운영은?
2. 한국 컴플 운영의 특수성 1가지?
3. AMLO의 권한 부족이 부르는 위험?

## 🛠️ 미니 프로젝트 4 (~120분)

### 목표
**OFAC SDN의 가상자산 주소를 fetch + 입력 주소 스크리닝 함수**

### 사양
- 입력: 가상자산 지갑주소 1개
- 출력: 매칭 결과 (TRUE/FALSE) + 매칭 시 SDN entity 정보

### 구현 가이드
프로젝트: `aml/09_automation/04_ofac_screener/`

```python
# main.py 의사코드
import requests
from xml.etree import ElementTree as ET

OFAC_SDN_XML = "https://www.treasury.gov/ofac/downloads/sdn.xml"
# 또는 SDN.csv, advanced consolidated list

def fetch_ofac_crypto_addresses() -> dict[str, dict]:
    """
    OFAC SDN.xml 파싱 → {wallet_address.lower(): {entity_name, sdn_id, programs, listed_date}}
    """
    ...

CACHE = {}  # 일 1회 갱신

def screen(address: str) -> dict:
    """
    return {
        "matched": bool,
        "address": address,
        "match_info": {...} | None,
    }
    """
    addr = address.lower()
    info = CACHE.get(addr)
    return {
        "matched": info is not None,
        "address": address,
        "match_info": info,
    }

def bulk_screen(addresses: list[str]) -> list[dict]:
    return [screen(a) for a in addresses]

if __name__ == "__main__":
    # 테스트: 알려진 SDN crypto address (공개) + 정상 wallet
    test_addrs = ["0xKnownSDN...", "0xNormal..."]
    for r in bulk_screen(test_addrs):
        print(r)
```

### 산출물
- `09_automation/04_ofac_screener/main.py`
- `09_automation/04_ofac_screener/cache/sdn_crypto.json` (캐시)
- `09_automation/04_ofac_screener/README.md`
- `09_automation/04_ofac_screener/test.py`

→ 가이드: [`../09_automation/04_ofac_screener/README.md`](../09_automation/04_ofac_screener/README.md)

### 보너스
- Cluster matching (Etherscan label 또는 자체 데이터셋과 결합)
- 일일 배치 + diff 알람

## ✅ 체크포인트
- [ ] 스크리너 작동
- [ ] OFAC SDN crypto 주소 수십 개 캐시
- [ ] 테스트 케이스 통과
- [ ] [`progress.md`](progress.md) Week 7 + W7 미니 프로젝트 체크
- [ ] git commit + push

## 💭 7주차 회고

가장 어려웠던 컴플 운영:
가장 자동화 가치가 큰 영역:
다음주 사례 중 가장 기대되는:
