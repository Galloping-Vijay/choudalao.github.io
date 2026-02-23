---
title: "VM25039:1 Uncaught SyntaxError: Invalid or unexpected token"
date: 2020-12-16T16:27:28+08:00
updated: 2026-02-23T05:47:59+08:00
author: "臭大佬"
categories: [前端]
description: "VM25039:1 Uncaught SyntaxError: Invalid or unexpected token"
cover: "https://www.choudalao.com/uploads/20201216/Jul6L7YHsIvkNZrt8bXvAFE9N3O7YDYGNYENKGQI.jpeg"
click: 4226
---

# 问题
使用 ` eval('(' + jsonstr + ')')`或`JSON.parse(jsonstr)` 对`json`字符串转对象时报错了。

> VM25039:1 Uncaught SyntaxError: Invalid or unexpected token

![](https://www.choudalao.com/uploads/20201216/20201216162103Ytg5QH.png)

# 解决
错误原因：`JSON.parse` 或 `eval()` 转`json`字符串时遇到一些特殊字符需要先转义，

可以用`str.replace(/\n/g,"\\\\n")`转义,`'\\'`转成单个`'\'`,`'\\n'`转成`'\n'`,最后转成`'\\n'`这样就可以用`parse`转成对象时变为`'\n'`，取出的字符串设置到`html`文本中`\n`被解析为换行。

### 栗子
```php
// goods是json字符串

var goods = '{:json_encode($info.order_goods)}';

 //goods = eval('(' + goods.replace(/\n/g,"\\\\n") + ')');
goods = JSON.parse(goods.replace(/\n/g,"\\\\n"));
console.log(goods);
```

结果不报错了。

![](https://www.choudalao.com/uploads/20201216/20201216162532LuS0Hu.png)