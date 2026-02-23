---
title: "Warning: chdir(): open_basedir restriction in effect. File(../) is not within the allowed path(s):"
date: 2020-04-04T21:56:15+08:00
updated: 2026-02-23T18:40:10+08:00
author: "臭大佬"
categories: [php]
description: "Warning: chdir(): open_basedir restriction in effect. File(../) is not within the allowed path(s):"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 5391
---

# 问题
在宝塔环境下报：
Warning: chdir(): open_basedir restriction in effect. File(../) is not within the allowed path(s):
![](https://www.choudalao.com/uploads/20200404/20200404215446XGeiu6.png)

# 解决
关闭防跨站攻击(open_basedir)即可！
![](https://www.choudalao.com/uploads/20200404/20200404215548bh8hYN.png)