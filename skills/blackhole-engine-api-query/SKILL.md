---
name: blackhole-engine-api-query
description: Query and answer questions from a bundled BlackHole Engine Plus JavaScript API Markdown document generated from output.md. Use when the user asks about BlackHole Engine, BlackHole3D, BIM/GIS engine APIs, method parameters, return values, event names, module usage, code examples, or release notes from the local API documentation.
---

# BlackHole Engine API Query

Use this skill to look up BlackHole Engine Plus / BlackHole3D JavaScript APIs from the bundled Markdown reference.

## Quick Start

Prefer the query script before loading the full reference:

```bash
python scripts/query_api.py loadDataSet
python scripts/query_api.py "Model loadDataSet" --max-chars 12000
python scripts/query_api.py setData --titles --max-matches 20
```

The script searches `references/blackhole-engine-api.md`, which is copied from the user's `output.md`.

## Workflow

1. Extract the user's API name, module name, event name, or keyword.
2. Run `scripts/query_api.py` with the most specific query first.
3. If multiple APIs share the same title, rerun with module context, such as `Water setData`, `Projection setData`, `Camera setCamLocateTo`, or `Model loadDataSet`.
4. Read only the returned sections unless the answer needs broader context.
5. Answer with the module path, method/event name, purpose, parameters, return value, example call, and any important notes from the reference.

## Ambiguity Handling

Many methods are repeated across modules, especially names such as `setData`, `getData`, `setVisible`, and `getVisible`.

When results are ambiguous:

- Use `--titles --max-matches 20` to list candidate sections.
- Ask for the module only if the surrounding user request does not imply one.
- Keep original spellings from the docs when they matter, including documented typos such as `renderHieght`.

## Broad Searches

For concepts that are not exact API names, search keywords:

```bash
python scripts/query_api.py getTransGeoCoords
python scripts/query_api.py RESystemMouseMove
python scripts/query_api.py "V3.2.0.3690" --max-matches 8
```

Use `rg -n` directly against `references/blackhole-engine-api.md` only when the script output is not enough.

## Answer Style

Keep answers practical and grounded in the reference:

- Include a concise JavaScript usage snippet when the section contains one.
- Mention whether the documented return value is `true/false`, an object, an array, or unspecified.
- If the reference section is incomplete or unclear, say so and provide the safest inference separately.
- Do not invent API behavior that is not in the bundled documentation.
