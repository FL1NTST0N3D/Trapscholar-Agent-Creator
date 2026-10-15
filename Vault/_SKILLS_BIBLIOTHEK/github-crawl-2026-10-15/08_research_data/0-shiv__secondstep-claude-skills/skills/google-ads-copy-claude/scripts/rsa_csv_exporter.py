#!/usr/bin/env python3
"""
RSA CSV Exporter

Converts RSA ad copy into Google Ads Editor-compatible CSV format
for bulk upload.

Usage:
    python rsa_csv_exporter.py --input rsa_data.json --output ads_import.csv
    python rsa_csv_exporter.py --interactive
"""

import argparse
import csv
import json
import sys
from typing import List, Dict


# Google Ads Editor column headers for RSA import
RSA_COLUMNS = [
    "Campaign",
    "Ad Group",
    "Ad type",
    "Headline 1",
    "Headline 2",
    "Headline 3",
    "Headline 4",
    "Headline 5",
    "Headline 6",
    "Headline 7",
    "Headline 8",
    "Headline 9",
    "Headline 10",
    "Headline 11",
    "Headline 12",
    "Headline 13",
    "Headline 14",
    "Headline 15",
    "Description 1",
    "Description 2",
    "Description 3",
    "Description 4",
    "Path 1",
    "Path 2",
    "Final URL",
    "Headline 1 position",
    "Headline 2 position",
    "Headline 3 position",
    "Description 1 position",
    "Description 2 position",
]


def validate_rsa_data(rsa: Dict) -> List[str]:
    """Validate RSA data before export."""
    errors = []

    headlines = rsa.get("headlines", [])
    descriptions = rsa.get("descriptions", [])

    if len(headlines) < 3:
        errors.append(f"Minimum 3 headlines required, got {len(headlines)}")
    if len(headlines) > 15:
        errors.append(f"Maximum 15 headlines allowed, got {len(headlines)}")
    if len(descriptions) < 2:
        errors.append(f"Minimum 2 descriptions required, got {len(descriptions)}")
    if len(descriptions) > 4:
        errors.append(f"Maximum 4 descriptions allowed, got {len(descriptions)}")

    for i, h in enumerate(headlines, 1):
        text = h if isinstance(h, str) else h.get("text", "")
        if len(text) > 30:
            errors.append(f"Headline {i} exceeds 30 chars: '{text}' ({len(text)} chars)")

    for i, d in enumerate(descriptions, 1):
        text = d if isinstance(d, str) else d.get("text", "")
        if len(text) > 90:
            errors.append(f"Description {i} exceeds 90 chars: '{text}' ({len(text)} chars)")

    if not rsa.get("campaign"):
        errors.append("Campaign name is required")
    if not rsa.get("ad_group"):
        errors.append("Ad Group name is required")
    if not rsa.get("final_url"):
        errors.append("Final URL is required")

    return errors


def rsa_to_row(rsa: Dict) -> Dict:
    """Convert RSA data to a CSV row."""
    row = {col: "" for col in RSA_COLUMNS}

    row["Campaign"] = rsa.get("campaign", "")
    row["Ad Group"] = rsa.get("ad_group", "")
    row["Ad type"] = "Responsive search ad"
    row["Final URL"] = rsa.get("final_url", "")
    row["Path 1"] = rsa.get("path1", "")
    row["Path 2"] = rsa.get("path2", "")

    headlines = rsa.get("headlines", [])
    for i, h in enumerate(headlines[:15], 1):
        text = h if isinstance(h, str) else h.get("text", "")
        row[f"Headline {i}"] = text

    descriptions = rsa.get("descriptions", [])
    for i, d in enumerate(descriptions[:4], 1):
        text = d if isinstance(d, str) else d.get("text", "")
        row[f"Description {i}"] = text

    # Handle pin positions
    pins = rsa.get("pins", {})
    for key, position in pins.items():
        if key in row:
            row[f"{key} position"] = position

    return row


def export_csv(rsas: List[Dict], output_path: str):
    """Export RSAs to Google Ads Editor CSV format."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=RSA_COLUMNS)
        writer.writeheader()

        for rsa in rsas:
            errors = validate_rsa_data(rsa)
            if errors:
                print(f"WARNING - RSA for '{rsa.get('ad_group', 'unknown')}' has issues:")
                for e in errors:
                    print(f"  - {e}")
                print("  Exporting anyway...\n")

            row = rsa_to_row(rsa)
            writer.writerow(row)

    print(f"Exported {len(rsas)} RSA(s) to {output_path}")


def interactive_mode():
    """Collect RSA data interactively."""
    print("=== RSA CSV Exporter — Interactive Mode ===\n")

    rsa = {}
    rsa["campaign"] = input("Campaign name: ").strip()
    rsa["ad_group"] = input("Ad Group name: ").strip()
    rsa["final_url"] = input("Final URL: ").strip()
    rsa["path1"] = input("Display Path 1 (optional): ").strip()
    rsa["path2"] = input("Display Path 2 (optional): ").strip()

    print("\nEnter headlines (3-15). Type 'done' when finished:")
    headlines = []
    for i in range(1, 16):
        h = input(f"  H{i}: ").strip()
        if h.lower() == "done":
            break
        if h:
            headlines.append(h)
    rsa["headlines"] = headlines

    print("\nEnter descriptions (2-4). Type 'done' when finished:")
    descriptions = []
    for i in range(1, 5):
        d = input(f"  D{i}: ").strip()
        if d.lower() == "done":
            break
        if d:
            descriptions.append(d)
    rsa["descriptions"] = descriptions

    output = input("\nOutput file path (default: rsa_export.csv): ").strip() or "rsa_export.csv"
    export_csv([rsa], output)


def main():
    parser = argparse.ArgumentParser(description="RSA CSV Exporter for Google Ads Editor")
    parser.add_argument("--input", type=str, help="JSON file with RSA data")
    parser.add_argument("--output", type=str, default="rsa_export.csv", help="Output CSV file path")
    parser.add_argument("--interactive", action="store_true", help="Interactive input mode")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.input:
        with open(args.input, "r") as f:
            data = json.load(f)

        rsas = data if isinstance(data, list) else [data]
        export_csv(rsas, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
