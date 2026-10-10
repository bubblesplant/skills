# 运行时：core、加载、持久化与作用域

本参考基于技能入口记录的源码快照。接入其他版本时核对实际导出和类型。

## 包与词条格式

```sh
pnpm add @bubblesjs/i18n-core
```

命令示例使用 pnpm；目标项目使用其他包管理器时采用对应命令。框架业务代码直接从 core 导入 API 时，应把 core 声明为直接依赖。

准备 `src/locales/zh-CN.json`：

```json
{
  "welcome": "你好，{name}！",
  "menu.home": "首页",
  "empty": ""
}
```

`src/locales/en-US.json` 使用相同 key：

```json
{
  "welcome": "Hello, {name}!",
  "menu.home": "Home",
  "empty": ""
}
```

- 类型 `Messages = Record<string, string>`，不展开嵌套对象。
- `tr("missing")` 返回 `"missing"`；空字符串译文保留为空字符串。回退的 key 也会进行插值。
- `{name}`、`{count}` 等占位符匹配 `\w+`，即 ASCII 字母、数字和下划线；缺失参数保留原占位符。`0` 正常替换为 `"0"`。
- 不内置 ICU、复数规则、HTML 渲染、地区回退或词条合并。需要这些能力时明确应用扩展的边界，不编造库选项。
- TypeScript 导入 JSON 需要合适的 `resolveJsonModule` 配置。

## 同步首屏与按需加载

以下为可供 Vue、React 和普通脚本共用的初始化方式。先在 `src/locale-loader.ts` 建立显式加载映射，让构建器识别资源，并使支持的语言可见：

```ts
import type { Messages } from "@bubblesjs/i18n-core";
import zhCN from "./locales/zh-CN.json";

const loaders: Record<string, () => Promise<Messages>> = {
  "zh-CN": async () => zhCN,
  "en-US": async () => (await import("./locales/en-US.json")).default,
};

export const loaderMessage = async (locale = "zh-CN"): Promise<Messages> => {
  const load = loaders[locale];
  if (!load) throw new Error(`Unsupported locale: ${locale}`);
  return load();
};
```

在 `src/i18n.ts` 同步创建容器：

```ts
import { createI18n } from "@bubblesjs/i18n-core";
import zhCN from "./locales/zh-CN.json";
import { loaderMessage } from "./locale-loader";

export const store = createI18n({
  locale: "zh-CN",
  message: zhCN,
  loaderMessage,
});
```

`createI18n` 不执行 loader，首屏直接使用中文 JSON。英文包直到切换时才加载；切回中文复用已导入的默认包。语言列表、资源路径、网络加载、缓存、重试由应用决定。

构建器支持时，也可使用仓库文档中的动态路径导入：

```ts
const loaderMessage = async (locale = "zh-CN") =>
  (await import(`./locales/${locale}.json`)).default;
```

不要假定任意运行环境都支持这类路径。普通 Node.js 的 JSON 模块加载方式取决于 Node 版本与构建产物；网络资源也可以用目标应用已有请求工具加载，最后返回扁平词条对象。

普通脚本使用：

```ts
import { store } from "./i18n";

const { tr, loadLocale } = store.getState();
tr("welcome", { name: "Bubbles" }); // 你好，Bubbles！
await loadLocale("en-US");
tr("welcome", { name: "Bubbles" }); // Hello, Bubbles!

const unsubscribe = store.subscribe(() => {
  console.log(store.getState().locale);
});
unsubscribe();
```

保存过的 `tr` 引用始终读取最新 store 词条；保存的 `locale` 值只是当时快照。框架组件应通过适配器订阅。

## 异步初始化与语言偏好

默认词条也需异步获取时：

```ts
import { initI18n } from "@bubblesjs/i18n-core";
import { loaderMessage } from "./locale-loader";

const store = await initI18n({ locale: "zh-CN", loaderMessage });
// 等待初始化后挂载应用，将这个 store 交给 Provider。
```

在实际项目中选择一种初始化方式：采用此方式时，替换同步创建 store 的入口，再将同一个初始化结果传给 Provider。

需要恢复保存的语言时，使用 `initI18n` 的存储选项：

```ts
import { createJsonStorage, initI18n } from "@bubblesjs/i18n-core";
import { loaderMessage } from "./locale-loader";

const storage = createJsonStorage(
  typeof window === "undefined" ? undefined : window.localStorage,
);

const store = await initI18n({
  locale: "zh-CN",
  loaderMessage,
  storage,
  storageKey: "app:locale",
});
```

