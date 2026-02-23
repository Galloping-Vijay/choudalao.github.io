---
title: "借助 golang-set 来判断切片中是否存在某个元素"
date: 2023-01-04T10:01:10+08:00
updated: 2026-02-23T09:17:29+08:00
author: "臭大佬"
categories: [Go]
description: "借助 golang-set 来判断切片中是否存在某个元素"
cover: "https://www.choudalao.com/uploads/20230104/Pj5LusTm42FJTWoEZdN0XhrKSzrja0WhznPnpg57.jpeg"
click: 2922
---

# 代码

```go
package main

import (
	"fmt"

	mapset "github.com/deckarep/golang-set"
)

func main() {
	var sl = []interface{}{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
	s := mapset.NewSetFromSlice(sl)
	fmt.Println(s.Contains("m"))	// true
	fmt.Println(s.Contains("mm"))	// false
}
```