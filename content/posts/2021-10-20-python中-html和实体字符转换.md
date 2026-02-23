---
title: "Python中 html和实体字符转换"
date: 2021-10-20T17:27:47+08:00
updated: 2026-02-23T07:16:23+08:00
author: "臭大佬"
categories: [Python]
description: "Python中 html和实体字符转换"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3401
---

# 前言
在与数据库交互中，出于安全考虑，存入的数据要把标签转换成实体字符，

# 代码
```python
# encoding: utf-8
import html

# 原字符串
str = "<html><body><div>测试</div></body></html>"
# 转化为实体
esc_str = html.escape(str)
# 实体转化会标签
unesc_str = html.unescape(esc_str)
print(esc_str)    
print(unesc_str) 

# &lt;html&gt;&lt;body&gt;&lt;div&gt;测试&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;
# <html><body><div>测试</div></body></html>
```