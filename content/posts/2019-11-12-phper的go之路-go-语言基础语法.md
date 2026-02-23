---
title: "PHPer的Go之路 -- Go 语言基础语法"
date: 2019-11-12T23:08:31+08:00
updated: 2026-02-23T08:19:10+08:00
author: "臭大佬"
categories: [Go]
description: "Go基本语法，包括标记、行分隔符、注释、变量、数据类型、常量、运算符"
cover: "https://www.choudalao.com/uploads/20191112/a8yxhvzO6QhtRa5DjKJMbzr7HvXwWMxoyXeaWGSX.jpeg"
click: 3278
---

# Go 标记
Go 程序可以由多个标记组成，可以是关键字，标识符，常量，字符串，符号。如以下 GO 语句由 6 个标记组成：

# 行分隔符
在 Go 程序中，一行代表一个语句结束。每个语句不需要像 C 家族中的其它语言一样以分号 ; 结尾，因为这些工作都将由 Go 编译器自动完成。

如果你打算将多个语句写在同一行，它们则必须使用 ; 人为区分，但在实际开发中我们并不鼓励这种做法。
以下为两个语句：

```
	fmt.Println("德玛西亚")
	fmt.Println("啦啦啦")
```
&nbsp;
# 注释

Go语言的单行注释是最常见的注释形式，你可以在任何地方使用以 、**//** 开头的单行注释。多行注释也叫块注释，均已以 /\* 开头，并以 \*/ 结尾。如：
```
// 单行注释

/*
 我是多行注释
 */
```
&nbsp;
# 数据类型
&nbsp;
## 布尔型：

布尔型的值只可以是常量 true 或者 false。一个简单的栗子：

```
var b bool = true。
```
&nbsp;
## 数字类型：

整型 int 和浮点型 float32、float64，Go 语言支持整型和浮点型数字，并且支持复数，其中位的运算采用补码。

### uint8
无符号 8 位整型 (0 到 255)

### uint16
无符号 16 位整型 (0 到 65535)

### uint32
无符号 32 位整型 (0 到 4294967295)

### uint64
无符号 64 位整型 (0 到 18446744073709551615)

### int8
有符号 8 位整型 (-128 到 127)

### int16
有符号 16 位整型 (-32768 到 32767)

### int32
有符号 32 位整型 (-2147483648 到 2147483647)

### int64
有符号 64 位整型 (-9223372036854775808 到 9223372036854775807)

### float32
IEEE-754 32位浮点型数，float32 等价于 PHP 的 float 类型（单精度浮点数），可以精确到小数点后 7 位

### float64
IEEE-754 64位浮点型数，float64 等价于 PHP 的 double 类型（双精度浮点数），可以精确到小数点后 15 位。

### complex64
32 位实数和虚数

### complex128
64 位实数和虚数

Go 语言还支持复数类型，与复数相对，我们可以把整型和浮点型这种日常比较常见的数字称为实数，复数是实数的延伸，可以通过两个实数（在计算机中用浮点数表示）构成，一个表示实部（real），一个表示虚部（imag），常见的表达形式如下：

```
z = a + bi
```
其中 a、b 均为实数，i 称为虚数单位，当 b = 0 时，z 就是常见的实数，当 a = 0 而 b ≠ 0 时，将 z 称之为纯虚数，如果你理解数学概念中的复数概念，这些都很好理解，下面我们来看下复数在 Go 语言中的表示和使用。

在 Go 语言中，复数支持两种类型：complex64（32位实部和虚部） 和 complex128（64位实部与虚部），对应的表示示例如下，和数学概念中的复数表示形式一致：

```
var complex_value_1 complex64

complex_value_1 = 1.10 + 10i// 由两个 float32 实数构成的复数类型
complex_value_2 := 1.10 + 10i// 和浮点型一样，默认自动推导的实数类型是 float64，所以 complex_value_2 是 complex128 类型
complex_value_3 := complex(1.10, 10)// 与 complex_value_2 等价
```

对于一个复数 z = complex(x, y)，就可以通过 Go 语言内置函数 real(z) 获得该复数的实部，也就是 x，通过 imag(z) 获得该复数的虚部，也就是 y。

