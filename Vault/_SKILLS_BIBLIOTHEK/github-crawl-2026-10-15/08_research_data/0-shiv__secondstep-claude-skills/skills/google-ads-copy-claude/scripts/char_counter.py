#!/usr/bin/env python3
"""
Google Ads Character Counter & Validator

Validates headlines and descriptions against Google Ads character limits.
Flags violations and provides optimization suggestions.

Usage:
    python char_counter.py --file ads.csv
    python char_counter.py --headline "Your Headline Here"
    python char_counter.py --description "Your description text here"
"""

import argparse
import csv
import sys
from typing import List, Tuple


# Google Ads character limits
LIMITS = {
    "headline": 30,
    "long_headline": 90,
    "description": 90,
    "display_path": 15,
    "business_name": 25,
    "sitelink_title": 25,
    "sitelink_description": 35,
    "callout": 25,
    "structured_snippet": 25,
}

# DKI pattern for extracting default text
DKI_PATTERN = r"\{[A-Za-z]+:([^}]+)\}"


def count_chars(text: str) -> int:
    """Count characters in ad copy, handling DKI syntax."""
    import re
    # Replace DKI syntax with default text for counting
    processed = re.sub(DKI_PATTERN, r"\1", text)
    return len(processed)


def validate_headline(text: str) -> Tuple[bool, int, str]:
    """Validate a headline against the 30-character limit."""
    char_count = count_chars(text)
    is_valid = char_count <= LIMITS["headline"]
    status = "PASS" if is_valid else f"FAIL (over by {char_count - LIMITS['headline']})"
    return is_valid, char_count, status


def validate_description(text: str) -> Tuple[bool, int, str]:
    """Validate a description against the 90-character limit."""
    char_count = count_chars(text)
    is_valid = char_count <= LIMITS["description"]
    status = "PASS" if is_valid else f"FAIL (over by {char_count - LIMITS['description']})"
    return is_valid, char_count, status


def suggest_shortening(text: str, limit: int) -> List[str]:
    """Suggest ways to shorten text that exceeds the limit."""
    suggestions = []
    char_count = count_chars(text)

    if char_count <= limit:
        return ["Already within limit."]

    overage = char_count - limit

    # Check for common shortenable patterns
    if " and " in text:
        suggestions.append(f"Replace 'and' with '&' (saves 2 chars)")
    if " the " in text.lower():
        suggestions.append(f"Remove 'the' where possible (saves 3-4 chars)")
    if " that " in text.lower():
        suggestions.append(f"Remove 'that' if grammatically optional (saves 4-5 chars)")
    if " your " in text.lower() and limit == 30:
        suggestions.append(f"Remove 'your' — implied in ads (saves 4-5 chars)")
    if "  " in text:
        suggestions.append(f"Remove double spaces (saves {text.count('  ')} chars)")

    # Check for long words that could be abbreviated
    words = text.split()
    for word in words:
        if len(word) > 8:
            suggestions.append(f"Consider abbreviating '{word}' ({len(word)} chars)")

    if not suggestions:
        suggestions.append(f"Need to cut {overage} characters. Try removing filler words or using shorter synonyms.")

    return suggestions


