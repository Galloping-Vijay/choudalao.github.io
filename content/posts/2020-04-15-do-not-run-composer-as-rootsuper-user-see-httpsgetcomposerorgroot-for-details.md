---
title: "Do not run Composer as root/super user! See https://getcomposer.org/root for details"
date: 2020-04-15T10:36:33+08:00
updated: 2026-02-23T16:32:44+08:00
author: "臭大佬"
categories: [php]
description: "Do not run Composer as root/super user! See https://getcomposer.org/root for details"
cover: "https://www.choudalao.com/uploads/20200415/jdZQ7aU8Bk6SWU0Zko5ueDxxt0S8wJGVIJnevQVd.jpeg"
click: 7919
---

# 问题
Do not run Composer as root/super user! See https://getcomposer.org/root for details

意思是说：不要以root /超级用户身份运行Composer！
有关详细信息，请参见https://getcomposer.org/root
![](https://www.choudalao.com/uploads/20200415/20200415103148wU9RFc.png)

# 解决
既然超级管理员不行，那我们创建一个别的用户
```shell
useradd wjf

```
```shell
passwd wjf
```
![](https://www.choudalao.com/uploads/20200415/20200415103334F6upSu.png)

```shell
 su - wjf
```
![](https://www.choudalao.com/uploads/20200415/20200415103615lnFspx.png)

切换为root
```shell
su root
```