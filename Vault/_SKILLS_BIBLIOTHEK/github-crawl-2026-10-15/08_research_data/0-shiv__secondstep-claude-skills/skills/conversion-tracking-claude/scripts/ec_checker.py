#!/usr/bin/env python3
"""
Enhanced Conversions Checker — Validates EC for Web and EC4L configuration.

Checks for user data hashing, GCLID capture, and Enhanced Conversions
implementation patterns in website source code.
"""

import re
import sys
import json
import hashlib
import argparse
from dataclasses import dataclass, field, asdict
from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# --- EC Detection Patterns ---

EC_WEB_PATTERNS = {
    "gtag_user_data": {
        "description": "gtag set user_data call",
        "patterns": [
            r"gtag\s*\(\s*['\"]set['\"]\s*,\s*['\"]user_data['\"]",
            r"gtag\s*\(\s*['\"]config['\"][^)]*user_data",
        ],
    },
    "gtm_user_provided_data": {
        "description": "GTM User-Provided Data variable",
        "patterns": [
            r"user[_-]?provided[_-]?data",
            r"enhanced[_-]?conversions",
        ],
    },
    "email_field": {
        "description": "Email field detection",
        "patterns": [
            r'<input[^>]*type=["\']email["\'][^>]*>',
            r'<input[^>]*name=["\']email["\'][^>]*>',
            r'<input[^>]*id=["\']email["\'][^>]*>',
        ],
    },
    "phone_field": {
        "description": "Phone field detection",
        "patterns": [
            r'<input[^>]*type=["\']tel["\'][^>]*>',
            r'<input[^>]*name=["\']phone["\'][^>]*>',
            r'<input[^>]*name=["\']telephone["\'][^>]*>',
        ],
    },
}

GCLID_PATTERNS = {
    "url_param_capture": {
        "description": "GCLID URL parameter extraction",
        "patterns": [
            r'["\']gclid["\']',
            r'URLSearchParams.*gclid',
            r'getParam.*gclid',
            r'get\s*\(\s*["\']gclid["\']',
        ],
    },
    "hidden_field": {
        "description": "GCLID hidden form field",
        "patterns": [
            r'<input[^>]*type=["\']hidden["\'][^>]*name=["\']gclid["\'][^>]*>',
            r'<input[^>]*name=["\']gclid["\'][^>]*type=["\']hidden["\'][^>]*>',
            r'id=["\']gclid["\']',
        ],
    },
    "cookie_storage": {
        "description": "GCLID cookie storage",
        "patterns": [
            r'cookie.*gclid',
            r'gclid.*cookie',
            r'setCookie.*gclid',
            r'document\.cookie.*gclid',
        ],
    },
    "wbraid_gbraid": {
        "description": "WBRAID/GBRAID capture (iOS)",
        "patterns": [
            r'["\']wbraid["\']',
            r'["\']gbraid["\']',
        ],
    },
}

DATA_HASHING_PATTERNS = {
    "sha256": {
        "description": "SHA-256 hashing implementation",
        "patterns": [
            r'sha256',
            r'SHA-256',
            r'crypto\.subtle\.digest',
            r'CryptoJS\.SHA256',
            r'hashlib\.sha256',
        ],
    },
    "normalization": {
        "description": "Data normalization (lowercase, trim)",
        "patterns": [
            r'\.toLowerCase\s*\(\)',
            r'\.trim\s*\(\)',
            r'\.strip\s*\(\)',
            r'\.lower\s*\(\)',
        ],
    },
}


@dataclass
class ECCheckResult:
    category: str
    check_name: str
    detected: bool
    description: str
    details: list = field(default_factory=list)
    issues: list = field(default_factory=list)


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


def check_ec_web(html: str) -> list:
    """Check Enhanced Conversions for Web implementation."""
    results = []

    for key, config in EC_WEB_PATTERNS.items():
        detected = False
        details = []
        for pattern in config["patterns"]:
            matches = re.findall(pattern, html, re.IGNORECASE)
            if matches:
                detected = True
                details.extend([m[:80] if isinstance(m, str) else str(m)[:80] for m in matches[:3]])

        issues = []
        if key == "email_field" and not detected:
            issues.append("No email input field found — EC Web needs email for matching")
        if key == "gtag_user_data" and not detected:
            issues.append("No gtag user_data call found — EC Web may not be sending user data")

        results.append(ECCheckResult(
            category="EC Web",
            check_name=config["description"],
            detected=detected,
            description=f"{'Found' if detected else 'Not found'}: {config['description']}",
            details=details,
            issues=issues,
        ))

    return results


def check_gclid_capture(html: str) -> list:
    """Check GCLID capture implementation."""
    results = []

    for key, config in GCLID_PATTERNS.items():
        detected = False
        details = []
        for pattern in config["patterns"]:
            matches = re.findall(pattern, html, re.IGNORECASE)
            if matches:
                detected = True
                details.extend([m[:80] if isinstance(m, str) else str(m)[:80] for m in matches[:3]])

        issues = []
        if key == "url_param_capture" and not detected:
            issues.append("No GCLID URL parameter capture code found")
        if key == "hidden_field" and not detected:
            issues.append("No hidden GCLID form field found — GCLID may not be submitted with leads")

        results.append(ECCheckResult(
            category="EC4L / GCLID",
            check_name=config["description"],
            detected=detected,
            description=f"{'Found' if detected else 'Not found'}: {config['description']}",
            details=details,
            issues=issues,
        ))

    return results


