---
title: "解决ubuntu中使用git碰到的问题：error: cannot open .git/FETCH_HEAD: Permission denied"
date: 2019-11-14T21:23:04+08:00
updated: 2026-02-23T13:51:11+08:00
author: "臭大佬"
categories: [linux]
description: "解决ubuntu中使用git碰到的问题：error: cannot open .git/FETCH_HEAD: Permission denied"
cover: "https://www.choudalao.com/uploads/20191114/2WpJvmTqM80aGmIm99qN5yLM843wq8aIFGqu8301.jpeg"
click: 8471
---

##### 腾讯云服务器默认用户是ubuntu,在里面配置宝塔作为web的开发环境,在使用git时老是会遇到问题。

例如拉取代码：


```
git pull
```

## error: cannot open .git/FETCH_HEAD: Permission denied

![](https://www.choudalao.com/uploads/20191114/20191114205601FqtcJ7.png)

这是一个linux权限问题，我们可以看一下.git当前用户组。

![](https://www.choudalao.com/uploads/20191114/20191114212138c4vslb.png)

它属于root用户，当前用户是ubuntu！

之前都只专注于搬砖，没太在意它，都是使用sudo暴利解决：

```
sudo git pull
```

之前还做过一个特别危险的骚操作，就是把整个网站目录设置成777，

```
sudo chmod -R 777 ./*
```

这样做确实可以解决问题，之后`git pull`等操作非常顺，但是这样做太危险了，网站很容易被别人攻击，警告大家，慎用。

网上还有看到说把。git设置成777权限的，虽然这也是一种解决方法，但个人觉得，以上三种操作，都不是做好的解决方法。

```
sudo chmod -R 777 .git/*
```

其实，我觉得，把.git目录的权限设置成当前用户和用户组会更好一下。

```php
sudo chown -R ubuntu:ubuntu .git
```

我们再看一下.git目录权限组

![](https://www.choudalao.com/uploads/20191114/20191114210820yp58IO.png)

![](https://www.choudalao.com/uploads/20191114/20191114212241zTOo7N.png)

之后执行git命令就不会出现以上问题了。

![](https://www.choudalao.com/uploads/20191114/20191114210915PcbUQp.png)