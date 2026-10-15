#!/usr/bin/env python3
"""
Pixel Auditor — Audits Meta Pixel and TikTok Pixel implementations.

Validates pixel installation, event configuration, parameter completeness,
and identifies common issues like duplicate initialization or missing events.
"""

import re
import sys
import json
import argparse
from dataclasses import dataclass, field, asdict
from typing import Optional, List
from urllib.parse import urlparse

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# --- Meta Pixel Standard Events ---

META_STANDARD_EVENTS = [
    "PageView", "ViewContent", "Search", "AddToCart", "AddToWishlist",
    "InitiateCheckout", "AddPaymentInfo", "Purchase", "Lead",
    "CompleteRegistration", "Contact", "CustomizeProduct", "Donate",
    "FindLocation", "Schedule", "StartTrial", "SubmitApplication",
]

META_EVENTS_REQUIRING_VALUE = ["Purchase", "AddToCart", "InitiateCheckout", "StartTrial", "Donate"]

# --- TikTok Standard Events ---

TIKTOK_STANDARD_EVENTS = [
    "ViewContent", "ClickButton", "Search", "AddToWishlist", "AddToCart",
    "InitiateCheckout", "AddPaymentInfo", "CompletePayment", "PlaceAnOrder",
    "Contact", "Download", "SubmitForm", "CompleteRegistration", "Subscribe",
]

TIKTOK_EVENTS_REQUIRING_VALUE = ["CompletePayment", "PlaceAnOrder", "AddToCart"]


@dataclass
class PixelFinding:
    platform: str
    finding_type: str  # "info", "warning", "error"
    category: str
    message: str
    details: Optional[str] = None


@dataclass
class PixelAuditResult:
    url: str
    status_code: int = 0
    meta_pixel: dict = field(default_factory=dict)
    tiktok_pixel: dict = field(default_factory=dict)
    findings: List[dict] = field(default_factory=list)
    score: int = 0


def fetch_page(url: str, timeout: int = 15) -> tuple:
    """Fetch page HTML content."""
    if not HAS_REQUESTS:
        return None, 0, "requests library not installed"
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


def audit_meta_pixel(html: str) -> tuple:
    """Audit Meta Pixel implementation. Returns (pixel_data, findings)."""
    findings = []
    pixel_data = {
        "detected": False,
        "pixel_ids": [],
        "events_found": [],
        "custom_events": [],
        "has_noscript": False,
        "has_dedup_event_id": False,
        "init_count": 0,
    }

    # Check pixel presence
    if not re.search(r'connect\.facebook\.net/[a-z_]+/fbevents\.js', html):
        findings.append(PixelFinding(
            platform="Meta", finding_type="error",
            category="Installation", message="Meta Pixel not detected on this page"
        ))
        return pixel_data, findings

    pixel_data["detected"] = True

    # Extract pixel IDs
    init_matches = re.findall(r"fbq\s*\(\s*['\"]init['\"]\s*,\s*['\"](\d+)['\"]", html)
    pixel_data["pixel_ids"] = list(set(init_matches))
    pixel_data["init_count"] = len(init_matches)

    if len(init_matches) == 0:
        findings.append(PixelFinding(
            platform="Meta", finding_type="error",
            category="Installation", message="Pixel script loaded but no fbq('init') call found"
        ))
    elif len(init_matches) > 1:
        unique_ids = set(init_matches)
        if len(unique_ids) > 1:
            findings.append(PixelFinding(
                platform="Meta", finding_type="warning",
                category="Installation",
                message=f"Multiple Pixel IDs initialized: {', '.join(unique_ids)}",
                details="Multiple pixels may cause double-counting. Verify this is intentional."
            ))
        else:
            findings.append(PixelFinding(
                platform="Meta", finding_type="warning",
                category="Installation",
                message=f"Pixel initialized {len(init_matches)} times with same ID",
                details="Duplicate init calls may cause inflated PageView counts."
            ))

    # Check noscript fallback
    pixel_data["has_noscript"] = bool(re.search(r'facebook\.com/tr\?id=\d+', html))
    if not pixel_data["has_noscript"]:
        findings.append(PixelFinding(
            platform="Meta", finding_type="warning",
            category="Installation", message="noscript fallback image tag not found"
        ))

    # Detect standard events
    for event in META_STANDARD_EVENTS:
        pattern = rf"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]{event}['\"]"
        match = re.search(pattern, html)
        if match:
            pixel_data["events_found"].append(event)

            # Check for value parameter on events that need it
            if event in META_EVENTS_REQUIRING_VALUE:
                # Look for value parameter near the event
                event_block = html[match.start():match.start() + 500]
                if not re.search(r'value\s*:', event_block):
                    findings.append(PixelFinding(
                        platform="Meta", finding_type="warning",
                        category="Events",
                        message=f"{event} event missing 'value' parameter",
                        details="Value is needed for value optimization and ROAS reporting."
                    ))
                if not re.search(r'currency\s*:', event_block):
                    findings.append(PixelFinding(
                        platform="Meta", finding_type="warning",
                        category="Events",
                        message=f"{event} event missing 'currency' parameter"
                    ))

    # Detect custom events
    custom_matches = re.findall(r"fbq\s*\(\s*['\"]trackCustom['\"]\s*,\s*['\"]([^'\"]+)['\"]", html)
    pixel_data["custom_events"] = list(set(custom_matches))

    # Check for event deduplication (event_id)
    pixel_data["has_dedup_event_id"] = bool(re.search(r'eventID\s*:', html, re.IGNORECASE))
    if not pixel_data["has_dedup_event_id"]:
        findings.append(PixelFinding(
            platform="Meta", finding_type="warning",
            category="Deduplication",
            message="No eventID found — events may be double-counted if CAPI is also active",
            details="Add {eventID: 'unique_id'} as the 4th parameter to fbq('track') calls."
        ))

    # Check PageView
    if "PageView" not in pixel_data["events_found"]:
        if re.search(r"fbq\s*\(\s*['\"]track['\"]\s*,\s*['\"]PageView['\"]", html):
            pixel_data["events_found"].append("PageView")
        else:
            findings.append(PixelFinding(
                platform="Meta", finding_type="error",
                category="Events", message="PageView event not firing"
            ))

    findings.append(PixelFinding(
        platform="Meta", finding_type="info",
        category="Summary",
        message=f"Events detected: {', '.join(pixel_data['events_found']) if pixel_data['events_found'] else 'None'}",
        details=f"Custom events: {', '.join(pixel_data['custom_events'])}" if pixel_data["custom_events"] else None
    ))

    return pixel_data, findings


