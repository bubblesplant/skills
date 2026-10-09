# Vue Vapor 项目验证与性能

只在当前任务涉及本文包或能力时读取；本文不会要求自动加载其他生态参考。

“官方规则”表示官方文档明确说明；“已核实机制”表示固定 tag 源码具有该实现；“源码风险”表示发现了可能影响 Vapor 的具体依赖，但没有在用户项目中实跑；“建议”表示项目执行与验证方法。不要把源码风险写成生态库整体禁用，也不要把局部支持推定为所有功能兼容。

验证范围由当前任务与实际使用的能力决定。SPA/CSR 任务跳过 SSR/hydration 专项；仅实际 SSR、SSG 或 hydration 路径才检查服务端输出、hydration 与状态恢复。不自动加载其他生态文件。

## 按项目使用范围验证并度量性能

**建议：** 完成修改后运行项目要求的类型检查、构建和已有相关测试。补充验证应对应本次改动和实际依赖，重点检查：

- 纯 Vapor 或 VDOM interop 入口与所用组件是否匹配。
- props、events、slot、`v-model`、动态条件与列表更新的用户可观察结果。
- 原生事件与显式 `.delegate` 的实际触发；有第三方阻止冒泡时检查对应边界。
- 路由守卫、缓存恢复、异步组件的 loading/error，以及实际使用的生命周期。
- 组件卸载后 effect、DOM widget、监听和指令 cleanup 是否释放。
- 使用 SSR 时，服务端输出、客户端 hydration、延迟 hydration 与数据一致性。
- 采用 Nuxt、Pinia、组件库、DevTools 或 VTU 时，对应包实际使用的具体 API 与组合。

官方 runtime 与 hydration 测试可用于理解预期行为，不能替代用户项目自己的验证。报告结果时区分“阅读了官方测试”“本地测试已通过”“该项目场景尚未验证”。不需要为无关或未使用的功能补齐完整测试矩阵。

Vapor 的性能收益应实测。使用相同业务数据、浏览器、机器和生产构建，对比修改前后；记录所比较的渲染模式与 interop 依赖。按问题选择测量产物大小及实际压缩体积、加载与首次渲染、频繁更新耗时、内存与卸载后的资源残留。不要将开发模式/HMR 的耗时用于生产性能结论，也不要承诺所有组件都更快或固定百分比的提升。

纯 Vapor 的基础体积优势只适用于构建确实移除 VDOM runtime 的情况。Nuxt 的 VDOM 根、普通组件库、普通异步 wrapper 或 RC.10 的 `<Suspense>` 都可能保留 VDOM；应通过生产产物确认实际依赖，而非仅查看 SFC 标记。

来源：

- [Vue RC.10：Vapor 的目标、成熟度与建议采用范围](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L374)
- [Vue RC.10：纯 Vapor 体积与 interop 的取舍](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L417)
- [Vue RC.10：hydration 测试目录](https://github.com/vuejs/core/tree/v3.6.0-rc.10/packages/runtime-vapor/__tests__/hydration)
- [Vue RC.10：异步 wrapper 的 VDOM 实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-core/src/apiAsyncComponent.ts#L50)
- [Nuxt：interop 与 VDOM 根](https://github.com/nuxt/nuxt/blob/v4.6.0/docs/3.guide/1.concepts/10.vuejs-development.md#L49)
