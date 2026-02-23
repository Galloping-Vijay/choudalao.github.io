---
title: "sudo: source: command not found"
date: 2022-10-07T09:57:46+08:00
updated: 2026-02-23T04:27:17+08:00
author: "臭大佬"
categories: [linux]
description: "sudo: source: command not found"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3448
---

# 分析
source 命令用于执行被修改的配置文件，使最新配置更新到操作系统
通常有如下命令
```go
source ~/.profile
source ~/.bash_profile
source /etc/profile
```
# 解决
```go
vim ~/.bash_profile
```
在`.bash_profile`文件里面输入
```go
export PATH=/usr/bin:/usr/sbin:/bin:/sbin:/usr/X11R6/bin
```