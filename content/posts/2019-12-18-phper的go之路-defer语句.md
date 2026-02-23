---
title: "PHPer的Go之路 -- defer语句"
date: 2019-12-18T23:14:56+08:00
updated: 2026-02-23T12:18:53+08:00
author: "臭大佬"
categories: [Go]
description: "Go 语言的 defer 语句相当于 PHP 中析构函数和 finally 语句的功效，常用于定义兜底逻辑，如果一个函数定义了多个 defer 语句，则按照先进后出的顺序执行。"
cover: "https://www.choudalao.com/uploads/20191218/UkCsTBgQh8puC2YGcWwlfSEVq10NpVeEbawfyhu4.jpeg"
click: 3307
---

### 先进后出

Go 语言的 defer 语句相当于 PHP 中析构函数和 finally 语句的功效，常用于定义兜底逻辑，如果一个函数定义了多个 defer 语句，则按照先进后出的顺序执行。

```go
package main

import "fmt"

func main() {
	var whatever [5]struct{}

	for i := range whatever {
		defer fmt.Println(i)
	}
}
```

> λ go run defer.go    
4                    
3                    
2                    
1                    
0                    

![](https://www.choudalao.com/uploads/20191218/20191218225113wd2AKS.png)

### 如果函数里面有多条defer指令，他们的执行顺序是反序，即后定义的defer先执行。

```go
package main

import (
	"fmt"
)

func foo()  {
	defer fmt.Println("1111")
	defer fmt.Println("2222")
	defer fmt.Println("3333")
}

func main() {
	foo()
}
```

> λ go run defer.go
3333
2222
1111

![](https://www.choudalao.com/uploads/20191218/20191218225546LzmSfb.png)

### 计算时间点

defer函数的参数是在defer语句出现的位置做计算的，而不是在函数运行的时候做计算的，即所在函数结束的时候计算的。

```go
package main

import (
	"fmt"
)

func foo(n int) int {
	fmt.Println("n1=", n)
	defer fmt.Println("n=", n)//n就是100
	n += 100
	fmt.Println("n2=", n)
	return n
}

func main() {
	var i int = 100
	foo(i)
}
```

> λ go run defer.go
n1= 100
n2= 200
n= 100

![](https://www.choudalao.com/uploads/20191218/20191218225938p4E8Jb.png)

可以看到defer函数的位置时n的值为100，尽管在函数foo结束的时候n的值已经是200了，但是defer语句本身所处的位置时刻，即foo函数入口时n为100，所以最终defer函数打印出来的n值为100。

再来一个栗子:

```go
package main

import (
	"fmt"
)

func foo(n int) int {
	fmt.Println("n1=", n)
	defer func() {
		n += 1
		fmt.Println("n=", n)
	}()
	n += 1
	fmt.Println("n2=", n)
	return n
}

func main() {
	var i int = 1
	foo(i)
}
```

> λ go run defer.go
n1= 1
n2= 2
n= 3

![](https://www.choudalao.com/uploads/20191218/2019121823053608cHnE.png)

n的值最后是3,这也就是说明了defer相当于php的析构函数。在程序执行完后，最后执行的defer内部的匿名函数。

### defer 读取函数返回值（return返回机制）
defer、return、返回值三者的执行逻辑是：
1. return最先执行，return负责将结果写入返回值中；
2. 接着defer开始执行一些收尾工作；
3. 最后函数携带当前返回值（可能和最初的返回值不相同）退出。
4. 当defer语句放在return后面时，不会被执行。

##### 无名返回值：
```go
package main
 
import (
    "fmt"
)
 
func a(i int) int {
 
    defer func() {
        i++
        fmt.Println("defer2:", i)
    }() // ③ 执行: i = 2
 
 
    defer func() {
        i++
        fmt.Println("defer1:", i)
    }() // ② 后声明,先执行: i = 1
 
    return i  // ① i = 0, 已经完成了返回值的赋值,但是这个时候先不返回; 先去执行 defer.
}
 
func main() {
    var a = a(0)
    fmt.Println("a:", a)
}
// 结果
//defer1: 1
//defer2: 2
//a: 0
```

**解释说明：**
①返回值由变量 i 赋值，相当于 返回值i=0。
②第二个defer中 i++ , i= 1， 第一个 defer中i++, i = 2，所以最终i的值是2。
③但是返回值已经被赋值了，即使后续修改i也不会影响返回值。所以, 最终函数的返回值 = 0。

#### 有名返回值：
```go
package main
 
import (
    "fmt"
)
 
func b() (i int) { // 有名返回值: 此处函数声明, 已经指明了返回值就是 i
    defer func() {
        i++
        fmt.Println("defer2:", i)
    }()
    defer func() {
        i++
        fmt.Println("defer1:", i)
    }()
    return i // 或者直接写成 return
}
 
func main() {
    fmt.Println("return:", b())
}
// 结果
//defer1: 1
//defer2: 2
//return: 2
```
**解释说明：**
这里已经指明了返回值就是i，所以后续对i进行修改都相当于在修改返回值，所以最终函数的返回值是2。

#### 函数返回值为地址
```go
package main
 
import (
    "fmt"
)
 
func c() *int {
    var i int
    defer func() {
        i++
        fmt.Println("defer2:", i)
    }()
    defer func() {
        i++
        fmt.Println("defer1:", i)
    }()
    return &i
}
 
func main() {
    fmt.Println("return:", *(c()))
}
// 结果
//defer1: 1
//defer2: 2
//return: 2
```
**解释说明：**
此时的返回值是一个指针（地址），这个指针 =&i，相当于指向变量i所在的地址，两个defer语句都对 i进行了修改，那么返回值指向的地址的内容也发生了改变，所以最终的返回值是2。

#### defer与闭包
```go
package main
 
import "fmt"
 
type Test struct {
    name string
}
func (t *Test) pp() {
    fmt.Println(t.name)
}
func main() {
    ts := []Test{{"a"}, {"b"}, {"c"}}
    for _, t := range ts {
        defer t.pp()
    }
}
// 结果
// c
// c
// c
```
**解释说明：**
for 结束时 t.name=“c”，接下来执行的那些defer语句中用到的 t.name 的值均为”c“。

```go
package main

import "fmt"

type Test struct {
	name string
}

func pp(t Test) {
	fmt.Println(t.name)
}
func main() {
	ts := []Test{{"a"}, {"b"}, {"c"}}
	for _, t := range ts {
		defer pp(t) // defer函数的参数是在defer语句出现的位置做计算的，
	}
}
// 结果
//c 
//b 
//a 
```
**解释说明：**
defer语句中的参数会实时解析，所以在碰到defer语句的时候就把此时的 t 代入了。

修改代码
```go
package main

import "fmt"

type Test struct {
	name string
}

func (t *Test) pp() {
	fmt.Println(t.name)
}

func main() {
	ts := []Test{{"a"}, {"b"}, {"c"}}
	for _, t := range ts {
		tt := t 
		println(&tt)
		defer tt.pp()
	}
}
// 结果
//0xc000050250
//0xc000050270
//0xc000050290
//c
//b
//a
```
**解释说明：**

① :=用来声明并赋值，连续使用2次a:=1就会报错，但是在for循环内，可以看出每次tt:=t时，tt 的地址都不同，说明他们是不同的变量，所以并不会报错。
② 每次都有一个新的变量tt:=t，所以每次在执行defer语句时，对应的tt不是同一个（for循环中实际上生成了3个不同的tt），所以输出的结果也不相同。


参考资料：
https://blog.csdn.net/universsky2015/article/details/124601011