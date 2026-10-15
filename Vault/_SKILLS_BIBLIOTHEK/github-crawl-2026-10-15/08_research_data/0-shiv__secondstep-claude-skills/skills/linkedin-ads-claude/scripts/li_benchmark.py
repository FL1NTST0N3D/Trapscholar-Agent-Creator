#!/usr/bin/env python3
"""
LinkedIn Ads Benchmark Comparison Engine

Compares campaign performance metrics against industry benchmarks
and generates a benchmark report with status indicators.

Author: Shivendra Rawat | Second Step (getsecondstep.com)
License: MIT 2026
"""

import json
import sys
from dataclasses import dataclass
from typing import Optional


# Industry CPL benchmarks (Lead Gen Form)
INDUSTRY_BENCHMARKS = {
    "technology": {
        "name": "Technology / SaaS",
        "cpl_min": 100, "cpl_max": 200,
        "ctr_min": 0.45, "ctr_max": 0.75,
        "cpc_min": 4, "cpc_max": 8,
        "lgf_completion": 14.0,
    },
    "cybersecurity": {
        "name": "Cybersecurity",
        "cpl_min": 150, "cpl_max": 300,
        "ctr_min": 0.35, "ctr_max": 0.60,
        "cpc_min": 6, "cpc_max": 12,
        "lgf_completion": 11.0,
    },
    "financial_services": {
        "name": "Financial Services",
        "cpl_min": 150, "cpl_max": 300,
        "ctr_min": 0.35, "ctr_max": 0.60,
        "cpc_min": 5, "cpc_max": 10,
        "lgf_completion": 12.0,
    },
    "healthcare": {
        "name": "Healthcare / Pharma",
        "cpl_min": 200, "cpl_max": 400,
        "ctr_min": 0.30, "ctr_max": 0.55,
        "cpc_min": 6, "cpc_max": 14,
        "lgf_completion": 10.0,
    },
    "manufacturing": {
        "name": "Manufacturing / Industrial",
        "cpl_min": 80, "cpl_max": 150,
        "ctr_min": 0.40, "ctr_max": 0.70,
        "cpc_min": 3, "cpc_max": 6,
        "lgf_completion": 15.0,
    },
    "professional_services": {
        "name": "Professional Services",
        "cpl_min": 75, "cpl_max": 175,
        "ctr_min": 0.45, "ctr_max": 0.75,
        "cpc_min": 3, "cpc_max": 7,
        "lgf_completion": 14.0,
    },
    "education": {
        "name": "Education / EdTech",
        "cpl_min": 50, "cpl_max": 120,
        "ctr_min": 0.50, "ctr_max": 0.80,
        "cpc_min": 2, "cpc_max": 5,
        "lgf_completion": 16.0,
    },
    "staffing": {
        "name": "Staffing / HR Tech",
        "cpl_min": 100, "cpl_max": 250,
        "ctr_min": 0.40, "ctr_max": 0.65,
        "cpc_min": 4, "cpc_max": 9,
        "lgf_completion": 13.0,
    },
    "real_estate": {
        "name": "Real Estate (Commercial)",
        "cpl_min": 120, "cpl_max": 250,
        "ctr_min": 0.35, "ctr_max": 0.60,
        "cpc_min": 5, "cpc_max": 10,
        "lgf_completion": 12.0,
    },
    "telecom": {
        "name": "Telecommunications",
        "cpl_min": 100, "cpl_max": 200,
        "ctr_min": 0.40, "ctr_max": 0.65,
        "cpc_min": 4, "cpc_max": 8,
        "lgf_completion": 13.0,
    },
}

# Funnel stage CPL benchmarks
FUNNEL_BENCHMARKS = {
    "tofu": {"cpl_min": 30, "cpl_max": 75, "label": "TOFU (Awareness)"},
    "mofu": {"cpl_min": 75, "cpl_max": 200, "label": "MOFU (Consideration)"},
    "bofu": {"cpl_min": 150, "cpl_max": 600, "label": "BOFU (Conversion)"},
}

