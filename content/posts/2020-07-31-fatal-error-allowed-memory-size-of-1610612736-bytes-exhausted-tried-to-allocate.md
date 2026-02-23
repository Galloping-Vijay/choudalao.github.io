---
title: "Fatal error: Allowed memory size of 1610612736 bytes exhausted (tried to allocate 134217736 bytes)"
date: 2020-07-31T10:11:10+08:00
updated: 2026-02-23T16:52:20+08:00
author: "臭大佬"
categories: [php]
description: "Fatal error: Allowed memory size of 1610612736 bytes exhausted (tried to allocate 134217736 bytes) in phar://C:/ProgramData/ComposerSetup/bin/composer.phar/src/Composer/Dep
endencyResolver/RuleSet.php on line 84"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3143
---

# 问题

WIN10 下拉取 composer 时报如下错误。
> Fatal error: Allowed memory size of 1610612736 bytes exhausted (tried to allocate 134217736 bytes) in phar://xxx/bin/composer.phar/src/Composer/Dep
endencyResolver/RuleSet.php on line 84

![](https://www.choudalao.com/uploads/20200731/20200731095301lzsVNr.png)

# 分析

原因是内存不够，打开 php.ini 配置文件，搜索 memory_limit 配置项，修改如下

```php
memory_limit=-1
```
![](https://www.choudalao.com/uploads/20200731/20200731095632RUmY0D.png)