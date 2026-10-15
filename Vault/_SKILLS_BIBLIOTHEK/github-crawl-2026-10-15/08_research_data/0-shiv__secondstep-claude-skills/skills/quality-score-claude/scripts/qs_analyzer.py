#!/usr/bin/env python3
"""
Quality Score Analyzer
Parses Google Ads keyword CSV exports and produces QS analysis.

Usage:
    python qs_analyzer.py <csv_file> [--output json|text|csv]
    python qs_analyzer.py data.csv --output text
    python qs_analyzer.py data.csv --compare previous_data.csv
"""

import csv
import sys
import json
import argparse
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field, asdict


# CPC multiplier relative to QS 7 baseline
CPC_MULTIPLIERS = {
    1: 5.00,
    2: 4.00,
    3: 3.00,
    4: 2.00,
    5: 1.67,
    6: 1.25,
    7: 1.00,
    8: 0.83,
    9: 0.67,
    10: 0.50,
}

# Realistic target QS for each current QS level
REALISTIC_TARGETS = {
    1: 5, 2: 5, 3: 6, 4: 7, 5: 7,
    6: 7, 7: 8, 8: 9, 9: 10, 10: 10,
}


@dataclass
class KeywordData:
    keyword: str
    match_type: str
    campaign: str
    ad_group: str
    quality_score: Optional[int]
    expected_ctr: str
    ad_relevance: str
    landing_page_exp: str
    impressions: int
    clicks: int
    ctr: float
    avg_cpc: float
    cost: float
    conversions: float
    conv_rate: float
    cost_per_conv: float
    final_url: str
    status: str = "enabled"
    monthly_waste: float = 0.0
    realistic_waste: float = 0.0
    priority_score: float = 0.0


@dataclass
class QSAnalysis:
    total_keywords: int = 0
    keywords_with_qs: int = 0
    keywords_null_qs: int = 0
    weighted_avg_qs: float = 0.0
    total_spend: float = 0.0
    total_waste_theoretical: float = 0.0
    total_waste_realistic: float = 0.0
    distribution: dict = field(default_factory=dict)
    band_distribution: dict = field(default_factory=dict)
    component_summary: dict = field(default_factory=dict)
    top_waste_keywords: list = field(default_factory=list)
    grade: str = ""


def parse_number(value: str) -> float:
    """Parse a number string, handling currency symbols, commas, and percentages."""
    if not value or value == "--" or value == "—":
        return 0.0
    value = value.replace("$", "").replace(",", "").replace("%", "").strip()
    try:
        return float(value)
    except ValueError:
        return 0.0


def parse_qs(value: str) -> Optional[int]:
    """Parse Quality Score value, returning None for null/missing."""
    if not value or value in ("--", "—", "null", ""):
        return None
    try:
        qs = int(float(value))
        return qs if 1 <= qs <= 10 else None
    except ValueError:
        return None


def normalize_component(value: str) -> str:
    """Normalize component rating to standard format."""
    value = value.strip().lower()
    if "above" in value:
        return "Above Average"
    elif "below" in value:
        return "Below Average"
    elif "average" in value or "avg" in value:
        return "Average"
    return value


def find_column(headers: list, candidates: list) -> int:
    """Find column index from a list of possible header names."""
    headers_lower = [h.lower().strip() for h in headers]
    for candidate in candidates:
        candidate_lower = candidate.lower()
        for i, header in enumerate(headers_lower):
            if candidate_lower in header or header in candidate_lower:
                return i
    return -1


