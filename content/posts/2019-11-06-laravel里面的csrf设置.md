---
title: "laravel里面的CSRF设置"
date: 2019-11-06T23:15:10+08:00
updated: 2026-02-23T08:33:21+08:00
author: "臭大佬"
categories: [php]
description: "laravel里面的CSRF设置"
cover: "https://www.choudalao.com/uploads/20191218/Ws8Gn7h2fKuhtYNe4osd5GFO2b4ElrydZT2KjZ0k.jpeg"
click: 3528
---

<p>Laravel默认是开启了CSRF功能。</p><h2>关闭此功能有两种方法</h2><h3>方法一</h3><p>打开文件：app\Http\Kernel.php</p><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">'App\Http\Middleware\VerifyCsrfToken'//注释掉</code></pre><h3>方法二</h3><p><code class="JavaScript"></code></p><p>打开文件：app\Http\Middleware\VerifyCsrfToken.php修改为：</p><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">namespace App\Http\Middleware;

use Closure;
use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;

class VerifyCsrfToken extends BaseVerifier {

    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        // 使用CSRF
        //return parent::handle($request, $next);
        // 禁用CSRF
        return $next($request);
    }
}</code></pre><h2><br></h2><h2>CSRF的使用有两种方法：</h2><h3>第一种</h3><p><code class="JavaScript"></code></p><p>在HTML的代码中加入：</p><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">&lt; input type="hidden" name="_token" value="{{ csrf_token() }}"/&gt;</code></pre><p><br></p><h3>第二种</h3><p>使用cookie方式。</p><p>使用cookie方式的CSRF，可以不用在每个页面都加入这个input的hidden标签。</p><p><code class="JavaScript"></code></p><p>使用cookie方式，需要把app\Http\Middleware\VerifyCsrfToken.php修改为：</p><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">namespace App\Http\Middleware;

use Closure;
use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;

class VerifyCsrfToken extends BaseVerifier {

    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        return parent::addCookieToResponse($request, $next($request));
    }

}</code></pre><h3><br></h3><h3>只对GET的方式提交使用CSRF，对POST方式提交表单禁用CSRF</h3><p>对指定的表单[提交方式]使用CSRF，如：</p><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">namespace App\Http\Middleware;

use Closure;
use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;

class VerifyCsrfToken extends BaseVerifier {

    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        // Add this:
        if($request-&gt;method() == 'POST')
        {
            return $next($request);
        }
        
        if ($request-&gt;method() == 'GET' || $this-&gt;tokensMatch($request))
        {
            return $next($request);
        }
        throw new TokenMismatchException;
    }

}</code></pre><h3><br></h3><h3>修改CSRF的cookie名称方法</h3><p>要修改这个名称值，可以到打开这个文件：vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\VerifyCsrfToken.php 找到”XSRF-TOKEN“，修改</p><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">/**
 * Add the CSRF token to the response cookies.
 *
 * @param  \Illuminate\Http\Request  $request
 * @param  \Symfony\Component\HttpFoundation\Response  $response
 * @return \Symfony\Component\HttpFoundation\Response
 */
protected function addCookieToResponse($request, $response)
{
	$config = config('session');

	$response-&gt;headers-&gt;setCookie(
		new Cookie(
			'XSRF-TOKEN', $request-&gt;session()-&gt;token(), $this-&gt;availableAt(60 * $config['lifetime']),
			$config['path'], $config['domain'], $config['secure'], false, false, $config['same_site'] ?? null
		)
	);

	return $response;
}</code></pre><p><span><br></span></p><p><span>也可以在app\Http\Middleware\VerifyCsrfToken.php文件中，重写addCookieToResponse()方法做到</span></p><p><code class="JavaScript"><br></code></p><p><code class="JavaScript"><br></code></p>