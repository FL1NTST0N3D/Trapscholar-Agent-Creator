"""
build_calendar_template.py
--------------------------
This is an ANNOTATED TEMPLATE showing the structure of the Python script
that Claude generates during Phase 5 of the social-calendar-skill.

Claude generates this script fresh every month, populated with:
  - The brand's actual content for that month
  - Posts derived from the approved narrative brief
  - Real hooks, copy, captions, scripts, and meme concepts

This template uses fictional "AcmeCorp" data so you can see exactly
what Claude produces — and run it yourself to see the Excel output.

Requirements: pip install openpyxl
Run with:     PYTHONUTF8=1 python3 build_calendar_template.py
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import os

wb = openpyxl.Workbook()

# ─────────────────────────────────────────────────────────────────────
# COLOUR PALETTE
# Claude adapts these to match the brand's visual identity.
# Convention: C_ prefix for all colour constants (hex strings, no #).
# ─────────────────────────────────────────────────────────────────────
C_BG        = "0F0F1A"   # Dark background — used for header rows
C_ACCENT    = "E87B3A"   # Brand accent — used for hooks, header fills
C_WEEK1_LT  = "D6E8F5"  # Week 1 pillar colour (light)
C_WEEK2_LT  = "D6F5D6"  # Week 2 pillar colour (light)
C_WEEK3_LT  = "F0D6F0"  # Week 3 pillar colour (light)
C_WEEK4_LT  = "F5F0D6"  # Week 4 pillar colour (light)

# Product/service area colours — one per pillar or product line
C_AREA_1    = "D6E8FF"  # e.g. Core Product
C_AREA_2    = "D6FFE8"  # e.g. Feature Set A
C_AREA_3    = "FFF0D6"  # e.g. Feature Set B
C_AREA_4    = "F0D6FF"  # e.g. Platform / Brand
C_VIDEO     = "E8F5E8"  # Soft green — video rows

C_WHITE     = "FFFFFF"
C_LIGHT     = "F8F8F8"
C_DARK_TXT  = "1A1A2E"
C_ACCENT_TXT= "C0500A"

# ─────────────────────────────────────────────────────────────────────
# STYLE HELPERS
# These three helpers + write_cell() do all the formatting work.
# ─────────────────────────────────────────────────────────────────────
def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def font(bold=False, size=10, color="1A1A2E", italic=False):
    return Font(name="Calibri", bold=bold, size=size, color=color, italic=italic)

def align(h="left", v="top", wrap=True):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

def thin_border():
    s = Side(style="thin", color="CCCCCC")
    return Border(left=s, right=s, top=s, bottom=s)

def write_cell(ws, row, col, value, bold=False, size=10, fg=C_DARK_TXT,
               bg=None, h="left", v="top", wrap=True, italic=False, border=True):
    cell = ws.cell(row=row, column=col, value=value)
    cell.font = font(bold=bold, size=size, color=fg, italic=italic)
    cell.alignment = align(h=h, v=v, wrap=wrap)
    if bg:
        cell.fill = fill(bg)
    if border:
        cell.border = thin_border()
    return cell

# ─────────────────────────────────────────────────────────────────────
# VIDEO SCRIPTS
# Claude writes one production-ready script per week.
# Each is stored as a module-level string constant and embedded in the
# post data + rendered in a dedicated Videos sheet.
#
# Script format is designed to be fed directly into AI video tools
# (Runway, Kling, Sora, HeyGen, etc.) with no further editing.
# ─────────────────────────────────────────────────────────────────────
VIDEO_1 = """\
DURATION: ~45 sec | FORMAT: Text-on-screen + AI voiceover
STYLE: Dark, minimal. White text on black. Accent colour highlights.
TONE: Provocative, calm — not salesy
MUSIC: Low ambient tension. No beat until the turn at 0:28.

[0:00–0:06] HOOK
VISUAL: Black screen. Single bold stat fades in.
ON-SCREEN: "[Attention-grabbing stat about the ICP's core problem]"
VO: "[Read the stat. Pause. Let it land.]"

[0:06–0:15] THE MARKET REALITY
VISUAL: Fast text cuts — three common claims competitors or the market makes.
ON-SCREEN: "[Claim 1]" / "[Claim 2]" / "[Claim 3]"
VO: "Everyone is promising [X]. Nobody is delivering [Y]."

[0:15–0:28] THE QUESTION
VISUAL: Slow fade to black. One line appears.
ON-SCREEN: "[The question that reframes the problem]"
VO: "[Voiceover that surfaces the gap — why the current approach is wrong]"

[0:28–0:38] THE REFRAME
VISUAL: Clean card with accent line left.
ON-SCREEN: "[The brand's core insight — one sentence]"
VO: "[Explain why the brand's approach is different and why it matters]"

[0:38–0:44] THE ANSWER
VISUAL: Brand wordmark fades in. Minimal.
ON-SCREEN: "[Brand name]. [Core value proposition — one line]."
VO: "[Read the CTA line. Calm. Confident.]"

