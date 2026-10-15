#!/usr/bin/env python3
"""
Technology Stack Detector
Detects CMS, analytics, marketing tools, and frameworks from HTTP headers and page source.

Usage:
    python tech_detect.py <url>
    python tech_detect.py https://competitor.com
"""

import sys
import re
import json
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
import click


console = Console()

# Technology signatures
SIGNATURES = {
    'CMS': {
        'WordPress': [r'wp-content', r'wp-includes', r'wordpress', r'wp-json'],
        'Webflow': [r'webflow\.com', r'webflow\.js'],
        'Shopify': [r'cdn\.shopify\.com', r'shopify\.com'],
        'Squarespace': [r'squarespace\.com', r'sqsp\.com'],
        'Wix': [r'wix\.com', r'wixstatic\.com'],
        'Ghost': [r'ghost\.io', r'ghost\.org'],
        'Contentful': [r'contentful\.com', r'ctfassets\.net'],
        'HubSpot CMS': [r'hs-sites\.com', r'hubspot\.net'],
    },
    'Analytics': {
        'Google Analytics (GA4)': [r'gtag.*G-', r'googletagmanager.*gtag'],
        'Google Analytics (UA)': [r'google-analytics\.com.*ua-', r'analytics\.js'],
        'Google Tag Manager': [r'googletagmanager\.com', r'gtm\.js', r'GTM-'],
        'Mixpanel': [r'mixpanel\.com', r'mixpanel\.init'],
        'Amplitude': [r'amplitude\.com', r'amplitude\.init'],
        'Segment': [r'segment\.com', r'analytics\.load'],
        'Plausible': [r'plausible\.io'],
        'Fathom': [r'usefathom\.com'],
        'Hotjar': [r'hotjar\.com', r'hj\.js'],
        'Microsoft Clarity': [r'clarity\.ms'],
        'FullStory': [r'fullstory\.com', r'fs\.js'],
    },
    'Marketing': {
        'HubSpot': [r'hubspot\.com', r'hs-scripts\.com', r'hbspt\.forms'],
        'Marketo': [r'marketo\.com', r'munchkin', r'mkto'],
        'Salesforce': [r'salesforce\.com', r'pardot\.com'],
        'Intercom': [r'intercom\.io', r'intercomcdn\.com'],
        'Drift': [r'drift\.com', r'driftt\.com'],
        'Zendesk': [r'zendesk\.com', r'zdassets\.com'],
        'Crisp': [r'crisp\.chat'],
        'Calendly': [r'calendly\.com'],
        'Mailchimp': [r'mailchimp\.com', r'chimpstatic\.com'],
        'ActiveCampaign': [r'activecampaign\.com'],
        'Klaviyo': [r'klaviyo\.com'],
    },
    'Advertising': {
        'Google Ads': [r'googleads\.g\.doubleclick', r'google_conversion', r'AW-'],
        'Meta Pixel': [r'facebook\.net.*fbq', r'fbevents\.js', r'connect\.facebook'],
        'LinkedIn Insight': [r'snap\.licdn\.com', r'linkedin.*insight'],
        'Twitter Pixel': [r'static\.ads-twitter\.com', r'twq\('],
        'TikTok Pixel': [r'analytics\.tiktok\.com'],
        'Pinterest Tag': [r'pintrk'],
        'AdRoll': [r'adroll\.com'],
    },
    'Frameworks': {
        'React': [r'react\.js', r'react-dom', r'__NEXT_DATA__', r'_next/'],
        'Vue.js': [r'vue\.js', r'vue\.min\.js', r'__vue__'],
        'Angular': [r'angular\.js', r'ng-app', r'ng-controller'],
        'Next.js': [r'_next/', r'__NEXT_DATA__'],
        'Nuxt.js': [r'_nuxt/', r'__NUXT__'],
        'Gatsby': [r'gatsby', r'___gatsby'],
        'Svelte': [r'svelte'],
        'jQuery': [r'jquery\.min\.js', r'jquery-\d'],
        'Tailwind CSS': [r'tailwindcss', r'tailwind\.css'],
        'Bootstrap': [r'bootstrap\.min', r'bootstrap\.css'],
    },
    'Payments': {
        'Stripe': [r'stripe\.com', r'js\.stripe\.com'],
        'PayPal': [r'paypal\.com', r'paypalobjects\.com'],
        'Braintree': [r'braintree', r'braintreegateway'],
        'Chargebee': [r'chargebee\.com'],
        'Paddle': [r'paddle\.com'],
    },
    'Infrastructure': {
        'Cloudflare': [r'cloudflare', r'cf-ray', r'__cf_bm'],
        'AWS': [r'amazonaws\.com', r'aws\.'],
        'Vercel': [r'vercel\.app', r'vercel\.com'],
        'Netlify': [r'netlify\.app', r'netlify\.com'],
        'Fastly': [r'fastly\.net'],
    },
}


def detect_from_headers(headers):
    """Detect technologies from HTTP response headers."""
    detected = []
    header_str = json.dumps(dict(headers), default=str).lower()

    for category, techs in SIGNATURES.items():
        for tech, patterns in techs.items():
            for pattern in patterns:
                if re.search(pattern.lower(), header_str):
                    detected.append({
                        'technology': tech,
                        'category': category,
                        'confidence': 'Confirmed',
                        'evidence': f'HTTP header match: {pattern}',
                    })
                    break
    return detected


def detect_from_source(html):
    """Detect technologies from page source."""
    detected = []
    html_lower = html.lower()

    for category, techs in SIGNATURES.items():
        for tech, patterns in techs.items():
            for pattern in patterns:
                if re.search(pattern.lower(), html_lower):
                    detected.append({
                        'technology': tech,
                        'category': category,
                        'confidence': 'Likely',
                        'evidence': f'Source match: {pattern}',
                    })
                    break
    return detected


def deduplicate(detections):
    """Remove duplicate detections, keeping highest confidence."""
    seen = {}
    for d in detections:
        key = d['technology']
        if key not in seen or d['confidence'] == 'Confirmed':
            seen[key] = d
    return list(seen.values())


def analyze_tech_stack(url):
    """Main function to detect technology stack."""
    if not url.startswith('http'):
        url = f'https://{url}'

    console.print(f"\n[bold blue]Detecting tech stack:[/bold blue] {url}\n")

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; TechDetector/1.0)'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
    except requests.RequestException as e:
        console.print(f"[red]Error fetching URL: {e}[/red]")
        return None

    # Detect from headers and source
    header_detections = detect_from_headers(response.headers)
    source_detections = detect_from_source(response.text)

    all_detections = deduplicate(header_detections + source_detections)

    # Group by category
    by_category = {}
    for d in all_detections:
        cat = d['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(d)

    # Display results
    for category, techs in by_category.items():
        table = Table(title=category)
        table.add_column("Technology", style="cyan")
        table.add_column("Confidence", style="green")
        table.add_column("Evidence", style="dim")
        for tech in techs:
            table.add_row(tech['technology'], tech['confidence'], tech['evidence'])
        console.print(table)
        console.print()

    result = {
        'url': url,
        'domain': urlparse(url).netloc,
        'technologies': all_detections,
        'by_category': {k: [t['technology'] for t in v] for k, v in by_category.items()},
        'total_detected': len(all_detections),
    }

    console.print(f"[bold green]Total technologies detected: {len(all_detections)}[/bold green]\n")
    return result


@click.command()
@click.argument('url')
@click.option('--json-output', '-j', is_flag=True, help='Output as JSON')
def main(url, json_output):
    """Detect the technology stack of a competitor's website."""
    result = analyze_tech_stack(url)
    if result and json_output:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
