---
title: "fatal: could not read Username for 'https://gitee.com': No such device or address"
date: 2020-04-30T09:55:34+08:00
updated: 2026-02-23T16:24:22+08:00
author: "臭大佬"
categories: [其他]
description: "fatal: could not read Username for 'https://gitee.com': No such device or address"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 17904
---

# 问题
```shell
fatal: could not read Username for 'https://gitee.com': No such device or address
```

这是因为git config文件中没有用户身份信息。

# 解决方法
在请求串中加入身份信息即可：
格式
```php
https://[username]:[password]@gitee.com/[username]/project.git
```
操作如下：
```shell
cd .git
vim config
url=https://choudalao:12345@gitee.com/choudalao/test.git
```
*注
choudalao：gitee账号
12345：密码
test：项目名*

![](https://www.choudalao.com/uploads/20200430/20200430095527666ke1.png)