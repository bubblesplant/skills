# 项目依赖升级扫描清单

扫描时间：2026-11-11T14:42:38+08:00。本轮只读扫描，没有执行安装或升级。

共解析 837 个 package.json；发现 32 个有 Vite+ 声明的安装单元候选，其中全依赖范围内 10 个，仅升级 Vite+ 范围内 22 个（12 个 Git 根目录）。
仅脚本候选 0 个；待补充检查的 workspace 候选 0 个；扫描错误 0 个。

工作空间 YAML 按常见块状标量提取，完整列表见 JSON 的 workspace_files_for_review；需复核锚点、别名和 flow 写法。安装根也需核对 workspace 成员及嵌套仓库，不能直接把数量视为独立 Git 仓库数。

## 全部兼容依赖升级范围

以下项目的工作空间成员和独立模板均检查全部依赖，包括未使用 Vite+ 的包。

### antv-next-pro

范围：[C:\malei\stu\antv-next-pro](<C:/malei/stu/antv-next-pro>)；包含 4 个 manifest、1 个安装单元候选。

- [C:\malei\stu\antv-next-pro](<C:/malei/stu/antv-next-pro>)

### bubbles

范围：[C:\malei\stu\bubbles](<C:/malei/stu/bubbles>)；包含 30 个 manifest、11 个安装单元候选。

- [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-nextjs-vinext-eslint](<C:/malei/stu/bubbles/packages/create-bubbles/template-nextjs-vinext-eslint>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-pnpm-vp-monorepo](<C:/malei/stu/bubbles/packages/create-bubbles/template-pnpm-vp-monorepo>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-react-rsbuild-biome](<C:/malei/stu/bubbles/packages/create-bubbles/template-react-rsbuild-biome>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-taro-react-oxc](<C:/malei/stu/bubbles/packages/create-bubbles/template-taro-react-oxc>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-taro-vue-eslint](<C:/malei/stu/bubbles/packages/create-bubbles/template-taro-vue-eslint>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-monorepo-react-nestjs](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-monorepo-react-nestjs>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-react](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-react>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-react-shadcn](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-react-shadcn>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-vue-eslint-vapor](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-vue-eslint-vapor>)
- [C:\malei\stu\bubbles\packages\create-bubbles\template-vue-vp-eslint](<C:/malei/stu/bubbles/packages/create-bubbles/template-vue-vp-eslint>)

### i18n

范围：[C:\malei\stu\i18n](<C:/malei/stu/i18n>)；包含 9 个 manifest、1 个安装单元候选。

- [C:\malei\stu\i18n](<C:/malei/stu/i18n>)

### workflow

范围：[C:\malei\stu\workflow](<C:/malei/stu/workflow>)；包含 8 个 manifest、1 个安装单元候选。

- [C:\malei\stu\workflow](<C:/malei/stu/workflow>)


## 全依赖范围内使用 Vite+ 的安装单元

