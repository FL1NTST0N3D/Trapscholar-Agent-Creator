# Email Deliverability Audit — Sub-Skill

## Overview

Deliverability is the foundation of email marketing. If your emails don't reach the inbox, nothing else matters. This sub-skill audits email authentication, sender reputation, bounce management, and spam complaint handling.

**Command:** `/email deliverability`

---

## Authentication Chain Audit

### 1. SPF (Sender Policy Framework)

SPF tells receiving mail servers which IP addresses are authorized to send email on behalf of your domain.

**What to check:**
- Does the domain have an SPF record?
- Does it include the ESP's sending servers?
- Is it using `~all` (softfail) or `-all` (hardfail)?
- Are there more than 10 DNS lookups? (SPF has a 10-lookup limit)

**Example SPF record:**
```
v=spf1 include:_spf.google.com include:servers.mcsv.net include:sendgrid.net ~all
```

**Common issues:**
- No SPF record at all (critical)
- Too many `include:` statements exceeding the 10-lookup limit
- Using `+all` which allows anyone to send as your domain
- Multiple SPF records (only one is allowed per domain)

**Scoring:**
| Status | Score |
|--------|-------|
| Valid SPF with `-all` | 100 |
| Valid SPF with `~all` | 80 |
| Valid SPF with `?all` | 50 |
| SPF with >10 lookups | 30 |
| No SPF record | 0 |
| Multiple SPF records | 0 |

### 2. DKIM (DomainKeys Identified Mail)

DKIM adds a digital signature to outgoing emails, allowing the receiver to verify the email wasn't altered in transit.

**What to check:**
- Is DKIM configured for the sending domain?
- Is the key length 2048-bit? (1024-bit is outdated)
- Is the DKIM selector correct for the ESP?
- Does the signature align with the From domain?

**Example DKIM DNS record:**
```
selector._domainkey.yourdomain.com IN TXT "v=DKIM1; k=rsa; p=MIIBIjANBgkqh..."
```

**Common DKIM selectors by ESP:**
| ESP | Typical Selector |
|-----|-----------------|
| Mailchimp | `k1` |
| Klaviyo | `kl`, `kl2` |
| SendGrid | `s1`, `s2` |
| HubSpot | `hs1`, `hs2` |
| Postmark | `20XXXXXX` (date-based) |
| Amazon SES | Custom CNAME |

**Scoring:**
| Status | Score |
|--------|-------|
| Valid DKIM, 2048-bit, aligned | 100 |
| Valid DKIM, 1024-bit | 70 |
| DKIM present but not aligned | 40 |
| No DKIM | 0 |

### 3. DMARC (Domain-based Message Authentication, Reporting, and Conformance)

DMARC builds on SPF and DKIM. It tells receiving servers what to do when authentication fails and provides reporting.

**What to check:**
- Does the domain have a DMARC record?
- What is the policy? (`none`, `quarantine`, `reject`)
- Is there a `rua` tag for aggregate reports?
- Is there a `ruf` tag for forensic reports?
- What is the `pct` value?

**Example DMARC records (progression):**
```
# Stage 1: Monitor only
v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com;

# Stage 2: Quarantine 25%
v=DMARC1; p=quarantine; pct=25; rua=mailto:dmarc@yourdomain.com;

# Stage 3: Full enforcement
v=DMARC1; p=reject; rua=mailto:dmarc@yourdomain.com; ruf=mailto:dmarc-forensic@yourdomain.com;
```

**Scoring:**
| Status | Score |
|--------|-------|
| `p=reject` with reporting | 100 |
| `p=quarantine` with reporting | 80 |
| `p=none` with reporting | 50 |
| `p=none` without reporting | 30 |
| No DMARC record | 0 |

---

## Sender Reputation Scoring

### IP Reputation

Check the sending IP reputation using these services:
- **Google Postmaster Tools** — Shows domain/IP reputation for Gmail
- **Microsoft SNDS** — Sender reputation for Outlook/Hotmail
- **Sender Score (Validity)** — 0-100 reputation score
- **Talos Intelligence (Cisco)** — IP reputation lookup

### Domain Reputation

Domain reputation is increasingly more important than IP reputation. Check:
- Domain age (newer domains have lower trust)
- Sending history consistency
- Complaint rate history
- Volume patterns (sudden spikes are red flags)

---

## Blacklist Check

Check the sending IP and domain against major blacklists:

| Blacklist | Impact | Check URL |
|-----------|--------|-----------|
| Spamhaus ZEN | Critical | zen.spamhaus.org |
| Barracuda BRBL | High | b.barracudacentral.org |
| SpamCop | Medium | bl.spamcop.net |
| SORBS | Medium | dnsbl.sorbs.net |
| CBL | Medium | cbl.abuseat.org |
| UCEProtect | Low-Medium | dnsbl-1.uceprotect.net |

**If listed:** Identify the cause (spam complaints, compromised account, bad list), fix the issue, then request delisting.

---

## Bounce Rate Analysis

### Hard Bounces (Permanent)
- Invalid email address
- Domain doesn't exist
- Recipient server permanently rejected

**Target:** <0.5% hard bounce rate per send
**Action:** Remove immediately after first hard bounce. Never re-send.

### Soft Bounces (Temporary)
- Mailbox full
- Server temporarily unavailable
- Message too large
- Rate limiting

**Target:** <2% soft bounce rate per send
**Action:** Retry 2-3 times over 48 hours. Convert to hard bounce after 3 consecutive soft bounces.

### Bounce Rate Scoring
| Bounce Rate | Score | Action |
|-------------|-------|--------|
| <0.2% | 100 | Excellent list hygiene |
| 0.2-0.5% | 80 | Good, monitor |
| 0.5-1.0% | 60 | Clean list, check acquisition sources |
| 1.0-2.0% | 40 | Significant issue, audit list sources |
| 2.0-5.0% | 20 | Critical, likely purchased or old list |
| >5.0% | 0 | Emergency, stop sending, clean list |

---

## Spam Complaint Rate

**Industry target:** <0.1% (1 complaint per 1,000 emails)
**Gmail threshold:** 0.3% (above this, Gmail will block you)

### Spam Complaint Scoring
| Complaint Rate | Score | Status |
|----------------|-------|--------|
| <0.05% | 100 | Excellent |
| 0.05-0.1% | 80 | Good |
| 0.1-0.2% | 50 | Warning — take action |
| 0.2-0.3% | 20 | Critical — approaching Gmail threshold |
| >0.3% | 0 | Emergency — likely blocked by major ISPs |

---

## Deliverability Score Calculation

```
Deliverability Score =
  (SPF Score x 0.15) +
  (DKIM Score x 0.15) +
  (DMARC Score x 0.15) +
  (Reputation Score x 0.20) +
  (Blacklist Score x 0.10) +
  (Bounce Score x 0.15) +
  (Spam Complaint Score x 0.10)
```

---

## Action Items by Priority

### Critical (Fix immediately)
- No SPF/DKIM/DMARC records
- Listed on Spamhaus or Barracuda
- Spam complaint rate >0.3%
- Hard bounce rate >2%

### High (Fix within 1 week)
- DMARC set to `p=none` without monitoring
- 1024-bit DKIM key
- Soft bounce rate >2%
- No Google Postmaster Tools configured

### Medium (Fix within 1 month)
- DMARC not at `p=reject`
- No feedback loop registration
- SPF approaching 10-lookup limit
- No dedicated sending IP (for high-volume senders >100K/month)

### Low (Optimization)
- Custom return-path domain
- BIMI record setup
- ARC authentication chain
- MTA-STS policy
