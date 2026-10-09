# Vapor 的启用、版本与编译边界

本文以链接中的官方源码和发布记录为依据。项目 Vue 与适用版本不同时，按对应官方 tag 核查当前任务涉及的行为，不把开发分支的新行为当作 rc.10 已发布事实。

## 首先检查 Vue 插件的全局开关

**已核实行为：** `@vitejs/plugin-vue` 的字段是复数 **`features.vapor`**，默认值为 `false`，不是 `feature.vapor`。

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue({ features: { vapor: true } })],
})
```

**建议：** 阅读实际生效的 Vite 配置及其共享配置、条件分支和 Vue 插件实例；不要只搜索到某个 `vapor: true` 就认定当前应用已启用。该开关控制 SFC 编译，不会自动选择应用入口 API 或安装运行时互操作插件。

来源：[plugin-vue 配置类型](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/index.ts)、[模式判定源码](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/utils/vapor.ts)。

## 全局开启的适用范围

**已核实行为：** plugin-vue 的全局开关会强制以下输入进入 Vapor 模式：

- 包含 `<script setup>` 的 SFC。
- 没有脚本的纯模板 SFC。
- 被其他插件转换为 SFC、且 descriptor 文件名不以 `.vue` 结尾的输入。

没有显式 Vapor 标记、仅含普通 `<script>` 且没有 setup 的 `.vue` 不会被全局开关强制转换，仍走 VDOM。这个判定以实际传给插件的 descriptor 为准；只有“全局开关存在”不足以证明每个组件已转换。

**建议：** 新建 Vapor 组件使用 setup 语法；对宏插件或非 `.vue` 输入，检查转换后的代码。不要把全局模式表述为“所有组件，包括依赖中的预编译组件，都会成为 Vapor”。

来源：[plugin-vue `isVaporMode` / `canForceVaporMode`](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/utils/vapor.ts)。

## 未全局开启时使用 script setup vapor

**已核实行为：** 未开启全局模式时，给目标组件添加 `vapor` 属性即可逐文件启用；未标记的组件保留默认 VDOM 模式。

```vue
<script setup vapor lang="ts">
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>
```

**建议：** 对逐步接入或混合项目，优先采用这种显式标记，便于确认组件边界。仅写 `<script setup>` 不代表已启用 Vapor；需要同时满足插件全局开关或文件显式标记之一。

来源：[Vue 3.6.0-rc.1 官方接入说明](https://github.com/vuejs/core/releases/tag/v3.6.0-rc.1#about-vapor-mode)、[Vue rc.10 SFC 解析源码](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-sfc/src/parse.ts)。

## 其他有效标记：script vapor 与 template vapor

**已核实行为：** Vue rc.10 的解析器也识别以下写法：

```vue
<!-- vapor 属性同时使脚本被识别为 setup 脚本 -->
<script vapor lang="ts">
import { ref } from 'vue'
const count = ref(0)
</script>

<template>{{ count }}</template>
```

```vue
<!-- 纯模板组件可以直接标记，不需要补空脚本 -->
<template vapor>
  <div>静态内容</div>