| 安装单元候选 | 当前声明 | Git 根目录 |
| --- | --- | --- |
| [C:\malei\stu\antv-next-pro](<C:/malei/stu/antv-next-pro>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; catalog.vite-plus = 1.5.0; devDependencies.vite-plus = catalog: | [C:\malei\stu\antv-next-pro](<C:/malei/stu/antv-next-pro>) |
| [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.1; catalog.vite-plus = 1.5.1; devDependencies.vite-plus = catalog: | [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>) |
| [C:\malei\stu\bubbles\packages\create-bubbles\template-pnpm-vp-monorepo](<C:/malei/stu/bubbles/packages/create-bubbles/template-pnpm-vp-monorepo>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.1; catalog.vite-plus = 1.5.1; devDependencies.vite-plus = catalog: | [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>) |
| [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-monorepo-react-nestjs](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-monorepo-react-nestjs>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.1; catalog.vite-plus = 1.5.1; devDependencies.vite-plus = catalog: | [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-monorepo-react-nestjs](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-monorepo-react-nestjs>) |
| [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-react-shadcn](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-react-shadcn>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.1; devDependencies.vite-plus = 1.5.1; overrides.vite = npm:@voidzero-dev/vite-plus-core@1.5.1 | [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>) |
| [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-react](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-react>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.1; devDependencies.vite-plus = 1.5.1; overrides.vite = npm:@voidzero-dev/vite-plus-core@1.5.1 | [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>) |
| [C:\malei\stu\bubbles\packages\create-bubbles\template-vp-vue-eslint-vapor](<C:/malei/stu/bubbles/packages/create-bubbles/template-vp-vue-eslint-vapor>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.1; devDependencies.vite-plus = 1.5.1 | [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>) |
| [C:\malei\stu\bubbles\packages\create-bubbles\template-vue-vp-eslint](<C:/malei/stu/bubbles/packages/create-bubbles/template-vue-vp-eslint>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.1; devDependencies.vite-plus = 1.5.1 | [C:\malei\stu\bubbles](<C:/malei/stu/bubbles>) |
| [C:\malei\stu\i18n](<C:/malei/stu/i18n>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; catalog.vite-plus = 1.5.0; devDependencies.vite-plus = catalog: | [C:\malei\stu\i18n](<C:/malei/stu/i18n>) |
| [C:\malei\stu\workflow](<C:/malei/stu/workflow>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; catalog.vite-plus = 1.5.0; devDependencies.vite-plus = catalog: | [C:\malei\stu\workflow](<C:/malei/stu/workflow>) |

## 其余项目：仅升级 Vite+

| 安装单元候选 | 当前声明 | Git 根目录 |
| --- | --- | --- |
| [C:\malei\job\bee\bee-charger-admin](<C:/malei/job/bee/bee-charger-admin>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; catalog.vite-plus = 1.5.0; devDependencies.vite-plus = catalog: | [C:\malei\job\bee\bee-charger-admin](<C:/malei/job/bee/bee-charger-admin>) |
| [C:\malei\job\bee\bee-drama\bee-drama-flash - 副本](<C:/malei/job/bee/bee-drama/bee-drama-flash - 副本>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | 未发现 |
| [C:\malei\job\bee\bee-drama\bee-drama-flash-claude](<C:/malei/job/bee/bee-drama/bee-drama-flash-claude>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\job\bee\bee-drama\bee-drama-flash-claude](<C:/malei/job/bee/bee-drama/bee-drama-flash-claude>) |
| [C:\malei\job\bee\bee-drama\bee-drama-flash-gemini](<C:/malei/job/bee/bee-drama/bee-drama-flash-gemini>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | 未发现 |
| [C:\malei\job\bee\bee-drama\bee-drama-flash-lj](<C:/malei/job/bee/bee-drama/bee-drama-flash-lj>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | 未发现 |
| [C:\malei\job\bee\bee-drama\bee-drama-flash](<C:/malei/job/bee/bee-drama/bee-drama-flash>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\job\bee\bee-drama\bee-drama-flash](<C:/malei/job/bee/bee-drama/bee-drama-flash>) |
| [C:\malei\job\bee\bee-screen](<C:/malei/job/bee/bee-screen>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\job\bee\bee-screen](<C:/malei/job/bee/bee-screen>) |
| [C:\malei\job\iglobal-platform\apps\portal](<C:/malei/job/iglobal-platform/apps/portal>) | devDependencies.vite-plus = catalog: | [C:\malei\job\iglobal-platform](<C:/malei/job/iglobal-platform>) |
| [C:\malei\job\iglobal-platform](<C:/malei/job/iglobal-platform>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; catalog.vite-plus = 1.5.0; devDependencies.vite-plus = catalog: | [C:\malei\job\iglobal-platform](<C:/malei/job/iglobal-platform>) |
| [C:\malei\job\liangjiang-engineering-project-lifecycle\ad-eplmbi-fe](<C:/malei/job/liangjiang-engineering-project-lifecycle/ad-eplmbi-fe>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\job\liangjiang-engineering-project-lifecycle\ad-eplmbi-fe](<C:/malei/job/liangjiang-engineering-project-lifecycle/ad-eplmbi-fe>) |
| [C:\malei\job\liangjiang-engineering-project-lifecycle\web](<C:/malei/job/liangjiang-engineering-project-lifecycle/web>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\job\liangjiang-engineering-project-lifecycle\web](<C:/malei/job/liangjiang-engineering-project-lifecycle/web>) |
| [C:\malei\job\liangjiang-engineering-project-lifecycle\workflow-test](<C:/malei/job/liangjiang-engineering-project-lifecycle/workflow-test>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | 未发现 |
| [C:\malei\stu\core](<C:/malei/stu/core>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\stu\core](<C:/malei/stu/core>) |
| [C:\malei\stu\dark-mode](<C:/malei/stu/dark-mode>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | 未发现 |
| [C:\malei\stu\lowercode\bubbles-project](<C:/malei/stu/lowercode/bubbles-project>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\stu\lowercode](<C:/malei/stu/lowercode>) |
| [C:\malei\stu\lowercode\codex\monorepo-demo](<C:/malei/stu/lowercode/codex/monorepo-demo>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; catalog.vite-plus = 1.5.0; devDependencies.vite-plus = catalog: | [C:\malei\stu\lowercode](<C:/malei/stu/lowercode>) |
| [C:\malei\stu\stu-repository\blackhole\bubbles-project](<C:/malei/stu/stu-repository/blackhole/bubbles-project>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\stu\stu-repository](<C:/malei/stu/stu-repository>) |
| [C:\malei\stu\stu-repository](<C:/malei/stu/stu-repository>) | devDependencies.vite-plus = 1.5.0 | [C:\malei\stu\stu-repository](<C:/malei/stu/stu-repository>) |
| [C:\malei\stu\stu-repository\react\zustand-store](<C:/malei/stu/stu-repository/react/zustand-store>) | devDependencies.vite-plus = 1.5.0 | [C:\malei\stu\stu-repository](<C:/malei/stu/stu-repository>) |
| [C:\malei\stu\test\黑洞预加载](<C:/malei/stu/test/黑洞预加载>) | devDependencies.vite-plus = 1.5.0 | [C:\malei\stu\test\黑洞预加载](<C:/malei/stu/test/黑洞预加载>) |
| [C:\malei\stu\tiny-engine-stu\child1](<C:/malei/stu/tiny-engine-stu/child1>) | catalog.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; catalog.vite-plus = 1.5.0; devDependencies.vite-plus = catalog: | [C:\malei\stu\tiny-engine-stu](<C:/malei/stu/tiny-engine-stu>) |
| [C:\malei\stu\tiny-engine-stu\parent](<C:/malei/stu/tiny-engine-stu/parent>) | devDependencies.vite = npm:@voidzero-dev/vite-plus-core@1.5.0; devDependencies.vite-plus = 1.5.0 | [C:\malei\stu\tiny-engine-stu](<C:/malei/stu/tiny-engine-stu>) |

## 仅脚本候选

这些目录有 vp／vpr／vpx 脚本，尚未确认本地 Vite+ 依赖；不能自动补依赖或升级全局 CLI。

无。

## Workspace 额外候选

无。

## 扫描错误

无。

本文件是最近一次扫描的定位快照；每次升级前重新扫描。完整声明、脚本和锁文件路径见同目录 project-inventory.json。