def parse_csv(filepath: str) -> list[KeywordData]:
    """Parse a Google Ads keyword CSV export."""
    keywords = []
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        headers = next(reader)

        # Find column indices
        col_keyword = find_column(headers, ["keyword", "search keyword", "keyword text"])
        col_match = find_column(headers, ["match type"])
        col_campaign = find_column(headers, ["campaign"])
        col_adgroup = find_column(headers, ["ad group"])
        col_qs = find_column(headers, ["quality score", "qual. score"])
        col_ectr = find_column(headers, ["expected ctr", "exp. ctr", "expected clickthrough"])
        col_ar = find_column(headers, ["ad relevance"])
        col_lp = find_column(headers, ["landing page exp", "landing page experience", "land. page exp"])
        col_impressions = find_column(headers, ["impressions", "impr."])
        col_clicks = find_column(headers, ["clicks"])
        col_ctr = find_column(headers, ["ctr", "click-through rate"])
        col_cpc = find_column(headers, ["avg. cpc", "avg cpc", "average cpc"])
        col_cost = find_column(headers, ["cost", "spend"])
        col_conv = find_column(headers, ["conversions", "conv."])
        col_conv_rate = find_column(headers, ["conv. rate", "conversion rate"])
        col_cost_conv = find_column(headers, ["cost / conv", "cost/conv", "cost per conv"])
        col_url = find_column(headers, ["final url", "final url", "destination url"])
        col_status = find_column(headers, ["status", "keyword status"])

        for row in reader:
            if not row or len(row) < 3:
                continue
            # Skip summary rows
            if row[0].lower().startswith("total"):
                continue

            def get(col, default=""):
                return row[col] if col >= 0 and col < len(row) else default

            kw = KeywordData(
                keyword=get(col_keyword, "unknown"),
                match_type=get(col_match, "unknown"),
                campaign=get(col_campaign, "unknown"),
                ad_group=get(col_adgroup, "unknown"),
                quality_score=parse_qs(get(col_qs)),
                expected_ctr=normalize_component(get(col_ectr, "unknown")),
                ad_relevance=normalize_component(get(col_ar, "unknown")),
                landing_page_exp=normalize_component(get(col_lp, "unknown")),
                impressions=int(parse_number(get(col_impressions))),
                clicks=int(parse_number(get(col_clicks))),
                ctr=parse_number(get(col_ctr)),
                avg_cpc=parse_number(get(col_cpc)),
                cost=parse_number(get(col_cost)),
                conversions=parse_number(get(col_conv)),
                conv_rate=parse_number(get(col_conv_rate)),
                cost_per_conv=parse_number(get(col_cost_conv)),
                final_url=get(col_url, ""),
                status=get(col_status, "enabled").lower(),
            )
            keywords.append(kw)

    return keywords


def calculate_waste(kw: KeywordData) -> None:
    """Calculate CPC waste for a single keyword."""
    if kw.quality_score is None or kw.quality_score >= 10 or kw.clicks == 0:
        kw.monthly_waste = 0.0
        kw.realistic_waste = 0.0
        kw.priority_score = 0.0
        return

    current_mult = CPC_MULTIPLIERS.get(kw.quality_score, 1.0)
    qs10_mult = CPC_MULTIPLIERS[10]
    theoretical_cpc = kw.avg_cpc * (qs10_mult / current_mult)
    kw.monthly_waste = kw.clicks * (kw.avg_cpc - theoretical_cpc)

    target_qs = REALISTIC_TARGETS.get(kw.quality_score, kw.quality_score)
    target_mult = CPC_MULTIPLIERS.get(target_qs, 1.0)
    realistic_cpc = kw.avg_cpc * (target_mult / current_mult)
    kw.realistic_waste = kw.clicks * (kw.avg_cpc - realistic_cpc)

    kw.priority_score = kw.monthly_waste


