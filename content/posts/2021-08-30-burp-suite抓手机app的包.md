---
title: "Burp Suite抓手机app的包"
date: 2021-08-30T10:55:38+08:00
updated: 2026-02-23T07:01:20+08:00
author: "臭大佬"
categories: [linux]
description: "Burp Suite抓手机app的包"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4554
---

# 前言

之前在[Burpsuite 安装及简单使用](https://www.choudalao.com/article/257 "Burpsuite 安装及简单使用")有简单介绍pc端的抓包，那么手机端的怎么抓包呢？这边简单介绍一下。

# 前提
pc端已经安装了Burp Suite，并且手机和pc在同一局域网内。

# 配置
## 查询电脑IP地址
在pc命令行中输入`ipconfig`查看ip地址

![](https://www.choudalao.com/uploads/20210830/20210830102542fUzRQo.png)

我插的是网线，以太网 ipv4地址是我们需要用到的，`192.168.1.17`。如果pc连接的是`wifi`的话，应该是 无线局域网适配器 WLAN 那一栏，

##  设置 burp
打开burp，Proxy（代理）---Options（选项）---添加。
我的是已经添加好了，所以是编辑状态，端口弄一个比较不常用的，避免冲突，地址：刚才ipconfig查看的IP地址

![](https://www.choudalao.com/uploads/20210830/20210830103515R1i8NE.png)

## 手机端配置
我的是华为手机，如有不同，请自行百度。
设置---WLAN
长按已经连接上的wifi名称 ---  修改网络。
填写我们刚才在burp上设置的端口和ip。

![](https://www.choudalao.com/uploads/20210830/20210830104121MCabSK.png)

## 证书

本地建一个空cer文件

![](https://www.choudalao.com/uploads/20210830/20210830110203TnlfLS.png)

Proxy（代理）---Options（选项）---导入/导出CA证书---DER格式的证书

![](https://www.choudalao.com/uploads/20210830/202108301103270WHMeb.png)

把下载好的传到手机

![](https://www.choudalao.com/uploads/20210830/20210830110913puStw0.png)

安装
![](https://www.choudalao.com/uploads/20210830/20210830110928XU1Y6G.png)

手机打开软件，burp就能抓取包数据了。