---
title: "AttributeError: module 'pymysql' has no attribute 'escape_string'"
date: 2021-03-30T00:01:00+08:00
updated: 2026-02-23T07:21:12+08:00
author: "臭大佬"
categories: [Python]
description: "AttributeError: module 'pymysql' has no attribute 'escape_string'"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 9242
---

# 问题

>  AttributeError: module 'pymysql' has no attribute 'escape_string'

### 代码
```php
# coding:utf-8
import pymysql

# ....
s = r'sss'
ss =  pymysql.escape_string(s)

```

# 解决
```php
# coding:utf-8
import pymysql
from pymysql.converters import escape_string


# ....
s = r'sss'
ss =  escape_string(s)
```