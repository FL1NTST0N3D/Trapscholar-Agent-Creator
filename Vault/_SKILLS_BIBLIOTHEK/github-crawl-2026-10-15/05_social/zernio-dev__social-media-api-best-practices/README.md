# Social Media API Best Practices

[![skills.sh](https://img.shields.io/badge/skills.sh-social--media--api-blue)](https://skills.sh)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Battle-tested patterns for integrating social media APIs, from scheduling 1M+ posts across **13 platforms**.

## Installation

```bash
npx skills add mikipalet/skills/social-media-api-best-practices
```

## All 13 Platforms Covered

| Platform | Auth | Unique Feature |
|----------|------|----------------|
| Instagram | OAuth 2-step | Error 2207051 edge case |
| TikTok | OAuth + UX compliance | Privacy/duet/stitch toggles |
| Twitter/X | PKCE required | 3-tier rate limits |
| LinkedIn | OAuth + API version | Text escaping rules |
| YouTube | Google OAuth | Resumable uploads |
| Facebook | Page tokens | Multi-image posts |
| Threads | OAuth 2-step | Aggressive rate limiting |
| Pinterest | Basic auth | Presigned S3 uploads |
| **Bluesky** | **AT Protocol** | DIDs, PDS, rich text facets |
| **Snapchat** | Basic (allowlist) | **AES-256-CBC encryption** |
| **Google Business** | Google OAuth | Location hierarchy, reviews |
| **Reddit** | OAuth | Strict user-agent, flair system |
| **Telegram** | Bot token only | HTML subset, no OAuth |

## What's Included

- **OAuth & Authentication** - All flows including AT Protocol for Bluesky
- **Rate Limiting** - Multi-tier handling, exponential backoff
- **Media Uploads** - Streaming, chunked uploads, format requirements
- **Error Handling** - Complete error code mappings for all platforms
- **Platform Quirks** - Large integer IDs, character counting, encryption
- **Code Snippets** - Copy-paste ready TypeScript examples

## Usage

Once installed, Claude Code will automatically apply these best practices when working on social media integrations:

```
/social-media-api-best-practices
```

## Example Prompts

- "Help me implement Twitter OAuth with PKCE"
- "Why is my Instagram post returning error 2207052?"
- "How do I post to Bluesky using AT Protocol?"
- "What's the rate limit for TikTok uploads?"
- "How do I encrypt media for Snapchat?"

## Key Insights

### Instagram 2207051 Edge Case
Instagram's anti-spam sometimes returns "blocked" but actually publishes the post. Always verify by checking recent media before treating as failure.

### Twitter's Three-Tier Rate Limits
Twitter has app-level, user-level, AND endpoint-specific limits. Check all three headers to avoid unexpected blocks.

### Bluesky AT Protocol
Bluesky doesn't use OAuth. It uses DIDs (Decentralized Identifiers) and PDS (Personal Data Servers). Rich text requires byte-offset facets.

### Snapchat Encryption
Snapchat requires AES-256-CBC encryption of media before upload. You must generate random key/IV and include them in the upload request.

### Reddit User-Agent
Reddit strictly enforces descriptive user agents. Generic agents like "axios/1.0" will be blocked.

## Contributing

Found a new platform quirk? PRs welcome!

## License

MIT

---

Maintained by [Zernio](https://zernio.com) - Social Media Scheduling API for Developers
