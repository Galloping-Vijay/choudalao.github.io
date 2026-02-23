---
title: "cURL error 60: SSL certificate problem: unable to get local issuer certifica 解决"
date: 2019-11-05T10:16:03+08:00
updated: 2026-02-23T07:57:48+08:00
author: "臭大佬"
categories: [php]
description: "cURL error 60: SSL certificate problem: unable to get local issuer certifica 解决"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 6490
---

&lt;p&gt;&lt;b&gt;&lt;font color=&quot;#cc0000&quot;&gt;&lt;/font&gt;&lt;p&gt;&lt;span style=&quot;font-size:24px&quot;&gt;&lt;font color=&quot;#cc0000&quot;&gt;解决:GuzzleHttp \ Exception \ RequestException cURL error 60: SSL certificate problem: unable to get local issuer certificate (see http://curl.haxx.se/libcurl/c/libcurl-errors.html)&lt;/font&gt;&lt;/span&gt;&lt;/p&gt;&lt;/b&gt;&lt;/p&gt;&lt;p&gt;&lt;span&gt;从&amp;nbsp;&lt;/span&gt;&lt;a href=&quot;https://curl.haxx.se/docs/caextract.html&quot; target=&quot;_blank&quot;&gt;https://curl.haxx.se/docs/caextract.html&lt;/a&gt;&lt;span&gt;&amp;nbsp;上下载&lt;/span&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://curl.haxx.se/ca/cacert.pem&quot;&gt;cacert.pem&lt;/a&gt;&lt;/p&gt;&lt;p&gt;打开php.ini&amp;nbsp; 搜索curl.cainfo 与 openssl.cafile,将其配置成你自己cacert.pem文件的路径&lt;/p&gt;&lt;p&gt;curl.cainfo=&quot; 路径 &quot;&lt;/p&gt;&lt;p&gt;openssl.cafile=&quot;路径&quot;&lt;/p&gt;&lt;p&gt;例如:&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;[curl]
; A default value for the CURLOPT_CAINFO option. This is required to be an
; absolute path.
curl.cainfo = &quot;E:\phpstudy_pro\Extensions\php\cacert.pem&quot;

[openssl]
; The location of a Certificate Authority (CA) file on the local filesystem
; to use when verifying the identity of SSL/TLS peers. Most users should
; not specify a value for this directive as PHP will attempt to use the
; OS-managed cert stores in its absence. If specified, this value may still
; be overridden on a per-stream basis via the &quot;cafile&quot; SSL stream context
; option.
openssl.cafile=&quot;E:\phpstudy_pro\Extensions\php\cacert.pem&quot;

; If openssl.cafile is not specified or if the CA file is not found, the
; directory pointed to by openssl.capath is searched for a suitable
; certificate. This value must be a correctly hashed certificate directory.
; Most users should not specify a value for this directive as PHP will
; attempt to use the OS-managed cert stores in its absence. If specified,
; this value may still be overridden on a per-stream basis via the &quot;capath&quot;
; SSL stream context option.
;openssl.capath=&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;code class=&quot;PHP&quot;&gt;&lt;br&gt;&lt;/code&gt;&lt;/p&gt;&lt;p style=&quot;text-align: center;&quot;&gt;&lt;img src=&quot;https://www.choudalao.com/uploads/20191105/Bw0vp6ONrC5dIbM9FcHuqrmjqS828KxJYZv1kBxf.png&quot; alt=&quot;&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;code class=&quot;PHP&quot;&gt;&lt;br&gt;&lt;/code&gt;&lt;/p&gt;