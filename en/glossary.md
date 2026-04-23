# AML Glossary — English/Korean Bilingual

> Bilingual glossary of AML, cryptocurrency, and Korean regulatory terms. Roughly 200 entries organized A-Z. Aimed at international readers who need the Korean context behind each term. For the original Korean version, see [`../notes/glossary.md`](../notes/glossary.md).

Core entries carry an "Industry practice" note — a one-or-two-line sketch of how the term actually gets used in Korean VASP operations.

---

## A

### AML — Anti-Money Laundering (자금세탁방지)
The body of laws, regulations, and procedures designed to prevent criminals from disguising illegally obtained funds as legitimate income.

**Industry practice**: A Korean VASP's AML program is the sum of nine statutory duties — registration, KYC, EDD, KYT, sanctions, STR, Travel Rule, recordkeeping, and internal controls. The "AML lead" usually owns all nine.

### AMLA — Anti-Money Laundering Authority
EU AML supervisor, headquartered in Frankfurt and operational from 2025.

**Industry practice**: Scheduled to begin direct supervision of about 40 large cross-border financial institutions around 2028. Whether a Korean VASP expanding into the EU appears on that list dictates how hands-on its supervision will be.

### AMLD — Anti-Money Laundering Directive
EU AML directive series. AMLD5 is in force; AMLD6 is being transposed.

### AMLO — Anti-Money Laundering Officer (자금세탁방지책임자)
Senior executive designated as AML compliance owner.

**Industry practice**: Korean Tukgeumbeop requires an **executive-tier** AMLO with STR decision authority and a direct reporting line to the CEO. After Binance's CZ prosecution, personal criminal liability for AMLOs has become an explicit risk.

### AMLR — Anti-Money Laundering Regulation
EU AML regulation, in force 2027-07-10.

### AML/CFT
Combined notation for anti-money laundering and counter-terrorist financing.

**Industry practice**: ML is about "hiding the source" (ex-post); TF is about "blocking the destination" (ex-ante). Rule engines work better when the two are managed as separate groups, not a single bucket.

### APG — Asia-Pacific Group on Money Laundering
FATF regional body. Korea is a member.

### APT — Advanced Persistent Threat
State-sponsored intrusion (Lazarus etc.). Usually refers to nation-state cyber units.

### ARGOS
Korean KYC vendor providing identity verification integrated with 본인확인기관 (PASS/NICE/KCB). Dominant in Korean VASP onboarding.

### ART — Asset-Referenced Token
MiCA token category pegged to multiple assets.

### Attribution
Mapping a wallet cluster to a known real-world entity.

**Industry practice**: This is the real moat for Chainalysis, TRM, and Elliptic. Clustering algorithms are reproducible; attribution databases take years to accumulate.

## B

### Beneficial Owner / BO (실소유자)
The ultimate natural-person owner of a legal entity (25%+ in Korea).

**Industry practice**: During corporate onboarding you recurse through the ownership chain. If UBO cannot be confirmed, **refuse the account** — accepting anyway risks STR exposure plus business suspension.

### Binance
Global crypto exchange. Not registered in Korea; partially blocked by FIU-coordinated addresses.

### Bithumb
Korean Big-4 exchange. Banking partner: NH NongHyup. KYT: Chainalysis + CODE.

### BSA — Bank Secrecy Act (1970)
US foundational AML law.

**Industry practice**: The original model for FATF Recommendations. Many Tukgeumbeop provisions mirror BSA structure, so US legal knowledge accelerates Korean legal comprehension.

### Bridge
Cross-chain asset transfer infrastructure.

**Industry practice**: When a withdrawal address is a bridge contract, the next hop cannot be traced natively. Many Korean VASPs auto-queue such transactions for STR review.

## C

### CASP — Crypto-Asset Service Provider
EU MiCA term, roughly equivalent to VASP.

### CCO — Chief Compliance Officer
Head of compliance.

### CDD — Customer Due Diligence (고객실사)
Standard due diligence.

**Industry practice**: Four steps — identify, confirm BO, purpose, ongoing monitoring. Not a one-shot event. Korean guideline: re-review every 5 years (low), 3 years (medium), 1 year (high).

### CFT — Combating the Financing of Terrorism (테러자금조달방지)

