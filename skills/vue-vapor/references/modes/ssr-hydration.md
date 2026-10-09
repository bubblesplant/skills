# SSR / SSG / Hydration 应用

适用：SSR 服务端输出、SSG 预渲染，以及浏览器认领这些 DOM 的 hydration；也包括只修改其中一个阶段的任务。存在浏览器接管时才检查 hydration，不要求仅输出 HTML 的任务增加客户端应用。

## 按当前阶段加载

| 当前修改 | 需要关注 | 不随之展开 |
| --- | --- | --- |
| 服务端输出或预渲染 | 对应服务端编译与渲染链、Vue/server-renderer 版本、输出与数据一致性 | 不将客户端 `createVaporApp` 等入口复制到 Node 服务端 |
| 客户端 hydration | hydration 入口、DOM 认领与实际组件模式 | 不因只改 hydration 入口就重做整个服务端 |
| 两端共享模块或自定义 alias | 公开 API 的导出差异与两端构建 | 不根据客户端构建成功推定服务端可用 |

下面的 `create*SSRApp(...).mount(...)` 仅指浏览器 hydration 入口。纯 Vapor 使用 `createVaporSSRApp`；VDOM/Vapor 混用时配置客户端互操作。选择方式取决于实际组件路径，父组件或入口名称不能自动转换组件模式。

```ts
// 浏览器端：VDOM 壳与 Vapor 组件混用的 hydration 入口
import { createSSRApp, vaporInteropPlugin } from 'vue'
import App from './App.vue'

createSSRApp(App).use(vaporInteropPlugin).mount('#app')
```

只验证本次任务涉及的阶段。涉及 SSR 数据恢复、异步组件或混合边界时，验证相应 hydration 路径；不要仅凭页面最终显示正常判定 DOM 已被认领。Nuxt 项目保留框架管理的入口，并按需读 [Nuxt 适配](../ecosystem/nuxt.md)，不要直接套用手写入口示例改写 Nuxt。

编译配置变化时读 [配置](../configuration.md)；异步组件、顶层 await、async setup、Suspense、JSX 或内置组件变化时读 [公共运行时](../runtime.md) 的对应项；涉及组件 API、ref、attrs、slot、指令或事件时读 [组件](../components.md) 的对应项；库变更时从 [生态索引](../ecosystem.md) 选择对应参考。无需再读 SPA 挂载文档；若另一个区域确实采用独立 CSR，按该区域加载 [SPA 分支](spa.md)。

## SSR 和 hydration 已支持

**已确认支持。** 纯 Vapor 浏览器端 hydration 使用 `createVaporSSRApp`；VDOM 壳内混用 Vapor 可使用 `createSSRApp` 配合 `vaporInteropPlugin`。按当前问题核对相关的既有服务端输出与客户端编译前提，并验证涉及的混合边界；仅修 hydration 入口不要求重做服务端渲染检查。

```ts
// 浏览器端：认领服务端已生成的 DOM
import { createVaporSSRApp } from 'vue'
import App from './App.vue'

createVaporSSRApp(App).mount('#app')
```

这个示例是浏览器 hydration 入口，不代表完整 SSR 服务端配置。不要沿用“Vapor 不支持 SSR/hydration”的早期结论。

来源：[SSR 入口](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/apiCreateApp.ts#L140)、[官方 hydration 测试帮助器](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/hydration/_helpers.ts#L132)、[混合 hydration 测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/hydration/interopBasic.spec.ts#L122)。

## 普通 mount 不能代替 hydration

**已确认行为。** `createVaporApp` 挂载会清空已有容器。页面已有 SSR HTML 时应选择对应 hydration 入口；只验证页面最终显示正常，不能证明服务端 DOM 被正确认领。

来源：[两种 mount 的实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/apiCreateApp.ts)。

## 公开 API 从 vue 导入并保留环境差异

**RC.10 实现边界。** 优先从 `vue` 导入公开 API。标准 SSR runtime 对 `defineVaporAsyncComponent` 采用普通异步组件别名，客户端 Vapor runtime 再提供 Vapor wrapper。不要把所有环境的 Vue 导入统一 alias 到仅供客户端使用的 Vapor runtime。

存在自定义 alias 或构建链时，分别验证客户端与服务端使用的导出；不凭客户端 build 成功判断 SSR 正确。

来源：[标准 runtime 的 SSR 别名](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/vue/src/runtime.ts#L12)、[客户端 Vapor runtime 导出](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/vue/src/runtime-with-vapor.ts)。