def audit_tiktok_pixel(html: str) -> tuple:
    """Audit TikTok Pixel implementation. Returns (pixel_data, findings)."""
    findings = []
    pixel_data = {
        "detected": False,
        "pixel_ids": [],
        "events_found": [],
        "has_identify": False,
        "has_page_call": False,
    }

    if not re.search(r'analytics\.tiktok\.com/i18n/pixel/events\.js', html):
        findings.append(PixelFinding(
            platform="TikTok", finding_type="info",
            category="Installation", message="TikTok Pixel not detected on this page"
        ))
        return pixel_data, findings

    pixel_data["detected"] = True

    # Extract pixel IDs
    load_matches = re.findall(r"ttq\.load\s*\(\s*['\"]([A-Z0-9]+)['\"]", html)
    pixel_data["pixel_ids"] = list(set(load_matches))

    if not load_matches:
        findings.append(PixelFinding(
            platform="TikTok", finding_type="error",
            category="Installation", message="Pixel script loaded but no ttq.load() call found"
        ))

    # Check ttq.page()
    pixel_data["has_page_call"] = bool(re.search(r'ttq\.page\s*\(', html))
    if not pixel_data["has_page_call"]:
        findings.append(PixelFinding(
            platform="TikTok", finding_type="warning",
            category="Installation", message="ttq.page() not called — PageView not tracked"
        ))

    # Detect standard events
    for event in TIKTOK_STANDARD_EVENTS:
        pattern = rf"ttq\.track\s*\(\s*['\"]{event}['\"]"
        match = re.search(pattern, html)
        if match:
            pixel_data["events_found"].append(event)

            if event in TIKTOK_EVENTS_REQUIRING_VALUE:
                event_block = html[match.start():match.start() + 500]
                if not re.search(r'value\s*:', event_block):
                    findings.append(PixelFinding(
                        platform="TikTok", finding_type="warning",
                        category="Events",
                        message=f"{event} event missing 'value' parameter"
                    ))

    # Check advanced matching (identify)
    pixel_data["has_identify"] = bool(re.search(r'ttq\.identify\s*\(', html))
    if not pixel_data["has_identify"]:
        findings.append(PixelFinding(
            platform="TikTok", finding_type="warning",
            category="Advanced Matching",
            message="ttq.identify() not called — advanced matching not active",
            details="Add ttq.identify({email: '...', phone_number: '...'}) for better match rates."
        ))

    findings.append(PixelFinding(
        platform="TikTok", finding_type="info",
        category="Summary",
        message=f"Events detected: {', '.join(pixel_data['events_found']) if pixel_data['events_found'] else 'None'}"
    ))

    return pixel_data, findings


