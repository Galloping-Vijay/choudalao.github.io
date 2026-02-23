---
title: "[Composer\\Downloader\\TransportException]   The \"https://mirrors.aliyun.com/composer/p/illuminate/routing%240a2e3fa   144abf87e1be17bad358021a26920b57b15cd8461db18f0ad3165ece4.json\" file co   uld not be downloaded (HTTP/1.1 404 Not Found)"
date: 2020-06-02T23:47:31+08:00
updated: 2026-02-23T19:34:36+08:00
author: "臭大佬"
categories: [php]
description: "[Composer\\Downloader\\TransportException]
  The \"https://mirrors.aliyun.com/composer/p/illuminate/routing%240a2e3fa
  144abf87e1be17bad358021a26920b57b15cd8461db18f0ad3165ece4.json\" file co
  uld not be downloaded (HTTP/1.1 404 Not Found)"
cover: "https://www.choudalao.com/uploads/20200602/F5l0Ij3ojtnoPKfFuZL29umaieeFbnqYtKHxEZ0R.jpeg"
click: 6488
---

# 问题

今天准备把博客的laravel升级一下，原来是5.8版本的，现在都更新到7.x了，得与时俱进呀，哈哈哈，但是，在执行 `composer update` 报如下错误，

```php
 [Composer\Downloader\TransportException]
  The "https://mirrors.aliyun.com/composer/p/illuminate/routing%240a2e3fa
  144abf87e1be17bad358021a26920b57b15cd8461db18f0ad3165ece4.json" file co
  uld not be downloaded (HTTP/1.1 404 Not Found)
```
![](https://www.choudalao.com/uploads/20200602/202006022341287AGxgL.png)

# 分析
原因是方法禁止了https的请求，需要换成http请求。

# 解决
### 方式一
在终端输入如下命令
```php
composer config secure-http false
```
这是通过命令行去修改composer.json文件，

### 方式二
可以直接在composer.json文件中的‘config’项中加上如下代码：
```php
"config" : {  
		// ....
        "vendor-dir" : "packages",
        "secure-http": false  
}
```
### 方式三
可以全局配置，推荐使用这种方式，配置方式如下：
```php
composer config -l -g
```
```php
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```
```php
composer config -g --unset repos.packagist
```