# Vue Vapor 与 Pinia

只在当前任务涉及本文包或能力时读取；本文不会要求自动加载其他生态参考。

“官方规则”表示官方文档明确说明；“已核实机制”表示固定 tag 源码具有该实现；“源码风险”表示发现了可能影响 Vapor 的具体依赖，但没有在用户项目中实跑；“建议”表示项目执行与验证方法。不要把源码风险写成生态库整体禁用，也不要把局部支持推定为所有功能兼容。

## Pinia 的使用与组件调试关联

**已核实机制：** Pinia 安装时调用 `app.provide(piniaSymbol, pinia)`；`useStore()` 使用 `hasInjectionContext()`、`inject()` 或已激活的 Pinia 获取 store。核心 store 获取并非完全依赖 `getCurrentInstance()`，不能据此把 Pinia 整体禁用。

在 Vapor setup 中显式调用 `useXxxStore()`。不要依赖通过 `app.config.globalProperties` 提供的 `$pinia`，因为 Vapor 不支持这个模板取值路径。

**源码风险，未项目实跑：** Pinia 的开发模式代码使用 `getCurrentInstance()` 与 `currentInstance.proxy`，将 store 关联到组件供 DevTools 使用。Vapor 组件没有相同 public instance proxy，这条组件关联路径需要单独验证；它与 state、getter、action 是否正常工作是不同检查项。

**建议：** 按项目验证 state 更新、getter、action、插件、持久化和 store HMR；有使用才检查对应能力。

**仅实际 SSR/hydration 路径检查：** 使用 SSR 时，再验证 SSR 状态恢复。SSR 继续按请求创建和传递 Pinia，不能把可用的全局 active Pinia 当成跨请求隔离的保证。SPA/CSR 任务跳过此项。

来源：

- [Pinia：安装与 provide](https://github.com/vuejs/pinia/blob/v4.0.3/packages/pinia/src/createPinia.ts#L22)
- [Pinia：useStore 注入路径与组件调试关联](https://github.com/vuejs/pinia/blob/v4.0.3/packages/pinia/src/store.ts#L883)
- [Pinia：SSR 使用说明](https://github.com/vuejs/pinia/blob/v4.0.3/packages/docs/ssr/index.md)
- [Vue RC.10：globalProperties 与组件 public instance 限制](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449)
