# Product Matrix — Printify blueprints, providers, variants, pricing

Shop: **Conundrum by Este**, sales channel **Etsy**. (The shop id resolves at runtime via
`pod_secrets.SHOP_ID`; the literal value is local operational data, never in these docs.)

| Product | Blueprint | Provider | Key variants | Scale notes |
|---|---|---|---|---|
| T-Shirt (Gildan) | 6 | 3 (also 99 in create_product) | 12126-12128 (S-2XL) | scale=1 |
| Trucker Hat | 1128 | 41 | 84650, 104276 | scale=1, wide format |
| Phone Case | 421 | 23 | 102547+ (iPhone 15/16) | scale=1 |
| Drawstring Bag | 414 | 10 | 61365 | scale=2.5 full coverage |
| AOP Tote | 1389 | 10 | 103599-103601 | scale=2.5 |
| Fanny Pack | 468 | 10 | 65045 | scale=2.5 |
| AOP Hoodie | 450 | 10 | 63241-63245 | ALL positions need images |
| AOP Joggers | 591 | 83 | 72926-72931 | 4 positions |
| Laptop Sleeve | 429 | 1 | 62038-62039 | scale=1 |
| Crew Socks | 1433 | 92 | 104469 | 4 positions |
| AirPods Case | 1505 | 23 | 108256+ | 3 positions (front/back/all) |
| Puzzle | 532 | 59 | 72543 (500pc) | scale=1 |
| Coaster | 1523 | 23 | 109346-109347 | scale=1.5 |
| Tumbler | 1507 | 217 | 108286, 108284 | 2 positions |
| Desk Mat | 488 | 1 | 65241, 72580 | scale=1 |
| Blanket | 522 | 47 | 68322-68324 | scale=1 |
| Hoodie (non-AOP) | 77 | 99 | — | from create_product.py |
| Mug | 635 | 28 | — | from create_product.py |

## Pricing (current)
- T-shirts: $24.99 (2XL: $26.99)
- Hats: $29.99
- Phone cases: $22.99
- Bags: $24.99
- Puzzles: $34.99
- Coasters: $14.99
- Mugs: ~$19.99 (create_product default 1999¢)
- Hoodies: ~$39.99 (create_product default 3999¢)

## Rate limits (don't get throttled)
- Upload: 3-5s delay between images.
- Publish: 5-10s delay; batch by product type.
- Use curl for uploads (urllib/requests get Cloudflare-blocked on upload endpoint).

## Remy's drop-math defaults
- A "drop" = one concept x 3-10 SKUs minimum. Never ship a single SKU.
- Hero product per concept is usually the tee or mug (best Etsy search volume).
- Reuse one base artwork across products before generating new art — cheapest way to add SKUs.
