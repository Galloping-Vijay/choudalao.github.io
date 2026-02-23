---
title: "v-u-l-t-r一键搭建S-S/S-S-R脚本"
date: 2020-05-07T23:11:28+08:00
updated: 2026-02-23T16:28:15+08:00
author: "臭大佬"
categories: [其他]
description: "v-u-l-t-r一键搭建S-S/S-S-R脚本"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 2921
---

# vultr注册及购买
国外VPS服务商除了[搬瓦工](https://bwh1.net/index.php "搬瓦工")可以在VPS管理后台进行一键搭建SS外，其它的商家还没有发现有这个额外的功能，都需要我们手动执行命令（代码）来进行操作。

[vultr注册地址](https://www.vultr.com/?ref=8566696 "vultr注册地址")

[充值活动](https://www.vultr.com/?ref=8566934-6G "充值活动")

### 注册

![](https://www.choudalao.com/uploads/20200507/20200507223549hUoR9j.png)

输入邮箱和密码，

![](https://www.choudalao.com/uploads/20200507/20200507223915JNe2JX.png)

注册成功后登陆进行验证邮箱，点击log in

### 充值

只有先充值余额才能够进行消费已经获赠Vultr官方的优惠活动金额。这里可以选择支付宝，比较方便。

![](https://www.choudalao.com/uploads/20200507/20200507224028DclraI.png)

### 创建VPS服务器

充值完成后，选择左侧面板“Servers”点击面板右上角的“+”号，进入“Deploy”页面进行创建VPS服务器。

![](https://www.choudalao.com/uploads/20200507/20200507224648NEwGbS.png)
![](https://www.choudalao.com/uploads/20200507/20200507224400SUbrNd.png)
![](https://www.choudalao.com/uploads/20200507/20200507224804k7dGo9.png)

![](https://www.choudalao.com/uploads/20200507/20200507224854vD6dbe.png)

当安装完成后就可以看到VPS的基本信息了，包括：root密码、IP地址以及内存、硬盘等各项信息，

![](https://www.choudalao.com/uploads/20200507/20200507224926guUzRn.png)

### 远程连接VPS服务器

如果发现xshell等工具不能登陆，有可能是22端口未开放，可以点击这个链接检测，[检测端口](http://coolaf.com/tool/port "检测端口")，
如果端口没有开放，请直接删除，重新创建一个，以免它一直扣费

![](https://www.choudalao.com/uploads/20200507/20200507225237cZnBWc.png)

删除成功后，按上面创建VPS服务器步骤重新创建即可，

# 安装bbr加速
用刚才截图的地址及账号密码登录xsell后,据说安装bbr可以提速，因为没有对比过，所以，只能说是据说，先安装一下
```shell
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh 
```
```shell
chmod +x bbr.sh  # 我用的时候需要改一下权限
```
```shell
./bbr.sh 
```

![](https://www.choudalao.com/uploads/20200508/20200508233921O8L4XY.png)

安装完后，输入 y 并回车后重启 VPS。
![](https://www.choudalao.com/uploads/20200508/202005082340267Jdb8s.png)

重启完成后，进入 VPS，验证一下是否成功安装最新内核并开启 TCP BBR，输入以下命令：

```shell
uname -r
```
```shell
sysctl net.ipv4.tcp_available_congestion_control

```
```shell
sysctl net.ipv4.tcp_congestion_control
```
```shell
sysctl net.core.default_qdisc 
```
```shell
lsmod | grep bbr
```

返回值有 tcp_bbr 模块即说明bbr已启动。

![](https://www.choudalao.com/uploads/20200508/20200508234330bxux3v.png)

# 搭建SS服务器

用刚才截图的地址及账号密码登录xsell后，运行如下命令

```shell
wget --no-check-certificate -O shadowsocks.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
// 获取所有版本
// wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh
```
如出现错误提示 bash: wget: command not found，可以请在先执行 `yum -y install wget` 或者 `apt-get install -y wget` 命令。成功后，再执行上面的命令。如果没有出现提示错误，请略过。

等待上一步的命令执行结束后，继续执行命令：
```shell
chmod +x shadowsocks.sh
// 对应上面的 shadowsocks-all
// chmod +x shadowsocks-all.sh
```
等待上一步的命令执行结束后，继续执行命令:
```shell
./shadowsocks.sh 2>&1 | tee shadowsocks.log
// 对应上面的 shadowsocks-all
// ./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
```
根据需要选择，不懂的话直接选1，或者默认回车。下面会提示你输入你的 SS SERVER 的密码和端口。不输入就是默认。跑完命令后会出来你的 SS 客户端的信息。

![](https://www.choudalao.com/uploads/20200507/20200507231854q8upkR.png)
![](https://www.choudalao.com/uploads/20200507/20200507231906a4O0hl.png)

全部选择完毕后，当出现如下命令就说明安装成功了：

![](https://www.choudalao.com/uploads/20200508/20200508103618Ou0nfm.png)

如果安装过程中出现如下错误，那需要配置python，如果没有出现，请自行跳过 安装python2.7 步骤

![](https://www.choudalao.com/uploads/20200507/20200507231946YLqIN9.png)

#### 安装python2.7
安装make
```shell
yum -y install gcc automake autoconf libtool make
```
安装g++:
```shell
yum install gcc gcc-c++
```
官网直接下载Python 2.7.11压缩包
```shell
wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
```
压缩包解压
```shell
tar -xvzf Python-2.7.11.tgz
```
将Python解压包移动到/home目录下
```shell
mv Python-2.7.11 /home
```
进入Python目录
```shell
cd Python-2.7.11

./configure --prefix=/usr/local/python2.7

make install

make
```
如果出现如下报错，

```shell
./python -E -S -m sysconfig --generate-posix-vars ;\ if test $? -ne 0 ; then \ 	echo "generate-posix-vars failed" ; \ 	rm -f ./pybuilddir.txt ; \ 	exit 1 ; \ fi
```

![](https://www.choudalao.com/uploads/20200508/20200508002210WkzI3O.png)

在 ./configure 操作前，先执行如下命令：

```shell
export LANGUAGE=en_US.UTF-8

export LANG=en_US.UTF-8

export LC_ALL=en_US.UTF-8
```

![](https://www.choudalao.com/uploads/20200508/20200508002400QRgVOS.png)

然后再从./configure --prefix=/usr/local/python2.7 命令开始

![](https://www.choudalao.com/uploads/20200508/20200508002434BkwBgp.png)


### SS配置

查看当前ss服务器所开放的端口

```shell
ss -lntp | grep ssserver
```

查看当前ss服务器的密码，通过以下命令可见ss的配置文件，配置文件中自然有密码

```shell
ps aux | grep ssserver
```
![](https://www.choudalao.com/uploads/20200508/20200508105814hEFMQn.png)

修改ss密码
```shell
vi /etc/shadowsocks.json
```
按i键进入编辑模式，修改密码为123456
```shell
"password":"123456",
```
重启ss即可
```shell
service shadowsocks restart
```
附：ss启动停止方法


```shell
service shadowsocks start # 启动
```
```shell
service shadowsocks stop # 停止
```
```shell
service shadowsocks restart # 重启
```
```shell
service shadowsocks status # 状态
```

# 搭建SSR服务器
此处注意：SS服务器和SSR服务器只需要搭一个。
```shell
wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocksR.sh

chmod +x shadowsocksR.sh

./shadowsocksR.sh 2>&1 | tee shadowsocksR.log
```
根据需要选择，不懂的话直接选1，或者默认回车。下面会提示你输入你的 SSR SERVER 的密码和端口。不输入就是默认。跑完命令后会出来你的 SSR 客户端的信息。

全部选择完毕后，当出现如下命令就说明安装成功了
```shell
Congratulations, ShadowsocksR server install completed!
Your Server IP :IP
Your Server Port :端口
Your Password :密码
Your Protocol :协议
Your obfs :混淆
Your Encryption Method:your_encryption_method

Welcome to visit:https://shadowsocks.be/9.html
Enjoy it!
```

# 获取客户端
关注臭大佬公众号，回复“墙”，获取各种系统的客户端。
![](https://www.choudalao.com/uploads/20200508/5eb4cc886b061.jpg)