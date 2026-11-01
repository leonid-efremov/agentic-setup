# agentic-setup
Personal setup for agentic development with OpenCode. Spec-driven gated workflow for complex projects.

## Overview
6 primary agents covering the full development cycle:
```
spec → plan → build → test → code-review → document
```

Each agent has a focused role with explicit gates between stages. The workflow ensures design happens before code, and every change is tested and reviewed.

## Usage

Requires OpenCode v2 and Python 3.13 with `pyyaml`. The manager compiles
`agents/*.md` + `permissions.yaml` into the adapter directory
`.config/opencode-custom/` (gitignored):

```bash
# generate / refresh the custom profile
python agent_manager.py opencode-on

# start OpenCode with the generated profile
export OPENCODE_CONFIG_DIR="$PWD/.config/opencode-custom"
opencode
```

```bash
# remove the generated agent files (cli.json is preserved)
python agent_manager.py opencode-off
```

The manager writes `agents/*.md` in OpenCode v2 frontmatter format. Built-in
agents remain available: `explore` and `general` subagents, plus the hidden
`compaction`, `summary`, and `title` system agents. Local `build.md` and
`plan.md` intentionally override the built-in primary agents of the same name.

## Agents
| Agent | Stage | When to Use |
|-------|-------|-------------|
| `spec` | Specify | New projects, complex features, multi-capability requirements |
| `plan` | Plan | After spec approval; decompose into tasks with acceptance criteria |
| `build` | Implement | Implement tasks from a plan, incrementally |
| `test` | Test | TDD, bug reproduction, coverage analysis |
| `code-review` | Review | Before commit; 5-axis quality review |
| `document` | Docs | ADRs, README updates, agent-facing documentation |

## Workflow Selection
| Scenario | Use |
|----------|-----|
| New project, complex feature | Full gated workflow (all 6 agents) |
| Small bugfix, routine edit | Skip to `build` |
| Codebase research | `explore` subagent |
| Parallel investigation | `general` subagent |

## Agent Permissions
Tool boundaries live in `permissions.yaml`. The adapter translates them into the
OpenCode v2 `permission` frontmatter field:

| Agent | `edit` boundary | Rationale |
|-------|-----------------|-----------|
| `spec` | only `docs/**` and root `*.md` | designs, must not touch code |
| `plan` | only `docs/**` and root `*.md` | decomposes, must not touch code |
| `document` | only `docs/**` and root `*.md` | documents, must not change logic |
| `build` | `src/**`, `lib/**`, root `*.toml` | implements code |
| `test` | `tests/**`, root `*.toml`, `pytest.ini` | writes tests/fixes |
| `code-review` | `deny` | read-only reviewer — reports, never edits |

Write/command lists become a glob → action map with `"*": deny` first, so
anything not explicitly listed is blocked. `code-review` has no write or shell
access at all. Read-only agents still get read access; only `edit` and `bash`
are constrained here. Extend `permissions.yaml` to tighten other tools.

## Repository Structure
```
agent_manager.py          CLI: opencode-on / opencode-off
agent_config.py           Loads agents + permissions.yaml
adapters/opencode2.py     Compiles agents into OpenCode v2 frontmatter
agents/                   Agent definitions (markdown + YAML frontmatter)
permissions.yaml          Per-agent tool permissions
references/               Templates, common instructions, shared docs
skills/                   OpenCode skills (optional)
AGENTS.md                 Project-level agent workflow instructions
```

`.config/opencode-custom/` is generated and gitignored. It contains the compiled
`agents/*.md` and an optional user-managed `cli.json`; `opencode-off` removes
only the generated `agents/` directory.

## References
- [agent-skills](https://github.com/addyosmani/agent-skills) — base principles and main concept
- [OpenSpec](https://github.com/Fission-AI/OpenSpec/tree/main) — spec-driven development framework
- [OpenCode Docs](https://opencode.ai/docs) — OpenCode configuration and agents
