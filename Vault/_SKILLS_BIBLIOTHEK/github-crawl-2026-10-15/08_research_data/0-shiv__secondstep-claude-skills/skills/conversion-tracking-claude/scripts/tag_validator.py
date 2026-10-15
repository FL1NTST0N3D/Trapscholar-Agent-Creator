#!/usr/bin/env python3
"""
Tag Validator — Validates tracking tag presence across website pages.

Checks for Google Tag (gtag.js), Meta Pixel, LinkedIn Insight Tag,
TikTok Pixel, and Google Tag Manager on specified URLs.
"""

import re
import sys
import json
import argparse
from urllib.parse import urlparse
from dataclasses import dataclass, field, asdict
from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# --- Tag Detection Patterns ---

TAG_PATTERNS = {
    "google_gtag": {
        "name": "Google Tag (gtag.js)",
        "patterns": [
            r'googletagmanager\.com/gtag/js\?id=(AW-\d+|G-[A-Z0-9]+)',
            r"gtag\s*\(\s*['\"]config['\"]\s*,\s*['\"](AW-\d+|G-[A-Z0-9]+)['\"]",
        ],
        "id_pattern": r'(AW-\d+|G-[A-Z0-9]+)',
    },
    "google_gtm": {
        "name": "Google Tag Manager",
        "patterns": [
            r'googletagmanager\.com/gtm\.js\?id=(GTM-[A-Z0-9]+)',
            r'googletagmanager\.com/ns\.html\?id=(GTM-[A-Z0-9]+)',
        ],
        "id_pattern": r'(GTM-[A-Z0-9]+)',
    },
    "meta_pixel": {
        "name": "Meta Pixel",
        "patterns": [
            r'connect\.facebook\.net/[a-z_]+/fbevents\.js',
            r"fbq\s*\(\s*['\"]init['\"]\s*,\s*['\"](\d+)['\"]",
        ],
        "id_pattern": r"fbq\s*\(\s*['\"]init['\"]\s*,\s*['\"](\d+)['\"]",
    },
    "linkedin_insight": {
        "name": "LinkedIn Insight Tag",
        "patterns": [
            r'snap\.licdn\.com/li\.lms-analytics/insight\.min\.js',
            r'_linkedin_partner_id\s*=\s*["\']?(\d+)',
        ],
        "id_pattern": r'_linkedin_partner_id\s*=\s*["\']?(\d+)',
    },
    "tiktok_pixel": {
        "name": "TikTok Pixel",
        "patterns": [
            r'analytics\.tiktok\.com/i18n/pixel/events\.js',
            r"ttq\.load\s*\(\s*['\"]([A-Z0-9]+)['\"]",
        ],
        "id_pattern": r"ttq\.load\s*\(\s*['\"]([A-Z0-9]+)['\"]",
    },
}

EVENT_PATTERNS = {
    "google_conversions": [
        r"gtag\s*\(\s*['\"]event['\"]\s*,\s*['\"]conversion['\"]",
        r"gtag\s*\(\s*['\"]event['\"]\s*,\s*['\"]purchase['\"]",
        r"gtag\s*\(\s*['\"]event['\"]\s*,\s*['\"]generate_lead['\"]",
    ],
    "meta_events": [
        r"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]Purchase['\"]",
        r"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]Lead['\"]",
        r"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]ViewContent['\"]",
        r"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]AddToCart['\"]",
        r"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]CompleteRegistration['\"]",
        r"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]InitiateCheckout['\"]",
    ],
    "tiktok_events": [
        r"ttq\.track\s*\(\s*['\"]CompletePayment['\"]",
        r"ttq\.track\s*\(\s*['\"]SubmitForm['\"]",
        r"ttq\.track\s*\(\s*['\"]ViewContent['\"]",
        r"ttq\.track\s*\(\s*['\"]AddToCart['\"]",
    ],
    "linkedin_events": [
        r"lintrk\s*\(\s*['\"]track['\"]",
    ],
}


@dataclass
class TagResult:
    tag_name: str
    detected: bool
    tag_id: Optional[str] = None
    events_found: list = field(default_factory=list)
    issues: list = field(default_factory=list)


@dataclass
class PageResult:
    url: str
    status_code: int = 0
    tags: list = field(default_factory=list)
    errors: list = field(default_factory=list)


def fetch_page(url: str, timeout: int = 15) -> tuple:
    """Fetch page HTML content. Returns (html, status_code, error)."""
    if not HAS_REQUESTS:
        return None, 0, "requests library not installed (pip install requests)"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        resp = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        return resp.text, resp.status_code, None
    except requests.RequestException as e:
        return None, 0, str(e)


