---
title: "dial tcp 34.64.4.113:443: connectex: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond."
date: 2020-07-27T15:57:47+08:00
updated: 2026-02-23T16:50:50+08:00
author: "臭大佬"
categories: [Go]
description: "dial tcp 34.64.4.113:443: connectex: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond."
cover: "https://www.choudalao.com/uploads/20200727/bU2p5ERAdvYDxEuQXJwJ9eQIsUEVORbo4pbiPAR2.jpeg"
click: 11494
---

# 问题

在拉取 go 第三方扩展包的时候报如下错误：

>  dial tcp 34.64.4.113:443: connectex: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.

![](https://www.choudalao.com/uploads/20200727/20200727155018uNIdDv.png)


# 分析
查看 GOSUMDB 的配置
```go
 go env
```
![](https://www.choudalao.com/uploads/20200727/20200727155555otuFMn.png)

最后是因为set GOSUMDB=sum.golang.org

把它关掉

```go
go env -w GOSUMDB=off
```

代理推荐

```go
go env -w GOPROXY=https://goproxy.cn,direct
```
这样，就不用翻墙了，
再次拉取
![](https://www.choudalao.com/uploads/20200727/20200727155743RoburJ.png)