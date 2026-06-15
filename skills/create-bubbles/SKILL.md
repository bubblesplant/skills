---
name: create-bubbles
description: Create, customize, and validate frontend projects with the create-bubbles CLI and BubblesJS templates. Use when Codex needs to scaffold a frontend app, ask the user to choose Vue/React/Taro/NextJS/Electron templates, explain template differences, add pages/components/routes/state, adapt an existing generated frontend, or update create-bubbles templates.
---

# Create Bubbles

## Core Workflow

Use the existing `create-bubbles` CLI and templates as the starting point whenever the user asks to create a frontend project. Treat the generated app as the first draft, then complete the requested product experience inside that app.

1. Inspect the local context before acting.
   - If inside the BubblesJS monorepo, read `packages/create-bubbles/package.json`, `packages/create-bubbles/src/index.ts`, and the relevant `packages/create-bubbles/template-*` directory.
   - Prefer the package manager declared by `packageManager`; in this repo that is usually `pnpm`.
   - Check whether the target directory already exists. Do not remove or overwrite user files unless the user clearly asked for it.

2. Guide the template choice before scaffolding.
   - If the user already named a framework, template, or platform, confirm the closest template and explain why in one short sentence.
   - If the request is ambiguous, ask whether they want Vue, React, Taro, NextJS, Electron, or a full-stack monorepo. Present only the relevant choices when the request narrows the domain.
   - Explain the main tradeoffs in the same message so the user can choose without opening source files.
   - Do not run the scaffold command until the user confirms the template and target directory.

3. Present these template options.
   - `vue-vite-eslint`: Vue 3 SPA with Vite and ESLint. Prefer for Vue admin pages, dashboards, component demos, and conventional browser apps.
   - `react-rsbuild-biome`: React app with Rsbuild and Biome. Prefer for fast React apps that should use Rsbuild and built-in formatting/linting through Biome.
   - `vp-react`: Vite React app. Prefer for lightweight React SPAs and simple product prototypes.
   - `vp-react-shadcn`: React app with shadcn-style UI. Prefer for dashboards, forms, settings pages, and component-heavy tools.
   - `vp-monorepo-react-nestjs`: React + NestJS monorepo. Prefer when the user needs frontend plus backend/API in one repo.
   - `taro-vue-eslint`: Taro Vue mini-app. Prefer for mini-program/mobile cross-platform work with Vue.
   - `taro-react-oxc`: Taro React mini-app. Prefer for mini-program/mobile cross-platform work with React and Oxc tooling.
   - `nextjs-vinext-eslint`: NextJS/Vinext app. Prefer for SSR, file routing, content-heavy sites, SEO, or server-side rendering needs.
   - `create-eletron-vite`: Electron app through `pnpm create electron-vite@latest`. Prefer for desktop apps.

4. Ask with a compact menu when the user has not chosen.

Localize this menu to the user's language when helpful:

```text
Which template do you want to use? I suggest choosing by target:
1. Vue SPA: vue-vite-eslint - Vue 3 + Vite + ESLint, good for standard frontend apps.
2. React Rsbuild: react-rsbuild-biome - React + Rsbuild + Biome, good for engineered React apps.
3. React Vite: vp-react - lightweight React SPA.
4. React shadcn: vp-react-shadcn - good for dashboards, forms, and component-heavy screens.
5. React + NestJS: vp-monorepo-react-nestjs - frontend + backend monorepo.
6. Taro Vue: taro-vue-eslint - Vue mini-app and cross-platform mobile.
7. Taro React: taro-react-oxc - React mini-app and cross-platform mobile.
8. NextJS: nextjs-vinext-eslint - SSR, SEO, and file-based routing.
9. Electron: create-eletron-vite - desktop app.

After you confirm the template and project directory, I will scaffold it with create-bubbles.
```

5. Scaffold with the CLI after confirmation.
   - Use `pnpm create bubbles <target-dir> -t <template>` for a published package flow.
   - Use `pnpm dlx create-bubbles <target-dir> -t <template>` when `pnpm create bubbles` is unavailable.
   - When developing the CLI locally, build first if needed, then run the generated bin from `packages/create-bubbles`.
   - Pass `--overwrite` only when the user explicitly wants to replace an existing non-empty target.

6. Finish the frontend, not just the scaffold.
   - Build the usable first screen requested by the user; do not leave a generic template landing page unless the request is a landing page.
   - Reuse the selected template's stack, aliases, router, styling, lint rules, and file layout.
   - Add real app states: empty, loading, error, success, and validation states when relevant.
   - Keep UI controls familiar and dense enough for the app type. Use existing icon, component, CSS, and utility patterns before introducing new dependencies.
   - Keep edits scoped to the generated app or the relevant `template-*` folder.

7. Validate the result.
   - Run the available local scripts such as `pnpm install`, `pnpm lint`, `pnpm typecheck`, `pnpm build`, or template-specific equivalents.
   - If dependency installation needs network access, ask for approval or explain the limitation.
   - For visible frontend work, start the dev server and inspect the app in a browser when browser tooling is available.
   - Fix obvious layout issues, console errors, broken imports, missing assets, and type errors before reporting completion.

## Updating create-bubbles Templates

When the task is to add or change a template inside the `create-bubbles` package:

1. Add or edit the matching `packages/create-bubbles/template-*` directory.
2. Update `FRAMEWORKS`, `TEMPLATES`, and `helpMessage` in `packages/create-bubbles/src/index.ts` when adding a new template.
3. Keep the generated `package.json` valid after the CLI replaces `name`.
4. Preserve special package-file behavior such as `_gitignore` being renamed to `.gitignore`.
5. Build and smoke-test the CLI with a temporary target directory.
6. Remove only temporary test output that was created during the task.

## Response Style

In the final response, include the selected template, the app path, the important files changed, and the validation commands that passed or could not be run. Keep it short and actionable.