### Chain Hopping
Layering across chains: BTC → ETH → Tron → BNB.

### Chainalysis
US blockchain analytics company, de facto industry standard.

**Industry practice**: Considered the reference tool by US federal agencies. Easiest to have admitted as evidence in Korean inspections. Used by most of the Korean Big 4.

### CIOH — Common Input Ownership Heuristic
"All inputs of a Bitcoin transaction are controlled by the same entity."

**Industry practice**: Powerful on UTXO chains (Bitcoin), inapplicable on account-model chains (Ethereum). A CoinJoin pre-filter is required to avoid false clusters.

### Circle
US stablecoin issuer (USDC).

### Cluster / Clustering
Grouping addresses estimated to belong to one entity.

**Industry practice**: UTXO (Bitcoin) clustering accuracy outperforms account-model (Ethereum). Ethereum analytics lean harder on attribution databases.

### CMLN — Chinese Money Laundering Network
Chinese-language money-laundering networks.

**Industry practice**: Telegram/WeChat OTC plus "laundering-as-a-service". Serves as Lazarus's laundering partner. Processed an estimated USD 16.1B in 2025.

### CODE
Korean Travel Rule consortium (Bithumb, Korbit, Coinone joint venture).

### Cold Wallet (콜드월렛)
Offline wallet.

**Industry practice**: The VAUPA enforcement decree requires **at least 80%** of user virtual assets to be held in cold storage.

### Coinbase
US exchange. Uses TRISA for Travel Rule.

### Coinone
Korean Big-4 exchange. Banking partner: Kakao Bank. Travel Rule: CODE.

### CoinJoin
Cooperative-spend Bitcoin mixing technique (Wasabi, Samourai, JoinMarket).

### CPF — Counter-Proliferation Financing
Blocking proliferation financing for WMD programs.

### CTR — Currency Transaction Report
Threshold-based cash transaction report.

**Industry practice**: Korea uses KRW 10M, the US uses USD 10K. Rarely triggered for VASPs (except OTC desks) because fiat cash is uncommon.

### CVC — Convertible Virtual Currency
FinCEN term for convertible virtual currency.

## D

### DAO — Decentralized Autonomous Organization

### DAXA — Digital Asset eXchange Association (디지털자산거래소공동협의체)
Korean Big-4 exchange industry body.

**Industry practice**: No statutory enforcement power, but self-regulation (joint listing review, shared blacklist) is the de facto industry standard. The first gate for any new token listing.

### DeFi — Decentralized Finance

### DEX — Decentralized Exchange

**Industry practice**: No-KYC swap venue, frequently abused for layering. DEX contract exposure is a common KYT rule trigger.

### DMLRO — Deputy MLRO
Deputy compliance officer.

### DPRK — Democratic People's Republic of Korea (North Korea)

### DTI — Digital Token Identifier (ISO 24165)
Standardized token identifier.

## E

### EDD — Enhanced Due Diligence (강화된 고객실사)

**Industry practice**: Sits **on top of** CDD, adding source-of-funds evidence plus executive approval. The core is **documented SoF/SoW**, not "an extra ID photo".

### Elliptic
UK blockchain analytics company, strong in European market and NFT analytics.

### EMT — E-Money Token
MiCA fiat-pegged stablecoin category.

### EOA — Externally Owned Account
Ethereum user account controlled by a private key.

### ERA — Enterprise-wide Risk Assessment

**Industry practice**: Korean RBA guideline requires at least annual execution. Typically the **first document** supervisors request during inspections.

### ESMA — European Securities and Markets Authority

### Exposure
The degree to which an address is directly or indirectly connected to risk categories.

**Industry practice**: The core output of a KYT system. Risk Score combines direct (1-hop) vs indirect (N-hop), amount, time, and category weighting.

## F

### FATF — Financial Action Task Force
International AML body.

**Industry practice**: Publishes recommendations, not laws. The parent framework of Korean regulation. Grey/Black Lists operate effectively as economic sanctions.

### FinCEN — Financial Crimes Enforcement Network
US FIU.

### FIU — Financial Intelligence Unit (금융정보분석원)

**Industry practice**: Korea's is KoFIU. The hub that receives, analyzes, and redistributes STRs to the police, prosecutors, National Tax Service, and Customs.

### Freezing
Asset freeze.

