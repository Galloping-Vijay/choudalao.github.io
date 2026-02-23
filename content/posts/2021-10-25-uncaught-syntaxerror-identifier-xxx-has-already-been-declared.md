---
title: "Uncaught SyntaxError: Identifier 'xxx' has already been declared"
date: 2021-10-25T15:30:37+08:00
updated: 2026-02-22T22:00:31+08:00
author: "臭大佬"
categories: [前端]
description: "Uncaught SyntaxError: Identifier 'xxx' has already been declared"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 8240
---

# 问题描述
js报"Uncaught SyntaxError: Identifier 'xxx' has already been declared",

![](https://www.choudalao.com/uploads/20211025/20211025152633Ippl8M.png)

可能是引用库渲染时间较长，网络不好，又没有缓存的情况下，我自己在后面定义的函数会过好久才被渲染，导致出现函数未定义的报错。

# 解决
我遇到问题是在使用jq的场景下，所以只需要把js代码都包在` document ready 函数`中，

```php
$(document).ready(function(){
 
   // 开始写 jQuery 代码...
 
});
```
这样就不会报错了。