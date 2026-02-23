---
title: "phpStudy+nginx配置laravel伪静态"
date: 2019-11-06T14:15:29+08:00
updated: 2026-02-23T15:18:34+08:00
author: "臭大佬"
categories: [php]
description: "phpStudy+nginx配置laravel伪静态"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 9119
---

之前一直用宝塔配置环境,但是,最近宝塔win版本的停止更新了,只能用回phpstudy了,

记录一下配置伪静态

1:点击创建站点的时候,进行伪静态配置

![](https://www.choudalao.com/uploads/20191115/20191115162649pDEZ1g.png)

在伪静态输入框中输入如下代码,并点击保存
```c
# Check if a file exists, or route it to index.php.
try_files $uri $uri/ /exploit/index.php?$query_string;
if (!-e $request_filename) {
    rewrite  ^(.*)$  /index.php?s=$1  last;
    break;
}
```

![](https://www.choudalao.com/uploads/20191115/20191115162832I7cfw5.png)

打开相应的配置文件,我现在配置的是localhost_80.conf

![](https://www.choudalao.com/uploads/20191115/201911151630494G2Cdh.png)

![](https://www.choudalao.com/uploads/20191115/20191115163142rxwzVV.png)

打开相应的站点跟目录可以看到在public下面会有个nginx.htaccess文件

![](https://www.choudalao.com/uploads/20191115/20191115163315nfc8qG.png)

```shell
server {
        listen        80;
        server_name  dev.test.net;
        root   "E:/wwwroot/xxxx/public";
        location / {
            index index.php index.html error/index.html;
			if (!-e $request_filename) {
		   rewrite  ^(.*)$  /index.php?s=/$1  last;
		   break;
			}
            autoindex  off;
        }
        location ~ \.php(.*)$ {
            fastcgi_pass   127.0.0.1:9001;
            fastcgi_index  index.php;
            fastcgi_split_path_info  ^((?U).+\.php)(/?.+)$;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            fastcgi_param  PATH_INFO  $fastcgi_path_info;
            fastcgi_param  PATH_TRANSLATED  $document_root$fastcgi_path_info;
            include        fastcgi_params;
        }
}

```

重启nginx查看效果

配置完成!