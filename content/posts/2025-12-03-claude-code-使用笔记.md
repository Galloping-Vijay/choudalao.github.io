---
title: "Claude Code 使用笔记"
date: 2025-12-03T10:24:08+08:00
updated: 2026-02-23T21:50:32+08:00
author: "臭大佬"
categories: [AI]
description: "Claude Code 使用笔记"
cover: "https://www.choudalao.com/uploads/20251203/V0YEuGCuSTtoPUz8EunJ4MgjROXbR94lKwXRR3yy.png"
click: 810
---

# 使用
安装就不用说了,可以去官网看相应文档:https://code.claude.com/docs/zh-CN/overview

`claude`会不定期更新,第一时间获取最新功能.
```bash
npm update -g @anthropic-ai/claude-code
```

值得注意的是:开始使用 Claude Code 时，你会发现每执行一个操作都需要确认权限，频繁的授权提示会严重影响工作流畅度。可以启动时使用"危险模式"
```bash
claude --dangerously-skip-permissions
```

## 设置厂商key和url

大模型厂商也Claude Code 进行了积极适配，最重要的是配置环境变量，记住这几个参数的配置,以WIN为例:

### 方法一

##### 设置厂商key和url
```bash
setx ANTHROPIC_AUTH_TOKEN your_zhipu_api_key
setx ANTHROPIC_BASE_URL https://dashscope.aliyuncs.com/apps/anthropic
setx CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC 1
# 设置git-bash 才能运行MCP命令
setx CLAUDE_CODE_GIT_BASH_PATH "D:\Program Files\Git\bin\bash.exe"
```

##### 切换模型
查看模型
```bash
/model
```
切换模型
```bash
/model qwen3-coder-plus
```
在配置文件中永久设置：在项目根目录创建.claude/settings.json文件中，并写入模型配置信息
```bash
{
  "env": {
    "ANTHROPIC_MODEL": "qwen3-max",
    "ANTHROPIC_SMALL_FAST_MODEL": "qwen3-vl-flash"
  }
}
```

### 方法二
#### 使用 cc-switch
安装地址: https://github.com/farion1231/cc-switch/releases
安装下载就可以使用了,使用时,如果用方法一配置了环境变量,这里在cc-switch中会提示是否删除,建议删除,全都交给cc-switch来处理.

处理配置厂商外,cc-switch还能管理MCP、Skills等等。

#### CCometixLine
基于 Rust 的高性能 Claude Code 状态栏工具，集成 Git 信息、使用量跟踪、交互式 TUI 配置和 Claude Code 补丁工具。
项目地址: [CCometixLine](https://github.com/Haleclipse/CCometixLine/blob/master/README.zh.md "CCometixLine")

##### 安装:
```go
npm install -g @cometix/ccline
```
##### 添加到 Claude Code settings.json
Windows:
```bash
{
  "statusLine": {
    "type": "command", 
    "command": "%USERPROFILE%\\.claude\\ccline\\ccline.exe",
    "padding": 0
  }
}
```

## 接入MCP

```bash
# mysql https://github.com/executeautomation/mcp-database-server
npm install -g @executeautomation/database-server

claude mcp add-json your_mcp_name "{\"type\":\"stdio\",\"command\":\"npx\",\"args\":[\"-y\",\"@executeautomation/database-server\",\"--mysql\",\"--host\",\"your_server_ip\",\"--database\",\"your_database_name\",\"--user\",\"your_username\",\"--password\",\"your_password\"],\"env\":{}}"


# Figma
claude mcp add --transport http figma-dev-mode-mcp-server http://127.0.0.1:3845/mcp

# 读文档  https://context7.com/dashboard
claude mcp add --transport http context7 https://mcp.context7.com/mcp \
  --header "CONTEXT7_API_KEY: YOUR_API_KEY"  --scope user

# 浏览器控制 playwright   https://github.com/microsoft/playwright-mcp
claude mcp add playwright npx @playwright/mcp@latest

# chrome-devtools  https://github.com/ChromeDevTools/chrome-devtools-mcp/
# 打开 http://dev.localhost.net
claude mcp add chrome-devtools npx chrome-devtools-mcp@latest --scope user
```

## 工具
### 插件

Claude Code 在Vscode和JetBrains中有对应插件,使用插件会比较友好.

Chat for Claude Code 是一个Vscode插件,提供了输入框、mcp、model等配置，还能添加图片等功能.


### 随时随地用手机继续你的AI编程对话

happy-coder：Claude 代码 & Codex 的移动端和网页客户端
地址：https://github.com/slopus/happy

第一步：手机端去应用市场搜索“happy Codex”(墙外)

第二步：pc端安装

```bash
npm i -g happy-coder
```
后会出现一个二维码，直接打开手机haapy应用扫描这个二维码就建立起链接了。
如果没有二维码，输入下面的命令：
```bash
happy auth login --force
```
接下来第三步：进入你的项目目录，

 将之前是claude的命令替换成："happy"