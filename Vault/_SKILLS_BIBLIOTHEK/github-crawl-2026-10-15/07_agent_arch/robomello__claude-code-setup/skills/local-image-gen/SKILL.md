---
name: local-image-gen
description: >
  DEFAULT image generator. Generate images locally using ComfyUI. No cloud API, no cost.
  Use for ALL image generation/creation requests unless user explicitly asks for cloud API.
  Triggers: "generate image", "create picture", "make illustration", "render", "draw",
  "photo of", "image of", "generate a [thing]", "make me a [visual]".
  DO NOT trigger on: "describe this image", "analyze photo", "what's in this image",
  "OCR", "read text from image" (those are vision/QwenVL tasks, not generation).
---

# Local Image Generation (ComfyUI)

This is the DEFAULT image generation method. Always use this unless the user explicitly requests a cloud API.

## CRITICAL: Sequential Only

**NEVER run parallel image generations.** Always generate one image at a time, wait for completion, then start the next. Parallel calls crash ComfyUI.

## Models Available

| Model | Flag | Speed | Quality | VRAM | Best For |
|-------|------|-------|---------|------|----------|
| Qwen Image 2512 | `--model qwen2512` (default) | ~110s | Very high | ~38 GB | Best quality, portraits, complex scenes |
| Z-Image Turbo | `--model turbo` | ~44s | High | ~8 GB | Fast, general purpose |
| Flux 2 Klein 4B | `--model klein` | ~46s | High | ~6 GB | Flux-quality, lighter VRAM |
| Flux 2 Dev fp8 | `--model flux` | ~60s | Very high | ~12 GB | Full Flux 2 quality |

**Default is `qwen2512`** (38 GB BF16, best quality). Use `turbo` when speed matters more than quality. Default size: 864x1536 (9:16 portrait) for qwen2512, 1024x1024 for others.

## Usage

```bash
python <skill-path>/scripts/generate_image_local.py "PROMPT" [options]
```

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `prompt` (positional) | required | Text description of the image |
| `--model` | `qwen2512` | `qwen2512`, `turbo`, `klein`, or `flux` |
| `--width` | model-dependent | Image width in pixels |
| `--height` | model-dependent | Image height in pixels |
| `-o`, `--output` | auto-generated | Output file path |
| `--seed` | random | Seed for reproducibility |
| `--steps` | model-dependent | Override inference steps (see table below) |

### Recommended Steps Per Model

| Model | Default Steps | CFG | Recommended Range |
|-------|--------------|-----|-------------------|
| qwen2512 | 30 | 5.0 | 20-40 |
| turbo | 8 | 1.0 | 4-12 |
| klein | 20 | 1.0 | 15-30 |
| flux | 30 | 1.0 | 20-40 |

Overriding `--steps` outside the recommended range may produce poor results.

### Examples

Qwen Image 2512 (highest quality, default):
```bash
python <skill-path>/scripts/generate_image_local.py "A photorealistic portrait of a woman in a red dress" --model qwen2512 --width 864 --height 1536
```

Z-Image Turbo (fast):
```bash
python <skill-path>/scripts/generate_image_local.py "A golden retriever playing in autumn leaves" --model turbo
```

Flux 2 Klein with custom size:
```bash
python <skill-path>/scripts/generate_image_local.py "A futuristic cityscape at night" --model klein --width 1024 --height 576
```

Portrait with custom output:
```bash
python <skill-path>/scripts/generate_image_local.py "Professional headshot, studio lighting" --width 720 --height 1024 -o ~/sites/portraits/headshot.png
```

### Defaults

- **Model**: Use Qwen Image 2512 (`qwen2512`) by default. Use `turbo` when speed matters. Use `klein` when user asks for Flux.
- **Size**: 864x1536 (9:16 portrait) for qwen2512. 1024x1024 for turbo/klein/flux.
- **Output**: Auto-generated as `~/output/comfyui/local-gen_<sanitized_prompt>.png`. Use `-o` to override.

## Requirements

- Local ComfyUI running at `comfyui:8188` (Docker DNS, default) or `localhost:8188` (override via `COMFYUI_URL` env var)
- No pip packages needed (uses stdlib `urllib` only)
- No API keys needed

## Encoder Compatibility

Each model uses a specific text encoder. These are NOT interchangeable:
- **Z-Image (turbo)**: Qwen 4B encoder (2560 dim)
- **Qwen Image (qwen2512)**: Qwen2.5-VL-7B encoder (3584 dim)
- **Flux models (klein, flux)**: Mistral 3 Small encoder
