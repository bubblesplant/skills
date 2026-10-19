# bubblesplant 的 AI Skills

[English](./README.md) | 简体中文

一组可复用的 AI Agent 技能，涵盖前端开发、项目 AI 规则、操作系统定时提醒和 BlackHole Engine API 查询。

## 技能总览

点击技能名称查看详细说明。表中命令在目标项目根目录运行；追加 `-g` 可全局安装。

| 技能 | 简要介绍 | 项目安装命令 |
| --- | --- | --- |
| [create-bubbles](#create-bubbles) | 创建、定制和验证 BubblesJS 前端项目。 | `pnpx skills add bubblesplant/skills --skill create-bubbles` |
| [bubblesjs-i18n](#bubblesjs-i18n) | 接入 BubblesJS 国际化，维护 JSON 和 Excel 翻译表。 | `pnpx skills add bubblesplant/skills --skill bubblesjs-i18n` |
| [vue-vapor](#vue-vapor) | 开发、迁移和排查 Vue Vapor 组件。 | `pnpx skills add bubblesplant/skills --skill vue-vapor` |
| [setup-project-agents](#setup-project-agents) | 初始化或接入前端与 Node.js 后端项目的 Agent 指令与规则。 | `pnpx skills add bubblesplant/skills --skill setup-project-agents` |
| [manage-prefixed-schedules](#manage-prefixed-schedules) | **测试中，不建议安装。** 管理 AI 自有的操作系统提醒。 | `pnpx skills add bubblesplant/skills --skill manage-prefixed-schedules` |
| [blackhole-engine-api-query](#blackhole-engine-api-query) | 查询 BlackHole3D API、模型资源 URL 和 SDK 升级说明。 | `pnpx skills add bubblesplant/skills --skill blackhole-engine-api-query` |

> [!IMPORTANT]
> 本仓库提供以文档为依据的 AI Agent 技能。用于生产决策时，请通过原始文档或实际运行结果核实关键 API 行为。

## 安装

交互选择需要安装的技能：

```bash
pnpx skills add bubblesplant/skills
```

安装全部技能：

```bash
pnpx skills add bubblesplant/skills --skill='*'
```

全局安装全部技能：

```bash
pnpx skills add bubblesplant/skills --skill='*' -g
```

下方每个技能均提供项目安装和全局安装命令。项目安装命令应在目标项目根目录运行；全局安装使用 `-g`。批量安装全部技能时，也会包含仍在测试中的 `manage-prefixed-schedules`，请留意其说明。

更多 CLI 用法见 [vercel-labs/skills](https://github.com/vercel-labs/skills)。

## 技能详解

当前包含六个技能。每个技能位于 `skills/<skill-name>`，以 `SKILL.md` 为入口，并可附带参考文档、规则模板、Agent 元数据或辅助脚本。下方链接指向各技能的使用说明。

### 前端技能

#### [create-bubbles](./skills/create-bubbles/SKILL.md)

使用 `create-bubbles` CLI 和 BubblesJS 模板创建、定制并验证前端应用。比较 Vue、React、Taro、NextJS、Electron 及 React + NestJS monorepo 模板，在确认模板和目标目录后生成项目，继续完成页面、组件、路由与应用状态，也支持维护 CLI 模板。

适用于创建前端项目、完善已生成应用或修改 `create-bubbles` 模板。修改范围限于目标应用或相关模板目录；覆盖已有非空目录需要用户明确要求。

**安装方式：**

```bash
# 安装到当前项目
pnpx skills add bubblesplant/skills --skill create-bubbles

# 全局安装
pnpx skills add bubblesplant/skills --skill create-bubbles -g
```

#### [bubblesjs-i18n](./skills/bubblesjs-i18n/SKILL.md)

在 Vue 3、React 和 JavaScript/TypeScript 应用中接入、使用或排查 BubblesJS i18n，处理响应式语言切换、插值、异步加载、持久化、局部作用域和 SSR。使用 CLI 扫描静态翻译 key、维护 JSON 语言包、检查 key 是否存在，并同步 Excel 翻译表。

适用于 BubblesJS i18n 及其 runtime、框架适配包和 CLI 相关任务，不用于无关国际化库的常规任务。已有国际化方案时，只处理用户要求的接入或迁移范围；CLI `check` 检查 key 是否存在，不检查翻译完成度。基础 API 使用 `0.0.2` 源码快照，CLI 说明还包含本地源码变更，需核实目标项目实际安装的功能。

**安装方式：**

```bash
# 安装到当前项目
pnpx skills add bubblesplant/skills --skill bubblesjs-i18n

# 全局安装
pnpx skills add bubblesplant/skills --skill bubblesjs-i18n -g
```

#### [vue-vapor](./skills/vue-vapor/SKILL.md)

用于 Vue Vapor 组件的开发、迁移、审查与排查。先确认目标组件的实际编译模式，再按 SPA/CSR 或 SSR/SSG/hydration 场景选择配置、组件、运行时和生态集成参考。文档核查基准为 Vue `3.6.0-rc.10`。

仅在用户要求 Vapor，或当前目标组件、直接依赖及有效配置出现 Vapor 相关线索时触发。没有相关线索的普通 Vue 任务不触发；仓库其他区域使用 Vapor，也不能证明当前组件使用 Vapor。编译模式、类型模式与运行时互操作需分别判断，使用其他 Vue 版本时应按对应官方 tag 核实行为。

**安装方式：**

```bash
# 安装到当前项目
pnpx skills add bubblesplant/skills --skill vue-vapor

# 全局安装
pnpx skills add bubblesplant/skills --skill vue-vapor -g
```

### 工作流技能

#### [setup-project-agents](./skills/setup-project-agents/SKILL.md)

使用内置个人规则模板，为前端和 Node.js 后端项目初始化或接入 Agent 指令与开发规则，写入或补齐 `AGENTS.md` 与 `.agents/rules`。支持单体项目、单应用全栈、普通前后端分目录仓库及 monorepo，按项目、包、目录或代码职责选择资产，逐条语义合并已有约定，适配路径与入口链接，并依据项目配置选择 React 条件规则。Node.js 后端目前使用代码设计、共享代码等通用规则，前端规则仅应用于对应前端职责。

适用于首次初始化、接入已有项目或明确要求补齐缺失规则；本次请求即比较当前适用的个人规则基线并补齐缺失要求。修改范围仅限目标规则文档及必要链接，不修改业务代码、依赖或构建配置；未经明确要求，不迁移或删除已有规则，也不会因模板后续变化自动回写项目。

**安装方式：**

```bash
# 安装到当前项目
pnpx skills add bubblesplant/skills --skill setup-project-agents

# 全局安装
pnpx skills add bubblesplant/skills --skill setup-project-agents -g
```

### 自动化技能

#### [manage-prefixed-schedules](./skills/manage-prefixed-schedules/SKILL.md)

**仍在测试中，不建议安装。** 在 Windows、macOS 和 Linux 上管理操作系统定时提醒，定义调度、真实可见的系统通知和安全边界；具体实现命令根据平台选择。

用户必须在对话中明确提供提醒管理目录。仅管理与该目录关联、且属于 `AI-Reminders` 命名空间或 `AI-Reminder-` 前缀的资源，不管理无关系统任务。该技能面向操作系统级提醒，不以聊天内提醒或宿主应用自动化替代。

**安装方式：**

以下命令仅供测试用途参考：

```bash
# 安装到当前项目
pnpx skills add bubblesplant/skills --skill manage-prefixed-schedules

# 全局安装
pnpx skills add bubblesplant/skills --skill manage-prefixed-schedules -g
```

### 文档技能

#### [blackhole-engine-api-query](./skills/blackhole-engine-api-query/SKILL.md)

查询 BlackHole Engine Plus / BlackHole3D JavaScript 方法、参数、返回值、事件及示例，指导查找模型资源 URL，并结合官方 SDK 升级说明排查兼容性与迁移问题。内置 API 参考为 `SDK_V3.2.0.3808`，发布日期为 `2026-07-20`。

适用于 BlackHole Engine、BlackHole3D 和相关 BIM/GIS 引擎 API 任务。普通查询使用内置默认 API 文档；SDK 错误、升级回归、弃用及行为变化等版本敏感问题需结合升级说明核查。内置版本表示文档快照，不代表当前线上最新 SDK。

**安装方式：**

```bash
# 安装到当前项目
pnpx skills add bubblesplant/skills --skill blackhole-engine-api-query

# 全局安装
pnpx skills add bubblesplant/skills --skill blackhole-engine-api-query -g
```

## 常见问题

### 这是什么？

本仓库存储可复用的技能，供 AI 助手在需要特定领域的操作说明和参考资料时加载。

### 哪些 AI 工具可以使用这些技能？

任何支持 Agent Skills 目录格式的助手或 Agent 运行环境都可以使用。这些技能不绑定特定 AI 产品。

### 如何使用与版本相关的说明？

请核对目标项目实际安装的包和配置，并与所选技能的参考资料比较。

- `vue-vapor` 基于 Vue `3.6.0-rc.10`。没有 Vapor 相关线索的普通 Vue 任务不触发该技能。
- `bubblesjs-i18n` 的基础 API 使用 `0.0.2` 源码快照，CLI 说明还纳入了本地源码变更。请核实已安装包的导出和 `bubbles-i18n --help`，尤其是在使用 Excel 命令前。
- 上方 BlackHole SDK 版本标识内置 API 快照，并不确认线上最新 SDK 发布版本。

### API 参考与升级说明如何维护？

需要参考资料的技能在自身目录内维护它们，仓库根目录不集中维护这些资料。

例如，`blackhole-engine-api-query` 在 [references/manifest.json](./skills/blackhole-engine-api-query/references/manifest.json) 中保存内置 SDK 元数据和兼容性策略。该技能保留一份 API Markdown 参考文档，以及从官方更新说明 API 生成的 [upgrade-notes.md](./skills/blackhole-engine-api-query/references/upgrade-notes.md) 缓存。

该技能的维护策略将 BlackHole Engine API 视为向后兼容，因此普通 API 查询使用内置默认参考，包括用户指定旧 SDK 的情况。SDK 错误、升级回归、弃用 API、参数变化、返回值、事件、初始化行为和发布说明等版本敏感问题，应结合 `upgrade-notes.md` 核查。

涉及近期 SDK 更新或升级问题时，在网络可用的情况下，从仓库根目录刷新说明：

```bash
node skills/blackhole-engine-api-query/scripts/refresh_upgrade_notes.mjs
```

刷新失败时使用缓存说明。该脚本只更新升级说明缓存；替换内置 API 手册和更新其 manifest 是独立的维护步骤。

## 许可证

[MIT](./LICENSE)
