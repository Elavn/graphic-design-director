# Replication & adaptation protocol

## First inspect the source at full size

Extract a source map with normalized coordinates (0–100% of width/height); do not rely on vague mood words.

1. **Canvas:** aspect, safe boundaries, background treatment, transparent/solid, intended medium.
2. **Zone map:** hero object boundaries, center of visual mass, negative-space regions, headline region, supporting elements and the dominant diagonal/axis.
3. **Scale relationships:** approximate ratios (hero width, type-to-hero size, gap ratios, label size, margins).
4. **Typography:** exact text where supplied, font anatomy/family likeness, sizes/weight, tracking, line breaks, baseline and alignment.
5. **Palette:** background/foreground/accent colors and relative luminance, not just color adjectives.
6. **Art treatment:** flat/photographic/3D/painted/collage, lighting, shadows, texture and edge behavior.
7. **Reference intent:** what creates the emotional or conceptual effect; what information is external site chrome?
8. **Change list:** what must change, what must remain, what cannot be reproduced faithfully without source assets.

## Execute by mode

**REPLICATE:** keep layout, scale, color, material and wording, to the extent authorized and technically possible. Prefer direct edit/compositing of user-provided art or careful vector re-typesetting when exact text required. Don't add design garnish.

**ADAPT:** freeze source geometry and visual language, apply a minimal-diff edit list. If replacement text grows or subject dimensions differ, reflow **locally** while protecting dominant hierarchy and negative space. Don't let a new asset erase the original visual logic.

**INSPIRE:** do *not* try for pixel similarity; transfer requested design mechanisms, not the source's exact identity. Choose a genuinely different hero arrangement, content and meaningful concept unless instructed otherwise.

**HYBRID:** reconstruct locked reference elements; honor user's new prohibitions and subject swaps even where they require an intentional divergence. Record that divergence.

## Renderer selection by requirement

- Text precision and branded marks: vector/typeset overlay is usually more controllable than raster generation.
- Tight composition and original source supplied: edit existing image when available; otherwise reconstruct in layers, verify placement.
- Flat vector/no gradients/no 3D: prefer vector shapes, flat fills, flat illustration or a tightly locked suitable renderer. Realistic CGI is **not** a faithful substitute.
- Photo or cinematic light specified: use consistent lens, shadows, light and material behavior; don't enforce flatness.
- When a renderer repeatedly adds forbidden features, switch to a different method; do not declare failure resolved by a more elaborate prompt alone.

## Visual-fidelity checklist

| Criterion | Compare source ↔ output | Fail pattern |
| --- | --- | --- |
| Spatial mapping | Relative coordinates, margins, directions, crop | Hero drifted; main subject switched side |
| Silhouette and relative size | Key subject shapes/scale relationships | Small/large relationship lost |
| Hierarchy | Dominant first read and sequence | Meaning replaced by UI labels |
| Color and value | Palette role, contrast, saturation balance | Image becomes neon or muddy without permission |
| Material and style | Flat vs photo vs 3D; outlines, texture, shading | Flat illustration becomes photorealistic CGI |
| Typography | Exact words, line breaks, emphasis, type character | Invented copy, missing or mistyped content |
| Clean canvas | Source wrapper separated from deliverable | Added navigation, bookmark, footer credit |
| Requested edits | Only specified modifications made | Unasked changes to brand/layout |

Score visually by category with explicit caveats. **Do not invent 95% match statistics**. If a quantitative metric is required, use an actual measured method (e.g., normalized geometry/SSIM after appropriate alignment) and disclose where perceptual similarity is not captured.

## The "same but editable" rule

When the user says "replicate using customizable replacement content," retain a stable base artwork and separate editable layers/variables for copy, brand colors and user-changeable hero assets **when tools support true editable output**. A raster image with blank labels is *not* automatically an editable design system. Offer actual layered/vector source when generated and verified; otherwise state that only a raster was delivered.

## Explicit source-layout versus brand-color conflict

If adapting Reference A's red/cream panel grid to Brand B's forest/lime/cream palette, keep the **same panel hierarchy and normalized grid** but replace the red blocks with Brand B's approved primary/background colors. Transfer the *role* of accent/contrast, **not the original brand's red hue**. If an extra color is included in Brand B's palette for alerts, do not extrapolate it into a hero background.

If the reference includes a phone screen as a significant **intended design panel**, it is not equivalent to incidental browser chrome: preserve or explicitly replace that panel's function rather than silently omitting it. When it is just viewer chrome surrounding another work, omit it. Review source proportions before choosing.

### Panel fidelity log

In the reference and the output, record each important panel's `[x0,y0,x1,y1]` in percentages of width/height. Compare arrangement and hierarchy; no fabricated similarity percentage. Record which material/photograph changed due to subject replacement and whether that change is justified.
