# Email Compliance — Sub-Skill

## Overview

Email compliance isn't optional — violations can result in fines up to $50,120 per email (CAN-SPAM), 4% of annual revenue (GDPR), or $7,500 per violation (CCPA). This sub-skill audits compliance across CAN-SPAM, GDPR, CCPA, and general consent management best practices.

**Command:** `/email compliance`

---

## Compliance Audit Checklist

- [ ] Sender identification is clear (From name and address)
- [ ] Physical mailing address is included in every email
- [ ] Unsubscribe mechanism works and is honored within 10 days
- [ ] Subject lines are not deceptive or misleading
- [ ] Commercial intent is disclosed where required
- [ ] Consent records are stored with timestamp and source
- [ ] Double opt-in is implemented (required for GDPR)
- [ ] Privacy policy is accessible and up to date
- [ ] Data processing agreements are in place with ESP
- [ ] Suppression lists are maintained and synced across systems
- [ ] CCPA "Do Not Sell" requests are honored (if applicable)
- [ ] Right to deletion requests can be fulfilled

---

## 1. CAN-SPAM Act (United States)

The CAN-SPAM Act of 2003 applies to all commercial email messages sent to US recipients. It does NOT require opt-in — but it does require opt-out and identification.

### CAN-SPAM Requirements

| Requirement | What It Means | Penalty |
|-------------|-------------|---------|
| No false headers | From, To, Reply-To must be accurate | $50,120/email |
| No deceptive subjects | Subject line must relate to content | $50,120/email |
| Identify as an ad | Must disclose commercial nature | $50,120/email |
| Physical address | Valid postal address in every email | $50,120/email |
| Opt-out mechanism | Clear, conspicuous unsubscribe | $50,120/email |
| Honor opt-outs | Process within 10 business days | $50,120/email |
| Monitor third parties | You're responsible for affiliates | $50,120/email |

### CAN-SPAM Compliance Checklist

```
[ ] From name identifies sender clearly
[ ] Reply-to address is monitored and functional
[ ] Subject line accurately reflects content
[ ] Email identifies itself as an advertisement (if applicable)
[ ] Physical postal address is included
[ ] Unsubscribe link is present, visible, and functional
[ ] Unsubscribe is processed within 10 business days
[ ] No purchased list emails without proper disclosure
[ ] Opt-out mechanism doesn't require login or personal info
[ ] Unsubscribe link works for at least 30 days after send
```

### CAN-SPAM Exemptions
- **Transactional emails** are mostly exempt (order confirmations, shipping updates, account notifications) — but they still can't have false headers
- **Relationship emails** (existing customer, ongoing business) have fewer requirements but still need opt-out

---

## 2. GDPR (European Union / EEA / UK)

The General Data Protection Regulation is far stricter than CAN-SPAM. It requires explicit, informed, freely given consent BEFORE sending any marketing email.

### GDPR Email Requirements

| Requirement | Detail | Fine |
|-------------|--------|------|
| Lawful basis | Consent or legitimate interest | Up to 4% of annual global revenue or EUR 20M |
| Explicit consent | Must be freely given, specific, informed, unambiguous | Same |
| Proof of consent | Must store when, how, what they consented to | Same |
| Right to withdraw | Easy to unsubscribe, as easy as subscribing | Same |
| Right to access | Provide copy of their data within 30 days | Same |
| Right to deletion | Delete their data upon request | Same |
| Right to portability | Export their data in machine-readable format | Same |
| Data minimization | Only collect data you actually need | Same |
| Privacy by design | Build privacy into systems from the start | Same |
| DPA required | Data Processing Agreement with ESP and all processors | Same |

### GDPR Consent Requirements

**Valid consent must be:**
1. **Freely given** — no pre-checked boxes, no bundled consent, no "consent wall" blocking access
2. **Specific** — separate consent for each purpose (marketing, analytics, third-party sharing)
3. **Informed** — tell them exactly what you'll send, how often, and who processes the data
4. **Unambiguous** — requires clear affirmative action (checking a box, clicking a button)

### Consent Record Storage

For every subscriber, store:
```
{
  "email": "user@example.com",
  "consent_given": true,
  "consent_timestamp": "2026-03-13T14:30:00Z",
  "consent_source": "website_signup_form",
  "consent_version": "v2.1",
  "ip_address": "192.168.1.1",
  "form_url": "https://example.com/newsletter",
  "consent_text": "I agree to receive weekly marketing emails from [Brand]. Unsubscribe anytime.",
  "double_optin_confirmed": true,
  "double_optin_timestamp": "2026-03-13T14:35:00Z"
}
```

