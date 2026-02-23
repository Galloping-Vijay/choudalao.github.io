---
title: "laravel上传文件不用软连接,直接存public下"
date: 2019-09-21T03:31:51+08:00
updated: 2026-02-23T11:08:07+08:00
author: "臭大佬"
categories: [php]
description: "laravel上传文件不用软连接,直接存public下"
cover: "http://www.choudalao.com/uploads/20190921/YOpFbf1KwkuIhC3QRAZKqQsIUA9cR1MgjbswrMTi.jpeg"
click: 3926
---

&lt;p&gt;&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;//配置上传文件config/filesystems.php,在 ‘disks’ 数组中添加uploads数组
'disks' =&amp;gt; [
    //自定义上传路径
    'uploads' =&amp;gt; [
        'driver' =&amp;gt; 'local',
        'root' =&amp;gt; public_path('uploads/' . date('Ymd')),
    ],
    ...
],
//控制器代码
if ($request-&amp;gt;isMethod('post')) {
    $date = date('Ymd');
    $path = $request-&amp;gt;file('file')-&amp;gt;store('', 'uploads');
    if ($path) {
        $fileUrl = '/uploads/' . $date . '/' . $path;
        return fileUrl;//返回的是文件路径
    } else {
      return  &quot;上传失败&quot;;
    }
}&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;/p&gt;