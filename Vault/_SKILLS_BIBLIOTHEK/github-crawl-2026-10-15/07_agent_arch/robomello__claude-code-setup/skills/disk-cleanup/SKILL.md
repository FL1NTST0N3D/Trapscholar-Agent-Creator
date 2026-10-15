---
name: disk-cleanup
description: >
  This skill should be used when the user mentions "disk space", "cleanup",
  "storage", "free space", "disk full", "prune", "disk audit", "clean disk",
  or when system-watcher alerts about disk usage. Audits disk usage, cleans
  safe targets, and offloads to NAS.
  DO NOT trigger on: "backup files", "move files to NAS" (use synology-nas skill),
  "docker logs" (general Docker questions, not disk cleanup).
---

# Disk Cleanup Skill

Audit disk usage, clean safe targets, and offload to NAS.

## Step 1: Disk Audit

```bash
# Overall usage
df -h /

# Top-level space consumers
sudo du -h --max-depth=1 / 2>/dev/null | sort -rh | head -20

# Home directory breakdown
sudo du -h --max-depth=1 ~ 2>/dev/null | sort -rh | head -20
```

## Step 2: Docker Cleanup

```bash
# Overview of Docker disk usage
docker system df

# Detailed breakdown
docker system df -v | head -50

# Dangling images (safe to remove)
docker images --filter "dangling=true"

# Check container writable layer bloat (>1GB is suspicious)
docker ps -a --format "table {{.Names}}\t{{.Size}}" | sort -k2 -rh

# Buildkit cache (often 10-20 GB)
docker buildx prune -f

# Full prune (dead containers, unused images, networks, build cache)
# USER APPROVAL REQUIRED for unused image removal
docker system prune -f          # safe: dead containers + dangling images + networks
docker image prune -a -f        # aggressive: ALL unused images (rebuilds needed, ~5-10 min for core services)
docker volume prune -f          # DANGEROUS: unnamed volumes removed permanently, data unrecoverable
```

## Step 3: Ollama Audit

```bash
# List models with sizes
docker exec ollama ollama list
```

**Models confirmed in use** (do NOT remove):
- `qwen3-embedding` - used for embeddings (4.7 GB)

**Models for interactive/dev use** (check with user before removing):
- `qwen3.5:35b-a3b` - latest Qwen reasoning (23 GB)
- `qwen3.5:27b` - Qwen 3.5 (17 GB)
- `glm-4.7-flash:bf16` - fast inference, full precision (59 GB)
- `glm-4.7-flash:q8_0` - fast inference, quantized (31 GB)
- `gemma3:12b` - general purpose (8.1 GB)

*Last verified: 2026-03-05. Run `docker exec ollama ollama list` to confirm.*

```bash
# Remove an Ollama model (USER APPROVAL REQUIRED)
docker exec ollama ollama rm <model-name>
```

## Step 4: ComfyUI Models

```bash
# List all model files with sizes
find ~/ComfyUI/models/ -type f \( -name "*.safetensors" -o -name "*.gguf" -o -name "*.bin" -o -name "*.pt" \) -exec du -sh {} \; 2>/dev/null | sort -rh
```

**Active models** (from MEDIA.md, do NOT remove):
- `z_image_turbo_bf16.safetensors` - Z-Image Turbo (fast default)
- `z_image_bf16.safetensors` - Z-Image Full
- `flux2_dev_fp8mixed.safetensors` - Flux 2 Dev
- `qwen_image_2512_bf16.safetensors` - Qwen Image 2512 (38 GB, best quality)
- `flux2_klein_9b_fp8.safetensors` - Flux 2 Klein 9B

**User preferences**:
- No GGUF models (exception: Z-Image clip GGUF which is required)
- Prefer safetensors format
- Archive cold models to NAS rather than delete

## Step 5: Quick Wins

```bash
# Journal logs (can be 4 GB+)
sudo journalctl --vacuum-size=500M

# Old snap revisions
snap list --all | awk '/disabled/{print $1, $3}'
# Then: sudo snap remove --purge <name> --revision <rev>

# NPM cache
npm cache clean --force

# Crash files
sudo rm -rf /var/crash/*

# Old temp files (>7 days)
find /tmp/ -maxdepth 1 -mtime +7 -exec du -sh {} \; 2>/dev/null | sort -rh

# HuggingFace temp downloads
find /tmp/ -name "hf_*" -mtime +1 -exec rm -rf {} \; 2>/dev/null

# Pip cache
find /tmp/ -name "pip-*" -mtime +7 -exec rm -rf {} \; 2>/dev/null
```

## Step 6: NAS Offload

**Already offloaded**: ComfyUI output -> `/mnt/nas/ComfyUI/output/`

**Offload candidates**:
- `~/sites/` (~3.6 GB) - web content
- Cold/unused models - archive before deleting
- Logs and build artifacts

**NOT moveable** (need NVMe speed):
- ComfyUI models (~700 GB)
- Ollama models (~226 GB)
- Docker overlay (~300 GB)
- `/data/llama-models/` (~97 GB)

### Adding a new NAS share

1. Create shared folder in DSM UI (https://192.168.x.x:5001)
2. Add to `/etc/fstab`:
   ```
   //192.168.x.x/<ShareName> /mnt/nas/<ShareName> cifs credentials=/root/.synology-creds,uid=1001,gid=1001,vers=3.0,nofail,x-systemd.automount,x-systemd.mount-timeout=30 0 0
   ```
3. Mount:
   ```bash
   sudo mkdir -p /mnt/nas/<ShareName> && sudo mount /mnt/nas/<ShareName>
   ```

## System-Watcher Auto-Cleanup

The system-watcher already handles basic cleanup at 85%/90% thresholds:
- Docker image/builder/network/volume prune
- Old logs in `~/logs/` (>7 days, >10 MB)
- `/tmp/hf_*`, apport dumps, pip cache
- Syslog truncation if >500 MB

Script: `~/commander/system-watcher.sh`
Service: `systemctl --user status system-watcher`

## Disk Budget (1.8 TB NVMe)

| Category | Size | Notes |
|----------|------|-------|
| ComfyUI models | ~700 GB | NVMe required |
| Docker overlay | ~300 GB | Local required |
| Ollama models | ~226 GB | NVMe required |
| /data/llama-models | ~97 GB | NVMe required |
| OS + packages | ~100 GB | Local required |
| Everything else | ~100 GB | Potentially moveable |

## Reference

Detailed thresholds and syslog fixes: [disk-management.md](../../.claude/projects/-home-user/memory/disk-management.md)
