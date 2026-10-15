#!/usr/bin/env python3
"""
YouTube Ads Score Calculator

Computes the composite YouTube Ads Score (0-100) from individual
dimension scores using the weighted scoring model.

Usage:
    python score_calculator.py --structure 75 --creative 60 --targeting 80 \
        --bidding 70 --placements 55 --remarketing 40 --shorts 30 --measurement 85

Author: Shivendra Rawat (@0-shiv)
License: MIT
"""

import argparse
import json
import sys
from typing import Dict, Optional


# Dimension weights (must sum to 1.0)
WEIGHTS = {
    "structure": 0.15,
    "creative": 0.20,
    "targeting": 0.15,
    "bidding": 0.10,
    "placements": 0.10,
    "remarketing": 0.10,
    "shorts": 0.10,
    "measurement": 0.10,
}

# Rating thresholds
RATINGS = [
    (90, "Elite", "Top 2% of YouTube advertisers. Maintain and iterate."),
    (70, "Strong", "Minor optimizations needed. Focus on weakest dimensions."),
    (50, "Average", "Significant improvement opportunities. Prioritize critical gaps."),
    (30, "Weak", "Fundamental issues in strategy or setup. Needs major overhaul."),
    (0, "Critical", "Campaign is likely wasting budget. Immediate intervention required."),
]

# Dimension descriptions
DIMENSION_INFO = {
    "structure": {
        "name": "Campaign Structure",
        "description": "Objective alignment, format mix, naming conventions, budget distribution",
        "key_factors": [
            "Objective-to-format alignment",
            "Campaign naming convention",
            "Budget distribution across campaigns",
            "Format coverage (6 YouTube ad formats)",
            "Frequency cap management",
        ],
    },
    "creative": {
        "name": "Creative Quality",
        "description": "ABCD framework compliance, hook quality, CTA clarity",
        "key_factors": [
            "Hook quality (first 5 seconds)",
            "Brand appearance timing and integration",
            "Storytelling and emotional connection",
            "CTA clarity and urgency",
            "Audio quality and caption usage",
        ],
    },
    "targeting": {
        "name": "Targeting Precision",
        "description": "Audience selection, layering strategy, exclusion hygiene",
        "key_factors": [
            "Custom Intent audience usage",
            "In-Market segment selection",
            "Remarketing list depth",
            "Demographic layering",
            "Audience exclusions (converters, irrelevant segments)",
        ],
    },
    "bidding": {
        "name": "Bidding Strategy",
        "description": "Bid type alignment, conversion maturity, seasonal adjustments",
        "key_factors": [
            "Bid strategy matches campaign objective",
            "Campaign maturity stage alignment",
            "Conversion volume for automated bidding",
            "Realistic bid targets",
            "Seasonal adjustments configured",
        ],
    },
    "placements": {
        "name": "Placement Hygiene",
        "description": "Channel exclusions, brand safety, inventory type",
        "key_factors": [
            "Inventory type selection (Expanded/Standard/Limited)",
            "Content exclusion configuration",
            "Channel exclusion list",
            "Placement performance review",
            "Brand safety vendor integration",
        ],
    },
    "remarketing": {
        "name": "Remarketing Depth",
        "description": "Funnel stages, sequential messaging, list freshness",
        "key_factors": [
            "Video viewer remarketing lists (tiered by engagement)",
            "Website visitor remarketing integration",
            "Customer Match list usage",
            "Sequential messaging strategy",
            "Cross-platform remarketing (YouTube + Search + Display)",
        ],
    },
    "shorts": {
        "name": "Shorts Readiness",
        "description": "Vertical creative, mobile-first approach, native feel",
        "key_factors": [
            "Vertical (9:16) native creative",
            "Mobile-first design and pacing",
            "Native Shorts feed aesthetic",
            "Shorts-specific bidding and audience strategy",
            "Creative refresh cadence (every 2-3 weeks)",
        ],
    },
    "measurement": {
        "name": "Measurement Setup",
        "description": "Conversion tracking, attribution, view-through windows",
        "key_factors": [
            "Google Ads conversion tag active",
            "View-through conversion window (30 days recommended)",
            "Enhanced Conversions enabled",
            "GA4 linked to Google Ads",
            "YouTube channel linked to Google Ads",
        ],
    },
}


def get_rating(score: float) -> tuple:
    """Return rating label and description for a given score."""
    for threshold, label, description in RATINGS:
        if score >= threshold:
            return label, description
    return "Critical", RATINGS[-1][2]


