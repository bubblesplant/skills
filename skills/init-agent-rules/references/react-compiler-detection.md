# React Compiler 检测

仅在某个 React 作用范围可能选择“React 手动记忆化”资产时读取本文件。检测只决定是否新增该规则及入口，不修改依赖或构建配置。

## 检测单位

- 按每个 React 应用或 React UI 包的实际构建作用范围独立判断，并同时检查它继承或实际引用的共享配置。
- 没有独立构建配置、由消费方编译的共享 React 包，应检查实际消费它的构建链。
- 无法识别 React 代码最终由哪条实际构建链编译时，当前作用范围判为“无法确认”，不要按未启用处理。
- 先从该范围的 package scripts、框架入口和工作区配置找到真实构建链，再检查对应配置；不要因为仓库其他包启用了 Compiler 就跳过当前包。
- Vue、非 React 工具包和没有 React 源码的范围不检测。
- 正常开发、生产、测试、Storybook 或文档站流程只要实际编译当前范围内维护的 React 源码，就属于实际构建模式；只展示静态产物、只处理隔离夹具，或没有被任何有效入口引用的配置不算。
- 同一 React 作用范围存在多个实际构建模式时逐一判断，再汇总结果；测试夹具、文档示例、废弃配置和未被脚本引用的样例不属于实际模式。

## 三态结果

对每个实际构建模式判断后，按以下顺序汇总当前 React 作用范围：

1. 任一实际模式有明确启用证据：`已启用`。
2. 没有模式确认启用，但至少一个实际模式因动态或间接配置无法解析：`无法确认`。
3. 所有实际模式都检查完毕且没有启用证据：`确认未启用`。

| 结果 | 初始化行为 |
| --- | --- |
| 已启用 | 不新增、不合并 `React手动记忆化.md`，也不添加对应入口。 |
| 确认未启用 | 同时安装或合并规则文件与对应入口，不能只处理其中一个。 |
| 无法确认 | 仅跳过当前 React 作用范围的规则和入口，并报告无法解析的配置；不影响其他包。 |

目标项目已经存在同主题规则时，本技能不因初始化自动删除它；若当前范围已启用 Compiler，应停止向该规则合入本技能内容，并在交付中报告现有规则与条件不一致。只有用户明确要求清理时才删除或迁移已有内容。

## 明确启用证据

以下配置必须位于当前作用范围实际生效的构建链中，且当前安装版本支持该配置，才算启用：

- Babel、Metro 或 React Router 的有效插件、preset 或 override 实际注册 `babel-plugin-react-compiler`。
- Vite 的 React 插件使用 `react({ compiler: true })`、`react({ compiler: { ... } })`，或实际生效的 Babel 集成注册 `reactCompilerPreset()`。
- Next.js 配置中的 `reactCompiler`，或旧版 `experimental.reactCompiler`，为 `true` 或配置对象。
- Expo 配置中的 `experiments.reactCompiler` 为 `true`，或实际生效的 Expo Babel preset 启用 Compiler。
- Rsbuild 的 `pluginReact` 启用 `reactCompiler`。
- Rspack、SWC 或其他转换器的有效配置实际启用 React Compiler 选项、preset、loader 或插件，例如 `jsc.transform.reactCompiler` 为 `true` 或配置对象。

已确认启用的 Compiler 配置即使使用 `compilationMode: "annotation"`、`sources`、Babel `overrides`、filter 或其他范围限制，也仍判为已启用。普通对象中出现同名字段但没有进入上述构建链，不算证据。

## 不能单独作为启用证据

- `package.json` 或锁文件中只出现 `babel-plugin-react-compiler`、`react-compiler-runtime` 等依赖。
- 仅使用 React 19、Compiler ESLint 插件、healthcheck 或相关编辑器工具。
- 源码中只有 `"use memo"` / `"use no memo"` 指令。
- 注释、README、迁移文档、示例配置、测试夹具或生成产物中出现 Compiler 字样。
- 相关选项明确为 `false`、`null` 或未注册到实际构建链。

仅有依赖记录时，继续检查真实配置；若所有实际配置均可解析且没有启用信号，结果是“确认未启用”，不是“无法确认”。

## 动态与继承配置

- 沿配置的实际导出、导入、变量、函数参数、环境分支和共享 preset 追踪到当前构建脚本使用的值。
- 任一实际分支确认启用后即可将当前作用范围判为“已启用”；不需要为了证明其他分支而继续扩大搜索。
- 只有配置确实进入实际构建链、但其最终值无法从仓库内容可靠确定时，才判为“无法确认”。不要因代码写法复杂就直接猜测启用或关闭。
- 不运行会修改项目、安装依赖或触发完整业务构建的命令来检测 Compiler；使用现有文件和安全的只读检查完成判断。