def validate_rsa(headlines: List[str], descriptions: List[str]) -> dict:
    """Validate a complete RSA."""
    results = {
        "headlines": [],
        "descriptions": [],
        "headline_count": len(headlines),
        "description_count": len(descriptions),
        "all_valid": True,
        "issues": [],
    }

    # Validate headline count
    if len(headlines) < 3:
        results["issues"].append(f"Too few headlines: {len(headlines)} (minimum 3)")
        results["all_valid"] = False
    if len(headlines) > 15:
        results["issues"].append(f"Too many headlines: {len(headlines)} (maximum 15)")
        results["all_valid"] = False

    # Validate description count
    if len(descriptions) < 2:
        results["issues"].append(f"Too few descriptions: {len(descriptions)} (minimum 2)")
        results["all_valid"] = False
    if len(descriptions) > 4:
        results["issues"].append(f"Too many descriptions: {len(descriptions)} (maximum 4)")
        results["all_valid"] = False

    # Validate each headline
    for i, headline in enumerate(headlines, 1):
        is_valid, char_count, status = validate_headline(headline)
        results["headlines"].append({
            "index": i,
            "text": headline,
            "chars": char_count,
            "limit": LIMITS["headline"],
            "valid": is_valid,
            "status": status,
        })
        if not is_valid:
            results["all_valid"] = False

    # Validate each description
    for i, desc in enumerate(descriptions, 1):
        is_valid, char_count, status = validate_description(desc)
        results["descriptions"].append({
            "index": i,
            "text": desc,
            "chars": char_count,
            "limit": LIMITS["description"],
            "valid": is_valid,
            "status": status,
        })
        if not is_valid:
            results["all_valid"] = False

    return results


def print_results(results: dict):
    """Pretty-print validation results."""
    print("\n" + "=" * 60)
    print("RSA VALIDATION REPORT")
    print("=" * 60)

    print(f"\nHeadlines: {results['headline_count']}/15")
    print(f"Descriptions: {results['description_count']}/4")
    print(f"Overall: {'PASS' if results['all_valid'] else 'FAIL'}")

    if results["issues"]:
        print(f"\nStructural Issues:")
        for issue in results["issues"]:
            print(f"  ! {issue}")

    print(f"\n--- Headlines ---")
    for h in results["headlines"]:
        indicator = "OK" if h["valid"] else "XX"
        print(f"  [{indicator}] H{h['index']:2d} ({h['chars']:2d}/{h['limit']} chars) \"{h['text']}\"")
        if not h["valid"]:
            suggestions = suggest_shortening(h["text"], h["limit"])
            for s in suggestions:
                print(f"       -> {s}")

    print(f"\n--- Descriptions ---")
    for d in results["descriptions"]:
        indicator = "OK" if d["valid"] else "XX"
        print(f"  [{indicator}] D{d['index']} ({d['chars']:2d}/{d['limit']} chars) \"{d['text']}\"")
        if not d["valid"]:
            suggestions = suggest_shortening(d["text"], d["limit"])
            for s in suggestions:
                print(f"       -> {s}")

    print("\n" + "=" * 60)


def process_csv(filepath: str):
    """Process a CSV file with headlines and descriptions."""
    headlines = []
    descriptions = []

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for i in range(1, 16):
                key = f"Headline {i}"
                if key in row and row[key].strip():
                    headlines.append(row[key].strip())
            for i in range(1, 5):
                key = f"Description {i}"
                if key in row and row[key].strip():
                    descriptions.append(row[key].strip())

    if headlines or descriptions:
        results = validate_rsa(headlines, descriptions)
        print_results(results)
    else:
        print("No headlines or descriptions found in CSV.")


def main():
    parser = argparse.ArgumentParser(description="Google Ads Character Counter & Validator")
    parser.add_argument("--headline", type=str, help="Validate a single headline")
    parser.add_argument("--description", type=str, help="Validate a single description")
    parser.add_argument("--file", type=str, help="Validate RSA from CSV file")

    args = parser.parse_args()

    if args.headline:
        is_valid, chars, status = validate_headline(args.headline)
        print(f"Headline: \"{args.headline}\"")
        print(f"Characters: {chars}/30 — {status}")
        if not is_valid:
            for s in suggest_shortening(args.headline, 30):
                print(f"  Suggestion: {s}")
    elif args.description:
        is_valid, chars, status = validate_description(args.description)
        print(f"Description: \"{args.description}\"")
        print(f"Characters: {chars}/90 — {status}")
        if not is_valid:
            for s in suggest_shortening(args.description, 90):
                print(f"  Suggestion: {s}")
    elif args.file:
        process_csv(args.file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
