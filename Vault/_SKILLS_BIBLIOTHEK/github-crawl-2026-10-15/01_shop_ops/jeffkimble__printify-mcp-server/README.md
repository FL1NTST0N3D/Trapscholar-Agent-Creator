# Printify MCP Server

A Model Context Protocol (MCP) server that exposes the Printify API, enabling AI agents like Manus to interact with Printify's print-on-demand services programmatically.

## Overview

This MCP server provides a bridge between AI agents and the Printify API, allowing automated management of:

- **Shops**: View connected shops
- **Catalog**: Browse product blueprints, print providers, and variants
- **Products**: Create, retrieve, and publish products
- **Orders**: Submit and manage orders
- **Uploads**: Upload design images

## Features

- ✅ Full Printify API v1 integration
- ✅ Secure authentication with API tokens
- ✅ Comprehensive error handling
- ✅ TypeScript implementation
- ✅ Compatible with MCP SDK 0.5.0+
- ✅ Easy deployment to cloud platforms

## Prerequisites

- Node.js 18+ or Node.js 20+
- A Printify account with API access
- Printify API token

## Installation

### 1. Clone or Download

```bash
git clone <your-repo-url>
cd printify-mcp-server
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your Printify API token:

```
PRINTIFY_API_TOKEN=your_actual_token_here
```

**How to get your Printify API token:**
1. Log in to your Printify account
2. Navigate to **My Profile** → **Connections**
3. Generate a new Personal Access Token
4. Copy the token (it will only be shown once)

### 4. Build the Project

```bash
npm run build
```

## Usage

### Running Locally

For development:

```bash
npm run dev
```

For production:

```bash
npm start
```

### Connecting to Manus

To use this MCP server with Manus, you need to configure it in your MCP settings. The server communicates via stdio (standard input/output).

**Example MCP configuration:**

```json
{
  "mcpServers": {
    "printify": {
      "command": "node",
      "args": ["/path/to/printify-mcp-server/dist/index.js"],
      "env": {
        "PRINTIFY_API_TOKEN": "your_token_here"
      }
    }
  }
}
```

## Available Tools

The MCP server exposes the following tools that AI agents can use:

### Shops

- **`get_shops`**: Retrieve all shops connected to the account

### Catalog

- **`get_blueprints`**: List all available product blueprints (t-shirts, mugs, etc.)
- **`get_blueprint`**: Get details of a specific blueprint
- **`get_print_providers`**: List all print providers
- **`get_blueprint_print_providers`**: Get print providers for a specific blueprint
- **`get_blueprint_variants`**: Get variants (sizes, colors) for a blueprint from a print provider

### Uploads

- **`upload_image`**: Upload a design image from URL or base64

### Products

- **`get_products`**: List all products in a shop
- **`get_product`**: Get details of a specific product
- **`create_product`**: Create a new product with designs and variants
- **`publish_product`**: Publish a product to a sales channel (Etsy, Shopify, etc.)

### Orders

- **`get_orders`**: List orders with optional filters
- **`create_order`**: Submit a new order

## Example Workflows

### 1. Create and Publish a T-Shirt

```
User: "Create a t-shirt with my logo and list it on Etsy"

Agent workflow:
1. get_shops → Get shop_id
2. upload_image → Upload the logo design
3. get_blueprints → Find t-shirt blueprint_id
4. get_blueprint_print_providers → Choose a print provider
5. get_blueprint_variants → Select sizes and colors
6. create_product → Create the product with design placement
7. publish_product → Publish to Etsy
```

### 2. Submit an Order

```
User: "Order 5 of product ABC123 and ship to John Doe"

Agent workflow:
1. get_shops → Get shop_id
2. create_order → Submit order with line items and shipping address
```

## Deployment

### Deploy to Stainless (or any cloud platform)

This MCP server can be deployed to any cloud platform that supports Node.js applications.

**General steps:**

1. Push your code to a Git repository
2. Configure environment variables on your hosting platform
3. Set the start command to `npm start`
4. Deploy

**For Stainless specifically:**
- Follow Stainless deployment documentation
- Ensure `PRINTIFY_API_TOKEN` is set in environment variables
- The server will communicate via stdio protocol

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `PRINTIFY_API_TOKEN` | Yes | Your Printify API personal access token |

## API Rate Limits

Be aware of Printify's API rate limits:

- **Global limit**: 600 requests per minute
- **Catalog endpoints**: 100 requests per minute
- **Product publishing**: 200 requests per 30 minutes

The MCP server will return error messages if rate limits are exceeded.

## Error Handling

The server includes comprehensive error handling:

- API errors are captured and returned with descriptive messages
- Network errors are handled gracefully
- Invalid tool calls return helpful error responses

## Development

### Project Structure

```
printify-mcp-server/
├── src/
│   └── index.ts          # Main server implementation
├── dist/                 # Compiled JavaScript (generated)
├── package.json          # Dependencies and scripts
├── tsconfig.json         # TypeScript configuration
├── .env.example          # Example environment variables
├── .gitignore
└── README.md
```

### Building

```bash
npm run build
```

### Watch Mode

For development with auto-rebuild:

```bash
npm run watch
```

## Troubleshooting

### "PRINTIFY_API_TOKEN environment variable is required"

Make sure you've created a `.env` file with your token, or set the environment variable in your deployment platform.

### Rate Limit Errors (429)

You've exceeded Printify's API rate limits. Wait a moment and try again, or implement request throttling in your agent logic.

### Authentication Errors (401)

Your API token may be invalid or expired. Generate a new token from your Printify account settings.

## Security Considerations

- **Never commit your `.env` file** to version control
- Store API tokens securely in environment variables
- Use HTTPS when deploying to production
- Rotate API tokens periodically
- Limit token scopes to only what's needed

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Resources

- [Printify API Documentation](https://developers.printify.com/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk)

## Support

For issues with:
- **This MCP server**: Open an issue in this repository
- **Printify API**: Contact [Printify Support](https://printify.com/contact-us/)
- **MCP Protocol**: Visit [MCP Documentation](https://modelcontextprotocol.io/)

---

Built with ❤️ for the AI automation community

