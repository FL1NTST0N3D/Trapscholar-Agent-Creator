---
name: email-marketing/channels
description: >
  Condensed guide to the messaging channel mix: email, SMS/RCS, conversational
  messaging (WhatsApp), mobile and browser push, in-app, website personalisation,
  wallet passes, point of sale, voice, and direct mail. Covers each channel's
  permission model, reach, constraints, cost profile, and measurement quirks.
  Reference this when choosing channels, comparing them, or advising on
  channel-specific mechanics.
---

# Channels

> Condensed offline fallback. The canonical, more complete versions live in the CRM Open Knowledge Wiki under `channels/` — prefer those when reachable.

## The Channel Mix

Channels differ on two axes: **how much of the delivery you control** and **whom they can reach**. In-app and direct mail land intact with no platform editing, but reach only the active user or a postal address. Email and push reach dormant users but are filtered and increasingly edited between you and the recipient. SMS sits in between: interruptive and largely unedited today, but expensive and low-tolerance.

The general rule: **reserve the interruptive, filtered channels (push, SMS) for what only they can do, and move everything else onto surfaces the recipient opened on purpose.** No single channel is the relationship; the relationship is the customer record and the addressability across all of them. Run channels as a portfolio under one contact strategy, not as rivals.

## Email

Covered in depth in the other local files — this is the short version for channel comparison.

- **Permission:** an address plus a consent record you hold and can take to another provider — unlike push tokens or messaging-app threads, which are platform-issued and cannot be taken elsewhere.
- **Reach:** governed by deliverability, not a per-device permission. The reachable audience is the engaged subset, not the list size.
- **Editing:** the most mediated channel. Providers classify into tabs, rank within them, and increasingly summarise for the recipient — and you see none of these decisions.
- **Cost:** effectively zero marginal cost per send; highest volume, deepest tooling.
- **Key technical constraints:** ~600px template width; Gmail clips above ~102KB (burying CTAs and tracking); send `multipart/alternative` with a plain-text part; bulk senders must support RFC 2369 `List-Unsubscribe` and RFC 8058 one-click unsubscribe; SPF, DKIM, and aligned DMARC are the price of entry.
- **Measurement quirk:** opens are corrupted by image prefetch and Mail Privacy Protection, and security scanners inflate clicks — both are directional only. Conversions, replies, and unsubscribes are the cleaner signals.
- **Best fit:** the default backbone for nurture, retention, and winback at scale. Rarely right for genuinely time-critical alerts — SMS or push lands faster and more intact.

## SMS and RCS

The most interruptive channel and, today, the one with the least editing between sender and recipient. Read almost immediately and almost always.

- **Permission:** explicit opt-in tied to a phone number, with a high legal bar — TCPA (US), PECR (UK). Log the affirmative act, the exact disclosure text, when, and the source; you cannot reconstruct the record later. STOP must unsubscribe immediately with one confirmation; HELP must return identity and contact — both carrier-enforced. Quiet hours: 8am–9pm recipient local time is the federal floor; state mini-TCPA laws (Florida, Oklahoma, Texas, Connecticut) impose tighter windows. Schedule against the recipient's zone, not the server's.
- **Encoding is a budget control, not a style preference.** One segment = 160 characters in GSM-7 or just 70 in UCS-2; multi-segment messages drop to 153/67 per segment, and you are billed per segment. One stray character — an emoji, a curly quote, an em dash, an accented letter, a non-breaking space pasted from a web page — flips the whole message to UCS-2 and halves the budget. A single smart quote turns a 158-character one-segment send into three segments. To stay in one segment:
  - Compose in a plain-text editor, never Word or a CMS that smartens punctuation.
  - Strip emoji from bulk marketing copy; if brand voice needs one, design deliberately to the 70-character UCS-2 budget.
  - Preview the actual encoding and live segment count in the ESP before send.
  - Count the tracked URL as part of the budget — a long tracked link alone can push a tight message over 160.
