# Anti-slop quality gates and revision algorithm

## Gate -1 — Mechanical and brand contract (must pass before aesthetic scoring)
- Measure output **width × height** from the actual exported file; reject wrong dimensions or aspect, even if the design is beautiful.
- Compare dominant background/panel colors with the supplied brand palette *and* the role of each color. A secondary alert color is **not** approved as a dominant campaign background.
- For reference ADAPT: compare normalized panel boundaries/regions against the source; declare meaningful deviations and correct them where feasible.
- Verify exact brand spelling, required logo/visual, copy and negatives by direct visual inspection. OCR/automated color checks are supporting evidence, not proof of text/logo or perceptual fidelity.
- A single hard violation means **FAIL**. Do not hide hard failures inside a high weighted aesthetic score.

## Gate 0 — Accuracy and legitimacy (must pass)
- No invented factual details, copied marks, unreadable generated text, false QR codes or fabricated output claims.
- Exact brief fidelity: confirm what is **visible**, not merely what was requested. A source-reference masthead, logo, hero text or other recognizable identity imported into an unrelated design is an automatic fail; a generic design under the wrong brand is not a delivery candidate.
- Content is consistent with user's brief and brand assets; required legal/cultural sensitivity checked.
- No use of unlicensed source material where licensing is necessary.

When generative art makes the same brand/copy substitution twice, switch to separately typeset layout and standalone hero imagery as described in [brief-fidelity.md](brief-fidelity.md).

## Gate 1 — Seven-part weighted scorecard (100 points)
| Criterion | Points | Excellent means... |
| --- | ---: | --- |
| Message clarity | 15 | Main idea obvious in a glance; essential facts present |
| Hierarchy / scan path | 15 | Clear primary → secondary → action order |
| Typography | 15 | Appropriate type, compelling hierarchy, polished spacing |
| Composition / grids | 15 | Intentional geometry, balanced visual mass, useful whitespace |
| Color / contrast | 10 | Role-based color, accessible functional text, cohesive values |
| Conceptual distinction | 20 | Specific, memorable, fitting visual idea rather than template sameness |
| Production / consistency | 10 | Correct format, alignment, crop, spelling and asset fidelity |

- **85–100:** delivery candidate if Gate 0 passes and no critical failure.
- **70–84:** revise weak criteria; explain what changed.
- **Below 70:** rethink concept/layout, not merely color.
- Regardless of sum, **block delivery** for illegible essential information, inaccurate event details, missing required logo, dangerous misrepresentation or obviously clipped text.
- A text-only evaluation is provisional; inspect real renders when tools allow.

## Gate 1A — Creative-concept and reference-image calibration
- Before scoring polish, identify the **specific message embodied in the dominant type or image**. If there is no concrete idea, aesthetics alone cannot score more than 5/20 on conceptual distinction.
- For **type architecture**, inspect headline silhouette, deliberate serif/sans role pairing, intentional overlap, legibility and whether editorial tags support actual meaning.
- For **surreal metaphors**, inspect one clear story, physical plausibility except for the deliberate impossible element, coherent shadows, size readability and negative space.
- For **tactile playful advertising**, inspect why the object/action is apt, realism of the composite, material contrast, restrained graphics and original—not copied—visual joke.
- Do not give every design the same large serif, pale grid, blue background or cutout hand because these appeared in supplied references. Overfitting a reference is a quality failure.
- Evaluate the **rendered** graphic at real device size, 25% scale and zoom; if only a prompt exists, state score is *not yet visually validated*.

## Gate 2 — Anti-generic checklist
Flag each issue present; revise rather than just count:
- Random geometric or shiny 3D decoration without concept.
- Same gradients, cards, or glows for every brand.
- Type chosen for novelty alone; too many fonts or all text same size.
- Random margins, inconsistent alignment, unbalanced crowded corners.
- Generic stock or synthetic hero unrelated to exact message.
- Unreadable title treatment or footer details.
- Trend vocabulary applied mechanically instead of intentionally.
- Unrequested literal copy of another designer's signature composition in an original/INSPIRE brief; authorized REPLICATE/ADAPT uses source geometry.

## Revision algorithm
1. **Identify the single largest communication failure.** Write it in one sentence.
2. **Fix structure first:** reading order, content grouping, concept, crop, grid.
3. **Fix typography next:** contrast, line breaks, spacing, weight, sizes.
4. **Fix color and imagery:** palette roles, value relationships, meaningful visual choice.
5. **Remove excess:** subtract every effect that does not earn its place.
6. **Review again** at thumbnail/actual/close-up. Repeat until no critical failure.

## Two-person mental review
- **Art director lens:** Is it distinctive, appropriate, courageous and coherent?
- **Production designer lens:** Is it accurate, aligned, legible, reproducible and deliverable?
Both must approve. A beautiful graphic with wrong event details fails.

## “What this skill would reject” statement
A design that looks expensive but cannot be read is not finished. A clear design that is indistinguishable from every template is not fully art-directed.
