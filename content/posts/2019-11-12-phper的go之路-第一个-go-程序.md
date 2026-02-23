---
title: "PHPer的Go之路 --  第一个 Go 程序"
date: 2019-11-12T09:50:43+08:00
updated: 2026-02-23T10:17:56+08:00
author: "臭大佬"
categories: [Go]
description: "第一个 Go 程序"
cover: "https://www.choudalao.com/uploads/20191112/2dvAOmHP6prncj0GLTHRvOLMMkQ3F3RkgUat3dnP.jpeg"
click: 3342
---

# 安装 Go
使用 Go 语言之前，首先要安装 Go。Go 为 Linux、Mac、Windows 等不同的平台分别提供了相应的安装包：[点击下载](https://golang.google.cn/doc/install "点击下载")，根据自己的操作系统选择对应的安装包点击下载，然后按照引导流程安装即可。

安装完成后，通过 go version 查看 Go 语言的版本来验证是否安装成功，以 Winsowa 为例，对应的版本信息如下：

`go version`

![](https://www.choudalao.com/uploads/20191112/20191112093453YoQHTN.png)

# 第一个 Go 程序
推荐使用[Goland](https://www.jetbrains.com/go/ "Goland")作为开发工具,点击下载[Goland](https://www.jetbrains.com/go/ "Goland"),

和 PHP 源码存放在 .php 文件类似，Go 语言源码都是存放在 .go 文件中，接下来，我们编写hello.go 源码如下：

我们在本地创建一个目录专门存放go代码,比如 goCode,然后用编辑器新建一个 index.go文件,里面的代码如下:
```go
package main

import "fmt"

func main(){
	fmt.Println("Hello, World!")
}
```
![](https://www.choudalao.com/uploads/20191112/20191112093824A5H4qp.png)

# 代码解读

和 Java 类似，Go 使用包作为基本单位来管理代码（可以类比为 PHP 中的命名空间），**每个 Go 源代码文件的开头都是一个 package 声明**，表示该文件中 Go 代码所属的包。包是 Go 语言里最基本的分发单位，也是工程管理中依赖关系的体现。**要生成 Go 可执行程序，必须建立一个名字为 main 的包**，并且在该包中包含一个叫 main() 的主函数，该函数是 Go 可执行程序的执行起点，这一点和 C 语言和 Java 语言很像，后续编译 Go 项目程序的时候也要从包含 main 包的文件开始。Go 语言的 main() 函数不能带参数，也不能定义返回值。

在包声明之后，是一系列的 import 语句，用于导入该程序所依赖的包（可类比为 PHP 中通过 use 引入其它命名空间的类来理解）。由于本示例程序用到了Println() 函数，所以需要导入该函数所属的 fmt 包。

有一点需要注意，与 Java 和 PHP 不同，**在 Go 语言中，不得包含在源代码文件中没有用到的包，否则 Go 编译器会报编译错误。**这与下面的强制函数左花括号 { 的放置位置以及之后会提到的函数名的大小写规则，均体现了 Go 语言在语言层面解决软件工程问题的设计哲学。

所有 Go 函数（包括在面向对象编程中会提到的类型成员函数）都以关键字 func 开头（这一点与 PHP、Java、JavaScript 等语言通过 function 定义函数不同）。另外在 Go 函数中，**左花括号 { 必须函数定义行的末尾，不能另起一行，否则 Go 编译器报告编译错误：**

```go
syntax error: unexpected semicolon or newline before {
```
另外，与 Python、JavaScript 类似，Go 程序并不要求在每个语句后面加上分号表示语句结束，这也是与 PHP、Java 等语言的不同之处。

最后，函数体很简单，就是调用 fmt 包提供的 Println 函数打印「hello,world」这行字符串，Go 语言可以直接通过包名+「.」号引用定义在该包中的函数。

# 编译 & 运行程序

对以上代码含义有了大致的了解后，我们接下来要编译并运行第一个 Go 程序，和 PHP 不同，Go 语言是编译型的静态语言（和 Java、C 一样），在运行 Go 程序之前，先要将其编译成二进制可执行文件，**我们可以通过 Go 语言提供的 go build 命令对 Go 程序进行编译**，然后运行编译后的可执行文件执行 Go 程序代码：

```go
go build index.go
```
![](https://www.choudalao.com/uploads/20191112/20191112094714DDLEev.png)

我们可以通过 go run xx.go 命令来达到同样的效果，该命令将编译和执行指令合二为一，会在编译之后立即执行相应的可执行文件显示执行结果：

```go
go run index.go
```
![](https://www.choudalao.com/uploads/20191112/20191112094812v7FiGF.png)