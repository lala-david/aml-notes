#!/usr/bin/env python3
"""
AML Notes — Chart Generator
=============================
Generates seaborn/matplotlib static charts used across notes & print packets.
Outputs PNG (300dpi) + SVG to charts/output/.

Run:
    pip install matplotlib seaborn pandas
    python charts/generate.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

# ========================= Shared Style =========================
# Tasteful, print-friendly palette. Charcoal navy accent matches print.css.

INK = "#111418"
INK_SOFT = "#3a414a"
INK_MUTE = "#6b7280"
ACCENT = "#1a2e4a"
RULE = "#d8dbe0"
PALETTE = ["#1a2e4a", "#4a5f7e", "#7e8ba4", "#c9a646", "#8c6b2f", "#6b7280"]

# Register all Korean fonts found on system
from matplotlib import font_manager as fm

_ko_keywords = ("pretendard", "malgun", "applesd", "notosans", "notosanskr", "notosanscjkkr")
for _f in fm.findSystemFonts():
    _stem = Path(_f).stem.lower()
    if any(k in _stem for k in _ko_keywords):
        try:
            fm.fontManager.addfont(_f)
        except Exception:
            pass

# Pick first available from preference list (prefer Malgun Gothic on Windows — always works)
_available = {f.name for f in fm.fontManager.ttflist}
_ko_font = None
for _candidate in ["Malgun Gothic",
                    "Pretendard", "Pretendard Variable",
                    "Apple SD Gothic Neo", "Noto Sans KR",
                    "NanumGothic", "AppleGothic"]:
    if _candidate in _available:
        _ko_font = _candidate
        break
if _ko_font is None:
    _ko_font = "DejaVu Sans"
    print(f"[WARN] No Korean font found; Korean text may render as tofu.",
          file=sys.stderr)
else:
    print(f"[INFO] Using Korean font: {_ko_font}", file=sys.stderr)

# Force the Korean font as the primary family — also on sans-serif AND serif
# lists so weighted/italic variants don't fall back to a glyph-less font.
plt.rcParams["font.family"] = _ko_font
plt.rcParams["font.sans-serif"] = [_ko_font, "DejaVu Sans"]
plt.rcParams["font.serif"] = [_ko_font, "DejaVu Serif"]
plt.rcParams["font.monospace"] = [_ko_font, "Consolas", "DejaVu Sans Mono"]
# Disable auto-fallback to glyph-less Latin fonts
plt.rcParams["axes.unicode_minus"] = False

# Apply seaborn style FIRST, then override with our fonts — seaborn.set_style
# resets font params otherwise.
sns.set_style("ticks")

plt.rcParams.update({
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "xtick.color": INK_SOFT,
    "ytick.color": INK_SOFT,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titleweight": "bold",
    "axes.titlesize": 14,
    "axes.labelsize": 10,
    "axes.labelweight": "normal",
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "legend.frameon": False,
    "axes.unicode_minus": False,
    "font.size": 10,
    "figure.dpi": 110,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.25,
    # Re-apply Korean font after sns.set_style may have reset it
    "font.family": _ko_font,
    "font.sans-serif": [_ko_font, "DejaVu Sans"],
})


def savefig(fig, name: str):
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  -> {name}.png + .svg")


# ========================= Chart 6: Travel Rule Thresholds =========================

def chart_travel_rule_thresholds():
    """관할별 Travel Rule 금액 기준 — 의무 발동형(A) vs 정보 심화형(B)

    한 축에 "임계금액"을 늘어놓으면 대부분의 관할이 틀린다. 금액이 의무를
    발동시키는 관할(미국·한국)과, 의무는 전건이고 금액은 넘겨야 할 정보
    항목만 늘리는 관할(EU·영국·일본·홍콩·싱가포르)은 성격이 다르기 때문이다.
    두 패널로 분리해 그 차이를 그림 자체가 말하게 한다.
    """
    # A형 — 이 금액 미만은 Travel Rule 대상이 아니다
    a_type = pd.DataFrame({
        "juris":  ["한국",        "미국 (BSA)"],
        "usd":    [770,           3000],
        "native": ["₩1,000,000 · 2027-02-18 까지", "$3,000"],
    })
    # B형 — 금액과 무관하게 전건 의무. 아래 금액은 정보 항목이 늘어나는 지점.
    b_type = pd.DataFrame({
        "juris":  ["일본",   "EU (TFR)", "영국",  "홍콩",      "싱가포르"],
        "usd":    [0,        0,          1010,    1020,        1130],
        # 영국: 2023-09-01~2026-06-29 은 €1,000, 2026-06-30 부터 £800 (S.I. 2026/621)
        "native": ["해당 없음", "해당 없음",  "£800 · 2026-06-30~",  "HK$8,000",  "S$1,500"],
    })

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(9.2, 6.4), gridspec_kw={"height_ratios": [2, 5]}
    )

    def draw(ax, data, color, note_zero):
        y = range(len(data))
        bars = ax.barh(y, data["usd"], color=color, edgecolor=INK,
                       linewidth=0.6, height=0.58)
        for bar, native, usd in zip(bars, data["native"], data["usd"]):
            if usd == 0:
                ax.text(60, bar.get_y() + bar.get_height() / 2, note_zero,
                        va="center", ha="left", fontsize=9,
                        color=INK_MUTE, style="italic")
            else:
                ax.text(bar.get_width() + 80, bar.get_y() + bar.get_height() / 2,
                        native, va="center", ha="left", fontsize=9.5,
                        color=INK, fontweight="bold")
        ax.set_yticks(y)
        ax.set_yticklabels(data["juris"], fontsize=10)
        ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${int(x):,}"))
        ax.set_xlim(0, 4000)
        ax.tick_params(axis="y", length=0)
        ax.grid(axis="x", linewidth=0.5, color=RULE)
        ax.set_axisbelow(True)

    draw(ax1, a_type, ACCENT, "")
    ax1.set_title("A형 · 금액이 의무를 발동시킨다 — 이 미만은 대상 아님",
                  loc="left", pad=10, fontsize=11)
    ax1.set_xticklabels([])

    draw(ax2, b_type, PALETTE[2], "정보 심화 기준 없음")
    ax2.set_title("B형 · 금액과 무관하게 전건 의무 — 금액은 정보 항목만 늘린다",
                  loc="left", pad=10, fontsize=11)
    ax2.set_xlabel("USD 환산")

    fig.suptitle("Travel Rule 의 금액 기준은 두 종류다", x=0.01, ha="left",
                 fontsize=13, fontweight="bold")

    fig.text(0.01, -0.02,
             "Source: 31 CFR 1010.410(f) · 특금법 시행령 §10의10 · EU TFR 2023/1113 art.14 · "
             "MLR 2017 reg 64C · 범수법 제10조의5 · AMLO Sch.2 s.13A · MAS PSN02 ¶13 — 기준일 2026-10-21\n"
             "한국은 대통령령 제36592호로 2027-02-19 부터 기준금액 없이 전건 적용(B형 전환, enacted-not-in-force). "
             "일본 10만엔은 CDD 기준이며 Travel Rule 기준이 아니다.",
             fontsize=7.5, color=INK_MUTE, ha="left")
    savefig(fig, "travel_rule_thresholds")


# ========================= Chart 7: FATF Grey/Black Heatmap =========================

def chart_fatf_watchlist():
    """FATF 2026 Grey/Black 국가 목록 시각화 (categorical strip)"""
    black = ["북한", "이란", "미얀마"]
    # 2026-06-19 총회 결과 22개 (BiH·이라크 편입, 알제리·나미비아 졸업).
    # 10월 총회(2026-10-28~30)는 기준일 2026-10-21 에 아직 열리지 않았다.
    grey = ["앙골라", "볼리비아", "보스니아\n헤르체고비나", "불가리아", "카메룬", "코트디부아르",
            "콩고민주공화국", "아이티", "이라크", "케냐", "쿠웨이트", "라오스",
            "레바논", "모나코", "네팔", "파푸아뉴기니", "남수단", "시리아",
            "베네수엘라", "베트남", "영국령\n버진아일랜드", "예멘"]

    fig, ax = plt.subplots(figsize=(10, 5.2))

    # Y positions
    y_black = 1.0
    y_grey = 0.0

    # Black list
    for i, country in enumerate(black):
        x = i * 2.4
        ax.add_patch(plt.Rectangle(
            (x - 0.9, y_black - 0.32), 1.8, 0.64,
            facecolor="#fee2e2", edgecolor="#dc2626", linewidth=1.2,
        ))
        ax.text(x, y_black, country, ha="center", va="center",
                fontsize=11, fontweight="bold", color="#991b1b")

    # Grey list (two rows)
    for i, country in enumerate(grey):
        col = i % 6
        row = i // 6
        x = col * 2.1 + 0.5
        y = y_grey - row * 0.7
        ax.add_patch(plt.Rectangle(
            (x - 0.95, y - 0.28), 1.9, 0.56,
            facecolor="#fff7d6", edgecolor="#c9a646", linewidth=1.0,
        ))
        ax.text(x, y, country, ha="center", va="center",
                fontsize=8, color="#78572d")

    # Labels
    ax.text(-1.5, y_black, "Black\n(High-Risk)",
            ha="right", va="center",
            fontsize=10, fontweight="bold", color="#991b1b",
            bbox=dict(facecolor="white", edgecolor="#dc2626", boxstyle="round,pad=0.4"))
    ax.text(-1.5, y_grey - 0.35, "Grey\n(Increased\nMonitoring)",
            ha="right", va="center",
            fontsize=10, fontweight="bold", color="#78572d",
            bbox=dict(facecolor="white", edgecolor="#c9a646", boxstyle="round,pad=0.4"))

    ax.set_xlim(-3.6, 12.5)
    ax.set_ylim(-2.9, 1.8)
    ax.axis("off")
    ax.set_title("FATF High-Risk · Grey List — 2026-06-19 총회 기준", loc="left", pad=14,
                 fontsize=14, fontweight="bold", color=INK)

    fig.text(0.01, 0.02, "Source: FATF Outcomes of the Plenary, 19 June 2026 (흑색 3 · 회색 22). "
             "회색 22개 명칭은 2차 출처로 재구성, 개수·변동은 FATF 원문과 일치. 다음 갱신 2026-10-30 예정.",
             fontsize=7.5, color=INK_MUTE, ha="left")
    savefig(fig, "fatf_watchlist")


# ========================= Chart 8: Vertical Regulation Timeline =========================

def chart_regulation_timeline():
    """2019~2030 주요 가상자산 AML 규제 타임라인 (세로형)

    reports/가상자산 AML KYT FDS 트래블룰 흐름.md 의 연대기 표(원문 확인분)에서만 뽑는다.
    y 값은 연도 + (월/12). 표에 없는 사건은 넣지 않는다.
    """
    events = [
        (2019.455, "2019-06", "FATF INR.15 §7(b) — 가상자산 트래블룰", "FATF", "#c9a646"),
        (2020.702, "2020-09-14", "FATF Red Flag Indicators", "FATF", "#c9a646"),
        (2021.824, "2021-10-28", "FATF 개정 RBA 가이던스", "FATF", "#c9a646"),
        (2022.232, "2022-03-25", "한국 트래블룰 시행 (100만원 이상)", "KR", ACCENT),
        (2023.417, "2023-06-01", "일본·홍콩 트래블룰 시행", "JP·HK", "#5b7a5b"),
        (2023.667, "2023-09-01", "영국 트래블룰 시행 (€1,000)", "GB", "#6b5b7a"),
        (2024.549, "2024-07-19", "한국 이용자보호법 시행 (§12 감시)", "KR", ACCENT),
        (2024.996, "2024-12-30", "EU TFR·MiCA 적용", "EU", "#4a5f7e"),
        (2025.221, "2025-03-21", "OFAC Tornado Cash 제재 해제", "US", "#8c6b2f"),
        (2025.455, "2025-06", "FATF R.16 개정", "FATF", "#c9a646"),
        (2025.547, "2025-07-18", "미국 GENIUS Act 서명", "US", "#8c6b2f"),
        (2026.0, "2026-01-01", "EU AML 권한 EBA → AMLA", "EU", "#4a5f7e"),
        (2026.496, "2026-06-30", "영국 £800 기준 (S.I. 2026/621)", "GB", "#6b5b7a"),
        (2026.541, "2026-07-16", "FATF 7차 Targeted Update", "FATF", "#c9a646"),
        (2026.635, "2026-08-20", "한국 특금법 제21358호 시행", "KR", ACCENT),
        (2026.764, "2026-10-06", "미국 믹싱·비수탁지갑 NPRM 철회", "US", "#8c6b2f"),
        (2027.133, "2027-02-19", "한국 트래블룰 전건 적용", "KR", ACCENT),
        (2027.525, "2027-07-10", "EU AMLR 적용", "EU", "#4a5f7e"),
        (2030.999, "2030-12-31", "개정 R.16 이행 기대시한", "FATF", "#c9a646"),
    ]
    today_date = 2026.81  # 2026-10-21
    # 날짜 간격대로 놓으면 2025~2026 사건이 겹친다 → 순서대로 등간격 배치,
    # 기준일 선은 기준일 직전·직후 사건 사이에 긋는다.
    n_past = sum(1 for e in events if e[0] <= today_date)
    events = [(i, *e[1:]) for i, e in enumerate(events)]
    today = n_past - 0.5

    fig, ax = plt.subplots(figsize=(8.4, 11))
    # Vertical timeline spine
    ax.plot([0.5, 0.5], [-0.6, len(events) - 0.4], color=INK, linewidth=1.4, zorder=1)

    for y, date_str, label, flag, color in events:
        is_past = y <= today
        marker_color = color if not is_past else color
        marker_face = "white" if not is_past else color
        # Circle marker
        ax.scatter(0.5, y, s=130, zorder=3,
                   facecolor=marker_face, edgecolor=color, linewidth=1.8)
        # Year label
        ax.text(0.35, y, date_str,
                ha="right", va="center",
                fontsize=9, color=INK_MUTE, fontfamily="monospace")
        # Flag tag (colored pill)
        ax.text(0.62, y, flag,
                ha="left", va="center",
                fontsize=8, color="white",
                fontweight="bold",
                bbox=dict(facecolor=color, edgecolor=color,
                          boxstyle="round,pad=0.25"))
        # Event text
        ax.text(0.82, y, label,
                ha="left", va="center",
                fontsize=10, color=INK,
                fontweight="bold" if not is_past else "normal",
                alpha=1.0 if not is_past else 0.78)

    # Today marker
    ax.axhline(today, xmin=0.05, xmax=0.95, color="#c9a646",
               linestyle="--", linewidth=1.1, alpha=0.7, zorder=2)
    ax.text(0.98, today, "  ← 기준일 (2026-10-21)",
            ha="left", va="center",
            fontsize=9, color="#8c6b2f", fontweight="bold")

    ax.set_ylim(len(events) - 0.2, -0.9)  # inverted: 과거가 위
    ax.set_xlim(-0.5, 1.7)
    ax.axis("off")
    ax.set_title("가상자산 AML 규제 타임라인 (2019~2030)",
                 loc="left", pad=20, x=-0.06,
                 fontsize=14, fontweight="bold", color=INK)

    fig.text(0.5, 0.01, "KR 한국 · US 미국 · EU · FATF",
             fontsize=9, color=INK_MUTE, ha="center")
    savefig(fig, "regulation_timeline")


# ========================= Main =========================

CHARTS = [
    ("Travel Rule Thresholds", chart_travel_rule_thresholds),
    ("FATF Grey/Black Watchlist", chart_fatf_watchlist),
    ("Regulation Timeline 2019-2030", chart_regulation_timeline),
]


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(f"Generating {len(CHARTS)} charts -> {OUT}\n")
    for name, fn in CHARTS:
        print(f"[*] {name}")
        fn()
    print(f"\nDone. {len(CHARTS)} charts x 2 formats = {len(CHARTS)*2} files.")


if __name__ == "__main__":
    main()
