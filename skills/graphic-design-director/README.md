# Graphic Design Director — Deep Universal Agent Skill (v0.7.2)

A **self-contained, model-neutral art-direction skill** for serious graphic-design thinking and production. It runs as instructions on whichever model is already active in a compatible skill host. **No external model, API key, orchestration service or paid AI account is required.**

## Philosophy

Design starts with a message and a visual concept, not an aesthetic preset. The skill distinguishes exact replication, controlled adaptation, inspiration, original briefs, design-system work and critique. It protects approved source assets and rejects incorrect specs or visually polished but conceptually empty output.

## Contents

- `SKILL.md`: full operating workflow, mode selection, constraint ledger, art direction and double review gate.
- `references/deep/`: in-depth craft and creative-process modules (strategy, visual art direction, typography, composition, color, identity, imagery, formats, reference analysis, critical review, examples).
- `references/`: original foundation rules and 18-book influence map, intentionally preserved.
- `evals/deep-regression-cases.md`: 18 cross-project behavior cases.
- `scripts/`: optional local file validation and project contract utilities. These do **not** contact external models.
- `docs/WORKFLOW.md`: setup, process and honest tool-capability boundaries.

## Installation

The portable `.skill` distribution and cross-CLI installer are documented in [INSTALL.md](INSTALL.md). This skill has no additional AI model requirement.


Copy the whole `graphic-design-director/` folder to the skill path supported by your current CLI; examples:

- Claude Code (user): `~/.claude/skills/graphic-design-director/`
- Codex (user): `~/.agents/skills/graphic-design-director/`
- Gemini CLI (project): `.gemini/skills/graphic-design-director/`
- Cursor (project): `.cursor/skills/graphic-design-director/`

Consult your CLI's current documentation for other locations. For a model without automatic skill loading, provide `SKILL.md` and the relevant focused reference files in its context. A skill alone cannot install image-generation software or access a design program it doesn't have.

## Invocation

“Use Graphic Design Director to create a [medium] for [brief]; [requirements and references]. Make it concept-led, obey locked brand assets and validate the actual output.”

For a faithful adaptation: “ADAPT the uploaded reference with these content changes. Preserve the unmodified layout and visual language. Do not import unrelated UI or invented statistics.”

For a critique: “CRITIQUE the uploaded design against the brief and reference, identify the three most consequential failures, then propose the smallest credible revisions.”

## Optional local checks

```bash
python scripts/validate_skill.py
python -m pip install -r requirements-pipeline.txt
python -m unittest discover -s tests -v
```

The optional JSON contracts are tools for tracking real assignments; they are **not prerequisites** for everyday design work. No external model adapters are bundled.

## Honesty and rights

This material is original guidance influenced by design literature and practice, not book passages. No third-party book scans, fonts, logos, commercial photographs or copyrighted source artwork are bundled. The package should not claim measured fidelity, brand verification or model-training improvements without evidence from actual results.

See [DEEP-SKILL-RELEASE.md](DEEP-SKILL-RELEASE.md) for changes and limits.


For v0.7.1 evidence-based critique and review gates, see [release notes](RELEASE-v0.7.1.md).
