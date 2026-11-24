# Constraint-first visual production and validation

Every design **must** pass this contract before it may be presented as approved. Run it for REPLICATE, ADAPT, INSPIRE, CREATE and HYBRID; only the amount of layout freedom changes.

## 1. Source-of-truth sheet

Record before generating (internal, or visible when useful):

```yaml
mode: ADAPT
reference_image: <actual user-provided image>
brand_source: <actual user-provided moodboard/assets>
output_media: raster_png
target_width_px: <exact integer>
target_height_px: <exact integer>
reference_aspect: <measured width / height>
brand_palette: # exact hex tokens from supplied brand source
  primary: ...
  highlight: ...
  neutral: ...
  alert_only: ...
required_copy: [ ... ]
forbidden: [ ... ]
layout_zones: # normalized percentages from supplied reference
  - [x0, y0, x1, y1]
brand_asset_fidelity: <must match approved logo if supplied>
```

Do not invent hex values or turn one moodboard's optional accent into a dominant background. Distinguish a reference's **visual-system roles** from its brand-specific exact colors; user brand tokens override its colors. A reference screenshot can contain a real phone/app demo as an intended *panel*, whereas external browser navigation is not artwork.

## 2. Exact-resolution lock

- If explicit pixel dimensions are supplied, exact equality is a hard gate.
- Otherwise for ADAPT / REPLICATE, retain the source aspect. If the user subsequently specifies a new size, that latest instruction overrides.
- When both source and requested output are 3:2, e.g. 735 × 490 reference and 1536 × 1024 output, maintain normalized composition.
- Measure the final file with a raster parser; NEVER claim correct size based solely on prompt wording or image canvas in a chat preview.
- Do not crop meaningful panels to force a ratio after generation. Rebuild the composition if the renderer's defaults are wrong.

## 3. Color-role lock

- Write **primary / highlight / neutral / supporting / semantic-alert** roles separately.
- Primary and neutral colors should dominate the frame when that is the intended brand system; highlight color should remain deliberate.
- A color swatch on the moodboard is not carte blanche to cover the background with it. For Pickam: Forest `#0E4B38` primary, Route Lime `#C4EE3A` highlight, Paper `#F6F5EC` and Mist `#E1EDD4` neutrals, Ink `#101512`; Load Orange `#FF6A13` and Alert Red `#E5301F` are limited functional accents.
- Photo tones may contain natural colors outside the brand palette; never recolor skin/cardboard/trees unnaturally merely to satisfy a global pixel limit. Flag **large saturated red regions/panels** for visual review.

## 4. Layout lock for adaptation

- Map source panels, relative size, dominant photography, typography blocks, crop direction and gutters in normalized coordinates.
- Apply **minimal changes**: brand/logo, copy, products, photos, tokens; keep unmodified hierarchy and structure.
- For text replacement, reflow **inside the same panel** before expanding or moving it.
- Compare the artwork side by side against the source at a common aspect ratio. Give an honest `pass / needs revision / fail` per constraint. Do not declare an exact similarity score without measurement.

## 5. Automated and manual gates

Run when local tools are available:

```sh
python scripts/check_raster.py OUTPUT.png --width 1536 --height 1024 --max-saturated-red-share 0.05
```

The pixel check catches format errors and dominant highly saturated red regions; it is a coarse proxy, **not** a perfect palette-compliance or layout-fidelity test. Confirm color roles, brand mark, captions, exact typography, source panels and overall aesthetics visually.

**Approval logic:** zero hard failures AND faithful panels AND legible/accurate copy AND good design craft. If a hard constraint fails, correct it before calling the deliverable finished. If a locked panel has been omitted or substantially replaced without user authorization, disclose `needs revision` rather than declaring full fidelity.
