# React 接入

适用于 `@bubblesjs/i18n-react`，要求 React `>=18.0.0`。语言包、`src/i18n.ts` 的公共容器初始化、持久化与加载失败行为见 [runtime.md](runtime.md)。下列示例假定该文件导出 `store`，语言为 `zh-CN` / `en-US`，两份扁平 JSON 含相同 key `welcome`，值分别为 `你好，{name}！` 和 `Hello, {name}!`。

## 安装与最小接入

在已有 React 项目中安装，应用自行提供兼容的 `react` 和 `react-dom`；直接从 core 导入创建方法，因此显式声明 core：

```sh
pnpm add @bubblesjs/i18n-core @bubblesjs/i18n-react
```

`src/main.tsx`：

```tsx
import { createRoot } from "react-dom/client";
import { I18nProvider } from "@bubblesjs/i18n-react";
import { store } from "./i18n";
import App from "./App";

createRoot(document.getElementById("root")!).render(
  <I18nProvider store={store}>
    <App />
  </I18nProvider>,
);
```

`src/App.tsx`：

```tsx
import { useI18n } from "@bubblesjs/i18n-react";

export default function App() {
  const { tr, locale, loadLocale } = useI18n();

  return (
    <main>
      <p>{tr("welcome", { name: "Bubbles" })}</p>
      <p>{locale}</p>
      <button
        type="button"
        onClick={() => void loadLocale(locale === "zh-CN" ? "en-US" : "zh-CN")}
      >
        中文 / English
      </button>
    </main>
  );
}
```

`locale` 是普通的 `string | undefined`，不使用 `.value`。组件渲染时调用 `tr(...)`，由适配层订阅促使语言切换后重渲染。容器在所属作用域创建一次，避免每次 render 新建 store。

## 公开 API 与选择器

下面是现有调用签名；`I18nState`、`I18nStore` 来自 core：

```ts
declare function useI18n(): {
  tr: I18nState["tr"];
  loadLocale: I18nState["loadLocale"];
  locale: I18nState["locale"];
};
declare function useI18nStore(store: I18nStore): I18nState;
declare function useI18nStore<T>(
  store: I18nStore,
  selector: (state: I18nState) => T,
): T;
```

`I18nProvider` 接收必需的 `store` 和 `children: ReactNode`，也是默认导出。另外公开 `I18nContext: Context<I18nStore | undefined>` 与 `I18nProviderProps`；没有单独导出的 `UseI18nReturn` 类型。

`useI18nStore` 直接订阅传入容器，不要求 Provider。例如只关注语言：

```tsx
import type { I18nState, I18nStore } from "@bubblesjs/i18n-core";
import { useI18nStore } from "@bubblesjs/i18n-react";

const selectLocale = (state: I18nState) => state.locale;

export function LocaleLabel({ store }: { store: I18nStore }) {
  const locale = useI18nStore(store, selectLocale);
  return <span>{locale}</span>;
}
```

适配层使用 `useSyncExternalStore`；selector 结果 `Object.is` 相等时，不会因该容器更新而重渲染。选择器应保持纯函数，优先返回原始值或稳定引用；每次返回新对象会使这次对象比较不同。源码缓存同一状态快照的选择结果，没有第三个 equality 参数，也没有 `select` 选项对象。组件卸载自动退订。

## Provider 与局部独立语言

`useI18n()` 读取最近的祖先 Provider，缺少 Provider 会抛出 `useI18n must be used within I18nProvider`。在组件返回的 JSX 中渲染内层 Provider，不会改变该组件自身 Hook 的上下文；将要读取内层容器的逻辑拆成后代组件：

```tsx
import type { I18nStore } from "@bubblesjs/i18n-core";
import { I18nProvider, useI18n } from "@bubblesjs/i18n-react";

export function Workspace({ projectStore }: { projectStore: I18nStore }) {
  return (
    <I18nProvider store={projectStore}>
      <ProjectContent />
    </I18nProvider>
  );
}

function ProjectContent() {
  const { tr } = useI18n();
  return <p>{tr("welcome", { name: "Project" })}</p>;
}
```

应用外层 Provider 使用全局 store，`projectStore` 是另行创建的 core 容器。独立容器分别维护语言、词条与加载器；传入同一个 store 会共享状态。局部词条不会自动继承或合并全局词条，缺失 key 返回 key 本身；当前 API 没有 namespace 或 scope 参数。启用持久化时，不同容器使用不同 `storageKey`。

React Provider 通过 Context 的 `value={store}` 传递容器，属性变更会使后代读取新 store；与 Vue 的初始化 provide 行为不同。仍应避免无意创建新 store，尤其不要在每次 render 初始化它。

## SSR

`useI18nStore` 向 `useSyncExternalStore` 提供服务端快照，可以渲染已经初始化的容器；源码测试确认服务端渲染不建立订阅。每请求分别创建 store；同步已有词条用 `createI18n`，需要异步加载时用 `await initI18n(...)` 后渲染。客户端水合前使用相同初始语言与词条。服务器模块顶层共享可变 store 会让请求互相影响，应改为请求作用域的工厂与 Provider。

## 源码依据

本参考核实于本仓库 `0.0.2` 适配包：`packages/i18n-react/src/index.tsx`、`src/use-store.ts`、`package.json`、`tests/i18n-react.test.tsx`，以及 `apps/docs/guide/react.md`、`scopes.md`。后续版本变更时，以目标项目实际安装版本的类型声明和源码为准。
