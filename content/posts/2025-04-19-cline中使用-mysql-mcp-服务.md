---
title: "Cline中使用 MySql MCP 服务"
date: 2025-04-19T14:07:45+08:00
updated: 2026-02-23T16:31:11+08:00
author: "臭大佬"
categories: [AI]
description: "Cline中使用 MySql MCP 服务"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
weight: 100
click: 2767
---

# MCP (Model Context Protocol)

## 简介
MCP（Model Context Protocol，模型上下文协议）是一个革命性的开放标准，它为 AI 模型提供了与外部数据源和工具建立安全双向连接的能力。就像 USB-C 在硬件领域的普及一样，MCP 为 AI 模型提供了一个统一的标准接口，用于连接各种数据源和服务，从而实现智能化的自动工作流程。该协议由 Anthropic 公司于 2024 年底提出并开源。

通过 MCP，AI 模型能够：
- 无缝访问本地文件系统
- 直接操作数据库
- 调用远程在线服务
- 实现更复杂的自动化任务

## 相关资源

### 官方文档
- MCP 官方文档：https://modelcontextprotocol.io/introduction

### 开源生态
- MCP 客户端列表：
  - https://glama.ai/mcp/clients
  - https://github.com/punkpeye/awesome-mcp-clients

- MCP 服务端资源：
  - https://glama.ai/mcp/servers
  - https://github.com/punkpeye/awesome-mcp-servers
  - https://github.com/modelcontextprotocol/servers
  - https://www.pulsemcp.com/servers

## MySQL MCP 服务配置指南

### 1. 环境搭建

#### 1.1 克隆服务端代码
```bash
git clone https://github.com/dpflucas/mysql-mcp-server.git
```
```go
cd mysql-mcp-server
```
#### 1.2 安装依赖并构建
```go
npm install
```
```go
npm run build
```
详细配置说明请参考： https://github.com/dpflucas/mysql-mcp-server

### 2. 配置步骤 
#### 2.1 模型配置
在配置文件中填入您的模型 API 密钥：
![](https://www.choudalao.com/uploads/20250419/20250419135219yXT341.png)

#### 2.2 VSCode Cline 插件配置
1. 在 VSCode 中安装 Cline 插件
2. 打开 Cline 界面
3. 点击右上角的 MCP Server 图标
4. 选择 Installed 标签
5. 点击 Configure MCP Servers
6. 复制 mcp-settings-example.json 内容并根据实际情况修改参数
7. 保存配置后，MCP 服务将自动启动
配置界面示例：

![](https://www.choudalao.com/uploads/20250419/202504191347046b8pnC.png)

![](https://www.choudalao.com/uploads/20250419/20250419134752N1zSkj.png)

#### 2.3 聊天界面配置
![](https://www.choudalao.com/uploads/20250419/20250419134951SR3U0O.png)

### 3.使用示例
示例查询：获取 users 表的所有数据

![](https://www.choudalao.com/uploads/20250419/20250419135116Ucuv0s.png)


# 参考资料
https://mp.weixin.qq.com/s/OGJYOAdixC8q_NSNY_djRw
https://blog.csdn.net/raoxiaoya/article/details/147254577