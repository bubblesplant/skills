# React SVG 使用

本规则适用于渲染 DOM 的 React Web 代码。

- 图标默认通过 `*.svg?react` 导入，使用 `SvgIcon` 统一渲染，默认导入路径为 `@/components/Icon/svg-icon/SvgIcon`；用 `size`、`color` 控制大小和颜色，不传时继承父级。已有封装时沿用其实际路径和参数。
- 公共图标放 `src/assets/svg/`，页面专用图标放所属页面的 `assets/svg/`；项目已有图标目录约定时沿用。
- 保留 `viewBox`；单色填充图标用 `fill="currentColor"`，线条图标用 `stroke="currentColor"`，保留 `none`、多色和渐变。
- 图片或背景直接导入 `*.svg` 获取 URL。

组件导入和 URL 导入须与当前构建工具及类型声明一致；项目已有不同的 SVG 导入约定时沿用，不混用两种用途。
