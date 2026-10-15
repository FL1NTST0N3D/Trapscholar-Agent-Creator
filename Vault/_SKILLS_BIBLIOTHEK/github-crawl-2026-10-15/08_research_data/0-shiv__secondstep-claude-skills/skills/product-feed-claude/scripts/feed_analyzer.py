#!/usr/bin/env python3
"""
Feed Analyzer — Product Feed Quality Scoring Tool

Parses CSV/TSV feed files and scores product titles, descriptions,
images, and attribute completeness. Outputs summary statistics and
a per-product quality report.

Usage:
    python feed_analyzer.py <feed_file> [--output report.csv] [--format csv|tsv]

Author: Shivendra Rawat (@0-shiv) | Second Step
"""

import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_ATTRIBUTES = [
    "id", "title", "description", "link", "image_link",
    "availability", "price", "brand", "condition",
]

GTIN_ATTRIBUTES = ["gtin", "mpn"]  # At least one needed if branded

RECOMMENDED_ATTRIBUTES = [
    "additional_image_link", "sale_price", "product_type",
    "google_product_category", "color", "size", "material",
    "pattern", "gender", "age_group", "item_group_id",
    "product_highlight", "shipping", "custom_label_0",
]

APPAREL_REQUIRED = ["gender", "age_group", "color", "size"]

VALID_AVAILABILITY = {"in_stock", "out_of_stock", "preorder", "backorder"}
VALID_CONDITION = {"new", "refurbished", "used"}

PROMOTIONAL_WORDS = [
    "sale", "discount", "free shipping", "best price", "limited time",
    "buy now", "clearance", "deal", "offer", "cheapest", "lowest price",
    "% off", "save", "bargain",
]

TITLE_MIN_LENGTH = 30
TITLE_OPTIMAL_MIN = 80
TITLE_OPTIMAL_MAX = 120
TITLE_MAX_LENGTH = 150

DESC_MIN_LENGTH = 100
DESC_OPTIMAL_MIN = 750
DESC_OPTIMAL_MAX = 1500
DESC_MAX_LENGTH = 5000


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class ProductScore:
    product_id: str
    title_score: int = 0
    description_score: int = 0
    image_score: int = 0
    attribute_score: int = 0
    overall_score: int = 0
    issues: list = field(default_factory=list)


@dataclass
class FeedSummary:
    total_products: int = 0
    avg_title_score: float = 0
    avg_description_score: float = 0
    avg_image_score: float = 0
    avg_attribute_score: float = 0
    overall_score: float = 0
    approval_rate: float = 0
    missing_required: dict = field(default_factory=dict)
    missing_recommended: dict = field(default_factory=dict)
    title_length_avg: float = 0
    desc_length_avg: float = 0
    products_with_issues: int = 0
    grade: str = "F"


# ---------------------------------------------------------------------------
# Scoring functions
# ---------------------------------------------------------------------------

def score_title(product: dict) -> tuple[int, list]:
    """Score a product title 0-100."""
    issues = []
    title = product.get("title", "").strip()

    if not title:
        return 0, ["Missing title"]

    score = 100
    length = len(title)

    # Length scoring
    if length < TITLE_MIN_LENGTH:
        score -= 40
        issues.append(f"Title too short ({length} chars, min {TITLE_MIN_LENGTH})")
    elif length < TITLE_OPTIMAL_MIN:
        score -= 15
        issues.append(f"Title below optimal length ({length} chars, target {TITLE_OPTIMAL_MIN}-{TITLE_OPTIMAL_MAX})")
    elif length > TITLE_MAX_LENGTH:
        score -= 30
        issues.append(f"Title exceeds max ({length} chars, max {TITLE_MAX_LENGTH})")
    elif length > TITLE_OPTIMAL_MAX:
        score -= 5
        issues.append(f"Title slightly long ({length} chars)")

    # Brand first check
    brand = product.get("brand", "").strip()
    if brand and not title.lower().startswith(brand.lower()):
        score -= 15
        issues.append(f"Brand '{brand}' not at start of title")

    # Promotional text check
    title_lower = title.lower()
    for word in PROMOTIONAL_WORDS:
        if word in title_lower:
            score -= 20
            issues.append(f"Promotional text in title: '{word}'")
            break

    # ALL CAPS check (more than 50% uppercase, excluding short titles)
    if length > 10:
        upper_ratio = sum(1 for c in title if c.isupper()) / max(sum(1 for c in title if c.isalpha()), 1)
        if upper_ratio > 0.5:
            score -= 15
            issues.append("Excessive capitalization in title")

    # Key attribute presence (color, size, material)
    has_color = bool(product.get("color", "").strip())
    has_size = bool(product.get("size", "").strip())
    color_in_title = has_color and product["color"].lower() in title_lower
    size_in_title = has_size and product["size"].lower() in title_lower

    if has_color and not color_in_title:
        score -= 5
        issues.append("Color attribute exists but not in title")
    if has_size and not size_in_title:
        score -= 5
        issues.append("Size attribute exists but not in title")

    return max(0, score), issues