def analyze(keywords: list[KeywordData]) -> QSAnalysis:
    """Run full QS analysis on keyword data."""
    analysis = QSAnalysis()
    analysis.total_keywords = len(keywords)

    # Filter to enabled keywords with QS
    active = [kw for kw in keywords if kw.status != "paused"]
    with_qs = [kw for kw in active if kw.quality_score is not None]
    analysis.keywords_with_qs = len(with_qs)
    analysis.keywords_null_qs = len(active) - len(with_qs)

    if not with_qs:
        return analysis

    # Calculate waste for each keyword
    for kw in with_qs:
        calculate_waste(kw)

    # Total spend
    analysis.total_spend = sum(kw.cost for kw in with_qs)
    analysis.total_waste_theoretical = sum(kw.monthly_waste for kw in with_qs)
    analysis.total_waste_realistic = sum(kw.realistic_waste for kw in with_qs)

    # Weighted average QS
    total_impressions = sum(kw.impressions for kw in with_qs)
    if total_impressions > 0:
        analysis.weighted_avg_qs = sum(
            kw.quality_score * kw.impressions for kw in with_qs
        ) / total_impressions

    # Distribution by QS value
    for qs in range(1, 11):
        qs_kws = [kw for kw in with_qs if kw.quality_score == qs]
        analysis.distribution[qs] = {
            "count": len(qs_kws),
            "pct": len(qs_kws) / len(with_qs) * 100 if with_qs else 0,
            "spend": sum(kw.cost for kw in qs_kws),
        }

    # Band distribution
    bands = {
        "Critical (1-2)": [kw for kw in with_qs if kw.quality_score <= 2],
        "Poor (3-4)": [kw for kw in with_qs if 3 <= kw.quality_score <= 4],
        "Average (5-6)": [kw for kw in with_qs if 5 <= kw.quality_score <= 6],
        "Good (7)": [kw for kw in with_qs if kw.quality_score == 7],
        "Excellent (8-10)": [kw for kw in with_qs if kw.quality_score >= 8],
    }
    for band, kws in bands.items():
        analysis.band_distribution[band] = {
            "count": len(kws),
            "pct": len(kws) / len(with_qs) * 100 if with_qs else 0,
            "spend": sum(kw.cost for kw in kws),
        }

    # Component summary
    for component in ["expected_ctr", "ad_relevance", "landing_page_exp"]:
        label = component.replace("_", " ").title()
        values = [getattr(kw, component) for kw in with_qs]
        analysis.component_summary[label] = {
            "Above Average": sum(1 for v in values if v == "Above Average"),
            "Average": sum(1 for v in values if v == "Average"),
            "Below Average": sum(1 for v in values if v == "Below Average"),
        }

    # Top waste keywords
    sorted_by_waste = sorted(with_qs, key=lambda k: k.monthly_waste, reverse=True)
    analysis.top_waste_keywords = [
        {
            "keyword": kw.keyword,
            "quality_score": kw.quality_score,
            "monthly_spend": round(kw.cost, 2),
            "monthly_waste": round(kw.monthly_waste, 2),
            "weakest_component": get_weakest_component(kw),
            "campaign": kw.campaign,
            "ad_group": kw.ad_group,
        }
        for kw in sorted_by_waste[:20]
    ]

    # Grade
    pct_at_7_plus = sum(1 for kw in with_qs if kw.quality_score >= 7) / len(with_qs) * 100
    if pct_at_7_plus >= 70 and analysis.weighted_avg_qs > 7.5:
        analysis.grade = "A"
    elif pct_at_7_plus >= 60 and analysis.weighted_avg_qs >= 6.5:
        analysis.grade = "B"
    elif pct_at_7_plus >= 45 and analysis.weighted_avg_qs >= 5.5:
        analysis.grade = "C"
    elif pct_at_7_plus >= 30 and analysis.weighted_avg_qs >= 4.5:
        analysis.grade = "D"
    else:
        analysis.grade = "F"

    return analysis


def get_weakest_component(kw: KeywordData) -> str:
    """Identify the weakest QS component for a keyword."""
    components = {
        "Expected CTR": kw.expected_ctr,
        "Ad Relevance": kw.ad_relevance,
        "Landing Page": kw.landing_page_exp,
    }
    for name, rating in components.items():
        if rating == "Below Average":
            return f"{name} (Below Avg)"
    for name, rating in components.items():
        if rating == "Average":
            return f"{name} (Avg)"
    return "All Above Avg"


