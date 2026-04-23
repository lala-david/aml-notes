# Blockchain Analytics — Technical Summary

> Summary of the algorithmic core of crypto AML: clustering, attribution, exposure scoring, cross-chain bridge matching, and the Korean fuzzy matching problem for sanctions screening. Condensed from [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) (685 lines) and [`../notes/5-compliance/sanctions-screening.md`](../notes/5-compliance/sanctions-screening.md). For the full pseudocode, SQL, and vendor-comparison tables, see the Korean originals.

## TL;DR

- Blockchain analytics sits on two pillars: **Clustering** (which addresses belong to one entity) and **Attribution** (which entity is that).
- Core heuristics: **Common Input Ownership (CIOH)**, Change Detection, Deposit Heuristic, behavior-based.
- Bitcoin (UTXO) clustering is stronger than Ethereum (account-model), which leans more on attribution databases.
- Exposure Score is the main KYT output: weighted sum of direct and indirect (N-hop) risk exposure with time decay.
- Cross-chain tracing reduces to **bridge event matching** by nonce, amount tolerance, and time window.
- Korean sanctions screening needs custom fuzzy matching — the top five Korean surnames account for roughly 50% of the population, which breaks default Jaro-Winkler thresholds.

---

## 1. Common Input Ownership Heuristic (CIOH)

### Algorithm

```python
def common_input_ownership(tx: Transaction) -> set[Address] | None:
    if len(tx.inputs) < 2:
        return None
    if is_coinjoin(tx):
        return None
    return {inp.address for inp in tx.inputs}
```

### Why it works

In Bitcoin's UTXO model, spending any UTXO requires its private key. Multiple inputs in the same transaction therefore imply a **common key controller**. Even if a user splits funds across 100 addresses, the moment they consolidate two UTXOs in a single transaction, the whole set collapses into one cluster. This makes Bitcoin de-anonymization a matter of time — and is the technical foundation Chainalysis was built on.

### Limits

- **UTXO-only**. Ethereum accounts have a single `from`, so CIOH does not apply.
- **CoinJoin** (Wasabi, Samourai Whirlpool, JoinMarket) intentionally combines inputs from different entities, breaking the assumption.
- **Custodial hot wallets** combine many customers' funds. The cluster identifies the exchange correctly, but not individual customers.

### CoinJoin fingerprint pre-filter

```python
def is_coinjoin(tx: Transaction) -> bool:
    if len(tx.inputs) < 2:
        return False

    amounts = [o.value for o in tx.outputs]
    uniform_outputs = [a for a in amounts if amounts.count(a) >= 3]
    if not uniform_outputs:
        return False

    # Known fixed denominations (Wasabi 0.1 BTC, Samourai 0.001 / 0.01 / 0.1)
    KNOWN_DENOMS = {0.1e8, 0.01e8, 0.001e8}
    if any(a in KNOWN_DENOMS for a in uniform_outputs):
        return True

    # Wasabi ~1:1.5 input:output, Whirlpool 5:5
    if len(tx.inputs) >= 5 and len(tx.outputs) >= 5:
        if abs(len(tx.inputs) - len(tx.outputs)) <= 1:
            return True

    return False
```

### Accuracy benchmarks

| Dataset | Precision | Recall | F1 | Source |
|---|---|---|---|---|
| Bitcoin mainnet random sample | 0.95-0.98 | 0.99 | 0.97 | Meiklejohn et al. 2013 |
| Elliptic (200K labels) | 0.87 | 0.93 | 0.90 | Weber et al. 2019 |
| CoinJoin-inclusive sample | 0.75 | 0.98 | 0.85 | Möser & Böhme 2017 |
| Elliptic2 (2024) + fingerprint filter | 0.95 | 0.92 | 0.93 | Bellei et al. 2024 |

---

## 2. Exposure Score Formula

### Definition

An Exposure Score quantifies on a 0-100 scale how tightly an address (or cluster) is linked — within **N hops** — to known risk entities (OFAC SDN, mixers, darknet markets, ransomware).

- **Direct (1-hop)**: address transacts directly with a risk entity
- **Indirect (N-hop, N >= 2)**: reaches a risk entity through intermediaries (usually analyzed up to 5 hops; beyond that the signal drowns in noise)

### Generalized formula

```
score = clip(
    Σ (e_direct_i × w_cat_i × f_amount × f_behavior)
    + Σ (e_indirect_j × w_cat_j × decay(age_j) × f_amount),
    0, 100
)
```

Where:

- e_direct_i, e_indirect_j: exposure percentage or amount share per category
- w_cat: category weight (see below)
- decay(age) = exp(-λ × age_days / 365), λ defaults to 0.5 (varies by vendor)
- f_amount = min(1 + ln(tx_krw / 100M), 1.3), floor 0
- f_behavior = 1.0 (normal), 1.2-1.5 (smurfing, pass-through, layering)

