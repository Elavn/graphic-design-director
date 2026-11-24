# v0.7.0 — Deep design intelligence refocus

## Why this release exists

The former v0.6.0 branch emphasized model-provider integrations. The intended goal is a detailed, cross-model Agent Skill that uses the **host's existing intelligence and tools**, without API integrations. This release returns to the v0.4.0 source-asset and local validation baseline, preserves its original design references, and expands the self-contained creative design practice significantly.

## Included

- Full art-director operating instructions in `SKILL.md`.
- Ten in-depth modules in `references/deep/`: strategy, art-direction atlas, typography, composition, color, identity, imagery, medium playbooks, reference analysis, critique and worked examples.
- Brand-neutral behavioral regression cases.
- Optional, local-first source-of-truth project contracts and QA helpers from the earlier baseline.
- No OpenAI, Anthropic, Gemini, or other provider adapters; no API keys or model router.

## What this does *not* promise

- It does not train a model's weights, provide a new image-generation tool, or guarantee identical outputs across hosts.
- It does not replace access to licensed fonts/photos or official brand assets.
- It cannot certify professional visual excellence without reviewing actual outputs.
- The cross-project design cases are written behavior tests, not successfully executed model benchmarks.

## Recommended use

Start with `SKILL.md` in your current host. The host model loads focused references and uses the graphics/editing tools it already has. Use the optional Python checks only when files and a Python runtime are available.