复数支持和其它数字类型一样的算术运算符。当你使用 == 或者 != 对复数进行比较运算时，由于构成复数的实数部分也是浮点型，需要注意对精度的把握。

更多关于复数的函数，请查阅   [math/cmplx ](https://golang.org/pkg/math/cmplx/ "math/cmplx ") 标准库的文档。如果你对内存的要求不是特别高，最好使用 complex128 作为计算类型，因为相关函数大都使用这个类型的参数。

### byte
类似 uint8，代表 UTF-8 字符串的单个字节的值。

### rune
类似 int32，代表单个 Unicode 字符，可查阅 Go 标准库的  [unicode](https://golang.org/pkg/unicode/ "unicode")  包

### uint
32 或 64 位

### int
与 uint 一样大小

### uintptr
无符号整型，用于存放一个指针

## 字符串类型:

字符串就是一串固定长度的字符连接起来的字符序列。Go 的字符串是由单个字节连接起来的。Go 语言的字符串的字节使用 UTF-8 编码标识 Unicode 文本。

在 Go 语言中，字符串是一种基本类型，默认是通过 UTF-8 编码的字符序列，当字符为 ASCII 码时则占用 1 个字节，其它字符根据需要占用 2-4 个字节，比如中文编码通常需要 3 个字节。

```
var str string         // 声明字符串变量
str = "Hello World"    // 变量初始化
str_2 := "你好，中国"  // 也可以同时进行声明和初始化
```

#### 获取单个字符
要获取字符串中的某个字符，可以通过访问数组下标的方式：

```
ch := str[0] // 取字符串的第一个字符
// H
```

虽然可以通过数组下标方式访问字符串中的字符，但是和数组不同，在 Go 语言中，字符串是一种不可变值类型，一旦初始化之后，它的内容不能被修改。

```
str := "Hello world"
str[0] = 'X' // 编译错误
```
> cannot assign to str[0]

#### 格式化输出
还可以通过 Go 语言内置的 len() 函数获取指定字符串的长度，以及通过 fmt 包提供的 Printf 进行字符串格式化输出（用法和 PHP 中的 printf 类似）：

```
fmt.Printf("The length of \"%s\" is %d \n", str, len(str)) 
fmt.Printf("The first character of \"%s\" is %c.\n", str, ch)
```

#### 转义字符
与 PHP 不同，**Go 语言的字符串不支持单引号**，只能通过双引号定义字符串字面值，**如果要对特定字符进行转义，可以通过 \ 实现**，就像我们上面在字符串中转义双引号和换行符那样，常见的需要转义的字符如下所示：

- \n ：换行符
- \r ：回车符
- \t ：tab 键
- \u 或 \U ：Unicode 字符
- \\ ：反斜杠自身
所以，上述打印代码输出结果为：

```
The length of "Hello world" is 11 
The first character of "Hello world" is H.
```

#### 字符串操作

##### 字符串连接
php中用“.”连接，Go中用“+”连接。

```
str = str + ", 臭大佬"
str += ", 臭大佬"  // 上述语句也可以简写为这样，效果完全一样
str = str +
        ", 臭大佬"//另外，还有一点需要注意的是如果字符串长度较长，需要换行，则「+」必须出现在上一行的末尾，否则会报错：
```

##### 字符串切片
在 PHP 中我们可以通过 substr 函数获取字符串的子串，在 Go 语言中，可以通过字符串切片功能实现类似的操作，相比 substr 函数，使用起来更加方便：

```
str = "hello, world"
str_1 := str[:5]  // 获取索引5（不含）之前的子串
str_2 := str[7:]  // 获取索引7（含）之后的子串
str_3 := str[0:5]  // 获取从索引0（含）到索引5（不含）之间的子串
fmt.Println(str_1)
fmt.Println(str_2)
fmt.Println(str_3)
//结果
//hello
//world
//hello
```

字符串切片和 PHP 的 substr 函数使用方式有所差异，通过「:」对字符串进行切片，冒号之前的数字代表起始点（为空表示从0开始），之后的数字代表结束点（为空表示到字符串最后），而不是子串的长度。

此外 Go 字符串也支持字符串比较、是否包含指定字符/子串、获取指定子串索引位置、字符串替换、大小写转换、trim 等操作，更多操作 API，请参考标准库 [ strings](https://golang.org/pkg/strings/ " strings")  包。

##### 字符串遍历
###### 以字节数组的方式遍历：

```
str := "Hello, 世界"
n := len(str)
for i := 0; i < n; i++ {
    ch := str[i]    // 依据下标取字符串中的字符，类型为byte
    fmt.Println(i, ch)
}
// 结果
// 0 72 
//1 101 
//2 108 
//3 108 
// 4 111 
//5 44 
//6 32 
//7 228 
//8 184 
//9 150 
//10 231 
//11 149 
//12 140
```

可以看出，这个字符串长度为 13，尽管从直观上来说，这个字符串应该只有 9 个字符。这是因为**每个中文字符在 UTF-8 中占 3 个字节**，而不是 1 个字节。

###### 以 Unicode 字符遍历：

```
str := "Hello, 世界" 
for i, ch := range str { 
    fmt.Println(i, ch)    // ch 的类型为 rune 
}
//结果
//0 72 
//1 101 
//2 108 
//3 108 
//4 111 
//5 44 
//6 32 
//7 19990 
//10 30028
```
这个时候，打印的就是 9 个字符了，以 Unicode 字符方式遍历时，每个字符的类型是 rune（早期的 Go 语言用 int 类型表示 Unicode 字符），而不是 byte。

#### 数字和字符串转化
```go
import "strconv" //先导入strconv包
// string到int
int, err := strconv.Atoi(string)
// string到int64
int64, err := strconv.ParseInt(string, 10, 64)
// string到float64 第二个参数:32 表示 float32，64 表示 float64
float64, err := strconv.ParseFloat(string, 64)
// int到string
string := strconv.Itoa(int)
// int64到string
// base 表示整数的进制，base 必须在2到36之间，结果中会使用小写字母'a'到'z'表示大于10的数字。
string := strconv.FormatInt(int64,10)
```

## 派生类型:

包括：
- 指针类型（Pointer）
- 数组类型
- 结构化类型(struct)
- Channel 类型
- 函数类型
- 切片类型
- 接口类型（interface）
- Map 类型

# 变量
声明变量的一般形式是使用 var 关键字：

```
//声明一个变量
var identifier type
//声明多个变量
var identifier1, identifier2 type
// 或者
var (
    identifier1 type 
    identifier2 type
）
```

需要注意的是，变量在声明之后，系统会自动将变量值初始化为对应类型的零值，比如 int类型 的值为 0，string 的值空字符串，bool 的值为 false

如果变量名包含多个单词，Go 语言变量命名规则遵循**驼峰命名法**，即首个单词小写，每个新单词的首字母大写，如 statusName。

但如果你的全局变量希望能够被外部包所使用，则需要将首个单词的首字母也大写。

## 变量初始化
&nbsp;
```
var v1 int = 10 // 方式一，常规的初始化操作
var v2 = 10 // 方式二，此时变量类型会被编译器自动推导出来
v3 := 10 // 方式三，可以省略 var，编译器可以自动推导出v3的类型
```

以上三种用法的效果是完全一样的。与第一种用法相比，第三种用法更简捷，推荐用这种方式对变量进行初始化。这里 Go 语言也引入了另一个 PHP 语言中没有的运算符 :=，用于明确表达同时对变量进行声明和初始化。

另外，出现在 := 左侧的变量不应该是已经被声明过的，否则会导致编译错误，比如下面这个写法：

```
var i int 
i := 2
```
会导致错误：

```
no new variables on left side of :=
```

> 注：在 PHP 中，通常变量声明和初始化是一体的，即通过初始化的方式完成变量的声明，类的成员变量除外

## 多变量声明
&nbsp;
```
//类型相同多个变量, 非全局变量
var vname1, vname2, vname3 type
vname1, vname2, vname3 = v1, v2, v3

var vname1, vname2, vname3 = v1, v2, v3 // 和 python 很像,不需要显示声明类型，自动推断

vname1, vname2, vname3 := v1, v2, v3 // 出现在 := 左侧的变量不应该是已经被声明过的，否则会导致编译错误


// 这种因式分解关键字的写法一般用于声明全局变量
var (
    vname1 v_type1
    vname2 v_type2
)
```

栗子：

```
package main

var x, y int
var (  // 这种因式分解关键字的写法一般用于声明全局变量
    a int
    b bool
)

var c, d int = 1, 2
var e, f = 123, "hello"

//这种不带声明格式的只能在函数体中出现
//g, h := 123, "hello"

func main(){
    g, h := 123, "hello"
    println(x, y, a, b, c, d, e, f, g, h)
}
//运行结果 
// 0 0 0 false 1 2 123 hello 123 hello
```
&nbsp;
## 匿名变量

我们在使用传统的强类型语言编程时，经常会出现这种情况，即在调用函数时为了获取一个值，却因为该函数返回多个值而不得不定义一堆没用的变量。

在 Go 语言中，这种情况可以通过结合使用多重赋值和匿名变量来避免这种丑陋的写法，让代码看起来更加优雅，多重赋值上面已经介绍过，匿名变量则通过下划线 _ 来声明，任何赋予它的值都会被丢弃。

我们来看个例子，假设 GetName() 函数的定义如下，它返回两个值，分别为 userName 和 nickName：

```
func GetName() (userName, nickName string) { 
    return userName, nickName
}
```

若只想获得 nickName，则函数调用语句可以用如下方式实现：

```
_, nickName := GetName()
```
&nbsp;
# 常量

常量是一个简单值的标识符，在程序运行时，不会被修改的量。
常量中的数据类型只可以是布尔型、数字型（整数型、浮点型和复数）和字符串型。
通过 const 关键字来定义常量（遵循 C 语言的约定）。

常量的定义格式：

```
const identifier [type] = value
//多个相同类型的声明可以简写为：
const c_name1, c_name2 = value1, value2
```

显式类型定义： const b string = "abc"
隐式类型定义： const b = "abc"

>Go语言常量和变量声明规律：
从左往右，第一个标识符 var 或  const 表明声明的是变量还是常量，第二个标识符标识变量或常量的内存存储块别名，以便后续引用，第三个标识符表示变量或常量的数据类型，可以省略，省略的情况下底层会在编译期自动推导对应的变量或常量类型。

## iota

iota，特殊常量，可以认为是一个可以被编译器修改的常量。

iota 在 const关键字出现时将被重置为 0(const 内部的第一行之前)，const 中每新增一行常量声明将使 iota 计数一次(iota 可理解为 const 语句块中的行索引)。

iota 可以被用作枚举值：

```
package main

import "fmt"

func main() {
    const (
            a = iota   //0
            b          //1
            c          //2
            d = "ha"   //独立值，iota += 1
            e          //"ha"   iota += 1
            f = 100    //iota +=1
            g          //100  iota +=1
            h = iota   //7,恢复计数
            i          //8
    )
    fmt.Println(a,b,c,d,e,f,g,h,i)
}
//结果
//0 1 2 ha ha 100 100 7 8
```
&nbsp;
## 运算符
&nbsp;
### 注意
在Go语言中，不同类型的变量是不能直接运算的，比如（`int`和`int32`两种类型的变量不能直接进行运算，这点和php不一样，一定要注意）。

Go中比较运算符也没有`===`和 `!==`这种严格比较运算符，因为所有运算符在比较的时候都会考虑数据类型。

# 类型转换

Go语言是强类型语言，不能像php那样，数据类型可以自动相互转换。

## 数值类型间的转换
&nbsp;
```go
v1 := uint(16)   // 初始化 v1 类型为 unit
v2 := int8(v1)   // 将 v1 转化为 int8 类型并赋值给 v2
v3 := uint16(v2) // 将 v2 转化为 uint16 类型并赋值给 v3

v1 := uint(-255) //由于 uint 是无符号整型，所以上述转化编译时会报错： constant -255 overflows uint
```
&nbsp;
## 数值和布尔值不支持转换
Go不能像php那样，true和1结果一样，false和0可以相同。