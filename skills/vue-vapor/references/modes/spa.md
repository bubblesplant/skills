# SPA / CSR 客户端应用

适用：浏览器创建当前页面的 Vue DOM，不认领服务端或预渲染生成的 Vue DOM。这是客户端挂载分支。

先按目标应用或挂载区域判断纯 Vapor 还是与 VDOM 混用，选择下列入口。全局编译开关不会自动替换入口，也不会安装互操作插件。

| 组件路径 | 客户端入口 |
| --- | --- |
| 全部实际为 Vapor | `createVaporApp(App)` |
| 普通 Vue 壳使用 Vapor | `createApp(App).use(vaporInteropPlugin)` |
| Vapor 壳使用 VDOM | `createVaporApp(App).use(vaporInteropPlugin)` |

按当前任务继续加载：改编译或类型配置时读 [配置](../configuration.md)；涉及 JSX、异步组件、顶层 await、async setup、Suspense 或内置组件时读 [公共运行时](../runtime.md) 的对应项；涉及组件 API、ref、attrs、slot、指令或事件时读 [组件](../components.md) 的对应项，仅增加 Vapor 标记无需自动加载组件参考；接入库时从 [生态索引](../ecosystem.md) 选择实际使用的库。不要因为 SPA 应用有客户端路由就加载 SSR 文档。

如果目标容器包含需要认领的 SSR/SSG HTML，切换到 [SSR / hydration 分支](ssr-hydration.md)；当前代码使用普通 mount 不足以证明它应当采用 CSR。

## 纯 Vapor 应用使用 createVaporApp

**已确认支持。** 根组件及运行路径均为 Vapor 时，使用 `createVaporApp(App)`，可以避免引入 VDOM runtime。先确认依赖的组件实际模式；不能只看根组件有 Vapor 标记就宣称应用完全纯 Vapor。

```ts
import { createVaporApp } from 'vue'
import App from './App.vue'

createVaporApp(App).mount('#app')
```

来源：[官方纯 Vapor 接入说明](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L417)。

## 普通 Vue 应用使用 Vapor 需要互操作插件

**已确认规则。** VDOM 应用中使用 Vapor 组件，安装 `vaporInteropPlugin`。SFC 编译开关与运行时互操作是独立检查点。

```ts
import { createApp, vaporInteropPlugin } from 'vue'
import App from './App.vue'

createApp(App).use(vaporInteropPlugin).mount('#app')
```

来源：[官方互操作说明](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L430)。

## Vapor 应用使用 VDOM 组件同样需要互操作

**已确认规则。** `createVaporApp(App).use(vaporInteropPlugin)` 支持使用 VDOM 组件，但会引入 VDOM runtime。报告体积收益时必须按实际依赖计算，不能仍以完全无 VDOM 的应用作比较。

来源：[双向互操作说明](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L430)。
