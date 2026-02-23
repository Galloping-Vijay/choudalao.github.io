---
title: "xxx be unexportedgo-lint"
date: 2020-11-06T00:07:13+08:00
updated: 2026-02-23T17:29:42+08:00
author: "臭大佬"
categories: [Go]
description: "xxx be unexportedgo-lint"
cover: "https://www.choudalao.com/uploads/20201105/hpJltRxwUR0438WjhUjH5JvBBOPdzxDt9uMJKK3K.jpeg"
click: 3543
---

# 问题
在用 `vscode` 写 `go` 代码的时候，总是有波浪线存在，如下图：

![](https://www.choudalao.com/uploads/20201105/20201105235334RJDqjA.png)

# 解决
如截图，有三处会触发`go-lint`的警告，分别是结构体上、方法上、下划线变量上

1： 结构体的上一行，编写结构体注释，而且一定要用这个结构体名称开头，如下:
![](https://www.choudalao.com/uploads/20201106/20201106000020ky6qiq.png)

2：方法上最好不要用`self`、`this`等词，然后编写函数注释文件，而且一定要用这个函数名称开头，

![](https://www.choudalao.com/uploads/20201106/20201106000341spQOmf.png)

3：不要在`go`中使用下划线命名，`current_url`改为`currentUrl`，

![](https://www.choudalao.com/uploads/20201106/20201106000710WMJ884.png)

# 另外

如果有爆红波浪线的状况，可以在settings.json文件中添加如下：
```shell
"window.zoomLevel": 0,
"go.docsTool": "gogetdoc",
"go.formatTool": "goimports",
"explorer.confirmDelete": false,
"go.lintFlags": ["--disable=varcheck", "--enable=errcheck"],
```