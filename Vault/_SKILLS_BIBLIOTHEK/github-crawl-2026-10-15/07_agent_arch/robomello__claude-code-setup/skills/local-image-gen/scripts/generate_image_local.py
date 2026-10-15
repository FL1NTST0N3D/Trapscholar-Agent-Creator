#!/usr/bin/env python3
"""Generate images locally using ComfyUI with Z-Image Turbo or Flux models.

Talks to the local ComfyUI instance at localhost:8188.
No cloud APIs, no API keys needed.

Usage:
    python generate_image_local.py "A golden retriever in autumn leaves"
    python generate_image_local.py "A futuristic city" --model flux --width 1024 --height 576
    python generate_image_local.py "Portrait photo" --width 720 --height 1024 -o ~/sites/output/portrait.png
"""

import argparse
import json
import os
import random
import sys
import time
import urllib.request
import urllib.error

COMFYUI_URL = os.environ.get("COMFYUI_URL", "http://comfyui:8188")


def build_z_image_turbo_prompt(text, width, height, seed):
    """Build API-format prompt for Z-Image Turbo."""
    return {
        "1": {
            "class_type": "CLIPLoader",
            "inputs": {
                "clip_name": "qwen_3_4b.safetensors",
                "type": "lumina2",
                "device": "default"
            }
        },
        "2": {
            "class_type": "UNETLoader",
            "inputs": {
                "unet_name": "z_image_turbo_bf16.safetensors",
                "weight_dtype": "default"
            }
        },
        "3": {
            "class_type": "VAELoader",
            "inputs": {
                "vae_name": "ae.safetensors"
            }
        },
        "4": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": text,
                "clip": ["1", 0]
            }
        },
        "5": {
            "class_type": "ConditioningZeroOut",
            "inputs": {
                "conditioning": ["4", 0]
            }
        },
        "6": {
            "class_type": "ModelSamplingAuraFlow",
            "inputs": {
                "model": ["2", 0],
                "shift": 3.0
            }
        },
        "7": {
            "class_type": "EmptySD3LatentImage",
            "inputs": {
                "width": width,
                "height": height,
                "batch_size": 1
            }
        },
        "8": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["6", 0],
                "positive": ["4", 0],
                "negative": ["5", 0],
                "latent_image": ["7", 0],
                "seed": seed,
                "steps": 20,
                "cfg": 1.0,
                "sampler_name": "euler_ancestral",
                "scheduler": "simple",
                "denoise": 1.0
            }
        },
        "9": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["8", 0],
                "vae": ["3", 0]
            }
        },
        "10": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["9", 0],
                "filename_prefix": "local-gen"
            }
        }
    }


def build_flux2_dev_prompt(text, width, height, seed):
    """Build API-format prompt for Flux 2 Dev (fp8 mixed, uses advanced sampler)."""
    return {
        "1": {
            "class_type": "CLIPLoader",
            "inputs": {
                "clip_name": "mistral_3_small_flux2_bf16.safetensors",
                "type": "flux2",
                "device": "default"
            }
        },
        "2": {
            "class_type": "UNETLoader",
            "inputs": {
                "unet_name": "flux2_dev_fp8mixed.safetensors",
                "weight_dtype": "default"
            }
        },
        "3": {
            "class_type": "VAELoader",
            "inputs": {
                "vae_name": "flux2-vae.safetensors"
            }
        },
        "4": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": text,
                "clip": ["1", 0]
            }
        },
        "5": {
            "class_type": "RandomNoise",
            "inputs": {
                "noise_seed": seed
            }
        },
        "6": {
            "class_type": "BasicGuider",
            "inputs": {
                "model": ["2", 0],
                "conditioning": ["4", 0]
            }
        },
        "7": {
            "class_type": "KSamplerSelect",
            "inputs": {
                "sampler_name": "euler"
            }
        },
        "8": {
            "class_type": "BasicScheduler",
            "inputs": {
                "model": ["2", 0],
                "scheduler": "simple",
                "steps": 30,
                "denoise": 1.0
            }
        },
        "9": {
            "class_type": "EmptyFlux2LatentImage",
            "inputs": {
                "width": width,
                "height": height,
                "batch_size": 1
            }
        },
        "10": {
            "class_type": "SamplerCustomAdvanced",
            "inputs": {
                "noise": ["5", 0],
                "guider": ["6", 0],
                "sampler": ["7", 0],
                "sigmas": ["8", 0],
                "latent_image": ["9", 0]
            }
        },
        "11": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["10", 0],
                "vae": ["3", 0]
            }
        },
        "12": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["11", 0],
                "filename_prefix": "local-gen"
            }
        }
    }


