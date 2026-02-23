---
title: "composer报错proc_open(): fork failed - Cannot allocate memory"
date: 2020-03-04T20:49:22+08:00
updated: 2026-02-23T15:52:31+08:00
author: "臭大佬"
categories: [php]
description: "composer报错proc_open(): fork failed - Cannot allocate memory"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3576
---

# 问题
在linux服务器使用composer部署yii项目时，出现“proc_open(): fork failed - Cannot allocate memory”
![](https://www.choudalao.com/uploads/20200304/202003042047415MZwez.png)

# 解决方法

先运行 free -m 看下空间是多少
在命令行环境依次运行以下三条命令
```shell
dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
mkswap /var/swap.1
swapon /var/swap.1
```
![](https://www.choudalao.com/uploads/20200304/20200304204909APWHu9.png)

![](https://www.choudalao.com/uploads/20200304/20200304204919nRlItB.png)