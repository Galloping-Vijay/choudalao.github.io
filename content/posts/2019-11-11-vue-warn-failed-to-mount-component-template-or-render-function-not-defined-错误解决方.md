---
title: "[Vue warn]: Failed to mount component: template or render function not defined. 错误解决方法"
date: 2019-11-11T15:49:52+08:00
updated: 2026-02-23T05:16:14+08:00
author: "臭大佬"
categories: [前端]
description: "[Vue warn]: Failed to mount component: template or render function not defined. 错误解决方法"
cover: "https://www.choudalao.com/uploads/20191111/jNkAA3ih1CgouJlkbVCSW32rW2cD2mKQ6MCo0qVu.jpeg"
click: 9340
---

### [Vue warn]: Failed to mount component: template or render function not defined. 错误解决方法
![](https://www.choudalao.com/uploads/20191111/20191111154141MpGbez.png)

### 分析
原因是 ES6 中导入default模块需要使用 require default 不再兼容 require 自动导入default模块

`Vue.component('xxx',require( 'xxxx' ))`

修改成
`Vue.component('xxx',require( 'xxxx' ).default)`

如:

![](https://www.choudalao.com/uploads/20191111/20191111160418ouhrGG.png)

可能还存在问题,先记录一下,后期发现再追加.