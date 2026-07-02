# bubblesplant's AI Skills

A collection of reusable agent skills for AI assistants.

> [!IMPORTANT]
> This repository bundles documentation-backed skills for AI agents. For production decisions, verify critical API behavior against the source documentation or runtime.

## Installation

Install this skill collection:

```bash
pnpx skills add bubblesplant/skills
```

Install all skills:

```bash
pnpx skills add bubblesplant/skills --skill='*'
```

Install globally:

```bash
pnpx skills add bubblesplant/skills --skill='*' -g
```

Learn more about the skills CLI at [vercel-labs/skills](https://github.com/vercel-labs/skills).

## Skills

Each skill is self-contained under `skills/<skill-name>`. A skill may include its own references, assets, or helper tools without changing the rest of this collection.

### Frontend Skills

| Name | Description |
| --- | --- |
| [create-bubbles](./skills/create-bubbles) | Create frontend apps with the `create-bubbles` CLI. Guides the user through Vue, React, Taro, NextJS, Electron, and monorego template choices, explains the main differences, then scaffolds the confirmed template. |
| [website-replica (experimental)](<./skills/website-replica(experimental)>) | **Experimental.** Replica workflow for existing websites and interactive pages. Uses a staged process: confirm scope, inspect original states with Playwright, output state dependencies and data flow, wait for user confirmation, then implement and compare screenshots until states match. |

### Workflow Skills

| Name | Description |
| --- | --- |
| [dev-team-orchestration](./skills/dev-team-orchestration) | Orchestrate a subagent team (PM → contract/architecture → frontend ‖ backend in parallel → integration → QA with Playwright → defect reflow) for full feature development from requirement to release. Forces human confirmation gates at the requirement, PRD, and contract stages; frontend and backend share one contract as the single source of truth. QA defaults to testing the built product with Playwright, and optionally inspects a reference site when the user provides a URL; it stops and asks the user on login walls, captchas, risk control, irreversible actions, or unreachable pages, never bypassing them. |

### Automation Skills

| Name | Description |
| --- | --- |
| [manage-prefixed-schedules](./skills/manage-prefixed-schedules) | **Testing only; installation is not recommended.** Manage AI-owned scheduled reminders, notifications, and scheduled jobs across Windows, macOS, and Linux by limiting operations to the `AI-Reminders` namespace and `AI-Reminder-` prefix. Defines safety boundaries, not command recipes. |

### Documentation Skills

| Name | Description |
| --- | --- |
| [blackhole-engine-api-query](./skills/blackhole-engine-api-query) | Search the latest bundled BlackHole Engine Plus / BlackHole3D JavaScript API docs, guide model resource URL discovery, and consult official SDK upgrade notes. Current API reference: `SDK_V3.2.0.3772` (`2026-06-12`). |

## FAQ

### What is this?

This repository stores reusable skills that AI assistants can load when they need domain-specific instructions and reference material.

### Which AI tools can use these skills?

Any assistant or agent runtime that supports the Agent Skills directory format can use them. The skills are not tied to a specific AI product.

### How are API references and upgrade notes handled?

Reference maintenance is handled inside each skill that needs it, not at the repository root.

For example, `blackhole-engine-api-query` stores its latest SDK metadata and compatibility policy in `skills/blackhole-engine-api-query/references/manifest.json`. It keeps one latest API Markdown reference and a generated `references/upgrade-notes.md` cache from the official update-note API.

BlackHole Engine APIs are treated as backward-compatible. Ordinary API lookup uses the latest bundled reference. Version-sensitive topics, such as SDK errors, upgrade regressions, deprecated APIs, parameter changes, return values, events, initialization behavior, and release notes, should be checked against `upgrade-notes.md`; refresh it with `node scripts/refresh_upgrade_notes.mjs` from inside the skill when latest update details matter.

## License

[MIT](./LICENSE)
