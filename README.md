# Graphic Design Director

**A deep, model-neutral Agent Skill for graphic design, creative direction and visual critique.**

Graphic Design Director equips a compatible AI assistant with structured design judgment: interpreting briefs, developing original concepts, composing layouts, choosing typography and color, adapting references faithfully, preserving approved brand assets, and reviewing real outputs. It uses **the model and graphics tools already available in your environment**—no extra AI provider, external model API, or paid subscription is required by the skill.

> **Version:** 0.7.2 · **Format:** Agent Skills · **License:** MIT

## Install with npx

Requires Node.js and an Agent Skills-compatible environment.

```bash
npx skills add Elavn/graphic-design-director --skill graphic-design-director -g -y
```

The command installs the skill globally for supported agents selected by the Skills CLI. To see or choose available agents interactively, omit `-g -y`:

```bash
npx skills add Elavn/graphic-design-director
```

You can also inspect the installation options with `npx skills add --help`. For the manual/alternative installation process, see [INSTALL.md](skills/graphic-design-director/INSTALL.md).

**Repository layout:** the installable skill is under [`skills/graphic-design-director/`](skills/graphic-design-director/), with its entrypoint at [`SKILL.md`](skills/graphic-design-director/SKILL.md).

## What it does

| Capability | How it helps |
| --- | --- |
| Creative strategy | Translates a brief into a message, audience, idea and visual direction before decoration |
| Concept development | Explores distinct concepts and tests whether the idea reads clearly |
| Typography and composition | Builds hierarchy, legibility, grids, optical balance and purposeful visual rhythm |
| Color and art direction | Selects context-appropriate palettes, material treatments and imagery |
| Brand identity | Helps design and critique logos, wordmarks and coherent identity systems |
| Reference handling | Distinguishes **REPLICATE**, **ADAPT**, **INSPIRE**, **CREATE** and **HYBRID** tasks |
| Brand/asset fidelity | Preserves uploaded approved assets and respects explicit constraints |
| Quality review | Separates measurable correctness from artistic quality, with targeted revision cycles |
| Production checks | Includes optional local validation scripts and structured project contracts |

The skill is **not** a graphics generator on its own. Actual rendering, image editing, vector work and file exporting depend on the host application's capabilities.

## Try it

After installation, open your AI coding/design assistant and ask:

**Original campaign**

> Use Graphic Design Director to develop three genuinely different concepts for a music festival poster. Explain the visual idea behind each, choose a direction, create the artwork with the available tools, and critique the result against the brief.

**Faithful adaptation**

> Use Graphic Design Director in ADAPT mode for this supplied reference. Preserve the panel geometry, visual hierarchy and imagery style. Change only the requested copy and approved brand elements. Do not invent figures or redraw my logo.

**Brand identity**

> Use Graphic Design Director to create an identity direction for a repair studio. Explore distinctive wordmark construction, type hierarchy, application rules and a small identity system. Critique originality and legibility before delivery.

**Critique**

> Review this design as Graphic Design Director. Separate objective specification failures from subjective creative weaknesses. Identify the three most important revisions and explain what would improve.

You can explicitly name the skill when your host supports it; otherwise, compatible hosts may discover skills from their descriptions.

## Design philosophy

1. **The brief is the source of truth.** Dimensions, approved text, references, logos, color roles, and prohibited treatments are real constraints.
2. **Concept first, styling second.** An attractive template is not a substitute for a clear, original visual idea.
3. **Reference intent matters.** Replication and adaptation require fidelity; inspiration leaves creative freedom.
4. **Keep approved assets intact.** Do not substitute model-redrawn logos or fabricate facts to fill layouts.
5. **Review the actual output.** Check files, dimensions, layout, typography, image artifacts and creative quality separately.
6. **Be honest about capability.** If the host cannot render or reliably inspect something, disclose the limitation instead of claiming success.

## What's inside

```text
skills/graphic-design-director/
├── SKILL.md                  # Entry point and operating instructions
├── references/               # Core rules: concept, layout, color, typography, fidelity
│   └── deep/                 # Expanded professional design craft modules
├── evals/                    # Scenario-based critique and regression cases
├── scripts/                  # Optional validators and local project tools
├── schemas/                  # Optional structured contracts for design work
├── tests/                    # Technical tests
├── docs/WORKFLOW.md          # How the skill works in practice
├── INSTALL.md                # Alternative installation instructions
└── README.md                 # Detailed skill overview
```

## Validate a local checkout

Optional: these checks help contributors evaluate the package; they are **not** needed to activate the skill.

```bash
cd skills/graphic-design-director
python scripts/validate_skill.py
python -m pip install -r requirements-pipeline.txt
python -m unittest discover -s tests -v
```

Technical tests assess packaging and rule-related checks; **they do not certify creative excellence**. Judge actual designs with real briefs and visual review.

## Compatibility

Built for the [Agent Skills](https://agentskills.io/) convention and intended for compatible hosts including Codex, Claude Code, Gemini CLI, Cursor and OpenCode, subject to each host's version and skill discovery behavior. No separate model adapters or external AI API keys are required.

## License and attribution

Released under the [MIT License](skills/graphic-design-director/LICENSE) for the original instructions and code. It does not include or grant rights to third-party photos, fonts, logos, artwork or books.

See the skill's [detailed README](skills/graphic-design-director/README.md) and [release notes](skills/graphic-design-director/RELEASE-v0.7.1.md) for scope and limitations.
