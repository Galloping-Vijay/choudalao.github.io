---
title: "go的viper包读取yml配置文件"
date: 2022-10-29T11:28:42+08:00
updated: 2026-02-23T08:33:21+08:00
author: "臭大佬"
categories: [Go]
description: "go的viper包读取yml配置文件"
cover: "https://www.choudalao.com/uploads/20221029/eoWMKYwxXubvJbYCvHgaDp2G8OtscQJ4Gc3OdiIt.jpeg"
click: 2815
---

# 代码
```go
package main

import (
	"fmt"
	"github.com/spf13/viper"
	"os"
)

func main() {
	//获取当前项目目录
	work, _ := os.Getwd()
	// 读取当前文件夹下的 settings.yml文件
	//设置文件名和文件后缀
	viper.SetConfigName("settings")
	viper.SetConfigType("yml")
	//配置文件所在的文件夹
	viper.AddConfigPath(work)
	err := viper.ReadInConfig()
	if err != nil {
		panic(err)
	}
	//获取全部文件内容
	fmt.Println("all settings: ", viper.AllSettings())
	//根据内容类型，解析出不同类型
	fmt.Println(viper.GetString("settings.logger.path"))
}
```
settings.yml 文件内容如下
```go
settings:
  logger:
    # 日志存放路径
    path: temp/logs
    # 日志输出，file：文件，default：命令行，其他：命令行
    stdout: '' #控制台日志，启用后，不输出到文件
    # 日志等级, trace, debug, info, warn, error, fatal
    level: trace
    # 数据库日志开关
    enableddb: false
```
结果

>  all settings: map[settings:map[logger:map[enableddb:false level:trace path:temp/logs stdout:]]]
> temp/logs