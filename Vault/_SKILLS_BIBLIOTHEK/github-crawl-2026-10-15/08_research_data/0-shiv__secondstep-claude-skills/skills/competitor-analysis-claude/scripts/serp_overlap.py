#!/usr/bin/env python3
"""
SERP Overlap Calculator
Calculates the percentage of search results overlap between two domains.

Usage:
    python serp_overlap.py <domain1> <domain2> --keywords "keyword1,keyword2,keyword3"
"""

import sys
import json
from urllib.parse import urlparse

from rich.console import Console
from rich.table import Table
import click


console = Console()


def calculate_overlap(domain_a_keywords, domain_b_keywords):
    """Calculate overlap percentage between two keyword sets."""
    set_a = set(domain_a_keywords)
    set_b = set(domain_b_keywords)

    if not set_a and not set_b:
        return 0.0, set(), set(), set()

    intersection = set_a & set_b
    union = set_a | set_b
    only_a = set_a - set_b
    only_b = set_b - set_a

    overlap_pct = (len(intersection) / len(union) * 100) if union else 0
    return overlap_pct, intersection, only_a, only_b


def analyze_overlap(domain_a, domain_b, keywords_a, keywords_b):
    """Main analysis function."""
    console.print(f"\n[bold blue]SERP Overlap Analysis[/bold blue]")
    console.print(f"Domain A: [cyan]{domain_a}[/cyan]")
    console.print(f"Domain B: [cyan]{domain_b}[/cyan]\n")

    overlap_pct, shared, only_a, only_b = calculate_overlap(keywords_a, keywords_b)

    # Summary table
    summary = Table(title="Overlap Summary")
    summary.add_column("Metric", style="bold")
    summary.add_column("Value", style="cyan")
    summary.add_row("Domain A Keywords", str(len(keywords_a)))
    summary.add_row("Domain B Keywords", str(len(keywords_b)))
    summary.add_row("Shared Keywords", str(len(shared)))
    summary.add_row("Overlap %", f"{overlap_pct:.1f}%")
    summary.add_row(f"Only {domain_a}", str(len(only_a)))
    summary.add_row(f"Only {domain_b}", str(len(only_b)))
    console.print(summary)

    # Shared keywords
    if shared:
        console.print(f"\n[bold green]Shared Keywords ({len(shared)}):[/bold green]")
        for kw in sorted(shared):
            console.print(f"  {kw}")

    # Unique to A
    if only_a:
        console.print(f"\n[bold yellow]Only {domain_a} ({len(only_a)}):[/bold yellow]")
        for kw in sorted(only_a):
            console.print(f"  {kw}")

    # Unique to B
    if only_b:
        console.print(f"\n[bold yellow]Only {domain_b} ({len(only_b)}):[/bold yellow]")
        for kw in sorted(only_b):
            console.print(f"  {kw}")

    # Competitive interpretation
    console.print(f"\n[bold]Competitive Interpretation:[/bold]")
    if overlap_pct > 70:
        console.print("[red]HIGH overlap — Direct competitors fighting for the same search territory[/red]")
    elif overlap_pct > 40:
        console.print("[yellow]MODERATE overlap — Significant competition with some differentiation[/yellow]")
    elif overlap_pct > 15:
        console.print("[green]LOW overlap — Adjacent competitors with distinct content strategies[/green]")
    else:
        console.print("[blue]MINIMAL overlap — Different search territories, low direct competition[/blue]")

    return {
        'domain_a': domain_a,
        'domain_b': domain_b,
        'overlap_percentage': round(overlap_pct, 1),
        'shared_keywords': sorted(shared),
        'only_a': sorted(only_a),
        'only_b': sorted(only_b),
        'total_a': len(keywords_a),
        'total_b': len(keywords_b),
    }


@click.command()
@click.argument('domain_a')
@click.argument('domain_b')
@click.option('--keywords-a', '-a', required=True, help='Comma-separated keywords for domain A')
@click.option('--keywords-b', '-b', required=True, help='Comma-separated keywords for domain B')
@click.option('--json-output', '-j', is_flag=True, help='Output as JSON')
def main(domain_a, domain_b, keywords_a, keywords_b, json_output):
    """Calculate SERP overlap between two domains.

    Provide keyword lists exported from SEMrush, Ahrefs, or similar tools.
    """
    kw_a = [k.strip() for k in keywords_a.split(',') if k.strip()]
    kw_b = [k.strip() for k in keywords_b.split(',') if k.strip()]

    result = analyze_overlap(domain_a, domain_b, kw_a, kw_b)

    if json_output:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