- **Links:** use branded, tracked short links on your own short domain, never generic public shorteners — those look illegitimate and are flagged by carrier filters that spam traffic has already burned. For RCS, prefer a suggested action over a raw URL, keeping the SMS fallback link intact.
- **US sending routes:** A2P 10DLC (cheapest, mandatory brand/campaign registration taking days to weeks, throughput scales with trust score), short codes (highest cost, slowest to provision, most reliable at scale), toll-free (the middle option). Pick by the binding constraint: cost-sensitive → 10DLC; high sustained volume → short code; need to launch before 10DLC vetting clears → toll-free.
- **Sender IDs:** alphanumeric sender IDs (common outside the US) are trivially spoofable and have no reply path. Registers are closing the gap — Australia's ACMA register becomes mandatory 1 July 2026, after which unregistered brand labels are replaced with "Unverified" and threaded alongside suspected scams. Treat sender ID registration as the SMS counterpart of email authentication.
- **RCS:** adds verified sender, branding, rich cards, suggested replies, and read receipts via Google Messages; on iPhone from iOS 18. Reach is uneven across device, carrier, and client — write the SMS fallback first as a complete, self-contained message, then enrich for RCS. Never put essential content only in a card or suggested reply.
- **Cost:** among the more expensive digital channels per message, well above email and push (though far below direct mail), and the lowest tolerance for volume — one unwanted text drives opt-outs fast.
- **Measurement quirk:** no opens exist. Delivery receipts (DLRs) are advisory — some carriers mark "delivered" on network handoff, not handset receipt. Read clicks and conversion against a randomised holdout; opt-out rate and per-message cost are the discipline metrics.
- **Best fit:** time-critical, high-value messages that must not be summarised or delayed — fraud alerts, delivery updates, 2FA, order confirmations, and a small number of genuinely urgent promotions. Do not spend it on routine marketing.

## Conversational Messaging (WhatsApp, Messenger, Instagram DM, Apple Messages)

CRM over the apps the customer uses with friends and family. Rich, two-way, opt-in only. WhatsApp is the default messaging channel across much of Europe, Latin America, Africa, and Asia — and marginal in North America, where SMS holds.

- **Permission:** the platform's opt-in bar is stricter than the law. WhatsApp requires recorded opt-in, naming your business, before any message. The thread lives in Meta's or Apple's graph — no portable list. The compensation is quality: an opted-in conversational contact is a high-intent grant, not a cold address.
- **The core mechanic:** when a user messages you, a 24-hour customer-service window opens for free-form messages. Outside it, only pre-approved templates — classified marketing, utility, or authentication. Since 1 July 2025 WhatsApp bills per delivered template, priced by category and recipient country. Utility templates sent inside an open window are free. Template category is both a compliance and a cost decision.
- **The editor is policy, not an algorithm:** each sending number carries a quality rating and sits in a messaging-limit tier; blocks and reports lower the rating and cap how many users you can reach. Irrelevance is punished structurally — relevance directly governs reach.
- **Rich payloads:** media, quick-reply and call-to-action buttons, list pickers, and location — well past SMS, so a message can carry an interaction rather than only text.
- **Versus SMS:** SMS is the lowest-common-denominator carrier channel — universal, no app needed, one-way, plain. Conversational messaging needs the app and the opt-in but returns a rich, two-way, identity-bearing thread, and in many markets lower cost at scale. Use SMS for universal urgent one-way reach; conversational for relationship-heavy two-way exchanges, especially where WhatsApp is the default app.
- **Constraints:** platform dependency is total — Meta and Apple set policy, pricing, and quality rules and can suspend a number with no appeal. Reach skews hard by market.
- **Measurement quirk:** delivered and read receipts are richer than email gives, but they measure the platform, not incremental behaviour — use a holdout. Watch quality rating, block rate, and report rate as guardrails; they cap future reach like a deliverability collapse.
- **Best fit:** two-way, high-intent moments — order and delivery updates, appointment reminders, auth codes, post-purchase support, conversational reactivation. Worst job: cold broadcast promotion, which wrecks the quality rating that makes the channel worth holding.

## Push (Mobile)

The one channel that can pull back a user who has not opened the app in weeks. Delivered via APNs (iOS) or FCM (Android).