### FSC — Financial Services Commission (금융위원회)
Top Korean financial policy body. Licensing and regulation authority.

### FSS — Financial Supervisory Service (금융감독원)
Korean prudential and conduct supervisor. Inspects user protection under VAUPA.

## G

### GENIUS Act
US stablecoin statute (July 2025). Full effect 2027-01.

### GLEIF LEI — Legal Entity Identifier
Global standard for legal-entity identification.

### Grandfathering
Transition period for incumbent operators. MiCA grandfathering ends 2026-07-01.

### Grey List
FATF enhanced-monitoring jurisdictions.

## H

### HSM — Hardware Security Module

## I

### IEEPA — International Emergency Economic Powers Act
US statutory basis for OFAC authority.

**Industry practice**: Core law in the 2024 Tornado Cash 5th Circuit decision, which held that "immutable smart contracts are not IEEPA 'property'" — OFAC lost.

### Integration
Third (and final) stage of money laundering — conversion into apparently legitimate assets.

### ISMS — Information Security Management System
Korean security certification, issued by KISA. Prerequisite for VASP registration.

### IVMS101 — InterVASP Messaging Standard 101

**Industry practice**: Every major Travel Rule protocol (TRISA, TRP, VerifyVASP, CODE, Notabene) uses IVMS101 as its JSON payload. Jurisdiction-specific field differences are the hardest part of validator implementation.

## J

### JVCEA — Japan Virtual and Crypto Assets Exchange Association
Japanese self-regulatory body.

### JWG — Joint Working Group
The IVMS101 consensus group.

## K

### KCB — Korea Credit Bureau
Korean identity verification institution (본인확인기관).

### KISA — Korea Internet & Security Agency
Issuer of ISMS certification.

### KoFIU — Korea Financial Intelligence Unit
Korean FIU. Unit within the FSC.

### Korbit
Korean Big-4 exchange. Banking partner: Shinhan Bank. Travel Rule: CODE.

### KYC — Know Your Customer (고객확인)

**Industry practice**: A broad "knowing the customer" concept. Korean VASPs typically combine 본인확인기관 (PASS, NICE) + SDK vendors (such as ARGOS) + PEP screening.

### KYT — Know Your Transaction

**Industry practice**: Complements KYC rather than replacing it. KYT alone gives you "address risk"; STRs still need the "who" from KYC.

## L

### Lambda256
Dunamu subsidiary, operator of VerifyVASP.

### Layering
Second stage of money laundering — concealment.

### Lazarus Group
DPRK-sponsored cyber unit.

**Industry practice**: Stole USD 2.02B in 2025, cumulative USD 6.75B. Post-Bybit, "fake recruiting + insider threat" is the new HR-security frontline.

### LE — Law Enforcement

### LEI — Legal Entity Identifier

### Lido
Largest Ethereum liquid staking provider.

### Liveness Check
Live-person verification (vs photo or video replay).

### Liquid Staking
Staking that issues a liquid receipt token (Lido stETH, Rocket Pool rETH, etc.).

### LST — Liquid Staking Token
Lido and similar protocols.

### LRT — Liquid Restaking Token
EigenLayer and similar.

## M

### MAS — Monetary Authority of Singapore

### MEV — Maximal Extractable Value
Value extracted by reordering block transactions.

### MiCA — Markets in Crypto-Assets Regulation

**Industry practice**: Fully in force 2024-12-30; grandfathering ends 2026-07-01. EU passporting lets a single national license cover 27 member states.

### Mixer / Tumbler
Fund-mixing services.

### MLRO — Money Laundering Reporting Officer
UK/EU AML officer title.

### ML/TF — Money Laundering / Terrorism Financing

### Monero
Privacy-focused cryptocurrency. De-listed by major Korean and Japanese exchanges.

### MPC — Multi-Party Computation
Used in custody key management.

### MSB — Money Services Business
US registration category.

**Industry practice**: The usual US category for crypto firms. Requires FinCEN registration plus state-by-state Money Transmitter Licenses (MTLs) — a notoriously onerous 50-state process.

## N

### NCA — National Competent Authority
EU member-state supervisor.

### NICE
Korean credit bureau, operates identity verification (본인확인기관).

### NFT — Non-Fungible Token

### NIST — National Institute of Standards and Technology (US)

