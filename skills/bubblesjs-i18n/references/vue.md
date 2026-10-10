# Vue 接入

适用于 `@bubblesjs/i18n-vue`。当前实现要求 Vue `^3.5.43`；已有项目先检查安装版本。语言包、`src/i18n.ts` 的公共容器初始化、持久化与加载失败行为见 [runtime.md](runtime.md)。下列示例假定该文件导出 `store`，语言为 `zh-CN` / `en-US`，两份扁平 JSON 含相同 key `welcome`，值分别为 `你好，{name}！` 和 `Hello, {name}!`。

## 安装与最小接入

在已有 Vue 项目中安装；直接从 core 导入创建方法，因此显式声明 core：

```sh
pnpm add @bubblesjs/i18n-core @bubblesjs/i18n-vue
```

`src/main.ts`：

```ts
import { createApp } from "vue";
import App from "./App.vue";

createApp(App).mount("#app");
```

`src/App.vue`：

```vue
<script setup lang="ts">
import { I18nProvider } from "@bubblesjs/i18n-vue";
import { store } from "./i18n";
import Greeting from "./Greeting.vue";
</script>

<template>
  <I18nProvider :store="store">
    <Greeting />
  </I18nProvider>
</template>
```

`src/Greeting.vue`：

```vue
<script setup lang="ts">
import { useI18n } from "@bubblesjs/i18n-vue";

const { tr, locale, loadLocale } = useI18n();

async function switchLocale() {
  await loadLocale(locale.value === "zh-CN" ? "en-US" : "zh-CN");
}
</script>

<template>
  <p>{{ tr("welcome", { name: "Bubbles" }) }}</p>
  <p>{{ locale }}</p>
  <button type="button" @click="switchLocale">中文 / English</button>
</template>
```

`locale` 在脚本中读 `.value`，模板自动解包。动态文字在模板或 `computed(() => tr(...))` 中求值；在 setup 中保存 `const title = tr(...)` 得到的普通字符串不会随语言切换自动更新。

## 公开 API 与直接订阅

下面是现有签名；`I18nState`、`I18nStore` 来自 core，`ComputedRef`、`ShallowRef` 来自 Vue：

```ts
interface UseI18nReturn {
  tr: I18nState["tr"];
  loadLocale: I18nState["loadLocale"];
  locale: ComputedRef<I18nState["locale"]>;
}

declare function useI18n(): UseI18nReturn;
declare function useI18nStore(store: I18nStore): ShallowRef<I18nState>;
declare function useI18nStore<T>(
  store: I18nStore,
  selector: (state: I18nState) => T,
): ComputedRef<T>;
```

`I18nProvider` 接收必需的 `store` 并原样渲染默认插槽，也是默认导出。另外公开 `I18nKey: InjectionKey<I18nStore>`、`I18nProviderProps` 和 `UseI18nReturn`。

不经 Provider 也可直接订阅，在组件 setup 或活动的 `effectScope` 中调用：

```ts
import { useI18nStore } from "@bubblesjs/i18n-vue";
import { store } from "./i18n";

const state = useI18nStore(store);
const locale = useI18nStore(store, (snapshot) => snapshot.locale);
// 脚本中通过 state.value / locale.value 读取。
```

适配层使用浅引用保存完整状态，并在容器更新时替换快照。通过 core 的方法更新状态，避免直接改动 `state.value.message` 内部。选择器返回计算引用；仅选择 locale 时，locale 未变的词条更新不会使该选择器订阅的组件重渲染。作用域销毁会自动退订，避免在没有活动作用域的普通模块顶层调用 composable。

## Provider 与局部独立语言

`useI18n()` 必须在 Provider 的后代组件中调用。`App.vue` 在自己模板中渲染 Provider，但它的 setup 不能读取这个 Provider；应像示例一样将 Hook 放在 `Greeting.vue` 中。缺少祖先 Provider 会抛出 `useI18n must be used within I18nProvider`。

局部独立语言用独立 core 容器和嵌套 Provider：

```vue
<template>
  <I18nProvider :store="globalStore">
    <GlobalContent />
    <I18nProvider :store="projectStore">
      <ProjectContent />
    </I18nProvider>
  </I18nProvider>
</template>
```

`globalStore` / `projectStore` 分别创建并持有自己的语言、词条与加载器。最近的 Provider 决定使用哪个容器；传入同一个 store 会共享状态。局部词条不会自动继承或合并全局词条，缺失 key 返回 key 本身；当前 API 没有 namespace 或 scope 参数。启用持久化时，不同容器使用不同 `storageKey`。

**Vue Provider 只在初始化时执行 provide，不跟随 store 属性替换重新注入。** 保持容器引用稳定；确需替换时，同时更换 Provider 的 `key`，重新挂载子树：

```vue
<I18nProvider :key="providerKey" :store="currentStore">
  <Greeting />
</I18nProvider>
```

应用在替换 `currentStore` 时一起更新 `providerKey`。直接 `useI18nStore(props.store)` 的订阅也绑定调用时传入的容器，不会自行追踪 prop 替换。

## SSR

客户端入口的模块级 store 示例只适合该客户端应用。服务端每请求分别创建容器，预加载请求语言；异步词条可用 `await initI18n(...)`。通过请求内的根组件属性传递 store，保持 Provider 引用稳定。客户端水合前使用相同初始语言与词条，避免请求间共享可变语言状态或水合首屏不一致。Vue 包没有单独的 SSR 初始化函数。

## 源码依据

本参考核实于本仓库 `0.0.2` 适配包：`packages/i18n-vue/src/index.ts`、`src/use-store.ts`、`package.json`，以及 `apps/docs/guide/vue.md`、`scopes.md`。后续版本变更时，以目标项目实际安装版本的类型声明和源码为准。