- **Permission:** lives inside a specific install on a specific device, tied to a token the platform can invalidate. No portable list. Opt-in rates fell once Android made the permission an explicit runtime grant.
- **The OS prompt is effectively one-shot.** A denial is only reversible by the user digging into Settings. Never fire it cold on first launch: show your own in-app soft ask first, framed in the value the user came for ("get told the moment your size is back in stock"), and trigger the real dialog only after they accept. A decline on the soft ask costs nothing; a decline on the OS prompt is the grant gone.
- **Editing:** the most opaque channel. On-device models (Apple Intelligence, Gemini Nano) can summarise, reorder, and rewrite notifications before the lock screen; Focus can suppress them — with no API telling you which happened.
- **Technical constraints:** payload capped at ~4KB, so the proposition must lead. iOS interruption levels: passive for things that can wait, active (default) for ordinary timely messages, time-sensitive only for what the user genuinely needs now (never marketing), critical requires an Apple entitlement and is never available for marketing. Android requires every notification to route through a user-controllable channel — define a few meaningful categories (transactional, shipping, offers) so users can mute offers without losing shipping; mis-categorising an offer into a transactional channel gets the whole channel muted, and a channel's importance cannot be raised again in code once the user lowers it. Prune dead tokens (APNs `410 Unregistered`, FCM `UNREGISTERED`) — the push equivalent of suppressing a hard bounce.
- **Cost:** effectively free per send; the real budget is the interruption tolerance and the permission itself.
- **Measurement quirk:** treat the dashboard with doubt. Opens and clicks sit downstream of an editor you cannot see; confirmed delivery fires when the OS takes the payload, not when the user sees it. The only clean read is downstream conversion (app return, purchase) against a randomised holdout — both arms sit behind the same suppression.
- **Best fit:** waking dormant users — the job only push owns — and messages tied to the recipient's own activity: a price alert they set, a delivery status, a reply waiting. Broadcast promotion competes worst for the interruption budget.
- **Re-engaging dormant users, done in steps:**
  - Segment by dormancy depth — a user three days quiet and one ninety days gone need different messages, and the ninety-day user may have churned for good.
  - Give a concrete reason to return tied to what changed since they left (a price drop on something they viewed, a reply waiting) — not a generic "we miss you" that the editor and the user both discount.
  - Send in the recipient's local daytime and hold frequency down — the re-engagement push that annoys is the last one before the opt-out.
  - Cap attempts: if a dormancy segment does not respond to a small sequence, stop pushing and fall back to email, which has no per-device permission to lose.
  - When unsure, ask whether the message needs the user back right now. If not, it is not a push.

## Browser Push

Web push via a service worker on your origin: the way back for a web product with no app, and the only CRM channel that reaches the desktop. Works in Chrome, Firefox, Edge, Safari on macOS, and on iOS 16.4+ only for web apps added to the Home Screen.

- **Permission:** bound to one browser on one device for your origin. The same person is several separate subscriptions and several separate asks. No list — only per-browser grants.
- **The one-shot trap is sharper here.** A browser block is sticky, origin-wide, and almost never reversed. Browsers actively punish cold prompting: Chrome routes low-accept-rate sites into a quieter UI that suppresses the dialog for everyone; Safari refuses prompts that don't come from a user gesture. Same fix: an in-page soft ask tied to a value moment and an explicit click, then the native prompt.
- **Technical:** service worker + `PushSubscription` endpoint + VAPID keys (RFC 8292); payloads encrypted (RFC 8291) and capped at ~4KB, so the proposition leads here too. Each browser uses its own push service (Chrome/Edge via FCM, Firefox via autopush, Safari via APNs), abstracted by the protocol. Requires HTTPS; without a registered service worker there is no web push.
- **iOS caveat:** on iPhone and iPad, web push reaches only a web app added to the Home Screen — not a page in a Safari tab — and the permission prompt must follow a direct user interaction. This caps iOS reach sharply.
- **Constraint to design for:** the subscription has no identity of its own — tie it to a logged-in user at grant time or you hold an anonymous endpoint you cannot reconcile with the customer record.
- **Measurement quirk:** same as mobile push — suppression is invisible, so measure downstream action against a holdout of the granted audience, not clicks.
- **Best fit:** desktop and no-app re-engagement — back-in-stock and price-drop alerts the user asked for, desktop cart recovery. Treat mobile and browser push as separate grants under one contact strategy, not a single "push" channel.

