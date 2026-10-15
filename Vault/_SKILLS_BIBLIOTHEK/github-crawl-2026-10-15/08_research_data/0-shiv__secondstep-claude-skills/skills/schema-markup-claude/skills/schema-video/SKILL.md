# Schema: Video

Generate VideoObject and BroadcastEvent schema markup in JSON-LD format. This schema enables video rich results in Google Search, video carousels, key moments, and livestream badges, driving significantly higher engagement from search results.

## Command

`/schema video`

## When to Use

VideoObject schema belongs on any page that features video content: product demo videos, tutorial videos, embedded YouTube/Vimeo videos, course lesson videos, webinar recordings, and self-hosted video content. If a page's primary content is a video, or if a video is a significant supporting element, it should have VideoObject schema. Video rich results occupy significantly more visual real estate in search results than standard text results, making this a high-impact schema type.

## Required Properties (Google)

- `@type`: "VideoObject"
- `name`: Video title
- `description`: Video description (max ~300 characters for rich result display)
- `thumbnailUrl`: URL to video thumbnail image (at least 1 thumbnail required; multiple recommended)
- `uploadDate`: ISO 8601 date the video was first published

## Recommended Properties

- `duration`: ISO 8601 duration format (e.g., "PT5M30S" for 5 minutes 30 seconds)
- `contentUrl`: URL to the actual video file (MP4, WebM, etc.)
- `embedUrl`: URL for the embedded video player (e.g., YouTube embed URL)
- `interactionStatistic`: View count using InteractionCounter
- `expires`: Date when the video will no longer be available
- `hasPart`: Array of Clip objects for key moments / chapters
- `publication`: BroadcastEvent for livestream videos
- `regionsAllowed`: Countries where the video is available
- `inLanguage`: Language of the video
- `transcript`: Full text transcript of the video
- `caption`: URL to caption/subtitle file
- `author`: Person or Organization who created the video
- `publisher`: Organization that published the video

## Key Moments (Clips)

Google can display key moments (chapters/timestamps) from videos. Use `hasPart` with Clip objects:

```json
"hasPart": [
  {
    "@type": "Clip",
    "name": "Introduction",
    "startOffset": 0,
    "endOffset": 30,
    "url": "https://example.com/video#t=0"
  },
  {
    "@type": "Clip",
    "name": "Step 1: Setup",
    "startOffset": 30,
    "endOffset": 120,
    "url": "https://example.com/video#t=30"
  }
]
```

For YouTube videos, Google can automatically extract key moments from chapter markers in the video description. For non-YouTube videos, Clip markup is required.

## Livestream (BroadcastEvent)

For live-streaming events, add a `publication` property with BroadcastEvent:

```json
"publication": {
  "@type": "BroadcastEvent",
  "isLiveBroadcast": true,
  "startDate": "2024-06-15T14:00:00-05:00",
  "endDate": "2024-06-15T16:00:00-05:00"
}
```

This enables the red "LIVE" badge in Google Search results. To use this feature, you must also implement the Indexing API to notify Google when the stream starts and ends.

## YouTube vs Self-Hosted Videos

### YouTube Embedded Videos
- `embedUrl`: "https://www.youtube.com/embed/VIDEO_ID"
- `contentUrl`: "https://www.youtube.com/watch?v=VIDEO_ID"
- `thumbnailUrl`: "https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg"
- YouTube videos may already have Google-indexed schema from YouTube itself. Adding your own schema on the embedding page helps YOUR page rank for video searches rather than just the YouTube page.

### Self-Hosted Videos
- `contentUrl`: Direct URL to the video file
- `embedUrl`: URL to your video player page
- Must provide `thumbnailUrl` (Google cannot auto-generate thumbnails from self-hosted videos)
- Ensure the video file URL is accessible to Googlebot (not behind authentication)

## Duration Formatting (ISO 8601)

- 30 seconds: `PT30S`
- 5 minutes: `PT5M`
- 5 minutes 30 seconds: `PT5M30S`
- 1 hour: `PT1H`
- 1 hour 30 minutes 45 seconds: `PT1H30M45S`

## Common Mistakes

- **Missing thumbnailUrl**: Google requires at least one thumbnail. Without it, no video rich result.
- **Thumbnail too small**: Thumbnails should be at least 60x30px, recommended 160x90px or larger.
- **Using YouTube URL as contentUrl when self-hosting**: contentUrl should point to the actual video file, not a webpage.
- **Missing uploadDate**: Required for all video rich results.
- **Expired video still indexed**: Use the `expires` property to tell Google when a video is no longer available.
- **Duration format errors**: "5:30" is wrong. Use ISO 8601: "PT5M30S".
- **Duplicate VideoObject**: Only use VideoObject schema on the page where the video is the primary or significant content, not on every page that has a background video or decorative clip.

## Google Rich Result Eligibility

VideoObject schema enables:
- **Video rich results**: Thumbnail, duration, and upload date in search results
- **Video carousel**: Horizontal scrollable video cards for relevant queries
- **Key moments**: Timestamp-linked sections within video results
- **LIVE badge**: Red live indicator for active livestreams
- **Google Video Search**: Enhanced listings in the Videos tab
- **Google Discover**: Video content surfaced in Discover feeds