</template>
```

**建议：** 带脚本的新组件统一使用清晰的 `<script setup vapor>`；不要把 `<script vapor>` 误判为 Options API，也不要因为纯模板组件没有脚本就判定其不支持 Vapor。`<template vapor>` 不会让普通 Options API 脚本获得兼容能力。

来源：[Vue rc.10 模板与脚本属性判定](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-sfc/src/parse.ts#L178)。

## 不能用 vapor=false 关闭，也没有通用的逐文件 opt-out

**已核实行为：** 以下两种属性值都是非空字符串，rc.10 仍将它们视为开启标记：

```vue
<script setup vapor="false">/* 仍会开启 Vapor */</script>
<template vapor="false"><div /></template>
```

plugin-vue 的 `features.vapor` 类型只有 `boolean`，没有通用的文件过滤器或逐文件禁用属性。`features.vapor: false` 只关闭全局强制转换，不会取消文件上已有的显式 `vapor` 标记。不要发明 `<script setup vdom>`、`no-vapor` 等未经该版本官方支持的写法。

**建议：** 未全局开启时，移除文件的所有有效 `vapor` 标记即可恢复默认模式。已全局开启且需要保留部分 setup 组件为 VDOM 时，先明确项目的模式边界；通常可改用逐文件启用，或设计并验证实际的构建分流。简单将组件排除出唯一的 Vue 插件可能导致它根本无法编译，不是可靠的 VDOM opt-out。

来源：[Vue rc.10 `createBlock` 属性值解析](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/compiler-sfc/src/parse.ts#L321)、[plugin-vue 判定优先级](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/utils/vapor.ts)。

## 实际 Vue 版本与全局开关支持

**Vue 版本检查：** Vapor 属于 Vue 3.6 的新增能力，本文适用 `3.6.0-rc.10`。不能因为项目安装“Vue 3”或使用 `<script setup>` 就认定支持 Vapor。

分别确认项目 Vue 插件对全局开关与逐文件标记的支持，不能把某个开关可用等同于整个工具链兼容。

**建议：** 根据 package manager 的依赖树和 lockfile 检查实际解析版本，不能只依据 `package.json` 的宽泛版本范围。沿用项目的包管理器，不为查询版本改写 lockfile。使用 rc.10 以外版本时，按对应官方 tag 检查变更。

来源：[Vue rc.10 发布记录](https://github.com/vuejs/core/releases/tag/v3.6.0-rc.10)、[plugin-vue 变更记录](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/CHANGELOG.md)、[Vue 3.5.43 发布记录](https://github.com/vuejs/core/releases/tag/v3.5.43)。

## 对齐 Vue、编译器、服务端渲染器与依赖解析

**已核实行为：** plugin-vue 默认优先从项目根目录解析 `vue/compiler-sfc`，然后回退到插件可解析的依赖。插件的 `compiler` 选项可以替换默认编译器。

**建议：** 核查以下实际依赖，保持属于同一套 Vue core 发布版本：`vue`、显式安装的 `@vue/compiler-sfc`、使用 SSR 时的 `@vue/server-renderer`，以及直接依赖的 `@vue/runtime-core`、`@vue/runtime-dom`、`@vue/reactivity`、`@vue/compiler-dom` 等 core 包。DevTools 等独立发布的 `@vue/*` 包按自己的版本线判断，不要求与 Vue core 同号。检查 lockfile、workspace、alias、overrides/resolutions、自定义 `compiler` 和重复 runtime，避免编译器与运行时分属不同版本或重复实例。

不要为了升级 Vapor 盲目添加独立编译器包；先确认插件已经解析的 `vue/compiler-sfc`。若项目使用自定义编译器，验证它具有目标版本的 Vapor 编译能力，而不仅是类型允许传入。

来源：[plugin-vue 编译器解析](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/compiler.ts#L17)、[Vue rc.10 包导出与依赖](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/vue/package.json)。

## Node 与 Vite 的要求

**环境兼容检查：** 根据项目实际安装的 Vue 插件 `package.json` 核对 Node engines 和 Vite peerDependencies，并结合所选 Vite、其他插件及 CI 的要求确认共同支持范围；peer 声明不等于每个插件组合都已验证。

来源：[plugin-vue package.json](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/package.json)。

## 全局模式的 tsconfig 类型检查配置

**语言工具检查：** 配置前确认项目的 Vue 语言工具支持全局 `vueCompilerOptions.vapor`。依赖全局编译时，应同步检查语言工具的有效配置：

**混合项目先检查 [编辑器模式与编译模式的差异](#混合项目的编辑器模式与编译模式差异)。** 下例会把语言工具覆盖的所有 SFC 设为 Vapor，包括可能仍被构建插件保留为 VDOM 的普通 `<script>` 文件，不能直接套用。也可显式标记目标组件并保留默认的全局类型模式。

```json
{
  "vueCompilerOptions": {
    "vapor": true
  }
}
```

**建议：** 当源组件依赖全局编译、没有逐文件标记时，在实际覆盖这些组件的 tsconfig 中同步语言工具配置。对于引用多个子项目的根 tsconfig，确认子项目实际继承或设置了该选项；只修改不参与组件检查的配置不会生效。检查项目的 vue-tsc 与编辑器所用 Vue 语言工具版本。

逐文件 `vapor` 标记不需要为了开启这些文件而把所有 SFC 的类型模式强制设为 Vapor。

来源：[language-tools 配置类型](https://github.com/vuejs/language-tools/blob/v3.3.8/packages/language-core/lib/types.ts)、[Vapor 模式判定](https://github.com/vuejs/language-tools/blob/v3.3.8/packages/language-core/lib/plugins/vue-tsx.ts)、[旧版对照类型](https://github.com/vuejs/language-tools/blob/v3.3.7/packages/language-core/lib/types.ts)。

## 混合项目的编辑器模式与编译模式差异

**已核实行为：** language-tools 将“全局 `vueCompilerOptions.vapor` 为 true”或“setup/template 上有显式 vapor 标记”判定为 Vapor。它的全局开关作用于所有 SFC；plugin-vue 的全局开关会保留没有显式 Vapor 标记、只有普通 `<script>` 且无 setup 的 `.vue` 为 VDOM。两者的范围并不完全相同。

**建议：** 混合项目需要同时确认每个源组件的编译结果与语言工具模式。不要单凭编辑器没有报错认定运行时兼容，也不要单凭编辑器对 Vapor 指令报错认定编译器不支持；先检查语言工具版本、有效 tsconfig、文件标记及构建边界。

如果这种全局范围差异影响现有 VDOM 组件，优先考虑逐文件标记并保留语言工具的默认全局模式；否则对实际分流方案进行编译和类型检查验证。不要用宽泛忽略、错误类型断言或 `skipTemplateCodegen` 掩盖模式不一致。

来源：[language-tools 模式判定](https://github.com/vuejs/language-tools/blob/v3.3.12/packages/language-core/lib/plugins/vue-tsx.ts)、[plugin-vue 模式判定](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/utils/vapor.ts)。

## 其他构建工具不共享这项插件配置

**已核实行为：** `features.vapor` 是 `@vitejs/plugin-vue` 的选项，不是所有 Vue 构建工具的通用配置。框架封装的同名概念也可能有不同含义：例如 Nuxt 的 `vue: { vapor: true }` 安装互操作插件，仍按组件显式启用，不等于 Vite 的全局强制转换。

**源码风险与待验证：** 官方 vue-loader 的 `templateLoader.ts` 调用 `compileTemplate` 时没有传递 `descriptor.vapor`。这说明不能仅因升级 Vue 或写入 SFC 标记，就假定该构建链具有完整 Vapor 支持；本文不据此断言所有 webpack 配置必然失败，也不宣称开箱兼容。

**建议：** 对 webpack、Rspack、Rollup 或其他框架适配，检查对应插件是否同步传递脚本和模板的 Vapor 模式、正确连接生成的渲染代码，并用项目实际配置验证开发与生产编译；使用 SSR 时增加 SSR 与 hydration 验证。先确认官方支持或生成结果，再给出该工具链的配置。

来源：[plugin-vue 配置](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/index.ts)、[vue-loader templateLoader](https://github.com/vuejs/vue-loader/blob/v17.4.2/src/templateLoader.ts)、[Nuxt Vapor 文档](https://github.com/nuxt/nuxt/blob/v4.6.0/docs/3.guide/1.concepts/10.vuejs-development.md#vapor-mode)。

## 运行时字符串 template 不会自动成为 Vapor

**已核实行为：** Vue rc.10 常规 full build 的运行时 `compile` 使用 `@vue/compiler-dom`。plugin-vue 的开关处理构建时 SFC，不能将运行时 `template: '<div>...</div>'`、DOM 中的模板或常规 `Vue.compile(...)` 自动转换成 Vapor。

**建议：** 新的 Vapor 页面和组件使用构建时编译的 SFC。若项目有动态字符串模板或手写编译管线，先确认其实际编译器、生成代码和运行时，不把它归入全局 SFC 开关的支持范围。特殊浏览器构建或自定义编译器应单独核查和验证，不能从常规 `compile` API 推导兼容性。

来源：[Vue rc.10 full build 入口与运行时编译器](https://github.com/vuejs/core/blob/v3.6.0-rc.10/packages/vue/src/index.ts)、[plugin-vue 脚本编译模式传递](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/script.ts)。

## 按组件编译：父组件的标记不会改变子组件

**已核实行为：** 模式按每个 SFC 的 descriptor 与插件配置决定。没有开启全局模式时，父组件使用 `<script setup vapor>` 不会自动让它导入的普通 `<script setup>` 子组件成为 Vapor；预编译组件库也不会被父组件的标记重新编译。

**建议：** 分别检查入口、父组件、子组件和第三方依赖的模式。组件跨越 Vapor/VDOM 边界时，按应用入口配置互操作；编译标记本身不替代运行时接入。需要保持纯 Vapor 区域时，不要只检查最外层文件的标记。

示例边界：`Parent.vue` 有显式 `vapor`，它导入的 `Child.vue` 没有标记且全局开关关闭，则前者为 Vapor、后者仍为 VDOM；是否能一起运行还取决于互操作配置与具体 API 的兼容性。

来源：[plugin-vue 按 descriptor 判定模式](https://github.com/vitejs/vite-plugin-vue/blob/plugin-vue%406.0.9/packages/plugin-vue/src/utils/vapor.ts)、[Vue 官方互操作接入说明](https://github.com/vuejs/core/releases/tag/v3.6.0-rc.1#about-vapor-mode)。