- `initI18n` 优先读取保存语言，无保存值才使用传入 `locale`；它调用一次 loader，并返回 `Promise<I18nStore>`。
- `createI18n` 不读取保存值。两者只有同时提供 `storage` 与非空 `storageKey` 才在状态变化后保存语言；不保存词条，初始化不写入默认语言。
- `createJsonStorage` 包装同步的 `getItem`、`setItem`、`removeItem` 字符串存储。损坏 JSON 会尝试删除；底层操作异常被忽略；写 `undefined` 会删除。无底层存储时读取 `null`、写入无操作。
- 适配器只做 JSON 解析，不校验存储数据类型或支持语言。保存值应是 JSON 字符串（如 `"en-US"`），已有外部缓存需校验。
- 浏览器禁止访问 `localStorage` 时，取得存储对象这一步也可能抛错；应用按自身运行环境选择存储或使用无存储模式。

## 加载语义与错误处理

加载期间保留旧语言和旧词条；完成后一次提交 `locale` 与 `message`。并发切换以最后一次调用为准，较早请求完成后不会覆盖最新请求结果。每次调用都可能执行 loader，core 没有内置词条缓存。

loader 返回 `undefined` 或抛错时，`loadLocale` 仍切换为目标语言与 `{}`；异常通过 `console.warn` 记录，`loadLocale` 不因该加载异常 reject。`initI18n` 加载失败也返回空词条容器。上例对不支持语言抛错会触发同样行为，应用应在切换前限制到支持的语言列表。

如果需求要求失败时保持旧语言，在应用层先确认词条成功加载再提交状态，或另行管理切换流程。仅在 loader 中抛错或对 `loadLocale` 写 `try/catch` 不能实现该需求。不要宣称 core 自带 loading/error 状态。

## Store 与公共 API

| API | 真实行为 |
| --- | --- |
| `createI18n(options?)` | 同步创建 `I18nStore`；省略语言时 `locale` 为 `undefined`，省略词条时为 `{}` |
| `initI18n(options?)` | 恢复语言偏好并加载词条；选项不含 `message` |
| `createI18nStore`、`i18n.init` | 分别兼容 `createI18n`、`initI18n` 的旧入口 |
| `formatMessage(message, values?)` | 独立进行占位符替换 |
| `createJsonStorage(storage?)` | JSON 存储适配器 |
| `createStore(initialState, onChange)`、`shallowEqualObject(a, b)` | 通用订阅容器和浅比较工具；普通接入通常无需直接使用 |

`CreateI18nOptions` 包含 `locale?: string`、`message?: Messages`、`loaderMessage?: (locale?: string) => Promise<Messages | undefined>`、`storage?: JsonStorage`、`storageKey?: string`。

`I18nStore` 提供 `getState()`、`setState(updater)`、`subscribe(listener)`；状态为 `locale`、`message`、`tr(key, values?)`、`loadLocale(locale)`。`setState` 的 updater 返回新的完整状态，保留方法：

```ts
store.setState((state) => ({
  ...state,
  locale: "en-US",
  message: loadedMessages,
}));
```

这里的 `loadedMessages` 必须是应用已经成功加载的词条。通知同步发生，浅比较相等时不通知；不要直接改当前状态或内部词条对象。手动提交与正在进行的 `loadLocale` 混用时，应用需处理后续异步提交对手动状态的覆盖。

## 局部作用域与 SSR

每个独立区域创建自己的 store，并用嵌套 Provider 包住该区域的业务组件。`useI18n()` 读取最近的祖先 Provider；同一个组件里渲染的新 Provider 不会影响该组件本身的 hook/composable。

不同 store 可对相同 key 提供不同译文；不继承或合并父词条。多个 Provider 接收同一个 store 时共享状态。store 在所属客户端作用域创建一次，保持引用稳定；持久化键按作用域或项目 ID 区分。

SSR 每请求创建容器，避免服务端模块级共享可变状态。服务端与客户端水合时使用相同初始语言和词条；浏览器偏好恢复若会改变初值，应安排在一致的水合流程内。库没有专用 SSR 初始化选项，框架接入见 [Vue](vue.md) 或 [React](react.md)。

源码依据：`packages/i18n-core/src/{index,types,i18n,format,store,storage}.ts`，`packages/i18n-core/tests/`，`apps/docs/guide/{core,scopes}.md`。
