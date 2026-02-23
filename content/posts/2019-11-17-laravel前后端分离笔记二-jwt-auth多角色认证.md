---
title: "laravel前后端分离笔记二 -- jwt-auth多角色认证"
date: 2019-11-17T22:14:45+08:00
updated: 2026-02-23T19:06:44+08:00
author: "臭大佬"
categories: [php]
description: "jwt-auth多角色认证"
cover: "https://www.choudalao.com/uploads/20191117/d34KIakqBE2kBJmp55UtKlGsml1egAFLVwnfXotz.jpeg"
click: 5449
---

前台用户功能我们已经基本完成，下面按照前台，搭建后台管理admin相应的功能。

# 数据迁移
里面的字段我们按照users的
```shell
php artisan make:migration create_admins_table
```
填充字段
```php
  */
    public function up()
    {
        Schema::create('admins', function (Blueprint $table) {
            $table->bigIncrements('id')->comment('用户表');
            $table->string('name')->comment('用户昵称');
            $table->text('last_token')->comment('登陆时的token');
            $table->tinyInteger('status')->default('0')->comment('用户状态 -1代表已删除 0代表正常 1代表冻结');
            $table->string('email',150)->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
        });
    }
```
![](https://www.choudalao.com/uploads/20191117/20191117213200DRiK23.png)

运行迁移
```php
php artisan migrate
```
# 数据填充
填充一些数据到admins表
```php
php artisan make:seeder AdminsTableSeeder
```
插入数据
![](https://www.choudalao.com/uploads/20191117/20191117213412ibfgMe.png)
```php
php artisan db:seed --class=AdminsTableSeeder
```

# Admin相关文件
根据users相关配套，我们把相应的文件也复制一份，相应的命名和模型需要修改，后期用到再说明。

# admin认证
`config/auth.php`修改配置
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
        'admin' => [
            'driver' => 'jwt',
            'provider' => 'admins',
        ],
    ],
//....

    'providers' => [
        'users' => [
            'driver' => 'eloquent',
            'model' => App\Models\User::class,
        ],
        'admins' => [
            'driver' => 'eloquent',
            'model' => App\Models\Admin::class,
        ],

        // 'users' => [
        //     'driver' => 'database',
        //     'table' => 'users',
        // ],
    ],
```
![](https://www.choudalao.com/uploads/20191117/20191117214155W6Gegl.png)
![](https://www.choudalao.com/uploads/20191117/20191117214206LmtQgy.png)
当 Auth::guard('admin') 时，就会自动查找 Admin 模型文件。

# 刷新用户认证中间件
刷新token,文件地址 `app/Http/Middleware/Api/RefreshAdminTokenMiddleware.php`
```php
<?php

namespace App\Http\Middleware\Api;

use Illuminate\Support\Facades\Auth;
use Closure;
use Tymon\JWTAuth\Exceptions\JWTException;
use Tymon\JWTAuth\Http\Middleware\BaseMiddleware;
use Tymon\JWTAuth\Exceptions\TokenInvalidException;
use Tymon\JWTAuth\Exceptions\TokenExpiredException;
use Symfony\Component\HttpKernel\Exception\UnauthorizedHttpException;

class RefreshAdminTokenMiddleware extends BaseMiddleware
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request $request
     * @param  \Closure $next
     *
     * @throws \Symfony\Component\HttpKernel\Exception\UnauthorizedHttpException
     *
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        // 检查此次请求中是否带有 token，如果没有则抛出异常。
        $this->checkForToken($request);

        //1. 格式通过，验证是否是专属于这个的token

        //获取当前守护的名称
        $present_guard = Auth::getDefaultDriver();

        //获取当前token
        $token=Auth::getToken();

        //即使过期了，也能获取到token里的 载荷 信息。
        $payload = Auth::manager()->getJWTProvider()->decode($token->get());

        //如果不包含guard字段或者guard所对应的值与当前的guard守护值不相同
        //证明是不属于当前guard守护的token
        if(empty($payload['guard'])||$payload['guard']!=$present_guard){
            throw new TokenInvalidException();
        }
        //使用 try 包裹，以捕捉 token 过期所抛出的 TokenExpiredException  异常
        //2. 此时进入的都是属于当前guard守护的token
        try {
            // 检测用户的登录状态，如果正常则通过
            if ($this->auth->parseToken()->authenticate()) {
                return $next($request);
            }
            throw new UnauthorizedHttpException('jwt-auth', '未登录');
        } catch (TokenExpiredException $exception) {
            // 3. 此处捕获到了 token 过期所抛出的 TokenExpiredException 异常，我们在这里需要做的是刷新该用户的 token 并将它添加到响应头中
            try {
                // 刷新用户的 token
                $token = $this->auth->refresh();
                // 使用一次性登录以保证此次请求的成功
                Auth::onceUsingId($this->auth->manager()->getPayloadFactory()->buildClaimsCollection()->toPlainArray()['sub']);
            } catch (JWTException $exception) {
                // 如果捕获到此异常，即代表 refresh 也过期了，用户无法刷新令牌，需要重新登录。
                throw new UnauthorizedHttpException('jwt-auth', $exception->getMessage());
            }
        }

        // 在响应头中返回新的 token
        return $this->setAuthenticationHeader($next($request), $token);
    }
}

