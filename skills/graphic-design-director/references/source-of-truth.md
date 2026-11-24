# Source-of-truth contract: brief, reference, and requested changes

## Select the right task, then lock constraints

The same image may be used for four different jobs; do not misclassify:
- **REPLICATE:** reconstruct the reference itself. Exact matching is the goal. Avoid adding new ideas.
- **ADAPT:** reconstruct the reference's visual grammar but swap only specified content, assets, color or brand material. Preserve hierarchy and geometry unless a replacement needs careful reflow.
- **INSPIRE:** carry over chosen traits while developing a new concept. Do not import identity or composition unless explicitly asked.
- **CREATE:** follow the textual brief and design an appropriate original solution.
- **HYBRID:** treat the reference as the baseline, then layer new brief requirements on top. Explicit overrides win.

## Constraint ledger (internal, not a user questionnaire)

| Layer | Questions to resolve | Lock status |
| --- | --- | --- |
| Deliverable | Is this a static poster, illustration, social post, brand identity, packaging art, print artwork or actual interactive UI? Dimensions/aspect? | Hard |
| Exact items | What must be present, verbatim, in which count and where? | Hard |
| Prohibitions | What must be absent, including all negative-prompt terms? | Hard |
| Reference geometry | Where are hero subjects, lines of motion, margins, empty areas, copy, sight lines? | Preserve in REPLICATE/ADAPT |
| Reference visual language | Colors, material, illustration method, contrast, finish, mood, typographic rhythm? | Preserve in REPLICATE/ADAPT unless overridden; brand palette and usage roles override reference colors |
| Style lock | What does the user mean by flat vector, realism, halftone, hand-painted, photographic, etc.? | Hard when explicit |
| Edits | Exactly which source parts should change and which should not? | Hard |
| Freedom | Which choices are not supplied or constrained? | Discretionary |

If a brief says **text-free**, *every* visible letter, numeral, icon glyph or CTA should be omitted. A *blank* price pill is only a shape, not a speech bubble; retain its specified shape. If a brief says **top 35% empty**, avoid objects, ornaments and type in that region. If it says **no 3D, photo, gradients, glow or outlines**, do not "upgrade" the illustration with realistic reflections, photographs or shaded CGI.

## When instructions collide

Priority: policy/licensing constraints > direct user changes and prohibitions > unchanged reference geometry and style for replication/adaptation > selected style lock > conventional best practice > aesthetic taste. The latest explicit correction overrides an earlier conflicting suggestion. Ask only for a truly blocking conflict; otherwise make the smallest faithful resolution and mention it.

## Evidence discipline

- Do not add facts, dates, prices, or functional interface labels the user did not supply.
- Distinguish artboard from screenshot wrapper; never interpret a browser's chrome as the design unless the user asks to reproduce a screenshot or UI.
- When the exact font, imagery, or logo is unavailable, state the substitution; do not claim exactness.
- In a multi-size campaign, preserve required content and style tokens but recompose to fit, unless user explicitly asks for pixel-consistent placements.

## Aspect ratio and brand overrides are not creative suggestions

- When adapting an uploaded landscape reference into a new brand, preserve its aspect ratio unless the user explicitly specifies new dimensions. **Do not let image-generation default to square or portrait.** If resolution is specified, preserve both dimensions exactly rather than satisfying only the ratio.
- Map the original layout using normalized zones before designing. The palette can change, but the source geometry remains locked unless the brief allows reflow.
- Brand palette rules include **where** colors can appear. A brand can include alert red without allowing red hero panels. State primary/background/accent/semantic roles before rendering.
- On delivery, verify the actual file's dimensions with a parser, then inspect the rendered image; reject any fail.
