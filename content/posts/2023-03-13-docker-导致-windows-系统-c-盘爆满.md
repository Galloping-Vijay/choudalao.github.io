---
title: "docker 导致 windows 系统 C 盘爆满"
date: 2023-03-13T11:13:28+08:00
updated: 2026-02-23T04:01:00+08:00
author: "臭大佬"
categories: [linux]
description: "docker 导致 windows 系统 C 盘爆满"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 6096
---

# 问题
今天发现电脑C盘爆红,找了一下大文件,发现是名为`ext4.vhdx`的文件,这个是与`docker`相关的文件,由于在`Linux`中下载安装各种软件、`Docker Image`，运行多个`Docker Container` 导致C盘空间严重不足。

# 收缩ext4.vhdx文件
### 清理不必要的镜像
```go
docker system prune
```
### 停止wsl服务
这个很慢,还不如重启,跳过这一步
```go
wsl --shutdown
```
### 运行diskpart释放空间
win命令行中执行, file= 换成自己的路径
```go
diskpart
```
# 选择虚拟机文件执行瘦身
```go
select vdisk file="C:\Users\Administrator\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04LTS_79rhkp1fndgsc\LocalState\ext4.vhdx"
```
```go
attach vdisk readonly
```
```go
compact vdisk
```
```go
detach vdisk
```
```go
exit
```
运行完可以发现释放了好大的空间。如果C盘够大,就没必要看下面的迁移了。

#### zerofree

进入到 WSL2 中，运行 zerofree 将 ext4 文件系统内已经不用的块填零，但 zerofree 不能运行在已经挂载为 rw 的文件系统上，那就把文件系统挂载为 readonly 就行了
```go
mount /dev/sda -o remount,ro
```
```go
zerofree /dev/sda
```
运行结束后，在 Windows 下关闭 WSL2
```go
wsl --shutdown
```
再次运行diskpart释放空间步骤

# 迁移
当然,如果C盘比较小,想迁移到别的盘也是可以的

### 查看WSL实例
```go
wsl -l -v
```
*  NAME            STATE           VERSION
* Ubuntu-20.04    Stopped         2*
我只安装了一个WSL2的实例，名为Ubuntu-20.04
### 将现有WSL2实例备份导出：
导出到D盘下，命名为buntu-20.04_bak.tar.tar
```go
wsl --export Ubuntu-20.04 D:\Ubuntu-20.04_bak.tar
```
### 备份完成后可以注销现有实例
```go
	wsl --unregister Ubuntu-20.04
```
### 指定存放虚拟磁盘镜像文件的路径
```go
	wsl --import Ubuntu_new D:\WSL_Ubuntu D:\Ubuntu-20.04_bak.tar --version 2
```
> Ubuntu_new
· 实例名称，可以自己设置，设置后即为第2步输入wsl -l -v后显示的名称；
D:\WSL_Ubuntu
· 导入后的镜像及其相关数据存放路径；
D:\Ubuntu-20.04_bak.tar
· 导入的备份，即第3步通过wsl --export导出的文件；
–version 2
· WSL版本为2

### 设置默认登录用户
```go
ubuntu config --default-user root
```