#!/usr/bin/env python3
"""YouTube video extractor - downloads metadata, transcript, and frames.

Usage:
    python yt_extract.py <youtube_url> [--interval 10] [--output-dir /tmp/yt_analysis]

Returns JSON with paths to all extracted assets.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def get_metadata(url: str) -> dict:
    """Extract video metadata via yt-dlp."""
    fields = [
        "title", "channel", "duration", "upload_date",
        "description", "view_count", "like_count", "channel_url",
        "thumbnail", "categories", "tags"
    ]
    cmd = ["yt-dlp", "--print", "%({})j".format("},{".join(
        f'"{f}": %({f})j' for f in fields
    ))]
    # Simpler approach: dump JSON
    cmd = [
        "yt-dlp", "--dump-json", "--no-download", url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"Warning: metadata fetch stderr: {result.stderr[:200]}", file=sys.stderr)

    data = json.loads(result.stdout)
    return {
        "title": data.get("title", "Unknown"),
        "channel": data.get("channel", data.get("uploader", "Unknown")),
        "channel_url": data.get("channel_url", ""),
        "duration": data.get("duration", 0),
        "upload_date": data.get("upload_date", ""),
        "description": data.get("description", ""),
        "view_count": data.get("view_count", 0),
        "like_count": data.get("like_count", 0),
        "categories": data.get("categories", []),
        "tags": data.get("tags", []),
        "thumbnail": data.get("thumbnail", ""),
    }


def download_transcript(url: str, output_dir: str) -> str:
    """Download and clean auto-generated subtitles."""
    sub_path = os.path.join(output_dir, "subs")
    os.makedirs(sub_path, exist_ok=True)

    cmd = [
        "yt-dlp", "--write-auto-sub", "--sub-lang", "en",
        "--skip-download", "--sub-format", "vtt",
        "-o", os.path.join(sub_path, "%(id)s"),
        url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    # Find the VTT file
    vtt_files = list(Path(sub_path).glob("*.vtt"))
    if not vtt_files:
        # Try other languages
        cmd[3] = "en,es,pt,de,fr"
        subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        vtt_files = list(Path(sub_path).glob("*.vtt"))

    if not vtt_files:
        return ""

    # Clean VTT to plain text
    with open(vtt_files[0], "r", encoding="utf-8") as f:
        raw = f.read()

    lines = raw.split("\n")
    clean = []
    seen = set()
    for line in lines:
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if re.match(r"^\d{2}:\d{2}", line):
            continue
        if not line.strip():
            continue
        line = re.sub(r"<[^>]+>", "", line).strip()
        if line and line not in seen:
            seen.add(line)
            clean.append(line)

    transcript_text = "\n".join(clean)
    transcript_path = os.path.join(output_dir, "transcript.txt")
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(transcript_text)

    return transcript_path


def download_video(url: str, output_dir: str) -> str:
    """Download video at 720p max for frame extraction."""
    video_path = os.path.join(output_dir, "video.mp4")
    if os.path.exists(video_path):
        os.remove(video_path)

    cmd = [
        "yt-dlp", "-f", "best[height<=720]",
        "-o", video_path, url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if result.returncode != 0:
        # Fallback to any format
        cmd = ["yt-dlp", "-f", "best", "-o", video_path, url]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

    if os.path.exists(video_path):
        return video_path
    return ""


def extract_frames(video_path: str, output_dir: str, interval: int = 10) -> list:
    """Extract frames at given interval using ffmpeg."""
    frames_dir = os.path.join(output_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    # Clean old frames
    for f in Path(frames_dir).glob("frame_*.jpg"):
        f.unlink()

    cmd = [
        "ffmpeg", "-i", video_path,
        "-vf", f"fps=1/{interval}",
        "-q:v", "2",
        os.path.join(frames_dir, "frame_%04d.jpg")
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=300)

    frames = sorted(Path(frames_dir).glob("frame_*.jpg"))
    return [str(f) for f in frames]


def main():
    parser = argparse.ArgumentParser(description="YouTube video extractor")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--interval", type=int, default=10,
                        help="Frame extraction interval in seconds (default: 10)")
    parser.add_argument("--output-dir", default="/tmp/yt_analysis",
                        help="Output directory (default: /tmp/yt_analysis)")
    parser.add_argument("--skip-video", action="store_true",
                        help="Skip video download and frame extraction")
    args = parser.parse_args()

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    print("Extracting metadata...", file=sys.stderr)
    metadata = get_metadata(args.url)

    print("Downloading transcript...", file=sys.stderr)
    transcript_path = download_transcript(args.url, output_dir)

    frames = []
    video_path = ""
    if not args.skip_video:
        print("Downloading video...", file=sys.stderr)
        video_path = download_video(args.url, output_dir)

        if video_path:
            print(f"Extracting frames every {args.interval}s...", file=sys.stderr)
            frames = extract_frames(video_path, output_dir, args.interval)

    # Save metadata
    meta_path = os.path.join(output_dir, "metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    result = {
        "metadata": metadata,
        "metadata_path": meta_path,
        "transcript_path": transcript_path,
        "video_path": video_path,
        "frames": frames,
        "frame_count": len(frames),
        "interval_seconds": args.interval,
        "output_dir": output_dir,
    }

    # Write result manifest
    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