def calculate_score(meta_data: dict, tiktok_data: dict, all_findings: list) -> int:
    """Calculate pixel audit score (0-100)."""
    score = 0
    errors = sum(1 for f in all_findings if f.get("finding_type") == "error")
    warnings = sum(1 for f in all_findings if f.get("finding_type") == "warning")

    # Meta Pixel scoring (60 points if active)
    if meta_data.get("detected"):
        score += 15  # Pixel present
        if meta_data.get("events_found"):
            score += min(len(meta_data["events_found"]) * 5, 20)  # Events (up to 20)
        if meta_data.get("has_dedup_event_id"):
            score += 10  # Deduplication
        if meta_data.get("has_noscript"):
            score += 5  # noscript fallback
        score += 10  # Base for having pixel

    # TikTok Pixel scoring (40 points if active)
    if tiktok_data.get("detected"):
        score += 10  # Pixel present
        if tiktok_data.get("has_page_call"):
            score += 5  # Page tracking
        if tiktok_data.get("events_found"):
            score += min(len(tiktok_data["events_found"]) * 5, 15)  # Events
        if tiktok_data.get("has_identify"):
            score += 10  # Advanced matching

    # Deductions
    score -= errors * 10
    score -= warnings * 3

    return max(0, min(100, score))


def audit_url(url: str) -> dict:
    """Run full pixel audit on a URL."""
    html, status_code, error = fetch_page(url)

    if error:
        return {"url": url, "error": error}

    meta_data, meta_findings = audit_meta_pixel(html)
    tiktok_data, tiktok_findings = audit_tiktok_pixel(html)

    all_findings = [asdict(f) for f in meta_findings + tiktok_findings]
    score = calculate_score(meta_data, tiktok_data, all_findings)

    return {
        "url": url,
        "status_code": status_code,
        "meta_pixel": meta_data,
        "tiktok_pixel": tiktok_data,
        "findings": all_findings,
        "score": score,
        "rating": (
            "Excellent" if score >= 90 else
            "Good" if score >= 70 else
            "Needs Work" if score >= 50 else
            "Poor" if score >= 30 else
            "Critical"
        ),
    }


def main():
    parser = argparse.ArgumentParser(description="Audit Meta Pixel and TikTok Pixel implementations")
    parser.add_argument("urls", nargs="+", help="URLs to audit")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--platform", choices=["meta", "tiktok", "all"], default="all",
                        help="Which platform to audit")
    args = parser.parse_args()

    if not HAS_REQUESTS:
        print("ERROR: 'requests' library required. Install with: pip install requests")
        sys.exit(1)

    results = []
    for url in args.urls:
        if not url.startswith("http"):
            url = f"https://{url}"
        print(f"Auditing: {url}")
        result = audit_url(url)
        results.append(result)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            print(f"\n{'=' * 60}")
            print(f"PIXEL AUDIT: {result['url']}")
            print(f"Score: {result.get('score', 'N/A')}/100 — {result.get('rating', 'N/A')}")
            print(f"{'=' * 60}")

            if result.get("error"):
                print(f"  ERROR: {result['error']}")
                continue

            # Meta summary
            meta = result.get("meta_pixel", {})
            if meta.get("detected"):
                print(f"\nMeta Pixel: DETECTED (ID: {', '.join(meta.get('pixel_ids', []))})")
                print(f"  Events: {', '.join(meta.get('events_found', [])) or 'None'}")
                print(f"  Custom events: {', '.join(meta.get('custom_events', [])) or 'None'}")
                print(f"  Dedup event_id: {'Yes' if meta.get('has_dedup_event_id') else 'No'}")
            else:
                print(f"\nMeta Pixel: NOT DETECTED")

            # TikTok summary
            tt = result.get("tiktok_pixel", {})
            if tt.get("detected"):
                print(f"\nTikTok Pixel: DETECTED (ID: {', '.join(tt.get('pixel_ids', []))})")
                print(f"  Events: {', '.join(tt.get('events_found', [])) or 'None'}")
                print(f"  Advanced matching: {'Yes' if tt.get('has_identify') else 'No'}")
            else:
                print(f"\nTikTok Pixel: NOT DETECTED")

            # Findings
            findings = result.get("findings", [])
            errors = [f for f in findings if f["finding_type"] == "error"]
            warnings = [f for f in findings if f["finding_type"] == "warning"]

            if errors:
                print(f"\nErrors ({len(errors)}):")
                for f in errors:
                    print(f"  [ERROR] [{f['platform']}] {f['message']}")

            if warnings:
                print(f"\nWarnings ({len(warnings)}):")
                for f in warnings:
                    print(f"  [WARN] [{f['platform']}] {f['message']}")
                    if f.get("details"):
                        print(f"    > {f['details']}")


if __name__ == "__main__":
    main()