def score_description(product: dict) -> tuple[int, list]:
    """Score a product description 0-100."""
    issues = []
    desc = product.get("description", "").strip()

    if not desc:
        return 0, ["Missing description"]

    score = 100
    length = len(desc)

    # Length scoring
    if length < DESC_MIN_LENGTH:
        score -= 40
        issues.append(f"Description too short ({length} chars, min {DESC_MIN_LENGTH})")
    elif length < DESC_OPTIMAL_MIN:
        score -= 15
        issues.append(f"Description below optimal ({length} chars, target {DESC_OPTIMAL_MIN}+)")
    elif length > DESC_MAX_LENGTH:
        score -= 10
        issues.append(f"Description exceeds max ({length} chars)")

    # Promotional text check
    desc_lower = desc.lower()
    for word in PROMOTIONAL_WORDS:
        if word in desc_lower:
            score -= 20
            issues.append(f"Promotional text in description: '{word}'")
            break

    # HTML check
    if re.search(r"<[a-z]+[^>]*>", desc, re.IGNORECASE):
        score -= 15
        issues.append("HTML tags found in description")

    # Placeholder check
    placeholders = ["tbd", "coming soon", "n/a", "description coming soon", "no description"]
    if desc_lower.strip() in placeholders or len(desc_lower.strip()) < 20:
        score -= 40
        issues.append("Placeholder or minimal description")

    # Duplicate of title check
    title = product.get("title", "").strip()
    if title and desc.strip() == title.strip():
        score -= 25
        issues.append("Description is identical to title")

    return max(0, score), issues


def score_image(product: dict) -> tuple[int, list]:
    """Score image attributes 0-100 (URL-level checks only, no download)."""
    issues = []
    image_link = product.get("image_link", "").strip()

    if not image_link:
        return 0, ["Missing image_link"]

    score = 100

    # URL format check
    if not image_link.startswith(("http://", "https://")):
        score -= 30
        issues.append("Image URL does not start with http:// or https://")

    # HTTPS preference
    if image_link.startswith("http://"):
        score -= 5
        issues.append("Image URL uses HTTP instead of HTTPS")

    # File extension check
    valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp")
    url_path = image_link.split("?")[0].lower()
    if not any(url_path.endswith(ext) for ext in valid_extensions):
        score -= 10
        issues.append("Image URL does not end with a recognized image extension")

    # Additional images check
    additional = product.get("additional_image_link", "").strip()
    if not additional:
        score -= 15
        issues.append("No additional_image_link — add 2-5 extra images for higher CTR")

    # Placeholder image detection (common patterns)
    placeholder_patterns = ["placeholder", "no-image", "noimage", "coming-soon", "default"]
    for pattern in placeholder_patterns:
        if pattern in image_link.lower():
            score -= 30
            issues.append(f"Image URL contains placeholder pattern: '{pattern}'")
            break

    return max(0, score), issues


