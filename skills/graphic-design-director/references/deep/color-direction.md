# Color direction — meaning, interaction and production

Colors do not behave in isolation. They change with neighboring hues, value, context, light and reproduction. This guidance is original, influenced conceptually by Josef Albers and design practice.

## 1. Make a role-based palette

Specify distinct roles: `base/background`, `primary`, `secondary`, `accent`, `text/ink`, `functional alert`, `neutral/support`, `material/native`. Record provided HEX/CMYK as known; do not invent “official” codes. The role matters more than the color name.

If a brand has a red warning color, this does not authorize a red billboard background. If a reference has a vivid blue field but the client approved a forest-green primary, the new identity overrides the old field in an adaptation.

## 2. Establish color proportions as design decisions

Not every design needs 60/30/10; this is a rough training aid, not law. Instead ask which color carries **mass**, which establishes **hierarchy**, and which provides a **single punctuation point**. Saturation is limited by attention economics: a fluorescent accent loses power when everything is fluorescent.

## 3. Consider simultaneous contrast and legibility

A green against orange may feel sharper than either hue on paper. A neutral may become visibly tinted by a neighboring saturated field. Test color combinations at actual output size and screen brightness. Do not conflate nominal numerical contrast with perceived readability under texture, glow or photographs.

For digital text with applicable accessibility requirements, use WCAG contrast as a baseline (4.5:1 normal text, 3:1 large text in WCAG 2.x AA), checking sizes and real background values; print requires separate ink/material visibility tests. Don't treat accessible contrast alone as sufficient art direction.

## 4. Build palettes from grounded sources

Options include physical subject colors, available brand assets, local cultural material, documentary photographs, specific historical print methods, or a deliberately invented conceptual premise. Record when a color is proposed rather than official.

For tactile visuals, account for how ink prints on kraft, uncoated stock or fabric; a pure digital RGB accent may not translate. Avoid making material surfaces uniformly “AI glossy” when source calls for matte, printed, grainy or hand-made.

## 5. Color-led hierarchy checks

- Squint and grayscale: does the key object/message still dominate?
- What % of visual area is each high-saturation hue occupying? An accent shouldn't silently become a background.
- Does a warm highlight draw the eye off the actual headline or product?
- Does the image's lighting shift approved colors away from their intended appearance? Distinguish material reflections from flat swatches.
- Are multiple accent colors creating unrelated emotional signals?

## 6. Repair rules

| Problem | Repair |
|---|---|
| Colors look trendy but off-brand | restore approved role hierarchy, not just hex codes |
| Every panel is bright | neutralize secondary surfaces to reintroduce attention gradients |
| Text unreadable on busy photograph | change text field, crop, weight or overlay with restraint |
| Vector art looks 3D despite no-3D brief | remove shading gradients, specular light and bevel |
| “Exact” swatch visually differs | inspect exported fill pixels away from labels; fix render pipeline |
| Moodboard looks like another company's palette | retain structure only, replace palette according to authorized brand |

## 7. Avoid color slop

Generic rainbow gradients, default neon-blue techno backdrops, arbitrary bright sticker shapes, gold glows masquerading as premium, red overlays because the inspiration had red, and swatches with printed hex labels that do not match actual fills.
