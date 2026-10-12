# bubblesplant's AI Skills

A collection of reusable agent skills for frontend development, project AI rules, operating-system reminders, and BlackHole Engine API lookup.

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

Install a specific skill:

```bash
pnpx skills add bubblesplant/skills --skill bubblesjs-i18n
```

Learn more about the skills CLI at [vercel-labs/skills](https://github.com/vercel-labs/skills).

## Skills

The collection currently includes six skills. Each lives under `skills/<skill-name>` with a `SKILL.md` entry point and may include references, rule templates, agent metadata, or helper scripts. The links below open each skill's instructions.

### Frontend Skills

| Name | Description |
| --- | --- |
| [create-bubbles](./skills/create-bubbles/SKILL.md) | Create, customize, and validate frontend apps with the `create-bubbles` CLI. Compare Vue, React, Taro, NextJS, Electron, and React + NestJS monorepo templates, scaffold the confirmed template and directory, complete pages and app states, and maintain CLI templates. |
| [bubblesjs-i18n](./skills/bubblesjs-i18n/SKILL.md) | Integrate and troubleshoot BubblesJS i18n in Vue 3, React, and JavaScript/TypeScript apps. Handle reactive locale switching, interpolation, loading, persistence, local scopes, and SSR; use the CLI to scan static translation keys, maintain JSON catalogs, check key presence, and synchronize Excel translation sheets. Applies to BubblesJS i18n tasks. |
| [vue-vapor](./skills/vue-vapor/SKILL.md) | Develop, migrate, review, and troubleshoot Vue Vapor components. Confirm the target's compilation mode, then consult SPA/CSR or SSR/SSG/hydration guidance for configuration, components, runtime behavior, and ecosystem integration. Applies when Vapor is requested or the current task has Vapor-related evidence. Reference baseline: Vue `3.6.0-rc.10`. |

### Workflow Skills

| Name | Description |
| --- | --- |
| [init-agent-rules](./skills/init-agent-rules/SKILL.md) | Initialize or fill gaps in project `AGENTS.md` and `.agents/rules` using bundled personal rule templates. Select assets for the actual scope of a single project or monorepo package, merge existing rules by meaning, adapt links, and condition React-specific rules on the project's configuration. Changes stay within rule documents and their necessary links. |

### Automation Skills

| Name | Description |
| --- | --- |
| [manage-prefixed-schedules](./skills/manage-prefixed-schedules/SKILL.md) | **Testing only; installation is not recommended.** Manage operating-system reminders across Windows, macOS, and Linux within a directory explicitly provided by the user. Only manage resources associated with that directory and owned by the `AI-Reminders` namespace or `AI-Reminder-` prefix. Defines scheduling, visible system notification, and safety rules; implementation commands depend on the platform. |

### Documentation Skills

| Name | Description |
| --- | --- |
| [blackhole-engine-api-query](./skills/blackhole-engine-api-query/SKILL.md) | Query BlackHole Engine Plus / BlackHole3D JavaScript methods, parameters, return values, events, and examples; guide model resource URL discovery; consult official SDK upgrade notes for compatibility and migration issues. Bundled API reference: `SDK_V3.2.0.3808` (`2026-07-20`). |

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
