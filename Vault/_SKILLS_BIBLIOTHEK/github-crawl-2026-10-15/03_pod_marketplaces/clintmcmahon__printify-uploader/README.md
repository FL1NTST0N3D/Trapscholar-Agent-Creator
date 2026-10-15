# Printify Product Uploader

A Python tool for automatically creating Printify products from design files organized in folders.

## Features

- **Folder-driven processing**: Automatically scans folders for design files instead of CSV data
- **Multi-product support**: Configure different product types (t-shirts, sweatshirts, etc.)
- **Batch processing**: Create products for multiple cities at once
- **Flexible file patterns**: Support different naming conventions for design files
- **Dry run mode**: Preview what would be created without uploading

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Credentials

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Printify API credentials:
   ```
   PRINTIFY_ACCESS_TOKEN=your_printify_access_token_here
   PRINTIFY_SHOP_ID=your_shop_id_here
   ```

3. Get your credentials from [Printify API Settings](https://printify.com/app/account/api)

### 3. Configure Products

Edit `product_config.json` to define your product configurations. Each product type includes:

- Blueprint ID and print provider
- Variant configurations (colors, sizes, prices)
- File patterns for design files
- Image positioning and properties

## Usage

### List Available Product Configurations
```bash
python run_folder_uploader.py --list-configs
```

### Create Products for All Cities
```bash
python run_folder_uploader.py --product comfort_colors_1717
python run_folder_uploader.py --product lane_seven_LS14004
```

### Create Products for Specific City
```bash
python run_folder_uploader.py --product comfort_colors_1717 --city Atlanta
```

### Preview Without Creating (Dry Run)
```bash
python run_folder_uploader.py --product comfort_colors_1717 --dry-run
```

### Specify Custom Base Path
```bash
python run_folder_uploader.py --product comfort_colors_1717 --base-path /path/to/designs
```

## Configuration

### Product Configuration Structure

```json
{
  "product_configs": {
    "your_product_key": {
      "name": "Product Name",
      "blueprint_id": 706,
      "print_provider_id": 99,
      "default_price": 3400,
      "file_pattern": "{city_name}_{image_color}_Design.png",
      "design_folder": "path/to/designs",
      "title_template": "{city_name} Custom Product",
      "variants": [
        {
          "id": 12345,
          "color": "Navy",
          "size": "M",
          "price": 3400,
          "image_color": "Ivory",
          "image_properties": {
            "x": 71,
            "y": 10,
            "height": 2,
            "scale": 1.0,
            "angle": 0
          }
        }
      ]
    }
  }
}
```

### File Organization

Design files should follow the pattern specified in `file_pattern`:
```
designs/
├── Atlanta_Ivory_Design.png
├── Atlanta_Red_Design.png
├── Boston_Ivory_Design.png
├── Boston_Red_Design.png
└── ...
```

## Blueprint Discovery Tool

### What is `get_blueprint_info.py`?

This is a **discovery utility** that helps you explore Printify's product catalog and find the specific IDs needed to configure new products in your store.

### What It Does:

1. **Lists all available product types** (blueprints) - t-shirts, hoodies, mugs, phone cases, etc.
2. **Shows print providers** for each product type
3. **Reveals variant IDs** - the specific combinations of color/size available for each product

### Why You Need It:

When adding a **new product type** to your configuration, you need three key pieces of information:

- **Blueprint ID** - Identifies the product type (e.g., 706 = Comfort Colors t-shirt, 446 = Lane Seven sweatshirt)
- **Print Provider ID** - Identifies the manufacturer (e.g., 99 = specific print provider)
- **Variant IDs** - Identifies exact color/size combinations (e.g., 73201 = Navy/M, 78897 = Blue Spruce/M)

### When to Use It:

- ✅ **Adding a new product type** to your store (e.g., adding hoodies after you already have t-shirts)
- ✅ **Finding available colors and sizes** for a specific product
- ✅ **Getting the exact IDs** to copy into `product_config.json`

### How to Use:

```bash
python get_blueprint_info.py
```

The tool will:
1. Show you all available blueprints
2. Let you select one to explore
3. Display available print providers
4. Show all variant IDs with their color/size combinations
5. Save the information to `blueprint_info.json` for reference

### Example Workflow:

1. Run `get_blueprint_info.py`
2. Find that Lane Seven sweatshirt = Blueprint **446**
3. Discover variant IDs like **62616** (Charcoal Heather/S) and **62625** (Oatmeal Heather/M)
4. Copy those IDs into `product_config.json` under a new product configuration
5. Use the main uploader to create products with your new configuration

**Note:** This is a reference utility - you don't need it for day-to-day product creation, only when expanding your product catalog with new product types.

## Security

- **Never commit API credentials**: The `.env` file is excluded from Git
- **Use environment variables**: Credentials are loaded from `.env` file
- **Example file provided**: Copy `.env.example` to `.env` for setup

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details