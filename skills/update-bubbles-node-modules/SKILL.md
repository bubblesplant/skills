---
name: update-bubbles-node-modules
description: 按个人项目范围维护依赖：C:\malei\stu 下的 bubbles、antv-next-pro、workflow、i18n 升级全部兼容依赖；扫描 C:\malei\job 和 C:\malei\stu，其余使用 Vite+ 的项目仅升级 Vite+ 及必要配套版本。用户要求执行这套批量升级、寻找这些目录中的 Vite+ 项目或调整该流程时使用。
---

# update bubbles node_modules

始终使用中文沟通。按本次用户请求执行扫描或升级；用户仅要求查找项目、编写或修改技能时，交付清单或技能即可，不把它当作批量修改项目的授权。

## 固定范围与版本选择

| 范围 | 默认维护内容 |
| --- | --- |
| `C:\malei\stu\bubbles` | 根工作空间、全部包、全部脚手架模板的兼容直接依赖、catalog、相关 overrides，以及每个已有锁文件；包括未采用 Vite+ 的模板 |
| `C:\malei\stu\antv-next-pro`、`C:\malei\stu\workflow`、`C:\malei\stu\i18n` | 全部兼容直接依赖、工作空间成员、catalog、相关 overrides，以及各自已有锁文件；不局限于 Vite+ |
| `C:\malei\job`、`C:\malei\stu` 中除以上四个范围外的 Vite+ 项目 | 仅更新 Vite+、现有配套 Vite 核心 alias、相关 override／peer 版本规则及由此必要变化的锁文件 |

以上四个全依赖项目及其成员按各自范围处理一次，不再重复计入 Vite+ 专项升级。全依赖范围内未使用 Vite+ 的包也要检查。仅升级 Vite+ 的项目不运行全依赖升级，不顺带更新 Vue、React、Nest、TypeScript、ESLint 等无关直接声明。Vite+ 的内置工具版本及必要传递依赖变化属于工具链升级。

本机目录实际名为 `antv-next-pro`；用户提及 `antdv-next-pro` 时按上述实际路径定位。

用户指定的目标版本优先，不能把本次示例的 `1.5.1` 固化为未来默认值。未指定版本时，联网查询 npm 官方源的 Vite+ 最新稳定版，在开始更新前告知实际选择；已有预发布版本按用户选择的通道处理。Vite+ 包版本与内部 Vite 版本不同：现有 `vite: npm:@voidzero-dev/vite-plus-core@<版本>` 应和 `vite-plus` 同步，不能把普通 `vite` 包直接设成 Vite+ 的版本号，也不擅自迁移项目现有工具链架构。

## 发现项目

先运行只读扫描脚本，默认即扫描两个目录：

```powershell
python "$env:USERPROFILE/.codex/skills/update-bubbles-node-modules/scripts/discover_projects.py" --output <本轮清单.json> --markdown <本轮清单.md>
```

脚本只读取 manifest、workspace 和目录标记，不执行项目代码、安装或升级。它优先使用 `rg`，排除依赖、VCS、构建和缓存目录，不跟随目录链接；没有 `rg` 时用标准库遍历。默认全依赖范围是上述四个项目。可用 `--roots <目录...>`、`--full-upgrade-roots <目录...>` 覆盖扫描根与全依赖范围；旧参数名 `--full-upgrade-root` 作为别名保留。

输出分为有依赖声明的项目与仅有 `vp` 脚本的候选，包含独立安装单元、Git 根目录、版本声明和扫描错误。安装单元是候选：执行前核对 workspace 成员、嵌套仓库和锁文件归属；共享 catalog 的子包在所属 workspace 更新，独立模板按自己的配置安装。仅脚本命中不等于已确认本地依赖，检查是否依赖全局 CLI，不能自动补入依赖或升级全局工具。

[项目清单](references/project-inventory.md)是最近一次扫描快照，仅供定位；每次执行重新扫描，并明确报告访问失败或无法解析的文件。

## 执行升级

