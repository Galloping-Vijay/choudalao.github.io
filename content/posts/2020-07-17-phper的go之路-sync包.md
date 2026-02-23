---
title: "PHPer的Go之路 --sync包"
date: 2020-07-17T00:24:26+08:00
updated: 2026-02-23T16:44:59+08:00
author: "臭大佬"
categories: [Go]
description: "PHPer的Go之路 --sync包"
cover: "https://www.choudalao.com/uploads/20200716/gnFQ9RDJzkSHnZ2XaXVTAxKsbha1f5XECjrPtMFT.jpeg"
click: 3303
---

好久没有学习Go啦，都颓废了，最近看到微软放弃对拍黄片（PHP）的支持，如果要在 Windows 上运行最新的 PHP 版本，则需要使用 WSL 并在 Linux 环境中运行 PHP。
> 我们知道，对于漏洞修复，当前的发布日期是 2 年，而对于安全修复，则是 1 年之后。这意味着 PHP 7.2 将在 11 月停止支持。PHP 7.3 仅在 11 月才进入安全修复模式。PHP 7.4 将继续进行一年的错误修复，然后再进行一年的安全修复。只要官方支持，我们致力于在 Windows 上针对 7.2、7.3 和 7.4 维护 PHP 的开发和构建。但是，我们不会以 8.0 及更高版本的任何能力支持 Windows 的 PHP。

近些年来，对拍黄片（PHP）看衰的新闻层出不穷，感觉拍黄片（PHP）并不是铁饭碗，周围的同行也危机感越来越严重，学Go学Python的很多呀。招聘信息也看到很多Go代替PHP的，再不学起来就要被淘汰了。把基础语法学完，然后搞个小项目，基本入门之后，才能理直气壮的继续骗工资。

进入正题，今天学习了一下 `sync 包` ，
# 什么是Sync包
Sync包官方文档：http://devdocs.io/go/sync/index#Map
> Package sync provides basic synchronization primitives such as mutual exclusion locks. Other than the Once and WaitGroup types, most are intended for use by low-level library routines. Higher-level synchronization is better done via channels and communication.

> Values containing the types defined in this package should not be copied.

这句话大意是说：
包同步提供基本的同步原语，例如互斥锁。除一次和等待组类型外，大多数都供低级库例程使用。更高级别的同步最好通过渠道和通信来完成。