[0:44–0:47] CLOSE
ON-SCREEN: "[brand website]"
VO: "Learn more at [brand website]."
"""

VIDEO_2 = """\
DURATION: ~50 sec | FORMAT: Split-screen comparison + AI voiceover
STYLE: Two-panel. Left = the old way (muted/red tint). Right = the new way (clean/white).
TONE: Educational, practitioner-level. No hype.
MUSIC: Neutral and clear. Slight tension left panel, resolution right.

[0:00–0:06] HOOK
VISUAL: Split screen appears instantly.
ON-SCREEN: "Two approaches. Same problem. Different outcomes."
VO: "Two approaches to [the ICP's core problem]. Watch what happens."

[0:06–0:18] THE OLD WAY
VISUAL: Left panel — chaotic, manual, slow.
ON-SCREEN (left): "[Old way label] — [what it looks like / feels like]"
VO: "The old way: [describe it in the ICP's language — the frustration, the waste, the risk]"

[0:18–0:34] THE NEW WAY
VISUAL: Right panel — clean, structured, fast.
ON-SCREEN (right): "[New way label] — [what it looks like / feels like]"
VO: "The new way: [describe the brand's approach — what it does differently, what the outcome is]"

[0:34–0:44] THE POINT
VISUAL: Panels merge. Single dark screen. Accent text.
ON-SCREEN: "[The core insight — one punchy sentence]"
VO: "[Reinforce the key difference. One sentence. No filler.]"

[0:44–0:50] CLOSE
VISUAL: Brand wordmark. Minimal.
ON-SCREEN: "[Brand tagline]. [brand website]"
VO: "[Brand name]. Built for [the ICP]."
"""

VIDEO_3 = """\
DURATION: ~50 sec | FORMAT: Human-led narrative + text cards
STYLE: Warm, empathetic — contrasts with the more assertive Week 1/2 tone.
       Mix of text-card animation and soft B-roll suggestions.
TONE: Honest, grounded. Speaks to the human doing the work, not just the buyer.
MUSIC: Quiet, resolving. Something that feels like a sigh of relief.

[0:00–0:07] OPENING — THE REALITY
VISUAL: Simple text card. Dark background. One fact.
ON-SCREEN: "[A number or fact that captures the ICP's daily reality]"
VO: "[Read the number or fact. Let it breathe.]"

[0:07–0:18] THE HUMAN COST
VISUAL: Quick cuts showing the repetitive, draining version of the work.
ON-SCREEN: "[What the ICP is doing instead of what they want to be doing]"
VO: "[Name the frustration. Be specific. This is the 'I feel seen' moment.]"

[0:18–0:30] THE SHIFT
VISUAL: Calmer scene — the contrast. The work done differently.
ON-SCREEN: "[What changes when the problem is solved]"
VO: "[Describe the better version of the work — still concrete, not abstract]"

[0:30–0:42] THE OUTCOME
VISUAL: Text cards — one stat or outcome per card.
ON-SCREEN: "[Outcome 1]" / "[Outcome 2]" / "[Outcome 3]"
VO: "[Read each outcome. Specific numbers preferred over vague claims.]"

[0:42–0:50] CLOSE
VISUAL: Brand wordmark + product/service name.
ON-SCREEN: "Meet [product name]. [brand website]"
VO: "[Product name]. For [ICP descriptor who deserves better]."
"""

VIDEO_4 = """\
DURATION: ~55 sec | FORMAT: Brand manifesto film
STYLE: Cinematic. Full dark aesthetic. Slow, deliberate cuts.
       This is the month's closing statement — a movement, not a product demo.
TONE: Authoritative, calm, earned. Not arrogant — earned confidence.
MUSIC: Builds slowly. Reaches a peak at 0:40, resolves quietly.

[0:00–0:08] OPENING STATEMENT
VISUAL: Pure black. Single line of white text. No logo yet.
ON-SCREEN: "[The market truth — the thing everyone knows but nobody says]"
VO: "[Read it. Pause.]"
ON-SCREEN: "[The consequence or gap that follows from that truth]"
VO: "[Read it. Another pause.]"

[0:08–0:20] THE EVIDENCE
VISUAL: Slow dissolve to data or activity — the scale of the problem.
ON-SCREEN: "[Stat 1]" / "[Stat 2]" / "[Stat 3]"
VO: "[Read each stat. These are the reasons the problem is real and urgent.]"

[0:20–0:34] THE TURN
VISUAL: Hard cut to clean, minimal. Brand accent appears. Structure.
ON-SCREEN: "The answer isn't [the wrong thing people are trying]."
VO: "The answer isn't [X]. It's [Y]. [Brief explanation of the brand's approach — transparent, reversible, accountable, scalable — whatever applies]."

[0:34–0:46] THE PLATFORM
VISUAL: Product areas or capabilities appear one by one — each snapping into place.
ON-SCREEN: "[Capability 1]" / "[Capability 2]" / "[Capability 3]" / "[Capability 4]"
VO: "[Brand name]. [How many capabilities/products]. [One-line description of what unifies them]."

[0:46–0:55] CLOSE
VISUAL: All elements resolve into the brand wordmark. Clean. Still. Confident.
ON-SCREEN: "[Brand tagline]."
        "[brand website]"
