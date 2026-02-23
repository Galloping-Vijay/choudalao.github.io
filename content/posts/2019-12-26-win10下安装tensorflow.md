---
title: "Win10下安装tensorflow"
date: 2019-12-26T23:27:28+08:00
updated: 2026-02-23T16:45:54+08:00
author: "臭大佬"
categories: [Python]
description: "Win10下安装tensorflow"
cover: "https://www.choudalao.com/uploads/20191226/jgkCZNEVCAGlKExRurDJsZncOSkjY12U1cMA9ZFo.jpeg"
click: 3997
---

# 前提
win安装tensorflow是基于Python的，并且需要从Anaconda仓库中下载

# 安装Anaconda
从官网下载：https://www.anaconda.com/download/

官网下载起来很慢，国内清华镜像网站：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

我下载的是这个：
![](https://www.choudalao.com/uploads/20191227/20191227101952yakQEp.png)
![](https://www.choudalao.com/uploads/20191227/20191227102008rNZj9t.png)

找到自己python对应的版本，下载安装，过程中点击next就可以。（如果不是默认安装，如修改了安装位置，需要配置环境变量，位置在xxx\Anaconda3\Scripts，如‘E:\Program Files (x86)\Anaconda3\Scripts’）

安装完成后`conda --version`，测试是否成功。
![](https://www.choudalao.com/uploads/20191226/20191226225409M2blWU.png)

# 安装Tensorflow

如果别的cmd工具出问题，推荐使用这个：
![](https://www.choudalao.com/uploads/20191227/20191227112433C6EAfI.png)

![](https://www.choudalao.com/uploads/20191227/20191227112450PPF0JL.png)

```shell
conda create -n tensorflow python=3.6
```

如果很慢修改镜像

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```

再执行

```shell
conda config --set show_channel_urls yes
```

打开`C:\Users\Administrator\.condarc`(也有可能在C:\Users\admin\.condarc,根据自己的情况),修改如下：
```shell
channels:
  - anaconda-fusion
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
show_channel_urls: true
ssl_verify: 'True'

```

![](https://www.choudalao.com/uploads/20191226/20191226225850W6hLBi.png)
![](https://www.choudalao.com/uploads/20191226/20191226225856vHHQGm.png)

输入`activate tensorflow`，切换了，就代表安装成功了。

```shell
conda activate tensorflow
```

有些要这样执行

```shell
activate tensorflow
# 退出
# deactivate tensorflow
```

![](https://www.choudalao.com/uploads/20191226/20191226225930sBwoWA.png)

然后就看到输入位置变成这样：
![](https://www.choudalao.com/uploads/20191226/20191226230251ofDSJM.png)

###  更新pip

提前打个预防针，因为很多时候安装不成功就是pip未更新的问题，所以，我们先把它更新了。

```shell
python -m pip install --upgrade pip
```

如果更新失败：

![](https://www.choudalao.com/uploads/20191226/20191226230425kjC097.png)

使用如下命令：

```shell
python -m pip install --upgrade pip -i https://pypi.douban.com/simple
```

![](https://www.choudalao.com/uploads/20191226/20191226230516JYSPSJ.png)

## 安装

```shell
pip install --upgrade --ignore-installed tensorflow
```

提示：如果更新了pip仍然无法安装，请使用:

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow
```

![](https://www.choudalao.com/uploads/20191226/20191226231211RlTF6k.png)

## 测试

输入
```shell
python
```
进入python后依次输入

```shell
>>> import tensorflow as tf
>>> print(tf.__path__)
```

![](https://www.choudalao.com/uploads/20191226/20191226232210xuJObU.png)

如上图，程序能够正常运行，Tensorflow安装成功。

# 导入PyCarm

![](https://www.choudalao.com/uploads/20191229/20191229121111X6fwhY.png)
![](https://www.choudalao.com/uploads/20191229/20191229121154r8WFZr.png)

这一步选择 `show all`

![](https://www.choudalao.com/uploads/20191229/20191229121250YCoDWQ.png)
![](https://www.choudalao.com/uploads/20191229/20191229121311h6D0pH.png)

找到`Anaconda3\envs\tensorflow`里面的python.exe导入。