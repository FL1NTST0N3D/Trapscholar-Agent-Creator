#!/usr/bin/env python3
"""
YouTube Ads Benchmark Comparison Tool

Compares campaign metrics against industry benchmarks and provides
performance ratings for each metric.

Usage:
    python benchmark_compare.py --view-rate 0.35 --cpv 0.12 --ctr 0.008 --conv-rate 0.02
    python benchmark_compare.py --input metrics.json --output report

Author: Shivendra Rawat (@0-shiv)
License: MIT
"""

import argparse
import json
import sys
from typing import Dict, List, Optional, Tuple


# Industry benchmarks by vertical
VERTICAL_BENCHMARKS = {
    "all_industries": {
        "view_rate": {"poor": 0.20, "average": 0.319, "good": 0.45, "excellent": 0.55},
        "cpv": {"excellent": 0.10, "good": 0.15, "average": 0.30, "poor": 0.40},
        "ctr_instream": {"poor": 0.003, "average": 0.005, "good": 0.010, "excellent": 0.015},
        "ctr_infeed": {"poor": 0.005, "average": 0.010, "good": 0.020, "excellent": 0.030},
        "cpm_shorts": {"excellent": 2.00, "good": 4.00, "average": 8.00, "poor": 12.00},
        "cpm_nonskip": {"excellent": 4.00, "good": 6.00, "average": 10.00, "poor": 15.00},
        "cpm_bumper": {"excellent": 2.00, "good": 3.50, "average": 6.00, "poor": 10.00},
        "conv_rate": {"poor": 0.005, "average": 0.015, "good": 0.030, "excellent": 0.050},
        "vtc_rate": {"poor": 0.001, "average": 0.003, "good": 0.008, "excellent": 0.015},
    },
    "ecommerce": {
        "view_rate": {"poor": 0.18, "average": 0.28, "good": 0.40, "excellent": 0.50},
        "cpv": {"excellent": 0.08, "good": 0.12, "average": 0.20, "poor": 0.30},
        "ctr_instream": {"poor": 0.004, "average": 0.008, "good": 0.015, "excellent": 0.025},
        "conv_rate": {"poor": 0.008, "average": 0.020, "good": 0.040, "excellent": 0.060},
    },
    "b2b_saas": {
        "view_rate": {"poor": 0.22, "average": 0.35, "good": 0.48, "excellent": 0.58},
        "cpv": {"excellent": 0.15, "good": 0.22, "average": 0.35, "poor": 0.50},
        "ctr_instream": {"poor": 0.002, "average": 0.004, "good": 0.007, "excellent": 0.012},
        "conv_rate": {"poor": 0.003, "average": 0.008, "good": 0.015, "excellent": 0.025},
    },
    "lead_gen": {
        "view_rate": {"poor": 0.20, "average": 0.30, "good": 0.42, "excellent": 0.52},
        "cpv": {"excellent": 0.10, "good": 0.18, "average": 0.28, "poor": 0.40},
        "ctr_instream": {"poor": 0.003, "average": 0.006, "good": 0.010, "excellent": 0.018},
        "conv_rate": {"poor": 0.005, "average": 0.012, "good": 0.025, "excellent": 0.040},
    },
    "mobile_app": {
        "view_rate": {"poor": 0.15, "average": 0.25, "good": 0.38, "excellent": 0.48},
        "cpv": {"excellent": 0.05, "good": 0.10, "average": 0.18, "poor": 0.25},
        "ctr_instream": {"poor": 0.005, "average": 0.010, "good": 0.020, "excellent": 0.035},
        "conv_rate": {"poor": 0.010, "average": 0.025, "good": 0.050, "excellent": 0.080},
    },
}

METRIC_LABELS = {
    "view_rate": "View Rate",
    "cpv": "Cost Per View",
    "ctr_instream": "CTR (In-Stream)",
    "ctr_infeed": "CTR (In-Feed)",
    "cpm_shorts": "CPM (Shorts)",
    "cpm_nonskip": "CPM (Non-Skippable)",
    "cpm_bumper": "CPM (Bumper)",
    "conv_rate": "Conversion Rate",
    "vtc_rate": "View-Through Conv Rate",
}


def rate_metric(value: float, benchmarks: Dict, lower_is_better: bool = False) -> Tuple[str, str]:
    """Rate a metric value against benchmarks. Returns (rating, color_indicator)."""
    if lower_is_better:
        if value <= benchmarks.get("excellent", 0):
            return "Excellent", "+++"
        elif value <= benchmarks.get("good", 0):
            return "Good", "++"
        elif value <= benchmarks.get("average", float("inf")):
            return "Average", "+"
        else:
            return "Poor", "---"
    else:
        if value >= benchmarks.get("excellent", float("inf")):
            return "Excellent", "+++"
        elif value >= benchmarks.get("good", 0):
            return "Good", "++"
        elif value >= benchmarks.get("average", 0):
            return "Average", "+"
        else:
            return "Poor", "---"


