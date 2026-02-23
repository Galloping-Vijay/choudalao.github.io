---
title: "raise ImportError(msg) from None ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd."
date: 2020-03-29T10:56:13+08:00
updated: 2026-02-23T16:08:41+08:00
author: "臭大佬"
categories: [Python]
description: "raise ImportError(msg) from None
ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd."
cover: "https://www.choudalao.com/uploads/20200329/mrTtUpNkB2pGyn8IIboYUX3iacvHtefGPIx9Pgzz.jpeg"
click: 12201
---

#问题
在使用 pandas打印折线图的时候，报如下错误
`raise ImportError(msg) from None
ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.`
![](https://www.choudalao.com/uploads/20200329/20200329105435KXXHu5.png)

# 解决
按照提示，安装xlrd，
```python
pip install xlrd
```
![](https://www.choudalao.com/uploads/20200329/20200329105552p2phSD.png)
![](https://www.choudalao.com/uploads/20200329/202003291056090IRDHN.png)