VO: "[Brand name]. [Tagline]."
"""

# ─────────────────────────────────────────────────────────────────────
# MEME CONCEPTS
# Claude populates this dict with meme formats for relevant social posts.
# Keys are post numbers (matching the num field in the posts list below).
# Video posts (nums 6, 12, 18, 24) are left out — they don't need memes.
#
# Each entry includes:
#   FORMAT: the meme template name
#   Panel descriptions: exactly what text goes in each panel
#   Caption: the line that appears below the meme image
#   STYLE: (optional) visual notes for the designer
# ─────────────────────────────────────────────────────────────────────
MEMES = {
    1: (
        "FORMAT: 'This is Fine' dog meme\n\n"
        "Classic burning-room panel.\n"
        "Fire label: '[Description of the uncontrolled problem happening in the background]'\n"
        "Dog label: '[ICP persona or company type]'\n"
        "Speech bubble: 'This is fine.'\n"
        "Caption: '[The insight — why this situation is not, in fact, fine]'\n"
        "STYLE: Dark bg, accent-colour fire glow, brand wordmark bottom-right."
    ),
    2: (
        "FORMAT: Gru's Plan (4-panel)\n\n"
        "Panel 1: '[Step 1 of the plan that sounds reasonable]' — Gru confident\n"
        "Panel 2: '[Step 2 — the obvious next step]' — Gru nodding\n"
        "Panel 3: '[The stat or reality that derails the plan]' — Gru reading paper, confused\n"
        "Panel 4: '[Repeat of Step 1]' — Gru horrified stare\n"
        "Caption: '[The lesson — what to do instead]'"
    ),
    3: (
        "FORMAT: Expanding Brain (4-panel)\n\n"
        "Dim brain: '[The obvious bad solution]'\n"
        "Medium glow: '[A slightly better but still wrong solution]'\n"
        "Bright brain: '[A good-sounding but still inadequate solution]'\n"
        "Galaxy brain: '[The brand's approach — the actual right answer]'\n"
        "Caption: '[Why the galaxy brain option is the right call]'"
    ),
    4: (
        "FORMAT: Drake Pointing\n\n"
        "Drake turns away (rejected): '[The thing the market/competitors are doing or claiming]'\n"
        "Drake points (approved): '[The brand's approach — the better alternative]'\n"
        "Caption: '[One-line insight that explains why the rejected thing is wrong]'"
    ),
    5: (
        "FORMAT: Anakin / Padme (4-panel)\n\n"
        "Panel 1 — Padme: '[Sets up the assumption — what people think is true]'\n"
        "Panel 2 — Anakin: [calm, confident silence]\n"
        "Panel 3 — Padme: '...[the follow-on assumption — the thing that turns out to be wrong]'\n"
        "Panel 4 — Padme: [blank thousand-yard stare]\n"
        "Caption: '[The stat or fact that reveals the reality]'"
    ),
    7: (
        "FORMAT: 'Always Has Been' (astronaut meme)\n\n"
        "Astronaut 1 (looking at Earth): 'Wait — [the thing they just realised is true / always was the case]?'\n"
        "Astronaut 2 (gun raised): 'Always has been.'\n"
        "Caption: '[The punchline insight]'\n"
        "STYLE: Dark space bg, accent colour on helmets, brand logo bottom-right."
    ),
    8: (
        "FORMAT: 'Two Buttons' (sweating businessman)\n\n"
        "Sweating man at panel, two glowing red buttons:\n"
        "Button 1: '[Option A — the fast/easy/tempting choice with a downside]'\n"
        "Button 2: '[Option B — the right choice that requires more effort]'\n"
        "Man: visibly sweating, hand hovering over both buttons\n"
        "Caption: '[ICP persona descriptor] in [year].'"
    ),
    9: (
        "FORMAT: 'One Does Not Simply' (Boromir, LOTR)\n\n"
        "Boromir at the council of Elrond, hands extended.\n"
        "Top text: 'One does not simply'\n"
        "Bottom text: '[The thing that sounds easy but clearly isn't — the ICP's real challenge]'\n"
        "Caption: '[The insight — what actually needs to happen instead]'"
    ),
    10: (
        "FORMAT: Anakin / Padme (4-panel)\n\n"
        "Panel 1 — Padme: '[Stat or claim that sounds promising]'\n"
        "Panel 2 — Anakin: [confident nod]\n"
        "Panel 3 — Padme: '...[the logical follow-on that turns out to not be true]'\n"
        "Panel 4 — Padme: [blank thousand-yard stare]\n"
        "Caption: '[The real number or reality that reveals the gap. Source attribution.]'"
    ),
    11: (
        "FORMAT: Drake Pointing\n\n"
        "Drake turns away: '[The thing most tools or teams stop at]'\n"
        "Drake points: '[What the brand does — the extra step that actually matters]'\n"
        "Caption: '[One-line insight explaining why the extra step is the whole point]'"
    ),
    13: (
        "FORMAT: 'This is Fine' dog meme\n\n"
        "Fire labels: '[Stat 1 showing the scale of the problem]' / '[Stat 2]' / '[Context label]'\n"
        "Dog label: '[ICP persona or team type]'\n"
        "Speech bubble: 'This is fine.'\n"
        "Caption: '[The reframe — why this is not a minor inconvenience but a real risk]'"
    ),
    14: (
        "FORMAT: Drake Pointing\n\n"
        "Drake turns away: '[The thing AI/automation/tools should NOT be doing autonomously]'\n"
        "Drake points: '[The correct split — what the tool handles vs what the human decides]'\n"
        "Caption: '[The principle that makes this split work]'"
    ),
    15: (
        "FORMAT: Gru's Plan (4-panel)\n\n"
        "Panel 1: '[The plan that sounds comprehensive]' — Gru confident\n"
        "Panel 2: '[The immediate result that seems good]' — Gru pleased\n"
        "Panel 3: '[The real constraint that ruins the plan]' — Gru reading report, horrified\n"
        "Panel 4: '[Repeat of Panel 1]' — Gru horrified stare\n"
        "Caption: '[The insight — the real problem the brand solves]'"
    ),
    16: (
        "FORMAT: 'Nobody / Absolutely Nobody' caption meme\n\n"
        "IMAGE: Person overwhelmed by the manual version of the ICP's recurring nightmare task\n"
        "Top caption: '[ICP team type] every [recurring time period]:'\n"
        "Nobody:\n"
        "Absolutely nobody:\n"
        "[ICP team]: '[Chaotic all-caps description of the panic that ensues]'\n"
        "Caption: '[The brand's answer — what it should look like instead]'"
    ),
    17: (
        "FORMAT: 'Change My Mind' (Steven Crowder at outdoor table)\n\n"
        "Man sitting at table, sign reading:\n"
        "'[A provocative but defensible claim about the market / ICP's situation]'\n"
        "Sub-text: 'Change My Mind.'\n"
        "Caption: '[The stat or source that backs the claim up]'"
    ),
    19: (
        "FORMAT: 'Always Has Been' (astronaut meme)\n\n"
        "Astronaut 1: 'Wait — [the thing competitors or the market are doing that sounds surprising once noticed]?'\n"
        "Astronaut 2 (gun raised): 'Always has been.'\n"
        "Caption: '[The brand's differentiation — what it does instead]'"
    ),
    20: (
        "FORMAT: Expanding Brain (4-panel)\n\n"
        "Dim brain: '[Naive solution — the first thing people try]'\n"
        "Medium glow: '[Slightly better solution — more resources, same approach]'\n"
        "Bright brain: '[Good-sounding but still incomplete solution]'\n"
        "Galaxy brain: '[The brand's solution — the approach that actually solves it at scale]'\n"
        "Caption: '[Why the galaxy brain option is the only one that compounds]'"
    ),
    21: (
        "FORMAT: Distracted Boyfriend\n\n"
        "Boyfriend label: '[ICP persona or buyer type]'\n"
        "Woman walking past (ignored): '[The old/slow/painful approach they've been using]'\n"
        "Woman he's staring at: '[The brand's product — faster, better, easier]'\n"
        "Caption: '[One-line payoff]'"
    ),
    22: (
        "FORMAT: Drake Pointing\n\n"
        "Drake turns away: '[The fragmented / disconnected version of the problem]'\n"
        "Drake points: '[The unified / connected / solved version the brand delivers]'\n"
        "Caption: '[The outcome that becomes possible when everything is connected]'"
    ),
    23: (
        "FORMAT: Gru's Plan (4-panel)\n\n"
        "Panel 1: '[The trend or behaviour everyone is doing]' — Gru confident\n"
        "Panel 2: '[The expected positive outcome]' — Gru thumbs up\n"
        "Panel 3: '[The uncomfortable reality stat that follows]' — Gru reading stat, wide-eyed\n"
        "Panel 4: '[Repeat of Panel 1]' — Gru horrified stare\n"
        "Caption: '[The reframe — the right approach vs the common one]'"
    ),
}

# ─────────────────────────────────────────────────────────────────────
# POST DATA
# Claude replaces all [placeholder] text below with real content
# derived from the approved narrative brief.
#
# Structure:
#   Posts 1–5:  Week 1 social posts
#   Post 6:     Week 1 video
#   Posts 7–11: Week 2 social posts
#   Post 12:    Week 2 video
#   Posts 13–17: Week 3 social posts
#   Post 18:    Week 3 video
#   Posts 19–23: Week 4 social posts
#   Post 24:    Week 4 video
# ─────────────────────────────────────────────────────────────────────
posts = [

  # ── WEEK 1 — [Pillar 1 Name] ──────────────────────────────────────

  {
    "num": 1, "week": 1, "pillar": "[Pillar 1 Name]",
    "date": "Mon 1 Jun", "topic": "[Post 1 Topic]",
    "teammate": "[Product Area 1]", "tm_color": C_AREA_1,
    "format": "Static Post",
    "hook": "[Scroll-stopping stat or claim — under 10 words]",
    "post_copy": (
        "[Bold headline — the one thing the visual says]\n\n"
        "[One supporting line that adds context or tension]"
    ),
    "carousel_slides": "",
    "video_script": "",
    "visual": "[Visual direction: background colour, layout, key text, brand element placement]",
    "meme_concept": MEMES.get(1, ""),
    "linkedin": "[LinkedIn caption — max 3 lines. 2–3 hashtags at end.]",
    "x": "[X caption — max 2 lines. Punchy. Often ends with a question.]",
    "instagram": "[Instagram caption — max 2 lines]\n\n[#hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5]",
    "facebook": "[Facebook caption — max 3 lines. Slightly more conversational.]",
    "reddit_sub": "r/[relevant subreddit]",
    "reddit": "[Value-first Reddit post — practitioner tone, no pitching. Ends with a genuine question.]",
  },

  {
    "num": 2, "week": 1, "pillar": "[Pillar 1 Name]",
    "date": "Tue 2 Jun", "topic": "[Post 2 Topic]",
    "teammate": "[Product Area 1]", "tm_color": C_AREA_1,
    "format": "Carousel (5 slides)",
    "hook": "[Hook for carousel — creates curiosity about what's inside]",
    "post_copy": (
        "[What the cover slide says — the promise of the carousel]\n\n"
        "[One line that makes them want to swipe]"
    ),
    "carousel_slides": (
        "Slide 1 (Cover):\n"
        "[Cover headline — mirrors the hook]\n\n"
        "Slide 2:\n"
        "[Slide 2 heading — first point]\n"
        "[Supporting detail — max 2 lines]\n\n"
        "Slide 3:\n"
        "[Slide 3 heading]\n"
        "[Supporting detail]\n\n"
        "Slide 4:\n"
        "[Slide 4 heading]\n"
        "[Supporting detail]\n\n"
        "Slide 5 (CTA):\n"
        "[Closing statement — the takeaway]\n\n"
        "[One-line CTA]\n"
        "[brand website]"
    ),
    "video_script": "",
    "visual": "[Visual direction for carousel: cover style, slide template, accent colour usage]",
    "meme_concept": MEMES.get(2, ""),
    "linkedin": "[LinkedIn caption — sets up the carousel. 2–3 hashtags.]",
    "x": "[X caption — teases the carousel content. No hashtags unless essential.]",
    "instagram": "[Instagram caption]\n\n[#hashtags]",
    "facebook": "[Facebook caption]",
    "reddit_sub": "r/[relevant subreddit]",
    "reddit": "[Reddit post]",
  },

  # ... (posts 3–5 follow the same pattern as posts 1–2)
  # Claude generates all 5 social posts + 1 video per week

  {
    "num": 6, "week": 1, "pillar": "[Pillar 1 Name]",
    "date": "Week 1 — Video", "topic": "[Video 1 Topic]",
    "teammate": "[Product Area]", "tm_color": C_AREA_1,
    "format": "Video Reel (<60 sec)",
    "hook": "[Video hook — the logline that appears in caption and captions the video]",
    "post_copy": (
        "[What the caption says above the video]\n\n"
        "[One or two lines that give context or add urgency]"
    ),
    "carousel_slides": "",
    "video_script": VIDEO_1,
    "visual": "[Visual direction for the video: style, pacing, aesthetic references]",
    "meme_concept": "",
    "linkedin": "[LinkedIn caption for the video post. Sets up why to watch it.]",
    "x": "[X caption — short, teases the content. Ends with [video].]",
    "instagram": "[Instagram caption]\n\n[#hashtags]",
    "facebook": "[Facebook caption — slightly warmer tone]",
    "reddit_sub": "r/[relevant subreddit]",
    "reddit": "[Reddit post framing the video as a discussion piece, not a promo]",
  },

  # ── WEEKS 2–4 follow the same structure ──────────────────────────
  # Claude generates weeks 2, 3, 4 with progressively stronger proof
  # and positioning, ending with brand authority and CTA in Week 4.
]

# ─────────────────────────────────────────────────────────────────────
# SHEET STRUCTURE
# Claude fills in the brand name, month, and narrative details below.
# ─────────────────────────────────────────────────────────────────────
WEEKS = {
    1: {"label": "Week 1 — [Pillar 1 Name]", "color": C_WEEK1_LT, "hdr": "1A2A3A"},
    2: {"label": "Week 2 — [Pillar 2 Name]", "color": C_WEEK2_LT, "hdr": "1A3A1A"},
    3: {"label": "Week 3 — [Pillar 3 Name]", "color": C_WEEK3_LT, "hdr": "2A1A3A"},
    4: {"label": "Week 4 — [Pillar 4 Name]", "color": C_WEEK4_LT, "hdr": "3A3A1A"},
}

# ─────────────────────────────────────────────────────────────────────
# SHEET 1 — OVERVIEW
# ─────────────────────────────────────────────────────────────────────
ws_ov = wb.active
ws_ov.title = "Overview"
ws_ov.sheet_view.showGridLines = False

ws_ov.merge_cells("A1:J1")
c = ws_ov["A1"]
c.value = "[Brand Name] — [Month Year] Social Media Calendar"
c.font = Font(name="Calibri", bold=True, size=18, color=C_WHITE)
c.fill = fill(C_BG)
c.alignment = align(h="center", v="center")
c.border = thin_border()
ws_ov.row_dimensions[1].height = 40

ws_ov.merge_cells("A2:J2")
c = ws_ov["A2"]
c.value = (
    "Narrative: \"[Monthly narrative theme]\"  |  "
    "5 posts + 1 video/week  |  24 pieces total  |  "
    "Built with social-calendar-skill"
)
c.font = Font(name="Calibri", size=10, color=C_ACCENT, italic=True)
c.fill = fill("1A1A28")
c.alignment = align(h="center", v="center")
ws_ov.row_dimensions[2].height = 22
ws_ov.row_dimensions[3].height = 10

pillars = [
    ("Pillar 1", "[Pillar 1 Name]", "Week 1", "5+1", C_WEEK1_LT),
    ("Pillar 2", "[Pillar 2 Name]", "Week 2", "5+1", C_WEEK2_LT),
    ("Pillar 3", "[Pillar 3 Name]", "Week 3", "5+1", C_WEEK3_LT),
    ("Pillar 4", "[Pillar 4 Name]", "Week 4", "5+1", C_WEEK4_LT),
]
for ci, h in enumerate(["Pillar", "Theme", "Week", "Posts (social+video)", ""], 1):
    write_cell(ws_ov, 4, ci, h, bold=True, fg=C_WHITE, bg=C_BG, size=10, h="center")
for ri, (p, t, w, ct, clr) in enumerate(pillars, 5):
    write_cell(ws_ov, ri, 1, p,  bold=True, bg=clr, fg=C_DARK_TXT, h="center")
    write_cell(ws_ov, ri, 2, t,  bg=clr,    fg=C_DARK_TXT)
    write_cell(ws_ov, ri, 3, w,  bg=clr,    fg=C_DARK_TXT, h="center")
    write_cell(ws_ov, ri, 4, ct, bg=clr,    fg=C_DARK_TXT, h="center")
    ws_ov.row_dimensions[ri].height = 22

ws_ov.row_dimensions[9].height = 10

legend = [
    ("[Product Area 1]",    C_AREA_1),
    ("[Product Area 2]",    C_AREA_2),
    ("[Product Area 3]",    C_AREA_3),
    ("[Brand / Platform]",  C_AREA_4),
    ("Video Reel (<60 sec)", C_VIDEO),
]
ws_ov.merge_cells("A10:D10")
c = ws_ov["A10"]
c.value = "PRODUCT AREA / FORMAT LEGEND"
c.font = Font(name="Calibri", bold=True, size=10, color=C_WHITE)
c.fill = fill(C_BG)
c.alignment = align(h="center", v="center", wrap=False)
ws_ov.row_dimensions[10].height = 20

for ri, (tm, clr) in enumerate(legend, 11):
    write_cell(ws_ov, ri, 1, tm, bold=True, bg=clr, fg=C_DARK_TXT)
    ws_ov.merge_cells(f"A{ri}:D{ri}")
    ws_ov.row_dimensions[ri].height = 18

for col, width in zip("ABCDEFGHIJ", [18, 45, 12, 14, 20, 20, 20, 20, 20, 20]):
    ws_ov.column_dimensions[col].width = width

# ─────────────────────────────────────────────────────────────────────
# SHEET 2 — FULL CALENDAR
# All 24 posts in one scrollable view, 19 columns wide.
# ─────────────────────────────────────────────────────────────────────
ws_cal = wb.create_sheet("Full Calendar")
ws_cal.sheet_view.showGridLines = False

COLS = [
    "#", "Week", "Date", "Pillar", "Teammate", "Topic", "Format",
    "Hook", "Post Copy (Creative)", "Carousel Slides", "Video Script",
    "Visual Direction",
    "LinkedIn Caption", "X Caption", "Instagram Caption",
    "Facebook Caption", "Reddit Subreddit", "Reddit Caption",
    "Meme Concept"
]
COL_WIDTHS = [4, 6, 16, 24, 22, 26, 18, 36, 38, 50, 60, 34, 42, 32, 42, 42, 16, 42, 42]

ws_cal.merge_cells(f"A1:{get_column_letter(len(COLS))}1")
c = ws_cal["A1"]
c.value = "[Brand Name] — [Month Year] Full Social Media Calendar (24 pieces: 20 posts + 4 videos)"
c.font = Font(name="Calibri", bold=True, size=14, color=C_WHITE)
c.fill = fill(C_BG)
c.alignment = align(h="center", v="center")
ws_cal.row_dimensions[1].height = 32

for ci, h in enumerate(COLS, 1):
    cell = ws_cal.cell(row=2, column=ci, value=h)
    cell.font = Font(name="Calibri", bold=True, size=9, color=C_WHITE)
    cell.fill = fill(C_ACCENT)
    cell.alignment = align(h="center", v="center", wrap=True)
    cell.border = thin_border()
ws_cal.row_dimensions[2].height = 28

for ri, p in enumerate(posts, 3):
    week_clr = WEEKS[p["week"]]["color"]
    tm_clr   = p["tm_color"]
    is_video = "Video" in p["format"]
    vals = [
        p["num"], p["week"], p["date"], p["pillar"], p["teammate"], p["topic"],
        p["format"], p["hook"], p["post_copy"], p["carousel_slides"], p["video_script"],
        p["visual"],
        p["linkedin"], p["x"], p["instagram"], p["facebook"],
        p["reddit_sub"], p["reddit"], MEMES.get(p["num"], "")
    ]
    for ci, val in enumerate(vals, 1):
        cell = ws_cal.cell(row=ri, column=ci, value=val)
        cell.alignment = align(v="top", wrap=True)
        cell.border = thin_border()
        cell.font = Font(name="Calibri", size=9, color=C_DARK_TXT)
        if is_video:
            if ci == 5:
                cell.fill = fill(tm_clr)
                cell.font = Font(name="Calibri", size=9, bold=True, color=C_DARK_TXT)
            elif ci == 7:
                cell.fill = fill("B8E6B8")
                cell.font = Font(name="Calibri", size=9, bold=True, color="1A3A1A")
            elif ci == 11:
                cell.fill = fill("F0FFF0")
                cell.font = Font(name="Calibri", size=8, color="1A3A1A")
            else:
                cell.fill = fill(C_VIDEO if ci not in [1,2,3,4] else week_clr)
        else:
            if ci == 5:
                cell.fill = fill(tm_clr)
                cell.font = Font(name="Calibri", size=9, bold=True, color=C_DARK_TXT)
            elif ci in [1, 2, 3, 4]:
                cell.fill = fill(week_clr)
                if ci == 4:
                    cell.font = Font(name="Calibri", size=9, bold=True, italic=True, color=C_DARK_TXT)
            elif ci == 7:
                fmt_clr = "D6FFE8" if "Carousel" in str(val) else "D6E8FF"
                cell.fill = fill(fmt_clr)
                cell.font = Font(name="Calibri", size=9, bold=True, color=C_DARK_TXT)
            elif ci == 8:  # Hook
                cell.fill = fill("FFF8F0")
                cell.font = Font(name="Calibri", size=9, bold=True, color=C_ACCENT_TXT)
            elif ci == 9:  # Post copy
                cell.fill = fill("FFFDF7")
            elif ci == 10:  # Carousel slides
                cell.fill = fill("F0F8FF")
                cell.font = Font(name="Calibri", size=8, color="1A3A5A")
            elif ci == 11:  # Video script
                cell.fill = fill("F8FFF8")
            elif ci == 19:  # Meme concept
                cell.fill = fill("F0EEFF")
                cell.font = Font(name="Calibri", size=8, color="3A1A5A")
            else:
                cell.fill = fill(C_LIGHT if ri % 2 == 0 else C_WHITE)

    if is_video:
        ws_cal.row_dimensions[ri].height = 220
    elif p["carousel_slides"]:
        ws_cal.row_dimensions[ri].height = 160
    else:
        ws_cal.row_dimensions[ri].height = 90

for ci, w in enumerate(COL_WIDTHS, 1):
    ws_cal.column_dimensions[get_column_letter(ci)].width = w
ws_cal.freeze_panes = "A3"

# ─────────────────────────────────────────────────────────────────────
# SHEET 3 — VIDEOS (dedicated wide-format script sheet)
# ─────────────────────────────────────────────────────────────────────
ws_vid = wb.create_sheet("Videos")
ws_vid.sheet_view.showGridLines = False

ws_vid.merge_cells("A1:G1")
c = ws_vid["A1"]
c.value = "[Brand Name] — [Month Year] Video Reels (4 videos, one per week, <60 sec each)"
c.font = Font(name="Calibri", bold=True, size=14, color=C_WHITE)
c.fill = fill(C_BG)
c.alignment = align(h="center", v="center")
c.border = thin_border()
ws_vid.row_dimensions[1].height = 32

VID_COLS = ["#", "Week", "Topic", "Hook / Logline", "Post Copy", "LinkedIn Caption", "Production Script"]
VID_WIDTHS = [4, 8, 28, 38, 38, 48, 90]

for ci, h in enumerate(VID_COLS, 1):
    cell = ws_vid.cell(row=2, column=ci, value=h)
    cell.font = Font(name="Calibri", bold=True, size=9, color=C_WHITE)
    cell.fill = fill(C_ACCENT)
    cell.alignment = align(h="center", v="center", wrap=True)
    cell.border = thin_border()
ws_vid.row_dimensions[2].height = 24

video_posts = [p for p in posts if "Video" in p["format"]]
for ri, p in enumerate(video_posts, 3):
    vals = [p["num"], p["week"], p["topic"], p["hook"], p["post_copy"],
            p["linkedin"], p["video_script"]]
    for ci, val in enumerate(vals, 1):
        cell = ws_vid.cell(row=ri, column=ci, value=val)
        cell.alignment = align(v="top", wrap=True)
        cell.border = thin_border()
        cell.font = Font(name="Calibri", size=9, color=C_DARK_TXT)
        if ci in [1, 2]:
            cell.fill = fill(WEEKS[p["week"]]["color"])
        elif ci == 4:
            cell.fill = fill("FFF8F0")
            cell.font = Font(name="Calibri", size=9, bold=True, color=C_ACCENT_TXT)
        elif ci == 7:
            cell.fill = fill("F0FFF0")
            cell.font = Font(name="Calibri", size=8, color="1A3A1A")
        else:
            cell.fill = fill(C_VIDEO)
    ws_vid.row_dimensions[ri].height = 320

for ci, w in enumerate(VID_WIDTHS, 1):
    ws_vid.column_dimensions[get_column_letter(ci)].width = w
ws_vid.freeze_panes = "A3"

# ─────────────────────────────────────────────────────────────────────
# SHEETS 4–7 — ONE SHEET PER WEEK
# Each week gets its own sheet for easy team handoff.
# ─────────────────────────────────────────────────────────────────────
WEEK_COLS = [
    "#", "Date", "Teammate", "Topic", "Format",
    "Hook", "Post Copy (Creative)", "Carousel Slides", "Video Script",
    "LinkedIn Caption", "X Caption", "Instagram Caption",
    "Facebook Caption", "Reddit Sub", "Reddit Caption",
    "Visual Direction", "Meme Concept"
]
WEEK_COL_W = [4, 16, 22, 26, 18, 34, 38, 50, 60, 42, 32, 42, 42, 14, 42, 34, 42]

for wk in [1, 2, 3, 4]:
    wk_info  = WEEKS[wk]
    wk_posts = [p for p in posts if p["week"] == wk]
    ws       = wb.create_sheet(f"Week {wk}")
    ws.sheet_view.showGridLines = False

    ws.merge_cells(f"A1:{get_column_letter(len(WEEK_COLS))}1")
    c = ws["A1"]
    c.value = f"[Brand Name] — [Month Year] | {wk_info['label']}"
    c.font = Font(name="Calibri", bold=True, size=13, color=C_WHITE)
    c.fill = fill(C_BG)
    c.alignment = align(h="center", v="center")
    ws.row_dimensions[1].height = 30

    for ci, h in enumerate(WEEK_COLS, 1):
        cell = ws.cell(row=2, column=ci, value=h)
        cell.font = Font(name="Calibri", bold=True, size=9, color=C_WHITE)
        cell.fill = fill(C_ACCENT)
        cell.alignment = align(h="center", v="center", wrap=True)
        cell.border = thin_border()
    ws.row_dimensions[2].height = 24

    for ri, p in enumerate(wk_posts, 3):
        tm_clr  = p["tm_color"]
        row_bg  = wk_info["color"]
        is_video = "Video" in p["format"]
        vals = [
            p["num"], p["date"], p["teammate"], p["topic"],
            p["format"], p["hook"],
            p["post_copy"], p["carousel_slides"], p["video_script"],
            p["linkedin"], p["x"], p["instagram"], p["facebook"],
            p["reddit_sub"], p["reddit"], p["visual"], MEMES.get(p["num"], "")
        ]
        for ci, val in enumerate(vals, 1):
            cell = ws.cell(row=ri, column=ci, value=val)
            cell.alignment = align(v="top", wrap=True)
            cell.border = thin_border()
            cell.font = Font(name="Calibri", size=9, color=C_DARK_TXT)
            if is_video:
                if ci == 3:
                    cell.fill = fill(tm_clr)
                    cell.font = Font(name="Calibri", size=9, bold=True, color=C_DARK_TXT)
                elif ci == 5:
                    cell.fill = fill("B8E6B8")
                    cell.font = Font(name="Calibri", size=9, bold=True, color="1A3A1A")
                elif ci == 9:
                    cell.fill = fill("F0FFF0")
                    cell.font = Font(name="Calibri", size=8, color="1A3A1A")
                else:
                    cell.fill = fill(C_VIDEO if ci not in [1, 2] else row_bg)
            else:
                if ci == 3:
                    cell.fill = fill(tm_clr)
                    cell.font = Font(name="Calibri", size=9, bold=True, color=C_DARK_TXT)
                elif ci == 5:
                    fmt_clr = "D6FFE8" if "Carousel" in str(val) else "D6E8FF"
                    cell.fill = fill(fmt_clr)
                    cell.font = Font(name="Calibri", size=9, bold=True, color=C_DARK_TXT)
                elif ci == 6:  # Hook
                    cell.fill = fill("FFF8F0")
                    cell.font = Font(name="Calibri", size=9, bold=True, color=C_ACCENT_TXT)
                elif ci == 7:  # Post copy
                    cell.fill = fill("FFFDF7")
                elif ci == 8:  # Carousel slides
                    cell.fill = fill("F0F8FF")
                    cell.font = Font(name="Calibri", size=8, color="1A3A5A")
                elif ci == 9:  # Video script
                    cell.fill = fill("F8FFF8")
                elif ci in [1, 2]:
                    cell.fill = fill(row_bg)
                elif ci == 17:  # Meme concept
                    cell.fill = fill("F0EEFF")
                    cell.font = Font(name="Calibri", size=8, color="3A1A5A")
                else:
                    cell.fill = fill(C_LIGHT if ri % 2 == 0 else C_WHITE)

        if is_video:
            ws.row_dimensions[ri].height = 280
        elif p["carousel_slides"]:
            ws.row_dimensions[ri].height = 180
        else:
            ws.row_dimensions[ri].height = 100

    for ci, w in enumerate(WEEK_COL_W, 1):
        ws.column_dimensions[get_column_letter(ci)].width = w
    ws.freeze_panes = "A3"

# ─────────────────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────────────────
BRAND_NAME   = "AcmeCorp"
TARGET_MONTH = "June-2026"
OUTPUT_DIR   = os.path.expanduser(f"~/Documents/{BRAND_NAME}/calendars")

os.makedirs(OUTPUT_DIR, exist_ok=True)
out = f"{OUTPUT_DIR}/{TARGET_MONTH}-Social-Calendar.xlsx"
wb.save(out)
print(f"SAVED: {out}")
