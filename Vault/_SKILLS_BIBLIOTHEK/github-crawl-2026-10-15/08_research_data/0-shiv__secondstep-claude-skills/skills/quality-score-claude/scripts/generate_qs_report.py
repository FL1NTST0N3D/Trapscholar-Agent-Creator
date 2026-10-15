#!/usr/bin/env python3
"""
QS Audit Report Generator
Generates a comprehensive Quality Score audit report in markdown format.

Usage:
    python generate_qs_report.py <csv_file> [--output report.md] [--account-name "Client Name"]
"""

import csv
import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict


CPC_MULTIPLIERS = {
    1: 5.00, 2: 4.00, 3: 3.00, 4: 2.00, 5: 1.67,
    6: 1.25, 7: 1.00, 8: 0.83, 9: 0.67, 10: 0.50,
}

REALISTIC_TARGETS = {
    1: 5, 2: 5, 3: 6, 4: 7, 5: 7,
    6: 7, 7: 8, 8: 9, 9: 10, 10: 10,
}


def parse_number(value: str) -> float:
    if not value or value in ("--", "—"):
        return 0.0
    return float(value.replace("$", "").replace(",", "").replace("%", "").strip() or "0")


def normalize_component(value: str) -> str:
    value = value.strip().lower()
    if "above" in value:
        return "Above Average"
    elif "below" in value:
        return "Below Average"
    elif "average" in value or "avg" in value:
        return "Average"
    return value


