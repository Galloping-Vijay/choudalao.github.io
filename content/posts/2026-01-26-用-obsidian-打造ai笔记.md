---
title: "用 Obsidian 打造AI笔记"
date: 2026-01-26T14:54:22+08:00
updated: 2026-02-23T16:31:07+08:00
author: "臭大佬"
categories: [AI]
description: "我在日常工作中发现，在大模型时代，**Obsidian 是本地笔记的不二之选**。特别是搭配大模型使用时，你可以随时调取本地笔记，就像随身携带了一套专属的知识库。这套体系一旦建立好，能极大地提升你的知识复用效率。"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 483
---

# 介绍

我在日常工作中发现，在大模型时代，**Obsidian 是本地笔记的不二之选**。特别是搭配大模型使用时，你可以随时调取本地笔记，就像随身携带了一套专属的知识库。这套体系一旦建立好，能极大地提升你的知识复用效率。

# 安装

访问官网下载：https://obsidian.md

我建议你花 10 分钟完成基础安装，然后再按照下面的步骤添加核心插件。

## 辅助工具

下面我介绍几个我在实践中觉得最实用的插件。这些插件虽然不是必需的，但能显著提升工作效率。

##### Editing Toolbar 插件
**作用**：辅助编辑工具栏，让常用的格式化操作一键完成。
**建议**：如果你经常手写 Markdown，这个插件能省不少时间。

#### Enhanced Publisher 插件
**作用**：支持 HTML 预览，文章写好后可以直接复制到各大内容平台发布。
**我的体验**：特别适合那些需要在多个平台同步更新的内容创作者。
** 公众号文章一键发布 **: 设置里面能配置微信公众号的 AppId 和 AppSecret，通过 Obsidian 一键发布公众号文章。

![](https://www.choudalao.com/uploads/20260126/20260126150506hZzdpa.png)

![](https://www.choudalao.com/uploads/20260126/202601261505172g8XrK.png)

####  Obsidian Local Images Plus 插件
**作用**：自动将远程图片保存到本地，防止笔记中出现失效链接。
**小贴士**：这在长期维护笔记库时非常重要。

#### Custom Frames 插件

这个插件能让你在 Obsidian 里面直接嵌入网页，把豆包、通义等 AI 「装」进了笔记软件里。这样你就不用在浏览器和编辑器之间频繁切换了。

**配置步骤**

首先，在插件市场搜索 `Custom Frames`，安装并开启。接下来，我以添加豆包为例，给你演示整个配置流程。
![](https://www.choudalao.com/uploads/20260126/20260126151300elTslX.png)

![](https://www.choudalao.com/uploads/20260126/20260126151309Ndeecz.png)
在配置对话框中，你只需要填写三个字段：

- **Display name**：这是显示在侧边栏的名称，我这里写「豆包」就行。
- **URL**：填入 `https://www.doubao.com`
- **Icon**：点击「Lucide icons」链接，选一个你喜欢的图标。

配置完成后，**一定要把 Obsidian 完全关掉，然后重新打开**，这样配置才能生效。这是一个容易被忽略但很重要的步骤。

###### 打开豆包面板

重新打开 Obsidian 后，按 Ctrl+P（Mac 用户用 Cmd+P）打开命令面板，输入「豆包」，选择「Open 豆包」。

![](https://www.choudalao.com/uploads/20260126/20260126145320Qzym8G.png)

![](https://www.choudalao.com/uploads/20260126/202601261453305UF8AS.png)

#### Claudian 插件

这是我最推荐的一个插件。它能在 Obsidian 侧边栏增加一个 AI 聊天窗口，让你随时可以问 Claude 任何问题。更强大的是，它还能读取你当前打开的笔记，提取内容或进行优化。

**前置条件**：你需要会用 Claude，并在本地安装和配置好 Claude 环境。

**安装步骤**

在 Obsidian 插件市场里搜索 `Claudian` 并安装启用。不过，这个插件还处于 Beta 阶段，所以你需要进行额外配置。

点击已安装的 Claudian 插件，找到「Beta plugin list」选项，点击「Add beta plugin」，然后输入官方仓库地址：`https://github.com/YishenTu/claudian`

![](https://www.choudalao.com/uploads/20260126/20260126145347YByy6u.png)

![](https://www.choudalao.com/uploads/20260126/202601261453534Q48Y9.png)

**关键一步**：安装完成后，**一定要完全关闭 Obsidian，然后重新打开**。这样 Claudian 插件才能正常加载，你就能在侧边栏看到新增的聊天窗口了。
![](https://www.choudalao.com/uploads/20260126/20260126151124nNkl01.png)

**使用聊天功能**

点击侧边栏的 Claudian 图标，就能看到聊天界面，开始与 Claude 对话。

![](https://www.choudalao.com/uploads/20260126/20260126145400DiGBMF.png)

---

# SKILL（高级功能）

如果你想进一步扩展 Obsidian 的功能，这部分介绍一些高级技能和工具集。

## obsidian-skills

**kepano/obsidian-skills** 是 Obsidian 创始人 Kepano 亲自维护的官方技能仓库。它遵循 Agent Skills 规范，可以被任何支持该规范的 AI Agent 使用，包括 Claude Code 和 Codex CLI。这个仓库中的 Skill 能让 Obsidian 和 AI 工具之间的协作更加高效。

##### 安装方式

如果你使用命令行工具，可以通过以下命令安装：

```bash
/plugin marketplace add kepano/obsidian-skills
```

或者直接安装指定版本：

```bash
/plugin install obsidian@obsidian-skills
```

安装完成后，你就可以在 Obsidian 中使用官方维护的各种 Skill，进一步增强 Obsidian 与 AI 工具的协作能力。