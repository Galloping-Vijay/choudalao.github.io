---
title: "Argument 1 passed to Tymon\\JWTAuth\\JWTGuard::login() must be an ...."
date: 2019-11-15T15:26:22+08:00
updated: 2026-02-22T08:51:05+08:00
author: "臭大佬"
categories: [php]
description: "Argument 1 passed to Tymon\\JWTAuth\\JWTGuard::login() must be an instance of Tymon\\JWTAuth\\Contracts\\JWTSubject, instance of App\\Models\\User given, called in......"
cover: "https://www.choudalao.com/uploads/20191115/Iq2mzbd8GrmsPJytPvHISbHoR7RiBKm2lEitBZQk.jpeg"
click: 11292
---

##### 在使用jwt-auth做登录认证的时候为什么报这个错误，出现如下报错：

> Symfony\Component\Debug\Exception\FatalThrowableError: Argument 1 passed to Tymon\JWTAuth\JWTGuard::login() must be an instance of Tymon\JWTAuth\Contracts\JWTSubject, instance of App\Models\User given, called in E:\wwwroot\laravel\dev.lar.net\vendor\tymon\jwt-auth\src\JWTGuard.php on line 127 in file E:\wwwroot\laravel\dev.lar.net\vendor\tymon\jwt-auth\src\JWTGuard.php on line 140

![](https://www.choudalao.com/uploads/20191115/20191115152256tm6rsy.png)

## 解决方法：
修改User.php模型

![](https://www.choudalao.com/uploads/20191115/20191115152346CLBKfT.png)

改成

![](https://www.choudalao.com/uploads/20191115/20191115152404l1M75v.png)

```php
<?php

//...

use Tymon\JWTAuth\Contracts\JWTSubject;
use Illuminate\Notifications\Notifiable;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Support\Facades\Auth;

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
	
	//...
```