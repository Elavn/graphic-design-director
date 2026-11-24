# Phase 1 — Project isolation, schemas, approved-asset locks and deterministic preflight

**Status: implemented and tested.** This does not generate a graphic, evaluate visual originality or connect to a model endpoint. The existing `SKILL.md` and its design craft references remain authoritative for design reasoning.

## Installation

Python 3.10+ is required. CLI stages use `jsonschema` for complete JSON Schema 2020-12 validation; installing it does not lock this pipeline to any AI provider:

```bash
python -m pip install -r requirements-pipeline.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

## One isolated project per assignment

```bash
python scripts/pipeline.py init --project ./work/example-campaign --id example-campaign --mode CREATE --medium 'event poster'
```

The command **refuses to overwrite** an existing nonempty directory. It creates:

- `project.json`: mode, medium, user brief, required copy, provenance, output spec, references and creative freedom
- `assets.json`: immutable snapshots of provided images/logos/assets, relative paths, SHA-256, explicit approval and reuse limits
- `constraints.json`: user-sourced hard/review requirements and approved decisions
- `concepts.json`: proposed art directions (blank until concept stage)
- `render-request.json`: rendering metadata (NOT_STARTED by default)
- `revisions.json`: change records (blank until critique)
- `BASELINE.json`: which core version initialized this project
- `approved-assets/`: source-preserving file copies (no transcodes or font redistribution)
- `reports/preflight.json`: generated after preflight; not an actual artwork QA approval

The blank project is intentionally a valid **DRAFT** and cannot pass preflight until its actual brief and required raster dimensions are supplied. Set `project.json`'s `brief.summary`, `brief.key_message`, and `output.width_px`/`height_px` for raster outputs. For original concepts without a source image, use `CREATE` and leave `reference_asset_ids` empty. In the four source-led modes, provide registered references rather than importing assumptions from another project.

## Register and lock a source asset

```bash
python scripts/pipeline.py register-asset --project ./work/example-campaign \
  --id approved-logo --file /path/to/logo.svg --kind logo --reuse exact --approved
python scripts/pipeline.py register-asset --project ./work/example-campaign \
  --id layout-reference --file /path/to/reference.png --kind reference --reuse style-only
```

`register-asset` copies bytes under `approved-assets/` and records a checksum. `--approved` means user/project approval of that specific asset, not ownership or trademark verification. Use the `reference_asset_ids` field in `project.json` to tell the pipeline which registered references apply. The actual file bytes are never modified by validation. An altered asset hash, unsafe traversal, missing reference, duplicated ID or conflicting project ID causes a BLOCKED result. Do not share asset manifests from one client/project with another.

## Validate then preflight

```bash
python scripts/pipeline.py validate --project ./work/example-campaign
python scripts/pipeline.py preflight --project ./work/example-campaign
cat ./work/example-campaign/reports/preflight.json
```

**`validate`** checks schema structure, IDs, paths and asset hashes. **`preflight`** also checks nonempty brief, exact raster output dimensions and source-led reference presence. Active manual constraints remain REVIEW_REQUIRED, not silently passed.

- `BLOCKED` (exit 1): schema/content/integrity failure; fix before producing art
- `REVIEW_REQUIRED` (exit 0, non-approval): human review required; cannot certify those properties programmatically
- `READY_FOR_CREATIVE` (exit 0): Phase 1 deterministic preflight passed, **not** an image or final-design approval
- CLI configuration/runtime error (exit 2)

Never claim this tool checks composition fidelity, subject identity, real-life dimensions, typography quality, prohibitions visibly present in output, or visual creativity. Those belong to later stages; any generated artwork needs additional review, irrespective of preflight result.

## Contracts

All seven schemas in `schemas/` use JSON Schema Draft 2020-12, `schema_version: "1.0"`, and a shared project ID. They cover: project brief, asset manifest, constraint ledger, concept proposals, render request, QA report and revision records. The CLI currently writes/validates six operational project files and generates a report matching the QA schema. The final design is not rendered and the QA schema is not an approval claim.

## Provenance, migration and versioning

`baselines/v0.3.1-manifest.json` records SHA-256 hashes for all 49 files from the source ZIP, and the ZIP itself. The extracted old loose folder is **not** the canonical baseline. The old ZIP is untouched and not packaged in this update. The current distribution is v0.4.0; its design reference core descends from v0.3.1. Keeping a baseline record does **not** automatically merge or edit another installation.

## Next phases (NOT implemented)

1. Model and renderer adapters with explicit capability declarations.
2. A Core Orchestrator that coordinates all stages and retries without mutating the brief.
3. Post-render deterministic checks and image/reference comparison.
4. Creative critique approval and versioned regression tests across diverse design briefs.