### Category weights (generalized estimates)

| Category | Direct | 2-hop | 3-hop | Rationale |
|---|---|---|---|---|
| OFAC SDN | 10.0 | 5.0 | 2.0 | Country-level sanctions — highest |
| UN / EU sanctions | 8.0 | 4.0 | 1.5 | |
| Ransomware | 6.0 | 3.0 | 1.0 | Direct criminal proceeds |
| Mixer (Tornado, Wasabi) | 5.0 | 2.0 | 0.5 | Intentional obfuscation |
| Darknet market | 4.0 | 1.5 | 0.3 | |
| Stolen funds | 3.0 | 1.5 | 0.3 | Victim assets |
| High-risk exchange | 1.5 | 0.5 | 0.1 | Weak regulation |
| Gambling | 0.5 | 0 | 0 | Legal but notable |

### Vendor-specific lambda (estimated)

| Vendor | λ | Philosophy |
|---|---|---|
| Chainalysis | 0.5 | Balanced |
| TRM Labs | 0.3 | Long-tail tracking (CT-focused) |
| Elliptic | 0.6 | Short-window focus (EU TFR zero-threshold) |

### Worked example

**Scenario**: Korean VASP customer A withdraws KRW 500M to 0xABC...

KYT results:
- Direct: Tornado Cash 5% (USD 20K), 180 days old
- 2-hop: OFAC SDN (Ren Fiery) 8%, 365 days old
- Direct: Binance (not high-risk) 0%, excluded
- Behavior: normal, f_behavior = 1.0
- Amount factor: f_amount = min(1 + ln(5), 1.3) = 1.3

Calculation:

```
direct_tornado  = 5 × 5.0 × 1.3 × 1.0                              = 32.5
indirect_ofac   = 8 × 5.0 × exp(-0.5 × 365/365) × 1.3 × 1.0
                = 8 × 5.0 × 0.61 × 1.3                             = 31.72
score           = clip(32.5 + 31.72, 0, 100)                       = 64.22  -> 64 (HIGH)
```

Action: BLOCK + auto-STR trigger.

### SQL reproduction

```sql
WITH exposures AS (
  SELECT 'Tornado'  AS category, 5.0 AS e_pct, 5.0 AS w, 1.0       AS decay, 1.3 AS f_amt, 1.0 AS f_beh
  UNION ALL
  SELECT 'OFAC_SDN',             8.0,          5.0,    EXP(-0.5),            1.3,         1.0
)
SELECT LEAST(SUM(e_pct * w * decay * f_amt * f_beh), 100) AS risk_score
FROM exposures;
-- result: 64.22
```

### Override factors (FP reduction)

Raw KYT scores, applied directly, yield FP rates of 30-50%. Production VASPs apply customer-attribute-based overrides:

```
score_final = score × override_factor
```

- KYC Tier 3 (passport + address verification + SoF evidence): × 0.7
- 2+ years of clean transaction history: × 0.85
- Receiver is internal customer: × 0.6
- Abnormal behavior (late-night, high velocity): × 1.2

### Threshold tuning

Monthly retune against target FP = 5%, FN = 1%:

```python
def tune_threshold(alerts, labels, target_fp=0.05, target_fn=0.01):
    from sklearn.metrics import roc_curve
    fpr, tpr, thresholds = roc_curve(labels, [a.score for a in alerts])
    fnr = 1 - tpr
    candidates = [(t, f, n) for t, f, n in zip(thresholds, fpr, fnr)
                  if f <= target_fp and n <= target_fn]
    return max(candidates, key=lambda x: x[0])[0] if candidates else None
```

---

## 3. Cross-chain Bridge Matching

### Problem

Funds flowing across chains (Ethereum -> Polygon -> Arbitrum -> Optimism, and so on) move through **bridge contracts**. Each chain's transactions are independent — KYT must reconnect them.

### Bridge event structure

| Chain | Event | Key fields | Nonce? |
|---|---|---|---|
| Polygon PoS | LockEvent | (user, token, amount, targetChain, depositCount) | Yes |
| Arbitrum | OutboundTransfer | (token, from, to, seqNumber, amount) | Yes |
| Optimism | WithdrawalInitiated | (l1Token, l2Token, from, to, amount, nonce) | Yes |
| Wormhole | LogMessagePublished | (sender, sequence, nonce, payload) | Yes |
| LayerZero | PacketSent | (dstEid, receiver, payload) | Generic — payload decoding required |
| Hop Protocol | TransferSentToL2 | (chainId, recipient, amount, transferId) | transferId acts as nonce |

### Matching algorithm

