# Brief fidelity and source-reference contamination guard (v0.2.1)

A gorgeous image that ignores the user's required words, identity or concept is **not a successful design**. This reference is medium-agnostic: apply it regardless of image model, CLI or layout software.

## Lock the brief before rendering

Write a short immutable preflight table internally:

| Field | Requirement |
| --- | --- |
| Identity | Exact supplied brand name, or explicitly labeled fictional working name |
| Exact copy | All user-supplied wording, including punctuation and capitalization |
| Concept | One specific visual metaphor or typography-led idea expressing the message |
| Format | Intended aspect ratio, platform and text-safe areas |
| Reference permissions | Analysis inspiration only vs authorized direct editing/recreation |
| Forbidden substitutions | No copied source masthead, logos, UI labels, copy, layout signatures or misattributed endorsement |

If no brand, date or event details were given, **do not invent real-world facts**; create an explicitly fictional test case only when the task permits.

## Translate visual references into mechanisms, not surface motifs

- Extract hierarchy, scale contrast, color-role logic, negative-space behavior, physical metaphor and emotional tone.
- Name **at least three source-specific elements to avoid copying** (e.g., exact masthead, chip labels, specific collage objects, composition positions, unique logo mark).
- Select an **opposed composition / palette / material system** for the first distinct concept when the references are strong enough to cause imitation.
- Avoid passing reference images as direct conditioning inputs when the task is *independent creation* and the renderer might copy their surface features. Use short verbal analysis instead, where the tool allows.
- Never mistake a visual reference for a user's active brand.

## Render and test

1. Produce the proposed concept. On inspection, **read back the visible brand, headline, body copy and image message**, not the prompt or intended copy.
2. Gate 0 FAIL if required identity, copy or core message is replaced, the artwork copies a source masthead/mark, or important text is clipped. Attractive composition does **not** compensate for a failed hard gate.
3. If exact wording is uncertain, generate the hero visual separately and apply text in SVG/HTML/CSS/PSD/Figma/Canva or equivalent layout software. Inspect the actual final rendering at full and thumbnail sizes.
4. If two render attempts make the same category of error, **change the method** (separate hero + deterministic copy, reduce image-reference conditioning, or use an alternate renderer). Do not retry a failing approach indefinitely.
5. Distinguish **art-direction instruction weakness** from **generator/tool limitations** in feedback logs; do not falsely claim a rule update has solved a model limitation.

## Concrete rejection test

**Brief:** Fictional creative collective `ODD HOURS`; exact headline `IDEAS REFUSE TO LIE FLAT.`; dimensional paper fold rising through a flat surface; distinct dark editorial direction.

**Pass:** “ODD HOURS” and exact headline rendered and readable; paper visibly lifts from flat surface; result does not inherit a user-uploaded reference's brand or recognizable UI collage.

**Reject:** Any swapped reference masthead or headline, unrelated branding, or near-repetition of reference composition, even if the design otherwise looks polished.

**Partial pass:** Exact copy and original layout but only stylized or weak material realism. Retain brief fidelity and improve imaging craft without forcing the user’s other projects into this aesthetic.
