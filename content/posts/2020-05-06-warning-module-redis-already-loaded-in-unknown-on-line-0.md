---
title: "Warning: Module 'redis' already loaded in Unknown on line 0"
date: 2020-05-06T11:06:16+08:00
updated: 2026-02-23T16:26:05+08:00
author: "臭大佬"
categories: [php]
description: "Warning: Module 'redis' already loaded in Unknown on line 0"
cover: "https://www.choudalao.com/uploads/20200506/GC30QiGI6q4Q4PAG2EXQnoyEPb2z1Vao3CtZR9dQ.jpeg"
click: 5506
---

# 问题
Warning: Module 'redis' already loaded in Unknown on line 0

# 分析
php加载模块有两种方式，一种是通过php.ini 加载模块，另一种是通过编译时的参数加载模块。

# 解决

这里，报错信息提示已经加载过，我尝试将php.ini 文件中的相关extensions注释掉
![](https://www.choudalao.com/uploads/20200506/20200506110542mPT2zk.png)
![](https://www.choudalao.com/uploads/20200506/20200506110552PIjzaI.png)