### Double Opt-In (Required for GDPR Best Practice)

```
Step 1: User submits email on form
Step 2: System sends confirmation email
Step 3: User clicks confirmation link
Step 4: Subscription is activated
Step 5: Welcome sequence begins
```

**Why double opt-in matters:**
- Proves consent was intentional (not a typo or bot)
- Reduces spam complaints by 75%+
- Improves list quality and engagement
- Required in some EU countries (Germany, Austria)
- Protects against abuse (someone entering another person's email)

---

## 3. CCPA / CPRA (California)

The California Consumer Privacy Act (CCPA) and its amendment (CPRA) give California residents rights over their personal data, including email addresses.

### CCPA Email Requirements

| Requirement | Detail |
|-------------|--------|
| Right to know | Disclose what personal data is collected and why |
| Right to delete | Delete personal data upon request |
| Right to opt-out | "Do Not Sell or Share My Personal Information" link |
| Right to non-discrimination | Can't penalize users who exercise their rights |
| Privacy notice | Must disclose data practices at or before collection |
| Data inventory | Know what data you have and where it's stored |

### CCPA Applicability

CCPA applies if your business:
- Has annual gross revenues over $25 million, OR
- Buys, sells, or shares personal data of 100,000+ consumers/households, OR
- Derives 50%+ of annual revenue from selling personal data

### CCPA Email Checklist
```
[ ] Privacy policy includes CCPA-required disclosures
[ ] "Do Not Sell My Personal Information" link in footer (if selling data)
[ ] Can fulfill deletion requests within 45 days
[ ] Can provide data access report within 45 days
[ ] Data inventory documented (what, where, who has access)
[ ] Opt-out honored for data sharing with third parties
[ ] No discriminatory practices against opt-out users
```

---

## 4. Other Regulations

### CASL (Canada)
- **Requirement:** Express consent before sending commercial emails
- **Implied consent:** Exists for 2 years after purchase, 6 months after inquiry
- **Fines:** Up to CAD $10M per violation (individuals: CAD $1M)
- **Unique:** Recipients can sue senders (private right of action)

### PECR (UK — Post-Brexit)
- **Requirement:** Consent for marketing emails
- **Soft opt-in:** Allowed for existing customers (similar products, opt-out provided)
- **Enforced by:** ICO (Information Commissioner's Office)

### Australia Spam Act
- **Requirement:** Consent (express or inferred)
- **Inferred consent:** From published email or existing business relationship
- **Fines:** Up to AUD $2.2M per day

---

## 5. Consent Management Best Practices

### Preference Center

Every email program should offer a preference center where subscribers can:
- Choose email frequency (daily, weekly, monthly)
- Select topics of interest
- Update their email address
- Unsubscribe from specific lists (not just all-or-nothing)
- Download their data (GDPR right to portability)
- Request deletion (GDPR right to erasure)

### Unsubscribe Best Practices

| Practice | Standard |
|----------|----------|
| One-click unsubscribe | Required (List-Unsubscribe header) |
| No login required | Unsubscribe must work without authentication |
| Confirmation page | Confirm the action, offer preference center |
| Processing time | Immediate (max 10 business days for CAN-SPAM) |
| No re-subscribe tricks | Don't add them back without new explicit consent |
| Suppression list | Maintain permanently, sync across all systems |

### List-Unsubscribe Header

Required by Gmail and Yahoo (as of February 2024):
```
List-Unsubscribe: <mailto:unsubscribe@example.com>, <https://example.com/unsubscribe?id=123>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
```

---

## Compliance Scoring

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Sender identification clear | 10% | 0 or 100 |
| Physical address in emails | 10% | 0 or 100 |
| Unsubscribe mechanism works | 15% | 0 or 100 |
| Consent records stored | 15% | 0 or 100 |
| Double opt-in implemented | 10% | 0 or 100 |
| GDPR requirements met (if applicable) | 15% | 0-100 |
| CCPA requirements met (if applicable) | 10% | 0-100 |
| Privacy policy up to date | 5% | 0 or 100 |
| Suppression lists maintained | 5% | 0 or 100 |
| List-Unsubscribe header present | 5% | 0 or 100 |
