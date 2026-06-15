---
name: blackhole-engine-api-query
description: Query and answer questions from bundled versioned BlackHole Engine Plus / BlackHole3D JavaScript API Markdown references. Use when the user asks about BlackHole Engine, BlackHole3D, BIM/GIS engine APIs, method parameters, return values, event names, module usage, code examples, release notes, SDK-version-specific API behavior, or differences across locally bundled SDK documentation.
---

# BlackHole Engine API Query

Use this skill to look up BlackHole Engine Plus / BlackHole3D JavaScript APIs from bundled SDK references.

## Versioned References

The bundled references are managed by `references/manifest.json`.

Current default:

- SDK: `BlackHole Engine SDK_V3.2.0.3757`
- Release date: `2026-05-22`
- Reference: `references/blackhole-engine-api.SDK_V3.2.0.3757.md`

## Compatibility Policy

Project guidance indicates most BlackHole Engine APIs are backward-compatible across SDK updates.

- When the user does not specify an SDK version, use the manifest default SDK reference.
- When the user specifies an SDK version, search that SDK reference if it is bundled.
- When only a newer bundled reference is available for an older SDK question, answer from the default reference but clearly say which SDK reference was used.
- Mention SDK version compatibility only when it matters, such as for removed APIs, deprecated APIs, parameter changes, return value changes, event names, initialization behavior, breaking changes, or release notes.
- Do not over-caveat ordinary method lookup answers; keep them practical.

## Quick Start

Prefer the query script before loading the full reference:

```bash
python scripts/query_api.py loadDataSet
python scripts/query_api.py loadDataSet --sdk SDK_V3.2.0.3757
python scripts/query_api.py loadDataSet --sdk latest
python scripts/query_api.py --list-sdks
python scripts/query_api.py "Model loadDataSet" --max-chars 12000
python scripts/query_api.py setData --titles --max-matches 20
```

Without `--sdk`, the script searches the manifest default SDK reference.

## Workflow

1. Extract the user's API name, module name, event name, or keyword.
2. Use `scripts/query_api.py --list-sdks` or read `references/manifest.json` when the answer needs SDK version, compatibility policy, or source metadata.
3. Run `scripts/query_api.py` with the most specific query first, adding `--sdk <version>` when the user specifies a version.
4. If multiple APIs share the same title, rerun with module context, such as `Water setData`, `Projection setData`, `Camera setCamLocateTo`, or `Model loadDataSet`.
5. Read only the returned sections unless the answer needs broader context.
6. Answer with the module path, method/event name, purpose, parameters, return value, example call, and any important notes from the reference. Include the SDK version when the user asks about version/current/latest behavior or the topic is version-sensitive.

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
python scripts/query_api.py loadDataSet --sdk 3.2.0.3690
python scripts/query_api.py setLogDepthEnable --sdk 3.2.0.3757
```

Use `rg -n` directly against the selected Markdown reference only when the script output is not enough.

## Answer Style

Keep answers practical and grounded in the reference:

- Include a concise JavaScript usage snippet when the section contains one.
- Mention the selected SDK version when version compatibility matters, or when the user asks about latest/current behavior.
- Mention whether the documented return value is `true/false`, an object, an array, or unspecified.
- If the reference section is incomplete or unclear, say so and provide the safest inference separately.
- Do not invent API behavior that is not in the bundled documentation.