```
![](https://www.choudalao.com/uploads/20191117/20191117214606POeCWe.png)

# 路由
routes/api.php
```php
<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::namespace('Api')->prefix('v1')->middleware('cors')->group(function () {
    //用户注册
    Route::post('/users','UserController@store')->name('users.store');
    //用户登录
    Route::post('/login','UserController@login')->name('users.login');
    Route::middleware('api.refresh')->group(function () {
        //当前用户信息
        Route::get('/users/info','UserController@info')->name('users.info');
        //用户列表
        Route::get('/users','UserController@index')->name('users.index');
        //用户信息
        Route::get('/users/{user}','UserController@show')->name('users.show');
        //用户退出
        Route::get('/logout','UserController@logout')->name('users.logout');
    });

    Route::middleware('admin.guard')->group(function () {
        //管理员注册
        Route::post('/admins', 'AdminController@store')->name('admins.store');
        //管理员登录
        Route::post('/admin/login', 'AdminController@login')->name('admins.login');
        Route::middleware('admin.refresh')->group(function () {
            //当前管理员信息
            Route::get('/admins/info', 'AdminController@info')->name('admins.info');
            //管理员列表
            Route::get('/admins', 'AdminController@index')->name('admins.index');
            //管理员信息
            Route::get('/admins/{user}', 'AdminController@show')->name('admins.show');
            //管理员退出
            Route::get('/admins/logout', 'AdminController@logout')->name('admins.logout');
        });
    });
});


```
![](https://www.choudalao.com/uploads/20191117/20191117214639ic6UWD.png)

# 控制器
`App\Http\Controllers\Api\AdminController.php`内容如下
```php
<?php

namespace App\Http\Controllers\Api;

use App\Http\Requests\Api\AdminRequest;
use App\Http\Resources\Api\AdminResource;
use App\Models\Admin;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

;

class AdminController extends BaseController
{
    public function index()
    {
        $admins = Admin::paginate(3);
        return AdminResource::collection($admins);
    }

    public function show(Admin $admin)
    {
        return $this->success(new AdminResource($admin));
    }

    public function info()
    {
        $admins = Auth::user();
        return $this->success(new AdminResource($admins));
    }

     public function login(Request $request)
    {
        //获取当前守护的名称
        $present_guard =Auth::getDefaultDriver();
        $token = Auth::claims(['guard'=>$present_guard])->attempt(['name' => $request->name, 'password' => $request->password]);
        if ($token) {
            return $this->setStatusCode(201)->success(['token' => 'bearer ' . $token]);
        }
        return $this->failed('账号或密码错误', 400);
    }

    public function logout()
    {
        Auth::logout();
        return $this->success('退出成功...');
    }
}


```
# 测试
![](https://www.choudalao.com/uploads/20191117/20191117214930YeKqvI.png)
![](https://www.choudalao.com/uploads/20191117/20191117214941DbXhX9.png)

# 自动区分 guard
我希望可以让 guard 自动化，如果我请求的是 users 的，我就守护 api。如果我请求的是 admins 的，我就守护 admin。

接下来，就以 admins 的为例，users 的保持不动，创建中间件
```php
php artisan make:middleware Api/AdminGuardMiddleware
```
代码内容如下：
```php
<?php

namespace App\Http\Middleware\Api;

use Closure;

class AdminGuardMiddleware
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request $request
     * @param  \Closure $next
     *
     * @throws \Symfony\Component\HttpKernel\Exception\UnauthorizedHttpException
     *
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        config(['auth.defaults.guard' => 'admin']);
        return $next($request);
    }
}
```
打开 app/Http 目录下的 Kernel.php 文件，添加如下一行

```php
protected $routeMiddleware = [
    ......
    'admin.guard'=>\App\Http\Middleware\Api\AdminGuardMiddleware::class,
];
```
# 测试
再次进行登录测试，可以区分user和admin。