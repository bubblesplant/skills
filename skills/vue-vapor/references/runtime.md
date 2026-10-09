# 公共运行时：混用、异步组件与内置组件

仅在当前任务涉及对应能力时读取相关项，不作为所有应用的默认参考。

本文件适用于 SPA 与 SSR 客户端两种路径。应用入口由已选择的 [SPA / CSR](modes/spa.md) 或 [SSR / hydration](modes/ssr-hydration.md) 分支决定，不需要同时加载两个分支。

| 当前任务 | 读取条目 |
| --- | --- |
| JSX、普通 render/h 或混合组件路径 | JSX 与手写 render/h |
| 异步组件 loader 与 wrapper | 异步组件的 wrapper |
| 顶层 await、async setup 或 Suspense | Suspense 的互操作 |
| Teleport、Transition、TransitionGroup、KeepAlive | 原生内置组件 |

## JSX 和普通手写 render/h 组件仍是 VDOM

**已确认边界。** 标记父组件不会把 JSX 或普通 render/h 组件编译成 Vapor。使用它们需要互操作。**建议：** 页面或区域内保持可辨认的模式边界，减少反复交叉嵌套；这不是禁止混用组件。

来源：[组件模式与互操作](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L430)。

## 异步组件区分 Vapor 与 VDOM wrapper

**已确认客户端行为与建议。** 浏览器端纯 Vapor 或关注体积时，优先使用 `defineVaporAsyncComponent`。普通 `defineAsyncComponent` 固定产生 VDOM wrapper，不会根据 loader 返回结果自动切为 Vapor；它可通过互操作使用。SSR 的标准 runtime 将 `defineVaporAsyncComponent` 导出为普通异步组件别名；涉及服务端时查看 [SSR 的公开 API 与环境差异](modes/ssr-hydration.md#公开-api-从-vue-导入并保留环境差异)，不能把客户端 wrapper 结论用于 Node 服务端。

```ts
import { defineVaporAsyncComponent } from 'vue'

// 浏览器客户端
const AsyncPanel = defineVaporAsyncComponent(() => import('./Panel.vue'))
```

`Panel.vue` 应实际编译为 Vapor。异步 loader 与 async setup 是不同场景，不能因使用此 API 就认为顶层 await 不需要 Suspense。

来源：[Vapor wrapper](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/apiDefineAsyncComponent.ts#L45)、[VDOM wrapper](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-core/src/apiAsyncComponent.ts#L50)。

## Suspense 当前走 VDOM 互操作

**RC.10 限制。** 此版本没有原生 Vapor Suspense，编译器将 `<Suspense>` 映射到 VDOM Suspense。使用时需要互操作，不能继续承诺全无 VDOM runtime。顶层 await 会形成 async setup，需要父级 `<Suspense>`；不要与异步组件 loader 混淆。

若顶层 await 位于应用根组件，增加同步根壳，由根壳的 `<Suspense>` 承载异步子组件；不能在异步根自身的模板里放一个 Suspense 就当成已有父级边界。

来源：[编译器映射](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/utils.ts#L178)、[Vapor Suspense 占位实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/components/Suspense.ts)、[互操作测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/components/Suspense.spec.ts#L90)、[async setup 检查](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/component.ts#L711)。

## 已有原生实现的内置组件不应误禁用

**已确认支持。** Teleport、Transition、TransitionGroup、KeepAlive 已有原生 Vapor 实现。它们与仍走 VDOM 互操作的 Suspense 边界不同；按业务用法验证复杂混用即可，不要沿用早期能力缺失列表。

来源：[内置组件实现](https://github.com/vuejs/core/tree/v3.6.0-rc.10/packages/runtime-vapor/src/components)、[对应测试](https://github.com/vuejs/core/tree/v3.6.0-rc.10/packages/runtime-vapor/__tests__/components)。