def detect_tags(html: str) -> list:
    """Detect tracking tags in HTML content."""
    results = []

    for tag_key, tag_config in TAG_PATTERNS.items():
        detected = False
        tag_id = None

        for pattern in tag_config["patterns"]:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                detected = True
                if match.groups():
                    tag_id = match.group(1)
                break

        if detected and not tag_id and tag_config.get("id_pattern"):
            id_match = re.search(tag_config["id_pattern"], html, re.IGNORECASE)
            if id_match:
                tag_id = id_match.group(1)

        issues = []
        if detected:
            # Check for common issues
            if tag_key == "google_gtag":
                if not re.search(r'<script[^>]*async[^>]*src="[^"]*gtag', html):
                    issues.append("Google Tag may be missing async attribute")
                gtag_count = len(re.findall(r"gtag\s*\(\s*['\"]config['\"]", html))
                if gtag_count > 1:
                    issues.append(f"Multiple gtag config calls found ({gtag_count})")

            if tag_key == "meta_pixel":
                init_count = len(re.findall(r"fbq\s*\(\s*['\"]init['\"]", html))
                if init_count > 1:
                    issues.append(f"Multiple Pixel init calls found ({init_count}) — may cause double-counting")

        # Check for relevant events
        events_found = []
        event_key_map = {
            "google_gtag": "google_conversions",
            "google_gtm": "google_conversions",
            "meta_pixel": "meta_events",
            "tiktok_pixel": "tiktok_events",
            "linkedin_insight": "linkedin_events",
        }
        if tag_key in event_key_map:
            for evt_pattern in EVENT_PATTERNS.get(event_key_map[tag_key], []):
                evt_match = re.search(evt_pattern, html, re.IGNORECASE)
                if evt_match:
                    events_found.append(evt_match.group(0)[:60])

        results.append(TagResult(
            tag_name=tag_config["name"],
            detected=detected,
            tag_id=tag_id,
            events_found=events_found,
            issues=issues,
        ))

    return results


def validate_urls(urls: list) -> list:
    """Validate tags across multiple URLs."""
    all_results = []

    for url in urls:
        parsed = urlparse(url)
        if not parsed.scheme:
            url = f"https://{url}"

        print(f"Scanning: {url}")
        html, status_code, error = fetch_page(url)

        page_result = PageResult(url=url, status_code=status_code)

        if error:
            page_result.errors.append(f"Failed to fetch: {error}")
        elif html:
            page_result.tags = [asdict(t) for t in detect_tags(html)]

        all_results.append(asdict(page_result))

    return all_results


def generate_summary(results: list) -> dict:
    """Generate a summary across all scanned pages."""
    tag_presence = {}
    total_pages = len(results)

    for page in results:
        for tag in page.get("tags", []):
            name = tag["tag_name"]
            if name not in tag_presence:
                tag_presence[name] = {
                    "detected_on": 0,
                    "total_pages": total_pages,
                    "ids_found": set(),
                    "all_issues": [],
                }
            if tag["detected"]:
                tag_presence[name]["detected_on"] += 1
                if tag.get("tag_id"):
                    tag_presence[name]["ids_found"].add(tag["tag_id"])
            tag_presence[name]["all_issues"].extend(tag.get("issues", []))

    # Convert sets to lists for JSON serialization
    summary = {}
    for name, data in tag_presence.items():
        coverage = (data["detected_on"] / total_pages * 100) if total_pages > 0 else 0
        summary[name] = {
            "coverage": f"{coverage:.0f}%",
            "pages_with_tag": data["detected_on"],
            "total_pages": total_pages,
            "ids_found": list(data["ids_found"]),
            "issues": list(set(data["all_issues"])),
            "status": "OK" if coverage == 100 else "INCOMPLETE" if coverage > 0 else "MISSING",
        }

    return summary


def main():
    parser = argparse.ArgumentParser(description="Validate tracking tags across website pages")
    parser.add_argument("urls", nargs="+", help="URLs to scan for tracking tags")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--timeout", type=int, default=15, help="Request timeout in seconds")
    args = parser.parse_args()

    if not HAS_REQUESTS:
        print("ERROR: 'requests' library required. Install with: pip install requests")
        sys.exit(1)

    results = validate_urls(args.urls)
    summary = generate_summary(results)

    if args.json:
        output = {"pages": results, "summary": summary}
        print(json.dumps(output, indent=2))
    else:
        print("\n" + "=" * 60)
        print("TAG VALIDATION SUMMARY")
        print("=" * 60)

        for tag_name, data in summary.items():
            status_icon = "PASS" if data["status"] == "OK" else "WARN" if data["status"] == "INCOMPLETE" else "FAIL"
            print(f"\n[{status_icon}] {tag_name}")
            print(f"  Coverage: {data['coverage']} ({data['pages_with_tag']}/{data['total_pages']} pages)")
            if data["ids_found"]:
                print(f"  IDs: {', '.join(data['ids_found'])}")
            for issue in data["issues"]:
                print(f"  Issue: {issue}")

        print("\n" + "=" * 60)
        print(f"Pages scanned: {len(results)}")
        errors = sum(1 for r in results if r.get("errors"))
        if errors:
            print(f"Pages with errors: {errors}")


if __name__ == "__main__":
    main()
