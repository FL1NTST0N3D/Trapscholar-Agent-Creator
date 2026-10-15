#!/usr/bin/env python3
"""
YouTube Campaign Data Parser

Parses Google Ads campaign export data (CSV or TSV) and structures it
for analysis by the YouTube Ads audit skill.

Usage:
    python parse_campaign_data.py <input_file> [--format csv|tsv] [--output json|table]

Author: Shivendra Rawat (@0-shiv)
License: MIT
"""

import csv
import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional


# YouTube Ads benchmarks for scoring
BENCHMARKS = {
    "view_rate": {"poor": 0.20, "average": 0.319, "good": 0.45, "excellent": 0.55},
    "cpv": {"excellent": 0.10, "good": 0.15, "average": 0.30, "poor": 0.40},
    "ctr": {"poor": 0.003, "average": 0.005, "good": 0.010, "excellent": 0.015},
    "cpm_shorts": {"excellent": 2.00, "good": 4.00, "average": 8.00, "poor": 12.00},
    "cpm_nonskip": {"excellent": 4.00, "good": 6.00, "average": 12.00, "poor": 16.00},
    "conv_rate": {"poor": 0.005, "average": 0.015, "good": 0.030, "excellent": 0.050},
}

# Column name mappings (Google Ads export variations)
COLUMN_MAPPINGS = {
    "campaign": ["Campaign", "Campaign name", "campaign_name"],
    "type": ["Campaign type", "Type", "campaign_type"],
    "status": ["Campaign status", "Status", "campaign_status"],
    "budget": ["Budget", "Daily budget", "budget_amount"],
    "bid_strategy": ["Bid strategy", "Bid strategy type", "bidding_strategy_type"],
    "impressions": ["Impressions", "Impr.", "impressions"],
    "views": ["Views", "Video views", "views"],
    "view_rate": ["View rate", "View rate (%)", "view_rate"],
    "cpv": ["Avg. CPV", "CPV", "average_cpv"],
    "clicks": ["Clicks", "clicks"],
    "ctr": ["CTR", "CTR (%)", "ctr"],
    "conversions": ["Conversions", "Conv.", "conversions"],
    "cost_per_conv": ["Cost / conv.", "Cost/conv.", "cost_per_conversion"],
    "cost": ["Cost", "Total cost", "cost_micros"],
    "cpm": ["Avg. CPM", "CPM", "average_cpm"],
}


def normalize_column_name(col: str) -> Optional[str]:
    """Map a column header to a normalized name."""
    col_clean = col.strip().lower()
    for normalized, variants in COLUMN_MAPPINGS.items():
        for variant in variants:
            if col_clean == variant.lower():
                return normalized
    return None


def parse_percentage(value: str) -> float:
    """Convert percentage string to float (e.g., '31.5%' -> 0.315)."""
    if not value or value == "--":
        return 0.0
    value = value.strip().replace("%", "").replace(",", "")
    try:
        return float(value) / 100.0
    except ValueError:
        return 0.0


def parse_currency(value: str) -> float:
    """Convert currency string to float (e.g., '$0.15' -> 0.15)."""
    if not value or value == "--":
        return 0.0
    value = value.strip().replace("$", "").replace(",", "").replace("£", "").replace("€", "")
    try:
        return float(value)
    except ValueError:
        return 0.0


def parse_number(value: str) -> float:
    """Convert number string to float."""
    if not value or value == "--":
        return 0.0
    value = value.strip().replace(",", "")
    try:
        return float(value)
    except ValueError:
        return 0.0


def score_metric(value: float, metric_name: str, lower_is_better: bool = False) -> str:
    """Score a metric against benchmarks."""
    if metric_name not in BENCHMARKS:
        return "N/A"
    bench = BENCHMARKS[metric_name]

    if lower_is_better:
        if value <= bench["excellent"]:
            return "Excellent"
        elif value <= bench["good"]:
            return "Good"
        elif value <= bench["average"]:
            return "Average"
        else:
            return "Poor"
    else:
        if value >= bench.get("excellent", float("inf")):
            return "Excellent"
        elif value >= bench.get("good", 0):
            return "Good"
        elif value >= bench.get("average", 0):
            return "Average"
        else:
            return "Poor"


def parse_campaign_file(filepath: str, file_format: str = "csv") -> List[Dict]:
    """Parse a campaign export file and return structured data."""
    campaigns = []
    delimiter = "," if file_format == "csv" else "\t"

    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=delimiter)

        for row in reader:
            campaign = {}
            for col, value in row.items():
                normalized = normalize_column_name(col)
                if normalized:
                    if normalized in ("impressions", "views", "clicks", "conversions"):
                        campaign[normalized] = parse_number(value)
                    elif normalized in ("view_rate", "ctr"):
                        campaign[normalized] = parse_percentage(value)
                    elif normalized in ("cpv", "cost_per_conv", "cost", "budget", "cpm"):
                        campaign[normalized] = parse_currency(value)
                    else:
                        campaign[normalized] = value.strip()

            if campaign.get("campaign"):
                # Add benchmark scores
                if "view_rate" in campaign:
                    campaign["view_rate_rating"] = score_metric(
                        campaign["view_rate"], "view_rate"
                    )
                if "cpv" in campaign:
                    campaign["cpv_rating"] = score_metric(
                        campaign["cpv"], "cpv", lower_is_better=True
                    )
                if "ctr" in campaign:
                    campaign["ctr_rating"] = score_metric(campaign["ctr"], "ctr")

                campaigns.append(campaign)

    return campaigns