def load_data(csv_file: str) -> list[dict]:
    """Load and parse keyword data from CSV."""
    keywords = []
    with open(csv_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            qs_str = (row.get("Quality Score") or row.get("Quality score") or
                      row.get("Qual. Score") or "")
            try:
                qs = int(float(qs_str)) if qs_str and qs_str not in ("--", "—") else None
                if qs is not None and (qs < 1 or qs > 10):
                    qs = None
            except ValueError:
                qs = None

            ectr = normalize_component(
                row.get("Expected CTR") or row.get("Exp. CTR") or ""
            )
            ar = normalize_component(
                row.get("Ad Relevance") or row.get("Ad relevance") or ""
            )
            lp = normalize_component(
                row.get("Landing Page Experience") or row.get("Landing page exp.") or
                row.get("Land. page exp.") or ""
            )

            keywords.append({
                "keyword": row.get("Keyword") or row.get("keyword") or "unknown",
                "match_type": row.get("Match type") or row.get("Match Type") or "",
                "campaign": row.get("Campaign") or row.get("campaign") or "",
                "ad_group": row.get("Ad group") or row.get("Ad Group") or "",
                "quality_score": qs,
                "expected_ctr": ectr,
                "ad_relevance": ar,
                "landing_page_exp": lp,
                "impressions": int(parse_number(row.get("Impressions") or row.get("Impr.") or "0")),
                "clicks": int(parse_number(row.get("Clicks") or row.get("clicks") or "0")),
                "ctr": parse_number(row.get("CTR") or "0"),
                "avg_cpc": parse_number(row.get("Avg. CPC") or row.get("Avg CPC") or "0"),
                "cost": parse_number(row.get("Cost") or row.get("Spend") or "0"),
                "conversions": parse_number(row.get("Conversions") or row.get("Conv.") or "0"),
                "final_url": row.get("Final URL") or row.get("Final url") or "",
            })
    return keywords


def get_weakest(kw: dict) -> str:
    components = {
        "Expected CTR": kw["expected_ctr"],
        "Ad Relevance": kw["ad_relevance"],
        "Landing Page": kw["landing_page_exp"],
    }
    for name, val in components.items():
        if val == "Below Average":
            return name
    for name, val in components.items():
        if val == "Average":
            return name
    return "All Above Avg"


def generate_report(keywords: list[dict], account_name: str) -> str:
    """Generate the full markdown report."""
    with_qs = [kw for kw in keywords if kw["quality_score"] is not None]
    if not with_qs:
        return "# Error\n\nNo keywords with Quality Score data found in the provided file."

    total = len(with_qs)
    total_spend = sum(kw["cost"] for kw in with_qs)
    total_impressions = sum(kw["impressions"] for kw in with_qs)

    # Weighted avg QS
    weighted_avg = 0.0
    if total_impressions > 0:
        weighted_avg = sum(kw["quality_score"] * kw["impressions"] for kw in with_qs) / total_impressions

    # Percentage at 7+
    at_7_plus = sum(1 for kw in with_qs if kw["quality_score"] >= 7)
    pct_7_plus = at_7_plus / total * 100

    # Grade
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

    # Calculate waste per keyword
    for kw in with_qs:
        qs = kw["quality_score"]
        current_mult = CPC_MULTIPLIERS.get(qs, 1.0)
        # Theoretical waste (vs QS 10)
        qs10_mult = CPC_MULTIPLIERS[10]
        theo_cpc = kw["avg_cpc"] * (qs10_mult / current_mult)
        kw["waste_theoretical"] = kw["clicks"] * (kw["avg_cpc"] - theo_cpc)
        # Realistic waste
        target = REALISTIC_TARGETS.get(qs, qs)
        target_mult = CPC_MULTIPLIERS.get(target, 1.0)
        real_cpc = kw["avg_cpc"] * (target_mult / current_mult)
        kw["waste_realistic"] = kw["clicks"] * (kw["avg_cpc"] - real_cpc)
        kw["weakest"] = get_weakest(kw)

    total_waste_theo = sum(kw["waste_theoretical"] for kw in with_qs)
    total_waste_real = sum(kw["waste_realistic"] for kw in with_qs)

    # Sort by waste
    by_waste = sorted(with_qs, key=lambda k: k["waste_theoretical"], reverse=True)

    # Component summary
    comp_counts = {}
    for comp_key, comp_label in [("expected_ctr", "Expected CTR"),
                                  ("ad_relevance", "Ad Relevance"),
                                  ("landing_page_exp", "Landing Page Exp")]:
        above = sum(1 for kw in with_qs if kw[comp_key] == "Above Average")
        avg = sum(1 for kw in with_qs if kw[comp_key] == "Average")
        below = sum(1 for kw in with_qs if kw[comp_key] == "Below Average")
        comp_counts[comp_label] = {"above": above, "avg": avg, "below": below}

    # Weakest component overall
    below_counts = {k: v["below"] for k, v in comp_counts.items()}
    weakest_overall = max(below_counts, key=below_counts.get)

    # Landing page analysis
    lp_groups = defaultdict(list)
    for kw in with_qs:
        url = kw["final_url"] or "(no URL)"
        lp_groups[url].append(kw)

    lp_summary = []
    for url, kws in sorted(lp_groups.items(), key=lambda x: -sum(k["cost"] for k in x[1])):
        avg_qs = sum(k["quality_score"] for k in kws) / len(kws)
        below_lp = sum(1 for k in kws if k["landing_page_exp"] == "Below Average")
        lp_summary.append({
            "url": url,
            "keyword_count": len(kws),
            "avg_qs": round(avg_qs, 1),
            "spend": round(sum(k["cost"] for k in kws), 2),
            "below_avg_count": below_lp,
        })

    # Ad group analysis
    ag_groups = defaultdict(list)
    for kw in with_qs:
        key = f"{kw['campaign']} > {kw['ad_group']}"
        ag_groups[key].append(kw)

    ag_summary = []
    for name, kws in sorted(ag_groups.items(), key=lambda x: -sum(k["cost"] for k in x[1])):
        avg_qs = sum(k["quality_score"] for k in kws) / len(kws)
        below_ar = sum(1 for k in kws if k["ad_relevance"] == "Below Average")
        ag_summary.append({
            "name": name,
            "keyword_count": len(kws),
            "avg_qs": round(avg_qs, 1),
            "spend": round(sum(k["cost"] for k in kws), 2),
            "below_avg_relevance": below_ar,
        })

    # Build the report
    today = datetime.now().strftime("%Y-%m-%d")
    report = []

    # Title
    report.append(f"# Quality Score Audit Report")
    report.append(f"**Account:** {account_name}")
    report.append(f"**Date:** {today}")
    report.append(f"**Generated by:** Quality Score Claude")
    report.append("")

    # Section 1: Executive Summary
    report.append("## 1. Executive Summary")
    report.append("")
    report.append(f"**Overall Grade: {grade}**")
    report.append("")
    report.append(
        f"This account has {total:,} keywords with Quality Score data, "
        f"spending ${total_spend:,.0f}/month. "
        f"{pct_7_plus:.0f}% of keywords are at QS 7 or above (target: 60%+). "
        f"The weighted average Quality Score is {weighted_avg:.1f}. "
        f"Quality Score optimization could save an estimated "
        f"**${total_waste_real:,.0f}/month** (${total_waste_real * 12:,.0f}/year) "
        f"in reduced CPC costs."
    )
    report.append("")
    report.append("**Top 3 Recommendations:**")
    # Generate top 3 based on component weakness
    recs = []
    if comp_counts.get("Landing Page Exp", {}).get("below", 0) > 0:
        recs.append(f"Fix landing page experience issues ({comp_counts['Landing Page Exp']['below']} keywords affected)")
    if any(d["keyword_count"] > 15 for d in ag_summary):
        oversized = sum(1 for d in ag_summary if d["keyword_count"] > 15)
        recs.append(f"Restructure {oversized} oversized ad groups into tighter themes")
    if comp_counts.get("Expected CTR", {}).get("below", 0) > 0:
        recs.append(f"Improve Expected CTR for {comp_counts['Expected CTR']['below']} keywords (ad copy + extensions)")
    if comp_counts.get("Ad Relevance", {}).get("below", 0) > 0:
        recs.append(f"Fix Ad Relevance for {comp_counts['Ad Relevance']['below']} keywords (keyword in headlines)")
    for i, rec in enumerate(recs[:3], 1):
        report.append(f"{i}. {rec}")
    report.append("")

    # Section 2: Distribution
    report.append("## 2. QS Distribution")
    report.append("")
    report.append("| QS | Keywords | % | Spend | % Spend |")
    report.append("|:--:|--------:|---:|------:|--------:|")

    bands = [
        ("1-2 (Critical)", lambda q: q <= 2),
        ("3-4 (Poor)", lambda q: 3 <= q <= 4),
        ("5-6 (Average)", lambda q: 5 <= q <= 6),
        ("7 (Good)", lambda q: q == 7),
        ("8-10 (Excellent)", lambda q: q >= 8),
    ]
    for band_name, band_filter in bands:
        kws = [kw for kw in with_qs if band_filter(kw["quality_score"])]
        count = len(kws)
        pct = count / total * 100
        spend = sum(kw["cost"] for kw in kws)
        spend_pct = spend / total_spend * 100 if total_spend > 0 else 0
        report.append(f"| {band_name} | {count:,} | {pct:.1f}% | ${spend:,.0f} | {spend_pct:.1f}% |")

    report.append("")

    # Section 3: CPC Impact
    report.append("## 3. CPC Impact Analysis")
    report.append("")
    report.append(f"| Metric | Value |")
    report.append(f"|:--|--:|")
    report.append(f"| Total monthly spend | ${total_spend:,.0f} |")
    report.append(f"| Max theoretical savings (all at QS 10) | ${total_waste_theo:,.0f}/mo |")
    report.append(f"| Realistic savings (achievable targets) | ${total_waste_real:,.0f}/mo |")
    report.append(f"| Annual realistic savings | ${total_waste_real * 12:,.0f}/yr |")
    report.append("")

    # Section 4: Component Breakdown
    report.append("## 4. Component Breakdown")
    report.append("")
    report.append(f"**Weakest component overall: {weakest_overall}**")
    report.append("")
    report.append("| Component | Above Avg | Average | Below Avg |")
    report.append("|:--|:--:|:--:|:--:|")
    for comp, counts in comp_counts.items():
        t = counts["above"] + counts["avg"] + counts["below"]
        if t > 0:
            report.append(
                f"| {comp} | {counts['above']} ({counts['above']/t*100:.0f}%) | "
                f"{counts['avg']} ({counts['avg']/t*100:.0f}%) | "
                f"{counts['below']} ({counts['below']/t*100:.0f}%) |"
            )
    report.append("")

    # Section 5: Top 20 Keywords
    report.append("## 5. Top 20 Keywords to Fix")
    report.append("")
    report.append("| # | Keyword | QS | Spend/Mo | Waste/Mo | Weakest Component |")
    report.append("|--:|:--------|:--:|--------:|---------:|:------------------|")
    for i, kw in enumerate(by_waste[:20], 1):
        report.append(
            f"| {i} | {kw['keyword'][:35]} | {kw['quality_score']} | "
            f"${kw['cost']:,.0f} | ${kw['waste_theoretical']:,.0f} | {kw['weakest']} |"
        )
    report.append("")

    # Section 6: Landing Page Analysis
    report.append("## 6. Landing Page Analysis")
    report.append("")
    report.append("| Landing Page | Keywords | Avg QS | Spend | Below Avg LP |")
    report.append("|:-------------|--------:|------:|------:|:-------------|")
    for lp in lp_summary[:10]:
        url_display = lp["url"][:50] if lp["url"] else "(none)"
        report.append(
            f"| {url_display} | {lp['keyword_count']} | {lp['avg_qs']} | "
            f"${lp['spend']:,.0f} | {lp['below_avg_count']} keywords |"
        )
    report.append("")

    # Section 7: Ad Group Assessment
    report.append("## 7. Ad Group Structure Assessment")
    report.append("")
    oversized = [ag for ag in ag_summary if ag["keyword_count"] > 15]
    if oversized:
        report.append(f"**{len(oversized)} ad groups have 15+ keywords and may need restructuring:**")
        report.append("")
        for ag in oversized[:10]:
            report.append(f"- **{ag['name']}** — {ag['keyword_count']} keywords, avg QS {ag['avg_qs']}, ${ag['spend']:,.0f}/mo")
    else:
        report.append("All ad groups have 15 or fewer keywords. Structure is within recommended limits.")
    report.append("")

    # Section 8: Estimated Savings
    report.append("## 8. Estimated Monthly Savings by Category")
    report.append("")
    # Estimate savings by fix category
    lp_savings = sum(
        kw["waste_realistic"] for kw in with_qs
        if kw["landing_page_exp"] == "Below Average"
    )
    ar_savings = sum(
        kw["waste_realistic"] for kw in with_qs
        if kw["ad_relevance"] == "Below Average" and kw["landing_page_exp"] != "Below Average"
    )
    ctr_savings = sum(
        kw["waste_realistic"] for kw in with_qs
        if kw["expected_ctr"] == "Below Average"
        and kw["ad_relevance"] != "Below Average"
        and kw["landing_page_exp"] != "Below Average"
    )

    report.append("| Category | Est. Savings/Mo | Effort | Timeline |")
    report.append("|:---------|----------------:|:------:|:---------|")
    report.append(f"| Landing Page Fixes | ${lp_savings:,.0f} | Medium | 2-4 weeks |")
    report.append(f"| Ad Group Restructuring | ${ar_savings:,.0f} | Medium | 2-4 weeks |")
    report.append(f"| CTR Optimization | ${ctr_savings:,.0f} | Low-Med | 1-3 weeks |")
    report.append(f"| **Total** | **${total_waste_real:,.0f}** | | **4-8 weeks** |")
    report.append("")

    # Section 9: Action Plan
    report.append("## 9. 30-60-90 Day Action Plan")
    report.append("")
    report.append("### Days 1-30")
    report.append("- Fix landing page speed issues on top 5 pages by spend")
    report.append("- Add missing ad extensions across all campaigns")
    report.append("- Add negative keywords from search terms report")
    report.append("- Begin restructuring top 5 oversized ad groups")
    report.append("")
    report.append("### Days 31-60")
    report.append("- Complete ad group restructuring")
    report.append("- Rewrite ad copy for all Below Average Ad Relevance keywords")
    report.append("- Update landing page content for keyword relevance")
    report.append("- Implement device and geographic bid adjustments")
    report.append("")
    report.append("### Days 61-90")
    report.append("- Monitor QS changes from first round of fixes")
    report.append("- A/B test new ad copy variations")
    report.append("- Create dedicated landing pages for remaining keyword themes")
    report.append("- Set up automated weekly QS tracking")
    report.append("")

    # Section 10: Methodology
    report.append("## 10. Methodology Notes")
    report.append("")
    report.append("- CPC multipliers are industry-standard estimates based on aggregate data. Actual CPC impact varies by auction.")
    report.append("- Realistic savings use conservative QS targets (e.g., QS 3 targets QS 6, not QS 10).")
    report.append("- Quality Score changes take 2-4 weeks to appear in Google Ads after improvements are made.")
    report.append("- Savings estimates do not account for competitive dynamics or auction-time QS variations.")
    report.append("")
    report.append("---")
    report.append("*Generated by Quality Score Claude | github.com/0-shiv/quality-score-claude*")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="QS Audit Report Generator")
    parser.add_argument("csv_file", help="Path to Google Ads keyword CSV")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    parser.add_argument("--account-name", default="Google Ads Account",
                        help="Account name for the report header")
    args = parser.parse_args()

    if not Path(args.csv_file).exists():
        print(f"Error: File not found: {args.csv_file}", file=sys.stderr)
        sys.exit(1)

    keywords = load_data(args.csv_file)
    report = generate_report(keywords, args.account_name)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report written to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
