---
title: "Ubuntu16.04 python2.7升级python3.5"
date: 2019-11-24T10:21:41+08:00
updated: 2026-02-22T11:56:56+08:00
author: "臭大佬"
categories: [Python]
description: "Ubuntu16.04 python2.7升级python3.5"
cover: "https://www.choudalao.com/uploads/20191124/WUJ4ixD9klMz4Yk3shfUgsxPlJVmQ1q8o85stgAT.jpeg"
click: 3011
---

博主用的是腾讯云,然后选择的服务器是ubuntu,首先确认一下ubuntu的版本。
```shell
cat /etc/issue
```
![](https://www.choudalao.com/uploads/20191124/20191124095833Iv8kgL.png)
正常情况下，你安装好ubuntu16.04版本之后，系统会自带 python2.7版本，
![](https://www.choudalao.com/uploads/20191124/20191124100141OFHv5y.png)
如果需要下载新版本的python3，就需要进行更新。下面给出具体教程：
# 步骤
## 首先在ubuntu的终端ternimal输入命令
```shell
sudo apt-get install python3.5
```
查看安装目录：
```shell
sudo whereis python
```
![](https://www.choudalao.com/uploads/20191124/20191124101638djUMMH.png)

## 指定默认打开的是python3.5版本
安装完成之后，你在终端中输入python，输出的信息里面会提示是2.7版本的，也就是说默认打开的并不是刚才安装好的3.5，所以还需要我们重新修改一下链接。方法如下：

### 先备份原来的链接（在对系统执行删除之前进行备份是个好的习惯）。在ternimal下输入命令：
```shell
sudo cp /usr/bin/python /usr/bin/python_bak
```
### 删除原来默认指向python2.7版本的链接。在ternimal下输入命令：
```shell
sudo rm /usr/bin/python
```
### 重新指定新的链接给python3.5版本。输入命令：
```shell
sudo ln -s /usr/bin/python3.5 /usr/bin/python
```
### 查看当前python版本
```shell
python
```
![](https://www.choudalao.com/uploads/20191124/201911241021259HU9pD.png)