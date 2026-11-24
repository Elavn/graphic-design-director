#!/usr/bin/env python3
"""Phase 1: model-neutral, project-isolated contracts and deterministic preflight.

Requires jsonschema (pip install -r requirements-pipeline.txt).
Does not call any model or renderer, alter approved images, or approve visual quality.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("Missing 'jsonschema'; run: python -m pip install -r requirements-pipeline.txt")

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"
CONTRACTS = {
    "project.json": "project-brief",
    "assets.json": "asset-manifest",
    "constraints.json": "constraint-ledger",
    "concepts.json": "concept-proposals",
    "render-request.json": "render-request",
    "revisions.json": "revision-record",
}
IDENT = re.compile(r"^[a-z][a-z0-9-]{1,62}$")
RASTER = {"PNG", "JPEG", "WEBP"}


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def schema_validator(name: str) -> Draft202012Validator:
    schema = json.loads((SCHEMAS / f"{name}.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def valid_path(project: Path, name: str) -> Path:
    """Only relative local files inside project; reject symlink escapes and traversal."""
    rel = Path(name)
    if rel.is_absolute() or not name or ".." in rel.parts or rel.parts[0] in {".", ""}:
        raise ValueError(f"unsafe project-local path: {name!r}")
    base = project.resolve()
    resolved = (project / rel).resolve()
    if not resolved.is_relative_to(base):
        raise ValueError(f"path escapes project: {name!r}")
    return resolved


def default_contracts(project_id: str, mode: str, medium: str) -> dict:
    k = {"schema_version": "1.0", "project_id": project_id}
    return {
        "project.json": {**k, "mode": mode, "medium": medium,
                         "brief": {"summary": "", "audience": "", "key_message": "", "required_copy": [], "sources": []},
                         "output": {"format": "PNG", "width_px": None, "height_px": None, "notes": ""},
                         "reference_asset_ids": [], "creative_scope": "GUIDED", "project_notes": ""},
        "assets.json": {**k, "assets": []},
        "constraints.json": {**k, "constraints": [], "approved_decisions": []},
        "concepts.json": {**k, "directions": [], "selected_direction_id": None},
        "render-request.json": {**k, "state": "NOT_STARTED", "engine": None, "direction_id": None,
                                "expected_artifacts": [], "notes": ""},
        "revisions.json": {**k, "revisions": []},
    }


def init_project(args: argparse.Namespace) -> int:
    if not IDENT.fullmatch(args.id):
        raise ValueError("project id: lowercase letters/numbers/hyphens, start with a letter, length 2-63")
    project = args.project.expanduser().resolve()
    if project.exists() and any(project.iterdir()):
        raise ValueError(f"project directory already contains files: {project}; refusing overwrite")
    project.mkdir(parents=True, exist_ok=True)
    for name, body in default_contracts(args.id, args.mode, args.medium).items():
        write_json(project / name, body)
    (project / "approved-assets").mkdir(exist_ok=True)
    (project / "reports").mkdir(exist_ok=True)
    write_json(project / "BASELINE.json", {
        "baseline_skill_version": "0.3.1", "pipeline_schema_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "skill_version_at_init": (ROOT / "VERSION").read_text(encoding="utf-8").strip(),
    })
    print(f"Initialized {args.id}: {project} (DRAFT; complete project.json before preflight)")
    return 0


def get_documents(project: Path):
    docs, issues = {}, []
    validators = {name: schema_validator(schema) for name, schema in CONTRACTS.items()}
    for filename, validator in validators.items():
        try:
            path = valid_path(project, filename)
            if not path.is_file():
                raise ValueError("missing contract")
            docs[filename] = json.loads(path.read_text(encoding="utf-8"))
            for err in sorted(validator.iter_errors(docs[filename]), key=lambda e: list(map(str, e.path))):
                loc = "/".join(map(str, err.path)) or "<root>"
                issues.append((f"schema.{filename}", f"{loc}: {err.message}"))
        except (ValueError, OSError, json.JSONDecodeError) as exc:
            issues.append((f"schema.{filename}", str(exc)))
    if docs:
        ids = {x.get("project_id") for x in docs.values() if isinstance(x, dict)}
        if len(ids) > 1:
            issues.append(("project.isolation", "project_id differs across contracts"))
    return docs, issues


def semantic_checks(project: Path, d: dict, *, strict: bool) -> tuple[list, list]:
    """Returns blocking issues and not-yet-automatable review items."""
    errors, reviews = [], []
    if not all(k in d for k in CONTRACTS):
        return [("contracts.missing", "one or more required documents is missing")], reviews
    brief = d["project.json"]
    assets = d["assets.json"].get("assets", [])
    ledger = d["constraints.json"]
    concepts = d["concepts.json"]
    render = d["render-request.json"]

    def dup(items, title):
        seen = set()
        for item in items:
            key = item.get("id")
            if key in seen:
                errors.append((f"{title}.duplicate_id", f"duplicate id {key!r}"))
            seen.add(key)

    dup(assets, "assets")
    dup(ledger.get("constraints", []), "constraints")
    dup(ledger.get("approved_decisions", []), "decisions")
    dup(concepts.get("directions", []), "concepts")
    dup(d["revisions.json"].get("revisions", []), "revisions")

    found = {a.get("id") for a in assets}
    for a in assets:
        try:
            path = valid_path(project, a["path"])
            if not path.is_file():
                errors.append(("asset.missing", f"{a['id']}: {a['path']} is missing"))
            elif sha256(path) != a["sha256"]:
                errors.append(("asset.integrity", f"{a['id']}: SHA-256 mismatch; asset changed"))
            if a.get("approved") and a.get("reuse") != "exact":
                reviews.append(("asset.approval_scope", f"{a['id']}: approved asset is not set to exact reuse"))
        except (ValueError, KeyError, OSError) as exc:
            errors.append(("asset.path", f"{a.get('id')}: {exc}"))
    for ref in brief.get("reference_asset_ids", []):
        if ref not in found:
            errors.append(("reference.missing", f"reference asset id {ref!r} not in assets.json"))
    if render.get("direction_id") is not None:
        if render["direction_id"] not in {c.get("id") for c in concepts.get("directions", [])}:
            errors.append(("render.concept", "render direction_id missing from concepts.json"))
    if concepts.get("selected_direction_id") is not None:
        if concepts["selected_direction_id"] not in {c.get("id") for c in concepts.get("directions", [])}:
            errors.append(("concept.selected", "selected direction id missing from concepts.json"))
    for expected in render.get("expected_artifacts", []):
        try:
            valid_path(project, expected["path"])
        except (ValueError, KeyError) as exc:
            errors.append(("render.path", str(exc)))

    if strict:
        if not brief["brief"]["summary"].strip():
            errors.append(("brief.empty", "brief.summary is empty; don't infer an assignment"))
        if not brief["brief"]["key_message"].strip():
            reviews.append(("brief.message", "key_message unspecified; review intent before concept selection"))
        if brief["output"]["format"] in RASTER:
            if not isinstance(brief["output"]["width_px"], int) or not isinstance(brief["output"]["height_px"], int):
                errors.append(("output.dimensions", "raster output must specify exact width_px and height_px"))
        if brief["mode"] in {"REPLICATE", "ADAPT", "HYBRID", "INSPIRE"} and not brief["reference_asset_ids"]:
            errors.append(("reference.required", f"mode {brief['mode']} requires at least one registered reference"))
        for c in ledger.get("constraints", []):
            if c.get("status") == "ACTIVE" and c.get("verification") in {"MANUAL", "BOTH"}:
                reviews.append((f"constraint.{c['id']}", f"manual review needed: {c['statement']}"))
        for a in assets:
            if a.get("kind") == "logo" and not a.get("approved"):
                reviews.append((f"asset.logo.{a['id']}", "logo is not marked approved; do not claim exact official fidelity"))
    return errors, reviews


def check_project(project: Path, *, preflight: bool) -> dict:
    docs, issues = get_documents(project)
    if not issues:
        errors, reviews = semantic_checks(project, docs, strict=preflight)
        issues.extend(errors)
    else:
        reviews = []
    status = "BLOCKED" if issues else "REVIEW_REQUIRED" if reviews else "READY_FOR_CREATIVE"
    checks = [{"id": key, "status": "FAIL", "severity": "BLOCKER", "detail": detail, "evidence": "local contract/asset"} for key, detail in issues]
    checks += [{"id": key, "status": "REVIEW", "severity": "WARNING", "detail": detail, "evidence": "requires human judgement"} for key, detail in reviews]
    if not checks:
        checks.append({"id": "contract.preflight", "status": "PASS", "severity": "INFO",
                       "detail": "All implemented deterministic Phase 1 checks passed", "evidence": "schemas and asset hashes"})
    project_id = docs.get("project.json", {}).get("project_id", "unknown-project")
    if not isinstance(project_id, str) or not IDENT.fullmatch(project_id):
        project_id = "unknown-project"
    return {"schema_version": "1.0", "project_id": project_id, "status": status,
            "stage": "PREFLIGHT", "generated_by": "graphic-design-director.phase1",
            "checks": checks,
            "unverified": ["No artwork was generated or examined", "Creative quality, logo appearance, layout fidelity and claims in rendered pixels require later-stage review"],
            "generated_at": datetime.now(timezone.utc).isoformat()}


def register_asset(args: argparse.Namespace) -> int:
    project = args.project.expanduser().resolve()
    docs, issues = get_documents(project)
    if issues:
        raise ValueError("validate project contracts before registering assets: " + "; ".join(v for _, v in issues))
    if not IDENT.fullmatch(args.id):
        raise ValueError("asset id must be lowercase hyphenated identifier")
    if any(a["id"] == args.id for a in docs["assets.json"]["assets"]):
        raise ValueError("asset id exists: " + args.id)
    src = args.file.expanduser().resolve(strict=True)
    if not src.is_file():
        raise ValueError("asset must be a regular file")
    # Refuse copying a file from this project over the asset itself.
    dest = valid_path(project, "approved-assets/" + args.id + src.suffix.lower())
    if dest.exists():
        raise ValueError(f"destination exists: {dest}")
    dest.parent.mkdir(exist_ok=True, parents=True)
    shutil.copy2(src, dest)
    if sha256(src) != sha256(dest):
        dest.unlink(missing_ok=True)
        raise ValueError("asset copy integrity failure")
    item = {"id": args.id, "path": dest.relative_to(project).as_posix(),
            "sha256": sha256(dest), "kind": args.kind, "approved": args.approved,
            "reuse": args.reuse, "source_name": src.name, "notes": args.notes or ""}
    docs["assets.json"]["assets"].append(item)
    write_json(project / "assets.json", docs["assets.json"])
    print(f"Registered {args.id} (SHA-256 locked); approval={args.approved}; reuse={args.reuse}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("init", help="create a project with blank, valid contracts; never overwrite")
    a.add_argument("--project", type=Path, required=True)
    a.add_argument("--id", required=True)
    a.add_argument("--mode", choices=["REPLICATE", "ADAPT", "INSPIRE", "CREATE", "HYBRID"], default="CREATE")
    a.add_argument("--medium", default="graphic design")
    b = sub.add_parser("validate", help="validate contract schemas, IDs, paths, and asset hashes")
    b.add_argument("--project", type=Path, required=True)
    c = sub.add_parser("preflight", help="check brief completeness and source constraints; write report")
    c.add_argument("--project", type=Path, required=True)
    d = sub.add_parser("register-asset", help="copy asset into project and lock SHA-256")
    d.add_argument("--project", type=Path, required=True)
    d.add_argument("--file", type=Path, required=True)
    d.add_argument("--id", required=True)
    d.add_argument("--kind", required=True, choices=["logo", "reference", "photo", "illustration", "font", "brand-guide", "other"])
    d.add_argument("--reuse", choices=["exact", "style-only", "editable"], default="exact")
    d.add_argument("--approved", action="store_true", help="mark supplied asset approved; not a claim of trademark ownership")
    d.add_argument("--notes", default="")
    args = p.parse_args(argv)
    try:
        if args.command == "init":
            return init_project(args)
        if args.command == "register-asset":
            return register_asset(args)
        project = args.project.expanduser().resolve()
        if not project.is_dir():
            raise ValueError(f"project not found: {project}")
        report = check_project(project, preflight=args.command == "preflight")
        if args.command == "preflight":
            path = valid_path(project, "reports/preflight.json")
            write_json(path, report)
            print(f"Wrote {path}")
        print(json.dumps({"project_id": report["project_id"], "status": report["status"],
                          "checks": report["checks"]}, indent=2))
        return 1 if report["status"] == "BLOCKED" else 0
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
