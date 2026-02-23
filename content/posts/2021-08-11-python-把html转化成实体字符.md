---
title: "python 把html转化成实体字符"
date: 2021-08-11T15:51:52+08:00
updated: 2026-02-23T14:43:50+08:00
author: "臭大佬"
categories: [Python]
description: "python 把html转化成实体字符"
cover: "https://www.choudalao.com/uploads/20210811/zeCoiHBiXOa00ZOnL2SN8Sb0qiMO3q2QR8HpUZ6Y.jpeg"
click: 3079
---

# 介绍
为了防止客户端注入攻击，在写入数据库的时候，最好把存在攻击可能的内容转义，所以，我们在写入数据库的时候很有必要把html转义成实体字符，下面介绍一下python3怎么实现

# 代码
```python
# coding:utf-8
import html

# 要转义的html内容 
content = "<div>这是html</div>"
# 替换
content = content.replace("&", "&amp;")
# html代码转义成实体字符
content = html.escape(content)
print(content)
```