def format_text(analysis: QSAnalysis) -> str:
    """Format analysis as human-readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("QUALITY SCORE ANALYSIS REPORT")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Grade: {analysis.grade}")
    lines.append(f"Total keywords: {analysis.total_keywords}")
    lines.append(f"Keywords with QS: {analysis.keywords_with_qs}")
    lines.append(f"Keywords (null QS): {analysis.keywords_null_qs}")
    lines.append(f"Weighted Avg QS: {analysis.weighted_avg_qs:.1f}")
    lines.append(f"Total monthly spend: ${analysis.total_spend:,.2f}")
    lines.append("")
    lines.append(f"Maximum theoretical savings: ${analysis.total_waste_theoretical:,.2f}/month")
    lines.append(f"Realistic savings: ${analysis.total_waste_realistic:,.2f}/month")
    lines.append(f"Annual realistic savings: ${analysis.total_waste_realistic * 12:,.2f}/year")
    lines.append("")

    lines.append("QS Distribution")
    lines.append("-" * 40)
    for qs, data in sorted(analysis.distribution.items()):
        bar = "#" * int(data["pct"])
        lines.append(f"QS {qs:>2}: {data['count']:>5} ({data['pct']:>5.1f}%) {bar}")
    lines.append("")

    lines.append("QS Band Summary")
    lines.append("-" * 40)
    for band, data in analysis.band_distribution.items():
        lines.append(f"{band:<20} {data['count']:>5} kws ({data['pct']:>5.1f}%) ${data['spend']:>10,.2f}")
    lines.append("")

    lines.append("Component Summary")
    lines.append("-" * 40)
    for comp, ratings in analysis.component_summary.items():
        total = sum(ratings.values())
        if total > 0:
            lines.append(f"{comp}:")
            for rating, count in ratings.items():
                pct = count / total * 100
                lines.append(f"  {rating:<15} {count:>5} ({pct:>5.1f}%)")
    lines.append("")

    lines.append("Top 20 Keywords by Monthly Waste")
    lines.append("-" * 60)
    for i, kw in enumerate(analysis.top_waste_keywords, 1):
        lines.append(
            f"{i:>2}. \"{kw['keyword']}\" — QS {kw['quality_score']} — "
            f"${kw['monthly_spend']:,.2f} spend — ${kw['monthly_waste']:,.2f} waste — "
            f"{kw['weakest_component']}"
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Google Ads Quality Score Analyzer")
    parser.add_argument("csv_file", help="Path to Google Ads keyword CSV export")
    parser.add_argument("--output", choices=["json", "text", "csv"], default="text",
                        help="Output format (default: text)")
    parser.add_argument("--compare", help="Path to previous CSV for trend comparison")
    args = parser.parse_args()

    if not Path(args.csv_file).exists():
        print(f"Error: File not found: {args.csv_file}", file=sys.stderr)
        sys.exit(1)

    keywords = parse_csv(args.csv_file)
    analysis = analyze(keywords)

    if args.output == "json":
        print(json.dumps(asdict(analysis), indent=2, default=str))
    elif args.output == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["Keyword", "QS", "Spend", "Waste", "Weakest Component"])
        for kw in analysis.top_waste_keywords:
            writer.writerow([kw["keyword"], kw["quality_score"],
                             kw["monthly_spend"], kw["monthly_waste"],
                             kw["weakest_component"]])
    else:
        print(format_text(analysis))

    if args.compare:
        if Path(args.compare).exists():
            prev_keywords = parse_csv(args.compare)
            prev_analysis = analyze(prev_keywords)
            print("\n" + "=" * 60)
            print("TREND COMPARISON")
            print("=" * 60)
            print(f"Previous weighted avg QS: {prev_analysis.weighted_avg_qs:.1f}")
            print(f"Current weighted avg QS:  {analysis.weighted_avg_qs:.1f}")
            diff = analysis.weighted_avg_qs - prev_analysis.weighted_avg_qs
            direction = "improved" if diff > 0 else "declined" if diff < 0 else "unchanged"
            print(f"Change: {diff:+.1f} ({direction})")
        else:
            print(f"Warning: Comparison file not found: {args.compare}", file=sys.stderr)


if __name__ == "__main__":
    main()
