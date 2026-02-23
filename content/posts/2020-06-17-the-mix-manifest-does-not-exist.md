---
title: "The Mix manifest does not exist."
date: 2020-06-17T10:16:52+08:00
updated: 2026-02-23T16:40:44+08:00
author: "臭大佬"
categories: [php]
description: "The Mix manifest does not exist."
cover: "https://www.choudalao.com/uploads/20200617/TNmBxe2xtKfSUjAxgXf7zfsWfFXl6iG7bJmxMiE1.jpeg"
click: 3777
---

# 错误信息

~~ErrorException (E_ERROR)
The Mix manifest does not exist. (View: /xxxx/vendor/laravel/horizon/resources/views/layout.blade.php)
Previous exceptions~~
![](https://www.choudalao.com/uploads/20200617/20200617101507DsMEJs.png)

# 方案
```shell
php artisan vendor:publish --provider="Laravel\Horizon\HorizonServiceProvider"
```
![](https://www.choudalao.com/uploads/20200617/20200617102249pPeXI5.png)