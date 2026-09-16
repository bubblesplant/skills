# 规则选择清单

本文件是初始化器的资产清单和放置指导，不复制到目标项目，也不替代 `assets/` 中的个人规则正文。

## 选择单位

- 先枚举 `assets/`，再按本清单选择。清单与实际资产不一致时，不猜测新增资产用途；读取其内容，只有适用范围明确时才使用，并在交付中报告清单差异。
- 以项目根和每个真实包为独立选择单位。根级通用规则、前端包规则和局部包规则分别判断，不能因一个包适用就扩散到全部包。
- 规则资产和对应入口视为一个组合：新增规则时同时新增入口；复用目标已有语义规则时，入口链接指向其真实位置。
- 选中资产后保留完整个人规则语义。仅替换参数、路径和与目标技术栈不兼容的示例，不自行降低约束强度。

## 默认布局

目标已有布局清晰且入口有效时沿用。缺少布局时，单体项目使用：

```text
项目根目录/
  AGENTS.md
  .agents/rules/
```

monorepo 的通用规则放根目录，包专属规则放实际包内：

```text
项目根目录/
  AGENTS.md
  .agents/rules/
  <实际包路径>/
    AGENTS.md
    .agents/rules/
```

单体前端将根入口与前端入口合并到根 `AGENTS.md`。monorepo 只给确有专属规则的包创建入口，不批量生成空 `AGENTS.md` 或空规则目录；已有深层局部规则保持原作用范围。

## 资产组合

| 组合 | 规则资产 | 入口资产 | 适用范围 | 排除或前置条件 | 默认目标 |
| --- | --- | --- | --- | --- | --- |
| `root-common` | [代码设计](../assets/rules/common/代码设计.md)、[共享代码](../assets/rules/common/共享代码.md) | [根入口](../assets/AGENTS.root.md) | 承载代码，或管理代码工作区的项目根 | 无 | 根 `AGENTS.md` 与根 `.agents/rules/` |
| `package-entry` | 无固定规则；承载已选包规则 | [其他包入口](../assets/AGENTS.package.md) | 确有包专属规则但缺少入口的真实包 | 不为没有专属规则的包选择 | 包 `AGENTS.md` |
| `frontend-file-split` | [文件拆分](../assets/rules/frontend/文件拆分.md) | [前端入口](../assets/AGENTS.frontend.md)中的“文件拆分”行 | 前端应用、UI 组件包 | 纯后端或工具包排除 | 当前前端范围的 `AGENTS.md` 与 `.agents/rules/` |
| `frontend-page-api` | [页面接口](../assets/rules/frontend/页面接口.md) | [前端入口](../assets/AGENTS.frontend.md)中的“页面接口”行 | 有页面或页面 API 职责的前端应用 | 纯 UI 组件包排除 | 当前前端范围 |
| `frontend-component-reuse` | [组件复用](../assets/rules/frontend/组件复用.md) | [前端入口](../assets/AGENTS.frontend.md)中的“组件复用”行 | 前端应用、UI 组件包 | 无前端组件职责的包排除 | 当前前端范围 |
| `frontend-component-name` | [组件命名](../assets/rules/frontend/组件命名.md) | [前端入口](../assets/AGENTS.frontend.md)中的“组件命名”行 | 前端应用、UI 组件包 | 无前端组件职责的包排除 | 当前前端范围 |
| `frontend-dialog` | [弹窗组件](../assets/rules/frontend/弹窗组件.md) | [前端入口](../assets/AGENTS.frontend.md)中的“弹窗组件”行 | 前端应用、UI 组件包 | 纯后端或工具包排除 | 当前前端范围 |
| `react-web-svg` | [React SVG 使用](../assets/rules/frontend/ReactSVG使用.md) | [React SVG 入口行](../assets/entries/frontend/ReactSVG使用.row.md) | 渲染 DOM 的 React Web 应用或 UI 包 | Vue、React Native、Taro 小程序排除 | 当前 React Web 范围 |
| `react-manual-memo` | [React 手动记忆化](../assets/rules/frontend/React手动记忆化.md) | [React 手动记忆化入口行](../assets/entries/frontend/React手动记忆化.row.md) | React 应用或 React UI 包 | 仅 React Compiler 确认未启用时选择 | 当前 React 范围 |

