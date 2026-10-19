---
name: create-bubbles
description: 指导 AI 选择并直接拉取 BubblesJS 项目模板，从本地模板目录或 Git 仓库初始化 Vue、React、Taro 小程序、Next.js 和 monorepo 项目，无需运行脚手架 CLI。适用于创建项目、获取模板或比较模板选型；已有项目的普通页面修改不触发重新初始化。
---

# Bubbles 项目模板拉取

根据用户需求选模板，将模板目录的内容直接复制到项目根目录，再按需安装依赖和验证。项目创建由 AI 完成，不运行 `create-bubbles`、`pnpm create bubbles`、`pnpm dlx create-bubbles` 或其他脚手架 CLI。

## 默认推荐

- 用户不懂技术选型、没有框架偏好，或只说做网站、后台、管理系统、普通前端项目：默认推荐并使用 **`template-vue-vp-eslint`**。
- 用户要做微信等小程序，没有框架偏好：默认推荐并使用 **`template-taro-vue-eslint`**。
- 用户明确指定框架、模板、运行平台或全栈需求时，优先满足明确要求。例如，React 小程序使用 `template-taro-react-oxc`，React + NestJS 全栈项目使用 `template-vp-monorepo-react-nestjs`。
- 用一句中文说明推荐理由即可，不要求用户理解或逐项比较所有技术方案。用户已授权创建项目且目录可确定时直接继续，不强制二次确认模板；只有影响落地的关键信息缺失时才提问。
- 用户只咨询模板时，给出建议和差异，不自行创建项目。已有项目的功能修改沿用现有技术栈，只有用户要求重新初始化或迁移时才重新拉取模板。

推荐话术示例：

> 普通网页项目默认用 `template-vue-vp-eslint`，适合常见页面和后台应用，我会直接获取这个模板。
>
> 小程序默认用 `template-taro-vue-eslint`，基于 Taro + Vue，我会直接获取这个模板。

## 模板目录与用途

模板位于 BubblesJS 仓库的 `packages/create-bubbles/` 下。下表使用**真实目录名**；源码中的变体名称不带 `template-` 前缀。

| 模板目录 | 技术栈与适用场景 |
| --- | --- |
| `template-vue-vp-eslint` | Vue + Vite+（`vp`）+ ESLint；普通前端项目的默认推荐 |
| `template-vp-vue-eslint-vapor` | Vue + Vite+ + ESLint + Vapor；明确要求 Vapor 时选择 |
| `template-react-rsbuild-biome` | React + Rsbuild + Biome；明确需要该工具链的 React 项目 |
| `template-vp-react` | React + Vite+；常规 React 网页项目 |
| `template-vp-react-shadcn` | React + Vite+ + shadcn；需要现成界面组件的 React 项目 |
| `template-vp-monorepo-react-nestjs` | React + NestJS monorepo；前后端一体项目 |
| `template-pnpm-vp-monorepo` | pnpm workspace + Vite+ monorepo；多包、组件库及文档站等需求 |
| `template-taro-vue-eslint` | Taro + Vue + ESLint；小程序的默认推荐 |
| `template-taro-react-oxc` | Taro + React + Oxc；明确使用 React 的小程序 |
| `template-nextjs-vinext-eslint` | Next.js + Vinext + ESLint；有服务端渲染、文件路由等需求的项目 |

选项以当前来源仓库的 `packages/create-bubbles/src/index.ts` 中 `FRAMEWORKS` 和实际模板目录为准；获取后核对选中模板的 `package.json`，不要沿用过时的 `template-vue-vite-eslint` 名称，也不要把 `vp` 当成普通 Vite。

源码中的 `create-eletron-vite` 是通过 `customCommand` 调用第三方 Electron 脚手架的入口，没有对应的 BubblesJS 模板目录。遇到桌面项目，应查明 Electron 官方模板的真实仓库与目录并直接获取，不能拼出不存在的 `template-create-eletron-vite`，也不能因此自动执行脚手架命令。目录存在但未在 `FRAMEWORKS` 注册的模板，不作为默认选项；用户点名时先核实完整性。

## 直接获取模板

### 1. 确定目标目录和模板来源

