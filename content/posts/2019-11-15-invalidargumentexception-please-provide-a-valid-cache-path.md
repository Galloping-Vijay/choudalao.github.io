---
title: "InvalidArgumentException Please provide a valid cache path"
date: 2019-11-15T16:45:53+08:00
updated: 2026-02-22T08:51:07+08:00
author: "臭大佬"
categories: [php]
description: "InvalidArgumentException：Please provide a valid cache path"
cover: "https://www.choudalao.com/uploads/20191115/SLb2LY19mAIrFcRGxJfYi7HIdrRaxlyLCllizIsR.jpeg"
click: 4760
---

InvalidArgumentException：Please provide a valid cache path

![](https://www.choudalao.com/uploads/20191115/20191115164331Ckk1Bz.png)

![](https://www.choudalao.com/uploads/20191115/20191115164359Fw8ljB.png)

这是因为laravel的缓存路径没有找到

laravel缓存文件路径是在 config/cache.php中设置，默认存在storage文件夹中

## 解决：

需要保证storage/framework下面创建 sessions， views, cache 文件夹并确保可写权限

![](https://www.choudalao.com/uploads/20191115/201911151645284Q5JHr.png)

再次访问：

![](https://www.choudalao.com/uploads/20191115/20191115164548xLLEzN.png)