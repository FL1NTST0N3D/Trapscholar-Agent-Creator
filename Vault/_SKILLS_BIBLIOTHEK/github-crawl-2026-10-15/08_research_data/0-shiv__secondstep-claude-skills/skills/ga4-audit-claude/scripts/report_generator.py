#!/usr/bin/env python3
"""
GA4 Audit Report Generator

Generates a formatted Markdown audit report from audit results JSON.
Can optionally convert to HTML for PDF generation.

Usage:
    python report_generator.py --input audit_results.json --output report.md
    python report_generator.py --input audit_results.json --output report.md --format html
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional


PRIORITY_LABELS = {
    1: "Critical (Fix Immediately)",
    2: "High (Fix This Week)",
    3: "Medium (Fix This Month)",
    4: "Low (Improvement Opportunity)",
}

GRADE_MAP = [
    (90, "A", "Excellent"),
    (75, "B", "Good"),
    (50, "C", "Fair"),
    (25, "D", "Poor"),
    (0, "F", "Critical"),
]

STATUS_ICONS = {
    "A": "++",
    "B": "+",
    "C": "~",
    "D": "-",
    "F": "--",
}


def get_grade(score: float):
    for threshold, grade, label in GRADE_MAP:
        if score >= threshold:
            return grade, label
    return "F", "Critical"


def generate_executive_summary(data: Dict) -> str:
    """Generate the executive summary section."""
    score = data.get("health_score", 0)
    grade, label = get_grade(score)
    property_name = data.get("property_name", "Unknown Property")
    business_type = data.get("business_type", "Unknown")

    strengths = []
    weaknesses = []
    for dim in data.get("dimensions", []):
        if dim.get("score", 0) >= 75:
            strengths.append(dim["name"])
        elif dim.get("score", 0) < 50:
            weaknesses.append(dim["name"])

    strength_text = (
        f"Strongest areas: {', '.join(strengths)}."
        if strengths
        else "No dimensions scored above 75."
    )
    weakness_text = (
        f"Critical gaps in: {', '.join(weaknesses)}."
        if weaknesses
        else "No dimensions scored below 50."
    )

    return f"""## Executive Summary

**Overall Health Score: {score}/100 (Grade: {grade} -- {label})**

This GA4 audit evaluated the {property_name} property ({business_type} business type)
across 8 weighted dimensions. {strength_text} {weakness_text}

Total checks performed: {data.get('total_checks', 0)} |
Passed: {data.get('passed_checks', 0)} |
Failed: {data.get('failed_checks', 0)} |
Warnings: {data.get('warning_checks', 0)}
"""


def generate_score_breakdown(data: Dict) -> str:
    """Generate the score breakdown table."""
    lines = [
        "### Score Breakdown\n",
        "| Dimension | Score | Grade | Status |",
        "|-----------|-------|-------|--------|",
    ]

    for dim in data.get("dimensions", []):
        score = dim.get("score", 0)
        grade, label = get_grade(score)
        status = STATUS_ICONS.get(grade, "?")
        lines.append(
            f"| {dim['name']} | {score}/100 | {grade} | {status} |"
        )

    return "\n".join(lines)


def generate_findings_section(findings: List[Dict], priority: int) -> str:
    """Generate a findings section for a specific priority level."""
    priority_findings = [f for f in findings if f.get("priority") == priority]

    if not priority_findings:
        return ""

    label = PRIORITY_LABELS.get(priority, f"Priority {priority}")
    lines = [f"\n## {label}\n"]

    for i, finding in enumerate(priority_findings, 1):
        lines.append(f"### {i}. {finding.get('title', 'Untitled Finding')}")
        lines.append(f"- **Dimension:** {finding.get('dimension', 'Unknown')}")
        lines.append(
            f"- **Impact:** {finding.get('impact', 'Unknown')} -- "
            f"{finding.get('impact_description', '')}"
        )
        lines.append(
            f"- **Current State:** {finding.get('current_state', 'Not assessed')}"
        )
        lines.append(
            f"- **Recommended:** {finding.get('recommended', 'See fix steps')}"
        )

        fix_steps = finding.get("fix_steps", [])
        if fix_steps:
            lines.append("- **Fix Steps:**")
            for step_num, step in enumerate(fix_steps, 1):
                lines.append(f"  {step_num}. {step}")

        effort = finding.get("effort_hours")
        if effort:
            lines.append(f"- **Estimated Effort:** {effort} hours")

        skill = finding.get("skill_required")
        if skill:
            lines.append(f"- **Skill Required:** {skill}")

        lines.append("")

    return "\n".join(lines)


def generate_roadmap(findings: List[Dict]) -> str:
    """Generate the implementation roadmap."""
    lines = ["\n## Implementation Roadmap\n"]

    week_map = {1: "Week 1: Critical Fixes", 2: "Week 2: High Priority",
                3: "Weeks 3-4: Medium Priority", 4: "Ongoing: Improvements"}

    for priority, week_label in week_map.items():
        priority_findings = [f for f in findings if f.get("priority") == priority]
        if priority_findings:
            lines.append(f"### {week_label}")
            for finding in priority_findings:
                effort = finding.get("effort_hours", "?")
                lines.append(
                    f"- [ ] {finding.get('title', 'Untitled')} "
                    f"(est. {effort} hours)"
                )
            lines.append("")

    return "\n".join(lines)


def generate_report(data: Dict) -> str:
    """Generate the complete audit report in Markdown format."""
    property_id = data.get("property_id", "Unknown")
    website = data.get("website_url", "Unknown")
    business_type = data.get("business_type", "Unknown")
    audit_date = data.get("audit_date", datetime.now().strftime("%Y-%m-%d"))
    auditor = data.get("auditor", "GA4 Audit Claude Skill")

    findings = data.get("findings", [])

    sections = [
        f"# GA4 Audit Report\n",
        f"**Property:** {data.get('property_name', property_id)} ({property_id})",
        f"**Website:** {website}",
        f"**Business Type:** {business_type}",
        f"**Audit Date:** {audit_date}",
        f"**Auditor:** {auditor}\n",
        "---\n",
        generate_executive_summary(data),
        generate_score_breakdown(data),
        "\n---\n",
    ]

    # Add findings by priority
    for priority in [1, 2, 3, 4]:
        section = generate_findings_section(findings, priority)
        if section:
            sections.append(section)

    sections.append("\n---\n")
    sections.append(generate_roadmap(findings))
    sections.append("\n---\n")

    # Methodology
    sections.append(f"""## Methodology

