#!/usr/bin/env python3
"""
Tracking Report Generator — Generates comprehensive tracking audit reports.

Combines results from tag_validator, ec_checker, and pixel_auditor into
a structured audit report with Tracking Health Score and prioritized fixes.
"""

import json
import sys
import argparse
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Issue:
    priority: str  # critical, high, medium, low
    platform: str
    category: str
    description: str
    impact: str
    fix: str
    effort: str = "1-2 hours"


@dataclass
class PlatformStatus:
    name: str
    active: bool = False
    components: dict = field(default_factory=dict)
    score: int = 0
    max_score: int = 0


def calculate_health_score(audit_data: dict) -> dict:
    """Calculate the Tracking Health Score from audit data."""
    categories = {
        "tag_presence": {"score": 0, "max": 15, "status": "Not assessed"},
        "event_config": {"score": 0, "max": 15, "status": "Not assessed"},
        "enhanced_matching": {"score": 0, "max": 15, "status": "Not assessed"},
        "server_side": {"score": 0, "max": 15, "status": "Not assessed"},
        "offline_import": {"score": 0, "max": 10, "status": "Not assessed"},
        "deduplication": {"score": 0, "max": 10, "status": "Not assessed"},
        "attribution": {"score": 0, "max": 10, "status": "Not assessed"},
        "data_freshness": {"score": 0, "max": 5, "status": "Not assessed"},
        "consent": {"score": 0, "max": 5, "status": "Not assessed"},
    }

    # Score based on audit data
    platforms = audit_data.get("platforms", {})

    # Tag Presence (15 points)
    tags_found = 0
    tags_expected = 0
    for platform, data in platforms.items():
        if data.get("active"):
            tags_expected += 1
            if data.get("tag_detected"):
                tags_found += 1

    if tags_expected > 0:
        tag_coverage = tags_found / tags_expected
        categories["tag_presence"]["score"] = round(15 * tag_coverage)
        categories["tag_presence"]["status"] = (
            "All tags present" if tag_coverage == 1 else
            f"{tags_found}/{tags_expected} tags detected"
        )

    # Event Configuration (15 points)
    events_configured = audit_data.get("events_configured", 0)
    events_expected = audit_data.get("events_expected", 0)
    if events_expected > 0:
        event_ratio = min(events_configured / events_expected, 1.0)
        categories["event_config"]["score"] = round(15 * event_ratio)
        categories["event_config"]["status"] = f"{events_configured}/{events_expected} events configured"

    # Enhanced Matching (15 points)
    ec_score = audit_data.get("ec_score", 0)
    categories["enhanced_matching"]["score"] = min(round(15 * ec_score / 100), 15)
    categories["enhanced_matching"]["status"] = (
        "Active" if ec_score >= 70 else
        "Partial" if ec_score >= 40 else
        "Not configured"
    )

    # Server-Side (15 points)
    if audit_data.get("server_side_active"):
        sgtm_score = audit_data.get("server_side_score", 0)
        categories["server_side"]["score"] = min(round(15 * sgtm_score / 100), 15)
        categories["server_side"]["status"] = "Active"
    else:
        categories["server_side"]["status"] = "Not implemented"

    # Offline Import (10 points)
    if audit_data.get("offline_import_active"):
        offline_score = audit_data.get("offline_import_score", 0)
        categories["offline_import"]["score"] = min(round(10 * offline_score / 100), 10)
        categories["offline_import"]["status"] = "Active"
    else:
        categories["offline_import"]["status"] = "Not applicable" if not audit_data.get("is_lead_gen") else "Not configured"

    # Deduplication (10 points)
    dedup_score = audit_data.get("dedup_score", 0)
    categories["deduplication"]["score"] = min(round(10 * dedup_score / 100), 10)
    categories["deduplication"]["status"] = (
        "Working" if dedup_score >= 80 else
        "Partial" if dedup_score > 0 else
        "Not configured"
    )

    # Attribution (10 points)
    attr_score = audit_data.get("attribution_score", 0)
    categories["attribution"]["score"] = min(round(10 * attr_score / 100), 10)
    categories["attribution"]["status"] = (
        "Optimized" if attr_score >= 80 else
        "Acceptable" if attr_score >= 50 else
        "Needs review"
    )

    # Data Freshness (5 points)
    freshness_ok = audit_data.get("data_freshness_ok", True)
    categories["data_freshness"]["score"] = 5 if freshness_ok else 2
    categories["data_freshness"]["status"] = "OK" if freshness_ok else "Delayed"

    # Consent (5 points)
    consent_configured = audit_data.get("consent_mode_active", False)
    categories["consent"]["score"] = 5 if consent_configured else 0
    categories["consent"]["status"] = "Configured" if consent_configured else "Not configured"

    total_score = sum(c["score"] for c in categories.values())
    total_max = sum(c["max"] for c in categories.values())

    rating = (
        "Excellent" if total_score >= 90 else
        "Good" if total_score >= 70 else
        "Needs Work" if total_score >= 50 else
        "Poor" if total_score >= 30 else
        "Critical"
    )

    return {
        "total_score": total_score,
        "total_max": total_max,
        "rating": rating,
        "categories": categories,
    }


