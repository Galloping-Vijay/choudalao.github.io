---
title: "PHPer的Go之路 -- http请求"
date: 2020-07-22T15:59:25+08:00
updated: 2026-02-23T16:48:38+08:00
author: "臭大佬"
categories: [Go]
description: "http请求"
cover: "https://www.choudalao.com/uploads/20200722/iBMrD1fOCcIGuszBpvPh79uM02XPYqxTUdOsUIrv.jpeg"
click: 2859
---

```go
package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
)

const getUrl string = "http://www.choudalao.com"
const postUrl string = "http://www.choudalao.com/login"

/**
get 请求
*/
func getHttp() {
	resp, err := http.Get(getUrl)
	if err != nil {
		fmt.Printf("发起请求失败：%v", err)
		return
	}
	defer resp.Body.Close()
	io.Copy(os.Stdout, resp.Body)
}

/**
post 请求
*/
func postHttp() {
	resp, err := http.PostForm(postUrl, url.Values{"name": {"choudalao"}, "password": {"123456"}})
	if err != nil {
		// 处理错误
		return
	}
	if resp.StatusCode != http.StatusOK {
		// 处理错误
		return
	}
	defer resp.Body.Close()
	io.Copy(os.Stdout, resp.Body)
}

/**
可以设置请求头信息等
*/
func clientHttp() {
	// 初始化客户端请求对象
	req, err := http.NewRequest("GET", getUrl, nil)
	if err != nil {
		fmt.Printf("请求初始化失败：%v", err)
		return
	}
	// 添加自定义请求头
	req.Header.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
	// ... 其它请求头配置
	client := &http.Client{
		// ... 设置客户端属性
	}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("客户端发起请求失败：%v", err)
		return
	}
	defer resp.Body.Close()
	io.Copy(os.Stdout, resp.Body)
}
func main() {
	//getHttp()
	//postHttp()
	clientHttp()
}

```