### Notabene
US Travel Rule gateway operator. Multi-protocol bridging (TRISA, TRP, VerifyVASP, CODE) and VASP directory, used by 1,500+ VASPs globally.

## O

### OCC — Office of the Comptroller of the Currency
US bank supervisor.

### OFAC — Office of Foreign Assets Control
US sanctions enforcement arm.

**Industry practice**: Secondary sanctions mean Korean VASPs must in practice comply with OFAC even without US customers — USD rails, stablecoins, and cloud providers all propagate exposure.

### OKX
Global exchange. Recent large US settlement (USD 504M).

### Onchain
Activity recorded on a public blockchain.

### OpenVASP
Distributed Travel Rule protocol. Low adoption in 2026.

### Originator
Sender (Travel Rule).

### OSINT — Open Source Intelligence

### OTC — Over-The-Counter

**Industry practice**: Concentrates large, cross-border, and special-customer flow — STR volume can rival a full exchange. Often underestimated, routinely flagged in inspections.

## P

### PASS
Korean mobile-based identity verification service (operated by Korean telcos).

### PATRIOT Act
US 2001 AML/CFT enhancement statute.

### Peel Chain
Laundering pattern that peels small amounts off a large balance.

**Industry practice**: Visually a straight chain in graph analytics. Detected by in-degree / out-degree signatures.

### PEP — Politically Exposed Person (정치적 주요인물)

**Industry practice**: Not an accusation. PEPs have structurally elevated corruption risk, so **automatic EDD** applies. Commercial databases like World-Check handle screening.

### PII — Personally Identifiable Information

### PIPA — Personal Information Protection Act (개인정보 보호법)

**Industry practice**: Travel Rule transmits PII between VASPs, which creates direct tension with PIPA. Cross-border transfer Privacy Impact Assessments must be run periodically.

### Placement
First stage of money laundering.

### Pool
Mining pool or staking pool, depending on context.

### PoR — Proof of Reserves
Reserve attestation for custodians.

### Privacy Coin
Anonymous cryptocurrencies (Monero, Zcash).

**Industry practice**: De-listed by Korean and Japanese major exchanges — the compliance burden outweighs the revenue.

## R

### R.15 / R.16
FATF Recommendations 15 and 16 (virtual assets, Travel Rule).

**Industry practice**: The direct parent of Korean Tukgeumbeop. Global regulatory shifts flow from revisions to these two recommendations.

### RBA — Risk-Based Approach (위험기반접근법)

**Industry practice**: Since FATF 2012, the operating principle for all AML duties. To credibly claim "we run RBA", a firm's policies must specify **Risk Score formulas, weights, and thresholds**.

### Ronin Bridge
Axie Infinity sidechain bridge. USD 624M hack in March 2022, attributed to Lazarus.

## S

### SAR — Suspicious Activity Report
US counterpart to STR.

### SDD — Simplified Due Diligence

**Industry practice**: Rarely used in the Korean crypto sector — supervisors treat "crypto = high risk" as a baseline assumption.

### SDN List — Specially Designated Nationals
US OFAC sanctions list.

**Industry practice**: The **only** sanctions list that explicitly publishes **cryptocurrency wallet addresses**. SDN.XML uses `<feature><type>Digital Currency Address</type>`.

### SEC — Securities and Exchange Commission (US)

### SFC — Securities and Futures Commission (Hong Kong)

### Sanctions
Financial and trade restrictions imposed by governments or multilateral bodies.

### Smurfing / Structuring
Breaking up deposits to evade KYC or reporting thresholds.

### Staking
Locking tokens to secure a Proof-of-Stake network in exchange for yield.

### Stablecoin
A crypto-asset designed to maintain a stable value, usually pegged to fiat (USDC, USDT) or assets.

### STR — Suspicious Transaction Report (의심거래보고)

**Industry practice**: No amount threshold — suspicion alone triggers the report. Supervisors are actually **more** suspicious of firms filing few STRs. Tipping off the customer is a separate offense.

### Sumsub
Global KYC vendor headquartered in the UK.

### Sunrise Issue
Travel Rule inconsistency across jurisdictions.

**Industry practice**: The reason Notabene Gateway became the global leader. Full resolution is not expected before the FATF 2030 deadline, so fallback policies are mandatory.

