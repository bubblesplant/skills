# bubblesplant's AI Skills

English | [简体中文](./README.zh-CN.md)

A collection of reusable agent skills for frontend development, project AI rules, operating-system reminders, and BlackHole Engine API lookup.

## Skills at a glance

Click a skill name for details. Run the commands below from the target project's root directory; add `-g` to install globally.

| Skill | Brief description | Project installation |
| --- | --- | --- |
| [create-bubbles](#create-bubbles) | Create, customize, and validate BubblesJS frontend projects. | `pnpx skills add bubblesplant/skills --skill create-bubbles` |
| [bubblesjs-i18n](#bubblesjs-i18n) | Integrate BubblesJS i18n and maintain JSON and Excel translation catalogs. | `pnpx skills add bubblesplant/skills --skill bubblesjs-i18n` |
| [vue-vapor](#vue-vapor) | Develop, migrate, and troubleshoot Vue Vapor components. | `pnpx skills add bubblesplant/skills --skill vue-vapor` |
| [setup-project-agents](#setup-project-agents) | Set up agent instructions and rules in new or existing frontend and Node.js backend projects. | `pnpx skills add bubblesplant/skills --skill setup-project-agents` |
| [manage-prefixed-schedules](#manage-prefixed-schedules) | **Testing only; installation is not recommended.** Manage AI-owned operating-system reminders. | `pnpx skills add bubblesplant/skills --skill manage-prefixed-schedules` |
| [blackhole-engine-api-query](#blackhole-engine-api-query) | Query BlackHole3D APIs, model resource URLs, and SDK upgrade notes. | `pnpx skills add bubblesplant/skills --skill blackhole-engine-api-query` |

> [!IMPORTANT]
> This repository bundles documentation-backed skills for AI agents. For production decisions, verify critical API behavior against the source documentation or runtime.

## Installation

Interactively choose skills to install:

```bash
pnpx skills add bubblesplant/skills
```

Install all skills:

```bash
pnpx skills add bubblesplant/skills --skill='*'
```

Install all skills globally:

```bash
pnpx skills add bubblesplant/skills --skill='*' -g
```

Each skill below includes its own project and global installation commands. Run project installation commands from the target project's root directory; choose the global command to make a skill available across projects.

Installing all skills also includes the testing-only `manage-prefixed-schedules` skill; see its status below.

Learn more about the skills CLI at [vercel-labs/skills](https://github.com/vercel-labs/skills).

## Skill details

The collection currently includes six skills. Each lives under `skills/<skill-name>` with a `SKILL.md` entry point and may include references, rule templates, agent metadata, or helper scripts. The links below open each skill's instructions.

### Frontend Skills

#### [create-bubbles](./skills/create-bubbles/SKILL.md)

Create, customize, and validate frontend apps with the `create-bubbles` CLI. Compare Vue, React, Taro, NextJS, Electron, and React + NestJS monorepo templates, scaffold the confirmed template and directory, complete pages and app states, and maintain CLI templates.

Use for new frontend projects, existing generated apps, or `create-bubbles` template changes. Edits stay within the target app or relevant template directory; overwriting an existing non-empty directory requires an explicit user request.

**Installation:**

```bash
# Install in the current project
pnpx skills add bubblesplant/skills --skill create-bubbles

# Install globally
pnpx skills add bubblesplant/skills --skill create-bubbles -g
```

#### [bubblesjs-i18n](./skills/bubblesjs-i18n/SKILL.md)

Integrate and troubleshoot BubblesJS i18n in Vue 3, React, and JavaScript/TypeScript apps. Handle reactive locale switching, interpolation, loading, persistence, local scopes, and SSR; use the CLI to scan static translation keys, maintain JSON catalogs, check key presence, and synchronize Excel translation sheets. Applies to BubblesJS i18n tasks.

Use for BubblesJS i18n runtime, framework adapters, and CLI tasks. With an existing i18n solution, handle only the requested integration or migration scope. CLI `check` checks key presence, not translation completeness. Base APIs use a `0.0.2` source snapshot, and CLI guidance includes local source changes; verify the target project's installed features.

**Installation:**

```bash
# Install in the current project
pnpx skills add bubblesplant/skills --skill bubblesjs-i18n

# Install globally
pnpx skills add bubblesplant/skills --skill bubblesjs-i18n -g
```

#### [vue-vapor](./skills/vue-vapor/SKILL.md)

Develop, migrate, review, and troubleshoot Vue Vapor components. Confirm the target's compilation mode, then consult SPA/CSR or SSR/SSG/hydration guidance for configuration, components, runtime behavior, and ecosystem integration. Applies when Vapor is requested or the current task has Vapor-related evidence. Reference baseline: Vue `3.6.0-rc.10`.

Ordinary Vue tasks without Vapor-related evidence do not trigger this skill. Vapor use elsewhere in the repository does not prove the current component uses Vapor. Check compilation mode, type mode, and runtime interoperability separately; verify other Vue versions against their official tags.

**Installation:**

```bash
# Install in the current project
pnpx skills add bubblesplant/skills --skill vue-vapor

# Install globally
pnpx skills add bubblesplant/skills --skill vue-vapor -g
```

### Workflow Skills

#### [setup-project-agents](./skills/setup-project-agents/SKILL.md)

Set up agent instructions and development rules in new or existing frontend and Node.js backend projects through `AGENTS.md` and `.agents/rules` using bundled personal rule templates. Select assets for the actual scope of a single project or monorepo package, merge existing rules by meaning, adapt links, and condition React-specific rules on the project's configuration. Node.js backend projects currently use common code-design and shared-code rules; frontend rules apply only to frontend scopes.

Use for initial setup, adoption in existing projects, or explicitly requested missing rules. The skill does not change business code, dependencies, or build configuration. Template upgrades and existing rule migrations require an explicit request; later template changes do not automatically update configured projects.

**Installation:**

```bash
# Install in the current project
pnpx skills add bubblesplant/skills --skill setup-project-agents

# Install globally
pnpx skills add bubblesplant/skills --skill setup-project-agents -g
```

### Automation Skills

#### [manage-prefixed-schedules](./skills/manage-prefixed-schedules/SKILL.md)

**Testing only; installation is not recommended.** Manage operating-system reminders across Windows, macOS, and Linux within a directory explicitly provided by the user. Only manage resources associated with that directory and owned by the `AI-Reminders` namespace or `AI-Reminder-` prefix. Defines scheduling, visible system notification, and safety rules; implementation commands depend on the platform.

The user must explicitly provide the reminder management directory in the conversation. Unrelated system tasks are outside the scope. This skill manages operating-system reminders and does not substitute chat reminders or host-app automations.

**Installation (for testing):**

```bash
# Install in the current project
pnpx skills add bubblesplant/skills --skill manage-prefixed-schedules

# Install globally
pnpx skills add bubblesplant/skills --skill manage-prefixed-schedules -g
```

### Documentation Skills

#### [blackhole-engine-api-query](./skills/blackhole-engine-api-query/SKILL.md)

Query BlackHole Engine Plus / BlackHole3D JavaScript methods, parameters, return values, events, and examples; guide model resource URL discovery; consult official SDK upgrade notes for compatibility and migration issues. Bundled API reference: `SDK_V3.2.0.3808` (`2026-07-20`).

Use for BlackHole Engine, BlackHole3D, and related BIM/GIS engine API tasks. Ordinary lookup uses the bundled default reference; SDK errors, upgrade regressions, deprecations, and behavior changes also require upgrade-note checks. The bundled version identifies a documentation snapshot, not the latest online SDK.

**Installation:**

```bash
# Install in the current project
pnpx skills add bubblesplant/skills --skill blackhole-engine-api-query

# Install globally
pnpx skills add bubblesplant/skills --skill blackhole-engine-api-query -g
```

## FAQ

### What is this?

This repository stores reusable skills that AI assistants can load when they need domain-specific instructions and reference material.

### Which AI tools can use these skills?

Any assistant or agent runtime that supports the Agent Skills directory format can use them. The skills are not tied to a specific AI product.

### How should I use version-specific guidance?

Check the target project's installed packages and configuration against the selected skill's references.

- `vue-vapor` is based on Vue `3.6.0-rc.10`. Ordinary Vue tasks without Vapor-related evidence do not trigger this skill.
- `bubblesjs-i18n` uses a `0.0.2` source snapshot for its base APIs, with CLI guidance also incorporating local source changes. Verify installed package exports and `bubbles-i18n --help`, especially before using Excel commands.
- The BlackHole SDK version above identifies the bundled API snapshot. It does not confirm the latest online SDK release.

### How are API references and upgrade notes handled?

Reference maintenance is handled inside each skill that needs it, not at the repository root.

For example, `blackhole-engine-api-query` stores its bundled SDK metadata and compatibility policy in [references/manifest.json](./skills/blackhole-engine-api-query/references/manifest.json). It keeps one API Markdown reference and an [upgrade-notes.md](./skills/blackhole-engine-api-query/references/upgrade-notes.md) cache generated from the official update-note API.

The skill's maintenance policy treats BlackHole Engine APIs as backward-compatible, so ordinary API lookup uses the bundled default reference, including when an older SDK is requested. Version-sensitive topics, such as SDK errors, upgrade regressions, deprecated APIs, parameter changes, return values, events, initialization behavior, and release notes, should be checked against `upgrade-notes.md`.

When recent SDK updates or upgrade issues matter, refresh the notes from the repository root when network access is available:

```bash
node skills/blackhole-engine-api-query/scripts/refresh_upgrade_notes.mjs
```

If refresh fails, use the cached notes. This script updates the upgrade-note cache only; replacing the bundled API manual and updating its manifest is a separate maintenance step.

## License

[MIT](./LICENSE)
