# Reference intelligence — learn what to preserve and what to transform

Analyze user-provided references as **evidence**, not as a permission slip to copy every visible element. A design can be embedded in a browser, slideshow, portfolio, screenshot or moodboard; the surrounding framing may not belong to the artifact.

## 1. Classify the source

- **Primary artwork:** the graphic the user wants replicated/adapted.
- **Presentation wrapper:** browser bars, platform tabs, fake app controls, creator credit, reference gallery chrome.
- **Sample content:** brand names, testimonials, people, charts, numbers and sample data from inspiration.
- **Immutable client asset:** approved wordmark, official logo, product, approved photography, pattern or mandated color.
- **Supporting context:** factual PDF brief, audience notes, format constraints.

In strict screenshot reproduction, the wrapper may itself be part of the target; otherwise, exclude incidental UI by default.

## 2. Create a decomposition map

For a source-led layout, map:
1. Canvas size and proportions.
2. Major panel boundaries or composition anchors, using percentages of width/height where helpful.
3. Primary/secondary focal object areas and overlap order.
4. Type families/classes, scale ratios, line breaks, alignment and leading.
5. Palette roles (dominant background, type, accent, neutral, functional UI).
6. Asset treatment (crop, lighting, perspective, texture, stroke, shadows).
7. White-space zones and intentionally omitted information.
8. Elements that must **not** transfer (old branding, fake metrics, UI wrapper, creator credits).

## 3. Mode-specific transformation rules

**REPLICATE:** preserve artwork including its composition. Replace only requested content. If a specific font/photo is unavailable, disclose substitution instead of claiming exact fidelity.

**ADAPT:** preserve recognizable composition and hierarchy, replace source brand colors, names, logos, photographs and facts with authorized client material. The source's primary red block does not override the client's approved dark-green palette.

**INSPIRE:** lift **mechanisms** (e.g. monumental type, tight photographic crop, unexpected juxtaposition), not identical layout, branding, visual assets or incidental widgets. Develop new concept and composition.

**CREATE:** references may signal quality bar or content genre, but do not replace the user's own objective and constraints.

## 4. Compare side by side with a fidelity checklist

Check canvas ratio, margin proportion, focal areas, crop, placement, dominant palette roles, typography voice, reading order, density and whitespace. In an exact recreation, compare matching anchor points and visual structure. In an adaptation, score **changed content accuracy separately from unchanged structure fidelity**. Never present a “95% fidelity” score from intuition alone.

## 5. A/B failure diagnosis

| Failure | Reason | Remedy |
|---|---|---|
| Reference brand name remains | generated copy instead of compositing approved text | replace with source-of-truth asset |
| Layout changed with no authorization | treated ADAPT as INSPIRE | lock panel/anchor map, recompose only content |
| Wrong background color | copied inspiration's palette | enforce client color roles |
| Navigation added to social ad | copied presentation wrapper | isolate actual artwork and omit external UI |
| New vehicle category | model archetype drift | preserve source subject geometry |
| Wrong aspect or output resolution | renderer ignored canvas spec | verify export pixels, rerender/composite |

## 6. High-fidelity workflow

1. Determine exact transformation mode.
2. Mark `KEEP`, `REPLACE`, `REMOVE`, `FREE` regions and assets.
3. Build the layout skeleton before final styling.
4. Replace only authorized elements; protect true client assets.
5. Render at requested size; compare against source at matching display scale.
6. Record *specific mismatches*, fix them, and recheck both source fidelity and new-brand compliance.
