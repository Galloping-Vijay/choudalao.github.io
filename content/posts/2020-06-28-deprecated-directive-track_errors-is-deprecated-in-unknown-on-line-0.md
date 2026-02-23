---
title: "Deprecated: Directive 'track_errors' is deprecated in Unknown on line 0"
date: 2020-06-28T14:10:56+08:00
updated: 2026-02-23T16:41:31+08:00
author: "臭大佬"
categories: [php]
description: "Deprecated: Directive 'track_errors' is deprecated in Unknown on line 0"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 6577
---

# 问题
在命令行运行php命令的时候，报如下提示：
Deprecated: Directive 'track_errors' is deprecated in Unknown on line 0
![](https://www.choudalao.com/uploads/20200628/20200628140644usRWWp.png)

# 解决方法
打开`php.ini`，搜索`track_errors`，
```shell
track_errors=On
```
改成
```shell
track_errors=Off
```
![](https://www.choudalao.com/uploads/20200628/20200628140904JCXXa5.png)
然后重启nginx或者apache,重新运行：
![](https://www.choudalao.com/uploads/20200628/20200628141053V1IWti.png)