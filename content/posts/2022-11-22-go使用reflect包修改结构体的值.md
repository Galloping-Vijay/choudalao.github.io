---
title: "go使用reflect包修改结构体的值"
date: 2022-11-22T10:09:29+08:00
updated: 2026-02-23T07:08:24+08:00
author: "臭大佬"
categories: [Go]
description: "go使用reflect包修改结构体的值"
cover: "https://www.choudalao.com/uploads/20221122/Sn2Qx5tdlboJOfPkJ9gELtp7OK3afQeaNeFSxIa7.jpeg"
click: 2571
---

# 问题
有个方法是通用的,参数是Interface,可以丢进来任何结构体,这时候,就不知道 interface 里面有哪些成员了,假设我们知道 interface 里面有 ShopId 字段,并且我们要修改它的值,该怎么操作呢?

# 方法
直接上代码
```go
package test

import (
	"reflect"
	"testing"
)

func TestA(t *testing.T) {
	type shop struct {
		ShopId int64
		Name   string
	}
	d := &shop{
		ShopId: 2,
		Name:   "测试一下",
	}
	var e int64 = 40
	changeValue(d, e)
	t.Log(d)
}

// changeValue 修改 s 的 shopId 的值
func changeValue(s interface{}, value int64) {
	// 使用ValueOf()获取到变量的Value对象
	ref := reflect.ValueOf(s)
	// value是一个指针,这里获取了该指针指向的值,相当于value.Elem()
	ref = reflect.Indirect(ref)
	// 如果是结构体,才往下走
	if ref.Kind() != reflect.Struct {
		return
	}
	//获取结构体shop中的ShopId字段的值
	val := ref.FieldByName("ShopId")
	// 要先判断是否有这个值,如果类型为 reflect.Invalid,则不存在这个成员
	// val.Kind() 获取对象或者变量的类型, 如果类型不为 Invalid ,则赋值
	if val.Kind() == reflect.Int64 {
		// ShopId 的值设为 value
		val.SetInt(value)
	}
}

```
结果
*=== RUN   TestA
    a_test.go: 19: &{40 测试一下}
--- PASS: TestA (0.00s)
PASS*

如果不存在要修改的成员名会不会出问题呢?我们把结构体的 ShopId 改成 ShopIds 看一下结果:

```go
package test

import (
	"reflect"
	"testing"
)

func TestA(t *testing.T) {
	type shop struct {
		ShopIds int64
		Name    string
	}
	d := &shop{
		ShopIds: 2,
		Name:    "测试一下",
	}
	var e int64 = 40
	changeValue(d, e)
	t.Log(d)
}

// changeValue 修改 s 的 shopId 的值
func changeValue(s interface{}, value int64) {
	// 使用ValueOf()获取到变量的Value对象
	ref := reflect.ValueOf(s)
	// value是一个指针,这里获取了该指针指向的值,相当于value.Elem()
	ref = reflect.Indirect(ref)
	//获取结构体shop中的ShopId字段的值
	val := ref.FieldByName("ShopId")
	// 要先判断是否有这个值,如果类型为 reflect.Invalid,则不存在这个成员
	// val.Kind() 获取对象或者变量的类型, 如果类型不为 Invalid ,则赋值
	if val.Kind() != reflect.Invalid {
		// ShopId 的值设为 value
		val.SetInt(value)
	}
}

```
结果
*=== RUN   TestA
    a_test.go: 19: &{2 测试一下}
--- PASS: TestA (0.00s)
PASS*

并没有出来恐慌或者错误.

# 反射结构体

```go
package main

import (
	"fmt"
	"reflect"
)

type Order struct {
	orderId string `json:"order_id"`
	price   int    `json:"price"`
}

func main() {
	type InfoData struct {
		ShopUuid string `json:"shopUuid"`
		UserUuid string `json:"userUuid"`
		Types    int64  `json:"types"`
		Status   int64  `json:"status"`
	}
	d := InfoData{
		"Sfx135", "sd54", 1, 2,
	}
	// 返回原始值的值信息
	v := reflect.ValueOf(d)
	if v.Kind() != reflect.Struct {
		return
	}
	// 获得结构体成员的详细信息
	f := reflect.TypeOf(d)
	for i := 0; i < f.NumField(); i++ {
		field := f.Field(i)
		// field.Name 可以获取key
		// v.Field(i).String() 获取对应的值
		switch field.Name {
		case "ShopUuid":
			fmt.Printf("key:%s val:%s type: %v\n", field.Name, v.Field(i).String(), field.Type)
		case "UserUuid":
			fmt.Printf("key:%s val:%s type: %v\n", field.Name, v.Field(i).String(), field.Type)
		case "Status":
			fmt.Printf("key:%s val:%d type: %v\n", field.Name, v.Field(i).Int(), field.Type)
		}
	}
	// 取字段
	vv := reflect.ValueOf(&d)
	vv = vv.Elem()
	vf := vv.FieldByName("ShopUuid")
	if vf.Kind() == reflect.String {
		// 原值
		fmt.Printf("原值:%v\n", vf.String())
		// 修改值
		vf.SetString("SW56")
		fmt.Printf("新值:%v\n", vf.String())
	}
	fmt.Print(d)
}
```
结果:
*key:ShopUuid val:Sfx135 type: string
key:UserUuid val:sd54 type: string
key:Status val:2 type: int64
原值:Sfx135
新值:SW56
{SW56 sd54 1 2}*

# 指针结构体
```go
package main

import (
	"fmt"
	"reflect"
)

type User struct {
	Name     string `json:"name"`
	Age      int    `json:"age"`
	Location string `json:"location"`
}

func main() {
	user := &User{
		Name:     "Alice",
		Age:      25,
		Location: "New York",
	}
// 获取指针类型
	userType := reflect.TypeOf(user)
	// 解引用指针获取结构体类型
	structType := userType.Elem()
// 遍历结构体字段
	for i := 0; i < structType.NumField(); i++ {
		field := structType.Field(i)
		// 获取字段名
		name := field.Name
		// 获取字段标签
		tag := field.Tag.Get("json")

		value := reflect.ValueOf(user).Elem().FieldByName(name)
		// 获取类型
		valueType := value.Type()
		// 获取字段值
		fieldValue := value.Interface()
		// 获取 Kind
		kind := valueType.Kind()

		fmt.Printf("Field Name: %s, Tag: %s, Value: %v, Type: %v; Kind:%v\n", name, tag, fieldValue, valueType, kind)
	}
}
```
结果:
Field Name: Name, Tag: name, Value: Alice, Type: string; Kind:string
Field Name: Age, Tag: age, Value: 25, Type: int; Kind:int
Field Name: Location, Tag: location, Value: New York, Type: string; Kind:string