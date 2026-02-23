---
title: "pyython把html转为为makedown"
date: 2021-08-11T15:56:17+08:00
updated: 2026-02-23T14:22:51+08:00
author: "臭大佬"
categories: [Python]
description: "pyython把html转为为makedown"
cover: "https://www.choudalao.com/uploads/20210811/c8KsdIHsXnIvaExV4nolH2mKuI5K0Mmb9PMVDp5k.jpeg"
click: 3078
---

# 介绍
如果我们原来有后台管理系统，而且文章是用makedown方式添加编辑的，当我们需要爬取别的文章到我们数据库的时候，需要把html转化成makedown，不然编辑的时候是乱的。下面我们来实现一下

# 代码
```python
# coding:utf-8
import html2text as ht  # pip install html2text

text_maker = ht.HTML2Text()
text_maker.bypass_tables = False
text = text_maker.handle(content)
md = text.split("#")
print(md[0])
```