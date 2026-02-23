---
title: "$GOPATH not set. For more details see: go help gopath"
date: 2020-08-06T14:14:50+08:00
updated: 2026-02-23T16:55:19+08:00
author: "臭大佬"
categories: [Go]
description: "$GOPATH not set. For more details see: go help gopath"
cover: "https://www.choudalao.com/uploads/20200806/fQlA8U2r9Tkhca9pgTUIMATonseNcB5fSBoUNzQS.jpeg"
click: 3782
---

# 问题
今天在`ubuntu`上安装 `go` 依赖时报错，执行命令如下：

```shell
sudo go get github.com/gorilla/mux
```
> $GOPATH not set. For more details see: go help gopath

![](https://www.choudalao.com/uploads/20200806/20200806135704FeBsN2.png)


# 分析
因为`sudo`我们使用了`root`的环境，而我们没有在`root`的`.bashrc`文件中设置`GOPATH`。

查看环境配置：

```shell
go env
```

![](https://www.choudalao.com/uploads/20200806/20200806134703bAQaLg.png)

需要注意的是`GOPATH`变量的值`GOPATH=/www/wwwroot/default/goCode`，GOPATH是`go get`指令默认下载和安装包的位置，通过`go get`指令，获取`go`的包，默认下载到`GOPATH`所指示的目录中。

# 解决方案
###方式一：直接go get xxx即可。

这种方式需要设置目录权限。到`GOPATH`目录下的src -> github.com 目录下：

```shell
sudo chmod -R 777 ./*
```

然后再安装相应的包

```shell
go get github.com/gorilla/mux
```

###方式二：在/etc/profile文件中添加GOPATH变量。

修改`/etc/profile`文件

```shell
sudo vim /etc/profile
```

在文件最后面加上：`export GOPATH=/www/wwwroot/default/goCode
`

![](https://www.choudalao.com/uploads/20200806/20200806140832IgGPc6.png)

编辑完成后在终端运行如下命令，使文件立刻生效，

```shell
source /etc/profile
```

###方式三：sudo env GOPATH=/opt/go go get github.com/nsf/gocode，命令里面手动给出GOPATH变量值。

举个拉取 `go-sql-driver`的栗子：

```shell
sudo env GOPATH=/www/wwwroot/default/goCode go get github.com/go-sql-driver/mysql
```

以上三种方式都可以解决`$GOPATH not set `问题，这样就可以拉取需要的`go`依赖包了。