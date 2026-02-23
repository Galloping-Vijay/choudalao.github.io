---
title: "docker: Error response from daemon: status code not OK but 500:     ���� FDocker.Core, Version=3.4.0.64130, Culture=neutral, PublicKeyToken=null"
date: 2021-06-10T18:19:07+08:00
updated: 2026-02-22T21:00:28+08:00
author: "臭大佬"
categories: [linux]
description: "docker: Error response from daemon: status code not OK but 500:     ����
FDocker.Core, Version=3.4.0.64130, Culture=neutral, PublicKeyToken=null"
cover: "https://www.choudalao.com/uploads/20210610/jcfnpZIFflGyAilQtjC67wNKBKiOpE30M0bPcIT5.jpeg"
click: 4237
---

# 问题

> docker: Error response from daemon: status code not OK but 500:     ����
FDocker.Core, Version=3.4.0.64130, Culture=neutral, PublicKeyToken=nullock                              ClassNameMessageDataInnerExceptionHelpURLStackTraceStringRemoteStackTraceStringRemoteStackIndexExceptionMethodHResultSoWatsonBuckets  System.Collections.IDictionarySystem.Excepti   
 ocker.Core.DockerException   Filesharing has been cancelled
 
![](https://www.choudalao.com/uploads/20210610/20210610181011rFF8ls.png)

# 解决
我们的命令如下：

```php
// 使用镜像 gallopingvijay/mylinux:v1.0.0，以后台模式启动一个容器,将容器的 80 端口映射到主机的 12345 端口,主机的目录 D:\wwwroot 映射到容器的 /www/wwwroot/，并指定名称为 mylinux
docker run -it -d -v D:\wwwroot:/www/wwwroot/ -p 12345:80 -p 1111:8888 --name="mylinux" gallopingvijay/mylinux:v1.0.0
```
我们想把本地的 D:\wwwroot 映射到容器内部，但是没有权限，修改设置，添加对应磁盘的分享权限，就可以使用了。

![](https://www.choudalao.com/uploads/20210610/20210610181755uXy4f5.png)

再次运行：
![](https://www.choudalao.com/uploads/20210610/20210610181857sS0PSt.png)