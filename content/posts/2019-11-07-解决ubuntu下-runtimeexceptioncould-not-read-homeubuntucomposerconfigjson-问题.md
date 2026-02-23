---
title: "解决ubuntu下 [RuntimeException]Could not read /home/ubuntu/.composer/config.json ...问题"
date: 2019-11-07T16:29:12+08:00
updated: 2026-02-23T04:58:43+08:00
author: "臭大佬"
categories: [php]
description: "解决ubuntu下 [RuntimeException]Could not read /home/ubuntu/.composer/config.json file_get_contents(/home/ubuntu/.composer/config.json): failed to open stream: Permission denied问题"
cover: "https://www.choudalao.com/uploads/20191107/dMUqX48DfeYKovgEtGsfXaOzattGlR0uSgFRSuTv.png"
click: 5708
---

####  腾讯云的ubuntu环境下,使用composer切换镜像的时候出现报错,代码如下
`composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/`
#### 出现如下错误:

>**[RuntimeException]                                                      
  Could not read /home/ubuntu/.composer/config.json                                                                                                
  file_get_contents(/home/ubuntu/.composer/config.json): failed to open   
  stream: Permission denied**

![](https://www.choudalao.com/uploads/20191107/201911071607118aQOsw.png)

#### 可以看出,这是用于权限问题引起的
这种情况需要修改一下.composer/config.json 和同一目录下的auth.json 的权限

### 操作步骤如下:
1. 移动到相应目录下(我的是 /home/ubuntu/.composer),执行如下命令

`cd /home/ubuntu/.composer`

`sudo chmod +777 ./config.json`

`sudo chmod +777 ./auth.json`

![](https://www.choudalao.com/uploads/20191107/20191107162044zJTr4s.png)
![](https://www.choudalao.com/uploads/20191107/20191107162118e2n9e1.png)

完成