def build_flux2_klein_prompt(text, width, height, seed):
    """Build API-format prompt for Flux 2 Klein 4B (fast, lighter on VRAM)."""
    return {
        "1": {
            "class_type": "CLIPLoader",
            "inputs": {
                "clip_name": "qwen_3_4b_fp4_flux2.safetensors",
                "type": "flux2",
                "device": "default"
            }
        },
        "2": {
            "class_type": "UNETLoader",
            "inputs": {
                "unet_name": "flux-2-klein-4b-fp8.safetensors",
                "weight_dtype": "default"
            }
        },
        "3": {
            "class_type": "VAELoader",
            "inputs": {
                "vae_name": "flux2-vae.safetensors"
            }
        },
        "4": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": text,
                "clip": ["1", 0]
            }
        },
        "5": {
            "class_type": "RandomNoise",
            "inputs": {
                "noise_seed": seed
            }
        },
        "6": {
            "class_type": "BasicGuider",
            "inputs": {
                "model": ["2", 0],
                "conditioning": ["4", 0]
            }
        },
        "7": {
            "class_type": "KSamplerSelect",
            "inputs": {
                "sampler_name": "euler"
            }
        },
        "8": {
            "class_type": "BasicScheduler",
            "inputs": {
                "model": ["2", 0],
                "scheduler": "simple",
                "steps": 20,
                "denoise": 1.0
            }
        },
        "9": {
            "class_type": "EmptyFlux2LatentImage",
            "inputs": {
                "width": width,
                "height": height,
                "batch_size": 1
            }
        },
        "10": {
            "class_type": "SamplerCustomAdvanced",
            "inputs": {
                "noise": ["5", 0],
                "guider": ["6", 0],
                "sampler": ["7", 0],
                "sigmas": ["8", 0],
                "latent_image": ["9", 0]
            }
        },
        "11": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["10", 0],
                "vae": ["3", 0]
            }
        },
        "12": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["11", 0],
                "filename_prefix": "local-gen"
            }
        }
    }


def build_qwen_image_2512_prompt(text, width, height, seed):
    """Build API-format prompt for Qwen Image 2512 (BF16, 38 GB).

    Uses Lightning LoRA + ModelSamplingAuraFlow + CFGNorm.
    30 steps, CFG 2, euler_ancestral, beta57 scheduler.
    """
    return {
        "1": {
            "class_type": "UNETLoader",
            "inputs": {
                "unet_name": "qwen_image_2512_bf16.safetensors",
                "weight_dtype": "default"
            }
        },
        "2": {
            "class_type": "CLIPLoader",
            "inputs": {
                "clip_name": "qwen_2.5_vl_7b.safetensors",
                "type": "qwen_image",
                "device": "default"
            }
        },
        "3": {
            "class_type": "VAELoader",
            "inputs": {
                "vae_name": "qwen_image_vae.safetensors"
            }
        },
        "4": {
            "class_type": "LoraLoaderModelOnly",
            "inputs": {
                "model": ["1", 0],
                "lora_name": "Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors",
                "strength_model": 1.0
            }
        },
        "5": {
            "class_type": "ModelSamplingAuraFlow",
            "inputs": {
                "model": ["4", 0],
                "shift": 3.0
            }
        },
        "6": {
            "class_type": "CFGNorm",
            "inputs": {
                "model": ["5", 0],
                "strength": 1.0
            }
        },
        "7": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": text,
                "clip": ["2", 0]
            }
        },
        "8": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": "",
                "clip": ["2", 0]
            }
        },
        "9": {
            "class_type": "EmptyLatentImage",
            "inputs": {
                "width": width,
                "height": height,
                "batch_size": 1
            }
        },
        "10": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["6", 0],
                "positive": ["7", 0],
                "negative": ["8", 0],
                "latent_image": ["9", 0],
                "seed": seed,
                "steps": 30,
                "cfg": 2.0,
                "sampler_name": "euler_ancestral",
                "scheduler": "beta57",
                "denoise": 1.0
            }
        },
        "11": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["10", 0],
                "vae": ["3", 0]
            }
        },
        "12": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["11", 0],
                "filename_prefix": "local-gen"
            }
        }
    }


