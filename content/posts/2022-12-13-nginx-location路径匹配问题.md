---
title: "nginx location路径匹配问题"
date: 2022-12-13T14:58:14+08:00
updated: 2026-02-23T12:14:35+08:00
author: "臭大佬"
categories: [linux]
description: "nginx location路径匹配问题"
cover: "https://www.choudalao.com/uploads/20221213/Ofg34TeU8LVdai70E2pc6vpqWtNUyPm8idYw6hxP.png"
click: 2607
---

# 描述
现在很多前端web程序都是打包单页面程序，只能有一个入口，这样会导致刷新页面报404

![](https://www.choudalao.com/uploads/20221213/20221213145314tyHdtl.png)

其实在 nginx 中加个配置就能解决，

```go
location / {
# 其他代码
try_files $uri $uri/ /index.html;
}
```
解释:
`匹配所有“/”开头的路径到html目录下。try_files的含义是：首先会匹配$uri文件，如果没有去匹配$url/文件，如果再没有去找/index.html`

假设请求 127.0.0.1/home;
变量解释
try_files  固定语法
$uri       指代home文件(ip地址后面的路径，假如是127.0.0.1/index/a.png，那就指代index/a.png)
$uri/      指代home文件夹
/index.html  向ip/index.html 地址发起请求