---
title: "Linux 下安装python3 | 臭大佬"
date: 2020-09-08T23:12:37+08:00
updated: 2026-02-23T17:14:33+08:00
author: "臭大佬"
categories: [php]
description: "Linux 下安装python3 | 臭大佬"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 2985
---

# 问题
`Linux` 系统一般默认装的是 `Python2`，不过开发中大家都一般用`python3`了，但很多系统依赖的东西还是`Python2`,那怎么在不破坏原环境的情况下安装 `Python3` 呢？

# 方法
由于某种不可抗拒力量，下载`python`包会特别慢，所以在安装`python3`前，我们先来个加速，可使用`mwget`进行加速，其中m代表多线程的意思。

### 安装 mwget
```shell
wget http://jaist.dl.sourceforge.net/project/kmphpfm/mwget/0.1/mwget_0.1.0.orig.tar.bz2
```

```shell
tar -xjvf mwget_0.1.0.orig.tar.bz2
```
```shell
cd mwget_0.1.0.orig
```
```shell
./configure
```
如果出现 `error: C++ compiler cannot create executables` 说明没有安装`c++`编译器 安装一个`c++`编译器就可以了
```shell
yum install gcc-c++
```
如果执行`./configure` 出现 `configure: error: Your intltool is too old.  You need intltool 0.35.0 or later.`

需要安装0.35.0以上的版本
```shell
yum install intltool
```
安装
```shell
make && make install
```
安装完毕后 可以使用`mwget`下载了。

### 安装 python3

依赖包

```shell
yum -y groupinstall "Development tools"
```
```shell
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```
一般用`python3.7`比较多，我们下载`3.7.3`。

```shell
mwget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
```
创建文件夹

```shell
mkdir /usr/local/python3 
```

解压

```shell
tar  zxvf Python-3.7.3.tgz
```

```shell
cd Python-3.7.3
```

```shell
./configure --prefix=/usr/local/python3
```

```shell
make && make install
```

软链

```shell
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```

```shell
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

这样，我们输入 `python` 就会调用`python2`,输入`python3`就会调用`python3`，`pip`一样的道理。

# 测试

```shell
python -V
```
```shell
python3 -V
```
![](https://www.choudalao.com/uploads/20200908/20200908230824Xc1GEN.png)