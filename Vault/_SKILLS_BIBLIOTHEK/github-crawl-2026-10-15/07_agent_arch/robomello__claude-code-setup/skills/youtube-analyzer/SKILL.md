---
name: youtube-analyzer
description: >
  Comprehensive YouTube video analyzer that extracts transcripts AND does visual
  frame-by-frame analysis. Use this skill whenever a user shares a YouTube URL
  (youtube.com or youtu.be) and wants to understand what's in the video, asks to
  "analyze this video", "break down this video", "summarize this video",
  "what's in this video", "video analysis", or any request to extract content/insights
  from a YouTube video. Also trigger when user pastes a YouTube link and asks about
  its content, even casually like "what does this video talk about?" or "check this out".
  DO NOT trigger on: "upload to youtube", "create a video", "generate video",
  "youtube SEO", "youtube analytics", "youtube tags" (those are other skills/agents).
---

# YouTube Video Analyzer

Analyze YouTube videos by combining transcript analysis with visual frame-by-frame inspection. This produces a comprehensive content breakdown that captures both what's said and what's shown on screen.

## Why both transcript AND visuals?

Many YouTube videos convey critical information visually: code on screen, diagrams, slides, UI demos, terminal output, whiteboard drawings. The transcript alone misses all of this. By reading every extracted frame, you capture the full picture.

## Process

### Step 1: Extract everything

Run the helper script to download metadata, transcript, and frames:

```bash
python3 <skill-path>/scripts/yt_extract.py "<YOUTUBE_URL>" --interval 10 --output-dir /tmp/yt_analysis
```

This produces:
- `metadata.json` - title, channel, duration, upload date, description, view/like counts
- `transcript.txt` - cleaned auto-generated subtitles
- `frames/frame_NNNN.jpg` - one frame every 10 seconds
- `manifest.json` - paths to everything

If the script fails or yt-dlp has issues, troubleshoot:
- Update yt-dlp: `pip install -U yt-dlp`
- Try without format selection: remove the `-f` flag in the script
- Check if the video is age-restricted or private

### Step 2: Read the transcript

Read `/tmp/yt_analysis/transcript.txt` to understand the spoken content. Note the major topics, transitions, and structure.

### Step 3: Read every frame

Read EVERY frame image using the Read tool. You are multimodal and can see images directly. Go through them sequentially - do not skip frames.

For each frame, note:
- **What's on screen**: person talking to camera, code editor, terminal, slides, diagrams, browser, whiteboard, B-roll
- **Text visible**: any text overlays, code, slide titles, URLs, terminal commands
- **UI elements**: which app is shown (VS Code, terminal, browser, Figma, etc.)
- **Transitions**: when the visual format changes (e.g., from talking head to screen share)

Group consecutive similar frames together (e.g., if frames 15-22 all show VS Code with the same file, note it once with the time range).

### Step 4: Produce the analysis document

Create the output directory if it doesn't exist:

```bash
mkdir -p ~/projects/youtube-analyses
```

Write the analysis as a markdown file at:
`~/projects/youtube-analyses/YYYY-MM-DD_channel-name_video-title.md`

Sanitize the filename: lowercase, replace spaces with hyphens, remove special characters. Keep it readable.

### Output Structure

```markdown
# [Video Title]

| Field | Value |
|-------|-------|
| **Channel** | [Channel Name](channel_url) |
| **Published** | YYYY-MM-DD |
| **Duration** | MM:SS |
| **Views** | N |
| **Likes** | N |
| **URL** | [link](url) |

## Description
> Original video description here

## Content Breakdown

### [Timestamp Range] - [Section Title]
[What's discussed + what's shown on screen. Merge transcript content with visual observations. If there's code, diagrams, or slides visible, describe them in detail or reproduce key parts.]

### [Next Timestamp Range] - [Next Section Title]
...

## Visual Elements Catalog
List all unique visual elements that appeared:
- Diagrams/flowcharts (describe each)
- Code shown on screen (reproduce key snippets)
- Slides/text overlays (capture content)
- Tools/apps demonstrated
- UI screenshots

## Key Takeaways
1. [Takeaway 1]
2. [Takeaway 2]
...

## Full Transcript
<details>
<summary>Click to expand full transcript</summary>

[Full cleaned transcript text]

</details>
```

## Important notes

- **Frame reading is sequential**: Read frames one batch at a time. For very long videos (100+ frames), you can read them in batches of 10-15 to manage context. But never skip frames - every frame matters.
- **Merge visual + audio**: The most valuable part of this analysis is connecting what's said in the transcript with what's shown on screen. Don't treat them as separate sections - weave them together in the Content Breakdown.
- **Code and diagrams**: When you see code, terminal output, or diagrams in frames, reproduce them in the analysis (as code blocks or descriptions). This is often the most valuable content.
- **Timestamps**: Calculate approximate timestamps from frame numbers. Frame N at 10-second intervals = (N-1) * 10 seconds from the start.
