# Phase 1 verification record — 2026-11-19

This document records tests executed on `graphic-design-director` v0.4.0.

## Baseline custody

- Source: `graphic-design-director-v0.3.1-brand-verified-workflow.zip` (49 files)
- Its SHA-256 and all file hashes are recorded in `baselines/v0.3.1-manifest.json`.
- All **23 original** files inside `references/` are byte-identical to those in the v0.3.1 source ZIP. Earlier audit shorthand that said "25 references" was inaccurate; the archive contains 23.
- Original source ZIP and older loose directory were not overwritten. Brand-specific cases remain in `evals/` solely as regression examples, never cross-project defaults.

## What is executable now

- Creates a schema-valid, project-isolated DRAFT without overwriting a nonempty project.
- Validates six contract files against seven JSON Schemas, including an independent QA report schema.
- Registers a source file by *copying original bytes* into project assets, hashing it with SHA-256 and recording project-specific source provenance/approval.
- Rejects duplicate IDs, project-ID mismatch, unsafe traversal and symlink escapes, absent referenced assets, changed asset bytes, and undefined concept IDs.
- Enforces populated brief summary and raster pixel dimensions for strict preflight; source-led jobs require a registered reference.
- Writes `reports/preflight.json` and distinguishes BLOCKED, REVIEW_REQUIRED, READY_FOR_CREATIVE.

## Executed checks

- `python scripts/validate_skill.py` — PASS
- `python -m unittest discover -s tests -v` — 17 tests PASS
- `python scripts/install.py --target codex --scope project --project /tmp/gdd-audit --dry-run` — PASS
- `.github/workflows/validate.yml` now runs installation of jsonschema and the regression suite.

## Explicitly not implemented

- No renderer/model calls, cross-provider adapters, end-to-end orchestration, visual comparison, typographic fidelity detection, design-score calibration, autonomous skill edits, or publication to GitHub.
- Image-only fidelity and creative quality are **not** validated by schema checks.
- Asset approval metadata is supplied by the project/user; its presence does not prove rights, authenticity or real-world accuracy.