## In-App

Everything you can show inside your own product: modals, slide-ups, embedded cards, a message centre. The only channel with **no platform editor and no permission gate** in the delivery path.

- **Permission:** none needed — the user is already inside a product they chose to open. The hard limit is the mirror image of push: in-app reaches only the active user. A user dormant for a fortnight cannot be reached this way at all.
- **Format is the main control, and it is an interruption ladder:** modal (highest attention, stops the session — reserve for the single highest-value blocking moment), slide-up/banner (timely but not blocking), embedded card/feed (ambient, persistent), message centre (durable, on-demand). When in doubt, drop one rung down; the cheaper format usually does the job without spending goodwill.
- **Frequency discipline:** cap interruptive formats to one per session and at most one modal per user per day, enforced centrally with a priority order so two eligible campaigns never stack. Never fire an interruption mid-checkout or on top of an active task. Over-using modals degrades the product itself — a steeper cost than an ignored email, because it sits on the surface the relationship is built on.
- **Sync lag:** messages are cached at session start and triggers evaluate on-device, so eligibility is only as fresh as the last sync — a server-side edit does not reach a device until it next syncs. Plan trigger timing and end dates around this.
- **Trigger conditions in practice:** tie the message to a context window so it lands when useful and not before. Show a "finish setup" card when the user reaches the screen the unfinished step belongs to and it is still incomplete — not on every launch. Surface a feature tip the first time the user opens the area it applies to, capped to once. Fire an upsell slide-up after the user repeats the action the paid tier would improve, not on session one.
- **Cost:** no per-message cost; the budget is session quality.
- **Measurement quirk — the good kind:** the cleanest measurement of any channel. The SDK records every render, dismiss, and interaction with no mediated gap, so holdout-based incrementality is easiest to run honestly here. But watch guardrails (session abandonment, task completion, dismiss rate) — a modal can lift its own click rate while pushing everyone else out of the flow.
- **Best fit:** onboarding, activation, feature education, contextual prompts, upsell, surveys — the in-session work. It is the destination the other channels drive toward, not a way to initiate contact.

## Website Personalisation

Your own site as a delivery surface: hero swaps, recommendations, overlays, reranked listings. The web counterpart of in-app, with one difference that governs everything: **most traffic is anonymous.**

- **Reach:** the live visitor only; it cannot initiate contact. Until identity resolves (sign-in, a click-through from an addressed email/SMS carrying an identifier, or a profile match), personalisation runs on session signals — referrer, geo, campaign, pages viewed — not the customer record. Turning the anonymous visit into a known one is one of the channel's primary jobs, not a precondition.
- **Consent gates tracking:** a visitor who declines cookie consent cannot be profiled and falls into the anonymous tail by law, not just by being new.
- **The engineering trade is flicker:** client-side rewriting is fast to deploy but the default page paints first and visibly snaps to the variant. Anti-flicker snippets trade the flash for a page-load delay on the critical path; server-side rendering avoids both but costs engineering. Neither option is free.
- **Cost:** tooling (Adobe Target, Optimizely, Dynamic Yield, VWO) plus the page-speed tax.
- **Measurement quirk:** the cleanest experimental surface alongside in-app — but watch bounce rate, page-load time, and overall conversion, because a heavy anti-flicker snippet can cost more conversions than the personalised module wins.
- **Best fit:** converting anonymous traffic into consented contacts (feeds list building), in-session merchandising and recommendations, landing-page continuity with the campaign that drove the click, and onsite experimentation. Generative per-visitor pages remain experimental — latency, brand safety, and the collapse of clean A/B measurement hold them back.

## Wallet Passes

A loyalty card, coupon, ticket, or membership in Apple Wallet or Google Wallet. **Presence without a send:** a persistent object on the device that you update remotely and that surfaces itself on the lock screen by time or geofence.

