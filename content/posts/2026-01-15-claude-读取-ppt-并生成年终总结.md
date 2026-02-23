---
title: "Claude 读取 PPT 并生成年终总结"
date: 2026-01-15T10:18:23+08:00
updated: 2026-02-23T22:03:46+08:00
author: "臭大佬"
categories: [AI]
description: "Claude 利用 PPT 生成年终总结技能推荐（含安装与使用指南）"
cover: "https://www.choudalao.com/uploads/20260115/kUlmGY6PywfdIdGux1ybF5QgG7Qf8nFk1by2DT3f.png"
click: 360
---

选用官方 document-skills（含 pptx 模块），这是 Claude 读取 PPT 并生成年终总结的核心技能；搭配辅助技能可进一步提升效率。以下是具体的技能推荐、安装步骤、使用方法及关键技巧：

一、核心技能推荐

1. document-skills（必装）：Anthropic 官方技能包，核心亮点是内置 pptx 模块，支持完整的 PPT 内容提取（含文本、表格、备注、母版信息），同时具备 HTML 转 PPT、批量编辑等功能，是实现“读取 PPT 生成年终总结”的核心依赖。

2. theme-factory（辅助）：专注于统一 PPT 样式，在生成年终总结的同时，可借助该技能快速套用规范风格，让导出的总结配套 PPT 更整洁、专业。

3. example-skills（可选）：包含各类 PPT 处理的实操示例，适合新手参考学习，快速掌握核心技能的使用逻辑。

二、安装步骤（Claude Code 指令）

1. 添加官方插件市场：在对话窗口输入指令 /plugin marketplace add anthropics/skills，按下回车执行。

2. 安装核心技能包：输入指令 /plugin install document-skills@anthropic-agent-skills，按下回车执行。

3. （可选）安装辅助技能包：分别输入以下两条指令并回车，按需安装：
        

  - /plugin install theme-factory

  - /plugin install example-skills

三、读取 PPT 生成年终总结：提示词模板

1. 发送提示词（直接复制使用，可按需微调）：
        用 document-skills 的 pptx 模块读取我的 PPT，提取核心成果、数据亮点、项目进展、待改进点，生成一份结构清晰的年终总结。总结需包含以下 4 个部分：1. 年度核心成果（需体现量化数据）；2. 重点项目复盘；3. 现存问题；4. 明年规划。语言要求正式简洁，最后同步生成 1 份总结 PPT（使用 theme-factory 套用商务简约风格）。

四、关键使用技巧

1. 素材准备：确保 PPT 中包含明确的数据、项目名称、成果描述等关键信息，能显著提升内容提取的精准度。

2. 格式指定：可在提示词中补充“输出格式为 Word 文档/Markdown”，让生成的总结更适配后续编辑需求。

3. 误差核对：总结生成后，务必人工核对核心数据与关键信息，避免因 PPT 内容模糊或提取偏差导致错误。