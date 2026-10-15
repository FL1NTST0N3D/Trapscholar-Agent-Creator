# 626 Labs POD Pipeline

A print-on-demand pipeline that runs a real merch shop: concept → AI-generated art → QA → background removal → text compositing → variant matrix → Printify → live Etsy listing. All Python scripts and a JSON catalog — no app server, no build step, no framework.

The designs it produces ship at [**Conundrum by Este**](https://www.etsy.com/shop/ConundrumByEste), the 626 Labs merch line.

<p align="center">
  <img src="showcase/the_audacity_cat.png" width="260" alt="The Audacity — cat design">
  <img src="showcase/meeting_email_frog.png" width="260" alt="This Meeting Could Have Been An Email — frog design">
  <img src="showcase/not_my_problem_penguin.png" width="260" alt="Not My Problem — penguin design">
</p>

## The pipeline

```
CONCEPT -> GENERATE (Gemini, no text) -> QA (AI-slop filter) -> BG REMOVE -> TEXT COMPOSITE (PIL)
        -> VARIANT MATRIX (5-10 SKUs/base) -> UPLOAD (curl) -> CREATE PRODUCT -> PUBLISH (gated)
```

Nine stages, and the interesting engineering is in the rules between them:

- **The model never writes the words.** Every generation prompt includes "no text"; type is composited afterward with PIL. AI-rendered text is gibberish often enough that the only winning move is not to play. Fonts, stroke, and layout stay deterministic and reusable.
- **Every image passes an AI-slop QA gate.** Extra limbs, melted faces, leaked gibberish, artifact objects — a checklist runs against every generation, and failures get regenerated with a tighter prompt, not shipped.
- **One artwork becomes 5-10 SKUs.** Transparent cutout, pattern combos, text variants, hat panels — the variant matrix multiplies each concept before any new art is generated. Catalog width without catalog cost.
- **Background removal is classical CV, not a model.** `bgremove.py` does corner-sampled color keying, GrabCut, contour matting, and alpha unmixing across six modes. Deterministic, fast, free, and it preserves interior transparency (negative space matters when the design floats on a shirt).
- **Typography is a generator, not a hand-placement.** `city_nickname_art.py` auto-fits fill-the-box lockups to ~86% panel width with controlled shadow. It exists because hand-placed type shipped a broken design once; now the lesson is enforced.

<p align="center">
  <img src="showcase/panther_city_lockup.png" width="200" alt="Panther City typographic lockup">
  <img src="showcase/funky_town_lockup.png" width="200" alt="Funky Town typographic lockup">
  <img src="showcase/buy_a_boat_hat_panel.png" width="420" alt="I Should Buy A Boat — hat panel layout">
</p>

## The safety model

Publishing is human-gated, and the gates live **in code**, not in documentation:

- `pod build` forces `--no-publish` and strips `--auto-publish`. It cannot go live.
- `pod draft` / `pod deploy` / `pod reassess` default to plan/dry-run modes that touch no write endpoint.
- `pod ship publish` is the primary route to the live store, and it walks drafts one at a time behind a per-product y/n confirm. The one other write path — `pod deploy execute --republish`, which re-pushes art to already-live products — sits behind its own typed-CONFIRM gate.

The dispatcher (`pod.py`) enforces all of this before any child script runs, so a typo can't publish a product.

## Hard-won operational notes

- **Printify's image-upload endpoint Cloudflare-blocks `requests`/`urllib`.** Uploads shell out to `curl`, with the base64 payload written to a temp file to dodge argv length limits. Every other endpoint works fine with `requests`. This cost an afternoon; take it for free.
- **Rate limits are respected by design**: 3-5s between uploads, 5-10s between publishes.
- **The Gemini model here is the analysis model.** `gemini_agent.py` runs text/vision (listing copy, QA verdicts) on a cheap flash model. Image *generation* uses a separate image model in an unshipped step — the generation prompt templates are the taste layer and stay private.
- **Secrets never live in the tree.** `pod_secrets.py` resolves credentials from the OS credential manager (`keyring`) first, with env-var fallback. There is no secrets file to leak.

## Repo tour

| Path | What it is |
|---|---|
| `pod.py` | Single entry point — `pod <verb>` dispatches everything with safe defaults enforced in code |
| `create_product.py` | Image + product type + title → Printify product (always a draft) |
| `generate.py` | Product-art generator: art + procedural background + text → sock/hat/tote panels |
| `bgremove.py` | Six-mode classical-CV background remover |
| `gemini_agent.py` | Gemini text/vision client: artwork analysis → listing copy, tags, color recommendations |
| `qa.py` | AI-slop QA pass over generated art |
| `city_nickname_art.py` | Fill-the-box typographic lockup generator |
| `inventory.py` / `batch_draft.py` | Backlog scan → bulk draft creation |
| `ship.py` | Draft review gallery + the gated publish path |
| `deploy_redesigns.py` / `manage_listings.py` | Push art redesigns to live products; execute repricing/cuts |
| `build_rich_backgrounds.py` / `gen_procedural_bgs.py` | Procedural background builders (PIL + numpy) |
| `remy/` | The in-house designer skill: persona, product matrix, pipeline reference |
| `fonts/` | SIL OFL typefaces used by the compositor (license texts included) |
| `POD_DESIGN_PIPELINE.md` | The canonical stage-by-stage pipeline doc |
| `UPGRADE_ROADMAP.md` | How this matured from a whim into a machine |

## Running it

Python 3.11+.

```
pip install -r requirements.txt
python pod_secrets.py set PRINTIFY_TOKEN   # stored via OS credential manager
python pod_secrets.py set PRINTIFY_SHOP_ID
python pod_secrets.py set GEMINI_API_KEY
python pod_secrets.py                      # presence check

python pod.py                              # list verbs
python pod.py inventory                    # what's live vs backlog (read-only)
python gen_procedural_bgs.py               # one-time: build the procedural backgrounds
python pod.py gen socks                    # composite product art, local only
                                           #   (bring your own source art — the shop's
                                           #    artwork isn't part of this repo)
python pod.py cut art.png                  # background removal
python pod.py build art.png tee "Title"    # create ONE product, as a draft
python pod.py ship review                  # HTML gallery of drafts
```

Everything that could touch the live store dry-runs by default. You have to mean it.

## License

Dual-licensed — see [LICENSE](LICENSE):

- **Code:** MIT. Learn from it, fork it, run your own machine.
- **Artwork, designs, and brand marks** (including everything in `showcase/`): all rights reserved. Not for reproduction or resale — putting these designs on merchandise is expressly prohibited.

---

Built by [626 Labs](https://626labs.dev). The shop: [**Conundrum by Este** on Etsy](https://www.etsy.com/shop/ConundrumByEste).
