# Graphic Design Director — npx-ready Agent Skill

Model-neutral graphic-design art direction skill. The design knowledge is unchanged from v0.7.2. No third-party AI service or API key is required.

## Install with the standard Skills CLI

Install it from GitHub:

```sh
npx skills add Elavn/graphic-design-director --skill graphic-design-director -g -a codex -y
```

Change `codex` to `claude-code`, `gemini`, `cursor`, or `opencode`, or omit `-a` to choose interactively. Remove `-g` to install for the current project instead.

For installation from a local clone, run:

```sh
npx skills add . --skill graphic-design-director -g -a codex -y
```

The `skills` CLI downloads the installer from npm the first time; Node.js/npm and an internet connection are needed. This repository has not been published to GitHub, so `Elavn/graphic-design-director` is a placeholder, not an active link.

Alternatively, the included standalone Node installer tarball supports `npx --yes --package=./graphic-design-director-installer-0.7.2.tgz graphic-design-director install --agent codex --scope user` after download, and requires no npm registry access.

## What gets installed

The directory `skills/graphic-design-director/` contains the authoritative `SKILL.md`, reference library and optional validation tools. No external model adapters. Installation does not run design generation or require Python to load the skill.

## Verify

```sh
npx skills list -g
```

For offline structural integrity, `MANIFEST.json` contains SHA-256 hashes of all 80 original skill files. The manifest is outside the installed skill directory.

License: see `skills/graphic-design-director/LICENSE`.
