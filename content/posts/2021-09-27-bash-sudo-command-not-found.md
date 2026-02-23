---
title: "bash: sudo: command not found"
date: 2021-09-27T15:19:58+08:00
updated: 2026-02-23T05:00:21+08:00
author: "臭大佬"
categories: [linux]
description: "在docker容器内的ubuntu下，报bash: sudo: command not found"
cover: "https://www.choudalao.com/uploads/20210927/YKTFrjzC0dYgfyu9sWw1dT2EyVOeHmXrrg2rRFcr.jpeg"
click: 3965
---

# 问题

在`docker`容器内的`ubuntu`下，报`bash: sudo: command not found`，
![](https://www.choudalao.com/uploads/20210927/20210927162747hvunGC.png)

容器内避免使用角色`root`，建立新用户执行命令 使用`sudo`。


# 解决方法

更新软件列表
```php
apt-get update
```

![](https://www.choudalao.com/uploads/20210927/202109271519271eweVD.png)

安装` sudo` 命令

```php
apt-get install sudo
```

![](https://www.choudalao.com/uploads/20210927/20210927162509jSmLLP.png)

用 `sudo` 试试
```php
sudo
```

![](https://www.choudalao.com/uploads/20210928/20210928090247uE57Fx.png)