def generate_report(audit_data: dict, format: str = "full") -> str:
    """Generate the tracking audit report."""
    score_data = calculate_health_score(audit_data)
    issues = audit_data.get("issues", [])
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if format == "checklist":
        return generate_checklist(issues)
    elif format == "client":
        return generate_client_summary(score_data, issues, audit_data)

    # Full report
    report = []
    report.append("=" * 70)
    report.append("CONVERSION TRACKING AUDIT REPORT")
    report.append(f"Generated: {now}")
    report.append(f"Website: {audit_data.get('website', 'Not specified')}")
    report.append("=" * 70)

    # Executive Summary
    report.append("\n## EXECUTIVE SUMMARY\n")
    report.append(f"Tracking Health Score: {score_data['total_score']}/{score_data['total_max']} — {score_data['rating']}")

    critical_count = sum(1 for i in issues if i.get("priority") == "critical")
    high_count = sum(1 for i in issues if i.get("priority") == "high")
    report.append(f"Critical Issues: {critical_count}")
    report.append(f"High Priority Issues: {high_count}")

    estimated_waste = critical_count * 800 + high_count * 400
    if estimated_waste > 0:
        report.append(f"Estimated Monthly Spend at Risk: ${estimated_waste:,}")

    # Score Breakdown
    report.append("\n## TRACKING HEALTH SCORE BREAKDOWN\n")
    report.append(f"{'Category':<35} {'Score':>6} {'Max':>5} {'Status':<20}")
    report.append("-" * 70)
    for cat_key, cat_data in score_data["categories"].items():
        cat_name = cat_key.replace("_", " ").title()
        report.append(f"{cat_name:<35} {cat_data['score']:>6} {cat_data['max']:>5} {cat_data['status']:<20}")
    report.append("-" * 70)
    report.append(f"{'TOTAL':<35} {score_data['total_score']:>6} {score_data['total_max']:>5} {score_data['rating']:<20}")

    # Platform Status
    report.append("\n## PLATFORM STATUS\n")
    for platform_name, platform_data in audit_data.get("platforms", {}).items():
        if platform_data.get("active"):
            status = "OK" if platform_data.get("tag_detected") else "ISSUES"
            report.append(f"  [{status}] {platform_name.upper()}")
            for component, comp_status in platform_data.get("components", {}).items():
                report.append(f"       {component}: {comp_status}")

    # Issues
    for priority in ["critical", "high", "medium", "low"]:
        priority_issues = [i for i in issues if i.get("priority") == priority]
        if priority_issues:
            report.append(f"\n## {priority.upper()} ISSUES ({len(priority_issues)})\n")
            for idx, issue in enumerate(priority_issues, 1):
                report.append(f"{idx}. [{issue.get('platform', '?')}] {issue.get('description', '')}")
                report.append(f"   Impact: {issue.get('impact', 'Unknown')}")
                report.append(f"   Fix: {issue.get('fix', 'See documentation')}")
                report.append(f"   Effort: {issue.get('effort', '1-2 hours')}")
                report.append("")

    # Recommendations
    report.append("\n## RECOMMENDATIONS\n")
    if score_data["total_score"] < 50:
        report.append("1. Address all critical issues immediately — significant data loss is occurring")
        report.append("2. Implement Enhanced Conversions to recover lost conversion data")
        report.append("3. Set up server-side tracking to bypass ad blockers")
    elif score_data["total_score"] < 70:
        report.append("1. Fix high-priority issues within the next week")
        report.append("2. Review attribution model settings across platforms")
        report.append("3. Implement event deduplication if using both client-side and server-side")
    else:
        report.append("1. Address remaining medium/low priority items")
        report.append("2. Set up regular tracking health monitoring")
        report.append("3. Review attribution alignment quarterly")

    report.append(f"\n{'=' * 70}")
    report.append("Report generated by Conversion Tracking Claude")
    report.append(f"{'=' * 70}")

    return "\n".join(report)


def generate_checklist(issues: list) -> str:
    """Generate a developer checklist from issues."""
    lines = ["# TRACKING FIX CHECKLIST", ""]
    for priority in ["critical", "high", "medium", "low"]:
        priority_issues = [i for i in issues if i.get("priority") == priority]
        if priority_issues:
            lines.append(f"## {priority.upper()}")
            for issue in priority_issues:
                lines.append(f"[ ] [{issue.get('platform', '?')}] {issue.get('description', '')}")
                lines.append(f"    Fix: {issue.get('fix', '')}")
            lines.append("")
    return "\n".join(lines)


