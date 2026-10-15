#!/usr/bin/env python3
"""
Feed Report Generator — Comprehensive Feed Health Report

Generates a formatted feed health report from analysis results.
Wraps feed_analyzer.py with additional reporting, trend tracking,
and recommendation generation.

Usage:
    python feed_report.py <feed_file> [--output report.txt] [--previous previous_scores.csv]

Author: Shivendra Rawat (@0-shiv) | Second Step
"""

import argparse
import csv
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Import from sibling module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from feed_analyzer import (
    analyze_feed,
    FeedSummary,
    ProductScore,
    get_grade,
    REQUIRED_ATTRIBUTES,
    RECOMMENDED_ATTRIBUTES,
)


# ---------------------------------------------------------------------------
# Recommendation engine
# ---------------------------------------------------------------------------

def generate_recommendations(scores: list[ProductScore], summary: FeedSummary) -> list[dict]:
    """Generate prioritized recommendations from analysis results."""
    recommendations = []

    # Title recommendations
    low_title = [s for s in scores if s.title_score < 70]
    if low_title:
        recommendations.append({
            "priority": "HIGH" if len(low_title) > len(scores) * 0.3 else "MEDIUM",
            "category": "Titles",
            "action": f"Optimize {len(low_title)} product titles scoring below 70",
            "detail": "Apply Brand + Product Type + Attributes formula, target 80-120 chars",
            "impact": f"Est. +20-40% CTR on {len(low_title)} products",
            "effort": "2-4 hours" if len(low_title) < 50 else "1-2 days",
            "timeframe": "This week",
        })

    # Description recommendations
    low_desc = [s for s in scores if s.description_score < 70]
    if low_desc:
        recommendations.append({
            "priority": "MEDIUM",
            "category": "Descriptions",
            "action": f"Rewrite {len(low_desc)} product descriptions",
            "detail": "Target 750-1500 chars with features, specs, benefits. Remove promotional text.",
            "impact": f"Est. +10-20% relevance on {len(low_desc)} products",
            "effort": "4-8 hours" if len(low_desc) < 50 else "2-3 days",
            "timeframe": "This month",
        })

    # Image recommendations
    low_image = [s for s in scores if s.image_score < 70]
    if low_image:
        recommendations.append({
            "priority": "HIGH",
            "category": "Images",
            "action": f"Fix image issues on {len(low_image)} products",
            "detail": "Check URLs, add additional images, remove placeholders",
            "impact": f"Est. -30% disapprovals, +20% CTR",
            "effort": "Varies — URL fixes fast, re-shoots slow",
            "timeframe": "This week (URLs), This month (re-shoots)",
        })

    # Attribute recommendations
    low_attr = [s for s in scores if s.attribute_score < 70]
    if low_attr:
        recommendations.append({
            "priority": "HIGH",
            "category": "Attributes",
            "action": f"Complete attributes on {len(low_attr)} products",
            "detail": "Fill missing required attributes, add GTIN/MPN, enrich recommended fields",
            "impact": f"Est. +25% impressions, -50% disapprovals",
            "effort": "2-4 hours for required, 1-2 days for recommended",
            "timeframe": "This week (required), This month (recommended)",
        })

    # Missing required attributes
    for attr, count in sorted(summary.missing_required.items(), key=lambda x: -x[1]):
        if count > 0:
            recommendations.append({
                "priority": "CRITICAL",
                "category": "Required Attributes",
                "action": f"Add '{attr}' to {count} products",
                "detail": f"Missing required attribute will cause disapproval",
                "impact": f"{count} products at risk of disapproval",
                "effort": "30 min - 2 hours",
                "timeframe": "Immediately",
            })

    # Custom label opportunity
    label_attrs = ["custom_label_0", "custom_label_1", "custom_label_2",
                   "custom_label_3", "custom_label_4"]
    missing_labels = sum(1 for la in label_attrs if la in summary.missing_recommended
                        and summary.missing_recommended[la] == summary.total_products)
    if missing_labels > 0:
        recommendations.append({
            "priority": "MEDIUM",
            "category": "Custom Labels",
            "action": f"{missing_labels} custom label slots unused",
            "detail": "Set up labels for margin tiers, performance, seasonality, price range",
            "impact": "+20% ROAS from differentiated bidding",
            "effort": "2-4 hours to define strategy + populate",
            "timeframe": "This month",
        })

    # Sort by priority
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    recommendations.sort(key=lambda r: priority_order.get(r["priority"], 99))

    return recommendations


# ---------------------------------------------------------------------------
# Trend comparison
# ---------------------------------------------------------------------------

def load_previous_scores(file_path: str) -> Optional[dict]:
    """Load previous scores CSV for trend comparison."""
    if not os.path.isfile(file_path):
        return None

    prev = {}
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            prev[row["id"]] = {
                "title_score": int(row.get("title_score", 0)),
                "description_score": int(row.get("description_score", 0)),
                "image_score": int(row.get("image_score", 0)),
                "attribute_score": int(row.get("attribute_score", 0)),
                "overall_score": int(row.get("overall_score", 0)),
            }
    return prev