def generate_summary(campaigns: List[Dict]) -> Dict:
    """Generate a summary analysis of all campaigns."""
    if not campaigns:
        return {"error": "No campaigns found in data"}

    total_cost = sum(c.get("cost", 0) for c in campaigns)
    total_impressions = sum(c.get("impressions", 0) for c in campaigns)
    total_views = sum(c.get("views", 0) for c in campaigns)
    total_clicks = sum(c.get("clicks", 0) for c in campaigns)
    total_conversions = sum(c.get("conversions", 0) for c in campaigns)

    active = [c for c in campaigns if c.get("status", "").lower() in ("enabled", "active")]
    paused = [c for c in campaigns if c.get("status", "").lower() == "paused"]

    summary = {
        "total_campaigns": len(campaigns),
        "active_campaigns": len(active),
        "paused_campaigns": len(paused),
        "total_cost": round(total_cost, 2),
        "total_impressions": int(total_impressions),
        "total_views": int(total_views),
        "total_clicks": int(total_clicks),
        "total_conversions": int(total_conversions),
        "overall_view_rate": round(total_views / total_impressions, 4) if total_impressions > 0 else 0,
        "overall_ctr": round(total_clicks / total_impressions, 4) if total_impressions > 0 else 0,
        "overall_cpv": round(total_cost / total_views, 2) if total_views > 0 else 0,
        "overall_cpa": round(total_cost / total_conversions, 2) if total_conversions > 0 else 0,
    }

    # Identify issues
    issues = []
    for c in active:
        name = c.get("campaign", "Unknown")
        if c.get("view_rate", 0) < 0.20:
            issues.append(f"Low view rate ({c['view_rate']:.1%}) on '{name}' — weak hook or targeting")
        if c.get("cpv", 0) > 0.30:
            issues.append(f"High CPV (${c['cpv']:.2f}) on '{name}' — overpaying for views")
        if c.get("budget", 0) > 0 and c.get("budget", 0) < 10:
            issues.append(f"Budget below $10/day on '{name}' — insufficient for video optimization")
        if c.get("conversions", 0) == 0 and c.get("cost", 0) > 100:
            issues.append(f"Zero conversions with ${c['cost']:.0f} spent on '{name}' — check conversion tracking")

    summary["issues"] = issues
    summary["issue_count"] = len(issues)

    return summary


def format_table(campaigns: List[Dict]) -> str:
    """Format campaigns as a markdown table."""
    if not campaigns:
        return "No campaign data found."

    headers = ["Campaign", "Status", "Budget", "Views", "View Rate", "CPV", "CTR", "Conv", "Cost"]
    rows = []

    for c in campaigns:
        rows.append([
            c.get("campaign", "N/A")[:30],
            c.get("status", "N/A"),
            f"${c.get('budget', 0):.0f}",
            f"{c.get('views', 0):,.0f}",
            f"{c.get('view_rate', 0):.1%}",
            f"${c.get('cpv', 0):.2f}",
            f"{c.get('ctr', 0):.2%}",
            f"{c.get('conversions', 0):.0f}",
            f"${c.get('cost', 0):,.0f}",
        ])

    # Build table
    col_widths = [max(len(h), max(len(r[i]) for r in rows)) for i, h in enumerate(headers)]
    separator = "| " + " | ".join("-" * w for w in col_widths) + " |"
    header_line = "| " + " | ".join(h.ljust(w) for h, w in zip(headers, col_widths)) + " |"

    table_lines = [header_line, separator]
    for row in rows:
        table_lines.append("| " + " | ".join(v.ljust(w) for v, w in zip(row, col_widths)) + " |")

    return "\n".join(table_lines)


def main():
    parser = argparse.ArgumentParser(description="Parse YouTube campaign data from Google Ads exports")
    parser.add_argument("input_file", help="Path to the campaign export file (CSV or TSV)")
    parser.add_argument("--format", choices=["csv", "tsv"], default="csv", help="Input file format")
    parser.add_argument("--output", choices=["json", "table"], default="table", help="Output format")

    args = parser.parse_args()

    if not Path(args.input_file).exists():
        print(f"Error: File not found: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    campaigns = parse_campaign_file(args.input_file, args.format)
    summary = generate_summary(campaigns)

    if args.output == "json":
        output = {
            "summary": summary,
            "campaigns": campaigns,
        }
        print(json.dumps(output, indent=2))
    else:
        print("\n## Campaign Data Summary\n")
        print(f"- Total Campaigns: {summary['total_campaigns']}")
        print(f"- Active: {summary['active_campaigns']} | Paused: {summary['paused_campaigns']}")
        print(f"- Total Cost: ${summary['total_cost']:,.2f}")
        print(f"- Overall View Rate: {summary['overall_view_rate']:.1%}")
        print(f"- Overall CPV: ${summary['overall_cpv']:.2f}")
        print(f"- Overall CPA: ${summary['overall_cpa']:.2f}")
        print(f"\n## Campaign Performance\n")
        print(format_table(campaigns))

        if summary["issues"]:
            print(f"\n## Issues Found ({summary['issue_count']})\n")
            for i, issue in enumerate(summary["issues"], 1):
                print(f"{i}. {issue}")


if __name__ == "__main__":
    main()
