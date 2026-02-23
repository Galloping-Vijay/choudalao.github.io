---
title: "xshell的vim小键盘不能用"
date: 2020-01-05T13:25:39+08:00
updated: 2026-02-23T15:40:05+08:00
author: "臭大佬"
categories: [linux]
description: "xshell的vim小键盘不能用"
cover: "https://www.choudalao.com/uploads/20200105/bFAUZzQQ267inWnVtbxSO4LhC8LKZOi2vw5M6Sp4.jpeg"
click: 3673
---

#起因
在用vim（或vi）编辑文件的时，使用小键盘数字键的时候，可能会输入一堆字母和换行，并不是数字。像这样
![](https://www.choudalao.com/uploads/20200105/20200105131934Dk9why.png)

# 解决方法

文件->打开->选择会话->点击属性：
![](https://www.choudalao.com/uploads/20200105/20200105132233mucoE0.png)

选择终端->VT模式->初始数字键盘模式->设置为普通
![](https://www.choudalao.com/uploads/20200105/20200105132356ha66om.png)

# 效果
已经可以完美使用小键盘了
![](https://www.choudalao.com/uploads/20200105/20200105132533C7yPif.png)