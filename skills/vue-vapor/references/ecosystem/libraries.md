# Vue Vapor 第三方组件与插件

只在当前任务涉及本文包或能力时读取；本文不会要求自动加载其他生态参考。

“官方规则”表示官方文档明确说明；“已核实机制”表示固定 tag 源码具有该实现；“源码风险”表示发现了可能影响 Vapor 的具体依赖，但没有在用户项目中实跑；“建议”表示项目执行与验证方法。不要把源码风险写成生态库整体禁用，也不要把局部支持推定为所有功能兼容。

## 按具体机制审查第三方组件与插件

**官方规则：** `vaporInteropPlugin` 能使 VDOM 与 Vapor 组件双向嵌套，覆盖标准 props、events、slots。官方仍提示 VDOM 组件库存在边缘兼容问题，建议维持清晰的渲染区域边界。不能把所有第三方库整体禁用，也不能只加 interop 就宣布全部功能兼容。

**建议：** 先检查项目实际依赖的组件、指令、插件或 composable 是否使用以下机制，再设计验证或适配：

- 调用 slot 来过滤、克隆或检查 VNode，或把 `slots.default()` 当成无副作用的试渲染。
- 读取 `getCurrentInstance().proxy`、`vnode`、`subTree` 或组件 ref 的 `$el/$refs/$slots`。
- 通过 `app.config.globalProperties` 提供模板中的 `$xxx`。
- 提供 VDOM 的对象指令，或使用与 Vapor 指令不一致的函数参数。
- 使用 JSX/render function：这些组件仍走 VDOM，需要互操作并计入体积。
- 操作 DOM、依赖事件顺序、阻止冒泡，或自行挂载和卸载外部 widget。
- 使用 `<Suspense>`、异步 wrapper、`KeepAlive`、`Transition` 等组合并依赖其 VNode 或组件实例行为。

**行为注意：** Vue RC.10 原生元素事件默认直接监听；显式 `.delegate` 才请求事件委托，且仍须满足编译条件。只有实际进入 document 委托路径的监听，才受祖先 `stopPropagation()` 阻止事件到达 document 的风险影响。不要把旧发布说明中的默认委托描述套用到 RC.10 所有事件。

Vue RC.10 的 `<Suspense>` 映射为 VDOM `Suspense`，通过 interop 使用；原生 `VaporSuspense` 尚未实现。含 `<Suspense>` 的区域应计入 VDOM 依赖，不能将它归为纯 Vapor 原生能力。

来源：

- [Vue RC.10：互操作支持与组件库边缘场景](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L430)
- [Vue RC.10：slot 调用不是安全 dry run](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L476)
- [Vue RC.10：对象指令被跳过，Vapor 指令的实际接口](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/directives/custom.ts#L29)
- [Vue RC.10：.delegate 的编译条件](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/transforms/vOn.ts#L120)
- [Vue RC.10：document 委托监听实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/dom/event.ts#L191)
- [Vue RC.10：Suspense 编译映射](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/utils.ts#L178)
- [Vue RC.10：VaporSuspense 占位实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/components/Suspense.ts)