- 沿用用户已给出的项目名、目标目录、仓库、分支或提交；没有项目名时可使用 `bubbles-project`。当前目录仅在用户要求或上下文明确且可安全写入时作为项目根目录。
- 先检查目标目录。非空目录中的原有文件不能被直接覆盖；按已有授权处理，存在未授权的冲突时展示冲突并询问，或使用可确定的新目录。
- 用户指定了本地 BubblesJS 仓库时，直接读取该仓库的 `packages/create-bubbles/src/index.ts` 和选中模板，再复制模板内容。不要修改模板源目录，也不要擅自更新或切换用户已有仓库。例如，本地仓库为 `C:\malei\stu\bubbles` 时，默认网页模板在 `C:\malei\stu\bubbles\packages\create-bubbles\template-vue-vp-eslint`。
- 没有指定可用的本地来源时，从 `https://github.com/435012357/bubblesjs.git` 获取对应目录。未指定版本时使用远端默认分支的当前版本，不硬编码分支名；需要复现时记录实际提交。

### 2. 远程获取时只检出所需目录

可使用 Git 浅克隆与稀疏检出。以下以默认网页模板为例，将占位路径替换为本次任务的真实缓存路径；选择其他模板时替换最后一个目录：

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/435012357/bubblesjs.git "<本次下载缓存目录>"
git -C "<本次下载缓存目录>" sparse-checkout set packages/create-bubbles/src packages/create-bubbles/template-vue-vp-eslint
git -C "<本次下载缓存目录>" rev-parse HEAD
```

稀疏检出会同时保留父目录中的文件，可据此读取 `packages/create-bubbles/package.json`。用户指定分支、标签或提交时按该版本获取，不能静默换成默认分支；浅克隆不含指定提交时需补充获取该提交。校验来源代码中的模板名称、目录和 `package.json` 均存在后再复制。

本次创建的下载缓存放在任务独有目录；Windows 可使用 `C:\Users\Administrator\Documents\Codex\scratch-tests` 下的独立子目录，不放入用户 `TEMP` / `TMP`。用 `try/finally` 清理自己创建的缓存，清理前核对绝对路径位于本次目录内；不跟随链接删除其目标，不删除用户原有仓库或已生成项目。清理失败时如实说明遗留路径。

### 3. 复制内容并完成初始化

- 将选中模板目录**内部的全部项目文件**复制到目标根目录，避免多套一层 `template-*`。保留点文件、环境配置、`.agents`、`AGENTS.md`、工作区配置、锁文件、补丁和 monorepo 子包等项目内容。
- 本地模板可能含开发残留。复制时排除任意层级的 `.git`、`node_modules`、`.pnpm-store`、`.codegraph`、`.spaces`、`dist`、`coverage`、`.vite`、`.swc`、`.vitepress/cache`、生成的 `.vite-hooks/_`、`*.tsbuildinfo`、`*.tgz` 等依赖、索引、缓存或构建产物；不要跟随依赖链接把模板目录外的内容复制进来。
- 递归将 `_gitignore` 转成 `.gitignore`。两者同时存在时先比较并保留有效规则，避免无声覆盖。
- 将根 `package.json` 的 `name` 改为合法项目包名，可由目录名转换为小写英文、数字和连字符。monorepo 内部包名及 `workspace:`、`catalog:` 引用保持一致，不批量改名。
- 读取目标项目的 `AGENTS.md`、`package.json`、`pnpm-workspace.yaml` 及必要配置后再继续。使用该模板已有的包管理、路由、状态管理、样式和目录约定，不复制 BubblesJS 仓库根配置来替代模板配置。
- 下载、检出或复制失败时说明具体原因，不改用脚手架 CLI，也不把不完整目录报告为已完成。

## 按请求验证并交付

- 用户只要求获取模板时，完成复制和必要的包名、忽略文件处理，并核对项目结构；不自行扩展业务页面。
- 用户要求可运行项目或功能开发时，继续安装依赖并完成相应需求。先看项目的 `packageManager` 和锁文件；未声明工具而模板包含 pnpm 锁文件或工作区时使用 pnpm，`template-pnpm-vp-monorepo` 使用 pnpm 工作区。
- 执行模板实际提供的检查脚本，不假设每个模板都有 `dev`、`lint`、`typecheck`、`test` 或 `build`。Vite+ 的 `vp <命令>` 与 `vp run <脚本名>` 不等价，优先按 `package.json` 的脚本入口执行。
- 网页项目根据实际脚本运行开发、检查与构建；小程序按目标平台使用 `dev:weapp`、`build:weapp`、`build:h5` 等实际存在的脚本。构建通过只能说明编译成功，未在开发者工具中运行时不要声称已验证小程序运行效果。
- 最终简要说明所选模板、项目绝对路径、来源版本，以及已执行的验证或尚未执行的部分；存在阻塞或缓存遗留时一并说明。
