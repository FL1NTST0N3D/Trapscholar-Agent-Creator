#!/usr/bin/env python3
"""
CPC Impact Calculator
Calculates the dollar impact of Quality Score on CPC across a Google Ads account.

Usage:
    python cpc_impact_calculator.py <csv_file> [--target-qs 7] [--format text|json|csv]
"""

import csv
import sys
import json
import argparse
from pathlib import Path


CPC_MULTIPLIERS = {
    1: 5.00, 2: 4.00, 3: 3.00, 4: 2.00, 5: 1.67,
    6: 1.25, 7: 1.00, 8: 0.83, 9: 0.67, 10: 0.50,
}


def parse_number(value: str) -> float:
    if not value or value in ("--", "—"):
        return 0.0
    return float(value.replace("$", "").replace(",", "").replace("%", "").strip() or "0")


def calculate_impact(csv_file: str, target_qs: int = 10) -> dict:
    """Calculate CPC impact for all keywords in the CSV."""
    results = {
        "target_qs": target_qs,
        "total_keywords": 0,
        "keywords_below_target": 0,
        "total_spend": 0.0,
        "total_waste": 0.0,
        "total_theoretical_spend": 0.0,
        "keywords": [],
    }

    target_mult = CPC_MULTIPLIERS.get(target_qs, 1.0)

    with open(csv_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Try different column name formats
            keyword = (row.get("Keyword") or row.get("keyword") or
                       row.get("Search keyword") or "unknown")
            qs_str = (row.get("Quality Score") or row.get("Quality score") or
                      row.get("Qual. Score") or "")
            clicks_str = row.get("Clicks") or row.get("clicks") or "0"
            cpc_str = (row.get("Avg. CPC") or row.get("Avg CPC") or
                       row.get("avg. cpc") or "0")
            cost_str = row.get("Cost") or row.get("cost") or row.get("Spend") or "0"
            campaign = row.get("Campaign") or row.get("campaign") or ""
            ad_group = row.get("Ad group") or row.get("Ad Group") or ""

            if not qs_str or qs_str in ("--", "—"):
                continue

            try:
                qs = int(float(qs_str))
            except ValueError:
                continue

            if qs < 1 or qs > 10:
                continue

            clicks = int(parse_number(clicks_str))
            avg_cpc = parse_number(cpc_str)
            cost = parse_number(cost_str)

            results["total_keywords"] += 1
            results["total_spend"] += cost

            current_mult = CPC_MULTIPLIERS.get(qs, 1.0)

            if qs < target_qs:
                results["keywords_below_target"] += 1
                theoretical_cpc = avg_cpc * (target_mult / current_mult)
                waste = clicks * (avg_cpc - theoretical_cpc)
                theoretical_cost = cost * (target_mult / current_mult)
            else:
                theoretical_cpc = avg_cpc
                waste = 0.0
                theoretical_cost = cost

            results["total_waste"] += waste
            results["total_theoretical_spend"] += theoretical_cost

            results["keywords"].append({
                "keyword": keyword,
                "campaign": campaign,
                "ad_group": ad_group,
                "quality_score": qs,
                "clicks": clicks,
                "avg_cpc": round(avg_cpc, 2),
                "cost": round(cost, 2),
                "theoretical_cpc": round(theoretical_cpc, 2),
                "theoretical_cost": round(theoretical_cost, 2),
                "monthly_waste": round(waste, 2),
                "annual_waste": round(waste * 12, 2),
                "cpc_reduction_pct": round((1 - target_mult / current_mult) * 100, 1) if qs < target_qs else 0,
            })

    # Sort by waste descending
    results["keywords"].sort(key=lambda x: x["monthly_waste"], reverse=True)
    results["total_waste"] = round(results["total_waste"], 2)
    results["total_theoretical_spend"] = round(results["total_theoretical_spend"], 2)
    results["savings_pct"] = round(
        (results["total_waste"] / results["total_spend"] * 100)
        if results["total_spend"] > 0 else 0, 1
    )

    return results


def format_text(results: dict) -> str:
    lines = []
    lines.append("=" * 70)
    lines.append(f"CPC IMPACT ANALYSIS (Target QS: {results['target_qs']})")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"Total keywords analyzed:    {results['total_keywords']}")
    lines.append(f"Keywords below target QS:   {results['keywords_below_target']}")
    lines.append(f"Total monthly spend:        ${results['total_spend']:>12,.2f}")
    lines.append(f"Theoretical spend at QS {results['target_qs']}:  ${results['total_theoretical_spend']:>12,.2f}")
    lines.append(f"Monthly waste:              ${results['total_waste']:>12,.2f}")
    lines.append(f"Annual waste:               ${results['total_waste'] * 12:>12,.2f}")
    lines.append(f"Savings potential:           {results['savings_pct']}%")
    lines.append("")
    lines.append("Top 20 Keywords by Monthly Waste")
    lines.append("-" * 70)
    lines.append(f"{'#':>3}  {'Keyword':<30} {'QS':>3} {'CPC':>8} {'Target':>8} {'Waste/Mo':>10}")
    lines.append("-" * 70)

    for i, kw in enumerate(results["keywords"][:20], 1):
        name = kw["keyword"][:28]
        lines.append(
            f"{i:>3}. {name:<30} {kw['quality_score']:>3} "
            f"${kw['avg_cpc']:>6.2f} ${kw['theoretical_cpc']:>6.2f} "
            f"${kw['monthly_waste']:>9,.2f}"
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="CPC Impact Calculator")
    parser.add_argument("csv_file", help="Path to Google Ads keyword CSV")
    parser.add_argument("--target-qs", type=int, default=10,
                        help="Target Quality Score for comparison (default: 10)")
    parser.add_argument("--format", choices=["text", "json", "csv"], default="text")
    args = parser.parse_args()

    if not Path(args.csv_file).exists():
        print(f"Error: File not found: {args.csv_file}", file=sys.stderr)
        sys.exit(1)

    results = calculate_impact(args.csv_file, args.target_qs)

    if args.format == "json":
        print(json.dumps(results, indent=2))
    elif args.format == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["Keyword", "QS", "Avg CPC", "Target CPC",
                          "Monthly Cost", "Monthly Waste", "Annual Waste"])
        for kw in results["keywords"]:
            writer.writerow([kw["keyword"], kw["quality_score"], kw["avg_cpc"],
                             kw["theoretical_cpc"], kw["cost"],
                             kw["monthly_waste"], kw["annual_waste"]])
    else:
        print(format_text(results))


if __name__ == "__main__":
    main()