```python
def match_bridge_events(
    lock_events: list[LockEvent],
    mint_events: list[MintEvent],
    time_window: int = 300,           # seconds
    amount_tolerance: float = 0.005,  # 0.5%
) -> list[tuple[LockEvent, MintEvent]]:
    matches = []
    for lock in lock_events:
        candidates = []
        for mint in mint_events:
            if mint.token_canonical != lock.token_canonical:
                continue
            if abs(mint.timestamp - lock.timestamp) > time_window:
                continue
            if abs(mint.amount - lock.amount) / lock.amount > amount_tolerance:
                continue
            # Nonce match is deterministic
            if hasattr(lock, 'nonce') and hasattr(mint, 'nonce'):
                if lock.nonce == mint.nonce:
                    candidates = [mint]
                    break
            candidates.append(mint)
        if len(candidates) == 1:
            matches.append((lock, candidates[0]))
        elif len(candidates) > 1:
            # Fallback: pick the closest amount
            best = min(candidates, key=lambda m: abs(m.amount - lock.amount))
            matches.append((lock, best))
        # Zero candidates: Sunrise (destination not yet received) — requeue
    return matches
```

### Accuracy by bridge type

| Bridge | Nonce match | Accuracy | Notes |
|---|---|---|---|
| Polygon PoS | Yes | 97-99% | Standard |
| Arbitrum | Yes | 96-99% | seqNumber is deterministic |
| Optimism | Yes | 96-99% | Standard |
| Wormhole | Yes (VAA) | 94-98% | Requires VAA validation |
| Hop Protocol | transferId | 92-96% | Indirect via transferRoot |
| LayerZero OFT | Generic | 85-92% | Only token-bridge payloads |
| LayerZero Generic | Decoder needed | 40-60% | Per-DApp custom decoder |

### Limits

- Multi-hop chains (ETH -> Polygon -> Arbitrum -> BSC) multiply errors: 3 hops at 90% each yields ~0.73.
- Centralized OTC or P2P transfers have **no on-chain bridge events** — untraceable.
- Liquidity-based bridges (THORChain, Across) pool funds, breaking 1-to-1 sender-to-receiver linkage.

---

## 4. Korean Fuzzy Matching for Sanctions

### Problem

The top five Korean surnames (Kim, Lee, Park, Choi, Jung) cover roughly 50% of the population. Applying the default global Jaro-Winkler threshold of 0.85 produces hundreds of false positives per day.

**Example**: Customer "Kim Min-soo 1990-01-01 KR" screens against OFAC SDN "Kim Min-su 1985-03-15 KP" (North Korea). Jaro-Winkler similarity: 0.97. At the default threshold this becomes a HIT, requiring manual analyst disposition. At a large Korean VASP, junior analysts spend ~30% of their time clearing exactly this kind of FP.

### Tuned pipeline

```python
from jellyfish import jaro_winkler_similarity

COMMON_KR_SURNAMES = {
    "Kim", "Lee", "Park", "Choi", "Jung", "Jang",
    "Yoon", "Cho", "Kang", "Lim", "Han", "Shin",
}

def screen_korean_customer(customer: Customer, sdn_list: list[SDN]) -> list[Hit]:
    hits = []
    for sdn in sdn_list:
        # 1. Surname variant match (Kim / Gim / Ghim etc.)
        surname_match = any(
            jaro_winkler_similarity(
                normalize_kr(customer.surname),
                normalize_kr(variant)
            ) >= 0.95
            for variant in sdn.surname_variants
        )
        if not surname_match:
            continue

        # 2. Raise threshold to 0.92 if surname is a top Korean one
        threshold = 0.92 if customer.surname in COMMON_KR_SURNAMES else 0.88
        name_score = jaro_winkler_similarity(
            normalize(customer.full_name),
            normalize(sdn.name)
        )
        if name_score < threshold:
            continue

        # 3. Require a secondary identifier (DOB or nationality)
        dob_match = customer.dob and customer.dob == sdn.dob
        nat_match = sdn.nationalities and customer.nationality in sdn.nationalities
        if not (dob_match or nat_match):
            continue

        # 4. Whitelist (5-year validity)
        if (customer.id, sdn.id) in WHITELIST_5Y:
            continue

        hits.append(Hit(
            sdn=sdn,
            name_score=name_score,
            dob_match=dob_match,
            nat_match=nat_match,
        ))
    return hits
```

### Name normalization

```python
def normalize_kr(name: str) -> str:
    import re
    name = name.lower().strip()
    NORMALIZATIONS = [
        (r"-", ""), (r",\s*", " "),
        ("gil-dong", "gildong"),
        ("min-soo", "minsoo"), ("minsu", "minsoo"),
        # McCune-Reischauer vs Revised Romanization
        ("hoon", "hun"), ("seung", "sung"),
    ]
    for pat, rep in NORMALIZATIONS:
        name = re.sub(pat, rep, name)
    return " ".join(name.split())
```

### Threshold performance (representative Korean VASP, 1M customer DB x 1.5K OFAC SDN)

