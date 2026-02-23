---
title: "PHPer的Go之路 -- Go 项目基本工程管理示例"
date: 2019-11-12T14:14:55+08:00
updated: 2026-02-23T13:55:05+08:00
author: "臭大佬"
categories: [Go]
description: "Go 项目基本工程管理示例"
cover: "https://www.choudalao.com/uploads/20191112/GuVh5rhQ0RUnxM2pc08NSyEC0CGiHgNvVj7aQCb3.jpeg"
click: 3707
---

# 编写计算器工程源码

新建一个src目录存放代码,由于我用到了git管理,所以会有一些git库管理的文件,这里可以忽略,我们主要关心src里面的内容.

我们假设这个工程被划分为两个部分：

可执行程序，名为 calc，内部只包含一个 calc.go 文件，该文件是计算器程序的入口文件；
算法库，名为 simplemath，每个计算操作对应于一个同名的 Go 文件，比如 add.go 用于计算加法运算。
这样，对应的工程目录组织应该如下所示：

![](https://www.choudalao.com/uploads/20191112/20191112111403GTjm5a.png)

然后我们来编写每个 Go 文件的源代码，src/calc/calc.go 的源码如下：

```go
package main

// 引入其它包
import (
	"fmt"
	"os"
	"simplemath"
	"strconv"
)

// 定义一个用于打印程序使用指南的函数
var Usage = func() {
	fmt.Println("USAGE: calc command [arguments] ...")
	fmt.Println("\nThe commands are:\n\tadd\t计算两个数值相加\n\tsqrt\t计算一个非负数的平方根")
}

// 程序入口函数
func main() {
	/*
	 * 用于获取命令行参数，注意程序名本身是第一个参数，
	 * 比如 calc add 1 2 这条指令，第一个参数是 calc
	 */
	args := os.Args
	// 除程序名本身外，至少需要传入两个其它参数，否则退出
	if args == nil || len(args) < 3 {
		Usage()
		return
	}

	// 第二个参数表示计算方法
	switch args[1] {
	// 如果是加法的话
	case "add":
		// 至少需要包含四个参数
		if len(args) != 4 {
			fmt.Println("USAGE: calc add <integer1><integer2>")
			return
		}
		// 获取待相加的数值，并将类型转化为整型
		v1, err1 := strconv.Atoi(args[2])
		v2, err2 := strconv.Atoi(args[3])
		// 获取参数出错，则退出
		if err1 != nil || err2 != nil {
			fmt.Println("USAGE: calc add <integer1><integer2>")
			return
		}
		// 从 simplemath 包引入 Add 方法进行加法计算
		ret := simplemath.Add(v1, v2)
		// 打印计算结果
		fmt.Println("Result: ", ret)
	// 如果是计算平方根的话
	case "sqrt":
		// 至少需要包含三个参数
		if len(args) != 3 {
			fmt.Println("USAGE: calc sqrt <integer>")
			return
		}
		// 获取待计算平方根的数值，并将类型转化为整型
		v, err := strconv.Atoi(args[2])
		// 获取参数出错，则退出
		if err != nil {
			fmt.Println("USAGE: calc sqrt <integer>")
			return
		}
		// 从 simplemath 包引入 Sqrt 方法进行平方根计算
		ret := simplemath.Sqrt(v)
		// 打印计算结果
		fmt.Println("Result: ", ret)
	// 如果计算方法不支持，打印程序使用指南
	default:
		Usage()
	}
}

```
这段代码相信对于有 PHP 编程基础的人来说，都不困难，需要注意的是在 Go 语言中，**通过 var 来声明变量**，**并且可以将匿名函数赋值给变量以便后续使用**，此外，还可以通过 **:= 运算符来声明并初始化变量**，这个时候，不需要通过 var 声明该变量，比如  args := os.Args 就是如此，需要明确的是，虽然看起来有点和动态语言声明变量类似，但与 PHP 不同，**Go 是强类型语言**，只不过底层会自动根据赋值判断对应变量的类型，如果你试图声明一个没有初始化值的变量，就会报错，关于 Go 语言变量声明和初始化我们后面还会详细介绍，这里简单了解下即可。

接下来，我们编辑 src/simplemath/add.go 和 src/simplemath/sqrt.g 代码如下:

add.go

```go
package simplemath

func Add(a int, b int) int {
	return a + b
}
```
sqrt.go

```go
package simplemath

import "math"

func Sqrt(i int) int {
    v := math.Sqrt(float64(i))
    return int(v)
}

```
# 配置 GOPATH 环境变量

查看go的相关环境参数

```go
go env
```

这里几个比较关键的变量 GOPATH 和GOROOT；
GOPATH是go get指令默认下载和安装包的位置，通过go get指令，获取go的包，默认下载到GOPATH所指示的目录中。
GOROOT是go安装的位置，也是go可执行文件的位置，也就是说，当我们命令行中打出go的指令时，系统能不能准确调用go的可执行文件 

## win10下：

![](https://www.choudalao.com/uploads/20191112/20191112114556AG5Kcv.png)

我们发现GOPATH不是我们的项目路径，这时候我们需要设置环境变量GOPATH，如图所示：

![](https://www.choudalao.com/uploads/20191112/20191112115043FNGjZD.png)

![](https://www.choudalao.com/uploads/20191112/20191112115121hprzbm.png)

确定关闭窗口后，需要重启cmd工具，重新打开后输入 go env 如下：

![](https://www.choudalao.com/uploads/20191112/20191112115333lx411H.png)

## ubuntu下

![](https://www.choudalao.com/uploads/20191112/20191112122439EBwiwL.png)

### 配置环境变量

默认的时候，GOPATH是没有配置好的，那么我们怎么修改这些环境变量呢 
首先，我们可以按照自己的意愿，在一个位置建一个文件夹，比如

```
mkdir /www/wwwroot/default/goCode
```

然后，配置环境变量有三个方法：

#### 最根本的方法就是修改/etc/profile文件

```
sudo vim /etc/profile
```

> *注意这里必须要sudo，因为系统目录下的文档不允许任意修改的 
在最后添加export GOPATH=/www/wwwroot/default/goCode 
这个办法修改是对所有的用户都生效的,修改之后要重启就会另修改生效

#### 这个办法也可以，修改用户目录下的.profile文件

比如这里是/home/ubuntu/.profile 
通过vim /home/ubuntu/.profile打开之后就能修改了 
修改的方法跟第一种是一样的，就是再最后添加 
export GOPATH=/www/wwwroot/default/goCode

#### 临时性的起作用，只有本次生效，当你关闭terminal之后，不再生效

直接在命令行中 
ubuntu@VM-0-9-ubuntu:~$ export GOPATH=/www/wwwroot/default/goCode

##### 这里演示第一种方法

![](https://www.choudalao.com/uploads/20191112/20191112134021tD1zk5.png)

使文件立刻生效，

```
source /etc/profile
```


为了能够构建这个工程，需要先把这个工程的根目录加入到环境变量 GOPATH 中，假设计算器项目根目录 calc 目录位于 ~/go 下，如果是基于 GoLand 进行开发的话，可以通过「首选项（Preferences）->Go->GOPATH」（Windows 的话对应的路径是 File->Settings->Go->GOPATH）界面来进行设置：

![](https://www.choudalao.com/uploads/20191112/20191112121115BVlxDz.png)

# 构建 Go 工程

现在我们开始构建工程。假设我们希望把生成的可执行文件放到我们设置的GOPATH目录下的calc/bin目录中，进入到bin目录。执行指令如下：

```go
cd bin

go build calc
```

## win10下

![](https://www.choudalao.com/uploads/20191112/201911121212437z8GWy.png)

这样就会在bin下生成执行文件calc

![](https://www.choudalao.com/uploads/20191112/2019111212142696hsFW.png)

现在我们就可以执行calc文件了

```go
calc  help
```

![](https://www.choudalao.com/uploads/20191112/20191112121625eUJtuG.png)

![](https://www.choudalao.com/uploads/20191112/20191112121810DHR4F7.png)

## ubuntu下

ubuntu下需要注意权限问题，

![](https://www.choudalao.com/uploads/20191112/20191112140628mXEWSC.png)

运行如下命令（这边和上面win有点不一样，不知道为啥需要用 ./calc 才能运行，这边先记录一下，后期研究）

```
./calc help
```

![](https://www.choudalao.com/uploads/20191112/20191112140939xRCAYr.png)

![](https://www.choudalao.com/uploads/20191112/20191112141126TM0SNh.png)

# 注意

如果在运行的时候报如下错误

```
can't load package: package calc: cannot find package "calc" in any of:
```
![](https://www.choudalao.com/uploads/20191112/20191112141237urjEJN.png)

可能存在的问题是：
1. $PATHON未配置；
1. $PATHON配置了但未生效，需要重启erminal 窗口；
1. 如果是linux下，可能是权限问题呢，需要注意权限问题；