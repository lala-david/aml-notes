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
_ko_keywords = ("pretendard", "malgun", "applesd", "notosans", "gothic", "batang")
for _f in fm.findSystemFonts():
    _name = Path(_f).stem.lower()
    if any(k in _name for k in _ko_keywords):
        try:
            fm.fontManager.addfont(_f)
        except Exception:
            pass

# Pick first available from preference list
_available = {f.name for f in fm.fontManager.ttflist}
_ko_font = None
for _candidate in ["Pretendard", "Pretendard Variable", "Malgun Gothic",
                    "Apple SD Gothic Neo", "Noto Sans KR", "AppleSDGothicNeoR00"]:
    if _candidate in _available:
        _ko_font = _candidate
        break
if _ko_font is None:
    _ko_font = "DejaVu Sans"

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [_ko_font, "DejaVu Sans", "Arial"]

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
})

sns.set_style("ticks")


def savefig(fig, name: str):
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  -> {name}.png + .svg")


# ========================= Chart 1: Lazarus Yearly =========================

def chart_lazarus_yearly():
    """DPRK·Lazarus 연도별 가상자산 탈취 금액 (2017~2025)"""
    data = pd.DataFrame({
        "year": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
        "usd_m": [82, 570, 50, 280, 400, 1650, 1700, 800, 2020],  # 주요 사건 기준 추정
    })

    fig, ax = plt.subplots(figsize=(8.8, 4.4))
    bars = ax.bar(
        data["year"].astype(str),
        data["usd_m"] / 1000,  # to Billion
        color=[ACCENT if y != 2025 else "#c9a646" for y in data["year"]],
        edgecolor=INK, linewidth=0.6, width=0.68,
    )

    # Highlight 2025
    for bar, year in zip(bars, data["year"]):
        if year == 2025:
            ax.annotate(
                "Bybit + 다수\n$2.02B",
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 6), textcoords="offset points",
                ha="center", va="bottom",
                fontsize=9, fontweight="bold", color="#8c6b2f",
            )
        else:
            ax.annotate(
                f"${data.loc[data['year']==year, 'usd_m'].values[0]}M",
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 3), textcoords="offset points",
                ha="center", va="bottom",
                fontsize=8, color=INK_SOFT,
            )

    ax.set_title("DPRK · Lazarus 연도별 가상자산 탈취", loc="left", pad=14)
    ax.set_xlabel("")
    ax.set_ylabel("탈취 금액 (USD Billion)")
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('$%.1fB'))
    ax.set_ylim(0, data["usd_m"].max() / 1000 * 1.25)
    ax.tick_params(axis="x", length=0)
    ax.grid(axis="y", linewidth=0.5, color=RULE)
    ax.set_axisbelow(True)

    fig.text(0.01, -0.02, "Source: Chainalysis · TRM Labs · UN Panel of Experts (~2025)",
             fontsize=7.5, color=INK_MUTE, ha="left")
    savefig(fig, "lazarus_yearly")


# ========================= Chart 2: Enforcement Fines (log) =========================

def chart_enforcement_fines():
    """주요 가상자산 AML enforcement 벌금 궤적 (로그스케일)"""
    data = pd.DataFrame({
        "case":   ["BitGo\n(2021)", "Bittrex\n(2022)", "Paxful\n(2025)", "OKX\n(2025)", "Binance\n(2023)"],
        "fine":   [98e3,            29e6,              3.5e6,            500e6,          4.3e9],
        "color":  [INK_MUTE,        "#7e8ba4",         "#4a5f7e",        "#c9a646",      ACCENT],
    })

    fig, ax = plt.subplots(figsize=(8.8, 4.4))
    bars = ax.bar(data["case"], data["fine"], color=data["color"],
                  edgecolor=INK, linewidth=0.6, width=0.62)

    ax.set_yscale("log")
    ax.set_ylim(1e4, 2e10)

    for bar, fine in zip(bars, data["fine"]):
        if fine >= 1e9:
            label = f"${fine/1e9:.1f}B"
        elif fine >= 1e6:
            label = f"${fine/1e6:.0f}M"
        else:
            label = f"${fine/1e3:.0f}K"
        ax.annotate(label,
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 4), textcoords="offset points",
                    ha="center", va="bottom",
                    fontsize=10, fontweight="bold", color=INK)

    ax.set_title("가상자산 AML 벌금 궤적 — 5년 만에 $98K → $4.3B", loc="left", pad=14)
    ax.set_xlabel("")
    ax.set_ylabel("벌금 (USD, 로그스케일)")

    ax.yaxis.set_major_formatter(mtick.FuncFormatter(
        lambda x, pos: f"${x/1e9:.0f}B" if x >= 1e9 else
                       f"${x/1e6:.0f}M" if x >= 1e6 else
                       f"${x/1e3:.0f}K"
    ))
    ax.tick_params(axis="x", length=0, pad=4)
    ax.grid(axis="y", linewidth=0.5, color=RULE, which="both")
    ax.set_axisbelow(True)

    fig.text(0.01, -0.04, "Source: DOJ · FinCEN · OFAC press releases",
             fontsize=7.5, color=INK_MUTE, ha="left")
    savefig(fig, "enforcement_fines")


