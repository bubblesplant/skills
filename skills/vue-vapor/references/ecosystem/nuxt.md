# Vue Vapor 与 Nuxt

只在当前任务涉及本文包或能力时读取；本文不会要求自动加载其他生态参考。

“官方规则”表示官方文档明确说明；“已核实机制”表示固定 tag 源码具有该实现；“源码风险”表示发现了可能影响 Vapor 的具体依赖，但没有在用户项目中实跑；“建议”表示项目执行与验证方法。不要把源码风险写成生态库整体禁用，也不要把局部支持推定为所有功能兼容。

先检查实际 `nuxt.config.*`、配置扩展、模块覆盖与 `routeRules`，按当前目标路径的实际渲染方式判定：

- `ssr: false` 且目标路径仅做客户端渲染：按需读取 [SPA/CSR 模式](../modes/spa.md)。
- SSR、SSG、预渲染后的 hydration，或混合路由中具有这些行为的目标路径：按需读取 [SSR/hydration 模式](../modes/ssr-hydration.md)。

只读取当前路径对应的模式；不要因为项目使用 Nuxt 就自动加载 SSR 专项。两种模式的 Nuxt 应用根都保持 VDOM。

## Nuxt 的 vue.vapor 开关含义

**官方规则，Nuxt：** 在 `nuxt.config.ts` 配置：

```ts
export default defineNuxtConfig({
  vue: {
    vapor: true,
  },
})
```

该配置启用 Nuxt 的 Vapor interop 支持、安装 `vaporInteropPlugin`。它不等同于 Vite Vue 插件的全局 Vapor 编译选项，也不会将所有 SFC 自动编译为 Vapor。仍需在选中的组件或页面使用 `<script setup vapor>`、`<template vapor>` 等有效标记。

Nuxt 应用根保持 VDOM；Nuxt 官方明确不支持全 Vapor 应用。不要把启用 `vue.vapor` 描述为切换到 `createVaporApp`，也不要承诺能移除整个 VDOM runtime。

Nuxt 的支持仍标为实验性，要求包含 Vapor 和互操作修复的 Vue 3.6 版本。固定文档示例使用 `^3.6.0-rc.2`；本 skill 的 Vue 核查基准是 `3.6.0-rc.10`。旧 Vue 不满足要求时 Nuxt 会告警并关闭此选项，应核查 lockfile 中实际解析的 Vue 版本。

**已核实机制：** Nuxt 的互操作插件只在客户端安装。

来源：

- [Nuxt 官方文档：Vapor 开启方式与 interop 含义](https://github.com/nuxt/nuxt/blob/v4.6.0/docs/3.guide/1.concepts/10.vuejs-development.md#L41)
- [Nuxt：vue.vapor 配置定义](https://github.com/nuxt/nuxt/blob/v4.6.0/packages/schema/src/config/app.ts#L32)
- [Nuxt：客户端互操作插件](https://github.com/nuxt/nuxt/blob/v4.6.0/packages/nuxt/src/app/plugins/vapor-interop.client.ts#L1)

## Nuxt 的专有限制

**官方规则：** 以下为所链接的官方文档明确列出的限制；不要推广为所有 Nuxt composable 或内置组件不可用。

- Vapor 组件 ref 不暴露 `$el`；需要显式暴露能力或获取原生元素 ref。
- `<ClientOnly>` 无法对 Vapor slot 子内容做相同的 attribute fallthrough；需要的 attrs 应显式传给目标内容。
- 读取 slot 文本 VNode 的 `<Title>`、`<Style>`、`<Noscript>` 等场景，不能按普通 VDOM slot 方式检查 Vapor 子内容。按对应 API 直接传入值，例如给 `<Title>` 传入字符串，并验证实际输出。
- Vapor 不支持 Options API，因此 `defineNuxtComponent` 上依赖 Options API 的 `asyncData`、`fetchKey` 不适用；使用 `<script setup>` 与 `useAsyncData()`。
- Vapor `<script setup>` 在 `await` 之后调用 Nuxt composable 可能丢失 Nuxt context。尽量在第一次 `await` 前获取需要的 composable 结果；涉及异步上下文时验证实际执行路径，不推定 Vue 的 await 转换能覆盖所有 Nuxt context。

Nuxt 官方同时说明，多数通过 injection 工作的 composable 和内置组件保持可用。上述项目应按具体使用路径审查。

### 仅实际 SSR/SSG/hydration 路径检查

仅当目标路径执行对应服务端或 hydration 能力时检查以下项目；SPA/CSR 任务跳过此节。

**已核实机制：** Vapor SFC 在服务端编译为普通 SSR render function，Node 条件下的 Vue 不提供相同 Vapor runtime 导出；不要在服务端无条件调用客户端专用 Vapor runtime API。该机制见上方 Nuxt 官方文档与配置定义。

- `<NuxtIsland>`、服务端组件不能按普通 VDOM slot 方式检查 Vapor 子内容。按对应 API 直接传入值，并验证实际输出。
- 带 key 的 `onPrehydrate` 在缺少 VDOM 实例时回退为不带 key 的形式，并在开发模式提示；回调作用域扩大，应检查回调对整个 document 是否仍正确。

**已核实机制：** `<NuxtClientFallback>` 的服务端实现也专门检查 Vapor slot，并指出无法按 VNode 方式进行 server-render/fallback-on-error；使用它时应验证该边界，不把它与一般 SSR 支持混为一谈。Vue RC.10 已支持 Vapor SSR 和 hydration。

来源：

- [Nuxt 官方文档：Known limitations](https://github.com/nuxt/nuxt/blob/v4.6.0/docs/3.guide/1.concepts/10.vuejs-development.md#L93)
- [Nuxt：ClientOnly 的 Vapor slot 分支](https://github.com/nuxt/nuxt/blob/v4.6.0/packages/nuxt/src/app/components/client-only.ts#L66)
- [Nuxt：NuxtClientFallback 服务端分支](https://github.com/nuxt/nuxt/blob/v4.6.0/packages/nuxt/src/app/components/client-fallback.server.ts#L70)
- [Nuxt：组件与 slot 诊断](https://github.com/nuxt/nuxt/blob/v4.6.0/packages/nuxt/src/app/diagnostics/render.ts#L107)
- [Vue RC.10：createVaporSSRApp](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/apiCreateApp.ts#L140)
