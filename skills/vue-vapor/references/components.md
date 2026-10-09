# Vue Vapor：组件、模板、指令和事件

以下结论以链接中的官方源码和测试为依据。Vapor 仍处于预发布阶段；升级时重新核查这些限制。旧 RC 文档中的指令参数签名、自动事件委托和 `compilerOptions.eventDelegation` 说明不能直接沿用。

## Options API

Vapor 组件不支持 Options API。使用 `<script setup>` 或 setup 函数和 Composition API；迁移时重写 `data`、`methods`、Options 生命周期等逻辑。不要把这条限制扩展到 `defineOptions({ name, inheritAttrs })` 等受支持的组件元数据。

来源：[官方限制清单](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449-L458)、[SFC 宏编译](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-sfc/src/compileScript.ts)。

## app.config.globalProperties

Vapor 组件不支持通过 `app.config.globalProperties` 注入并读取 `$xxx`。检查依赖此机制的插件和项目工具，将业务依赖改为显式导入或 `provide` / `inject`，再核对插件的 Vapor 兼容性。

来源：[官方限制清单](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449-L458)。

## getCurrentInstance() 返回 null

普通 Vue 的 `getCurrentInstance()` 在 Vapor 组件中返回 `null`。不要依赖 `instance.proxy`、内部实例字段或通过实例读取 app 配置；优先使用公开的组合式 API、传参和依赖注入。迁移第三方 composable 时搜索这一调用。

来源：[官方限制清单](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449-L458)。

## 组件 ref 的公开接口

Vapor 组件 ref 不提供 VDOM 公共实例上的 `$el`、`$props`、`$attrs`、`$slots`、`$refs`。父组件需要调用子组件方法时，用 `defineExpose()` 定义明确接口；需要 DOM 时使用元素 ref。当前实现可能在未 expose 时返回内部实例，不能把这些内部字段当成稳定接口。