def score_attributes(product: dict, all_headers: list) -> tuple[int, list]:
    """Score attribute completeness 0-100."""
    issues = []
    score = 100

    # Required attributes
    missing_required = []
    for attr in REQUIRED_ATTRIBUTES:
        if attr not in all_headers or not product.get(attr, "").strip():
            missing_required.append(attr)

    if missing_required:
        penalty = min(60, len(missing_required) * 12)
        score -= penalty
        issues.append(f"Missing required: {', '.join(missing_required)}")

    # GTIN/MPN check (at least one needed for branded products)
    has_gtin = bool(product.get("gtin", "").strip())
    has_mpn = bool(product.get("mpn", "").strip())
    has_brand = bool(product.get("brand", "").strip())

    if has_brand and not has_gtin and not has_mpn:
        identifier_exists = product.get("identifier_exists", "").strip().lower()
        if identifier_exists != "false":
            score -= 10
            issues.append("Branded product missing GTIN and MPN")

    # GTIN validation (check digit)
    gtin = product.get("gtin", "").strip()
    if gtin and not validate_gtin(gtin):
        score -= 15
        issues.append(f"Invalid GTIN check digit: {gtin}")

    # Availability validation
    availability = product.get("availability", "").strip().lower()
    if availability and availability not in VALID_AVAILABILITY:
        score -= 15
        issues.append(f"Invalid availability value: '{availability}' (must be one of: {', '.join(VALID_AVAILABILITY)})")

    # Condition validation
    condition = product.get("condition", "").strip().lower()
    if condition and condition not in VALID_CONDITION:
        score -= 10
        issues.append(f"Invalid condition value: '{condition}' (must be one of: {', '.join(VALID_CONDITION)})")

    # Price format check
    price = product.get("price", "").strip()
    if price and not re.match(r"^\d+(\.\d{1,2})?\s*[A-Z]{3}$", price):
        score -= 10
        issues.append(f"Price format issue: '{price}' (expected: '29.99 USD')")

    # Recommended attributes
    filled_recommended = 0
    for attr in RECOMMENDED_ATTRIBUTES:
        if attr in all_headers and product.get(attr, "").strip():
            filled_recommended += 1

    applicable = len([a for a in RECOMMENDED_ATTRIBUTES if a in all_headers]) or len(RECOMMENDED_ATTRIBUTES)
    fill_rate = filled_recommended / applicable if applicable > 0 else 0

    if fill_rate < 0.3:
        score -= 15
        issues.append(f"Low recommended attribute fill rate: {fill_rate:.0%}")
    elif fill_rate < 0.5:
        score -= 8
        issues.append(f"Recommended attribute fill rate below 50%: {fill_rate:.0%}")

    # Apparel-specific checks
    product_type = product.get("product_type", "").lower() + product.get("google_product_category", "").lower()
    if any(kw in product_type for kw in ["apparel", "clothing", "shoes", "accessories"]):
        missing_apparel = [a for a in APPAREL_REQUIRED if not product.get(a, "").strip()]
        if missing_apparel:
            score -= 10
            issues.append(f"Apparel product missing: {', '.join(missing_apparel)}")

    return max(0, score), issues


def validate_gtin(gtin: str) -> bool:
    """Validate GTIN check digit (works for UPC-12, EAN-13, GTIN-14)."""
    gtin = gtin.strip().replace("-", "").replace(" ", "")
    if not gtin.isdigit() or len(gtin) not in (8, 12, 13, 14):
        return False

    digits = [int(d) for d in gtin]
    check = digits[-1]
    total = 0
    for i, d in enumerate(reversed(digits[:-1])):
        total += d * (3 if i % 2 == 0 else 1)
    expected = (10 - (total % 10)) % 10
    return check == expected


def calculate_overall(title: int, desc: int, image: int, attr: int) -> int:
    """Calculate weighted overall score."""
    return round(title * 0.30 + attr * 0.25 + image * 0.20 + desc * 0.15 + attr * 0.10)


