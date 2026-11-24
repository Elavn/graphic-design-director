# Installing Graphic Design Director v0.7.2

This is an **Agent Skills** folder containing `SKILL.md` and focused design references. Its output quality depends on the active model and its available image/vector tools. No external AI provider or API key is required by the skill.

## Download and verify

Choose **one** installation method. Do not install the same skill into both native and compatibility directories for the same agent unless you deliberately want duplicates.

### A. Gemini CLI (direct `.skill` package)

```sh
gemini skills install ./graphic-design-director-v0.7.2.skill --scope user
```

Run `/skills reload` in the interactive Gemini session, then `/skills list`.

### B. Windows, macOS, Linux — bundled installer (Python 3)

Download `graphic-design-director-v0.7.2.skill` and `install_graphic_design_director.py` into the same directory, then run:

```sh
python install_graphic_design_director.py graphic-design-director-v0.7.2.skill --agent codex --scope user
python install_graphic_design_director.py graphic-design-director-v0.7.2.skill --agent claude --scope user
python install_graphic_design_director.py graphic-design-director-v0.7.2.skill --agent gemini --scope user
python install_graphic_design_director.py graphic-design-director-v0.7.2.skill --agent cursor --scope project --project .
python install_graphic_design_director.py graphic-design-director-v0.7.2.skill --agent opencode --scope project --project .
```

To preview paths first, append `--dry-run`. To replace an existing skill, append `--replace` (it backs up the old directory). To verify a previously installed skill, use `--verify`. A clean install refuses to overwrite existing files.

Alternatively extract the `.skill` ZIP; copy the **entire** `graphic-design-director/` folder to the selected skills directory, preserving the directory name and `SKILL.md`.

| Agent | User-wide location | Project location |
|---|---|---|
| Claude Code | `~/.claude/skills/graphic-design-director/` | `.claude/skills/graphic-design-director/` |
| Codex | `~/.agents/skills/graphic-design-director/` | `.agents/skills/graphic-design-director/` |
| Gemini CLI | `~/.gemini/skills/graphic-design-director/` | `.gemini/skills/graphic-design-director/` |
| Cursor | `~/.cursor/skills/graphic-design-director/` | `.cursor/skills/graphic-design-director/` |
| OpenCode | `~/.config/opencode/skills/graphic-design-director/` | `.opencode/skills/graphic-design-director/` |

`~` is your user home directory, including on Windows when using the installer. Check agent-specific discovery in your installed version.

## Activate

Claude Code: type `/graphic-design-director` or ask for a graphic-design task. Other compatible agents typically load a skill based on the description; invoke by name when supported. Gemini CLI: `/skills list`, or `gemini skills list --all`.

Example: **Use Graphic Design Director to design a poster for a community event. Start by identifying the brief constraints and explore at least three distinct creative concepts. Then create the artwork using available tools and perform separate correctness and design-quality reviews.**

## Verify the installation

```sh
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

The commands above are run **inside the installed skill folder**. Some optional pipeline tests require the dependencies in `requirements-pipeline.txt`. Those tests are *not* required for skill loading.

This package is an installable **Agent Skill**, not a ChatGPT web plugin or an automatically installed account-level skill. It does not automatically install itself into remote machines or apps.