def calculate_trend(current: float, previous: float) -> str:
    """Return trend indicator."""
    diff = current - previous
    if diff > 2:
        return f"+{diff:.1f} (improving)"
    elif diff < -2:
        return f"{diff:.1f} (declining)"
    return f"{diff:+.1f} (stable)"


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(
    scores: list[ProductScore],
    summary: FeedSummary,
    feed_path: str,
    previous_path: Optional[str] = None,
) -> str:
    """Generate the full feed health report as a formatted string."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    feed_name = os.path.basename(feed_path)
    recommendations = generate_recommendations(scores, summary)

    lines = []
    lines.append("=" * 56)
    lines.append("  PRODUCT FEED HEALTH REPORT")
    lines.append(f"  Generated: {now}")
    lines.append(f"  Feed: {feed_name}")
    lines.append(f"  Products: {summary.total_products}")
    lines.append("=" * 56)
    lines.append("")

    # Overall score
    lines.append(f"  OVERALL SCORE: {summary.overall_score} / 100 — Grade: {summary.grade}")

    # Trend
    if previous_path:
        prev_data = load_previous_scores(previous_path)
        if prev_data:
            prev_avg = sum(p["overall_score"] for p in prev_data.values()) / len(prev_data) if prev_data else 0
            trend = calculate_trend(summary.overall_score, prev_avg)
            lines.append(f"  Trend: {trend} vs previous report")
    lines.append("")

    # Component scores
    lines.append("  COMPONENT SCORES:")
    components = [
        ("Title Quality", summary.avg_title_score, "30%"),
        ("Attribute Completeness", summary.avg_attribute_score, "25%"),
        ("Image Compliance", summary.avg_image_score, "20%"),
        ("Description Quality", summary.avg_description_score, "15%"),
        ("Data Accuracy", summary.avg_attribute_score, "10%"),
    ]
    for name, score, weight in components:
        bar_len = int(score / 100 * 20)
        bar = "#" * bar_len + "-" * (20 - bar_len)
        lines.append(f"    {name:<25} {score:>5.1f}/100  [{bar}]  Weight: {weight}")
    lines.append("")

    # Key metrics
    lines.append("  KEY METRICS:")
    lines.append(f"    Avg Title Length:       {summary.title_length_avg} chars (target: 80-120)")
    lines.append(f"    Avg Description Length: {summary.desc_length_avg} chars (target: 750-1500)")
    lines.append(f"    Products with Issues:   {summary.products_with_issues} / {summary.total_products}")
    lines.append("")

    # Score distribution
    bands = {"A (90-100)": 0, "B (80-89)": 0, "C (70-79)": 0,
             "D (60-69)": 0, "E (50-59)": 0, "F (0-49)": 0}
    for s in scores:
        g = get_grade(s.overall_score)
        for band_name in bands:
            if band_name.startswith(g):
                bands[band_name] += 1
                break

    lines.append("  SCORE DISTRIBUTION:")
    for band, count in bands.items():
        pct = count / summary.total_products * 100 if summary.total_products > 0 else 0
        bar_len = int(pct / 100 * 30)
        bar = "#" * bar_len
        lines.append(f"    {band}: {count:>5} products ({pct:>5.1f}%)  {bar}")
    lines.append("")

    # Missing required attributes
    if summary.missing_required:
        lines.append("  MISSING REQUIRED ATTRIBUTES:")
        for attr, count in sorted(summary.missing_required.items(), key=lambda x: -x[1]):
            pct = count / summary.total_products * 100
            lines.append(f"    {attr:<25} {count:>5} products ({pct:.1f}%)")
        lines.append("")

    # Top issues by frequency
    issue_counts = {}
    for s in scores:
        for issue in s.issues:
            # Normalize issue text
            base = issue.split(":")[0] if ":" in issue else issue.split("(")[0].strip()
            issue_counts[base] = issue_counts.get(base, 0) + 1

    if issue_counts:
        lines.append("  TOP ISSUES (by frequency):")
        for issue, count in sorted(issue_counts.items(), key=lambda x: -x[1])[:10]:
            lines.append(f"    {count:>5}x  {issue}")
        lines.append("")

    # Worst products
    worst = sorted(scores, key=lambda s: s.overall_score)[:5]
    lines.append("  LOWEST SCORING PRODUCTS:")
    lines.append(f"    {'ID':<30} {'Score':>6} {'Issues':>7}")
    lines.append("    " + "-" * 48)
    for ps in worst:
        lines.append(f"    {ps.product_id:<30} {ps.overall_score:>6} {len(ps.issues):>7}")
    lines.append("")

    # Recommendations
    lines.append("  PRIORITIZED RECOMMENDATIONS:")
    lines.append("")
    for i, rec in enumerate(recommendations[:10], 1):
        lines.append(f"  {i}. [{rec['priority']}] {rec['action']}")
        lines.append(f"     {rec['detail']}")
        lines.append(f"     Impact: {rec['impact']}")
        lines.append(f"     Effort: {rec['effort']} | Timeframe: {rec['timeframe']}")
        lines.append("")

    lines.append("=" * 56)
    lines.append("  Generated by Product Feed Claude")
    lines.append("  https://github.com/0-shiv/product-feed-claude")
    lines.append("=" * 56)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate a comprehensive feed health report."
    )
    parser.add_argument("feed_file", help="Path to CSV or TSV feed file")
    parser.add_argument("--output", "-o", help="Save report to file (default: stdout)")
    parser.add_argument("--scores", "-s", help="Also export per-product scores to CSV")
    parser.add_argument("--previous", "-p", help="Previous scores CSV for trend comparison")
    parser.add_argument("--format", "-f", choices=["csv", "tsv"],
                        help="Force delimiter (auto-detected by default)")

    args = parser.parse_args()

    if not os.path.isfile(args.feed_file):
        print(f"ERROR: File not found: {args.feed_file}")
        sys.exit(1)

    delimiter = None
    if args.format == "tsv":
        delimiter = "\t"
    elif args.format == "csv":
        delimiter = ","

    scores, summary = analyze_feed(args.feed_file, delimiter)
    report = generate_report(scores, summary, args.feed_file, args.previous)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report saved to: {args.output}")
    else:
        print(report)

    if args.scores:
        from feed_analyzer import export_scores
        export_scores(scores, args.scores)


if __name__ == "__main__":
    main()
