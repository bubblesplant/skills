---
name: blackhole-engine-api-query
description: Query and answer questions from the latest bundled BlackHole Engine Plus / BlackHole3D JavaScript API Markdown reference, plus curated SDK upgrade notes. Use when the user asks about BlackHole Engine, BlackHole3D, BIM/GIS engine APIs, model resource URLs, method parameters, return values, event names, module usage, code examples, recent SDK updates, SDK upgrade errors, compatibility issues, or migration guidance.
---

# BlackHole Engine API Query

Use this skill to look up BlackHole Engine Plus / BlackHole3D JavaScript APIs from the latest bundled SDK reference.

## References

The bundled references are managed by `references/manifest.json`.

Current API reference:

- SDK: `BlackHole Engine SDK_V3.2.0.3772`
- Release date: `2026-06-12`
- Reference: `references/blackhole-engine-api.SDK_V3.2.0.3772.md`
- Upgrade notes: `references/upgrade-notes.md`
- Upgrade notes API: `https://developer.bjblackhole.com/api/developercenter/Doc/DocItem/list/bydcid?dcid=3a0b9cac-880a-697b-9bf4-6328c4b94612`
- Upgrade notes refresh script: `scripts/refresh_upgrade_notes.mjs`

## Maintenance Policy

Project guidance indicates BlackHole Engine APIs are backward-compatible across SDK updates.

- Maintain only one latest API Markdown reference.
- When the user does not specify an SDK version, use the latest API reference.
- When the user specifies an older SDK version for ordinary API lookup, still use the latest API reference and briefly say the docs are maintained as latest-only because APIs are backward-compatible.
- When the user asks about recent/latest updates, or reports an SDK error, upgrade issue, changed behavior, missing API, runtime exception, deprecation, parameter change, event-name issue, initialization issue, or breaking behavior, refresh `references/upgrade-notes.md` from the API when network is available, then read it before answering.
- Do not over-caveat ordinary method lookup answers; keep them practical.

## Quick Start

Prefer the query script before loading the full reference:

```bash
python scripts/query_api.py loadDataSet
python scripts/query_api.py loadDataSet --sdk SDK_V3.2.0.3772
python scripts/query_api.py loadDataSet --sdk latest
python scripts/query_api.py --list-sdks
python scripts/query_api.py "Model loadDataSet" --max-chars 12000
python scripts/query_api.py setData --titles --max-matches 20
node scripts/refresh_upgrade_notes.mjs --dry-run
node scripts/refresh_upgrade_notes.mjs
```

Without `--sdk`, the script searches the latest API reference. If an older SDK is passed with `--sdk`, the script falls back to the latest reference.

## Model Resource URL Guidance

When a task needs a model resource URL and the user has not provided one, or when the user asks how to find the model URL, guide them through the BlackHole platform preview flow:

1. Open the model in the BlackHole platform and enter model preview.
2. Open browser DevTools with `F12`, then switch to the Console panel.
3. Find a printed URL similar to:

```text
https://xxx/newblackholeapi/engineweb/blackhole3D/EngineRes/RequestEngineRes?dir=url_res02&path=3a1dc5d88820f8d47940acf5f13d5a81/hugemodel/
```

4. The model resource URL is the same `RequestEngineRes` URL, but with the trailing `/hugemodel/` removed from the `path` value:

```text
https://xxx/newblackholeapi/engineweb/blackhole3D/EngineRes/RequestEngineRes?dir=url_res02&path=3a1dc5d88820f8d47940acf5f13d5a81
```

Preserve the original host, path prefix, `dir`, and resource hash. Only remove the final `hugemodel/` segment and trailing slash from the `path` query parameter.

## Workflow

1. Extract the user's API name, module name, event name, or keyword.
2. For ordinary API lookup, run `scripts/query_api.py` with the most specific query first.
3. If the user specifies an older SDK version, still query the latest API reference and mention the latest reference used only when it matters.
4. If the user needs a model resource URL but has not provided one, use the Model Resource URL Guidance before asking for more details.
5. If multiple APIs share the same title, rerun with module context, such as `Water setData`, `Projection setData`, `Camera setCamLocateTo`, or `Model loadDataSet`.
6. If the user asks about recent/latest updates or reports an SDK error or upgrade problem, run `node scripts/refresh_upgrade_notes.mjs` when network is available; if refresh fails, use the cached `references/upgrade-notes.md`.
7. Search `references/upgrade-notes.md` with exact API names, module names, SDK versions, and error keywords before answering upgrade-sensitive questions.
8. Read only the returned API sections or relevant upgrade-note entries unless the answer needs broader context.
9. Answer with the module path, method/event name, purpose, parameters, return value, example call, and any important notes from the reference. Include upgrade-note findings only when the issue is version-sensitive.

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
python scripts/query_api.py setLogDepthEnable --sdk 3.2.0.3772
python scripts/query_api.py setShpSelClr --sdk 3.2.0.3772
rg -n "体剖切|Projection|setShpSelClr|SDK_V3.2.0.3772" references/upgrade-notes.md
```

Use `rg -n` directly against the selected Markdown reference only when the script output is not enough.

## Answer Style

Keep answers practical and grounded in the reference:

- Include a concise JavaScript usage snippet when the section contains one.
- Mention the latest API reference version when version compatibility matters, or when the user asks about latest/current behavior.
- Mention whether the documented return value is `true/false`, an object, an array, or unspecified.
- If the reference section is incomplete or unclear, say so and provide the safest inference separately.
- Do not invent API behavior that is not in the bundled documentation.