def generate_client_summary(score_data: dict, issues: list, audit_data: dict) -> str:
    """Generate a client-facing summary."""
    lines = []
    lines.append("# Tracking Audit Summary")
    lines.append("")
    lines.append(f"**Tracking Health Score: {score_data['total_score']}/100 — {score_data['rating']}**")
    lines.append("")

    critical_count = sum(1 for i in issues if i.get("priority") == "critical")
    if critical_count > 0:
        lines.append(f"We found {critical_count} critical tracking issue(s) that are causing conversion data loss.")
        estimated_loss = critical_count * 15
        lines.append(f"Estimated {estimated_loss}% of conversions are currently not being tracked.")
    else:
        lines.append("No critical tracking issues found. Your core tracking is functioning.")

    lines.append("")
    lines.append("## Key Findings")
    for issue in issues[:5]:
        lines.append(f"- **{issue.get('description', '')}** — {issue.get('impact', '')}")

    lines.append("")
    lines.append("## Recommended Next Steps")
    lines.append("1. Address critical and high-priority issues (estimated 4-8 hours of developer time)")
    lines.append("2. Implement Enhanced Conversions for improved data accuracy")
    lines.append("3. Schedule quarterly tracking health checks")

    return "\n".join(lines)


def load_audit_data(filepath: str) -> dict:
    """Load audit data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def create_sample_audit_data() -> dict:
    """Create sample audit data for testing."""
    return {
        "website": "https://example.com",
        "platforms": {
            "google_ads": {
                "active": True,
                "tag_detected": True,
                "components": {
                    "Google Tag": "Present on all pages",
                    "Enhanced Conversions": "Not configured",
                    "Server-Side GTM": "Not implemented",
                }
            },
            "meta_ads": {
                "active": True,
                "tag_detected": True,
                "components": {
                    "Meta Pixel": "Present, 3 events configured",
                    "Conversions API": "Not active",
                }
            },
            "linkedin_ads": {
                "active": False,
                "tag_detected": False,
            },
            "tiktok_ads": {
                "active": False,
                "tag_detected": False,
            },
        },
        "events_configured": 5,
        "events_expected": 8,
        "ec_score": 0,
        "server_side_active": False,
        "offline_import_active": False,
        "is_lead_gen": True,
        "dedup_score": 0,
        "attribution_score": 50,
        "data_freshness_ok": True,
        "consent_mode_active": False,
        "issues": [
            {
                "priority": "critical",
                "platform": "Google Ads",
                "description": "Enhanced Conversions not enabled",
                "impact": "5-15% of conversions lost due to cookie restrictions",
                "fix": "Enable EC in Google Ads > Conversions > Settings, implement user_data in gtag",
                "effort": "2-4 hours",
            },
            {
                "priority": "critical",
                "platform": "Google Ads",
                "description": "GCLID not captured on lead forms",
                "impact": "Cannot import offline conversions, Smart Bidding blind to lead quality",
                "fix": "Add hidden gclid field to all forms, capture from URL parameter",
                "effort": "1-2 hours",
            },
            {
                "priority": "high",
                "platform": "Meta",
                "description": "No Conversions API (CAPI) configured",
                "impact": "Missing 25-40% of Safari/Firefox conversions",
                "fix": "Set up CAPI via Conversions API Gateway or server-side GTM",
                "effort": "4-8 hours",
            },
            {
                "priority": "high",
                "platform": "Meta",
                "description": "Purchase event missing value parameter",
                "impact": "Cannot use value optimization or report ROAS",
                "fix": "Add value and currency parameters to Purchase event",
                "effort": "1 hour",
            },
            {
                "priority": "medium",
                "platform": "Google Ads",
                "description": "No server-side tracking (sGTM)",
                "impact": "Ad blockers preventing 10-15% of tag fires",
                "fix": "Deploy sGTM via Stape.io or Google Cloud",
                "effort": "8-16 hours",
            },
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="Generate tracking audit report")
    parser.add_argument("--input", "-i", help="Path to audit data JSON file")
    parser.add_argument("--format", "-f", choices=["full", "checklist", "client"], default="full",
                        help="Report format")
    parser.add_argument("--output", "-o", help="Output file path (prints to stdout if not specified)")
    parser.add_argument("--sample", action="store_true", help="Generate report from sample data")
    args = parser.parse_args()

    if args.sample:
        audit_data = create_sample_audit_data()
    elif args.input:
        audit_data = load_audit_data(args.input)
    else:
        print("ERROR: Provide --input <file.json> or --sample for demo data")
        sys.exit(1)

    report = generate_report(audit_data, format=args.format)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
