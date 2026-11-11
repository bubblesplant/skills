# Bubbles 兼容边界与验证入口

按需读取。本文件来自 2026-11-11 依赖维护经验，是复查线索，不是永久禁止升级的版本表。升级时检查实际 manifest、上游发布内容及 peer／engine 要求，已有代码迁移完成后可以调整边界。

## 全依赖升级时复查

- Nest／Vue 工具链当时使用 TypeScript 6，React 模板当时使用 TypeScript 7。Nest CLI、Swagger、vue-tsc、ts-node 是否支持目标编译器必须分别核对，不能只用 npm latest 标签做决定。
- Taro React 当时保持 React 18 及对应类型、Babel 7、react-refresh 0.14，runner 精确要求 webpack 5.91.0。Taro 各包优先同版本，核对官方适配矩阵。
- Taro Vue 的 UnoCSS／webpack 插件当时保持 0.58.9、weapp preset 为 0.58.8。此前 66.x 在当前 Webpack 集成中出现 CommonJS 导出或内嵌字体解析失败；有新版兼容证据后再升级，不为追 latest 自动引入业务迁移或兼容补丁。
- `@vue/babel-plugin-jsx` 当时保留 Babel 7 兼容的 2 系列；Stylelint 保留与现有 SCSS config 匹配的 17 系列。
- `vue-element-plus-x` 当时保留仍提供现有代码所用 `XMarkdown` 的 1 系列。
- Vue Vapor、Pro Components、NutUI 等已有预发布按原通道检查，不把稳定依赖自动换成 beta；Vue Vapor 同时核对编译插件、入口互操作模式及相关类型配置。
- Next 模板的 lefthook 2.2.2 当时被 `trustPolicy: no-downgrade` 拒绝，保留 2.2.1。未来按实际供应链元数据复查，通用策略不放宽。
- 根仓库与 Taro 曾保留特定安全 override、Taro mini-ci 补丁；它们不属于 Vite+ 补丁，不因移除 Vite+ 补丁而一并删除。

## 验证选择

先看现有 `package.json`、`vite.config.ts`、工作空间和项目规则，以下是已有入口示例，不要求无条件执行所有命令：

| 安装单元 | 曾用入口 |
| --- | --- |
| bubbles 根项目 | `vp run typecheck`、`vp run build`、`vp run docs:build` |
| React／NestJS monorepo 模板 | `vp run -r build`、`vp run -r test --run`；server 的 `vp exec tsc --noEmit -p tsconfig.json` |
| 普通 React、Shadcn、pnpm-vp monorepo 模板 | `vp run build` |
| 两个 Vue 模板 | `vp run build`，当时脚本同时执行 `vue-tsc -b` |
| Next／vinext、Rsbuild 模板 | 现有 `typecheck` 与 `build` 脚本 |
| Taro 模板 | `vp exec taro build --type weapp`；不调用含 open／upload 的构建脚本 |

根目录直接运行 `vp test` 曾扫入独立模板，导致浏览器模式、别名、happy-dom 和多份测试运行器的环境不匹配；按各安装单元运行的测试更能验证其实际配置。仍需如实记录根命令执行结果，不得把局部通过描述为全仓全部测试通过。

`pnpm peers check` 对 Vite+ alias 的包版本号可能报告与插件要求的 Vite 主版本不一致；核查实际内置 Vite 版本与运行结果，不为消除告警而扩大 peer 允许范围。其它真实 peer 告警应分别判断与记录。

当前正式记录位于 bubbles 的 `packages/create-bubbles/template-vp-monorepo-react-nestjs/.spaces/05.运行维护/工具链依赖.md`，使用该模板时应按其文档规则在原正文更新实际验收。中文流解码工具位于同目录下 `提交钩子中文路径/工具/验证流解码.mjs`：先观察实际输出，再按它的断言方式记录；失败不授权重新加入已移除的 Vite+ 补丁。
