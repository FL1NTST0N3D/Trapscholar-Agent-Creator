# TomeScout — KDP listing tools for Claude

TomeScout gives Claude (and any MCP client) KDP listing tools for self-published authors:

| Tool | What it does |
| --- | --- |
| `keyword_boxes` | Packs your keyword phrases into KDP's seven 50-character boxes, drops words the title already covers and leaves out other authors' names, trademarks and Amazon programme names. |
| `check_listing` | Title, subtitle, description, keywords and categories against KDP's published guidelines, with the KDP help page for each issue. |
| `royalty_calculator` | eBook 70%/35% in 13 Amazon stores (2026 price bands, delivery cost, VAT), paperback printing cost and royalty, Kindle Unlimited earnings. |
| `bsr_to_sales` | Best Sellers Rank → a range of daily and monthly sales from two public models. |

Results render as interactive tables and cards (MCP Apps) in Claude and ChatGPT.

This plugin adds the TomeScout connector plus two skills: `kdp-listing-prep` and `kdp-niche-sizing-by-rank`.
Amazon Ads for authors is in development.

## Install

**Claude Code**

```
/plugin marketplace add semrebayrak/tomescout-claude-plugin
/plugin install tomescout@tomescout
```

**Claude (web, desktop, mobile)** — open [TomeScout in Claude's connector directory](https://claude.ai/directory/tomescout) and select *Connect to Claude*, or Settings → Connectors → Add custom connector → `https://tomescout.com/mcp`. No sign-in needed.

**Any MCP client** — remote Streamable HTTP server at `https://tomescout.com/mcp`.

Docs: https://tomescout.com/docs

### TomeScout Toolkit (second plugin in this marketplace)

[`toolkit/`](toolkit) holds `tomescout-toolkit`, the version submitted to Claude's plugin directory. It connects to
`https://tomescout.com/mcp/toolkit`, which serves the same four tools. Install it with
`/plugin install tomescout-toolkit@tomescout`.

## What the connector can see

TomeScout only receives the arguments Claude sends to its tools (candidate keywords, the metadata you ask it to check,
a price or a Best Sellers Rank). It does not read your conversation, files or memory, and it has no accounts. Nothing
is sent to Amazon or any other third party: every tool calculates from its arguments, KDP's published guidelines and
KDP's price tables. Privacy policy: https://tomescout.com/privacy

## Honest data

- Sales-from-rank and royalty figures are estimates from public models and KDP's pricing pages, shown as ranges.
- Famous titles made of ordinary words are only caught if they are on our list; review before publishing.

TomeScout is made by BlazeApps LLC. Amazon, Kindle and KDP are trademarks of Amazon.com, Inc. or its affiliates.
TomeScout is independent and not affiliated with Amazon.

## License

MIT — see [LICENSE](LICENSE). Security issues: see [SECURITY.md](SECURITY.md).