# ========================= Chart 3: Illicit Asset Share (donut) =========================

def chart_illicit_asset_share():
    """2025년 불법 거래 자산 비중 — 스테이블코인 84% 등"""
    labels = ["Stablecoin\n(USDT · USDC)", "BTC", "ETH", "Altcoin · Privacy"]
    values = [84, 7, 5, 4]
    colors = [ACCENT, "#4a5f7e", "#7e8ba4", "#c9a646"]

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        colors=colors,
        startangle=90,
        wedgeprops=dict(width=0.38, edgecolor="white", linewidth=2),
        autopct=lambda pct: f"{pct:.0f}%",
        pctdistance=0.82,
        textprops=dict(fontsize=10, color=INK),
    )

    for i, at in enumerate(autotexts):
        at.set_color("white" if i == 0 else INK)
        at.set_fontweight("bold")
        at.set_fontsize(11 if i == 0 else 9)

    # Center text
    ax.text(0, 0.08, "2025", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)
    ax.text(0, -0.12, "Illicit\nCrypto", ha="center", va="center",
            fontsize=9, color=INK_SOFT)

    ax.set_title("불법 가상자산 거래 자산별 비중 — 스테이블코인 84%", loc="center", pad=14)

    fig.text(0.5, 0.01, "Source: Chainalysis Crypto Crime Report 2026",
             fontsize=7.5, color=INK_MUTE, ha="center")
    savefig(fig, "illicit_asset_share")


# ========================= Chart 4: VASP Obligation Radar =========================

def chart_vasp_obligations_radar():
    """사업 유형별 VASP 의무 강도 비교 (RBA)"""
    categories = ["KYC", "KYT", "Travel\nRule", "제재\n스크리닝", "자산\n분리보관", "STR"]
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    # 0=없음, 1=약, 2=중, 3=강
    scenarios = {
        "거래소":      [3, 3, 3, 3, 3, 3],
        "수탁업":      [3, 2, 2, 2, 3, 2],
        "OTC desk":   [3, 2, 3, 2, 1, 3],
        "NFT 마켓":    [2, 2, 1, 2, 1, 2],
    }
    colors = {"거래소": ACCENT, "수탁업": "#c9a646", "OTC desk": "#4a5f7e", "NFT 마켓": "#7e8ba4"}

    fig, ax = plt.subplots(figsize=(7.2, 6.4), subplot_kw=dict(polar=True))

    for name, values in scenarios.items():
        vals = values + values[:1]
        ax.plot(angles, vals, color=colors[name], linewidth=1.8, label=name)
        ax.fill(angles, vals, color=colors[name], alpha=0.12)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9.5, color=INK)
    ax.set_rlabel_position(90)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["약", "중", "강"], fontsize=8, color=INK_MUTE)
    ax.set_ylim(0, 3.2)

    ax.spines["polar"].set_color(RULE)
    ax.grid(color=RULE, linewidth=0.6)
    ax.set_title("사업 유형별 VASP 의무 강도 (RBA)", pad=26)

    ax.legend(loc="upper right", bbox_to_anchor=(1.22, 1.08),
              frameon=False, fontsize=9)

    fig.text(0.5, 0.02, "Source: 특금법 §2 · §5의2~§5의4 + 가상자산이용자보호법 §10",
             fontsize=7.5, color=INK_MUTE, ha="center")
    savefig(fig, "vasp_obligations_radar")


# ========================= Chart 5: 2025 Trend Summary =========================