| Configuration | FP rate | FN rate | Daily alerts |
|---|---|---|---|
| Jaro-Winkler 0.85 alone | ~90% | ~0.5% | 200+ |
| JW 0.92 + DOB required | ~45% | ~1.5% | ~80 |
| JW 0.92 + DOB + surname filter | ~25% | ~2% | ~30 |
| Full pipeline (above) | ~12% | ~3% | 10-15 |

**Trade-off**: lower FP means more FN. Supervisors expect FN below 3%; driving FN to 0.5% forces FP close to 90%, which is operationally unmanageable.

### SQL implementation (Snowflake or Postgres)

```sql
WITH candidates AS (
  SELECT c.id AS cust_id, s.id AS sdn_id,
         JARO_WINKLER(c.full_name, s.name) AS score,
         (c.dob = s.dob) AS dob_match,
         (c.nationality = ANY(s.nationalities)) AS nat_match
  FROM customers c
  CROSS JOIN ofac_sdn s
  WHERE SOUNDEX(c.surname) = SOUNDEX(s.surname)  -- primary filter
)
SELECT * FROM candidates
WHERE score >= CASE
    WHEN cust_id IN (SELECT id FROM customers
                     WHERE surname IN ('Kim','Lee','Park','Choi','Jung',
                                       'Jang','Yoon','Cho','Kang'))
    THEN 0.92 ELSE 0.88 END
  AND (dob_match OR nat_match);
```

---

## 5. Clustering Benchmarks

### Public datasets

| Dataset | Year | Size | Labels | Use |
|---|---|---|---|---|
| Elliptic | 2019 | 203K nodes, 234K edges | 23% labeled | First public AML graph |
| Elliptic++ | 2022 | ~840K tx, 1.6M addresses | Both addresses and transactions | Extended edition |
| Elliptic2 | 2024 | ~122M tx, 196M transactions | Subgraph-level labels | Shape-aware |
| BABD-13 | 2022 | 13 behavior classes | Supervised | Address classification |
| WalletExplorer dump | Continuous | ~8M addresses | Exchange-tagged | Label seed |

### Bitcoin clustering accuracy

| Method | Precision | Recall | F1 | Source |
|---|---|---|---|---|
| CIOH only | 0.87 | 0.93 | 0.90 | Meiklejohn 2013 reproduction |
| CIOH + Change Detection | 0.91 | 0.95 | 0.93 | Androulaki 2013 |
| CIOH + CoinJoin Fingerprint | 0.95 | 0.92 | 0.93 | Möser 2017 basis |
| Random Forest (Elliptic) | 0.93 | 0.77 | 0.84 | Weber 2019 |
| GCN (Graph Conv Network) | 0.92 | 0.83 | 0.87 | Weber 2019 |
| GAT (Graph Attention) | 0.94 | 0.86 | 0.90 | Alarab 2020 |
| Shape-based SSL (Elliptic2) | 0.96 | 0.89 | 0.92 | Bellei 2024 |
| Chainalysis Behavior (proprietary) | ~0.97 (claim) | ~0.95 (claim) | — | Vendor-internal |

---

## 6. References

- Meiklejohn et al. (2013) — "A Fistful of Bitcoins" (IMC). The original formalization of CIOH and change detection.
- Androulaki et al. (2013) — "Evaluating User Privacy in Bitcoin" (FC). Empirical clustering evaluation.
- Möser and Böhme (2017) — "Anonymous Alone? Measuring Bitcoin's Second-Generation Anonymization Techniques" (ESORICS). CoinJoin analysis.
- Weber et al. (2019) — "Anti-Money Laundering in Bitcoin with Graph Convolutional Networks". Elliptic release.
- Harlev et al. (2018) — "Breaking Bad: De-Anonymising Entity Types on the Bitcoin Blockchain".
- Bellei et al. (2024) — "Shape vs. Structure: Topology-Aware Self-Supervised Learning for AML on Elliptic2".
- Xiang et al. (2022) — "BABD: A Bitcoin Address Behavior Dataset".
- Farrugia et al. (2020) — "Detection of Illicit Accounts over the Ethereum Blockchain".

---

## Korean Source

The Korean notes go deeper on pseudocode, SQL, vendor-specific behaviors, the self-build vs vendor debate, Reactor operator workflow, and industry economics:

- [`../notes/4-technology/blockchain-analytics.md`](../notes/4-technology/blockchain-analytics.md) — Core analytics (685 lines)
- [`../notes/5-compliance/sanctions-screening.md`](../notes/5-compliance/sanctions-screening.md) — Korean fuzzy matching detail
- [`../notes/7-vendors/analytics-vendors.md`](../notes/7-vendors/analytics-vendors.md) — Vendor comparison (Chainalysis, TRM, Elliptic, Crystal)