## T

### TF — Terrorism Financing

### TFR — Transfer of Funds Regulation
EU Travel Rule.

**Industry practice**: Threshold is **zero** — every transfer in scope. The strictest regime in the world, and therefore the baseline for global VASP design.

### Tipping-off
Informing a customer that an STR has been filed. Prohibited.

**Industry practice**: Tukgeumbeop §9 — up to one year in prison or KRW 10M fine. When explaining an account closure, use generic language like "pursuant to internal policy".

### TM — Transaction Monitoring

### Tornado Cash
Ethereum mixer. OFAC-sanctioned 2022-08 → 5th Circuit ruling in Van Loon v. Treasury 2024-11 → delisted 2025-03-21.

**Industry practice**: De-listed but still in the **high-risk** category across the industry. "Legally permitted" does not equal "operationally permitted".

### TraderTraitor
FBI-designated Lazarus sub-cluster. Uses fake-recruitment tradecraft.

### Travel Rule
FATF R.16 obligation to transmit originator and beneficiary information with a VA transfer.

### TRISA
Distributed Travel Rule protocol. Started at CipherTrace (acquired by Mastercard).

### TRP — Travel Rule Protocol
REST-based Travel Rule protocol.

### TRM Labs
US blockchain analytics company. Strong in cross-chain and real-time analytics.

### Tukgeumbeop (特金法, 특금법)
Short name for 특정 금융거래정보의 보고 및 이용 등에 관한 법률 (Act on Reporting and Using Specified Financial Transaction Information). Korea's primary AML statute.

## U

### UBO — Ultimate Beneficial Owner

### UNODC — UN Office on Drugs and Crime

### Unhosted Wallet
Personal wallet outside any VASP.

**Industry practice**: Korean Big-4 exchanges run an **external-wallet registration regime**. Proof of wallet ownership (Satoshi Test or signed message) is required before withdrawal.

### Upbit
Largest Korean exchange (Dunamu). Banking partner: K-Bank. Travel Rule: VerifyVASP.

### USAPA — USA PATRIOT Act

### USDC
Regulated US dollar stablecoin, issued by Circle.

### USDT
Tether-issued US dollar stablecoin. Largest stablecoin by market cap.

### UTXO — Unspent Transaction Output
Bitcoin transaction model.

## V

### VA — Virtual Asset (가상자산)

### VARA — Virtual Assets Regulatory Authority (Dubai)

### VASP — Virtual Asset Service Provider (가상자산사업자)

**Industry practice**: Not only exchanges — also custodians, OTC desks, and brokers. The five activities in Tukgeumbeop §2.1.ha are the reference test.

### VAUPA — Virtual Asset User Protection Act (가상자산 이용자 보호 등에 관한 법률)
Effective 2024-07-19. User-asset segregation, market manipulation prohibition, insurance.

### VerifyVASP
Korean Travel Rule solution (Lambda256 + Chainalysis). Upbit is the anchor member.

## W

### Wash Trading
Artificial trades to inflate price or volume.

**Industry practice**: Especially prevalent in NFTs — Chainalysis estimated 25-50% of the 2022-2023 NFT market was wash trading.

### Wolfsberg Group
Industry body of global banks on AML good-practice standards (HSBC, Citi, JPMorgan, and others).

## Z

### Zcash
Privacy coin using zk-SNARKs.

### ZKP — Zero-Knowledge Proof

**Industry practice**: The long-run path to reconciling privacy with compliance. zk-KYC, Polygon ID, and Worldcoin are early real-world attempts.

### zk-SNARK
A specific zero-knowledge proof construction (used by Tornado Cash, Zcash).

---

## Frequently Confused Pairs

### 고객확인 vs 실명확인 vs KYC

| Term | Source | Meaning |
|---|---|---|
| **고객확인 (Customer Verification)** | Tukgeumbeop §5-2 | Statutory umbrella term covering identity, BO, purpose, and SoF verification. Broad. |
| **실명확인 (Real-Name Verification)** | 금융실명법 / Tukgeumbeop §5-2 ① | A **subset of 고객확인** — only confirms identity through an ID document or a 본인확인기관 (PASS/NICE). Narrower. |
| **KYC** | FATF / global | International term, roughly equivalent to 고객확인 but with country-specific detail differences. |
| **CDD** | FATF R.10 | Formal legal phrasing — the "official" KYC in regulatory texts. |

