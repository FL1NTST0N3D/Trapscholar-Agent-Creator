#!/usr/bin/env python3
"""
Pricing Page Data Extractor
Extracts and structures pricing information from competitor websites.

Usage:
    python scrape_pricing.py <url>
    python scrape_pricing.py https://competitor.com/pricing
"""

import sys
import json
import re
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
import click


console = Console()


def extract_prices(soup):
    """Extract price values from page content."""
    prices = []
    # Common pricing patterns
    price_patterns = [
        r'\$[\d,]+(?:\.\d{2})?(?:/mo(?:nth)?)?',
        r'[\d,]+(?:\.\d{2})?\s*(?:USD|EUR|GBP)',
        r'(?:Starting at|From)\s*\$[\d,]+',
    ]
    text = soup.get_text()
    for pattern in price_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        prices.extend(matches)
    return list(set(prices))


def extract_tiers(soup):
    """Extract pricing tier names and details."""
    tiers = []
    # Look for common pricing card patterns
    tier_selectors = [
        '.pricing-card', '.plan', '.tier',
        '[class*="pricing"]', '[class*="plan"]',
        '.price-column', '.pricing-column',
    ]
    for selector in tier_selectors:
        cards = soup.select(selector)
        if cards:
            for card in cards:
                tier = {
                    'name': '',
                    'price': '',
                    'features': [],
                }
                # Try to extract tier name
                header = card.find(['h2', 'h3', 'h4'])
                if header:
                    tier['name'] = header.get_text(strip=True)
                # Extract price
                price_el = card.select_one('[class*="price"], .amount, .cost')
                if price_el:
                    tier['price'] = price_el.get_text(strip=True)
                # Extract features
                features = card.select('li, [class*="feature"]')
                tier['features'] = [f.get_text(strip=True) for f in features]
                if tier['name'] or tier['price']:
                    tiers.append(tier)
            break
    return tiers


def extract_cta_buttons(soup):
    """Extract CTA button text from pricing page."""
    ctas = []
    buttons = soup.select('a[class*="btn"], button, a[class*="cta"], a[class*="button"]')
    for btn in buttons:
        text = btn.get_text(strip=True)
        href = btn.get('href', '')
        if text and len(text) < 50:
            ctas.append({'text': text, 'href': href})
    return ctas


def analyze_pricing_page(url):
    """Main function to analyze a pricing page."""
    console.print(f"\n[bold blue]Analyzing pricing page:[/bold blue] {url}\n")

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; PricingAnalyzer/1.0)'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        console.print(f"[red]Error fetching URL: {e}[/red]")
        return None

    soup = BeautifulSoup(response.text, 'lxml')

    # Extract data
    result = {
        'url': url,
        'domain': urlparse(url).netloc,
        'title': soup.title.string if soup.title else '',
        'prices_found': extract_prices(soup),
        'tiers': extract_tiers(soup),
        'ctas': extract_cta_buttons(soup),
    }

    # Display results
    console.print("[bold green]Prices Found:[/bold green]")
    for price in result['prices_found']:
        console.print(f"  {price}")

    if result['tiers']:
        table = Table(title="Pricing Tiers")
        table.add_column("Tier", style="cyan")
        table.add_column("Price", style="green")
        table.add_column("Features", style="white")
        for tier in result['tiers']:
            features = '\n'.join(tier['features'][:5])
            if len(tier['features']) > 5:
                features += f'\n... +{len(tier["features"]) - 5} more'
            table.add_row(tier['name'], tier['price'], features)
        console.print(table)

    if result['ctas']:
        console.print("\n[bold green]CTA Buttons:[/bold green]")
        for cta in result['ctas'][:10]:
            console.print(f"  [{cta['text']}] -> {cta['href']}")

    return result


@click.command()
@click.argument('url')
@click.option('--json-output', '-j', is_flag=True, help='Output as JSON')
def main(url, json_output):
    """Extract pricing data from a competitor's pricing page."""
    result = analyze_pricing_page(url)
    if result and json_output:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
