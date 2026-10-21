# Quick Start Guide — For International Readers

> How to navigate this repository if you do not read Korean. Three learning paths tailored by goal. Last updated: 2026-10-21.

---

## Before You Start

- This repository's primary content is **in Korean**.
- The English edition in [`../en/`](./) is a **gateway**, not a translation.
- For any deep dive, follow the Korean link — consider using browser translation or a reliable human translator for critical work.
- This guide was updated on **2026-10-21**. Other English documents may lag behind the Korean notes; the canonical source is the Korean report [`../reports/가상자산 AML KYT FDS 트래블룰 흐름.md`](../reports/가상자산%20AML%20KYT%20FDS%20트래블룰%20흐름.md).
- **One Korean word, three legal regimes.** "이상거래" (abnormal trading) is *not* the Korean term for STR. Korea runs three separate regimes that all get loosely called "abnormal transaction" monitoring: (1) fraud detection (FDS) and voice-phishing temporary measures under the Telecommunications Fraud Refund Act, applying to exchanges from 2026-10-01; (2) market surveillance under VAUPA Article 12; (3) suspicious transaction reporting (STR) under Tukgeumbeop Article 4. Each has a different legal basis, output and recipient. See [`../notes/4-technology/fds.md`](../notes/4-technology/fds.md).

---

## Path A — "I want to enter the Korean market"

Target audience: global VASPs, M&A teams, country-GM hires preparing a Korean strategy.

### Reading order

1. [`korea-aml-overview.md`](korea-aml-overview.md) — understand the landscape, the two laws, and the Big 4.
2. [`regulatory-comparison.md`](regulatory-comparison.md) §2 and §7 — calibrate Korea against your home regime.
3. [`inspection-response-summary.md`](inspection-response-summary.md) — understand what steady-state supervision looks like.
4. Korean deep dives (browser-translate if needed):
   - [`../notes/2-regulations/korea-fiu-act.md`](../notes/2-regulations/korea-fiu-act.md) — Tukgeumbeop article-by-article.
   - [`../notes/2-regulations/korea-user-protection.md`](../notes/2-regulations/korea-user-protection.md) — VAUPA.
   - [`../notes/7-vendors/korea-solutions.md`](../notes/7-vendors/korea-solutions.md) — local vendor ecosystem.
   - [`../notes/5-compliance/inspection-response.md`](../notes/5-compliance/inspection-response.md) — the full inspection workbook (now split by regime: FIU / VAUPA Art. 12 / Telecommunications Fraud Refund Act).
   - [`../notes/4-technology/fds.md`](../notes/4-technology/fds.md) — FDS vs market surveillance vs STR.

### Practical next steps (10 items)

1. Confirm business model fit — retail KRW exchange, B2B custody, staking, or DeFi frontend each hit different legal regimes.
2. Engage Korean counsel early.
3. Pre-align with a bank on the real-name account partnership. Without this, KRW fiat on-ramps are unavailable.
4. Start the ISMS certification track with KISA early; plan the timeline with your advisers.
5. Recruit an AMLO candidate with Korean financial AML experience. The FIU registration manual revised on 2026-08-13 requires at least 4 AML staff and domestic location of IT facilities (domestic cloud regions accepted).
6. Map your controls against Tukgeumbeop, VAUPA (including Art. 12 market surveillance) and — for exchanges — the Telecommunications Fraud Refund Act (temporary measures, payment suspension and victim refunds, in force for exchanges since 2026-10-01).
7. Choose a blockchain analytics (KYT) provider and a Travel Rule solution through your own PoC; this repository does not rank vendors.
8. Plan for major-shareholder changes: the 2026-08-13 registration manual requires prior notice 30 days before the change.
9. Evaluate DAXA self-regulation (e.g. the withdrawal-delay standard rules in force since 2026-04-07).
10. Build a KoFIU and FSS inspection readiness plan from day one (see [`inspection-response-summary.md`](inspection-response-summary.md)). Note the changes taking effect on 2027-02-19 (enacted-not-in-force as of 2026-10-21): the KRW 1 million Travel Rule threshold is removed, transfers to self-hosted wallets are allowed only between the same person, and transfers of KRW 10 million or more to foreign VASPs or self-hosted wallets require an in-house suspicious-transaction monitoring system — **not** automatic STR filing.

---

## Path B — "I want to compare Korea to my jurisdiction"

Target audience: international consultants, comparative researchers, benchmark teams.

### Reading order