### STR vs SAR

| Term | Jurisdiction | Meaning |
|---|---|---|
| **STR** | FATF, Korea, EU, Singapore | Suspicious transaction report. Korean basis: Tukgeumbeop §5-3. |
| **SAR** | US (FinCEN) | Suspicious activity report. BSA 31 CFR 1020.320. Can be filed on suspicious activity even without a completed transaction — broader. |

### Travel Rule vs Wire Transfer Rule

| Term | Context |
|---|---|
| **Travel Rule** | FATF R.16 for virtual assets. 2019+. |
| **Wire Transfer Rule** | Traditional wire transfers under BSA. 1996+. The ancestor of Travel Rule. |

### AMLO vs MLRO vs Compliance Officer

| Term | Jurisdiction |
|---|---|
| **AMLO** | Korea, global general use |
| **MLRO** | UK/EU tradition |
| **Compliance Officer (CO)** | Broad compliance role (may include or be distinct from AML) |
| **CCO** | C-level executive |

### Tipping-off vs Disclosure

| Term | Meaning |
|---|---|
| **Tipping-off** | Revealing an STR to the customer. Prohibited under Tukgeumbeop §5-2 ⑤ — up to 5 years imprisonment. |
| **Disclosure** | Generic disclosure. Tipping-off is a specifically prohibited form. |

### PEP vs BO

| Term | Meaning |
|---|---|
| **PEP** | Politically exposed person. Senior officials, family, close associates. Elevated corruption risk. |
| **BO** | Ultimate beneficial owner. Natural-person owner of a legal entity (typically 25%+). |

---

## Korean to English Quick Reference

| Korean | English |
|---|---|
| 자금세탁방지 | Anti-Money Laundering (AML) |
| 테러자금조달방지 | CFT |
| 고객확인 | KYC |
| 고객실사 | CDD |
| 강화된 고객실사 | EDD |
| 의심거래보고 | STR |
| 고액현금거래보고 | CTR |
| 가상자산사업자 | VASP |
| 실소유자 | Beneficial Owner |
| 정치적 주요인물 | PEP |
| 위험기반접근법 | RBA |
| 자금세탁방지 보고책임자 | AMLO |
| 금융정보분석원 | FIU (KoFIU) |
| 특금법 | Tukgeumbeop / Specified Financial Information Act |
| 가상자산이용자보호법 | Virtual Asset User Protection Act (VAUPA) |
| 트래블룰 | Travel Rule |
| 외부지갑 등록 | Unhosted Wallet Registration |
| 콜드월렛 | Cold Wallet |
| 분리보관 | Segregated Storage |
| 시세조종 | Market Manipulation |
| 미공개정보이용 | Insider Trading |
| 부정거래 | Fraudulent Practices |
| 제재 | Sanctions |
| 자산동결 | Asset Freeze |
| 본인확인기관 | Identity Verification Institution |
| 실명계좌 | Real-Name Bank Account |

---

## Top 15 Terms for Newcomers

If AML is new to you, memorize these 15 first — the rest will come naturally in context.

1. **AML / CFT** — the pair
2. **KYC / KYT** — people vs transactions
3. **CDD / EDD** — standard vs enhanced
4. **STR** — suspicious transaction report
5. **VASP** — virtual asset service provider
6. **FATF / FIU** — international standard vs Korean enforcement
7. **Tukgeumbeop / VAUPA** — Korea's two crypto AML statutes
8. **Travel Rule / IVMS101** — originator and beneficiary information
9. **OFAC / SDN** — US sanctions
10. **PEP** — politically exposed person
11. **RBA** — risk-based approach
12. **AMLO** — AML officer
13. **Mixer / Tornado Cash** — anonymization tools
14. **Lazarus / DPRK** — top-tier threat actor
15. **Tipping-off** — never do this

---

## Further Reading

- [`../notes/glossary.md`](../notes/glossary.md) — Original Korean glossary, with more 💡 Industry notes
- [`korea-aml-overview.md`](korea-aml-overview.md) — Korean AML framework overview
- [`regulatory-comparison.md`](regulatory-comparison.md) — Korea vs US, EU, Asia