def check_data_hashing(html: str) -> list:
    """Check data hashing implementation."""
    results = []

    for key, config in DATA_HASHING_PATTERNS.items():
        detected = False
        details = []
        for pattern in config["patterns"]:
            matches = re.findall(pattern, html, re.IGNORECASE)
            if matches:
                detected = True
                details.extend([m[:80] if isinstance(m, str) else str(m)[:80] for m in matches[:3]])

        results.append(ECCheckResult(
            category="Data Hashing",
            check_name=config["description"],
            detected=detected,
            description=f"{'Found' if detected else 'Not found'}: {config['description']}",
            details=details,
        ))

    return results


def validate_hash(value: str, expected_type: str = "email") -> dict:
    """Validate that a value is correctly hashed for EC."""
    result = {
        "original": value,
        "type": expected_type,
        "is_hashed": False,
        "correct_hash": None,
        "issues": [],
    }

    # Check if already hashed (64 hex chars = SHA-256)
    if re.match(r'^[a-f0-9]{64}$', value):
        result["is_hashed"] = True
        return result

    # Normalize and hash
    if expected_type == "email":
        normalized = value.strip().lower()
    elif expected_type == "phone":
        normalized = re.sub(r'[^0-9+]', '', value)
        if not normalized.startswith('+'):
            result["issues"].append("Phone should be in E.164 format (e.g., +12125551234)")
    else:
        normalized = value.strip().lower()

    correct_hash = hashlib.sha256(normalized.encode('utf-8')).hexdigest()
    result["correct_hash"] = correct_hash
    result["normalized"] = normalized

    return result


def run_checks(url: str) -> dict:
    """Run all EC checks on a URL."""
    html, status_code, error = fetch_page(url)

    if error:
        return {"url": url, "error": error, "results": []}

    ec_web = check_ec_web(html)
    gclid = check_gclid_capture(html)
    hashing = check_data_hashing(html)

    all_results = ec_web + gclid + hashing

    # Calculate EC readiness score
    ec_web_detected = any(r.detected for r in ec_web if "user_data" in r.check_name.lower())
    gclid_detected = any(r.detected for r in gclid if "url" in r.check_name.lower() or "hidden" in r.check_name.lower())
    email_detected = any(r.detected for r in ec_web if "email" in r.check_name.lower())

    score = 0
    if ec_web_detected:
        score += 40
    if gclid_detected:
        score += 30
    if email_detected:
        score += 15
    if any(r.detected for r in hashing):
        score += 15

    all_issues = []
    for r in all_results:
        all_issues.extend(r.issues)

    return {
        "url": url,
        "status_code": status_code,
        "ec_readiness_score": score,
        "ec_readiness_rating": (
            "Good" if score >= 70 else
            "Partial" if score >= 40 else
            "Poor" if score > 0 else
            "Not Detected"
        ),
        "results": [asdict(r) for r in all_results],
        "issues": all_issues,
    }


def main():
    parser = argparse.ArgumentParser(description="Check Enhanced Conversions implementation")
    parser.add_argument("urls", nargs="+", help="URLs to check (use thank-you / conversion pages)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--hash-test", nargs=2, metavar=("VALUE", "TYPE"),
                        help="Test hashing a value (e.g., --hash-test user@email.com email)")
    args = parser.parse_args()

    if args.hash_test:
        result = validate_hash(args.hash_test[0], args.hash_test[1])
        print(json.dumps(result, indent=2))
        return

    if not HAS_REQUESTS:
        print("ERROR: 'requests' library required. Install with: pip install requests")
        sys.exit(1)

    all_results = []
    for url in args.urls:
        if not url.startswith("http"):
            url = f"https://{url}"
        print(f"Checking: {url}")
        result = run_checks(url)
        all_results.append(result)

    if args.json:
        print(json.dumps(all_results, indent=2))
    else:
        for result in all_results:
            print(f"\n{'=' * 60}")
            print(f"EC CHECK: {result['url']}")
            print(f"EC Readiness Score: {result.get('ec_readiness_score', 'N/A')}/100 — {result.get('ec_readiness_rating', 'N/A')}")
            print(f"{'=' * 60}")

            current_category = None
            for r in result.get("results", []):
                if r["category"] != current_category:
                    current_category = r["category"]
                    print(f"\n--- {current_category} ---")

                status = "FOUND" if r["detected"] else "NOT FOUND"
                print(f"  [{status}] {r['check_name']}")
                for detail in r.get("details", []):
                    print(f"    > {detail}")
                for issue in r.get("issues", []):
                    print(f"    ! {issue}")

            if result.get("issues"):
                print(f"\nAll Issues:")
                for issue in result["issues"]:
                    print(f"  - {issue}")


if __name__ == "__main__":
    main()
