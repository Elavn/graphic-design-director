# Production and accessibility

## Accessible design
- For digitally delivered text, meet WCAG 2.2 AA text-contrast baseline when possible: 4.5:1 normal-sized text; 3:1 large-scale text (the definition of large-scale text matters). These are not blanket guarantees of readability; thin letterforms, busy textures and small rendered type may still be difficult.
- Never convey information with color alone. Pair with labels, shapes or position.
- Check minimum practical rendered sizes on actual target devices and viewing distances. There is no universal pixel threshold for all social media or print contexts.
- Set content in semantic reading order when working in HTML/PDF or an accessible source format; provide meaningful alt text where supported.
- Check spelling, diacritics, script shaping, language direction, numerals and date/time context.
- Respect reduced motion and photosensitivity for animated designs; avoid rapid intense flashes.

W3C reference: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html

## Art direction into production
- **Raster:** select resolution based on displayed physical dimensions; “300 dpi” is a common print target at final size, not an all-purpose magic number. Avoid resampling low-resolution images as if it adds real detail.
- **Vector:** preferred for marks, icons and large-scale sharp typography; inspect curves and expand/export only as needed, retaining editable master.
- **Photo:** verify rights and subject releases where needed. Inspect cropping and retouching artifacts; do not invent recognizable brand/product imagery.
- **Fonts:** verify licensing, language glyphs, font rendering and editable handoff. Do not bundle proprietary font binaries without permission.
- **Color:** distinguish RGB digital from CMYK process print; use proofing and a print-provider-specified profile. Metallic effects rendered in RGB are not the same as metallic ink or foil.
- **Bleed and safe zones:** use output-provider specs, not assumptions. Leave text and critical marks inside safe area; allow image/background extension into actual bleed.
- **QR, URL and tracking:** only make functional codes from provided/confirmed destinations; test scans at final size and print contrast.

## Review at three scales
1. **Thumbnail:** does the first impression and key hook survive?
2. **Actual size:** are the important facts readable, spacing stable and margins sufficient?
3. **Close-up:** are ligatures, letter spacing, edges, alignment, contrast and image defects clean?

## Honest handoff
If a source/design file was not actually generated, say so. Deliver specs instead of fabricated links. Keep editability and export format distinct: a PNG is not an editable layered master.
