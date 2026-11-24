# Universal workflow — no external AI model needed

This package is a portable Agent Skill: `SKILL.md` is the primary instruction file, `references/` contains design judgment and craft, and `evals/` contains review cases. Your current AI host is the creative model. Optional Python scripts can check files and contracts locally.

## Route by user intent

1. Identify medium and mode (REPLICATE, ADAPT, INSPIRE, CREATE, CRITIQUE or SYSTEM).
2. Read concise SKILL.md; load only the references needed for the current job.
3. Extract explicit constraints, approved assets, truth claims and style locks.
4. Create an internal design thesis. For open original jobs, explore three *conceptually* different ideas; for source-led jobs preserve required fidelity.
5. Produce artwork with the host's available tools; for exact copy or brand logos, use deterministic placement where possible.
6. Run fidelity gate and creative-craft critique separately.
7. Revise locally; do not regenerate an entire scene to fix a small logo issue.
8. Deliver files only if generated and verified. Archive critiques as evidence, not as automatic universal preferences.

## Optional local validation

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/pipeline.py init --project ./work/example --id example --mode CREATE --medium poster
```

To use the JSON contract workflow, install `jsonschema` from `requirements-pipeline.txt`; it does not connect any model. The `scripts/check_raster.py` and `scripts/check_palette_regions.py` helpers use locally available imaging packages and files. Missing optional dependencies should not block Markdown-based skill usage.

## Example activation for text-only clients

“Read `SKILL.md` and `references/deep/creative-strategy.md` plus the relevant craft references. Behave as an art director for the following user brief. Preserve all exact constraints, avoid unsupported facts, explain production limitations, and perform separate fidelity and aesthetic reviews.”

## Truthfulness

Do not imply that inserting this skill into a CLI installs graphics software. Do not imply that having an adapter architecture means a model has been connected. Rendering must use tools already available to the host and authorized by the user.
