# Shopify Scout — Shopify Store Scraper & Product Catalog Extractor

**Free, open-source Shopify scraper**: scan ANY Shopify store's full product catalog in seconds — prices, variants, compare-at (sale) signals, and a clean report. Powered by the public `products.json` endpoint. No API key. No captcha. No subscription.

Built for **e-commerce product research, competitor price monitoring, and dropshipping research**. Python 3.9+.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Shopify](https://img.shields.io/badge/Scraper-Any%20Shopify%20store-green.svg)]()

---

## What is this?

A **Shopify web scraper** that extracts complete product data (titles, prices, variants, compare-at values, tags, images) from any Shopify store. It uses the storefront's **public `/products.json` endpoint** — the same one the store itself uses to render — so there's **no API key, no login, no captcha** to fight.

Most "product research tools" charge $50+/month for repackaging this public data. This **Shopify data scraper** does it locally, for free, in seconds — and pairs perfectly with **price monitoring, dropshipping research, and competitor analysis** workflows.

## Demo

```
$ python shopify_scout.py allbirds.com

== Shopify Scout: scanning allbirds.com ==
  Page 1: +250 products (total 250)
  Page 2: +41 products (total 291)

# 选品调研报告：allbirds.com
- 商品总数：2829（含变体）
- 价格区间：$50.00 - $160.00
- 中位价：$99.00
- 平均价：$96.26
```

*Sample report: [`sample/report-allbirds.md`](sample/report-allbirds.md) (real data)*

## Features

| Feature | Description |
|---|---|
| 🛰️ **Full catalog scan** | Automatic pagination — handles stores with 10,000+ products (tested on gymshark.com: 9,466 products / 57,532 SKUs) |
| 📊 **Price intelligence** | Price range, median, average — automatic |
| 🏷️ **Compare-at sale signals** | `compare_at > price` = product is actively on sale = "this seller is pushing a winner" |
| 🔍 **Keyword filter** | `--keywords shoes,leather` (matches title/type/tags) |
| 💰 **Price filter** | `--min-price 50 --max-price 150` |
| 📄 **Clean report** | Markdown report with product table + stats + sale flags |
| 🤖 **Agent-friendly** | One-command CLI — works great as a Claude Code / Codex skill |

## Install

```bash
pip install requests
```

## Usage

```bash
# Basic scan
python shopify_scout.py allbirds.com

# Keyword + price filters
python shopify_scout.py allbirds.com --keywords shoes --min-price 50 --sort price-desc

# Save report to file
python shopify_scout.py gymshark.com --max-price 60 --out report.md

# Behind a proxy (e.g. China network)
python shopify_scout.py allbirds.com --proxy http://127.0.0.1:7897
```

### Options

| Flag | Description |
|---|---|
| `--keywords` | Comma-separated keyword filter (title/type/tags) |
| `--min-price` / `--max-price` | Price range filter |
| `--sort` | `title` (default) / `price` / `price-desc` |
| `--out` | Save report to file |
| `--proxy` | HTTP proxy |

## Real-world use cases

- **Dropshippers**: scan competitor stores → find price gaps + what they're actively pushing
- **FBA sellers**: full catalog audits of competitors
- **Store owners**: competitor pricing research
- **Data analysts**: e-commerce market research, price trend tracking

## Related searches

`shopify scraper` · `shopify products.json` · `shopify data extraction` · `shopify price monitor` · `ecommerce scraping` · `web scraping python` · `dropshipping research tool`

## ⭐ Support the project

If Shopify Scout saves you time:

- **Star this repo** — it helps others find it
- Report bugs / request features via Issues

## 🚀 Pro version

Need **automatic price monitoring**? The Pro version adds:

- 📈 **Daily competitor snapshots** — price changes detected within 24h
- 🔔 **Change reports** — price up/down, new SKUs, restocks
- 🗓️ **Scheduling** — runs on your schedule (Task Scheduler / cron)
- 🎥 **Video tutorial** + priority support

→ [Get Shopify Scout Pro](https://www.fiverr.com/zhaoheng588/scrape-data-from-login-protected-websites-with-browser-automation)

*Pro is a one-time purchase — no subscription. Also available as a custom scraping service on [Fiverr](https://www.fiverr.com/zhaoheng588/scrape-data-from-login-protected-websites-with-browser-automation).*

## License

[MIT](LICENSE) — free to use, modify, and distribute (keep the copyright notice).

*Data is fetched from public endpoints that store owners control and may disable at any time. Use for research purposes and respect store terms.*
