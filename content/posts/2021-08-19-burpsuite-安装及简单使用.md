---
title: "Burpsuite 安装及简单使用"
date: 2021-08-19T16:04:06+08:00
updated: 2026-02-23T09:48:55+08:00
author: "臭大佬"
categories: [linux]
description: "Burpsuite 安装及简单使用"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 5828
---

# 概述

Burp Suite 是用于攻击web 应用程序的集成平台，包含了许多工具。Burp Suite为这些工具设计了许多接口，以加快攻击应用程序的过程。所有工具都共享一个请求，并能处理对应的HTTP 消息、持久性、认证、代理、日志、警报。

# WIN下安装

#### 获取
官网获取：https://portswigger.net/burp

#### java环境安装
因为burpsuite是在JAVA环境下运行的，所以首先应该配置好JAVA环境
java安装详见我的另一篇文章[《在windows下安装 Elasticsearch》](https://www.choudalao.com/article/207 "《在windows下安装 Elasticsearch》")

#### 安装Burpsuite

###### 下载完成exe包直接点击安装就行，然后双击打开会出现如下界面，

![](https://www.choudalao.com/uploads/20210819/20210819152411Ac9FLh.png)
###### 这些配置直接跳过，点击下一步就行
![](https://www.choudalao.com/uploads/20210819/20210819152625hLiG0E.png)

###### 配置 Burp suite 代理 ，打开burp 选择 proxy----->options
![](https://www.choudalao.com/uploads/20210819/20210819153237gLliAb.png)

###### 默认是8080端口，这个端口比较常用，如果冲突记得修改一下，我的改成8081了。

![](https://www.choudalao.com/uploads/20210819/20210819153437RTi7Sc.png)

### 浏览器进行配置
这里以谷歌浏览器为例 ,其他浏览器类似，可自行百度。设置----->高级 ----->打开您计算机的代理设置，如下图
![](https://www.choudalao.com/uploads/20210819/2021081915384735u6wK.png)

点击打开如下如设置
![](https://www.choudalao.com/uploads/20210819/20210819154227CycSWU.png)

### 设置完代理，设置burp suite

![](https://www.choudalao.com/uploads/20210819/20210819155017bQpPfT.png)

#### 抓HTTPS数据包
如果出现如下情况，解决办法就是安装burp的受信任证书。
![](https://www.choudalao.com/uploads/20210819/20210819154834hH99nX.png)

###### 安装SSL受信任证书，打开浏览器访问 http://burp ，点击CA   Certificate  下载证书进行安装

在使用Burp site对HTTPS进行拦截时他会提示,你的连接不是私密连接或此连接不信任等,这是由于通常情况下burp默认只抓HTTP的包，HTTPS因为含有证书，因而无法正常抓取，抓HTTPS数据包就需要设置可信证书。

![](https://www.choudalao.com/uploads/20210819/20210819155200YP657k.png)

下载完成的文件名是：cacert.der，后缀名是.der文件（证书的编码方式不一样），这个文件不是常规的.cer的证书文件，下面就是让浏览器信任我们刚才导出的证书。


#### 打开浏览器设置（我这里是谷歌）
隐私设置和安全性->证书管理->中间证书颁发机构

![](https://www.choudalao.com/uploads/20210819/20210819165249CysZkg.png)
选择下载的文件下一步下一步导入就可以。


#### 导出证书
导入刚才的cacert.der文件，那么在服务器中就会存在“PortSwigger CA”这样的证书（burp的内置证书）、然后选中它进行导出

![](https://www.choudalao.com/uploads/20210819/202108191654324pXYHf.png)

这里选择base64
![](https://www.choudalao.com/uploads/20210819/20210819165455ylZ94U.png)

自己建一个xxx.cer文件，然后选择它并替换就行

#### 导入cer证书

切换到受信任的证书颁发机构，进行导入刚才的cer文件

![](https://www.choudalao.com/uploads/20210819/20210819165655YuKFK3.png)

#### 效果
导入之后开启代理，不会出现警告了，
![](https://www.choudalao.com/uploads/20210819/20210819165809BrwJ23.png)

开启burp suite 抓包
![](https://www.choudalao.com/uploads/20210819/20210819165912fESDf0.png)

ok！

# 问题

### burp suite 中文乱码问题
按照如下步骤设置：

![](https://www.choudalao.com/uploads/20210819/20210819231539V9iwdJ.png)