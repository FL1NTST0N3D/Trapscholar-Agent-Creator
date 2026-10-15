#!/usr/bin/env python3
"""
LinkedIn Ads Health Score Calculator

Calculates a composite health score (0-100) across 8 dimensions
for LinkedIn Ads account audits.

Author: Shivendra Rawat | Second Step (getsecondstep.com)
License: MIT 2026
"""

import json
import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DimensionScore:
    """Score for a single audit dimension."""
    name: str
    score: int
    max_score: int
    findings: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)

    @property
    def percentage(self) -> float:
        if self.max_score == 0:
            return 0.0
        return (self.score / self.max_score) * 100

    @property
    def rating(self) -> str:
        pct = self.percentage
        if pct >= 90:
            return "Elite"
        elif pct >= 70:
            return "Strong"
        elif pct >= 50:
            return "Average"
        elif pct >= 30:
            return "Weak"
        else:
            return "Critical"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "score": self.score,
            "max_score": self.max_score,
            "percentage": round(self.percentage, 1),
            "rating": self.rating,
            "findings": self.findings,
            "recommendations": self.recommendations,
        }


@dataclass
class HealthScore:
    """Composite LinkedIn Ads health score."""
    campaign_structure: DimensionScore = field(
        default_factory=lambda: DimensionScore("Campaign Structure", 0, 15)
    )
    targeting_quality: DimensionScore = field(
        default_factory=lambda: DimensionScore("Targeting Quality", 0, 20)
    )
    lead_gen_forms: DimensionScore = field(
        default_factory=lambda: DimensionScore("Lead Gen Forms", 0, 15)
    )
    content_formats: DimensionScore = field(
        default_factory=lambda: DimensionScore("Content Formats", 0, 10)
    )
    budget_cpl: DimensionScore = field(
        default_factory=lambda: DimensionScore("Budget & CPL", 0, 15)
    )
    audience_building: DimensionScore = field(
        default_factory=lambda: DimensionScore("Audience Building", 0, 10)
    )
    conversion_tracking: DimensionScore = field(
        default_factory=lambda: DimensionScore("Conversion Tracking", 0, 10)
    )
    reporting_setup: DimensionScore = field(
        default_factory=lambda: DimensionScore("Reporting Setup", 0, 5)
    )

    @property
    def dimensions(self) -> list[DimensionScore]:
        return [
            self.campaign_structure,
            self.targeting_quality,
            self.lead_gen_forms,
            self.content_formats,
            self.budget_cpl,
            self.audience_building,
            self.conversion_tracking,
            self.reporting_setup,
        ]

    @property
    def total_score(self) -> int:
        return sum(d.score for d in self.dimensions)

    @property
    def max_total(self) -> int:
        return sum(d.max_score for d in self.dimensions)

    @property
    def percentage(self) -> float:
        if self.max_total == 0:
            return 0.0
        return (self.total_score / self.max_total) * 100

    @property
    def rating(self) -> str:
        pct = self.percentage
        if pct >= 90:
            return "Elite"
        elif pct >= 70:
            return "Strong"
        elif pct >= 50:
            return "Average"
        elif pct >= 30:
            return "Weak"
        else:
            return "Critical"

    def weakest_dimensions(self, n: int = 3) -> list[DimensionScore]:
        """Return the N weakest dimensions by percentage score."""
        return sorted(self.dimensions, key=lambda d: d.percentage)[:n]

    def strongest_dimensions(self, n: int = 3) -> list[DimensionScore]:
        """Return the N strongest dimensions by percentage score."""
        return sorted(self.dimensions, key=lambda d: d.percentage, reverse=True)[:n]

    def to_dict(self) -> dict:
        return {
            "total_score": self.total_score,
            "max_total": self.max_total,
            "percentage": round(self.percentage, 1),
            "rating": self.rating,
            "dimensions": [d.to_dict() for d in self.dimensions],
            "weakest": [d.to_dict() for d in self.weakest_dimensions()],
            "strongest": [d.to_dict() for d in self.strongest_dimensions()],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    def to_markdown_table(self) -> str:
        lines = [
            "| Dimension | Score | Max | Rating |",
            "|-----------|-------|-----|--------|",
        ]
        for d in self.dimensions:
            lines.append(f"| {d.name} | {d.score} | {d.max_score} | {d.rating} |")
        lines.append(
            f"| **TOTAL** | **{self.total_score}** | **{self.max_total}** | **{self.rating}** |"
        )
        return "\n".join(lines)

    def summary(self) -> str:
        """Generate a text summary of the health score."""
        weakest = self.weakest_dimensions(3)
        strongest = self.strongest_dimensions(2)

        summary_parts = [
            f"LinkedIn Ads Health Score: {self.total_score}/{self.max_total} ({self.rating})",
            "",
            self.to_markdown_table(),
            "",
            "Top Strengths:",
        ]
        for d in strongest:
            summary_parts.append(f"  + {d.name}: {d.score}/{d.max_score} ({d.rating})")

        summary_parts.append("")
        summary_parts.append("Priority Improvements:")
        for d in weakest:
            summary_parts.append(f"  ! {d.name}: {d.score}/{d.max_score} ({d.rating})")
            for rec in d.recommendations[:2]:
                summary_parts.append(f"    -> {rec}")

        return "\n".join(summary_parts)


def calculate_from_input(data: dict) -> HealthScore:
    """Calculate health score from a dictionary of dimension scores."""
    hs = HealthScore()

    dimension_map = {
        "campaign_structure": hs.campaign_structure,
        "targeting_quality": hs.targeting_quality,
        "lead_gen_forms": hs.lead_gen_forms,
        "content_formats": hs.content_formats,
        "budget_cpl": hs.budget_cpl,
        "audience_building": hs.audience_building,
        "conversion_tracking": hs.conversion_tracking,
        "reporting_setup": hs.reporting_setup,
    }

    for key, dimension in dimension_map.items():
        if key in data:
            entry = data[key]
            if isinstance(entry, dict):
                dimension.score = min(entry.get("score", 0), dimension.max_score)
                dimension.findings = entry.get("findings", [])
                dimension.recommendations = entry.get("recommendations", [])
            elif isinstance(entry, (int, float)):
                dimension.score = min(int(entry), dimension.max_score)

    return hs


def main():
    """CLI entrypoint: reads JSON from stdin or file argument."""
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        with open(filepath, "r") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    health_score = calculate_from_input(data)
    print(health_score.summary())
    print()
    print("--- JSON Output ---")
    print(health_score.to_json())


if __name__ == "__main__":
    main()
