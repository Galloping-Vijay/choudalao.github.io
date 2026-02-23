---
title: "在 Windows 下可以安装多个 Node.js 版本"
date: 2025-04-19T11:43:29+08:00
updated: 2026-02-23T17:33:08+08:00
author: "臭大佬"
categories: [前端]
description: "在 Windows 下可以安装多个 Node.js 版本"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 1800
---

# 使用 nvm-windows 管理多个 Node.js 版本
## 安装 nvm-windows:
下载并安装 [nvm-windows](https://github.com/coreybutler/nvm-windows "nvm-windows")
安装完成后，打开命令行工具（如 PowerShell 或 CMD）。

## 列出可下载的版本号
```go
nvm list available
```

## 安装多个 Node.js 版本
使用以下命令安装不同版本的 Node.js：
```go
nvm install 14.16.0  # 安装 Node.js 14.16.0
# nvm install 14.16.0 --reinstall-packages-from=14.16.0
nvm install 18.17.1  # 安装 Node.js 18.17.1
```
查看列表
```go
nvm list
```

### 切换 Node.js 版本：
使用以下命令切换到指定版本：
```go
nvm use 18.17.1  # 切换到 Node.js 18.17.1
```
查看版本
```go
node -v
```

### 问题
###### 无法安装npm
如果下载的node包无法安装npm,可以直接去node官网:https://nodejs.org/en/about/previous-releases,下载对应的版本,解压后放在nvm的安装目录
![](https://www.choudalao.com/uploads/20250419/20250419175802BY9TpN.png)