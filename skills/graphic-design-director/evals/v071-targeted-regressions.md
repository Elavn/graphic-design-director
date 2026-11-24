# v0.7.1 — Targeted creative-regression cases

These cases address three observed weaknesses from the v0.7 baseline. They are **project-neutral examples**, not required visual styles or universal template choices.

| ID | Mode | Previous failure | Required evidence | Automated checks | Human gate |
|---|---|---|---|---|---|
| V071-C01 | CREATE | Product-ad metaphor only identifiable after explanation | Brief, image, thumbnail, actual first-viewer reading, side-by-side before/after | File size, dimensions, unchanged approved copy if an exact text file exists | Metaphor understandable without prompt; lighting and physical or surreal logic explained |
| V071-R02 | ADAPT | Photo-led reference became a flat illustration | Source image, medium map, keep/replace/remove ledger, photo provenance and crop comparison | Photo source hash, asset existence, geometry/dimensions | Real photographic character preserved; no embedded reference UI, statistic or cutout halos |
| V071-W03 | SYSTEM | "Custom" logo is a default sans with an inconspicuous cut | Original vector master, working process, black/reversed proofs and small-size sample | Vector paths present, four semantic glyph groups, size and master reuse where testable | Distinctive letter grammar and optical quality without loss of reading |

## Test protocol

1. Freeze the *same* original brief before and after. Preserve its actual wording and constraints.
2. Save the original and revised artifact bytes separately. Do not overwrite the baseline.
3. Check the objectively verifiable constraints with `scripts/review_gate.py`. Do not infer creative quality from those results.
4. Have a human reviewer assess the image at intended size, with the prompt hidden first. Record the unaided reading and specific failures.
5. Declare `TECHNICAL_PASS_REVIEW_PENDING`, `REVISE`, or `APPROVED_BY_HUMAN` based on evidence. Never automatically award an originality score or approve creative output from file existence.
6. If a change fixes a local issue but introduces a new failure, retain both observations and mark the case as mixed rather than a clean pass.

### What this is not

A complete style library, a model weight update, a universal taste judgment or an automatic guarantee that any model will honor these instructions. A photoreal photo crop is not evidence of rights for commercial use. Vector path drawing does not establish trademark clearance.