- **Permission:** the add-to-wallet action is the opt-in. Updating a held pass needs no fresh consent and has no per-message cost — the channel's structural advantage over send-based channels. No portable list; reach is only ever the set of users who added the pass.
- **Editing:** minimal — the pass renders as you define it; updates land directly. The only gate is whether the user kept the pass's notifications on.
- **Technical:** Apple uses PassKit — a signed `.pkpass` bundle defining fields, barcode, and appearance, updated via a push that tells the device to pull the new pass; Google Wallet uses a class and object updated through its REST API, synced to the device. A pass can declare lock-screen relevance by geofence (around a store or venue) and by time, so it appears when the user is nearby or the event approaches, with no campaign send at all. The barcode ties in-store scans back to the customer record, closing the digital-to-physical loop.
- **Versus push and email:** the pass is the persistent owned object; push and email are the sends that drive adoption of it and re-engage around it. They are complementary, not competing.
- **Constraints:** adoption is the limiter — the reach ceiling is your distribution funnel, and two platforms mean two implementations. It is an updatable object and a location trigger, not a conversation: news and persuasion belong on the send channels.
- **Measurement quirk:** scans and redemptions are first-party and clean, but a redemption count is not incremental effect — a pass that would have been redeemed anyway is not the channel's doing. Hold out a slice of the programme; watch add rate and on-device retention as health metrics.
- **Best fit:** anything with a card, a balance, or a redeemable token. Email the offer, drop it in the wallet, let lock-screen relevance finish the job near the store.

## Point of Sale

The checkout as a CRM surface: an offer on the terminal, a coupon on the receipt, loyalty enrolment at the lane, a next-best-action for the associate. Intent is already proven by the transaction in front of you.

- **Reach:** whoever is physically at the till. No standing list, no absent customers. The gate is identity: a cash transaction with no loyalty lookup is anonymous, and everything personalised depends on the customer presenting a loyalty ID, phone number, card token, or app/wallet barcode in the seconds the sale takes.
- **Consent:** the transaction itself sits under a lighter regime, but an email or mobile number captured at the till falls under the same consent rules as every other channel. An opt-in taken at the lane is a real opt-in and must be recorded as one.
- **The editor is a person:** the cashier decides whether to mention the offer or pitch the signup at all — discretionary, inconsistent, dependent on training and incentives. The rest of the surface is a few lines of receipt or terminal shared with the total and the return policy.
- **Constraints:** POS estates are frequently legacy, on-premise, and fragmented; the vendor API is often the slowest, most constrained integration in the stack. What you can deliver is bounded by the terminal software, not by what the CRM can decide.
- **Measurement quirk:** redemptions are first-party and clean, but read incrementality against a lane-treatment holdout; watch enrolment rate and identity-capture rate as health metrics.
- **Best fit:** converting the anonymous shopper into an addressable, consented customer at the moment of first purchase, loyalty enrolment while the value is concrete, and closing offers issued on other channels. It is a capture-and-close surface, not a place to hold a relationship between visits.

## Voice

The phone call — live agent, IVR, or AI voice agent. The richest, most persuasive channel; the only one that resolves a complex issue or closes a sale in one synchronous exchange. Also the highest cost per touch when human-staffed, and the most legally exposed channel in the mix.

- **Permission:** the strictest regime of any channel. Under the TCPA, a marketing call using an artificial or prerecorded voice or an autodialler needs **prior express written consent**, plus DNC scrubbing, caller identification, immediate opt-out, and calling-hour restrictions.
- **AI voice agents are not a loophole.** The FCC ruled in February 2024 that an AI-generated voice is an "artificial or prerecorded voice" under the TCPA — an AI agent calling cold is an illegal robocall. Legitimate uses are inbound and consented outbound, with disclosure that the call is automated. AI removes the human-agent cost cap, which is precisely why the consent discipline matters more, not less.
- **Filtering:** STIR/SHAKEN signs the calling number; a number drawing complaints gets a "spam likely" label and stops being answered — the voice analogue of a sender-reputation collapse. Answer rate decides everything else.
- **Cost:** scales with cost when human-staffed and with regulatory risk when automated — there is no free volume lever.
- **Measurement quirk:** measure renewal, payment, or retention against a consented holdout — not connects. Watch answer rate, complaint rate, and spam labelling as guardrails.
- **Best fit:** high-value winback, premium renewals and onboarding, inbound sales and support, collections. Anything that can be a message should be one; the call is for what a message cannot resolve.

