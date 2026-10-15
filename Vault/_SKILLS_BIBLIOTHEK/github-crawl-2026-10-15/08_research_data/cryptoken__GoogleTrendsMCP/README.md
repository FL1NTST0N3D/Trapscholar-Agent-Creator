# Google Trends MCP Server

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server that gives AI assistants access to Google Trends data. Compare keywords, discover trending searches, explore related topics, and analyze regional interest — all through natural language.

## Tools

| Tool | Description |
|------|-------------|
| `compare_keywords` | Compare search interest for up to 5 keywords over time |
| `get_trending_searches` | Get today's real-time trending searches by country |
| `get_related_queries` | Find related search queries (top + rising) for a keyword |
| `get_related_topics` | Discover related topics and thematic connections |
| `get_interest_by_region` | See where a keyword is most popular geographically |

## Setup

### Prerequisites

- Python 3.10+

### Install

```bash
git clone https://github.com/cryptoken/GoogleTrendsMCP.git
cd GoogleTrendsMCP
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configure with Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "google-trends": {
      "command": "python",
      "args": ["path/to/GoogleTrendsMCP/server.py"]
    }
  }
}
```

## Example Prompts

- "Compare search interest for Python, JavaScript, and Rust over the past year"
- "What's trending in the US right now?"
- "What are people searching for related to 'machine learning'?"
- "Where in the world is 'soccer' most popular?"

## Rate Limits

Google Trends has unofficial rate limits. If you get 429 errors, wait 60 seconds before retrying.

## License

[MIT](LICENSE)
# GoogleTrendsMCP