# Format-specific benchmarks
FORMAT_BENCHMARKS = {
    "single_image": {
        "name": "Single Image",
        "ctr": 0.55, "cpc_min": 3, "cpc_max": 7, "cpl_min": 75, "cpl_max": 200,
    },
    "carousel": {
        "name": "Carousel",
        "ctr": 1.0, "cpc_min": 4, "cpc_max": 8, "cpl_min": 80, "cpl_max": 200,
    },
    "video": {
        "name": "Video",
        "ctr": 0.40, "cpc_min": 5, "cpc_max": 10, "cpl_min": 100, "cpl_max": 250,
    },
    "document": {
        "name": "Document Ads",
        "ctr": 0.60, "cpc_min": 3, "cpc_max": 7, "cpl_min": 50, "cpl_max": 150,
    },
    "message": {
        "name": "Message Ads",
        "ctr": 3.5, "cpc_min": 20, "cpc_max": 50, "cpl_min": 100, "cpl_max": 300,
    },
    "conversation": {
        "name": "Conversation Ads",
        "ctr": 5.0, "cpc_min": 15, "cpc_max": 40, "cpl_min": 80, "cpl_max": 200,
    },
}


@dataclass
class MetricComparison:
    """Comparison of a single metric against a benchmark range."""
    metric_name: str
    actual_value: float
    benchmark_min: float
    benchmark_max: float
    unit: str = ""
    lower_is_better: bool = False

    @property
    def status(self) -> str:
        if self.lower_is_better:
            if self.actual_value < self.benchmark_min:
                return "Below (Good)"
            elif self.actual_value <= self.benchmark_max:
                return "At Benchmark"
            else:
                return "Above (Bad)"
        else:
            if self.actual_value > self.benchmark_max:
                return "Above (Good)"
            elif self.actual_value >= self.benchmark_min:
                return "At Benchmark"
            else:
                return "Below (Bad)"

    @property
    def variance_pct(self) -> float:
        midpoint = (self.benchmark_min + self.benchmark_max) / 2
        if midpoint == 0:
            return 0.0
        return ((self.actual_value - midpoint) / midpoint) * 100

    def to_table_row(self) -> str:
        unit = self.unit
        if unit == "$":
            actual = f"${self.actual_value:,.2f}"
            bench = f"${self.benchmark_min:,.0f}-${self.benchmark_max:,.0f}"
        elif unit == "%":
            actual = f"{self.actual_value:.2f}%"
            bench = f"{self.benchmark_min:.2f}%-{self.benchmark_max:.2f}%"
        else:
            actual = f"{self.actual_value:,.2f}"
            bench = f"{self.benchmark_min:,.2f}-{self.benchmark_max:,.2f}"

        return f"| {self.metric_name} | {actual} | {bench} | {self.status} |"


def compare_to_industry(
    industry: str,
    cpl: Optional[float] = None,
    ctr: Optional[float] = None,
    cpc: Optional[float] = None,
    lgf_completion: Optional[float] = None,
) -> list[MetricComparison]:
    """Compare campaign metrics against industry benchmarks."""
    industry_key = industry.lower().replace(" ", "_").replace("/", "_")

    # Try exact match, then partial match
    benchmarks = INDUSTRY_BENCHMARKS.get(industry_key)
    if not benchmarks:
        for key, val in INDUSTRY_BENCHMARKS.items():
            if industry_key in key or key in industry_key:
                benchmarks = val
                break

    if not benchmarks:
        print(f"Industry '{industry}' not found. Available industries:")
        for key, val in INDUSTRY_BENCHMARKS.items():
            print(f"  - {key}: {val['name']}")
        return []

    comparisons = []

    if cpl is not None:
        comparisons.append(MetricComparison(
            "CPL (Lead Gen Form)", cpl,
            benchmarks["cpl_min"], benchmarks["cpl_max"],
            unit="$", lower_is_better=True,
        ))

    if ctr is not None:
        comparisons.append(MetricComparison(
            "CTR", ctr,
            benchmarks["ctr_min"], benchmarks["ctr_max"],
            unit="%", lower_is_better=False,
        ))

    if cpc is not None:
        comparisons.append(MetricComparison(
            "CPC", cpc,
            benchmarks["cpc_min"], benchmarks["cpc_max"],
            unit="$", lower_is_better=True,
        ))

    if lgf_completion is not None:
        comparisons.append(MetricComparison(
            "LGF Completion Rate", lgf_completion,
            benchmarks["lgf_completion"] * 0.8,
            benchmarks["lgf_completion"] * 1.3,
            unit="%", lower_is_better=False,
        ))

    return comparisons


