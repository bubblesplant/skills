---
name: vue-vapor
description: 用于 Vue 项目中可能涉及 Vapor 的开发、迁移、审查和排查。仅当用户要求使用 Vapor，或本次任务的目标组件、直接依赖及有效配置出现 vapor 标记、features.vapor、Vapor 入口、互操作或类型模式等相关线索时加载，先确认实际组件模式。没有相关线索的普通 Vue 任务不触发。
---

# Vue Vapor 开发

适用 Vue [`3.6.0-rc.10`](https://github.com/vuejs/core/tree/v3.6.0-rc.10)。

## 确认当前任务是否涉及 Vapor


首先检查 Vue 插件是否有 `vue({ features: { vapor: true } })`，字段为复数 **features**。全局开启覆盖 script setup 与纯模板 SFC；没有显式 Vapor 标记、仅含普通 `<script>` 且无 setup 的 `.vue` 仍是 VDOM；需要逐文件启用 Vapor 时使用 `<script setup vapor lang="ts">`；已有 `<script vapor>`、`<template vapor>` 也属于有效标记。不能用 `vapor="false"` 关闭。

组件编译、类型检查和运行时互操作分别判断；父组件标记不会自动转换子组件、JSX 或第三方组件。根据所选模式参考决定入口与互操作，保持用户既有架构与任务范围。

Nuxt 的 `vue.vapor` 与 `vaporInteropPlugin` 只说明互操作接入，`vueCompilerOptions.vapor` 是语言工具模式；这些配置与 Vapor 入口名称都是排查线索，不能单独证明目标 SFC 已编译为 Vapor。按当前目标及其直接相关的编译输入和组件边界判断，仓库其他区域使用 Vapor 不代表本次任务需要套用这些规则。

确认目标及修改路径仅为普通 VDOM，并且本次无需 Vapor 接入、迁移、互操作修复或配置排查时，结束本技能，不读取后续参考。仅涉及编译模式或类型配置冲突时，只读取 [配置与编译](references/configuration.md) 的相关部分；确认涉及 Vapor 开发后，再选择应用模式与专题。

## 判断目标应用模式

以本次任务涉及的应用、路由或挂载区域为单位，结合用户说明与实际入口、服务端渲染配置判断。只读取所选模式的参考，不把全部文件一次加载。

| 目标行为 | 选择参考 |
| --- | --- |
| 浏览器创建 Vue DOM，当前区域无需认领服务端输出 | [SPA / CSR](references/modes/spa.md) |
| SSR 服务端输出或 SSG 预渲染；浏览器需要认领这些 DOM 时进入 hydration 阶段 | [SSR / SSG / Hydration](references/modes/ssr-hydration.md)，只看当前阶段 |

客户端有路由不能证明它是纯 CSR，现有 mount API 也可能用错。同一仓库可同时存在两种区域。Nuxt 根据有效 `ssr`、目标路由的 routeRules 和预渲染/客户端入口判断；涉及 Nuxt 接入或专有能力时再读 [Nuxt 适配](references/ecosystem/nuxt.md)。

模式未知时先查看足够定位当前入口的项目文件，不为判定模式全量读取参考。若仍无法判断且会影响当前修改，再向用户澄清。

## 按当前修改加载专题

| 实际需要 | 加载参考 |
| --- | --- |
| 编译开关、SFC 标记、工具链或类型检查 | [配置与编译](references/configuration.md) |
| JSX、异步 loader、顶层 await、async setup、Suspense 或内置组件 | [公共运行时](references/runtime.md) 的相关项 |
| 组件 API、ref、attrs、slot、指令或事件 | [组件开发](references/components.md) 的相关项 |
| 接入某个库、调试、测试或性能验证 | 从 [生态索引](references/ecosystem.md) 只选实际相关的参考 |

先定位相关标题，只读取当前任务需要的条目。不默认读取整份配置、组件或生态说明，不因 SPA 任务展开 SSR 专项，也不因 SSR 任务展开无关生态库。Vapor 使用 Composition API；传统实例、VNode 插槽检查、指令签名与事件委托的差异，在对应专题中核查。

验证当前修改的编译、类型及可观察结果；SSR 项目只补相关阶段的检查。源码风险不等于项目已复现，性能和体积通过实际构建与场景度量。