## Direct Mail

A physical piece to a postal address. The message arrives whole — no model in the delivery path summarises, ranks, or suppresses it. The trade: the slowest channel, and expensive per piece by a wide margin over any digital send.

- **Permission:** a lighter consent regime than electronic channels in most jurisdictions, though data protection law still governs how the address was obtained. The address is a staler data point than an email or phone number and decays continuously as people move.
- **Cost ladder:** postcard → letter → dimensional package, climbing steeply; lead times run to weeks. In the US, bulk promotional mail (USPS Marketing Mail) requires a 200-piece or 50-pound minimum — no economical single-piece send. Match the unit cost to the value at stake in the segment: postcards for mid-value reactivation volume, letters where an envelope raises perceived value, dimensional packages only where the LTV of the account dwarfs the piece cost. Never send the dimensional package to a list the postcard would have served.
- **Make every piece trackable:** mint a **unique** per-recipient code, QR, or PURL and stamp it on the CRM record before the file goes to print. Shared codes tell you the drop worked; unique codes tell you which recipient acted, which is what match-back needs.
- **Address hygiene before print, always:** validate and standardise (CASS in the US), apply move data, dedup to one piece per household, and budget for decay — undeliverables on this channel are a postal-returns cost paid after print, not a free bounce.
- **Production-readiness checklist** (there is no post-print fix; frame the timeline in weeks):
  - Artwork final and proofed, with variable-data fields and the per-recipient code, QR, or PURL placed and tested on the layout.
  - Data file pulled, variable fields populated, deduped to one piece per household.
  - Address validation run: standardised, move-updated, undeliverables removed, decay budgeted.
  - Control group split out and recorded, unique codes minted and written back to the CRM.
  - Physical proof sent and internal addresses seeded in the live drop to confirm print, finishing, and the scan-to-landing-page path end to end.
  - Postal class chosen and checked against its rules (USPS Marketing Mail: the 200-piece or 50-pound minimum).
- **Variable-data printing** personalises copy, imagery, and offers per recipient from the customer record — the physical analogue of merge tags. Drive it from the same fields the digital programme uses so the piece is as relevant as the other channels, not a generic mailshot.
- **Measurement:** no opens or clicks exist, so the channel is one of the more honestly measured — incrementality is built into how it has always been run. Randomise a holdout before the drop, mail the treated group with unique codes, match responders back over a window long enough for the slow physical response, and read treated-vs-control lift, not gross response. Match-back alone counts responses; the holdout turns the count into causal lift. Run both.
- **Best fit:** high-value retention and reactivation — top-tier recognition, lapsed high-value winback, milestone gestures, premium acquisition into a saturated inbox. A scalpel, not a broadcast tool.

## Choosing Between Channels

| Job | Channel |
| --- | --- |
| Rich or non-urgent content, nurture at scale | Email |
| Time-critical, must land intact (fraud, delivery, 2FA) | SMS |
| Two-way, high-intent threads; WhatsApp-first markets | Conversational messaging |
| Waking a dormant app user | Push (the only channel that can) |
| Desktop or no-app re-engagement | Browser push |
| In-session onboarding, education, upsell | In-app |
| Converting anonymous web traffic; in-session merchandising | Website personalisation |
| Keeping a balance, coupon, or ticket live on the device | Wallet pass |
| Capturing identity at the till; closing offers in person | Point of sale |
| The few moments genuinely worth a conversation | Voice |
| High-value winback and recognition that earns the spend | Direct mail |

Default heuristic for the interruptive channels: if the user is in session, keep it in-app or onsite; if they are gone and the message justifies breaking into their day, push or SMS; if it is neither urgent nor worth an interruption, email it. Let orchestration and a single contact strategy decide which channel sends which message — and measure every mediated channel against a randomised holdout, because on most of them the dashboard measures the platform, not your incremental effect.
