# lecture-mindmap-html

一个给 Codex 用的 skill，专门把课件、PDF、PPT 课件导出和已有章节样例整理成静态 HTML 思维导图。

## 能做什么

- 根据课件生成两种 HTML：
  - `脉络大纲版`：粗线条主线、章节结构、核心问题、对比表
  - `细致解析版`：页码、公式、算法步骤、例题、考点
- 优先复用内置模板，不重新设计风格
- 生成后用脚本检查 HTML 结构是否完整

## 使用方式

在 Codex 对话里直接调用：

```text
用 $lecture-mindmap-html 根据这些课件生成脉络大纲版和细致版 HTML 思维导图
```

## 目录结构

- `SKILL.md`：skill 的核心说明
- `agents/openai.yaml`：界面元数据
- `assets/templates/`：内置 HTML 模板
- `references/`：抽取规则和样式规范
- `scripts/`：结构检查脚本

## 仓库说明

这个仓库保存的是 skill 本体和内置模板资产。它不包含课程原始课件，适合直接给 Codex 复用。