def chart_trend_2025():
    """2025 주요 통계 카드형 인포그래픽"""
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.2))

    stats = [
        ("$154B", "2025 불법 거래", "+162% YoY", ACCENT),
        ("84%", "스테이블코인 비중", "USDT 우세", "#c9a646"),
        ("$2.02B", "DPRK 탈취", "+51% YoY", "#4a5f7e"),
        ("$16.1B", "CMLN 처리", "1,800+ wallet", "#7e8ba4"),
    ]

    for ax, (big, small, sub, color) in zip(axes, stats):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.axis("off")
        ax.add_patch(plt.Rectangle((0.03, 0.03), 0.94, 0.94, fill=False,
                                    edgecolor=INK, linewidth=1.2))
        ax.add_patch(plt.Rectangle((0.03, 0.03), 0.94, 0.15, fill=True,
                                    color=color, edgecolor=color))
        ax.text(0.5, 0.62, big, ha="center", va="center",
                fontsize=28, fontweight="bold", color=INK,
                fontfamily=["IBM Plex Serif", "serif"])
        ax.text(0.5, 0.38, small, ha="center", va="center",
                fontsize=10, color=INK_SOFT)
        ax.text(0.5, 0.105, sub, ha="center", va="center",
                fontsize=8.5, color="white", fontweight="bold")

    fig.suptitle("2025 가상자산 범죄 · 규모 스냅샷", fontsize=14, fontweight="bold",
                 color=INK, x=0.02, ha="left", y=0.99)
    fig.text(0.02, -0.03, "Source: Chainalysis 2026 Crypto Crime Report",
             fontsize=7.5, color=INK_MUTE, ha="left")
    plt.tight_layout()
    savefig(fig, "trend_2025_snapshot")


# ========================= Chart 6: Travel Rule Thresholds =========================

def chart_travel_rule_thresholds():
    """관할별 Travel Rule 임계금액 비교 (USD 환산)"""
    data = pd.DataFrame({
        "juris":  ["EU (TFR)",  "싱가포르",   "일본",      "🌍 FATF 권고", "한국",       "미국 (BSA)"],
        "usd":    [0,           1130,         780,         1000,           770,          3000],
        "native": ["€0 (모든 거래)", "SGD 1,500",  "¥100,000",  "USD/EUR 1,000", "₩1,000,000", "$3,000"],
    })
    data = data.sort_values("usd", ascending=True).reset_index(drop=True)
    colors = ["#c9a646" if j == "🌍 FATF 권고" else ACCENT for j in data["juris"]]

    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    y = range(len(data))
    bars = ax.barh(y, data["usd"], color=colors, edgecolor=INK, linewidth=0.6, height=0.62)

    for bar, juris, native in zip(bars, data["juris"], data["native"]):
        ax.text(
            bar.get_width() + 80, bar.get_y() + bar.get_height() / 2,
            native, va="center", ha="left",
            fontsize=9.5, color=INK, fontweight="bold",
        )

    ax.set_yticks(y)
    ax.set_yticklabels(data["juris"], fontsize=10)
    ax.set_xlabel("USD 환산 임계금액")
    ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${int(x):,}"))
    ax.set_xlim(0, 4000)
    ax.set_title("관할별 Travel Rule 임계금액 — EU가 가장 엄격 (임계 0)", loc="left", pad=14)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", linewidth=0.5, color=RULE)
    ax.set_axisbelow(True)

    fig.text(0.01, -0.02, "Source: FATF R.16 · 한국 특금법 시행령 §10의10 · BSA 1996 · EU TFR 2023/1113",
             fontsize=7.5, color=INK_MUTE, ha="left")
    savefig(fig, "travel_rule_thresholds")


# ========================= Chart 7: FATF Grey/Black Heatmap =========================

def chart_fatf_watchlist():
    """FATF 2026 Grey/Black 국가 목록 시각화 (categorical strip)"""
    black = ["북한", "이란", "미얀마"]
    grey = ["케냐", "나미비아", "필리핀", "콩고민주공화국", "라이베리아", "시리아",
            "남수단", "예멘", "말리", "베네수엘라", "나이지리아", "크로아티아"]

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
        x = col * 1.8 + 0.5
        y = y_grey - row * 0.7
        ax.add_patch(plt.Rectangle(
            (x - 0.75, y - 0.28), 1.5, 0.56,
            facecolor="#fff7d6", edgecolor="#c9a646", linewidth=1.0,
        ))
        ax.text(x, y, country, ha="center", va="center",
                fontsize=9, color="#78572d")

    # Labels
    ax.text(-1.5, y_black, "Black\n(High-Risk)",
            ha="right", va="center",
            fontsize=10, fontweight="bold", color="#991b1b",
            bbox=dict(facecolor="white", edgecolor="#dc2626", boxstyle="round,pad=0.4"))
    ax.text(-1.5, y_grey - 0.35, "Grey\n(Increased\nMonitoring)",
            ha="right", va="center",
            fontsize=10, fontweight="bold", color="#78572d",
            bbox=dict(facecolor="white", edgecolor="#c9a646", boxstyle="round,pad=0.4"))

    ax.set_xlim(-3.6, 11.5)
    ax.set_ylim(-1.5, 1.8)
    ax.axis("off")
    ax.set_title("FATF 2026 High-Risk · Grey List", loc="left", pad=14,
                 fontsize=14, fontweight="bold", color=INK)

    fig.text(0.01, 0.02, "Source: FATF Plenary (수시 갱신) — 본 자료는 2026-04 기준",
             fontsize=7.5, color=INK_MUTE, ha="left")
    savefig(fig, "fatf_watchlist")