def calculate_score(dimensions: Dict[str, Optional[float]]) -> Dict:
    """Calculate the composite YouTube Ads Score."""
    scored_dimensions = {}
    total_weight = 0.0
    weighted_sum = 0.0
    missing_dimensions = []

    for dim, weight in WEIGHTS.items():
        score = dimensions.get(dim)
        if score is not None:
            score = max(0, min(100, score))  # Clamp to 0-100
            weighted_score = score * weight
            rating, _ = get_rating(score)
            scored_dimensions[dim] = {
                "name": DIMENSION_INFO[dim]["name"],
                "score": score,
                "weight": weight,
                "weighted_score": round(weighted_score, 1),
                "rating": rating,
                "description": DIMENSION_INFO[dim]["description"],
                "key_factors": DIMENSION_INFO[dim]["key_factors"],
            }
            total_weight += weight
            weighted_sum += weighted_score
        else:
            missing_dimensions.append(dim)

    # Normalize if some dimensions are missing
    if total_weight > 0 and total_weight < 1.0:
        composite_score = round(weighted_sum / total_weight, 1)
        confidence = "partial"
    elif total_weight >= 1.0:
        composite_score = round(weighted_sum, 1)
        confidence = "full"
    else:
        composite_score = 0
        confidence = "none"

    overall_rating, overall_description = get_rating(composite_score)

    # Identify weakest and strongest dimensions
    if scored_dimensions:
        weakest = min(scored_dimensions.items(), key=lambda x: x[1]["score"])
        strongest = max(scored_dimensions.items(), key=lambda x: x[1]["score"])
    else:
        weakest = strongest = (None, None)

    result = {
        "composite_score": composite_score,
        "rating": overall_rating,
        "rating_description": overall_description,
        "confidence": confidence,
        "dimensions_scored": len(scored_dimensions),
        "dimensions_total": len(WEIGHTS),
        "dimensions": scored_dimensions,
        "missing_dimensions": missing_dimensions,
        "weakest_dimension": {
            "name": weakest[1]["name"] if weakest[1] else "N/A",
            "score": weakest[1]["score"] if weakest[1] else 0,
        },
        "strongest_dimension": {
            "name": strongest[1]["name"] if strongest[1] else "N/A",
            "score": strongest[1]["score"] if strongest[1] else 0,
        },
    }

    return result


def format_report(result: Dict) -> str:
    """Format the score result as a markdown report."""
    lines = []
    lines.append(f"## YouTube Ads Score: {result['composite_score']}/100 — {result['rating']}")
    lines.append(f"\n{result['rating_description']}\n")

    if result["confidence"] == "partial":
        lines.append(f"*Note: Score based on {result['dimensions_scored']}/{result['dimensions_total']} dimensions. "
                      f"Missing: {', '.join(result['missing_dimensions'])}*\n")

    lines.append("| Dimension | Score | Weight | Weighted | Rating |")
    lines.append("|-----------|-------|--------|----------|--------|")

    for dim_key in WEIGHTS:
        if dim_key in result["dimensions"]:
            d = result["dimensions"][dim_key]
            lines.append(
                f"| {d['name']} | {d['score']}/100 | {d['weight']:.0%} | "
                f"{d['weighted_score']:.1f} | {d['rating']} |"
            )
        else:
            info = DIMENSION_INFO[dim_key]
            lines.append(
                f"| {info['name']} | N/A | {WEIGHTS[dim_key]:.0%} | -- | Not assessed |"
            )

    lines.append(f"| **TOTAL** | | **100%** | **{result['composite_score']}** | **{result['rating']}** |")

    lines.append(f"\n### Priority Focus")
    lines.append(f"- **Weakest dimension:** {result['weakest_dimension']['name']} "
                  f"({result['weakest_dimension']['score']}/100) — improve this first")
    lines.append(f"- **Strongest dimension:** {result['strongest_dimension']['name']} "
                  f"({result['strongest_dimension']['score']}/100) — maintain this")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Calculate YouTube Ads Score")
    parser.add_argument("--structure", type=float, help="Campaign Structure score (0-100)")
    parser.add_argument("--creative", type=float, help="Creative Quality score (0-100)")
    parser.add_argument("--targeting", type=float, help="Targeting Precision score (0-100)")
    parser.add_argument("--bidding", type=float, help="Bidding Strategy score (0-100)")
    parser.add_argument("--placements", type=float, help="Placement Hygiene score (0-100)")
    parser.add_argument("--remarketing", type=float, help="Remarketing Depth score (0-100)")
    parser.add_argument("--shorts", type=float, help="Shorts Readiness score (0-100)")
    parser.add_argument("--measurement", type=float, help="Measurement Setup score (0-100)")
    parser.add_argument("--output", choices=["json", "report"], default="report",
                        help="Output format (default: report)")

    args = parser.parse_args()

    dimensions = {
        "structure": args.structure,
        "creative": args.creative,
        "targeting": args.targeting,
        "bidding": args.bidding,
        "placements": args.placements,
        "remarketing": args.remarketing,
        "shorts": args.shorts,
        "measurement": args.measurement,
    }

    # Remove None values
    dimensions = {k: v for k, v in dimensions.items() if v is not None}

    if not dimensions:
        print("Error: Provide at least one dimension score.", file=sys.stderr)
        print("Example: python score_calculator.py --structure 75 --creative 60", file=sys.stderr)
        sys.exit(1)

    result = calculate_score(dimensions)

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print(format_report(result))


if __name__ == "__main__":
    main()