1. 读取每个实际操作目录适用的 `AGENTS.md` 与必要项目规则。保存 Git 状态、暂存区和本轮待改文件基线；保留用户已有修改，不运行会格式化并重新暂存文件的 `vp staged`。已是目标版本且配置一致的项目记为无需更新。
2. 四个全依赖项目分别检查全部依赖的 npm 版本及 peer／engine 兼容性，覆盖各自工作空间与独立安装单元。稳定依赖不切换到预发布，已有预发布沿原通道；库对外 peer 范围不机械替换成单一最新版本。维护 bubbles 时按需读[兼容与验证参考](references/compatibility.md)，重新检查当时的适用性；其它全依赖项目按各自项目配置判断兼容性。
3. Vite+ 专项范围的项目逐项更新现有 Vite+ 声明和配套版本配置，覆盖直接依赖、catalog、现有核心 alias、Vite override、版本相关的 peer 规则及精确发布年龄例外。保留通配规则的原有语义；不重建或宽泛替换安装策略。普通 Vite 是否需要调整，应由新工具链实际要求与项目现状决定。
4. `bubbles` 延续已确认的 Vite+ 补丁移除状态。其它仓库的补丁先核对内容和新版上游实现，不能把 bubbles 的决定自动扩散。处理目标版本所需的补丁兼容问题并验证；无法安全迁移时，保留该项目原状并记录具体阻塞，不用无补丁安装冒充等价升级。无关补丁继续保留。
5. 在各自安装根目录使用项目原有包管理器同步依赖和已有锁文件，不手工替换锁文件版本。Vite+ 项目优先遵循其 `vp install` 约定；嵌套模板安装考虑 `--ignore-scripts`，防止 prepare 将外层 Git hooks 指向模板。镜像缺少已发布版本时可为本次命令指定 npm 官方源，不永久修改 registry。供应链策略拒绝时保留约束，报告并跳过受阻版本／项目，不放宽 `trustPolicy`、`minimumReleaseAge` 或关闭校验。
6. 检查依赖声明的差异是否落在对应范围内。Vite+ 专项范围的项目允许工具链必需的传递依赖或 peer 快照变化，无关直接声明必须保持原有内容；四个全依赖项目按完整依赖升级检查。保持原有无锁文件项目的布局，验证时新生成的锁文件在结束前仅按本轮基线决定是否移除。

## 验证与交付

按项目实际脚本做类型检查、构建和相关测试，区分 `vp <内置命令>` 与 `vp run <脚本>`。只对本轮文件做格式检查；已有全仓格式或测试环境问题记录实际边界，不批量改写业务文件。Taro 只执行构建验证，不运行带上传、发布或打开开发者工具的脚本。

有 pnpm 锁文件时，在安装根目录冻结校验；例如遵循现有 Vite+／pnpm 项目的调用方式：

```powershell
vp install --lockfile-only --ignore-scripts --frozen-lockfile -- --registry=https://registry.npmjs.org
```

验证目标 Vite+ 和现有配套核心版本一致、旧版本配置无残留、补丁状态符合本仓库决定、用户暂存区未变化；恢复本轮构建带来的无关生成文件。若 bubbles 中保留中文流解码验证工具，按实际安装版本重跑，记录新结果，不沿用历史失败数量或恢复补丁来获得通过结果。

bubbles 的本轮发布相关改动按既有 Changesets 规则创建或更新 patch changeset，避免为同一批未发布改动重复创建；仅开发依赖变化是否需要发布按包的发布惯例决定。其它项目遵循其已有发布规范及用户要求。不要执行 `changeset version`、发布、提交、推送、部署或数据库迁移，除非用户另有明确要求。

较大的临时安装项目放在 `C:\Users\Administrator\Documents\Codex\scratch-tests` 的本轮专属子目录。需要的报告先保存到工作区；用 `try/finally` 清理本轮临时目录，删除前校验绝对路径，不跟随链接。清理被策略拒绝或文件占用时不绕过，如实列出遗留路径。

最终按两种升级范围分别汇报：发现数、实际升级／无需更新／跳过数、目标版本、changeset、验证结果和未解决问题。为项目路径和交付文件给出可点击的绝对路径链接；只扫描时明确本轮完成的是发现与清单。
