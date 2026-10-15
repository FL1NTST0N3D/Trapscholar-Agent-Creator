#!/usr/bin/env python3
"""
GA4 Event Validator

Validates GA4 event names and parameters against Google's specifications.
Checks naming conventions, parameter requirements, and data types.

Usage:
    python event_validator.py --event '{"name": "purchase", "params": {"transaction_id": "T123", "value": 99.99}}'
    python event_validator.py --file events.json
    python event_validator.py --datalayer '{"event": "purchase", "ecommerce": {...}}'
"""

import argparse
import json
import re
import sys
from typing import Any, Dict, List, Optional, Tuple


# Reserved prefixes that cannot be used in event names
RESERVED_PREFIXES = ("firebase_", "ga_", "google_", "gtag.")

# Reserved event names that cannot be used
RESERVED_EVENTS = {
    "ad_activeview", "ad_click", "ad_exposure", "ad_impression",
    "ad_query", "adunit_exposure", "app_clear_data", "app_exception",
    "app_install", "app_remove", "app_store_refund",
    "app_store_subscription_cancel", "app_store_subscription_convert",
    "app_store_subscription_renew", "app_update", "dynamic_link_app_open",
    "dynamic_link_app_update", "dynamic_link_first_open", "error",
    "firebase_campaign", "firebase_in_app_message_action",
    "firebase_in_app_message_dismiss", "firebase_in_app_message_impression",
    "first_open", "first_visit", "in_app_purchase",
    "notification_dismiss", "notification_foreground", "notification_open",
    "notification_receive", "os_update", "screen_view", "session_start",
    "user_engagement",
}

# Google recommended events with required and optional parameters
RECOMMENDED_EVENTS = {
    "add_payment_info": {
        "required": [],
        "recommended": ["currency", "value", "coupon", "payment_type", "items"],
    },
    "add_shipping_info": {
        "required": [],
        "recommended": ["currency", "value", "coupon", "shipping_tier", "items"],
    },
    "add_to_cart": {
        "required": [],
        "recommended": ["currency", "value", "items"],
    },
    "add_to_wishlist": {
        "required": [],
        "recommended": ["currency", "value", "items"],
    },
    "begin_checkout": {
        "required": [],
        "recommended": ["currency", "value", "coupon", "items"],
    },
    "generate_lead": {
        "required": [],
        "recommended": ["currency", "value"],
    },
    "login": {
        "required": [],
        "recommended": ["method"],
    },
    "purchase": {
        "required": ["currency", "transaction_id", "value"],
        "recommended": ["affiliation", "coupon", "shipping", "tax", "items"],
    },
    "refund": {
        "required": ["currency", "transaction_id", "value"],
        "recommended": ["affiliation", "coupon", "shipping", "tax", "items"],
    },
    "remove_from_cart": {
        "required": [],
        "recommended": ["currency", "value", "items"],
    },
    "search": {
        "required": [],
        "recommended": ["search_term"],
    },
    "select_content": {
        "required": [],
        "recommended": ["content_type", "item_id"],
    },
    "select_item": {
        "required": [],
        "recommended": ["item_list_id", "item_list_name", "items"],
    },
    "select_promotion": {
        "required": [],
        "recommended": [
            "creative_name", "creative_slot", "location_id",
            "promotion_id", "promotion_name", "items",
        ],
    },
    "share": {
        "required": [],
        "recommended": ["method", "content_type", "item_id"],
    },
    "sign_up": {
        "required": [],
        "recommended": ["method"],
    },
    "tutorial_begin": {
        "required": [],
        "recommended": [],
    },
    "tutorial_complete": {
        "required": [],
        "recommended": [],
    },
    "view_cart": {
        "required": [],
        "recommended": ["currency", "value", "items"],
    },
    "view_item": {
        "required": [],
        "recommended": ["currency", "value", "items"],
    },
    "view_item_list": {
        "required": [],
        "recommended": ["item_list_id", "item_list_name", "items"],
    },
    "view_promotion": {
        "required": [],
        "recommended": [
            "creative_name", "creative_slot", "location_id",
            "promotion_id", "promotion_name", "items",
        ],
    },
}

