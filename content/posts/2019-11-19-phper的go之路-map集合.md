---
title: "PHPer的Go之路 -- Map(集合)"
date: 2019-11-19T22:04:54+08:00
updated: 2026-02-22T09:43:58+08:00
author: "臭大佬"
categories: [Go]
description: "PHP 数组包含索引数组和关联数组，PHP 中的索引数组即对应 Go 语言的数组和切片类型，PHP 中的关联数组即对应 Go 语言中的字典类型（map）。"
cover: "https://www.choudalao.com/uploads/20191119/eQAuI1YPQQHlq7J2P6B6ahzKwnboNs4xTPyIbOtH.gif"
click: 3082
---

Map 是一种无序的键值对的集合。Map 最重要的一点是通过 key 来快速检索数据，key 类似于索引，指向数据的值。

Map 是一种集合，所以我们可以像迭代数组和切片那样迭代它。不过，Map 是无序的，我们无法决定它的返回顺序，这是因为 Map 是使用 hash 表来实现的。
# 声明
&nbsp;
```go
//其中，testMap 是声明的字典变量名，string 是键的类型，int 则是其中所存放的值类型。
var testMap map[string]int
```
&nbsp;
# 查找元素、删除和遍历Map
从字典中查找指定键时，会返回两个值，判断是否在字典中成功找到指定的键，不需要检查取到的值是否为 nil，只需查看第二个返回值 ok，这是一个布尔值，如果查找成功，返回 true，否则返回 false，配合 := 操作符，让你的代码没有多余成分，看起来非常清晰易懂。
```go
	//声明
	var testMap map[string]string
	//再使用make函数创建一个非nil的map，nil map不能赋值
	testMap = make(map[string]string)
	//给已声明的map赋值
	//map插入key - value对,各个国家对应的首都
	testMap [ "France" ] = "巴黎"
	testMap [ "Italy" ] = "罗马"
	testMap [ "Japan" ] = "东京"
	testMap [ "India " ] = "新德里"

	//遍历写法一
	for key, value := range testMap {
		fmt.Println(key, "首都是",value)
	}
	////遍历写法二
	//for _, value := range testMap {
	//	fmt.Println(value)
	//}
	////遍历写法三
	//for key := range testMap {
	//	fmt.Println(key)
	//}

	/*删除元素*/
	delete(testMap, "France")
	fmt.Println("法国条目被删除")
	//查看元素在集合中是否存在
	//如果确定是真实的,则存在,否则不存在
	value, ok := testMap["France"]
	if ok { // 找到了
		// 处理找到的value
		fmt.Println("France 的首都是", value)
	}else{
		fmt.Println("France 的首都不存在")
	}
```
![](https://www.choudalao.com/uploads/20191119/20191119224759M1hUdp.png)