# ========================= Chart 8: Vertical Regulation Timeline =========================

def chart_regulation_timeline():
    """2020~2030 주요 가상자산 AML 규제 타임라인 (세로형)"""
    events = [
        (2020.2, "한국 특금법 개정 공포",        "🇰🇷", ACCENT),
        (2021.3, "한국 VASP 신고제 시행",       "🇰🇷", ACCENT),
        (2022.3, "한국 Travel Rule 시행",       "🇰🇷", ACCENT),
        (2022.8, "OFAC Tornado Cash 제재",     "🇺🇸", "#8c6b2f"),
        (2024.7, "한국 이용자보호법 시행",       "🇰🇷", ACCENT),
        (2024.12, "EU MiCA + TFR 전면 시행",    "🇪🇺", "#4a5f7e"),
        (2025.3, "OFAC Tornado 제재 해제",     "🇺🇸", "#8c6b2f"),
        (2025.6, "FATF R.16 개정",              "🌍", "#c9a646"),
        (2025.7, "미국 GENIUS Act 통과",        "🇺🇸", "#8c6b2f"),
        (2026.1, "한국 특금법 개정 (대주주)",    "🇰🇷", ACCENT),
        (2026.7, "EU MiCA grandfathering 종료",  "🇪🇺", "#4a5f7e"),
        (2027.1, "GENIUS Act 전면 시행",        "🇺🇸", "#8c6b2f"),
        (2027.7, "EU AMLR + AMLD6 적용",       "🇪🇺", "#4a5f7e"),
        (2028.1, "EU AMLA 직접 감독 개시",      "🇪🇺", "#4a5f7e"),
        (2030.12, "FATF R.16 발효",             "🌍", "#c9a646"),
    ]
    today = 2026.31  # ~ 2026-04

    fig, ax = plt.subplots(figsize=(8.4, 11))
    # Vertical timeline spine
    ax.plot([0.5, 0.5], [2020, 2031], color=INK, linewidth=1.4, zorder=1)

    for y, label, flag, color in events:
        is_past = y <= today
        marker_color = color if not is_past else color
        marker_face = "white" if not is_past else color
        # Circle marker
        ax.scatter(0.5, y, s=130, zorder=3,
                   facecolor=marker_face, edgecolor=color, linewidth=1.8)
        # Year label
        ax.text(0.35, y, f"{int(y)}-{int(round((y-int(y))*12)):02d}",
                ha="right", va="center",
                fontsize=9, color=INK_MUTE, fontfamily="monospace")
        # Event card
        text = f"{flag}  {label}"
        ax.text(0.62, y, text,
                ha="left", va="center",
                fontsize=10, color=INK,
                fontweight="bold" if not is_past else "normal",
                alpha=1.0 if not is_past else 0.78)

    # Today marker
    ax.axhline(today, xmin=0.05, xmax=0.95, color="#c9a646",
               linestyle="--", linewidth=1.1, alpha=0.7, zorder=2)
    ax.text(0.98, today, "  ← 오늘 (2026-04)",
            ha="left", va="center",
            fontsize=9, color="#8c6b2f", fontweight="bold")

    ax.set_ylim(2031, 2019.5)  # inverted: 2020 top, 2030 bottom
    ax.set_xlim(-0.5, 1.7)
    ax.axis("off")
    ax.set_title("가상자산 AML 규제 타임라인 (2020~2030)",
                 loc="left", pad=20, x=-0.06,
                 fontsize=14, fontweight="bold", color=INK)

    fig.text(0.5, 0.01, "🇰🇷 한국 · 🇺🇸 미국 · 🇪🇺 EU · 🌍 FATF",
             fontsize=9, color=INK_MUTE, ha="center")
    savefig(fig, "regulation_timeline")


# ========================= Main =========================

CHARTS = [
    ("Lazarus Yearly Theft", chart_lazarus_yearly),
    ("Enforcement Fines Trajectory", chart_enforcement_fines),
    ("Illicit Asset Share", chart_illicit_asset_share),
    ("VASP Obligations Radar", chart_vasp_obligations_radar),
    ("2025 Trend Snapshot", chart_trend_2025),
    ("Travel Rule Thresholds", chart_travel_rule_thresholds),
    ("FATF Grey/Black Watchlist", chart_fatf_watchlist),
    ("Regulation Timeline 2020-2030", chart_regulation_timeline),
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