1. [`regulatory-comparison.md`](regulatory-comparison.md) — the side-by-side tables.
2. [`korea-aml-overview.md`](korea-aml-overview.md) — Korean specifics behind the table entries.
3. Pick your home jurisdiction's deep note (browser-translate if needed):
   - US: [`../notes/2-regulations/us-bsa-fincen.md`](../notes/2-regulations/us-bsa-fincen.md)
   - EU: [`../notes/2-regulations/eu-mica-amlr.md`](../notes/2-regulations/eu-mica-amlr.md)
   - Asia: [`../notes/2-regulations/asia-regs.md`](../notes/2-regulations/asia-regs.md)
4. FATF standards baseline: [`../notes/2-regulations/fatf.md`](../notes/2-regulations/fatf.md)

### Key questions to ask when comparing

- Is the regime **registration-based** or **license-based** in practice?
- What is the **Travel Rule threshold** in local currency?
- What is the **cold storage** requirement (percentage)?
- Is there a **real-name banking** gatekeeper?
- What is the **appeals** path for administrative actions?
- Is there an equivalent of **DAXA** (industry self-regulation)?

---

## Path C — "I want academic understanding"

Target audience: graduate students, academic researchers, policy think tanks.

### Recommended curated path

1. Start with the top-level map: [`../README.md`](../README.md).
2. Foundations: [`../notes/1-foundations/`](../notes/1-foundations/) — AML first principles.
3. Korean regulations: [`korea-aml-overview.md`](korea-aml-overview.md) in this English edition, then the Korean originals in [`../notes/2-regulations/`](../notes/2-regulations/).
4. Crypto-specific topics: [`../notes/3-crypto-aml/`](../notes/3-crypto-aml/) — mixers, DeFi, privacy coins, cross-chain bridges.
5. Compliance operations: [`../notes/5-compliance/`](../notes/5-compliance/) — STR/CTR, sanctions, CDD/EDD, internal controls.
6. Case studies: [`../notes/6-cases/`](../notes/6-cases/) — historical incidents and enforcement precedents.
7. Reading lists: [`../deep/papers.md`](../deep/papers.md), [`../deep/reports.md`](../deep/reports.md), [`../deep/conferences.md`](../deep/conferences.md).

### For a semester-length course

- The 60-day Korean curriculum in [`../curriculum/`](../curriculum/) can be adapted into a 15-week syllabus (4 days per week).
- The 6 capstone projects in [`../projects/`](../projects/) provide hands-on assignments:
  - `01-ivms101-builder` — Travel Rule message builder.
  - `02-onchain-tracer` — on-chain tracing tool.
  - `03-mixer-fetcher` — mixer pattern detector.
  - `04-ofac-screener` — sanctions screening service.
  - `05-kyt-wrapper` — KYT API integration.
  - `06-capstone-risk-engine` — unified AML risk engine.

---

## Glossary Reference

Korean AML uses specific terms that rarely translate cleanly. Some high-frequency items:

| Korean | Romanization | English |
|---|---|---|
| 특금법 | Tukgeumbeop | Specified Financial Information Act |
| 이용자보호법 | Iyongja-boholbeop | Virtual Asset User Protection Act |
| 금융정보분석원 | Geumyung Jeongbo Bunseokwon | KoFIU |
| 금융감독원 | Geumyung Gamdokwon | FSS |
| 금융위원회 | Geumyung Wiwonhoe | FSC |
| 자금세탁방지 | Jageum Setak Bangji | Anti-money-laundering (AML) |
| 신고 | Singo | Registration or filing |
| 실명계좌 | Silmyeong Gyejwa | Real-name account |
| 대주주 | Daejuju | Major shareholder |
| 의심거래보고 | Uisim Georae Bogo | Suspicious Transaction Report (STR) — Tukgeumbeop Art. 4 |
| 이상거래 | Isang Georae | Abnormal trading — VAUPA Art. 12 market surveillance (not STR) |
| 이상금융거래 | Isang Geumyung Georae | Abnormal financial transaction — the FDS (fraud detection) term |
| 임시조치 | Imsi Jochi | Temporary measure — delay/suspension of withdrawals or virtual-asset transfers (Telecommunications Fraud Refund Act Art. 2-5) |
| 콜드월렛 | Kold Wollet | Cold wallet |

Full Korean-English glossary: [`../notes/glossary.md`](../notes/glossary.md).

---

## Feedback and Contributions

- Missing concept in English? Open an Issue tagged `english-translation`.
- Translation quality improvements welcome — native English review is especially valuable.
- See [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

---

Back to the English edition entry point: [`README.md`](README.md)
