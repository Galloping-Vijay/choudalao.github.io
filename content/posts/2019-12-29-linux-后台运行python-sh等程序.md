---
title: "Linux 后台运行python .sh等程序"
date: 2019-12-29T20:56:16+08:00
updated: 2026-02-23T15:35:55+08:00
author: "臭大佬"
categories: [Python]
description: "Linux 后台运行python .sh等程序，以及查看和关闭后台运行程序操作"
cover: "https://www.choudalao.com/uploads/20191229/SXUgp6zT3ijXYlUJarRuLnhX1ElpxEVnXTqUMVbC.jpeg"
click: 4110
---

# 问题

这不马上春节了嘛，所以就开始研究抢票程序了，哈哈哈，看看我的程序，

![](https://www.choudalao.com/uploads/20191229/20191229201150dBgVBH.png)

程序是跑起来了，但是当我关闭终端（xshell）的时候，刷票也就退出了，这不是我要的结果啊，其实很多时候，像python文件以及一些.sh文件操作，我们都希望它在后台一直运行着，那怎么保持后台运行呢？

# 后台运行命令
首先我们先来介绍几个命令

### &命令
加在一个命令的最后，可以把这个命令放在后台执行

### nohup命令
不挂断的运行命令

# 查看当前后台运行的命令
### jobs命令
查看当前终端后台运行的任务

jobs -l选项可显示当前终端所有任务的PID，jobs的状态可以是running，stopped，Terminated。+ 号表示当前任务，- 号表示后一个任务。

![](https://www.choudalao.com/uploads/20191229/20191229202347g68tPA.png)

### ps命令
查看当前的所有进程

ps -aux | grep "test.sh"    #a:显示所有程序  u:以用户为主的格式来显示   x:显示所有程序，不以终端机来区分

![](https://www.choudalao.com/uploads/20191229/20191229202331IDnH8f.png)

### ps和jobs区别

jobs和ps,区别是jobs用于查看当前终端后台运行的任务，换了终端就看不到了。而ps命令用于查看瞬间进程的动态，可以看到别的终端运行的后台进程。

# 关闭当前后台运行的命令
有开启，肯定要知道关闭啊，

kill命令：结束进程
	通过jobs命令查看jobnum，然后执行   kill %jobnum
	通过ps命令查看进程号PID，然后执行  kill %PID
如果是前台进程的话，直接执行 Ctrl+c 就可以终止了
   
栗子：
```shell
kill -s 9 1827
```
其中-s 9 制定了传递给进程的信号是９，即强制、尽快终止进程。各个终止信号及其作用见附录。1827是PID

# 前后台进程的切换与控制
（1）fg命令

   功能：将后台中的命令调至前台继续运行

   如果后台中有多个命令，可以先用jobs查看jobnun，然后用 fg %jobnum 将选中的命令调出。

 （2）Ctrl + z 命令

   功能：将一个正在前台执行的命令放到后台，并且处于暂停状态

 （3）bg命令

   功能：将一个在后台暂停的命令，变成在后台继续执行

   如果后台中有多个命令，可以先用jobs查看jobnum，然后用 bg %jobnum 将选中的命令调出继续执行。

# 例子
就以微信群控那个为例吧！
```shell
nohup python -u WechatAddGroupHelper.py > python.log 2>&1 &
```
 \> 表示把标准输出（STDOUT）重定向到 那个文件，这里重定向到了python.log
 & 表示在后台执行脚本
 1是标准输出（STDOUT）的文件描述符，2是标准错误（STDERR）的文件描述符
 1> python.log 简化为 > python.log，表示把标准输出重定向到python.log这个文件
 2>&1 表示把标准错误重定向到标准输出，这里&1表示标准输出 ， 为什么需要将标准错误重定向到标准输出的原因，是因为标准错误没有缓冲区，而STDOUT有。 这就会导致 commond > python.log ，2> python.log 文件python.log被两次打开，而STDOUT和 STDERR将会竞争覆盖，这肯定不是我门想要的
 -u参数，使得python不启用缓冲。