来源：[官方限制清单](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449-L458)、[expose 实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/component.ts#L1649-L1673)、[组件 ref 取值](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/apiTemplateRef.ts#L465-L479)。

## 常用 API、宏、CSS 已支持

继续使用正常的 Composition API 和 SFC 写法：`ref`、`computed`、watch、生命周期，以及 `defineProps`、`defineEmits`、`defineModel`、`defineOptions`、`defineSlots`、`defineExpose` 等宏。`scoped`、`:slotted()`、CSS Modules 和 CSS `v-bind()` 有对应实现和测试。不要因 Vapor 模式而手写这些已有能力；特殊 API 和内置组件仍需逐项核查。

来源：[SFC 宏编译](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-sfc/src/compileScript.ts)、[scoped 与 slotted 测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/scopeId.spec.ts)、[CSS 变量测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/helpers/useCssVars.spec.ts)、[CSS Modules 测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/helpers/useCssModule.spec.ts)。

## attrs 的跟踪行为

Vapor 的 `useAttrs()` 返回值会跟踪 effect 中的属性读取、`in` 和 key 枚举；新增、修改、删除 attrs 能触发相关订阅，但 `isReactive(attrs)` 仍为 `false`。在 effect 中读取 `attrs.xxx`，避免 setup 阶段解构或复制成静态快照。不要直接套用 VDOM attrs 的响应性结论，也不要假定两种模式行为完全一致。

来源：[useAttrs 模式分流](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-core/src/apiSetupHelpers.ts#L420-L434)、[attrs 代理](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/componentProps.ts#L265-L294)、[跟踪与 isReactive 测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/componentAttrs.spec.ts#L3297-L3377)。

## slot 调用有副作用

不要用 `slots.default?.()` 判断插槽是否存在或是否为空。调用 Vapor slot 会实际创建 Block、DOM 和 effect，在 hydration 中还可能认领服务端 DOM。仅判断是否提供插槽时检查 `slots.default`；渲染和 fallback 尽量交给模板 `<slot>`。

来源：[官方 slot 行为说明](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L476-L502)、[slot 实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/componentSlots.ts)。

## 不假定 slot 返回 VNode 数组

Vapor slot 返回 Block，不能套用 VDOM 中遍历 `VNode[]`、检查 `.type` / `.children`、克隆或改写 VNode 的技巧。遇到这类组件库封装时先检查其渲染模式兼容性；业务组件优先通过 slot props、显式 props 和 `<slot>` 表达需求。

来源：[官方 slot 行为说明](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L476-L502)、[VaporSlot 类型和实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/componentSlots.ts)。

## v-memo

当前 Vapor 不支持 `v-memo`。这一版本的编译器会忽略它，不能依靠它减少更新，也不能依靠编译错误发现误用。迁移时移除这项优化假设，按实际响应式依赖和更新行为评估性能。

来源：[官方限制清单](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449-L458)、[已注册的模板转换](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/compile.ts#L83-L112)、[内置指令处理](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/transforms/transformElement.ts#L1537-L1569)。

## @vue:xxx 生命周期事件

Vapor 不支持 `@vue:mounted`、`@vue:updated` 等 VNode 生命周期事件。组件生命周期使用 Composition API；元素的创建、更新、销毁需求用模板 ref 或 Vapor 自定义指令实现，按元素作用域管理清理。

来源：[官方限制清单](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L449-L458)。

## v-once 的语义差异

`v-once` 受支持，但部分行为刻意与 VDOM 不同：`v-for` 内按每一行的创建冻结；`v-else` 和 slot template 上也会冻结；透传到 `v-once` 单根的 attrs 会被冻结；`v-once @click="data.fn"` 仍读取最新函数。`<Comp v-once>` 也不意味着插槽内容全部冻结。迁移复杂组合时检查数据变更、新增列表项、切换分支和触发事件后的结果。

来源：[插槽保持更新的测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/vOnce.spec.ts#L125-L179)、[刻意保留的 VDOM 差异测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/vOnce.spec.ts#L180-L271)。

## 使用 Vapor 专用类型

需要显式标注时使用 `VaporDirective`、`VaporSlot`、`VaporComponent`、`DefineVaporComponent` 等对应类型。组件 ref 优先由实际组件推导，或使用 `defineExpose()` 的业务接口。不要用 `VNode[]` / `ComponentPublicInstance` 硬套 Vapor，再通过类型断言绕过差异；`VaporComponentInstance` 含内部字段，不适合作为业务公开接口。

来源：[Vapor 类型导出](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/index.ts)、[Vapor 组件类型定义](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/apiDefineComponent.ts#L27-L101)。

## 自定义指令 getter 签名

Vapor 指令是函数，签名为 `(el, valueGetter?, argGetter?, modifiers?) => cleanup | void`。**value 和 arg 都是 getter**，必须调用 `value?.()` / `arg?.()` 取值；不接收 VDOM 的 binding 或 VNode 参数。动态参数也通过 getter 获取，不能沿用早期 RC 的字符串 arg 签名。

来源：[当前 VaporDirective 签名](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/directives/custom.ts#L34-L58)。

## 旧式指令不兼容

VDOM 的 `{ mounted, updated, unmounted }` 对象指令在 Vapor 模板中会被跳过，开发模式会警告。VDOM 函数指令的参数约定也不同，不能直接复用。迁移全局指令和 UI 库指令时，提供对应的 Vapor 实现并检查调用方模式。

来源：[对象指令检测与跳过](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/directives/custom.ts#L203-L229)、[对象指令测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/directives/customDirective.spec.ts#L119-L155)。

## effect 与 cleanup

指令函数不会像 VDOM `updated` 钩子那样按更新重复调用。需要跟随 value / arg 变化时，在指令内部使用 `watchEffect` 或 `watchPostEffect`；这些 effect 随指令作用域释放。额外创建的监听、observer、定时器等资源，通过返回的 cleanup 函数清理。不要在指令内部注册组件生命周期钩子，它们会挂到所属组件而非目标元素。

```ts
import { watchEffect, type VaporDirective } from 'vue'

const vTitle: VaporDirective<HTMLElement, string> = (el, value) => {
  watchEffect(() => {
    el.title = value?.() ?? ''
  })
}
```

来源：[指令调用和 cleanup 注册](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/directives/custom.ts#L196-L281)、[effect 与清理测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/directives/customDirective.spec.ts#L24-L59)。

## 指令访问 DOM 的时机

指令函数执行时，元素不一定已经插入文档。测量尺寸、聚焦或调用要求元素已挂载的 DOM 库时，用 `watchPostEffect()` 安排操作；不要在指令中用 `onMounted()` 替代。涉及条件分支或动态根时，也检查旧元素的资源是否已经清理。

来源：[官方运行时警告与建议](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/directives/custom.ts#L235-L281)、[挂载时机测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/directives/customDirective.spec.ts#L24-L59)。

## 指令需要单元素根

把自定义指令写在组件上时，组件必须能解析到单个根元素。多根组件或以 `<slot>` 为根的组件不能提供有效目标，开发模式会警告。需要作用于具体元素时，将指令放到该元素上；动态根切换时，运行时会清理旧根并在新根上重新应用指令。

来源：[根元素解析和重应用](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/directives/custom.ts#L88-L181)、[组件根测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/__tests__/directives/customDirective.spec.ts#L103-L180)。

## 默认直接监听 DOM 事件

从 RC4 起，普通 `@click` 等默认直接绑定到元素。只有显式写 `@click.delegate` 才请求事件委托。不要依据早期文章假定所有可冒泡事件都会自动委托；性能分析和事件时序判断应按实际模板写法进行。

来源：[RC4 行为变更](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L334-L343)、[编译器选择逻辑](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/transforms/vOn.ts#L120-L149)、[默认直接监听测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/__tests__/transforms/vOn.spec.ts#L766-L796)。

## .delegate 的范围

`.delegate` 只适用于原生 DOM 上事件名静态且属于编译器白名单的事件。组件事件不支持；动态事件名和 `scroll` 等非白名单事件会警告并回退直接监听。确有大量同类监听的优化需求时，再检查目标事件是否适用。

来源：[事件白名单](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/transforms/vOn.ts#L20-L25)、[动态事件与非白名单回退测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/__tests__/transforms/vOn.spec.ts#L798-L845)、[组件事件限制测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/__tests__/transforms/vOn.spec.ts#L960-L977)。

## .delegate 与修饰符

同时使用 `.capture`、`.passive` 或 `.once` 时，`.delegate` 会回退为直接监听。同一元素同一事件存在 `.stop` 监听时，也会阻止该事件使用委托。不要只看到 `.delegate` 字样就认定委托生效；组合修饰符后检查编译结果和事件行为。

来源：[委托条件](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/src/transforms/vOn.ts#L143-L149)、[选项修饰符回退测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/__tests__/transforms/vOn.spec.ts#L832-L845)、[同元素 stop 测试](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-vapor/__tests__/transforms/vOn.spec.ts#L898-L929)。

## 冒泡及 currentTarget

委托监听器绑定在 `document`。祖先的原生监听若提前 `stopPropagation()`，子元素的委托回调可能收不到事件；混用直接监听和委托时核对传播顺序。委托回调支持 `event.currentTarget`，运行时将其指向当前匹配元素；异步处理前先保存元素引用，避免 `await` 后再读已经变化的 `currentTarget`。

来源：[委托监听器和 currentTarget 实现](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/runtime-vapor/src/dom/event.ts#L191-L239)。

## 移除 compilerOptions.eventDelegation

当前版本已移除 `compilerOptions.eventDelegation`。不要再通过该配置启用或关闭委托，也不要把旧配置复制到 Vite 插件的 `template.compilerOptions` 中。普通事件默认直接监听，需要委托时逐事件使用 `.delegate`。

来源：[RC4 配置移除说明](https://github.com/vuejs/core/blob/v3.6.0-rc.10/CHANGELOG.md#L334-L343)。
