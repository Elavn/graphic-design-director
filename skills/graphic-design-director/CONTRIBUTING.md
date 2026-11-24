# Contributing and improving the skill

Improvements should follow `references/critique-learning-protocol.md`.

1. Start from a **specific observed design failure** or new brief and state evidence.
2. Separate aesthetic preference from objective inaccuracy/legibility/rights defects.
3. Create a narrowly scoped change in the appropriate `references/` file, or main skill only for globally important guidance.
4. Add one **regression case** to `evals/` describing pass/fail. Test on different style categories; don't make all outputs follow one template.
5. Run `python scripts/validate_skill.py`. A passing script checks document integrity, **not visual quality**. Manually review designed images.
6. With approval, bump `VERSION`, update `CHANGELOG.md`, and submit a reviewable PR. Do not commit private feedback logs or source images lacking redistribution permission.
7. GitHub publication and installation elsewhere require explicit authorized actions; no hidden automatic updates or model training.
