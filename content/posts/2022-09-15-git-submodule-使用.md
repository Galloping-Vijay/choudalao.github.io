---
title: "git submodule 使用"
date: 2022-09-15T16:59:11+08:00
updated: 2026-02-23T08:05:47+08:00
author: "臭大佬"
categories: [Go]
description: "git submodule 使用"
cover: "https://www.choudalao.com/uploads/20220915/pe5EFHmA8Jac0LkxvD2BjF3JJezVPSJHppze6g4o.jpeg"
click: 3247
---

# 前言
像工具类这种，很多项目都是通用的，我们可以把它提取出来放一个仓库，然后通过git子模块的方式引入当各个项目中，这样就可以减少很多重复的代码了。

# 使用
首先，假设我们有一个子模块项目`https://gitee.com/Galloping-Vijay/go-wjf-tools.git`,里面放着很多通用的工具方法，现在我们要把它引入到我们的`go`项目中来。

#### 添加子仓库
```go
git submodule add [项目地址] [存放目录]
```
```go
git submodule add https://gitee.com/Galloping-Vijay/go-wjf-tools.git ./submodule/wjf-tools
```

` git submodule add https://gitee.com/Galloping-Vijay/go-wjf-tools.git ./submodule/wjf-tools`,这条命令的意思是拉取项目，并它代码放在`./submodule/wjf-tools`目录下。

![](https://www.choudalao.com/uploads/20220915/20220915163300vbfrBt.png)

执行完会多出一个目录，同时会有个`.gitmodules`文件，该配置文件保存了项目 URL 与已经拉取的本地目录之间的映射：

如果有多个子模块，该文件中就会有多条记录。 要重点注意的是，该文件也像 .gitignore 文件一样受到（通过）版本控制。 它会和该项目的其他部分一同被拉取推送。 这就是克隆该项目的人知道去哪获得子模块的原因。

#### 更新子模块
当子模块代码有更新时，可以到子模块目录下拉取代码，也可以在主项目根目录下执行如下命令来取：
```go
// 主模块跟目录执行
git submodule update --remote
```

#### 调用
我们拉取子模块后，可能有些小伙伴不知道怎么调用子模块，
在调用的时候需要注意，使用`go mod`引用本地开发的代码，需要在`go.mod`中做替换。
```go
module wjfcms

go 1.18

replace gitee.com/Galloping-Vijay/go-wjf-tools => ./submodule/wjf-tools
```

然后我们在`index.go`引入
```go
package main

import (
	"fmt"
	"gitee.com/Galloping-Vijay/go-wjf-tools/tool"
)

func main() {
	s := tool.StrToSlices("32,56,8")
	fmt.Println(s)
}
```

运行报如下错误，

~~index.go:5 : 2: module gitee.com/Galloping-Vijay/go-wjf-tools provides package gitee.com/Galloping-Vijay/go-wjf-tools/tool and is replaced but not required; to add it:
        go get gitee.com/Galloping-Vijay/go-wjf-tools~~

引入就行
```go
 go get gitee.com/Galloping-Vijay/go-wjf-tools
```

再次使用就OK了。

*go run .\index.go
[32 56 8]*

#### 删除子模块

```go
rm -rf 子模块目录 删除子模块目录及源码
vi .gitmodules 删除项目目录下.gitmodules文件中子模块相关条目
vi .git/config 删除配置项中子模块相关条目
rm .git/module/* 删除模块下的子模块目录，每个子模块对应一个目录，注意只删除对应的子模块目录即可
```
执行完成后，再执行添加子模块命令即可，如果仍然报错，执行如下：
```go
git rm --cached 子模块名称
```