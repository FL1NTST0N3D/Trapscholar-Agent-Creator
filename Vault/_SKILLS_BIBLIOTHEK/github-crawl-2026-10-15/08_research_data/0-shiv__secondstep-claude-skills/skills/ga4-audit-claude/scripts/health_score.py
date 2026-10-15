#!/usr/bin/env python3
"""
GA4 Health Score Calculator

Calculates the overall GA4 Health Score based on individual dimension scores.
Supports both e-commerce and non-e-commerce property types.

Usage:
    python health_score.py --scores '{"data_streams": 80, "events": 65, ...}'
    python health_score.py --file audit_results.json
    python health_score.py --interactive
"""

import argparse
import json
import sys
from typing import Dict, Optional, Tuple


# Weight definitions
ECOMMERCE_WEIGHTS = {
    "data_streams": 0.10,
    "events": 0.20,
    "conversions": 0.15,
    "audiences": 0.10,
    "attribution": 0.10,
    "ecommerce": 0.15,
    "custom_dimensions": 0.10,
    "integrations": 0.10,
}

NON_ECOMMERCE_WEIGHTS = {
    "data_streams": 0.10,
    "events": 0.25,
    "conversions": 0.20,
    "audiences": 0.10,
    "attribution": 0.10,
    "ecommerce": 0.00,
    "custom_dimensions": 0.15,
    "integrations": 0.10,
}

GRADE_THRESHOLDS = [
    (90, "A", "Excellent"),
    (75, "B", "Good"),
    (50, "C", "Fair"),
    (25, "D", "Poor"),
    (0, "F", "Critical"),
]

DIMENSION_LABELS = {
    "data_streams": "Data Streams",
    "events": "Events",
    "conversions": "Conversions",
    "audiences": "Audiences",
    "attribution": "Attribution",
    "ecommerce": "E-commerce",
    "custom_dimensions": "Custom Dimensions",
    "integrations": "Integrations",
}


def get_grade(score: float) -> Tuple[str, str]:
    """Return letter grade and label for a given score."""
    for threshold, grade, label in GRADE_THRESHOLDS:
        if score >= threshold:
            return grade, label
    return "F", "Critical"


def calculate_health_score(
    scores: Dict[str, float],
    is_ecommerce: bool = True,
) -> Dict:
    """
    Calculate the overall GA4 Health Score.

    Args:
        scores: Dictionary of dimension name to score (0-100).
        is_ecommerce: Whether the property is e-commerce.

    Returns:
        Dictionary with health_score, grade, label, and dimension breakdown.
    """
    weights = ECOMMERCE_WEIGHTS if is_ecommerce else NON_ECOMMERCE_WEIGHTS

    weighted_sum = 0.0
    total_weight = 0.0
    dimension_breakdown = []

    for dimension, weight in weights.items():
        score = scores.get(dimension)
        if score is not None and weight > 0:
            weighted_sum += score * weight
            total_weight += weight
            grade, label = get_grade(score)
            dimension_breakdown.append({
                "dimension": DIMENSION_LABELS.get(dimension, dimension),
                "score": score,
                "weight": f"{weight * 100:.0f}%",
                "grade": grade,
                "label": label,
                "weighted_contribution": score * weight,
            })

    # Normalize if total weight doesn't sum to 1.0 (e.g., missing dimensions)
    if total_weight > 0:
        health_score = weighted_sum / total_weight
    else:
        health_score = 0.0

    overall_grade, overall_label = get_grade(health_score)

    return {
        "health_score": round(health_score, 1),
        "grade": overall_grade,
        "label": overall_label,
        "is_ecommerce": is_ecommerce,
        "dimensions": dimension_breakdown,
        "total_dimensions_scored": len(dimension_breakdown),
    }


def print_report(result: Dict) -> None:
    """Print a formatted health score report to stdout."""
    print("\n" + "=" * 60)
    print(f"  GA4 HEALTH SCORE: {result['health_score']}/100")
    print(f"  Grade: {result['grade']} - {result['label']}")
    print(f"  Property Type: {'E-commerce' if result['is_ecommerce'] else 'Non-E-commerce'}")
    print("=" * 60)
    print()
    print(f"{'Dimension':<22} {'Score':>6} {'Weight':>7} {'Grade':>6}")
    print("-" * 45)

    for dim in result["dimensions"]:
        print(
            f"{dim['dimension']:<22} {dim['score']:>5.1f} {dim['weight']:>7} {dim['grade']:>5}"
        )

    print("-" * 45)
    print(f"{'OVERALL':<22} {result['health_score']:>5.1f} {'100%':>7} {result['grade']:>5}")
    print()


def interactive_mode() -> Dict[str, float]:
    """Collect scores interactively from the user."""
    print("\nGA4 Health Score Calculator")
    print("-" * 30)
    print("Enter scores (0-100) for each dimension.")
    print("Press Enter to skip a dimension.\n")

    scores = {}
    for key, label in DIMENSION_LABELS.items():
        while True:
            value = input(f"  {label}: ").strip()
            if value == "":
                break
            try:
                score = float(value)
                if 0 <= score <= 100:
                    scores[key] = score
                    break
                else:
                    print("    Score must be between 0 and 100.")
            except ValueError:
                print("    Please enter a number.")

    return scores


def main():
    parser = argparse.ArgumentParser(
        description="Calculate GA4 Health Score from dimension audit scores."
    )
    parser.add_argument(
        "--scores",
        type=str,
        help='JSON string of scores, e.g. \'{"events": 80, "conversions": 65}\'',
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Path to JSON file containing scores",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Enter scores interactively",
    )
    parser.add_argument(
        "--non-ecommerce",
        action="store_true",
        help="Use non-e-commerce weights (default: e-commerce)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as JSON instead of formatted text",
    )

    args = parser.parse_args()

    # Determine input source
    if args.interactive:
        scores = interactive_mode()
    elif args.file:
        with open(args.file, "r") as f:
            data = json.load(f)
            scores = data.get("scores", data)
    elif args.scores:
        scores = json.loads(args.scores)
    else:
        parser.print_help()
        sys.exit(1)

    is_ecommerce = not args.non_ecommerce
    result = calculate_health_score(scores, is_ecommerce)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)


if __name__ == "__main__":
    main()
