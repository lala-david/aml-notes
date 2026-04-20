# Day 56 — 🛠️ 미니 프로젝트 5: KYT API 호출 wrapper + 8주 리뷰

> 벤더 KYT API 사용해보기. ⏱️ ~150분.

## 📖 오늘 뭘 배우나

Week 8의 결산이자 Capstone의 마지막 조각. D42(mixer fetcher)·D49(OFAC screener)·D35(2-hop tracer)의 결과물을 하나의 **KYT 호출 wrapper**로 통합. 결과 JSON에 `risk_score`·`risk_categories`·`exposure`·`recommended_action`이 담기면, 이게 그대로 Capstone Risk Engine의 **주요 입력**이 됩니다.

## 🎯 회고 질문
1. 8주차의 사례에서 가장 충격적이었던 것?
2. 학술 vs 산업 격차?
3. 벤더 KYT 도입 우선순위?

## 🛠️ 미니 프로젝트 5 (~120분)

### 목표
**KYT API 호출 wrapper 작성** (실제 무료 API 또는 Mock)

### 옵션 A: 실제 무료 API
- [AMLBot 무료 티어](https://amlbot.com/) — 일부 무료
- [Bitquery API](https://bitquery.io/) — GraphQL 무료 티어
- [Etherscan/BSCScan + 자체 라벨 매칭]

### 옵션 B: Mock API (학습용)
- 자기가 만든 OFAC fetcher (D49) + mixer fetcher (D42) 결과를 합쳐 자체 KYT 호출

### 사양
```python
# main.py 의사코드
def kyt_check(address: str) -> dict:
    """
    return {
        "address": "...",
        "risk_score": 0~100,
        "risk_categories": ["mixer", "sanctions", "ransomware", ...],
        "exposure": {
            "direct": [...],
            "indirect_2hop": [...],
        },
        "recommended_action": "ALLOW" | "REVIEW" | "BLOCK",
    }
    """
    ...
```

### 구현 가이드
프로젝트: `aml/projects/05-kyt-wrapper/`

- D42 (mixer fetcher) + D49 (OFAC screener) 결과를 통합
- exposure는 D35 (2-hop tracer)와 결합

### 산출물
- `projects/05-kyt-wrapper/main.py`
- `projects/05-kyt-wrapper/README.md`
- `projects/05-kyt-wrapper/sample_results/` (5개 주소 결과)

→ 가이드: [`../projects/05-kyt-wrapper/README.md`](../projects/05-kyt-wrapper/README.md)

## ✅ 체크포인트
- [ ] Wrapper 작동
- [ ] 5개 주소 sample 결과
- [ ] [`progress.md`](progress.md) Week 8 + W8 미니 프로젝트 체크
- [ ] git commit + push

## 💭 8주차 회고 (캡스톤 직전)

전체 8주에서 가장 큰 변화:
가장 약한 영역 (보강 필요):
캡스톤 방향:
