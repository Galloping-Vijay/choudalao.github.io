---
title: "ll: command not found"
date: 2022-07-20T09:12:04+08:00
updated: 2026-02-23T04:32:31+08:00
author: "臭大佬"
categories: [linux]
description: "ll: command not found"
cover: "https://www.choudalao.com/uploads/20220720/BtgR7UPiqhfovIKfkxDQW2PPmuJrybjJxBvHLtM1.jpeg"
click: 3315
---

# 问题
在`wsl`下，使用`ll`提示 `ll: command not found`,

网上的解决方法是编辑`/etc/profile`文件，但是`vim`方向键失效了。


### 解决`vim`方向键失效

```go
export TERM=sun-color
```
### 解决`ll: command not found`
```go
 vim /etc/profile
```
在末尾加上`alias ll='ls -l'`
```
alias ll='ls -l'
```

![](https://www.choudalao.com/uploads/20220720/20220720091132bJDweh.png)

重新加载profle文件
```go
source /etc/profile
```

### -bash: telnet: command not found
centos、ubuntu安装telnet命令的方法.
```go
yum list telnet*              列出telnet相关的安装包
yum install telnet-server          安装telnet服务
yum install telnet.*           安装telnet客户端
```