# AfterShip Tracking & Returns MCP Server

Real-time package tracking and returns demo for any AI assistant — powered by [AfterShip](https://www.aftership.com).

**No authentication required.** Connect instantly using the remote endpoint:

```
https://mcp.aftership.com/tracking/public
```

> Supports [Streamable HTTP](https://modelcontextprotocol.io/docs/concepts/transports) transport (MCP spec 2025-03-26).

---

## Tools

### `track_shipment` — Real-time package tracking

Tracks any shipment in real time across 1,200+ carriers worldwide. **No carrier knowledge needed** — just paste a tracking number and carrier is detected automatically.


| Parameter         | Type   | Required | Description                                                                         |
| ----------------- | ------ | -------- | ----------------------------------------------------------------------------------- |
| `tracking_number` | string | ✅        | The tracking number from your shipping confirmation                                 |
| `carrier_slug`    | string | —        | Carrier name or slug (e.g. `UPS`, `FedEx`, `royal-mail`). Auto-detected if omitted. |


**When to use:**
Ask your AI assistant anything like:

- *"Where is my package? Tracking number: 1Z999AA10123456784"*
- *"Track 9400111899223397623910"*
- *"Why is my DHL shipment delayed? JD0123456789"*
- *"Is my order out for delivery yet?"*
- *"My package says it's stuck in customs — what's the status?"*
- *"When will 773738233 arrive?"*

The AI will call this tool automatically whenever a tracking number is mentioned or delivery status is asked about.

---

### `get_returns_demo` — AfterShip Returns Center preview

Generates a live, interactive demo of [AfterShip Returns Center](https://www.aftership.com/returns) for any merchant store. For store owners and e-commerce teams evaluating the product.


| Parameter   | Type   | Required | Description                                                  |
| ----------- | ------ | -------- | ------------------------------------------------------------ |
| `store_url` | string | ✅        | Your store domain (e.g. `nike.com`, `example.myshopify.com`) |


**When to use:**
Ask your AI assistant things like:

- *"Show me what AfterShip returns would look like for my store: mystore.myshopify.com"*
- *"Generate a returns demo for nike.com"*
- *"I want to preview AfterShip Returns Center for my Shopify shop"*
- *"What does the AfterShip returns experience look like for customers on my site?"*

> Note: This tool is for **merchants evaluating AfterShip Returns**, not for consumers who want to return an item they purchased.

---

## Installation

### Claude Code (CLI)

```bash
claude mcp add --transport http aftership https://mcp.aftership.com/tracking/public
```

Verify:

```bash
claude mcp list
```

### Codex

Add to `~/.codex/config.toml`:

```toml
[mcp_servers.aftership]
url = "https://mcp.aftership.com/tracking/public"
```

### Cursor

Add to **Settings → Cursor Settings → MCP → Add new global MCP server**, or create `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "aftership": {
      "url": "https://mcp.aftership.com/tracking/public"
    }
  }
}
```

### Windsurf

Edit `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "aftership": {
      "url": "https://mcp.aftership.com/tracking/public"
    }
  }
}
```

### VS Code (GitHub Copilot)

Create `.vscode/mcp.json` in your workspace:

```json
{
  "servers": {
    "aftership": {
      "url": "https://mcp.aftership.com/tracking/public"
    }
  }
}
```

---

## Data Privacy & Security

AfterShip is committed to handling shipment data responsibly:

- **No sensitive personal data returned.** Tracking responses include shipment status, carrier events, and estimated delivery dates. No personally identifiable information (PII) — such as recipient names, addresses, phone numbers, or payment details — is exposed through this API.
- **Read-only.** This MCP server only retrieves tracking information. It cannot create, modify, or delete any data.
- **Compliant by design.** AfterShip's infrastructure follows industry-standard security and compliance practices. For details, see [AfterShip's Security & Privacy policies](https://www.aftership.com/legal/privacy).

---

## Fair Use Policy

This MCP server is provided free of charge for personal and non-commercial use. To ensure reliable service for all users, AfterShip applies rate limits to this endpoint.

**What this means in practice:**

- Reasonable, interactive use (individuals querying package status in an AI assistant) is fully supported.
- Automated scripts, bulk lookups, or integrations that generate high request volumes are **not permitted** under the free tier.
- AfterShip reserves the right to throttle, suspend, or terminate access for usage that is abusive, excessive, or inconsistent with the intended purpose of this service.

For high-volume or commercial use cases, please contact us at [AfterShip](https://www.aftership.com) to discuss API access options.

---

## About

Built on the [Model Context Protocol](https://modelcontextprotocol.io) open standard. Powered by [AfterShip](https://www.aftership.com) — tracking data from 1,300+ carriers worldwide.

- [AfterShip Tracking](https://www.aftership.com/track)
- [AfterShip Returns Center](https://www.aftership.com/returns)