源码全部位于子包中的 monorepo 根仍属于“管理代码工作区的项目根”，应选择 `root-common`。根入口不仅承载按需规则表，还包含“功能文件归入子目录”的个人强制规则；合并 [AGENTS.root.md](../assets/AGENTS.root.md) 时须一并处理该条款，不能只提取表格行。

`AGENTS.frontend.md` 是前端入口行的来源，不要求整份盲目复制。按已选组合合并相应行，例如纯 UI 组件包不合入页面接口行。`组件复用.md` 中的 React 条款已在正文中限定 React 语境，其他框架仍保留同文件内适用的通用组件规则，不需要在初始化时改写个人规则。

## 入口合并

- 目标已有“按需规则”表时，将选中组合的行合入现有表，不追加第二个同名章节。没有入口结构时才使用对应 `AGENTS.*.md` 模板建立结构。
- React 条件入口文件是表格行片段，只将数据行合入最终的按需表，不把片段另存为目标项目文档。
- 已有语义对应规则时沿用其真实文件名和位置，并据此修改入口链接；不要为了匹配模板文件名再复制一份。
- 入口使用从最终 `AGENTS.md` 到最终规则文件的相对链接。规则内部链接也按最终位置重新计算。
- 根入口中“逐级查找并阅读 `AGENTS.md`”的要求只保留一份；目标已有更详细的发现规则时保留其额外约束。根入口的其他独立个人规则也须逐条语义合并，不能因目标已有按需表而遗漏。

## 模板参数

| 参数 | 取值方式 |
| --- | --- |
| `{{SHARED_TYPES_DIR}}` | 优先使用目标已有的共用类型目录；没有约定的 JS/TS 单体项目使用 `src/types`，monorepo 使用 `packages/shared/types`，其他语言按实际结构适配。存在多个并列共享域时，在最终规则中按作用范围列出，不虚构一个统一目录。 |
| `{{SHARED_UTILS_DIR}}` | 优先使用目标已有的公用方法目录；没有约定的 JS/TS 单体项目使用 `src/utils`，monorepo 使用 `packages/shared/utils`，其他语言按实际结构适配。存在多个并列共享域时，在最终规则中按作用范围列出，不虚构一个统一目录。 |
| `{{PAGE_DIR}}` | 使用当前前端范围的实际页面目录，如 `src/pages`、`src/app`；遵循路由框架约定，没有既有线索时使用 `src/pages`。多个页面根同时生效时，在最终规则中明确列出各自范围，不强行缩成一个默认目录。 |
| `{{GLOBAL_COMPONENTS_DIR}}` | 使用当前前端范围已有的全局组件路径和导入形式；`@` 已指向 `src` 时可用 `@/components`，没有约定时使用 `src/components`，不要为模板新增别名。存在多个并列组件根时，在最终规则中明确各自作用范围。 |
| `{{SHARED_RULE_LINK}}` | 从最终 `文件拆分.md` 到承载“共享代码”规则的位置的相对链接；可以是独立规则文件，也可以是已有 `AGENTS.md` 中对应标题的锚点。必须按实际层级和真实标题计算，不能照抄示例深度；使用标题锚点时确认标题唯一且片段可解析。内联规则没有可链接标题时，可在不改动规则正文的前提下补充明确且不冲突的标题。 |

这些缺省目录只用于生成最终规则文字，不表示目录已经存在，也不授权初始化过程创建目录或业务文件。模板中的目录、扩展名和导入写法与目标不一致时，须按项目实际适配；页面接口的类型与 JSDoc 要求等个人规则不能因技术栈差异被静默删除。

替换参数后，只检查本次新增或修改的规则与入口文件，确认上述五个已知参数均已替换；不要在业务源码中搜索或改写框架自身合法的 `{{...}}` 插值。若目标技术栈无法落实某项强制要求，且本技能的修改边界又不允许调整依赖或构建配置，应将其视为真实冲突，暂缓相冲突条款并按合并规则报告，不能自行删掉或弱化个人规则。

## React 条件资产

- `react-web-svg` 只沿用目标构建工具和类型声明已经支持的 SVG 使用方式，不为套用规则新增依赖、别名或不存在的封装组件。
- 判断 `react-manual-memo` 前读取 [React Compiler 检测](react-compiler-detection.md)。每个 React 作用范围独立得到结果：已启用或无法确认时，规则文件和入口行都不新增；确认未启用时，两者同时选择。
- 一个 React 包的判断不能影响其他 React 包，Vue 等非 React 包不参与检测。
