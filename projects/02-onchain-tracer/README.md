# Project 02 — Etherscan API 2-hop Tracer

> 직접 온체인 데이터로 자금 흐름 분석. (D35 미니 프로젝트)

## 학습 목표

1. Etherscan API 사용 (무료 티어)
2. 1-hop / 2-hop 카운터파티 추출
3. 라벨 매칭 시도
4. 결과 시각화 (ASCII / Mermaid)

## 사양

### 입력
- Ethereum 주소 1개

### 출력
- 1-hop: 직접 거래 카운터파티 (이름/금액/시점)
- 2-hop: 1-hop 주소들의 추가 카운터파티
- 텍스트 그래프 또는 Mermaid 다이어그램

## 인터페이스

```python
def get_normal_txs(address: str, limit: int = 100) -> list[dict]:
    """주소의 normal transactions"""

def trace_one_hop(address: str) -> dict[str, dict]:
    """{counterparty: {tx_count, total_amount, last_tx}}"""

def trace_two_hop(address: str) -> dict[str, dict[str, dict]]:
    """{1-hop: {2-hop: {...}}}"""

def render_mermaid(graph: dict) -> str:
    """Mermaid 다이어그램 생성"""
```

## 테스트 주소 추천

공개로 알려진 주소 (학습용):
- Vitalik Buterin (0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045)
- Binance Hot Wallet (0x28C6c06298d514Db089934071355E5743bf21d60)
- Tornado Cash 1 ETH 풀 (0x12D66f87A04A9E220743712cE6d9bB1B5616B8Fc)

## 산출물

```
02_onchain_tracer/
├── README.md
├── main.py
├── requirements.txt
├── data/
│   └── label_db.json  # 자체 라벨 DB
├── sample_outputs/
│   ├── trace_vitalik.md
│   └── trace_tornado.md
└── .env.example
```

## .env

```
ETHERSCAN_API_KEY=your_free_key  # https://etherscan.io/apis
```

## 학습 자료

- [`../../notes/4-technology/blockchain-analytics.md`](../../notes/4-technology/blockchain-analytics.md) — Clustering + Attribution
- [Etherscan API 문서](https://docs.etherscan.io/)

## 한계 / 주의

- Etherscan 무료 티어: 5 calls/sec, 100,000/day
- 1 ETH 주소 → 100개 거래 → 100명 카운터파티 → 2-hop 시 10,000회 호출 가능 (rate limit 주의)
- ERC-20 token transfers는 별도 API endpoint (이 버전은 normal tx만)
- 한국 거래소 attribution은 한정적

## 보너스 챌린지

- ERC-20 token transfers 추가
- Risk Score 계산 (mixer/SDN exposure)
- Multi-chain (BSC, Polygon 추가)
- Visualization (graphviz, vis.js)
