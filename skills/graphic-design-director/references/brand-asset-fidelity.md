# Brand asset fidelity — approval gate for branded design

## Why this module exists

A generated logo that *resembles* the client's brand is **not** the client's logo. Visual approximation can alter signature geometry, negative space, custom letterforms and trademark identity. This Pickam/WAKU live case caught a generated rounded-square lime **p** substituted for the supplied pin-shaped organic **p** mark. Attractive packaging, correct dimensions and a green palette did **not** make the incorrect logo acceptable.

## Source hierarchy and permissions

1. **Approved production artwork** (vector SVG/PDF/AI/EPS, transparent high-resolution PNG, official brand kit): use the **actual supplied file** for marks, wordmarks, lockups, patterns and sanctioned variants. Do not ask an image generator to redraw logos. Use available compositing/vector-layout tools to place it.
2. **User-supplied flattened moodboard:** study and compare; if a separate logo file is unavailable, a direct *raster-derived* crop/mask may be used for **provisional proofing only**. Preserve original source pixels where feasible; do not claim to have recovered a true vector or certified a trademark. Disclose interpolation, background extraction and resolution limits.
3. **AI-generated logo approximation:** may be exploratory concept art when authorized; it is **not** an approved replacement for an existing brand logo. Mark as failed/unverified for client-ready production.

Do not publish or embed third-party/user brand files into public skill repositories by default. Keep any supplied client identity files outside the generic skill package unless the user explicitly authorizes redistribution.

## Visual identity QA — compare source to output at matched visible size

- **Symbol silhouette:** exact contour, asymmetry, proportions, stroke shape, termini and use of negative space/counters.
- **Wordmark:** custom glyph shapes, `i` dot, `p` bowl, `k` diagonals, `a` counter, terminal details, word spacing and baseline alignment.
- **Lockup:** symbol-to-wordmark orientation, relative scale, separation, tagline position and clearspace. Reflow only if the brief authorizes a different lockup and preserve original component artwork.
- **Palette:** approved HEX values in explicitly flat fields, primary/accent/semantic color role; photos and textured regions need separate visual inspection.
- **Application:** do not accept invented branded marks on clothing, vehicles, boxes or devices just because they are small or in perspective; inspect at 100% and, if necessary, composite official decals with perspective correction.
- **Deliverability:** exact resolution and legible copy; vector/transparent logo provenance when required; verify rights and font access where relevant.

## Decision logic

**PASS—source verified:** approved logo vector/raster is placed from the approved asset and visually inspected, with sufficient resolution and authorized lockup changes.

**PROVISIONAL—raster reconstructed:** original available only embedded in a moodboard. Identity is closer than AI redraw, but source resolution and masking artifacts may remain. Not a verified master logo or print-ready brand asset.

**FAIL—fabricated:** generated shape/wordmark differs in silhouette, glyph construction or proportions from authoritative asset. Do not present as brand-compliant.

**UNVERIFIED—hidden/small/perspective:** embedded photo applications cannot be confidently compared or no official asset supplied. Flag separately; do not silently pass by inference.

## Repair workflow

1. Identify source and destination logo locations. Compare against actual provided pixels, not an imagined brand standard.
2. If production logo is available, replace AI logo with supplied artwork in a layout editor or composite; never redraw.
3. If only moodboard pixels exist, raster-extract with appropriate alpha/edge checks **only as a disclosed proof** and compare the extracted mark to the source crop.
4. Visually inspect anti-aliasing and edge quality. If the extraction is jagged or tiny, revert to a readable source crop or request production asset; do not fake sharpness with generative rewriting.
5. Log all generated-logo appearances still in product imagery as not verified.
6. For flat swatches, measure their actual pixels independently of printed HEX labels: a label can read `#0E4B38` while the fill is a different color.
7. Revalidate the export, record the result and do not grant full approval until each required logo instance passes.

## Pickam regression case

- Source: user-provided **Pickam Bike Truck Brand Moodboard.png** (flattened raster; no separate official vector supplied in the task).
- Wrong output: first large logo changed into rounded-square app-like emblem and approximate wordmark.
- Source-derived fix: extract the pin-shaped mark and custom wordmark from the moodboard as raster and rearrange into a stacked logo lockup appropriate to the source layout. This is a **provisional adaptation** rather than a master identity certification.
- Brand swatches: Forest `#0E4B38`, Route Lime `#C4EE3A`, Paper `#F6F5EC`, Mist `#E1EDD4`, Ink `#101512`, Load Orange `#FF6A13`; Alert Red `#E5301F` is not a dominant panel color.
- Remaining risk: AI-generated logo decals on vehicles, packaging, hats and inside the phone preview. Do not call the composition wholly brand-verified until these are checked against approved assets.
