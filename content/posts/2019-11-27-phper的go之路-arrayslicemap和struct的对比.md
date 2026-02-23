---
title: "PHPer的Go之路  -- array、slice、map和struct的对比"
date: 2019-11-27T23:26:38+08:00
updated: 2026-02-23T08:09:39+08:00
author: "臭大佬"
categories: [Go]
description: "这篇讲解go语言中数据存储类型array、slice、map和struct，要清楚它们那些是值传递，那些是指针传递（也就是引用类型），这对后面的数据处理非常重要！"
cover: "https://www.choudalao.com/uploads/20191127/KNmXYhcHtURoAOGdyRW2KD10nWaj7aNFaJNvPfeS.jpeg"
click: 3332
---

# 数组Array
1、数组长度也是类型的一部分，因此具有不同长度的数组为不同类型；
2、注意区分指向数组的指针和指针数组；
3、数组在Go中为值类型；（这是和Java非常不同的一点）
4、数组之间可以使用 == 或者 != 进行比较，但不可以使用 < 或 >
5、可以使用new来创建数组，此方法返回一个指向数组的指针；
6、Go支持多维数组

```go 
package main

import "fmt"

func main() {
	arrayTest()
}

func arrayTest() {
	//先声明，后赋值
	var a [2] string
	a[0] = "hello"
	a[1] = "world"
	fmt.Println(a[0], a[1])
	fmt.Println(a)
	//声明并赋值
	prime := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(prime)
}

```
![](https://www.choudalao.com/uploads/20191127/20191127225947rWabW3.png)

区分指向数组的指针和指针数组:

```go
//可以利用...不指定数组长度
	a:=[...]int{9:1}
	//指向数组的指针
	var p *[10]int=&a
	fmt.Println(p)

	x,y :=1,2
	//指针数组
	b:=[...]*int{&x,&y}
	fmt.Println(b)
```
> λ go run gogo.go
&[0 0 0 0 0 0 0 0 0 1]
[0xc000012168 0xc000012180]

# 切片slice
1、其本身并不是数组，它指向底层的数组。（切片为引用类型）；
2、作为变长数组的替代方案，可以关联底层数组的局部或全部；
3、可以直接创建或从底层数组获取生成；
4、一般使用make()创建，使用len()获取元素个数，cap()获取容量；
5、如果多个slice指向相同的底层数组，其中一个的值改变会影响全部。

### 创建方式

```go
//创建一个切片,跟数组相比没有规定长度
	p:=[]int{2,3,5,7,11,13}
	fmt.Println("p==",p)
	for i := 0; i < len(p); i++ {
		fmt.Println(i,p[i])
	}
	//利用make创建包含3个元素，容量为10的slice
	//提前分配容量10是为了增加元素而在此分配内存
	s1:=make([]int,3,10)
	fmt.Println(len(s1),cap(s1))
	//注意打印出来的时候只包含三个元素
	fmt.Println(s1)
```
> λ go run gogo.go      
p== [2 3 5 7 11 13]   
0 2                   
1 3                   
2 5                   
3 7                   
4 11                  
5 13                  
3 10                  
[0 0 0]               

### Reslice的理解：
1、Reslice时索引以被slice的切片为准；
2、索引不可以超过被slice的切片的容量cap()值；
3、索引越界不会导致底层数组的重新分配而引发错误。

```go
a:=[]byte{'a','b','c','d','e','f','g','h','i','j','k'}
	//前闭后开
	sa:=a[2:5]
	//转化为字符串
	fmt.Println(string(sa))
	fmt.Println(len(sa),cap(sa))
	//从sa中取出元素--reslice功能
	sb:=sa[3:5]
	//打印出来的是fg，但是sa中并没有fg，这是为什么呢？
	//sa的本质是指针，指向的数组的地址,它会包含从3到最后一个元素的地址。（就像图中阴影部分的元素）
	fmt.Println(string(sb))
```
> λ go ru
cde    
3 9    
fg     

### Append的理解：
1、可以在slice尾部追加元素；
2、可以将一个slice追加在另一个slice尾部；
3、如果最终长度未超过追加到slice的容量则返回原始slice，如果超过追加到的slice的容量则将重新分配数组并拷贝原始数据。

```go
s1:=make([]int,3,6)
//按格式输出
fmt.Printf("%p\n",s1)
s1 =append(s1,1,2,3)
fmt.Printf("%v %p\n",s1,s1)
s1 =append(s1,1,2,3)
fmt.Printf("%v %p\n",s1,s1)
```
> λ go run gogo.go
0xc00000e360
[0 0 0 1 2 3] 0xc00000e360
[0 0 0 1 2 3 1 2 3] 0xc000046060

# 集合map
1、类似其它语言中哈希表或者字典，以key-value形式存储数据；
2、Key必须是支持==或!=比较运算的类型，不可以是函数、map或slice；
3、Map查找比线性搜索快很多，但比使用索引访问数据的类型慢100倍；
4、Map使用make()创建，支持:=这种简写方式，make([keyType] valueType,cap)，cap表示容量，可省略；超出容量时会自动扩容，但尽量提供一个合理的初始值；使用len()获取元素的个数。
5、键值对不存在时自动添加，使用delete()删除某键值对，比如delete(m,1)；
6、使用for range对map和slice进行迭代操作。

### 创建

```go
//声明一个map，int是key类型，string是value类型
	var m map[int]string
	//初始化map
	m =map[int]string{}
	fmt.Print(m)

	//使用make创建一个map
	n:=make(map[int]string)
	n[1]="OK"
	a:=n[1]
	fmt.Println(n)
	fmt.Print(a)
```
> λ go run gogo.go        
map[]map[1:OK]          
OK                      

### range操作

```go
//创建一个slice
sm:=make([]map[int]string,5)
//对一个slice进行迭代,并对slice中的map进行初始化（i对代表的索引下标，v是代表对应的值）
for i:= range sm {
//注意是通过索引去改变map中的值，否则只是普通的值拷贝
sm[i] =make(map[int]string,1)
sm[i][1] ="OK"
fmt.Println(sm[i])
}
fmt.Println(sm)
```
> λ go run gogo.go
map[1:OK]
map[1:OK]
map[1:OK]
map[1:OK]
map[1:OK]
[map[1:OK] map[1:OK] map[1:OK] map[1:OK] map[1:OK]]

# 结构体struct

1、Go中的struct与C中的struct非常相似，并且Go没有class，使用type<Name>struct{} 定义结构，名称遵循可见性规则；
2、支持指向自身的指针类型成员，支持匿名结构，可用作成员或定义成员变量，匿名结构也可以用于map值；
3、可以使用字面值对结构进行初始化，允许直接通过指针来读写结构成员；
4、相同类型的成员可进行直接拷贝赋值；
5、支持==与!=比较运算，但不支持 > 或 < ；
6、支持匿名字段，本质上是定义了以某种类型名为名称的字段；
7、可以使用匿名字段指针；
8、嵌入结构作为匿名字段看起来像继承，但不是继承。

```go
package main

import "fmt"
type person struct {
	Name string
	Age int
}
func main() {
	a:=person{}
	a.Name ="臭大佬"
	a.Age =26
	fmt.Print(a)
}
```
> λ go run gogo.go
{臭大佬 26}

### 值传递

```go
package main
import "fmt"
type person struct {
	Name string
	Age int
}
func main() {
	//字面值初始化
	a:=person{
		Name:"臭大佬",
		Age:26,
	}
	fmt.Println(a)
	A(a)
	fmt.Println(a)
}
func A(p person) {
	p.Age = 12
	fmt.Println("A:",p)
}
```
> λ go run gogo.go
{臭大佬 26}
A: {臭大佬 12}
{臭大佬 26}