def queue_prompt(prompt):
    """Queue a prompt and return the prompt_id."""
    data = json.dumps({"prompt": prompt}).encode("utf-8")
    req = urllib.request.Request(
        f"{COMFYUI_URL}/prompt",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
    prompt_id = result.get("prompt_id")
    if not prompt_id:
        print(f"Error: No prompt_id returned: {result}", file=sys.stderr)
        sys.exit(1)
    return prompt_id


def wait_for_completion(prompt_id, max_wait=300, poll=2.0):
    """Poll history until the prompt completes."""
    waited = 0
    while waited < max_wait:
        time.sleep(poll)
        waited += poll
        try:
            req = urllib.request.Request(f"{COMFYUI_URL}/history/{prompt_id}")
            with urllib.request.urlopen(req, timeout=10) as resp:
                history = json.loads(resp.read())
        except Exception:
            continue

        if prompt_id in history:
            entry = history[prompt_id]
            status = entry.get("status", {})
            if status.get("completed", False):
                return entry
            status_str = status.get("status_str", "")
            if status_str == "error":
                msgs = status.get("messages", [])
                print(f"Error from ComfyUI: {msgs}", file=sys.stderr)
                sys.exit(1)

        if int(waited) % 10 == 0:
            print(f"  Waiting... {int(waited)}s", file=sys.stderr)

    print(f"Timeout after {max_wait}s", file=sys.stderr)
    sys.exit(1)


def download_image(history, output_path):
    """Download the first output image from ComfyUI."""
    outputs = history.get("outputs", {})
    for node_id, node_out in outputs.items():
        if "images" not in node_out:
            continue
        for img in node_out["images"]:
            filename = img.get("filename")
            subfolder = img.get("subfolder", "")
            img_type = img.get("type", "output")
            if not filename:
                continue

            params = f"filename={filename}&type={img_type}"
            if subfolder:
                params += f"&subfolder={subfolder}"

            url = f"{COMFYUI_URL}/view?{params}"
            try:
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req, timeout=60) as resp:
                    image_data = resp.read()

                os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
                with open(output_path, "wb") as f:
                    f.write(image_data)
                print(f"Saved: {output_path}")
                return output_path
            except Exception as e:
                print(f"Failed to download {filename}: {e}", file=sys.stderr)
                continue

    print("No output images found in generation result.", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate images locally via ComfyUI")
    parser.add_argument("prompt", help="Text description of the image to generate")
    parser.add_argument("-o", "--output", default=None, help="Output file path (default: auto-generated in ~/output/comfyui/)")
    parser.add_argument("--model", choices=["turbo", "flux", "klein", "qwen2512"], default="qwen2512", help="Model: qwen2512 (Qwen Image 2512 BF16, default), turbo (Z-Image Turbo), flux (Flux 2 Dev fp8), klein (Flux 2 Klein 4B)")
    parser.add_argument("--width", type=int, default=None, help="Image width (default: 864 for qwen2512, 1024 for others)")
    parser.add_argument("--height", type=int, default=None, help="Image height (default: 1536 for qwen2512, 1024 for others)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (default: random)")
    parser.add_argument("--steps", type=int, default=None, help="Override inference steps")
    args = parser.parse_args()

    seed = args.seed if args.seed is not None else random.randint(0, 2**63)

    # Set default dimensions based on model
    if args.model == "qwen2512":
        if args.width is None:
            args.width = 864
        if args.height is None:
            args.height = 1536
    else:
        if args.width is None:
            args.width = 1024
        if args.height is None:
            args.height = 1024

    # Build the prompt
    if args.model == "turbo":
        api_prompt = build_z_image_turbo_prompt(args.prompt, args.width, args.height, seed)
        model_label = "Z-Image Turbo"
        steps_node = "8"
    elif args.model == "flux":
        api_prompt = build_flux2_dev_prompt(args.prompt, args.width, args.height, seed)
        model_label = "Flux 2 Dev (fp8)"
        steps_node = "8"
    elif args.model == "qwen2512":
        api_prompt = build_qwen_image_2512_prompt(args.prompt, args.width, args.height, seed)
        model_label = "Qwen Image 2512 (BF16)"
        steps_node = "10"
    else:
        api_prompt = build_flux2_klein_prompt(args.prompt, args.width, args.height, seed)
        model_label = "Flux 2 Klein 4B"
        steps_node = "8"

    # Override steps if specified
    if args.steps is not None:
        api_prompt[steps_node]["inputs"]["steps"] = args.steps

    # Default output path
    if args.output is None:
        safe_name = args.prompt[:50].lower().replace(" ", "_")
        safe_name = "".join(c for c in safe_name if c.isalnum() or c == "_")
        args.output = f"~/output/comfyui/local-gen_{safe_name}.png"

    print(f"Model: {model_label}")
    print(f"Size: {args.width}x{args.height}")
    print(f"Seed: {seed}")
    print(f"Prompt: {args.prompt[:100]}{'...' if len(args.prompt) > 100 else ''}")

    # Check ComfyUI is up
    try:
        req = urllib.request.Request(f"{COMFYUI_URL}/system_stats")
        with urllib.request.urlopen(req, timeout=5) as resp:
            pass
    except Exception as e:
        print(f"Error: ComfyUI not reachable at {COMFYUI_URL}: {e}", file=sys.stderr)
        sys.exit(1)

    # Queue and wait
    start = time.time()
    prompt_id = queue_prompt(api_prompt)
    print(f"Queued: {prompt_id}")

    history = wait_for_completion(prompt_id)
    elapsed = time.time() - start
    print(f"Generated in {elapsed:.1f}s")

    # Download
    download_image(history, args.output)


if __name__ == "__main__":
    main()
