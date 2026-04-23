# Hacker News Show HN Draft

> **Target**: HN front page engineer audience — compliance-curious technologists, RegTech engineers
> **Tone**: Engineer-focused, low-marketing, "what I built and why" register
> **Format**: Show HN submission + detailed self-comment

---

## Pre-post Checklist

- [ ] Repo README must be complete, scannable
- [ ] CONTRIBUTING.md polished — HN readers will click it
- [ ] License (CC BY 4.0) in LICENSE file, obvious
- [ ] Demo-like "quick read" entry point (Day 01 note recommended)
- [ ] Submit Tue-Thu 8-10am EST (lowest noise window)
- [ ] Have 30 min free post-submission for real-time comment reply

---

## Submission

**Title** (HN rules: 80-char max, no clickbait, no emoji):

Show HN: A 22,000-line open-source AML textbook for virtual assets (CC BY 4.0)

**URL**: https://github.com/lala-david/aml-notes

---

## Self-comment (post immediately after submission)

Hi HN — I built this over the last several months and would love engineering-
minded review.

**Context**: I wanted a single reference that connected (a) the actual text of
anti-money-laundering statutes, (b) how supervisors actually inspect firms
against them, and (c) how engineers would implement detection. Most AML
material covers only one layer. This tries to cover all three.

**What's there**:

- 60-day daily curriculum (1 note per day)
- 29 topic deep-dives (Korea SFTIA/VAUPA, EU MiCA, US FinCEN, FATF R.16)
- 1,200-line 4-week supervisory inspection response workbook
- Technical sections engineers might care about:
  - Exposure Score formula decomposition (Chainalysis-style + honest caveats
    on assumption fragility)
  - CIOH (Common Input Ownership Heuristic) walk-through with false-positive
    case studies
  - IVMS101 Travel Rule validator notes
  - KYT rule library (pseudocode, not runnable code yet)

**What it isn't**: it's not runnable software. It's prose + tables + diagrams
and a small number of pseudo-code blocks. If you were hoping for a binary,
not here yet (that's a separate repo I'll ship).

**Honest limitations**:

- Korean-first; English edition is partial
- I am one person. Expert review is thin. That's what I'm asking for.
- Anything date-sensitive (sanctions lists, enforcement cases) will age fast.
  See `meta/regulatory-watch.md` for the tracking plan.

**Tech stack of the repo itself**:

- Plain Markdown + Mermaid for diagrams
- Python scripts for link checking, URL health, print-to-PDF
- GitHub Actions for CI on link + lint
- No JS, no static site generator — intentional; portability matters more than pretty

**What I'd actually appreciate**:

1. Engineers who've shipped KYT / sanctions screening systems: does the rule
   library match your reality? False-positive rate ballpark?
2. Anyone outside Korea: does the jurisdictional comparison hold for yours?
3. OSS maintainers: is the CONTRIBUTING + GOVERNANCE structure reasonable for
   a docs-heavy repo?

License is CC BY 4.0 — use it in your team onboarding if useful, attribution
is all I ask.

Thanks for reading.

---

## Comment Reply Templates

**"Why Korean-first?"**:
> Because that's my jurisdiction and where I saw the gap clearest. The English edition is being written in parallel. Parts not yet translated are marked.

**"Isn't this just a wiki?"**:
> Fair — it's prose + tables, not code. I called it a textbook intentionally. The value is editorial: opinionated paths through dense statutes, not just a link dump.

**"How do you keep it current?"**:
> `meta/regulatory-watch.md` tracks a monthly review cadence. Quarterly major updates. I don't pretend this is current day-to-day — it's current to a stated revision date.

**"Travel Rule IVMS101 — any code?"**:
> Validator pseudocode and schema walk-through; no runnable validator yet. Happy to promote this if someone wants to contribute.

**Critical / dismissive**:
> That's fair. [Specific concrete response]. If you want to make the criticism concrete via an Issue, I'll prioritize the fix.

---

## Metrics (24h / 72h)

- Front page? (yes/no)
- Upvotes at 1h / 6h / 24h
- Comment count
- GitHub Star delta (pre- vs post-submission)
- New Issues / PRs within 7 days
- Other HN user referrals (posts citing the repo)

---

## Failure Mode Plan

If submission dies without engagement:
- Do NOT resubmit within 30 days (HN policy / shadow ban risk)
- Revisit title + first-comment clarity
- Consider targeted HN user outreach via Ask HN on a narrower question instead

If submission gets flagged:
- Check HN guidelines carefully
- If it's a genuine flag, accept it. If mistaken, email hn@ycombinator.com politely
