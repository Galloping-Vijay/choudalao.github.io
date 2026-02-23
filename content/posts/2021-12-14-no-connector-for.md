---
title: "No connector for []"
date: 2021-12-14T13:09:51+08:00
updated: 2026-02-23T02:44:57+08:00
author: "臭大佬"
categories: [php]
description: "No connector for []"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3273
---

# 问题

laravel队列报错

~~No connector for []~~

# 解决
这是配置文件写错了，QUEUE_CONNECTION的值没有找到对应的配置。配置改成正确的就可以了。
```php
QUEUE_CONNECTION=redis
```