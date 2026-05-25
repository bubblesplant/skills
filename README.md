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

### Documentation Skills

| Name | Description |
| --- | --- |
| [blackhole-engine-api-query](./skills/blackhole-engine-api-query) | Search bundled BlackHole Engine Plus / BlackHole3D JavaScript API docs and return practical usage details. |

## FAQ

### What is this?

This repository stores reusable skills that AI assistants can load when they need domain-specific instructions and reference material.

### Which AI tools can use these skills?

Any assistant or agent runtime that supports the Agent Skills directory format can use them. The skills are not tied to a specific AI product.

### Where does the BlackHole Engine reference come from?

The `blackhole-engine-api-query` skill searches the bundled Markdown reference at `skills/blackhole-engine-api-query/references/blackhole-engine-api.md`.

## License

[MIT](./LICENSE)