# PII patterns to detect
PII_PATTERNS = [
    (r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "email address"),
    (r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", "phone number"),
    (r"\b\d{3}-\d{2}-\d{4}\b", "SSN"),
    (r"\b\d{16}\b", "credit card number"),
]

# ISO 4217 currency codes (common subset)
VALID_CURRENCIES = {
    "USD", "EUR", "GBP", "CAD", "AUD", "JPY", "CNY", "INR", "BRL",
    "MXN", "CHF", "SEK", "NOK", "DKK", "NZD", "SGD", "HKD", "KRW",
    "TWD", "THB", "MYR", "PHP", "IDR", "VND", "ZAR", "AED", "SAR",
    "TRY", "PLN", "CZK", "HUF", "RON", "BGN", "HRK", "ILS", "EGP",
    "NGN", "KES", "GHS", "COP", "PEN", "CLP", "ARS", "PKR", "BDT",
    "LKR", "MMK", "KHR", "LAK",
}


class ValidationResult:
    def __init__(self):
        self.passed: List[str] = []
        self.failed: List[str] = []
        self.warnings: List[str] = []

    @property
    def is_valid(self) -> bool:
        return len(self.failed) == 0

    def to_dict(self) -> Dict:
        return {
            "is_valid": self.is_valid,
            "passed": self.passed,
            "failed": self.failed,
            "warnings": self.warnings,
            "total_checks": len(self.passed) + len(self.failed) + len(self.warnings),
        }


def validate_event_name(name: str) -> ValidationResult:
    """Validate a GA4 event name against naming rules."""
    result = ValidationResult()

    # Check snake_case
    if name != name.lower():
        result.failed.append(f"Event name '{name}' is not lowercase. Use '{name.lower()}'")
    elif not re.match(r"^[a-z][a-z0-9_]*$", name):
        result.failed.append(
            f"Event name '{name}' is not valid snake_case. "
            "Use only lowercase letters, numbers, and underscores."
        )
    else:
        result.passed.append("Event name is valid snake_case")

    # Check length
    if len(name) > 40:
        result.failed.append(
            f"Event name '{name}' is {len(name)} characters (max 40)"
        )
    else:
        result.passed.append(f"Event name length OK ({len(name)}/40)")

    # Check starts with letter
    if not name[0].isalpha():
        result.failed.append(f"Event name '{name}' must start with a letter")
    else:
        result.passed.append("Event name starts with a letter")

    # Check reserved prefixes
    for prefix in RESERVED_PREFIXES:
        if name.startswith(prefix):
            result.failed.append(
                f"Event name '{name}' uses reserved prefix '{prefix}'"
            )
            break
    else:
        result.passed.append("No reserved prefix used")

    # Check reserved names
    if name in RESERVED_EVENTS:
        result.warnings.append(
            f"Event name '{name}' is a reserved/auto-collected event. "
            "Ensure you are not overriding it with a custom event."
        )

    # Check if it's a recommended event
    if name in RECOMMENDED_EVENTS:
        result.passed.append(f"'{name}' is a Google recommended event name")
    else:
        result.warnings.append(
            f"'{name}' is a custom event name. Check if a Google recommended "
            "event name exists for this action."
        )

    return result


def validate_parameters(
    event_name: str,
    params: Dict[str, Any],
) -> ValidationResult:
    """Validate event parameters."""
    result = ValidationResult()

    if not params:
        result.warnings.append("No parameters provided for validation")
        return result

    # Check parameter count (excluding items array)
    custom_params = {k: v for k, v in params.items() if k != "items"}
    if len(custom_params) > 25:
        result.failed.append(
            f"Event has {len(custom_params)} custom parameters (max 25)"
        )
    else:
        result.passed.append(f"Parameter count OK ({len(custom_params)}/25)")

    # Check each parameter
    for param_name, param_value in params.items():
        if param_name == "items":
            continue  # Validated separately

        # Parameter name checks
        if len(param_name) > 40:
            result.failed.append(
                f"Parameter '{param_name}' is {len(param_name)} chars (max 40)"
            )

        if param_name != param_name.lower() or not re.match(
            r"^[a-z][a-z0-9_]*$", param_name
        ):
            result.failed.append(
                f"Parameter '{param_name}' is not valid snake_case"
            )

        # Parameter value checks
        if isinstance(param_value, str):
            if len(param_value) > 100:
                result.failed.append(
                    f"Parameter '{param_name}' value is {len(param_value)} "
                    "chars (max 100)"
                )

            # PII check
            for pattern, pii_type in PII_PATTERNS:
                if re.search(pattern, param_value):
                    result.failed.append(
                        f"CRITICAL: Parameter '{param_name}' may contain "
                        f"{pii_type}: '{param_value[:20]}...'"
                    )

        # Currency check
        if param_name == "currency":
            if isinstance(param_value, str) and param_value.upper() in VALID_CURRENCIES:
                result.passed.append(f"Currency '{param_value}' is valid ISO 4217")
            else:
                result.failed.append(
                    f"Currency '{param_value}' is not a valid ISO 4217 code"
                )

        # Value/price should be numeric
        if param_name in ("value", "price", "tax", "shipping", "discount"):
            if isinstance(param_value, str):
                result.failed.append(
                    f"Parameter '{param_name}' is a string ('{param_value}') "
                    "but should be a number"
                )
            elif isinstance(param_value, (int, float)):
                result.passed.append(f"Parameter '{param_name}' is numeric")

    # Check required parameters for recommended events
    if event_name in RECOMMENDED_EVENTS:
        spec = RECOMMENDED_EVENTS[event_name]
        for req_param in spec["required"]:
            if req_param not in params:
                result.failed.append(
                    f"REQUIRED parameter '{req_param}' is missing for "
                    f"'{event_name}' event"
                )
            else:
                result.passed.append(
                    f"Required parameter '{req_param}' is present"
                )

        for rec_param in spec["recommended"]:
            if rec_param not in params:
                result.warnings.append(
                    f"Recommended parameter '{rec_param}' is missing for "
                    f"'{event_name}' event"
                )

    return result


def validate_items_array(items: List[Dict]) -> ValidationResult:
    """Validate the items array for e-commerce events."""
    result = ValidationResult()

    if not items:
        result.failed.append("Items array is empty")
        return result

    if len(items) > 200:
        result.failed.append(f"Items array has {len(items)} items (max 200)")

    for i, item in enumerate(items):
        prefix = f"Item[{i}]"

        # Must have item_id or item_name
        has_id = "item_id" in item
        has_name = "item_name" in item
        if not has_id and not has_name:
            result.failed.append(
                f"{prefix}: Missing both item_id and item_name (at least one required)"
            )
        else:
            if has_id:
                result.passed.append(f"{prefix}: item_id present")
            if has_name:
                result.passed.append(f"{prefix}: item_name present")

        # Price should be numeric
        if "price" in item:
            if isinstance(item["price"], str):
                result.failed.append(
                    f"{prefix}: price is a string ('{item['price']}'), "
                    "should be a number"
                )
            elif isinstance(item["price"], (int, float)):
                if item["price"] < 0:
                    result.warnings.append(f"{prefix}: price is negative")
                else:
                    result.passed.append(f"{prefix}: price is valid")

        # Quantity should be positive integer
        if "quantity" in item:
            if not isinstance(item["quantity"], int) or item["quantity"] < 1:
                result.failed.append(
                    f"{prefix}: quantity should be a positive integer, "
                    f"got '{item['quantity']}'"
                )
            else:
                result.passed.append(f"{prefix}: quantity is valid")

        # Check for recommended item parameters
        recommended_item_params = [
            "item_brand", "item_category", "item_variant"
        ]
        for param in recommended_item_params:
            if param not in item:
                result.warnings.append(
                    f"{prefix}: Recommended parameter '{param}' is missing"
                )

    return result


def validate_event(event: Dict) -> Dict:
    """Validate a complete event (name + parameters + items)."""
    name = event.get("name", event.get("event", ""))
    params = event.get("params", event.get("parameters", {}))
    items = params.get("items", event.get("ecommerce", {}).get("items", []))

    name_result = validate_event_name(name)
    param_result = validate_parameters(name, params)
    items_result = validate_items_array(items) if items else ValidationResult()

    return {
        "event_name": name,
        "is_recommended": name in RECOMMENDED_EVENTS,
        "name_validation": name_result.to_dict(),
        "parameter_validation": param_result.to_dict(),
        "items_validation": items_result.to_dict() if items else None,
        "overall_valid": (
            name_result.is_valid
            and param_result.is_valid
            and (items_result.is_valid if items else True)
        ),
    }


def print_validation(result: Dict) -> None:
    """Print formatted validation results."""
    name = result["event_name"]
    status = "VALID" if result["overall_valid"] else "HAS ISSUES"
    event_type = "Recommended" if result["is_recommended"] else "Custom"

    print(f"\n{'=' * 50}")
    print(f"Event: {name} ({event_type})")
    print(f"Status: {status}")
    print(f"{'=' * 50}")

    for section_name, section_key in [
        ("Name", "name_validation"),
        ("Parameters", "parameter_validation"),
        ("Items", "items_validation"),
    ]:
        section = result.get(section_key)
        if section is None:
            continue

        print(f"\n  {section_name}:")
        for item in section.get("passed", []):
            print(f"    [PASS] {item}")
        for item in section.get("failed", []):
            print(f"    [FAIL] {item}")
        for item in section.get("warnings", []):
            print(f"    [WARN] {item}")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Validate GA4 event names and parameters."
    )
    parser.add_argument(
        "--event",
        type=str,
        help='JSON string of event, e.g. \'{"name": "purchase", "params": {...}}\'',
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Path to JSON file containing events (array or single event)",
    )
    parser.add_argument(
        "--datalayer",
        type=str,
        help="JSON string of dataLayer push format",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args()

    events = []

    if args.event:
        events = [json.loads(args.event)]
    elif args.file:
        with open(args.file, "r") as f:
            data = json.load(f)
            events = data if isinstance(data, list) else [data]
    elif args.datalayer:
        dl = json.loads(args.datalayer)
        events = [{"name": dl.get("event", ""), "params": dl.get("ecommerce", dl)}]
    else:
        parser.print_help()
        sys.exit(1)

    results = [validate_event(e) for e in events]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            print_validation(result)


if __name__ == "__main__":
    main()
