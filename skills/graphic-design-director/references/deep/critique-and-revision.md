# Critique, art direction and controlled revisions

Criticism should improve the design, not produce unstructured dissatisfaction or an ever-growing list of universal bans. Evaluate **what the actual image communicates**, not how impressive the prompt sounds.

## Gate A: hard constraint compliance (binary)

Fail if any material requirement is violated: wrong medium, wrong dimensions, missing mandatory copy, fabricated claim, wrong subject count/type, prohibited 3D/photo/gradient, missing negative space, modified approved logo, inappropriate user-interface elements, or unauthorized reference redesign. A polished image cannot make a hard failure pass.

## Gate B: professional craft (analytical, not an automatic numeric grade)

Review on at least eight dimensions:
1. **Central idea:** specific, intelligible and worth attention?
2. **Brief relevance:** tailored to actual audience, not generic trend output?
3. **Hierarchy:** first-second-third reading sequence in target context?
4. **Typography:** voice, optical spacing, line breaks, legibility, micro details?
5. **Composition:** scale, crop, tension, proximity, hierarchy, whitespace?
6. **Color:** semantic consistency, roles, contrast, perceptual balance?
7. **Imagery and materials:** authentic geometry, lighting, tactile plausibility, intentional medium?
8. **Craft & delivery:** file type, pixel size, print needs, editability, accurate assets, missing data?

Use `excellent / convincing / needs revision / failed` with specific evidence. A score such as “83/100” is optional, not proof. If numerical scoring is used, disclose what was measured versus subjectively judged.

## Diagnose before changing

| Observation | Type | Root-cause question | Targeted response |
|---|---|---|---|
| Generated rounded cards in a poster | MEDIUM | why was UI layout assumed? | remove cards; rebuild poster hierarchy |
| Correct logo letters changed | BRAND | was asset generated instead of placed? | composite original logo file |
| Huge subject occupies all type space | COMPOSITION | was crop planned for copy? | recrop/reposition or allocate dedicated field |
| “Modern” ad looks interchangeable | CONCEPT | what insight is unique? | reconceive core visual metaphor |
| Brand accent dominates background | COLOR | were palette roles ignored? | restore role balance |
| Tiny copy unreadable | TYPOGRAPHY | tested at real size? | increase or simplify, preserve message |
| Product body changed shape | SUBJECT | was image source anchor lost? | reference-led edit, preserve physical identity |
| Correct size, bad text clipping | PRODUCTION | did QA check glyph bounds? | reflow and re-export; record regression |

## Minimal-change revision protocol

1. State the approved aspects that must remain unchanged.
2. Isolate the failing region or decision.
3. Decide whether error is **local** (type spacing, logo, crop) or **conceptual** (entire idea weak).
4. Make the smallest change that fixes local errors; change the concept when concept is the problem.
5. Verify that locked elements did not drift, plus previously passing constraints remain passing.
6. Save observation and a reproducible test; do not make a single client's subjective choice universal.

## Self-critique questions

- What would a skeptical art director reject first?
- What element would improve if removed?
- Would this design work with any company's logo, or does it solve this specific brief?
- Is the aesthetic appropriate for context, or did I repeat a familiar prompt pattern?
- Does the image work at thumbnail scale and final medium?
- Which details cannot be verified and should be marked provisional?
- What one revision would most improve clarity/impact?

## Maintain a real improvement trail

For repeated skill failures, record `test_id`, `mode`, `brief`, `locked_assets`, `expected_behavior`, `observed_failure`, `root_cause`, `rule_update`, `regression_case`, `result`. A Markdown knowledge file is not model fine-tuning. A test is meaningful only when it actually checks future output, not when it merely exists as prose.
