# React SVG 使用

本规则适用于渲染 DOM 的 React Web 代码。

- 图标优先使用项目已有的 `SvgIcon` 等封装，沿用其实际导入路径、参数和样式继承方式。仅在当前构建工具和类型声明支持时通过 `*.svg?react` 导入组件；没有 `SvgIcon` 或 SVG 组件转换支持时，沿用项目已验证可用的 SVG 使用方式，不引用不存在的组件路径或强行使用 `?react`。
- 公共图标放 `src/assets/svg/`，页面专用图标放所属页面的 `assets/svg/`；项目已有图标目录约定时沿用。
- 保留 `viewBox`；单色填充图标用 `fill="currentColor"`，线条图标用 `stroke="currentColor"`，保留 `none`、多色和渐变。
- 图片或背景直接导入 `*.svg` 获取 URL。

组件导入和 URL 导入须与当前构建工具及类型声明一致；项目已有不同的 SVG 导入约定时沿用，不混用两种用途。
