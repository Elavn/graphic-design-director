# v0.7.1 — Targeted design-behavior regressions

Maintains the existing brand-neutral skill. Adds three specific learning modules, three behavior cases, a conservative local file/asset gate, and tests. No provider adapters or new models introduced.

**Proven improvements to the skill:** clearly documented separate checks for metaphor comprehension, photographic-material consistency, embedded source UI, genuine glyph construction, and master reuse. Technical gate cannot approve creative quality.

**Not proven:** consistent visual gains across different hosts/models, legal originality, or automatic detection of all AI slop. Three illustrative manual reruns are distributed separately from the universal skill so no one brand/image becomes a default.

To run locally:

```bash
python -m unittest discover -s tests -v
python scripts/validate_skill.py
python scripts/review_gate.py --manifest /path/to/your-project/review-manifest.json
```

Example `review-manifest.json` placed beside `output.png`:

```json
{"output":"output.png", "expected_dimensions":[1080,1350], "locked_assets":[]}
```

The check validates bytes, file dimensions and SHA-256 of locked assets. Conceptual clarity and image rights still need a human reviewer.
