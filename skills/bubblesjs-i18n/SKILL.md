---
name: bubblesjs-i18n
description: 在 Vue 3、React 和普通 JavaScript/TypeScript 项目中接入、使用或排查 BubblesJS i18n，并用 CLI 扫描翻译 key、维护 JSON 语言包和同步 Excel 翻译表。用户提及 BubblesJS 国际化、@bubblesjs/i18n-core、@bubblesjs/i18n-vue、@bubblesjs/i18n-react、@bubblesjs/i18n-cli 或 bubbles-i18n 时使用；不用于无关国际化库的常规任务。
---

# BubblesJS i18n

让应用使用真实的 BubblesJS API 完成翻译、响应式语言切换与词条维护。沿用目标项目的框架、包管理器、语言标识和 key 风格；已有国际化方案时，只处理用户要求的 BubblesJS 接入或迁移范围。

## 先确认上下文

- 查看目标项目的 `package.json`、锁文件、现有初始化模块、Provider 和语言包。根据任务选择 runtime 或 CLI，二者可独立安装。
- 本技能基础 API 依据 [bubblesplant/i18n](https://github.com/bubblesplant/i18n) 在 2026-10-10 的源码快照 `d5deed3b859838e63a9542df9d42d8156fa53f5f`，该快照四个公开包版本均为 `0.0.2`。CLI 参数、空来源保护、报告、Excel 默认值与备份目录规则于 2026-10-12 同步本地工作区变更，不表示对应改动已发布到 npm，也不代表目标项目已安装的 npm 包包含这些变更。
- 遇到版本差异，优先核实已安装包的导出、类型、README 和 `bubbles-i18n --help`；必要时查 [GitHub Releases](https://github.com/bubblesplant/i18n/releases)。尤其不要仅凭版本号假定 npm 产物支持本地源码里的 Excel 命令。
- React peer 要求 `>=18.0.0`；Vue peer 当前为 `^3.5.43`；CLI 文档要求 Node.js `>=22.18.0`。接入前核对目标环境。

## 按任务读取参考

| 任务                                                   | 读取内容                                                                                     |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| 准备 JSON、创建容器、异步加载、持久化、普通 JS/TS 使用 | [references/runtime.md](references/runtime.md)                                               |
| Vue Provider、响应式翻译、computed、selector           | [references/runtime.md](references/runtime.md) 和 [references/vue.md](references/vue.md)     |
| React Provider、Hooks、selector、SSR                   | [references/runtime.md](references/runtime.md) 和 [references/react.md](references/react.md) |
| 静态 key 扫描、JSON 同步、CI 检查、JSON ⇄ Excel        | [references/cli.md](references/cli.md)                                                       |

只读取本次任务需要的参考。局部作用域与 SSR 的公共约束在 runtime 中，框架差异在对应参考中。

## 核心约束

- 词条是扁平的 `Record<string, string>`。`menu.home` 是完整字符串 key；中文原文也可作为 key。占位符为 `{name}`，参数值为字符串或数字。
- 常规首屏用 `createI18n({ locale, message, loaderMessage })`，显式传入默认词条；它同步返回 store，不调用加载器。初始词条需要异步获取或恢复语言偏好时，才用 `await initI18n(...)` 后挂载。
- `tr()` 翻译，`loadLocale()` 加载后切换；不要虚构 `t()`、`setLocale()`、`fallbackLocale`、namespace 参数、复数或 ICU API。
- 加载失败仍会提交目标语言和空词条，翻译回退到 key；加载器异常被捕获，不能只靠 `try/catch loadLocale()` 判断加载失败。
- 组件使用适配器建立订阅。`useI18n()` 读取最近的祖先 Provider；局部区域用独立 store + 嵌套 Provider，不自动合并父词条。SSR 每请求创建 store。
- CLI 只有 `sync`、`check`、`excel export`、`excel import`，没有独立 `scan` 命令。它维护 JSON，不生成运行时词条模块。
- `check` 检查 key 是否存在，不检查翻译完成度。动态 key 不能依赖扫描自动收集；使用 `--prune` 前应核对扫描范围与预览。
- Excel 默认文件为配置目录下的 `.bubbles-i18n/<项目名>.xlsx`，默认工作表为精确小写 `sheet1`；`excel` 可省略或设为 `{}`，`file` 与 `sheet` 可分别覆盖。扫描与 Excel 命令都会解析每个项目的独立默认路径，配置示例见 [CLI 参考](references/cli.md#安装与配置)。
- Excel 备份默认集中到配置目录下的 `.bubbles-i18n/backups`；项目可通过可选 `excel.backupDir` 指定相对配置目录的路径或绝对路径。省略 `backupDir` 或整个 `excel` 均使用默认备份目录，预览不创建备份。自定义备份目录使用专用目录，CLI 扫描会排除全部项目的备份目录；路径限制与备份布局见 [CLI 参考](references/cli.md)。
- Excel 的 key 列和所选语言列只接受实际文本或空白；填写前将列设为“文本”，已有数值仅改显示格式不一定转换类型。`excel export` 也校验现有表，`--force` 不能绕过格式限制；详见 [Excel 单元格格式与报错排查](references/cli.md#excel-单元格格式与报错排查)。
- Excel 冲突默认阻止数据写入；`--force` 默认采用 Excel。命令方向决定写入端，`export --force --prefer excel` 保留 Excel 冲突值，不反写 JSON；写回 JSON 用 `import --force --prefer excel`，JSON 覆盖 Excel 用 `export --force --prefer json`。按任务选择冲突来源，不把强制覆盖写进默认同步命令；组合清理语义见 [Excel 范围与删除](references/cli.md#excel-范围与删除)。

## 完成与验证

接入任务应完成语言 JSON、容器、Provider 和业务组件中的真实翻译调用；CLI 任务应完成目标项目配置及所需命令。不要把库接入扩大为重建项目或修改无关配置。

按改动验证实际行为：默认语言显示正确、插值有效、切换后组件更新；涉及局部作用域时验证语言独立；SSR 核对服务端与水合初值一致。使用项目已有类型检查、构建或相关测试完成必要检查。

词条维护先查看 `sync --dry-run` 或相应 Excel 预览，再执行用户要求的写入。预览仍写报告；`sync`（含预览）和 `check` 默认写扫描 JSON 报告，路径与关闭方式见 [CLI 参考](references/cli.md#报告退出码与操作限制)。汇报修改位置、验证结果，以及仍需人工填写的译文或未解决冲突。