def compare_metrics(
    metrics: Dict[str, float],
    vertical: str = "all_industries",
) -> List[Dict]:
    """Compare provided metrics against benchmarks for a vertical."""
    benchmarks = VERTICAL_BENCHMARKS.get(vertical, VERTICAL_BENCHMARKS["all_industries"])
    results = []

    lower_is_better_metrics = {"cpv", "cpm_shorts", "cpm_nonskip", "cpm_bumper"}

    for metric_key, value in metrics.items():
        if metric_key in benchmarks:
            bench = benchmarks[metric_key]
            is_lower_better = metric_key in lower_is_better_metrics
            rating, indicator = rate_metric(value, bench, is_lower_better)

            result = {
                "metric": metric_key,
                "label": METRIC_LABELS.get(metric_key, metric_key),
                "value": value,
                "rating": rating,
                "indicator": indicator,
                "benchmarks": bench,
                "vs_average": value - bench.get("average", 0),
            }

            # Calculate improvement potential
            if rating in ("Poor", "Average"):
                target = bench.get("good", bench.get("average", 0))
                if is_lower_better:
                    result["improvement_target"] = target
                    result["improvement_needed"] = f"Reduce from {value:.4f} to {target:.4f}"
                else:
                    result["improvement_target"] = target
                    result["improvement_needed"] = f"Increase from {value:.4f} to {target:.4f}"
            else:
                result["improvement_needed"] = "On track"

            results.append(result)

    return results


def format_comparison_report(results: List[Dict], vertical: str) -> str:
    """Format benchmark comparison as a markdown report."""
    lines = []
    lines.append(f"## YouTube Ads Benchmark Comparison")
    lines.append(f"*Vertical: {vertical.replace('_', ' ').title()}*\n")

    lines.append("| Metric | Your Value | Rating | Avg Benchmark | vs Avg |")
    lines.append("|--------|-----------|--------|---------------|--------|")

    for r in results:
        value_fmt = f"{r['value']:.2%}" if r["value"] < 1 else f"${r['value']:.2f}"
        avg = r["benchmarks"].get("average", 0)
        avg_fmt = f"{avg:.2%}" if avg < 1 else f"${avg:.2f}"
        vs_avg = r["vs_average"]
        vs_fmt = f"+{vs_avg:.2%}" if vs_avg > 0 and r["value"] < 1 else f"{vs_avg:.2%}" if r["value"] < 1 else f"${vs_avg:+.2f}"

        lines.append(f"| {r['label']} | {value_fmt} | {r['indicator']} {r['rating']} | {avg_fmt} | {vs_fmt} |")

    # Improvement recommendations
    needs_improvement = [r for r in results if r["rating"] in ("Poor", "Average")]
    if needs_improvement:
        lines.append(f"\n### Improvement Priorities\n")
        for i, r in enumerate(needs_improvement, 1):
            lines.append(f"{i}. **{r['label']}**: {r['improvement_needed']}")

    performing_well = [r for r in results if r["rating"] in ("Good", "Excellent")]
    if performing_well:
        lines.append(f"\n### Performing Well\n")
        for r in performing_well:
            lines.append(f"- **{r['label']}**: {r['rating']} ({r['indicator']})")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Compare YouTube Ads metrics against benchmarks")
    parser.add_argument("--view-rate", type=float, help="View rate (decimal, e.g., 0.35 for 35%%)")
    parser.add_argument("--cpv", type=float, help="Cost per view (e.g., 0.12)")
    parser.add_argument("--ctr", type=float, help="Click-through rate for in-stream (decimal)")
    parser.add_argument("--ctr-infeed", type=float, help="CTR for in-feed ads (decimal)")
    parser.add_argument("--cpm-shorts", type=float, help="CPM for Shorts ads")
    parser.add_argument("--cpm-nonskip", type=float, help="CPM for non-skippable ads")
    parser.add_argument("--cpm-bumper", type=float, help="CPM for bumper ads")
    parser.add_argument("--conv-rate", type=float, help="Conversion rate (decimal)")
    parser.add_argument("--vtc-rate", type=float, help="View-through conversion rate (decimal)")
    parser.add_argument("--vertical", choices=list(VERTICAL_BENCHMARKS.keys()),
                        default="all_industries", help="Industry vertical for benchmarks")
    parser.add_argument("--input", help="JSON file with metrics")
    parser.add_argument("--output", choices=["json", "report"], default="report")

    args = parser.parse_args()

    # Build metrics dict
    metrics = {}
    if args.input:
        with open(args.input) as f:
            metrics = json.load(f)
    else:
        if args.view_rate is not None:
            metrics["view_rate"] = args.view_rate
        if args.cpv is not None:
            metrics["cpv"] = args.cpv
        if args.ctr is not None:
            metrics["ctr_instream"] = args.ctr
        if args.ctr_infeed is not None:
            metrics["ctr_infeed"] = args.ctr_infeed
        if args.cpm_shorts is not None:
            metrics["cpm_shorts"] = args.cpm_shorts
        if args.cpm_nonskip is not None:
            metrics["cpm_nonskip"] = args.cpm_nonskip
        if args.cpm_bumper is not None:
            metrics["cpm_bumper"] = args.cpm_bumper
        if args.conv_rate is not None:
            metrics["conv_rate"] = args.conv_rate
        if args.vtc_rate is not None:
            metrics["vtc_rate"] = args.vtc_rate

    if not metrics:
        print("Error: Provide at least one metric to compare.", file=sys.stderr)
        sys.exit(1)

    results = compare_metrics(metrics, args.vertical)

    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        print(format_comparison_report(results, args.vertical))


if __name__ == "__main__":
    main()
