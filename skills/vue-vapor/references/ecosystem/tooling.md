# Vue Vapor 调试与测试工具

只在当前任务涉及本文包或能力时读取；本文不会要求自动加载其他生态参考。

“官方规则”表示官方文档明确说明；“已核实机制”表示固定 tag 源码具有该实现；“源码风险”表示发现了可能影响 Vapor 的具体依赖，但没有在用户项目中实跑；“建议”表示项目执行与验证方法。不要把源码风险写成生态库整体禁用，也不要把局部支持推定为所有功能兼容。

## DevTools 与 HMR 分开核查

**已核实机制：** Vue RC.10 为 Vapor setup 状态暴露 `devtoolsRawSetupState`；DevTools 有读取和编辑该字段的实现。存在支持证据，不应写成“Vapor 无 DevTools”。

**证据范围：** 这些源码没有证明用户项目中的组件树、元素定位、状态编辑、路由面板和 Pinia 组件关联都能完整工作。按使用的 DevTools 版本、扩展或 Vite 插件形式，验证需要的功能；[Pinia 的组件调试关联](pinia.md) 仍需单独检查。

HMR 已实现，官方测试覆盖 template rerender、script reload、根组件 provide/inject，以及 VDOM 与 Vapor 切换等场景；不要沿用“Vapor 没有 HMR”的旧限制。

**建议：** 开发过程中检查编辑模板与 script 后的更新、卸载和副作用清理。遇到 HMR 后的异常，完整刷新并复测，再判断是否属于业务代码、互操作还是 HMR 路径；不能仅依赖 HMR 状态推断生产行为。

来源：

- [Vue RC.10：暴露 setup 调试状态](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/component.ts#L1827)
- [DevTools：读取 devtoolsRawSetupState](https://github.com/vuejs/devtools/blob/v8.2.1/packages/devtools-kit/src/core/component/state/process.ts#L132)
- [DevTools：编辑 devtoolsRawSetupState](https://github.com/vuejs/devtools/blob/v8.2.1/packages/devtools-kit/src/core/component/state/editor.ts#L168)
- [Vue RC.10：HMR 官方测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/hmr.spec.ts)

## Vue Test Utils 的 wrapper 行为需要项目验证

**源码风险，未项目实跑：** `@vue/test-utils` 的 mount 创建普通 VDOM wrapper，`VueWrapper` 使用 `vm.$.subTree`、`vm.$.vnode` 和 `$el`。这些假设与 Vapor 组件不暴露同一 public instance 的规则不同。

在已核查的固定 tag 中，没有找到专门的 Vapor 适配或测试覆盖。因此不要保证 `wrapper.vm`、`setData`、组件查找、stub、shallow mount 等行为都兼容，也不要把 VTU 整体列为不可用。

**建议：** 先用项目现有版本验证实际需要的 mount、props 更新、事件、slot、卸载与清理；普通 VDOM 测试壳若渲染 Vapor 子组件，按应用规则安装 `vaporInteropPlugin`。断言优先采用 DOM、用户交互、显式 expose 与可观察输出，避免只检查内部实例结构。必要时为关键混合边界补浏览器 E2E，不能把手动 mount 成功当成全部 VTU API 兼容的证明。

来源：

- [VTU：创建 VDOM 测试 wrapper](https://github.com/vuejs/test-utils/blob/v2.5.1/src/createInstance.ts#L205)
- [VTU：VueWrapper 的实例结构依赖](https://github.com/vuejs/test-utils/blob/v2.5.1/src/vueWrapper.ts#L133)
- [Vue RC.10：组件 template ref 的 public instance 限制](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449)