def compare_to_funnel(
    stage: str,
    cpl: float,
) -> MetricComparison:
    """Compare CPL against funnel stage benchmarks."""
    stage_key = stage.lower()
    benchmarks = FUNNEL_BENCHMARKS.get(stage_key)
    if not benchmarks:
        raise ValueError(f"Unknown funnel stage: {stage}. Use 'tofu', 'mofu', or 'bofu'.")

    return MetricComparison(
        f"CPL ({benchmarks['label']})", cpl,
        benchmarks["cpl_min"], benchmarks["cpl_max"],
        unit="$", lower_is_better=True,
    )


def generate_benchmark_report(
    industry: str,
    metrics: dict,
    campaigns: Optional[list[dict]] = None,
) -> str:
    """Generate a full benchmark comparison report."""
    lines = [
        "# LinkedIn Ads Benchmark Report",
        "",
        f"**Industry:** {industry}",
        "",
        "## Account-Level Metrics vs Industry Benchmarks",
        "",
        "| Metric | Your Value | Benchmark | Status |",
        "|--------|-----------|-----------|--------|",
    ]

    comparisons = compare_to_industry(
        industry,
        cpl=metrics.get("cpl"),
        ctr=metrics.get("ctr"),
        cpc=metrics.get("cpc"),
        lgf_completion=metrics.get("lgf_completion"),
    )

    for comp in comparisons:
        lines.append(comp.to_table_row())

    if campaigns:
        lines.extend([
            "",
            "## Campaign-Level Benchmark Comparison",
            "",
            "| Campaign | CPL | Funnel Stage | Benchmark | Status |",
            "|----------|-----|-------------|-----------|--------|",
        ])

        for campaign in campaigns:
            name = campaign.get("name", "Unknown")
            cpl = campaign.get("cpl", 0)
            stage = campaign.get("funnel_stage", "mofu")
            try:
                comp = compare_to_funnel(stage, cpl)
                bench_str = f"${comp.benchmark_min:.0f}-${comp.benchmark_max:.0f}"
                lines.append(
                    f"| {name} | ${cpl:.2f} | {stage.upper()} | {bench_str} | {comp.status} |"
                )
            except ValueError:
                lines.append(f"| {name} | ${cpl:.2f} | {stage} | N/A | Unknown |")

    lines.extend([
        "",
        "## Format Benchmarks Reference",
        "",
        "| Format | CTR Benchmark | CPC Range | CPL Range |",
        "|--------|--------------|-----------|-----------|",
    ])

    for fmt_key, fmt in FORMAT_BENCHMARKS.items():
        lines.append(
            f"| {fmt['name']} | {fmt['ctr']:.2f}% | ${fmt['cpc_min']}-${fmt['cpc_max']} | ${fmt['cpl_min']}-${fmt['cpl_max']} |"
        )

    return "\n".join(lines)


def main():
    """CLI entrypoint: reads JSON from stdin or file argument."""
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        with open(filepath, "r") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    industry = data.get("industry", "technology")
    metrics = data.get("metrics", {})
    campaigns = data.get("campaigns", [])

    report = generate_benchmark_report(industry, metrics, campaigns)
    print(report)


if __name__ == "__main__":
    main()
