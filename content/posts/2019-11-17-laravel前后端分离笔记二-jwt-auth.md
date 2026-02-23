---
title: "laravel前后端分离笔记二 -- jwt-auth"
date: 2019-11-17T14:44:40+08:00
updated: 2026-02-23T11:39:02+08:00
author: "臭大佬"
categories: [php]
description: "JWT 全称 JSON Web Tokens ，是一种规范化的 token。可以理解为对 token 这一技术提出一套规范，是在 RFC 7519 中提出的。"
cover: "https://www.choudalao.com/uploads/20191117/xuFvk6JbPbmzfGjkbbuGkp3HVq7no4rd745PuXo6.jpeg"
click: 3444
---

jwt-auth 的详细介绍分析可以看 JWT 超详细分析这篇文章，具体使用可以看 [JWT 完整使用详解](https://learnku.com/articles/17883 "JWT 完整使用详解") 这篇文章。

# 安装

## composer拉取
&nbsp;
```php
composer require tymon/jwt-auth 1.0.0-rc.3
```
## 发布配置文件

```php
php artisan vendor:publish --provider="Tymon\JWTAuth\Providers\LaravelServiceProvider"
```
此命令会在 config 目录下生成一个 jwt.php 配置文件，你可以在此进行自定义配置。

## 生成密钥

```php
php artisan jwt:secret
```
此命令会在你的 .env 文件中新增一行 JWT_SECRET=secret。以此来作为加密时使用的秘钥。

## 配置 Auth guard
打开 config 目录下的 auth.php 文件，修改为下面代码

```php
'guards' => [
        'web' => [
            'driver' => 'session',
            'provider' => 'users',
        ],

        'api' => [
            'driver' => 'jwt',
            'provider' => 'users',
        ],
    ],
```

![](https://www.choudalao.com/uploads/20191117/20191117144214b9wqLt.png)
这样，我们就能让 api 的用户认证变成使用 jwt。

## 更改 Model
如果需要使用 jwt-auth 作为用户认证，我们需要对我们的 User 模型进行一点小小的改变，实现一个接口，变更后的 User 模型如下：
```php
<?php

namespace App\Models;
//这里从App改成了App\Models

use Illuminate\Notifications\Notifiable;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Tymon\JWTAuth\Contracts\JWTSubject;

class User extends Authenticatable implements JWTSubject
{
    use Notifiable;

    public function getJWTIdentifier()
    {
        return $this->getKey();
    }

    public function getJWTCustomClaims()
    {
        return [];
    }
	//.....
```

编写相应路由进行测试就可以。