This audit evaluated the GA4 property across 8 weighted dimensions
using {data.get('total_checks', 0)} individual checks. Each check was scored
as passed, failed, or warning. The Health Score is a weighted average
of all dimension scores.

**Audit tool:** GA4 Audit Claude Skill v1.0.0
**Checks performed:** {data.get('total_checks', 0)}
**Passed:** {data.get('passed_checks', 0)} |
**Failed:** {data.get('failed_checks', 0)} |
**Warnings:** {data.get('warning_checks', 0)}
""")

    # Next steps
    sections.append("""---

## Next Steps

1. Share this report with your development/analytics team
2. Begin with Critical (P1) fixes immediately
3. Schedule a follow-up audit in 30 days to measure improvement
4. Set up ongoing monitoring via GA4 alerts and Looker Studio dashboards

---

*Report generated by GA4 Audit Claude Skill*
""")

    return "\n".join(sections)


def wrap_html(markdown_content: str, title: str = "GA4 Audit Report") -> str:
    """Wrap markdown content in basic HTML for PDF generation."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            color: #333;
            line-height: 1.6;
        }}
        h1 {{ color: #1b1b1b; border-bottom: 3px solid #E87811; padding-bottom: 10px; }}
        h2 {{ color: #1b1b1b; margin-top: 2em; }}
        h3 {{ color: #444; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
        th {{ background-color: #1b1b1b; color: white; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        code {{ background-color: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
        pre {{ background-color: #f4f4f4; padding: 16px; border-radius: 6px; overflow-x: auto; }}
        hr {{ border: none; border-top: 1px solid #ddd; margin: 2em 0; }}
        strong {{ color: #1b1b1b; }}
        .score-a {{ color: #22c55e; }}
        .score-b {{ color: #84cc16; }}
        .score-c {{ color: #eab308; }}
        .score-d {{ color: #f97316; }}
        .score-f {{ color: #ef4444; }}
    </style>
</head>
<body>
<pre style="white-space: pre-wrap; font-family: inherit; background: none; padding: 0;">
{markdown_content}
</pre>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(
        description="Generate GA4 Audit Report from audit results JSON."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to audit results JSON file",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="ga4-audit-report.md",
        help="Output file path (default: ga4-audit-report.md)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["markdown", "html"],
        default="markdown",
        help="Output format (default: markdown)",
    )

    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = json.load(f)

    report = generate_report(data)

    if args.format == "html":
        report = wrap_html(report)

    with open(args.output, "w") as f:
        f.write(report)

    print(f"Report generated: {args.output}")


if __name__ == "__main__":
    main()
