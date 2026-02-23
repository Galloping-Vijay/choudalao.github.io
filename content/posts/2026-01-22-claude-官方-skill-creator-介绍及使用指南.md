---
title: "Claude 官方 Skill-Creator 介绍及使用指南"
date: 2026-01-22T19:58:23+08:00
updated: 2026-02-23T21:50:19+08:00
author: "臭大佬"
categories: [AI]
description: "Claude 官方 skill-creator 技能：介绍、安装与使用指南"
cover: "https://www.choudalao.com/uploads/20260122/wD0j0X4oqxroR1II0RcDnPfU2GVCUUyacDqSffek.png"
click: 1862
---

# 介绍
skill-creator 是 Anthropic 官方 example-skills 包中的核心技能，用于快速创建/更新 Claude Agent Skills，通过交互式流程生成符合规范的技能目录、SKILL.md 配置与资源结构，无需手动编写完整模板，大幅降低自定义技能的开发门槛。

---

### 一、核心功能与定位
|功能|说明|适用场景|
| ---- | ---- | ---- |
|技能初始化|自动生成技能目录、SKILL.md（含 frontmatter 与内容模板）、assets/scripts 等配套文件夹|从零创建新技能|
|交互式需求梳理|引导用户明确技能名称、描述、允许工具、使用场景，自动填充配置|新手入门技能开发|
|配置校验|检查 SKILL.md 语法、权限设置、元数据规范，规避常见错误|技能调试与合规化|
|打包与分享|生成可分发的技能包（ZIP），支持上传至 Claude 或分享给他人|技能交付与协作|

---

### 二、安装步骤（Claude Code 命令行）
1. 添加官方插件市场：
    ```bash
    /plugin marketplace add anthropics/skills
    ```
2. 安装依赖包（skill-creator 属于 example-skills 子包）：
    ```bash
    # 安装核心示例包（含 skill-creator）
    /plugin install example-skills@anthropic-agent-skills
    ```
3. 验证安装：
    - 输入 `/plugin list` 查看是否存在 example-skills 及 skill-creator
    - 重启 Claude Code 确保技能生效

---

### 三、完整使用流程（创建自定义技能）
#### 1. 启动技能创建
- 上传需求文档（可选，如功能清单、流程说明）
- 发送触发指令：
    ```plaintext
    用 skill-creator 创建一个名为「weekly-report-generator」的技能，用于自动生成周度工作汇报，要求：1. 读取周报模板（assets/template.md）；2. 调用 Read 工具提取项目数据；3. 输出 Markdown 格式汇报；4. 允许工具：Read、Glob；语言简洁专业。
    ```

#### 2. 交互式配置（skill-creator 自动引导）
- 确认技能名称、描述、允许工具（如 Read/Write/CodeExecutor）
- 定义技能核心指令与工作流程（如数据提取→模板填充→格式校验）
- 选择是否生成示例脚本/资源文件（如模板、参考文档）

#### 3. 生成与校验技能
1. 自动生成目录结构：
    ```
    ~/.claude/skills/weekly-report-generator/
    ├── SKILL.md  # 核心配置文件（含 frontmatter 与提示词）
    ├── assets/   # 存放模板、图片等资源
    └── scripts/  # 可选：辅助脚本（如数据处理代码）
    ```
2. SKILL.md 示例（自动生成）：
    ```markdown
    ---
    name: weekly-report-generator
    description: Auto-generate weekly work reports by extracting project data and filling templates. Use for regular work summary.
    allowed-tools: Read, Glob
    ---
    # 周度工作汇报生成器
    ## 核心流程
    1. 用 Glob 工具匹配周报相关文件（如 ./data/*.md）
    2. 用 Read 工具读取模板与数据文件
    3. 提取项目进展、任务完成度、待办事项
    4. 填充模板并输出 Markdown 汇报
    ## 输出要求
    - 包含：本周成果、未完成任务、下周计划
    - 语言正式，量化数据优先
    ```
3. 校验技能：发送指令让 skill-creator 检查配置合法性
    ```plaintext
    用 skill-creator 验证我刚创建的 weekly-report-generator 技能，检查 SKILL.md 语法、权限设置是否合规
    ```

#### 4. 测试与迭代
1. 启用新技能（设置→功能→技能列表，开启「weekly-report-generator」）
2. 上传测试数据，发送提示词测试效果
3. 若需修改，重新触发 skill-creator 进行更新：
    ```plaintext
    用 skill-creator 更新 weekly-report-generator 技能，添加「自动生成 PDF 附件」功能，允许工具：Write、CodeExecutor
    ```

---

### 四、关键技巧与注意事项
1. 前置准备：提前整理技能的核心流程、允许工具、输出格式，提升交互效率
2. 权限控制：在 allowed-tools 中仅添加必要工具（如 Read/Write），避免权限冗余
3. 格式规范：SKILL.md 需严格遵循 YAML frontmatter + Markdown 内容结构，frontmatter 包含 name/description/allowed-tools 等必填项
4. 版本兼容：确保安装的 example-skills 版本与 Claude Code 兼容，可通过 `/plugin update example-skills` 升级
5. 人工复核：生成后检查 SKILL.md 中的指令逻辑，确保技能行为符合预期

---

### 五、常见问题排查
|问题|排查步骤|
| ---- | ---- |
|skill-creator 未触发|1. 确认已安装 example-skills；2. 指令中明确「用 skill-creator」；3. 开启代码执行/文件创建权限|
|SKILL.md 生成失败|1. 检查需求描述是否清晰；2. 确保磁盘有写入权限；3. 重启 Claude Code 重试|
|技能调用异常|1. 用 skill-creator 校验配置；2. 检查 allowed-tools 是否包含所需工具；3. 核对技能名称与触发条件|