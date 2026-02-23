---
title: "RROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.5/dist-packages/pymongo-3.10.0.dist-info'"
date: 2019-12-20T12:46:14+08:00
updated: 2026-02-23T05:12:30+08:00
author: "臭大佬"
categories: [Python]
description: "ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.5/dist-packages/pymongo-3.10.0.dist-info'
Consider using the `--user` option or check the permissions."
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4801
---

# pip在安装包的时候提示:

如
```shell
pip install pymongo

```

![](https://www.choudalao.com/uploads/20191220/20191220124120xxTqyW.png)


> ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.5/dist-packages/pymongo-3.10.0.dist-info'
Consider using the `--user` option or check the permissions.

#解决方案

```shell
pip install pymongo --user
```

不知道为什么,先做个笔记.

![](https://www.choudalao.com/uploads/20191220/20191220124156oVlFjW.png)