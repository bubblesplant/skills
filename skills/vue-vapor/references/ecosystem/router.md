# Vue Vapor 与 Vue Router

只在当前任务涉及本文包或能力时读取；本文不会要求自动加载其他生态参考。

“官方规则”表示官方文档明确说明；“已核实机制”表示固定 tag 源码具有该实现；“源码风险”表示发现了可能影响 Vapor 的具体依赖，但没有在用户项目中实跑；“建议”表示项目执行与验证方法。不要把源码风险写成生态库整体禁用，也不要把局部支持推定为所有功能兼容。

## Router 组件与注入式 composable

**官方规则与已核实机制：** `vaporInteropPlugin` 支持在 Vapor 与 VDOM 组件之间传递标准 props、events 和 slots。Vue Router 的 `RouterLink`、`RouterView` 仍由普通 `defineComponent` 创建；在 Vapor 应用中使用它们，需要配置 VDOM interop，不能把它们算作纯 Vapor 组件。

`useRouter()` 与 `useRoute()` 使用 `inject()` 获取 router 和 route。Vapor 不支持 `app.config.globalProperties`，因此优先在 setup 中调用这两个 composable，再使用返回值；不要直接依赖模板里的 `$router`、`$route`。注入式 API 可用，不意味着 Router 的每一个 API 都兼容，组件守卫须按 [组件守卫的源码风险](#router-组件守卫的源码风险) 检查。

**建议：** 路由壳保持 VDOM、内部性能敏感区域使用 Vapor，是可以逐步验证的边界。涉及 `RouterView` slot、动态 `<component>`、`KeepAlive`、`Transition` 的组合，检查路由切换、缓存、卸载和 ref；不要仅凭页面首次渲染成功判定兼容。

来源：

- [Vue RC.10：VDOM interop 与 globalProperties 限制](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L430)
- [Router：useRouter/useRoute 使用 inject](https://github.com/vuejs/router/blob/v5.4.0/packages/router/src/useApi.ts#L1)
- [Router：RouterView 实现](https://github.com/vuejs/router/blob/v5.4.0/packages/router/src/RouterView.ts#L52)
- [Router：RouterLink 实现](https://github.com/vuejs/router/blob/v5.4.0/packages/router/src/RouterLink.ts)

## Router 组件守卫的源码风险

**源码风险，未项目实跑：** Vue 官方说明，Vapor 组件的 `getCurrentInstance()` 返回 `null`。Router 的 `onBeforeRouteLeave()` 与 `onBeforeRouteUpdate()` 仍在开发模式检查 `getCurrentInstance()`；为空时诊断并提前返回，跳过后续 guard 注册。

这个问题属于所链接源码中具体 API 的检查点，不能概括为“Vue Router 不支持 Vapor”。开发模式的检查还有 `__DEV__` 条件，不能因为生产包没有同一条告警，就推定两种环境行为一致。

**建议：** 在 Vapor 路由页实际测试离开守卫、参数变化守卫、卸载、路由取消和 `KeepAlive` 恢复；开发与生产预览各检查一次。必要时将组件守卫放在普通 VDOM 路由边界组件，保留原有业务语义。不要为消除告警调用 Vue 内部实例 API，也不要未验证就改写依赖中的 guard 检查。

来源：

- [Vue RC.10：getCurrentInstance 的 Vapor 行为](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449)
- [Vue RC.10：公开实例查询实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-core/src/componentCurrentInstance.ts#L18)
- [Router：组件守卫的开发模式早返回](https://github.com/vuejs/router/blob/v5.4.0/packages/router/src/navigationGuards.ts#L73)