def get_grade(score: float) -> str:
    """Convert score to letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    return "F"


# ---------------------------------------------------------------------------
# Feed parsing
# ---------------------------------------------------------------------------

def detect_delimiter(file_path: str) -> str:
    """Auto-detect CSV vs TSV delimiter."""
    with open(file_path, "r", encoding="utf-8-sig") as f:
        first_line = f.readline()
    if "\t" in first_line:
        return "\t"
    return ","


def parse_feed(file_path: str, delimiter: Optional[str] = None) -> tuple[list[dict], list[str]]:
    """Parse a CSV/TSV feed file and return rows + headers."""
    if delimiter is None:
        delimiter = detect_delimiter(file_path)

    rows = []
    with open(file_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        headers = reader.fieldnames or []
        for row in reader:
            rows.append(row)

    return rows, headers


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyze_feed(file_path: str, delimiter: Optional[str] = None) -> tuple[list[ProductScore], FeedSummary]:
    """Run full feed analysis and return per-product scores + summary."""
    products, headers = parse_feed(file_path, delimiter)

    if not products:
        print("ERROR: Feed file is empty or could not be parsed.")
        sys.exit(1)

    scores = []
    total_title = 0
    total_desc = 0
    total_image = 0
    total_attr = 0
    total_title_len = 0
    total_desc_len = 0
    products_with_issues = 0
    missing_req_counts = {}
    missing_rec_counts = {}

    for product in products:
        pid = product.get("id", "UNKNOWN").strip()

        t_score, t_issues = score_title(product)
        d_score, d_issues = score_description(product)
        i_score, i_issues = score_image(product)
        a_score, a_issues = score_attributes(product, headers)

        overall = calculate_overall(t_score, d_score, i_score, a_score)
        all_issues = t_issues + d_issues + i_issues + a_issues

        ps = ProductScore(
            product_id=pid,
            title_score=t_score,
            description_score=d_score,
            image_score=i_score,
            attribute_score=a_score,
            overall_score=overall,
            issues=all_issues,
        )
        scores.append(ps)

        total_title += t_score
        total_desc += d_score
        total_image += i_score
        total_attr += a_score
        total_title_len += len(product.get("title", ""))
        total_desc_len += len(product.get("description", ""))

        if all_issues:
            products_with_issues += 1

        # Track missing required
        for attr in REQUIRED_ATTRIBUTES:
            if not product.get(attr, "").strip():
                missing_req_counts[attr] = missing_req_counts.get(attr, 0) + 1

        # Track missing recommended
        for attr in RECOMMENDED_ATTRIBUTES:
            if not product.get(attr, "").strip():
                missing_rec_counts[attr] = missing_rec_counts.get(attr, 0) + 1

    n = len(products)
    avg_title = total_title / n
    avg_desc = total_desc / n
    avg_image = total_image / n
    avg_attr = total_attr / n
    overall = calculate_overall(avg_title, avg_desc, avg_image, avg_attr)

    summary = FeedSummary(
        total_products=n,
        avg_title_score=round(avg_title, 1),
        avg_description_score=round(avg_desc, 1),
        avg_image_score=round(avg_image, 1),
        avg_attribute_score=round(avg_attr, 1),
        overall_score=round(overall, 1),
        approval_rate=round((1 - len(missing_req_counts.get("id", [])) / n) * 100, 1) if n > 0 else 0,
        missing_required=missing_req_counts,
        missing_recommended=missing_rec_counts,
        title_length_avg=round(total_title_len / n, 1),
        desc_length_avg=round(total_desc_len / n, 1),
        products_with_issues=products_with_issues,
        grade=get_grade(overall),
    )

    return scores, summary


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_summary(summary: FeedSummary) -> None:
    """Print feed analysis summary to stdout."""
    print("=" * 50)
    print("  PRODUCT FEED ANALYSIS SUMMARY")
    print("=" * 50)
    print()
    print(f"  Total Products:    {summary.total_products}")
    print(f"  Overall Score:     {summary.overall_score} / 100  (Grade: {summary.grade})")
    print(f"  Products w/Issues: {summary.products_with_issues} / {summary.total_products}")
    print()
    print("  COMPONENT SCORES:")
    print(f"    Title Quality:          {summary.avg_title_score}/100  (weight: 30%)")
    print(f"    Attribute Completeness: {summary.avg_attribute_score}/100  (weight: 25%)")
    print(f"    Image Compliance:       {summary.avg_image_score}/100  (weight: 20%)")
    print(f"    Description Quality:    {summary.avg_description_score}/100  (weight: 15%)")
    print(f"    Data Accuracy:          {summary.avg_attribute_score}/100  (weight: 10%)")
    print()
    print("  KEY METRICS:")
    print(f"    Avg Title Length:       {summary.title_length_avg} chars")
    print(f"    Avg Description Length: {summary.desc_length_avg} chars")
    print()

    if summary.missing_required:
        print("  MISSING REQUIRED ATTRIBUTES:")
        for attr, count in sorted(summary.missing_required.items(), key=lambda x: -x[1]):
            pct = round(count / summary.total_products * 100, 1)
            print(f"    {attr}: {count} products ({pct}%)")
        print()

    if summary.missing_recommended:
        print("  MISSING RECOMMENDED ATTRIBUTES (top 5):")
        for attr, count in sorted(summary.missing_recommended.items(), key=lambda x: -x[1])[:5]:
            pct = round(count / summary.total_products * 100, 1)
            print(f"    {attr}: {count} products ({pct}%)")
        print()

    print("=" * 50)


def print_worst_products(scores: list[ProductScore], limit: int = 10) -> None:
    """Print the lowest-scoring products."""
    worst = sorted(scores, key=lambda s: s.overall_score)[:limit]
    print()
    print(f"  LOWEST SCORING PRODUCTS (bottom {limit}):")
    print(f"  {'ID':<30} {'Title':>6} {'Desc':>6} {'Image':>6} {'Attr':>6} {'Overall':>8}")
    print("  " + "-" * 68)
    for ps in worst:
        print(f"  {ps.product_id:<30} {ps.title_score:>6} {ps.description_score:>6} "
              f"{ps.image_score:>6} {ps.attribute_score:>6} {ps.overall_score:>8}")
        if ps.issues:
            for issue in ps.issues[:3]:
                print(f"    -> {issue}")
    print()


def export_scores(scores: list[ProductScore], output_path: str) -> None:
    """Export per-product scores to CSV."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title_score", "description_score", "image_score",
                         "attribute_score", "overall_score", "issues"])
        for ps in scores:
            writer.writerow([
                ps.product_id,
                ps.title_score,
                ps.description_score,
                ps.image_score,
                ps.attribute_score,
                ps.overall_score,
                "; ".join(ps.issues),
            ])
    print(f"  Scores exported to: {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analyze a Google Merchant Center product feed and score quality."
    )
    parser.add_argument("feed_file", help="Path to CSV or TSV feed file")
    parser.add_argument("--output", "-o", help="Export per-product scores to CSV", default=None)
    parser.add_argument("--format", "-f", choices=["csv", "tsv"], help="Force delimiter (auto-detected by default)")
    parser.add_argument("--worst", "-w", type=int, default=10, help="Number of worst products to show (default: 10)")

    args = parser.parse_args()

    if not os.path.isfile(args.feed_file):
        print(f"ERROR: File not found: {args.feed_file}")
        sys.exit(1)

    delimiter = None
    if args.format == "tsv":
        delimiter = "\t"
    elif args.format == "csv":
        delimiter = ","

    print(f"\n  Analyzing: {args.feed_file}\n")

    scores, summary = analyze_feed(args.feed_file, delimiter)

    print_summary(summary)
    print_worst_products(scores, limit=args.worst)

    if args.output:
        export_scores(scores, args.output)

    # Exit with non-zero if feed is critical
    if summary.overall_score < 50:
        sys.exit(2)


if __name__ == "__main__":
    main()
