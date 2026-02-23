---
title: "在 Gemini CLI 中使用 Gemini 3.0"
date: 2025-12-16T22:11:17+08:00
updated: 2026-02-23T20:54:09+08:00
author: "臭大佬"
categories: [AI]
description: "在 Gemini CLI 中使用 Gemini 3.0"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 604
---

# 前言
最近 `Gemini 3.0` 想当火爆,但是墙内使用存在各种阻碍,今天教大家无需魔法免费白嫖.在 `Gemini CLI`中用上`Gemini 3.0`.

# 安装 Gemini CLI

安装教程网上很多,这边简单列举通过node安装步骤,各个操作系统都大差不差.不懂的网上自行查找.


### 安装

###### 前提 : Node.js 环境（版本 18 或更高）

```go
npm install -g @google/gemini-cli
```
### 验证
```go
gemini --version
```
有显示版本号说明安装了。

## 获取KEY

在官网的 [gemini 可用区域](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-cn "gemin 可用区域") 没有我们国家,使用魔法会比较麻烦还不稳定,推荐使用中转平台体验。

平台地址: https://www.univibe.cc/console/auth?type=register&invite=6VEBOV

## 配置

注册成功后,在API秘钥页面创建并获取KEY.

![](https://www.choudalao.com/uploads/20251216/202512162201576FWTBN.png)

配置环境变量(根据各操作系统自行配置,也可借助cc-switch等工具快速配置)
```go
GOOGLE_GEMINI_BASE_URL=https://api.univibe.cc/gemini
GEMINI_API_KEY=你的KEY
```

### 启用 Gemini 3 Pro 模型

##### 启动 Gemini CLI

```go
gemini
```
##### 设置
```go
/settings
```
选项中 `Preview Features`设置为`true`,按 ESC 键退出设置

#### 切换模型
```go
/model
```
选择` 2. Pro (gemini-3-pro-preview, gemini-2.5-pro)`

![](https://www.choudalao.com/uploads/20251216/20251216221014jMX3Pi.png)