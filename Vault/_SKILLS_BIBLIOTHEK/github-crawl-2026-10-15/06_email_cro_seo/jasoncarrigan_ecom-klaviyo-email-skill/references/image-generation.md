# Generating the email hero with Nano Banana Pro (via Higgsfield)

The email needs **one** strong hero image — a branded lifestyle shot, not a plain product-on-white. The real product
photo is a non-negotiable reference so the product renders accurately. Model: `nano_banana_pro` (Google's Nano Banana —
image-to-image, up to 4K), run through the **Higgsfield MCP connector** — no API key.

## The one rule that matters most

**The real product photo (from Phase 2) is the first reference image in the generation call.** Without it the model
invents the packaging/shape. Tell the model explicitly in the prompt:

> "REFERENCE IMAGE 1 is the ACTUAL product. Reproduce it with photographic accuracy — exact shape, materials, colors,
> branding, and any text/logos must match. Do not redesign it."

Add 1–2 style references (from Tavily) as REFERENCE IMAGE 2, 3 to anchor the mood and color world.

## How to write the prompt

Nano Banana rewards narrative, art-direction prompts — brief it like a creative director on a real shoot, not a keyword
list.

1. **Role-set** — "You are a world-class commercial photographer and art director shooting a hero image for a premium
   [brand] email campaign."
2. **Lead with the concept** — one sentence describing the scene and the feeling, tied to the email's angle.
3. **Commit to the brand color world** — name the exact brand hex and command the scene to live in it (props,
   background, lighting), with the product as the focal contrast.
4. **Camera + lens** for photographic control — e.g. lifestyle/set: "Fujifilm GFX 100S, 80mm f/1.7, medium format";
   product macro: "Canon EOS R5, 100mm macro, f/2.8".
5. **Lighting as mood** — "soft diffused editorial light" / "warm golden-hour outdoor light" / "bright even Apple-style
   product light," matched to the brand tone.
6. **Texture callouts** — real materials, legible product label, true-to-life surfaces.
7. **People, if any** — cast and wardrobe inside the brand world and the ICP; direct genuine emotion ("mid-laugh, eyes
   crinkled — not a stock smile"), never a forced pose.
8. **Composition for email** — wide hero framing (≈1200×600), product clearly placed, and **leave clean negative space
   where the HTML headline/CTA will sit** (remember: no baked-in text — keep the image text-free).
9. **Label the references** — "REFERENCE 1: actual product, match exactly. REFERENCE 2: aesthetic/style I want."
10. **Anti-generic close** — "This must not look like a generic stock photo or a product-on-countertop shot. It should
    look like a bold, high-budget brand campaign."

## Tool flow (Higgsfield)

No REST call and no key — generate through the Higgsfield MCP tools:

1. **Turn each reference into a Higgsfield `media_id`.** Product photo first: `media_import_url` if you have its web URL,
   otherwise `media_upload` for the local `email-workspace/RUN/images/product-original.png`. Same for the optional style
   reference(s).
2. **Call `generate_image`** with:
   - `model`: `"nano_banana_pro"`
   - `prompt`: your art-directed prompt above, with the reference labels.
   - `medias`: the product `media_id` **first**, then style — each `{ "value": "<media_id>", "role": "image" }`. The
     product photo is always first; it's the locked reference that keeps the product accurate.
   - `params`: `aspect_ratio "16:9"` (wide hero) and `resolution "2k"`.
3. **Retrieve** — poll `job_status` until the job completes, then pull the image via `reveal_generation` and save it to
   `email-workspace/RUN/images/hero.png`.

After generating, **host the hero** (Klaviyo image upload — see `klaviyo-deploy.md`) and use the returned URL in the
HTML. Tool names/params evolve; if a call is rejected, call `models_explore` (`action: get`, `model_id: nano_banana_pro`)
to check the current `medias` roles and `aspect_ratios`, then adjust — the workflow (product-as-first-reference →
art-directed prompt → host → embed) stays the same. Preflight credit cost anytime with `generate_image` + `get_cost: true`.

If the Higgsfield connector isn't available, skip the hero, use a strong real product photo in its place, and tell the user.
