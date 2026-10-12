# CLI：静态 key、JSON 与 Excel

本参考基于 BubblesJS i18n 本地源码快照：四个公开包版本 `0.0.2`，Git 提交 `d5deed3b859838e63a9542df9d42d8156fa53f5f`。仓库为 [bubblesplant/i18n](https://github.com/bubblesplant/i18n)。版本号来自本地 `package.json`，不表示已安装 npm 产物一定包含本地全部功能，尤其是 Excel 命令。操作前查看目标项目依赖版本与 `pnpm exec bubbles-i18n --help`，以实际支持的命令为准。

报告规则于 `2026-10-12` 同步自本地 `C:/malei/stu/i18n` 工作区变更；其余基础 API 保留上述 `0.0.2` 快照来源。此报告规则更新描述本地工作区行为，不表示对应改动已发布到 npm。用于已安装包时，应核实该包实际支持的 `report` 默认值与配置类型。

CLI 独立于运行时，只维护词条文件，不创建 Provider、切换语言或生成 `generated.ts`。以下假设项目使用 pnpm；其他包管理器使用项目已有的等价执行方式。

## 安装与配置

README 要求 Node.js `>=22.18.0`，TypeScript 配置由 Node 原生加载，仅使用可擦除类型语法。CLI 包没有 `engines` 校验，安装成功不代表 Node 版本满足要求。

```sh
pnpm add -D @bubblesjs/i18n-cli
```

在目标项目创建 `i18n.config.ts`：

```ts
import { defineConfig } from "@bubblesjs/i18n-cli";

export default defineConfig({
  callNames: ["tr"],
  projects: {
    web: {
      include: ["src/**/*.{js,jsx,ts,tsx,vue}"],
      exclude: ["src/**/*.test.*"],
      catalogs: {
        "zh-CN": "src/locales/zh-CN.json",
        "en-US": "src/locales/en-US.json",
      },
      excel: {
        file: "translations/web.xlsx",
        sheet: "translations",
      },
    },
  },
  // 默认写入 .bubbles-i18n/report.json；可选择以下一种覆盖方式：
  // report: false, // 关闭扫描 JSON 报告
  // report: "reports/i18n.json", // 自定义扫描 JSON 报告路径
});
```

- `projects`、每个项目的 `catalogs` 必须非空。JSON 必须是扁平字符串对象，例如 `{ "welcome": "你好，{name}！" }`；`menu.home` 也是一个完整字符串 key，不是嵌套对象。
- `callNames` 默认 `["tr"]`。项目使用其他调用名时显式配置，例如 `["tr", "$t"]`，不要假定所有翻译函数自动识别。
- `sync` / `check` 所选项目必须有非空 `include`；仅维护 Excel 的项目可省略它。Excel 命令所选项目必须有 `excel.file`，仅支持 `.xlsx`；sheet 默认 `translations`。
- 未指定 `--project` 时选择全部项目，不自动跳过缺少当前用途配置的项目。混合项目配置应显式选范围。
- 所有相对数据、glob 和报告路径基于配置文件所在目录。显式 `--config` 路径相对命令 cwd 解析。
- 默认从 cwd 向上找配置，同目录顺序为 `i18n.config.ts`、`.mts`、`.js`、`.mjs`、`.cts`、`.cjs`。ESM 用 `export default`，CommonJS 用 `module.exports`。
- 不同项目 / locale 不能共用同一个 JSON 路径，各项目 Excel 也必须独立。路径冲突对全部配置全局校验，不能用 `--project` 绕过。

## 扫描与缺失 key

源码使用静态调用：

```ts
tr("welcome", { name: "Bubbles" });
tr("menu.home");
tr(`保存`);
tr(/* 说明 */ "取消" /* 说明 */);
```

先预览，再补齐各语言 JSON，最后检查完整性：

```sh
pnpm exec bubbles-i18n sync --project web --dry-run
pnpm exec bubbles-i18n sync --project web
pnpm exec bubbles-i18n check --project web
```

`sync` 缺失 JSON 自动创建；缺失词条初始值等于 key，如 `"welcome": "welcome"`。已有译文保留，多余 key 默认保留并逐项报告。填译文时保留 `{name}` 等业务需要的占位符。

`check` 不修改语言包，只检查源码静态 key 是否存在于各语言 JSON；缺失 key 返回 `1`。它不检查翻译质量、默认值是否已翻译、空字符串或占位符是否一致。多余 key 默认允许，加 `--fail-on-stale` 使其也失败。缺失 JSON 视作空对象；源码没有 key 时，`check` 不保证空 JSON 文件一定存在。

扫描边界：

- 支持单双引号、无插值模板字符串、调用边界上的空白与注释，记录文件与行列位置。
- 不提取 `tr(key)`、`tr(getKey())`、`tr("prefix-" + value)`、带插值模板字符串。动态 key 需自行维护。
- 使用文本匹配，不用 AST；注释和普通字符串中的完整调用、`obj.tr("key")` 也可能被识别。清理前检查扫描范围和报告。
- 默认排除 `.git`、`.pnpm-store`、`.vite`、`build`、`coverage`、`dist`、`node_modules`、`.bubbles-i18n`、`.bubbles-i18n-backups` 目录；不跟随符号链接，跳过含 NUL 的二进制文件。
- 没有独立 `scan` 子命令。需要编程扫描时，公开 API 为 `scanSource` / `scanFiles`。

仅在用户任务需要删除多余 key 时执行清理，保留动态词条的使用事实：

```sh
pnpm exec bubbles-i18n sync --project web --prune --dry-run
pnpm exec bubbles-i18n sync --project web --prune
```

`--clean` 是扫描 `--prune` 的兼容别名。没有可读取源码时始终拒绝清理；有源码但扫描到零 key，清空非空 JSON 还需 `--allow-empty`。先核实 include、函数名和动态 key，不能把该参数当普通报错修复手段。扫描清理不强制指定项目；因此技能操作示例显式使用 `--project`。

## Excel 翻译工作流

Excel 命令不扫描源码，也不依赖上次同步记录；直接按 key × locale 比较 JSON 与 Excel 当前值。第一列 A1 必须严格为 `key`，语言表头为配置的 locale ID。

```sh
pnpm exec bubbles-i18n excel export --project web --dry-run
pnpm exec bubbles-i18n excel export --project web
```

首次导出可创建工作簿，新文件包含全部已配置语言的表头。已有文件必须包含指定 sheet 与所选语言表头，未选语言缺列不阻断操作。

| key | zh-CN | en-US |
| --- | --- | --- |
| welcome | 你好，{name}！ | welcome |
| menu.home | 首页 | Home |

译员将 `welcome` 英文改为 `Hello, {name}!` 后，普通导入会把它与 JSON 中的 `welcome` 比较，报告值冲突并返回 `1`。任务明确采用 Excel 译文时，预览后执行：

```sh
pnpm exec bubbles-i18n excel import --project web --dry-run
pnpm exec bubbles-i18n excel import --project web --force --prefer excel --dry-run
pnpm exec bubbles-i18n excel import --project web --force --prefer excel
pnpm exec bubbles-i18n check --project web
```

若任务要求将 JSON 译文更新到已有 Excel，使用相反优先方：

```sh
pnpm exec bubbles-i18n excel export --project web --force --prefer json --dry-run
pnpm exec bubbles-i18n excel export --project web --force --prefer json
```

冲突与新增规则：

| 情况 | 行为 |
| --- | --- |
| 来源新增 key / 目标缺值 | 按命令方向补入目标，不属于值冲突 |
| 同 key、同 locale 值相同 | 保持不变 |
| 同 key、同 locale 值不同 | 普通命令返回 `1`，所有所选项目数据均不写，包括计划新增与删除 |
| `--force` / `-f` | 允许处理冲突，默认 `--prefer excel`；两方向默认均如此 |
| export `--force --prefer json` | 将 JSON 冲突值写入 Excel |
| import `--force --prefer excel` | 将 Excel 冲突值写入 JSON |
| export `--force --prefer excel` | 保留目标 Excel 冲突值，仍补新 key，不回写 JSON |
| import `--force --prefer json` | 保留目标 JSON 冲突值，仍补新 key，不回写 Excel |
| Excel 空单元格 / 空字符串 | import 保留 JSON 原值，不新增空值，不按整行缺失删除 |

`--prefer` 必须搭配 `--force`。强制选择只影响冲突值，命令仅写目标端，不按修改时间判断，也不同时同步两边。选择目标端值后，两边可能仍不同，再次运行普通命令仍会报告冲突。

## Excel 范围与删除

`--project`、`--locale` 可重复：

```sh
pnpm exec bubbles-i18n excel import --project web --locale en-US --dry-run
```

目标独有 key 默认保留并报告。`--prune` 只删除这些 key，不解决冲突；`--force` 只解决冲突，不删除 key。Excel `--prune` 必须显式指定至少一个 `--project`：

```sh
pnpm exec bubbles-i18n excel export --project web --prune --dry-run
pnpm exec bubbles-i18n excel import --project web --locale en-US --prune --dry-run
```

- export 以项目**全部已配置语言 JSON 的 key 并集**判断多余行，删除整行；`--locale` 只筛选语言值，不缩小此并集。
- import 以 Excel key 行判断多余 JSON key，仅更新 / 删除所选语言。某行所选语言为空仍表示 key 行存在，不清空 JSON 译文。
- Excel 拒绝用空 JSON 并集清空已有 Excel，或用空 sheet 清空非空 JSON。`--allow-empty` 只适用于扫描。
- 若既有冲突又需删除，按任务确定优先方，使用 `--force --prefer excel|json --prune` 组合并先预览。

## 报告、退出码与操作限制

`--dry-run` 不修改 JSON 语言包或 XLSX 数据、不创建数据备份，**仍写报告**。默认 Markdown 报告会更新：

| 命令 | 路径（相对配置目录） |
| --- | --- |
| sync | `.bubbles-i18n/reports/sync.md` |
| excel export | `.bubbles-i18n/reports/excel-export.md` |
| excel import | `.bubbles-i18n/reports/excel-import.md` |

`sync`、`sync --dry-run` 和 `check` 默认将扫描 JSON 报告写入配置文件所在目录下的 `.bubbles-i18n/report.json`。顶层 `report` 省略时使用此默认路径，设为 `false` 关闭 JSON 报告，设为字符串自定义路径；相对路径以配置文件所在目录为基准。扫描 JSON 报告中的 `added` 是缺失项，`unused` 是保留的多余项，`deleted` 是清理项；预览时这些变更列表表示计划。

`report` 不影响自动 Markdown 报告；Excel 命令只生成 Markdown 报告，不读取或写入扫描 JSON 报告。`check` 无自动 Markdown，不接受 `--dry-run`、`--prune`、`--clean`；`--locale`、`--force`、`--prefer` 仅适用于 Excel，`--fail-on-stale` 仅适用于 check。

退出码：`0` 成功 / 帮助；`1` check 失败、Excel 未解决值冲突或未提供命令；`2` 参数、配置、格式、文件操作错误。若使用编程入口，`runCli` 抛异常，`main` 捕获并转换为 `2`。

操作限制：

- JSON 语言包同步保留已有 BOM、LF / CRLF、缩进和末尾换行，使用同目录临时文件原子替换；多文件操作不是事务。
- Excel 实际改写现有目标文件时，备份到目标同目录 `.bubbles-i18n-backups/<runId>/<filename>`，报告列出备份路径。先准备临时文件与备份，再提交；失败尽力回滚，不保证所有文件完全恢复。
- Excel 仅 `.xlsx`。locale 不得叫 `key`。key / 译文精确匹配，不 trim。重复 key / 非空表头、缺所选语言列、托管 key / 所选语言合并单元格、非字符串译文均报错，force 不绕过。
- 空 key 行只在整行完全空白时忽略；仅备注列有内容也报错。所有非空表头，包括备注列、未选语言，也必须是唯一字符串。
- import 文件不存在报错；已有文件缺指定 sheet 也报错，不悄悄创建 sheet。其他 sheet 与备注列保留，但发生导出写入时重写整本工作簿。
- 单元格字符串最多 32,767 个 UTF-16 代码单元。emoji、Tab、CR / LF、占位符与字面 `_xHHHH_` 支持；XML 非法控制字符、未配对代理项、U+FFFE / U+FFFF 不支持。
- 富文本、超链接、公式等不能作为托管译文。附加单元格若重写后不能保持值会阻断导出；嵌入对象等高级特性不保证保真，使用专门翻译工作簿。

## 源码依据

核实自仓库 `packages/i18n-cli/package.json`、`README.md`、`src/config.ts`、`src/load-config.ts`、`src/command.ts`、`src/files.ts`、`src/scanner.ts`、`src/sync.ts`、`src/excel.ts`、`src/index.ts`，并对照 `apps/docs/guide/cli.md`、`packages/i18n-cli/docs/excel-sync-plan.md` 和相关测试。不要将旧版或其他 i18n 库的 AST 提取、嵌套 JSON、历史同步、自动翻译能力套用到本 CLI。
