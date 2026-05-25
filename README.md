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

### Documentation Skills

| Name | Description |
| --- | --- |
| [blackhole-engine-api-query](./skills/blackhole-engine-api-query) | Search locally bundled, versioned BlackHole Engine Plus / BlackHole3D JavaScript API docs. Current default: `SDK_V3.2.0.3690` (`2026-04-17`). |

## FAQ

### What is this?

This repository stores reusable skills that AI assistants can load when they need domain-specific instructions and reference material.

### Which AI tools can use these skills?

Any assistant or agent runtime that supports the Agent Skills directory format can use them. The skills are not tied to a specific AI product.

### How are versioned references handled?

Versioning is handled inside each skill that needs it, not at the repository root.

For example, `blackhole-engine-api-query` stores its SDK version metadata and compatibility policy in `skills/blackhole-engine-api-query/references/manifest.json`, and keeps each API reference as a separate versioned Markdown file.

BlackHole Engine APIs are treated as mostly backward-compatible. If no SDK version is specified, the skill uses its manifest default reference. Version-sensitive topics, such as deprecated APIs, parameter changes, return values, events, initialization behavior, and release notes, should still be checked against the relevant SDK when possible.

## License

[MIT](./LICENSE)
