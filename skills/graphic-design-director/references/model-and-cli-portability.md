# Model and CLI portability

## Boundaries
- This skill is **instructions and reference files**, not model weights, a fine-tune or a graphics renderer.
- It aims to run on **any agent that reads Markdown instructions**; automatic loading requires a compatible Agent Skills client or explicit pasting/loading of the prompt. No instruction can guarantee identical results across all models, CLIs or rendering systems.
- Never assume a particular tool, image generator, font manager, IDE or network connection exists.

## Capability handshake (quiet, only when needed)
1. Determine whether you can read this SKILL.md and linked references.
2. Determine available outputs: image generation, image inspection, editable vector/raster, filesystem, browser, presentation, design software, or text-only.
3. Determine whether a font, logo, image or licensed asset is supplied; do not imply rights to unprovided materials.
4. Adapt: **Full build** (artwork+verification) / **Image concept** (raster+fact checking) / **Layout specification** (coordinates and type sizes) / **Critique** (uploaded images only).
5. State deliverables honestly. Do not imply that a package installed in Claude Code is automatically present in ChatGPT or any other agent.

## Fidelity invariants across models
- Preserve the user's actual brief and exact required copy.
- Generate an *original concept* not merely an adjective pile.
- Rank hierarchy and legibility above visual effects.
- Critique the rendered artifact when available instead of grading the prompt.
- Record limitations (fake brand text, image distortion, missing editable layers, unavailable tools).

## Fallback prompt when the host doesn't support skills
Read `prompts/portable-activation.md` together with `SKILL.md` and the relevant `references/*` file. For a closed chat model without file browsing, paste these texts in a conversation and attach the brief/reference images. Use smaller reference subsets for small context windows.

## Verified documented skill locations (November 2026; recheck as tools change)
- Claude Code: project `.claude/skills/graphic-design-director/`; user `~/.claude/skills/graphic-design-director/`.
- Codex: project `.agents/skills/graphic-design-director/`; user `~/.agents/skills/graphic-design-director/`.
- Gemini CLI: project `.gemini/skills/graphic-design-director/`; user `~/.gemini/skills/graphic-design-director/`.
- Cursor: project `.cursor/skills/graphic-design-director/`; user `~/.cursor/skills/graphic-design-director/`.
- OpenCode: project `.opencode/skills/graphic-design-director/`; user `~/.config/opencode/skills/graphic-design-director/`.
- Other tools: follow the vendor's current skill directory or supply SKILL.md manually.

Sources to verify later:
- https://agentskills.io/specification
- https://learn.chatgpt.com/docs/build-skills
- https://geminicli.com/docs/cli/creating-skills/
- https://cursor.com/docs/skills
- https://opencode.ai/docs/skills
- https://code.claude.com/docs/en/skills
