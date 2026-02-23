---
title: "cURL请求中CURLOPT_POSTFIELDS只支持一维数组"
date: 2022-01-11T20:20:35+08:00
updated: 2026-02-23T12:17:20+08:00
author: "臭大佬"
categories: [php]
description: "cURL请求中CURLOPT_POSTFIELDS只支持一维数组"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4227
---

# POST参数

使用 `CURL` 并且参数为数据时，向服务器提交数据的时候，`HTTP`头会发送`Content_type: application/x-www-form-urlencoded`。这个是正常的网页`<form>`提交表单时，浏览器发送的头部。而 `multipart/form-data` 我们知道这是用于上传文件的表单。包括了 `boundary` 分界符，会多出很多字节。

使用数组提供`post`数据时,默认把`content_type`设为了`multipart/form-data`,虽然对于大多数`web`服务器并没有影响,但是还是有少部分服务器不兼容.

需要注意的是`CURLOPT_POSTFIELDS`参数只支持一维数组参数，否则会出错,可以用下面代码判断是几维数组：
```php
if (count($param) == count($param, 1)) {
	echo '一维数组';
} else {
	echo '多维数组';
}
```

当提交的post为多维数组时，应该使用
```php
CURLOPT_POSTFIELDS =>json_encode($param, JSON_UNESCAPED_SLASHES)
```
当提交的参数为一维数组时，如下：
```php
CURLOPT_POSTFIELDS =>http_build_query($param)
```