在简书上看到一篇整理比较全面的文章，大部分引用于此：[sync包介绍](https://www.jianshu.com/p/b85018eb00c1 "sync包介绍")


### sync.Cond
```go
package main

import (
	"fmt"
	"sync"
	"time"
)

/*
* sync.Cond
* 条件变量的作用并不是保证在同一时刻仅有一个线程访问某一个共享数据，而是在某一个条件发生时，通知阻塞在该条件上的goroutine(线程)
*
* 条件变量+互斥量(锁)
* a. 互斥量为共享数据的访问提供互斥支持
* b. 条件变量就数据状态的变化向相关线程发出通知(goroutine)
*
* sync.Cond提供的三个相关方法:
* 1. wait: 阻塞当前线程(goroutine)，直到收到该条件变量发来的通知
* 2. signal: 单发通知，让该条件变量向至少一个正在等待它的goroutine发送通知，表示共享数据的状态已经改变
* 3. broadcast: 广播通知，让条件变量给正在等待它的所有goroutine发送通知，告知共享数据的状态已经改变
*
* sync.Cond struct
* // Each Cond has an associated Locker L (often a *Mutex or *RWMutex),
* // which must be held when changing the condition and
* // when calling the Wait method.
* //
* // A Cond must not be copied after first use.
* type Cond struct {
*   noCopy noCopy
*
*   // L is held while observing or changing the condition
*   L Locker
*
*   notify  notifyList
*   checker copyChecker
* }
*
* 通过sync.Cond的定义，我们需要注意以下几点:
* 1. Cond内部存在一个Locker(Mutex或RWMutex)，在Cond状态条件改变或调用Wait方法时，必须被锁住。即Locker是对
*    Wait, Signal，Broadcast进行保护，确保在发送信号的时候不会有新的goroutine进入wait而阻塞。
* 2. Cond变量在第一次创建之后不应该被copy。
* 3. 在调用Signal，Broadcast函数之前，应该确保目标进入wait阻塞状态。
*
 */

func main() {
	var wg sync.WaitGroup
	cond := sync.NewCond(new(sync.Mutex))
	for i := 0; i < 3; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()

			// wait前先上锁
			cond.L.Lock()
			fmt.Printf("goroutine_%d start wait\n", i)
			cond.Wait()
			fmt.Printf("goroutine_%d end wait\n", i)
			cond.L.Unlock()
		}(i)
	}

	/*
	   // 1. 调用signal方法，一次唤醒一个阻塞等待的goroutine
	   for i := 0; i < 3; i++ {
	       time.Sleep(1 * time.Second)
	       //cond.L.Lock()
	       cond.Signal() // 1秒唤醒一个goroutine
	       //cond.L.Unlock()
	   }
	*/

	// 2. 调用broadcast方法，一次性唤醒所有阻塞的goroutine
	time.Sleep(1 * time.Second)
	//cond.L.Lock()
	cond.Broadcast()
	//cond.L.Unlock()

	wg.Wait()
	fmt.Println("end test")
}

```
利用sync.Cond条件变量进行简单阻塞的示例:
```go
c := sync.NewCond(&sync.Mutex{}) // 1
c.L.Lock() // 2
for conditionTrue() == false {
c.Wait() // 3：该方法会使当前goroutine被阻塞（阻塞式）
}
c.L.Unlock() // 4
```
注意点:
- NewCond函数传入的参数实现了sync.Locker类型。Cond类型允许以并行安全的方式与其他goroutines协调。
- 在执行Wait操作前，必须进行锁定。因为，Wait函数的调用会执行解锁并暂停该goroutine。
- 进入暂停状态的goroutine会一直被阻塞住，直到接收到通知。
- 当前goroutine被唤醒后，必须执行解锁操作，因为在Wait函数退出前，会执行加锁操作。

###  sync.Map
```go
package main

import (
	"fmt"
	"sync"
)

/*
* Go1.9版本之前，其自带的map并不是并发安全的，如果要对其实现安全地并发访问，则需要对其进行加锁操作，即将map和sync.Mutex或sync.RWMutex
* 打包成一个struct来使用。
* Go1.9推出了sync.Map，其原生支持并发安全，相比上述struct的map具备更好的性能。sync.Map较内置map的用法不太一样，其内部封装了更为复杂的
* 数据结构。
*
*   var smp sync.Map
*   其主要提供了以下几种方法:
*   1. Store(key, value interface{}) : 设置一个键值对
*   2. LoadOrStore(key, value interface{})(actual interface{}, loaded bool): 如果key存在，则返回其对应的值；如果key不存在，则设置
        相应的值。如果是读取，则loaded返回true；如果是设置，则loaded返回false。
*   3. Load(key interface{})(value interface{}, ok bool) : 读取map中key对应的value。如果存在，ok返回true；否则，返回false。
*   4. Delete(key interface{}) : 删除对应的key
*   5. Range(f func(key, value interface{})bool) : 依次遍历map中的k-v对，如果函数f返回false，则停止迭代。
*       Tips: Range does not necessarily correspond to any consistent snapshot of the Map's contents:
        no key will be visited more than once, but if the value for any key is stored or deleted concurrently,
        Range may reflect any mapping for that key from any point during the Range call.
*   在Range函数调用的过程，遍历key的顺序同样是随机的，且range能否保证遍历key的唯一性(不存在重复)。如果，range过程中存在其它的goroutine并发
*   store, delete key，则range遍历的结果是反映当时时刻map的存储状态的。
*/

func main() {
	var smp sync.Map

	// 添加kv对
	smp.Store("1", 1)
	smp.Store("2", 2)
	smp.Store("3", 3)

	// 遍历
	fmt.Println("11111111111111")
	smp.Range(func(key, value interface{}) bool {
		fmt.Printf("%v:%v\n", key, value)
		return true
	})

	// 删除
	smp.Delete("3")

	// 遍历
	fmt.Println("222222222222222")
	smp.Range(func(key, value interface{}) bool {
		fmt.Printf("%v:%v\n", key, value)
		return true
	})

	v1, ok := smp.Load("1")
	if ok {
		fmt.Println(v1)
	}
}

```

### sync.WaitGroup  实现协程并发
sync.WaitGroup主要用于等待一组并发操作的完成。例如，使用sync.WaitGroup等待一组goroutine执行完对应的操作。

```go
wg :=&sync.WaitGroup{}

wg.Add(1) // 注册一个任务
go func() {
    defer wg.Done() // 通知当前任务已经完成。
    fmt.Println("1st goroutine sleeping...")
    time.Sleep(1)
}()

wg.Add(1) // 注册一个任务
go func() {
    defer wg.Done() // 通知当前任务已经完成。
    fmt.Println("2nd goroutine sleeping...")
    time.Sleep(2)
}()

wg.Wait() // 阻塞在这里，直到所有任务都已完成。
fmt.Println("All goroutines complete.")
```
可以将sync.WaitGroup视作一个安全的并发计数器：调用Add操作增加计数，调用Done操作减少计数，调用Wait操作会阻塞等待，直到计数器变为0。

另外，一种使用sync.WaitGroup的方法：
```go
// 传指针的方式，函数内部使用同一sync.WaitGroup
hello := func(wg *sync.WaitGroup, id int) {
    defer wg.Done()
    fmt.Printf("Hello from %v!\n", id)
}

const numGreeters = 5
var wg sync.WaitGroup
wg.Add(numGreeters)
for i := 0; i < numGreeters; i++ {
    go hello(&wg, i+1)  // 传指针参数
}
wg.Wait()
```
### sync.Once
顾名思义，sync.Once确保了即使在不同的goroutine上，调用Do传入的函数只执行一次。一般应用于初始化的场景，sync.Once确保该初始化操作只被执行一次。

注意
sync.Once只计算Do被调用的次数，而不是调用传入Do的唯一函数的次数。例如，下面函数count的输出值为1而不是0。

```go
    var count int
    increment := func() { count++ }
    decrement := func() { count-- }

    var once sync.Once
    once.Do(increment) // increment函数将被调用
    once.Do(decrement) // decrement函数不会被调用

    fmt.Printf("Count: %d\n", count)
```

### sync.Mutex和sync.RWMutex
被锁定部分是程序的性能瓶颈，进入和退出锁的成本有点高，因此应该尽量减少锁定涉及的范围。sync.RWMutex相比sync.Mutex具有更高的性能，因此在逻辑正确的情况下应该尽量使用sync.RWMutex而不是sync.Mutex。

### sync.Pool
sync.Pool是对象池模式的并发安全实现。池模式是一种创建和提供固定数量可用对象的方式。它通常用于约束创建资源昂贵的事务(例如，数据库连接)。Go中sync.Pool可以被多个例程安全地使用。

### Get/Put方法
Pool的主要接口是它的Get方法。 被调用时，Get将首先检查池中是否有可用实例返回给调用者，如果没有，则创建一个新成员变量。使用完成后，调用者调用Put将正在使用的实例放回池中供其他进程使用。 这里有一个简单的例子来演示：
```go
myPool := &sync.Pool{
    New: func() interface{} {
        fmt.Println("Creating new instance.")
        return struct{}{}
    },
}

instance := myPool.Get() //1: 从资源池拿取对象，否则新建一个对象
myPool.Put(instance)     //2: 将使用完的对象放回资源池
```
sync.Pool另一个用处可以预热分配对象的缓存，用于必须尽快进行的操作。在这种情况下，我们通过预先加载获取另一个对象的引用来减少消费者的时间消耗。在编写高吞吐量的网络服务器时，连接池是常见的优化技术。相关示例参考：https://www.kancloud.cn/mutouzhang/go/596830。

使用sync.Pool时应该注意的要点：
- 实例化sync.Pool时，给它一个新元素，该元素应该是线程安全的。
- 当你从Get获得一个实例时，不要假设你接收到的对象状态。
- 当你从池中取得实例时，请务必不要忘记调用Put。否则池的优越性就体现不出来了。这通常用defer来执行延迟操作。(defer Pool.Put())
- 池中的元素必须大致上是均匀的。

## errgroup.Group
### 场景
当我们有多个协程执行时，我们希望每个协程执行结果都是我们想要，即都是成功无异常的，那么我们就需要拿到所有协程的错误信息,知道所有协程的`error`都是`nil`,但是协程又是独立运行的,没有返回值.我们要怎样才能得到我们想要的结果呢?

这种场景很常见,比如我们方法中有个事务,多个协程结果都是成功,我们才提交事务,这时候我们就要判断各个协程是否有error,我们可以使用`golang.org/x/sync/errgroup`包，errgroup 底层实现多个 goroutine 调度，等待的能力还是基于 sync.WaitGroup。所以可以直接用它来处理协程。
示例：
```go
package main

import (
	"fmt"
	"golang.org/x/sync/errgroup"
)

func main() {
	var g errgroup.Group
	// 协程一
	g.Go(func() (err error) {
		// do something - 1
		return nil
	})
	// 协程二
	g.Go(func() (err error) {
		// do something - 2
		return nil
	})
	// 等待协程结果，拿到错误信息
	if err := g.Wait(); err != nil {
		fmt.Printf("错误信息为:%#v\n", err.Error())
		return
	}
	fmt.Println("无错误")
}
}
```
带函数
```go
	str := "aaa"
	var g errgroup.Group
	g.Go(func(parameter string) func() error {
		return func() (err error) {
			// 一些操作
			fmt.Println(parameter)
			return err
		}
	}(str))
	// 等待协程结果，拿到错误信息
	if err := g.Wait(); err != nil {
		return err
	}
```

##  goroutine 和 channel 实现一个控制协程数的应用
```go
package main

import (
	"fmt"
	"sync"
)

type User struct {
	ID   int
	Age  int
	Name string
}

func main() {
	numOfWorkers := 5                        // 限制最大协程数
	sem := make(chan struct{}, numOfWorkers) // 并发控制信号量
	lst := make([]*User, 20)                 // 模拟数据为20条
	var wg sync.WaitGroup
	wg.Add(len(lst))
	for _, v := range lst {
		sem <- struct{}{}
		// 数据操作
		go userAction(v, &wg, sem)
	}
	wg.Wait()
}

// 数据操作
func userAction(user *User, wg *sync.WaitGroup, sem chan struct{}) (err error) {
	// TODO
	defer func() {
		wg.Done()
		<-sem
	}()
	fmt.Println("操作用户")
	return
}
```