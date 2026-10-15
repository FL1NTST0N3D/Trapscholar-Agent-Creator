#!/usr/bin/env python3
"""
QS Distribution Analyzer
Generates histogram analysis of Quality Score distribution.

Usage:
    python qs_distribution.py <csv_file> [--by campaign|ad_group|landing_page]
"""

import csv
import sys
import json
import argparse
from pathlib import Path
from collections import defaultdict


CPC_MULTIPLIERS = {
    1: 5.00, 2: 4.00, 3: 3.00, 4: 2.00, 5: 1.67,
    6: 1.25, 7: 1.00, 8: 0.83, 9: 0.67, 10: 0.50,
}

BANDS = {
    "Critical (1-2)": (1, 2),
    "Poor (3-4)": (3, 4),
    "Average (5-6)": (5, 6),
    "Good (7)": (7, 7),
    "Excellent (8-10)": (8, 10),
}


def parse_number(value: str) -> float:
    if not value or value in ("--", "—"):
        return 0.0
    return float(value.replace("$", "").replace(",", "").replace("%", "").strip() or "0")


def load_keywords(csv_file: str) -> list[dict]:
    """Load keywords from CSV."""
    keywords = []
    with open(csv_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            qs_str = (row.get("Quality Score") or row.get("Quality score") or
                      row.get("Qual. Score") or "")
            if not qs_str or qs_str in ("--", "—"):
                qs = None
            else:
                try:
                    qs = int(float(qs_str))
                    if qs < 1 or qs > 10:
                        qs = None
                except ValueError:
                    qs = None

            cost_str = row.get("Cost") or row.get("cost") or row.get("Spend") or "0"
            impr_str = row.get("Impressions") or row.get("Impr.") or "0"

            keywords.append({
                "keyword": (row.get("Keyword") or row.get("keyword") or "unknown"),
                "quality_score": qs,
                "cost": parse_number(cost_str),
                "impressions": int(parse_number(impr_str)),
                "campaign": row.get("Campaign") or row.get("campaign") or "unknown",
                "ad_group": row.get("Ad group") or row.get("Ad Group") or "unknown",
                "final_url": row.get("Final URL") or row.get("Final url") or "",
            })
    return keywords


def compute_distribution(keywords: list[dict]) -> dict:
    """Compute QS distribution metrics."""
    with_qs = [kw for kw in keywords if kw["quality_score"] is not None]
    null_qs = [kw for kw in keywords if kw["quality_score"] is None]

    if not with_qs:
        return {"error": "No keywords with Quality Score data found."}

    total = len(with_qs)
    total_spend = sum(kw["cost"] for kw in with_qs)
    total_impressions = sum(kw["impressions"] for kw in with_qs)

    # Per-QS distribution
    qs_dist = {}
    for qs_val in range(1, 11):
        kws = [kw for kw in with_qs if kw["quality_score"] == qs_val]
        spend = sum(kw["cost"] for kw in kws)
        qs_dist[qs_val] = {
            "count": len(kws),
            "pct": round(len(kws) / total * 100, 1),
            "spend": round(spend, 2),
            "spend_pct": round(spend / total_spend * 100, 1) if total_spend > 0 else 0,
        }

    # Band distribution
    band_dist = {}
    for band_name, (low, high) in BANDS.items():
        kws = [kw for kw in with_qs if low <= kw["quality_score"] <= high]
        spend = sum(kw["cost"] for kw in kws)
        band_dist[band_name] = {
            "count": len(kws),
            "pct": round(len(kws) / total * 100, 1),
            "spend": round(spend, 2),
            "spend_pct": round(spend / total_spend * 100, 1) if total_spend > 0 else 0,
        }

    # Key metrics
    at_7_plus = sum(1 for kw in with_qs if kw["quality_score"] >= 7)
    at_1_4 = sum(1 for kw in with_qs if kw["quality_score"] <= 4)

    weighted_avg = 0.0
    if total_impressions > 0:
        weighted_avg = sum(
            kw["quality_score"] * kw["impressions"] for kw in with_qs
        ) / total_impressions

    qs_values = sorted([kw["quality_score"] for kw in with_qs])
    median = qs_values[len(qs_values) // 2]

    mean = sum(kw["quality_score"] for kw in with_qs) / total
    variance = sum((kw["quality_score"] - mean) ** 2 for kw in with_qs) / total
    std_dev = variance ** 0.5

    # Determine distribution shape
    peak_qs = max(qs_dist.keys(), key=lambda q: qs_dist[q]["count"])
    if peak_qs >= 7:
        shape = "Right-skewed (healthy)"
    elif peak_qs <= 4:
        shape = "Left-skewed (problematic)"
    else:
        # Check for bimodal
        counts = [qs_dist[q]["count"] for q in range(1, 11)]
        peaks = [i + 1 for i in range(1, 9) if counts[i] > counts[i-1] and counts[i] > counts[i+1]]
        if len(peaks) >= 2:
            shape = f"Bimodal (peaks at QS {peaks[0]} and {peaks[-1]})"
        else:
            shape = "Center-weighted (average)"

    # Grade
    pct_7_plus = at_7_plus / total * 100
    if pct_7_plus >= 70 and weighted_avg > 7.5:
        grade = "A"
    elif pct_7_plus >= 60 and weighted_avg >= 6.5:
        grade = "B"
    elif pct_7_plus >= 45 and weighted_avg >= 5.5:
        grade = "C"
    elif pct_7_plus >= 30 and weighted_avg >= 4.5:
        grade = "D"
    else:
        grade = "F"

    return {
        "total_keywords": len(keywords),
        "keywords_with_qs": total,
        "keywords_null_qs": len(null_qs),
        "total_spend": round(total_spend, 2),
        "weighted_avg_qs": round(weighted_avg, 1),
        "median_qs": median,
        "std_dev": round(std_dev, 2),
        "pct_at_7_plus": round(pct_7_plus, 1),
        "pct_at_1_4": round(at_1_4 / total * 100, 1),
        "distribution_shape": shape,
        "grade": grade,
        "per_qs": qs_dist,
        "bands": band_dist,
    }


def compute_segmented(keywords: list[dict], segment_by: str) -> dict:
    """Compute distribution segmented by campaign, ad group, or landing page."""
    segments = defaultdict(list)
    key_map = {
        "campaign": "campaign",
        "ad_group": "ad_group",
        "landing_page": "final_url",
    }
    key = key_map.get(segment_by, "campaign")

    for kw in keywords:
        if kw["quality_score"] is not None:
            segments[kw[key]].append(kw)

    results = {}
    for segment_name, kws in sorted(segments.items(), key=lambda x: -sum(k["cost"] for k in x[1])):
        total = len(kws)
        if total == 0:
            continue
        avg_qs = sum(kw["quality_score"] for kw in kws) / total
        spend = sum(kw["cost"] for kw in kws)
        at_7_plus = sum(1 for kw in kws if kw["quality_score"] >= 7)

        results[segment_name] = {
            "keyword_count": total,
            "avg_qs": round(avg_qs, 1),
            "spend": round(spend, 2),
            "pct_at_7_plus": round(at_7_plus / total * 100, 1),
        }

    return results


def format_histogram(dist: dict) -> str:
    """Generate text-based histogram."""
    lines = []
    lines.append("=" * 65)
    lines.append("QUALITY SCORE DISTRIBUTION")
    lines.append("=" * 65)
    lines.append("")
    lines.append(f"Grade: {dist['grade']}")
    lines.append(f"Total keywords: {dist['total_keywords']} ({dist['keywords_with_qs']} with QS, {dist['keywords_null_qs']} null)")
    lines.append(f"Weighted Avg QS: {dist['weighted_avg_qs']}")
    lines.append(f"Median QS: {dist['median_qs']}")
    lines.append(f"Std Dev: {dist['std_dev']}")
    lines.append(f"% at QS 7+: {dist['pct_at_7_plus']}%")
    lines.append(f"Distribution shape: {dist['distribution_shape']}")
    lines.append("")

    # Histogram
    max_count = max(d["count"] for d in dist["per_qs"].values()) if dist["per_qs"] else 1
    scale = 40 / max_count if max_count > 0 else 1

    lines.append("QS   Count   %KWs   %Spend  Histogram")
    lines.append("-" * 65)
    for qs in range(1, 11):
        d = dist["per_qs"][qs]
        bar = "#" * int(d["count"] * scale)
        lines.append(
            f"QS {qs:>2}  {d['count']:>5}  {d['pct']:>5.1f}%  {d['spend_pct']:>5.1f}%   {bar}"
        )
    lines.append("")

    # Band summary
    lines.append("Band Summary")
    lines.append("-" * 65)
    lines.append(f"{'Band':<20} {'Keywords':>8} {'%KWs':>6} {'Spend':>12} {'%Spend':>7}")
    lines.append("-" * 65)
    for band, d in dist["bands"].items():
        lines.append(
            f"{band:<20} {d['count']:>8} {d['pct']:>5.1f}% ${d['spend']:>10,.2f} {d['spend_pct']:>5.1f}%"
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="QS Distribution Analyzer")
    parser.add_argument("csv_file", help="Path to Google Ads keyword CSV")
    parser.add_argument("--by", choices=["campaign", "ad_group", "landing_page"],
                        help="Segment distribution by dimension")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    if not Path(args.csv_file).exists():
        print(f"Error: File not found: {args.csv_file}", file=sys.stderr)
        sys.exit(1)

    keywords = load_keywords(args.csv_file)
    dist = compute_distribution(keywords)

    if args.format == "json":
        output = {"distribution": dist}
        if args.by:
            output["segmented"] = compute_segmented(keywords, args.by)
        print(json.dumps(output, indent=2))
    else:
        print(format_histogram(dist))
        if args.by:
            segments = compute_segmented(keywords, args.by)
            print(f"\n{'=' * 65}")
            print(f"SEGMENTED BY {args.by.upper().replace('_', ' ')}")
            print(f"{'=' * 65}")
            print(f"{'Segment':<40} {'KWs':>5} {'Avg QS':>7} {'%7+':>6} {'Spend':>12}")
            print("-" * 65)
            for name, data in list(segments.items())[:20]:
                display_name = (name or "(empty)")[:38]
                print(
                    f"{display_name:<40} {data['keyword_count']:>5} "
                    f"{data['avg_qs']:>7.1f} {data['pct_at_7_plus']:>5.1f}% "
                    f"${data['spend']:>10,.2f}"
                )


if __name__ == "__main__":
    main()
