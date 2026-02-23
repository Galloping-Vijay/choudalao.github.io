---
title: "ModuleNotFoundError: No module named 'pip'"
date: 2020-05-12T23:40:54+08:00
updated: 2026-02-23T16:34:16+08:00
author: "臭大佬"
categories: [Python]
description: "ModuleNotFoundError: No module named 'pip'"
cover: "https://www.choudalao.com/uploads/20200512/dZlMvEJIKGXv123RCGj8sYGoRqiuBQTytrzXKRWs.jpeg"
click: 3364
---

# 问题
今天在安装python包的时候，发现如下报错信息：
```shell
Traceback (most recent call last):
  File "xxx", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "xxx\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "xxx\__main__.py", line 4, in <module>
ModuleNotFoundError: No module named 'pip'
```

![](https://www.choudalao.com/uploads/20200512/20200512233859kqzLD1.png)

# 解决
运行如下两行命令
```shell
python -m ensurepip
```

![](https://www.choudalao.com/uploads/20200512/20200512233920wOMPXB.png)

![](https://www.choudalao.com/uploads/20200512/20200512233933Y5e3WF.png)

```shell
 python -m pip install --upgrade pip
```

测试安装包：
![](https://www.choudalao.com/uploads/20200512/20200512234045Iuvbir.png)