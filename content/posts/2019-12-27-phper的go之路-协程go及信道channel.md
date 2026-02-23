---
title: "PHPer的Go之路 -- 协程（go）及信道（channel）"
date: 2019-12-27T22:40:05+08:00
updated: 2026-02-23T15:34:15+08:00
author: "臭大佬"
categories: [Go]
description: "PHPer的Go之路 -- 协程（go）及信道（channel）"
cover: "https://www.choudalao.com/uploads/20191227/PpuAX9xE2kiSHIKFwI2gWdAwnWAwOa70xgUqPQEu.jpeg"
click: 3503
---

# Go协程

Go 协程是与其他函数或方法一起并发运行的函数或方法。Go 协程可以看作是轻量级线程。与线程相比，创建一个 Go 协程的成本很小。因此在 Go 应用中，常常会看到有数以千计的 Go 协程并发地运行。

代码：

```go
package main

import (
    "fmt"
)

func hello() {
    fmt.Println("Hello world goroutine")
}
func main() {
	//协程
    go hello()
    fmt.Println("main function")
}
```
> λ go run ct.go
main function

![](https://www.choudalao.com/uploads/20191227/20191227223529KnzquB.png)

main()调用了 go hello() 之后，程序控制没有等待 hello 协程结束，立即返回到了代码下一行，打印 main function。接着由于没有其他可执行的代码，Go 主协程终止，于是 hello 协程就没有机会运行了。

- 启动一个新的协程时，协程的调用会立即返回。与函数不同，程序控制不会去等待 Go 协程执行完毕。在调用 Go 协程之后，程序控制会立即返回到代码的下一行，忽略该协程的任何返回值。
- 如果希望运行其他 Go 协程，Go 主协程必须继续运行着。如果 Go 主协程终止，则程序终止，于是其他 Go 协程也不会继续运行。

# 信道（channel）

信道如同管道中的水会从一端流到另一端，通过使用信道，数据也可以从一端发送，在另一端接收。
所有信道都关联了一个类型。信道只能运输这种类型的数据，而运输其他类型的数据都是非法的。
chan T 表示 T 类型的信道。
信道的零值为 nil。信道的零值没有什么用，应该像对 map 和切片所做的那样，用 make 来定义信道。

### 声明与关闭

```go 
//声明一个信道
var a chan int
//或者
a := make(chan int)
//关闭信道
close(a)
```

### 发送和接收

```go
//箭头对于 a 来说是向外指的，因此我们读取了信道 a 的值，并把该值存储到变量 data。
data := <- a // 读取信道 a  
//箭头指向了 a，因此我们在把数据写入信道 a。
a <- data // 写入信道 a

//<-a 这行代码通过信道 a 接收数据，但并没有使用数据或者把数据存储到变量中。这完全是合法的。
 <- a
```

### 发送与接收默认是阻塞的

程序控制会在发送数据的语句处发生阻塞，直到有其它 Go 协程从信道读取到数据，才会解除阻塞。与此类似，当读取信道的数据时，如果没有其它的协程把数据写入到这个信道，那么读取过程就会一直阻塞着。

```go
package main

import (
	"fmt"
	"time"
)

func hello(done chan bool) {
	fmt.Println("hello go routine is going to sleep")
	time.Sleep(4 * time.Second)
	fmt.Println("hello go routine awake and going to write to done")
	done <- true
}
func main() {
	done := make(chan bool)
	fmt.Println("Main going to call hello go goroutine")
	//开启 hello 协程
	go hello(done)
	//阻塞，等待数据，也就是上面go协程 done <- true完成，才运行下面的代码
	<-done
	fmt.Println("Main received data")
}
```

![](https://www.choudalao.com/uploads/20191227/20191227232840RWfc6B.png)

### 死锁

使用信道需要考虑的一个重点是死锁。当 Go 协程给一个信道发送数据时，照理说会有其他 Go 协程来接收数据。如果没有的话，程序就会在运行时触发 panic，形成死锁。
同理，当有 Go 协程等着从一个信道接收数据时，我们期望其他的 Go 协程会向该信道写入数据，要不然程序就会触发 panic。

```go
package main

func main() {
	ch := make(chan int)
	ch <- 5
}
```

![](https://www.choudalao.com/uploads/20191227/20191227233112YmY365.png)

### 单向信道
只能发送或者接收数据的信道。

```go
package main

import "fmt"

//传递一个接收信道
func sendData(sendch chan<- int) {
	sendch <- 10
}

func main() {
	//创建了一个双向信道
	cha1 := make(chan int)
	//改变信道
	go sendData(cha1)
	//输出信道的值
	fmt.Println(<-cha1)
}
```

![](https://www.choudalao.com/uploads/20191228/20191228083014pTc1N2.png)

把一个双向信道转换成唯送信道或者唯收（Receive Only）信道都是行得通的，但是反过来就不行。

###  for range 遍历信道

```go
package main

import (
	"fmt"
)

func producer(chnl chan int) {
	for i := 0; i < 10; i++ {
		chnl <- i
	}
	close(chnl)
}
func main() {
	ch := make(chan int)
	go producer(ch)
	for {
		//检测信道是否关闭，
		v, ok := <-ch
		if ok == false {
			fmt.Println("ok为false，则表示信道关闭")
			break
		}
		fmt.Println("接收 ", v, ok)
	}
	//for range遍历
	for v := range ch {
		fmt.Println("接收 ",v)
	}
}
```

![](https://www.choudalao.com/uploads/20191228/20191228085415KtTAc6.png)

# 信道容量和长度

# 缓冲信道

声明信道的时候，其实第二个参数（capacity）--容量参数，如果接收数量大于capacity，会发生死锁（deadlock）。程序会在运行时触发 panic

```go
//capacity默认为0，大于0的时候就称为缓存信道
ch := make(chan type, capacity)
```

## 长度和容量

容量代表信道能容纳元素数量，长度表示信道里面有几个元素。

```go
package main

import (
	"fmt"
)

func main() {
	//创建缓冲容量为3的信道
	ch := make(chan int,3)
	//接收值（如果写入信道的数量大于3，会发生死锁（deadlock）。程序会在运行时触发 panic
	ch <- 1
	ch <-2
	fmt.Println("容量： ", cap(ch))
	fmt.Println("长度： ", len(ch))
	fmt.Println("发送的值： ", <-ch)
	fmt.Println("现在的长度： ", len(ch))
}
```

![](https://www.choudalao.com/uploads/20191228/20191228091758dEprV5.png)

# 信道与协程使用实例
空结构体在协程中的使用
```go
	done := make(chan struct{})
	go func(ch chan struct{}) {
		defer func() {
			if er := recover(); er != nil {
				fmt.Printf("程序执行报错了 error:%s", er)
			}
			ch <- struct{}{} // 发送空结构体到通道，表示工作完成
		}()
		// TODO 一些业务操作
		// .....
	}(done)
	// TODO 主程序
	// .....
	<-done // 阻塞等待，直到收到工作完成的信号
```

下面是一个下单伪代码
```go
package main

import (
    "fmt"
    "sync"
    "time"
)

type Order struct {
    ID          uint
    OrderNumber string
    Amount      float64
}

type OrderDetail struct {
    ID        uint
    OrderID   uint
    ProductID uint
    Quantity  int
    Price     float64
}

type OrderLog struct {
    ID             uint
    OrderID        uint
    Action         string
    ActionDateTime time.Time
}

func main() {
    var wg sync.WaitGroup

    // 创建订单
    orderCh := make(chan Order)
    wg.Add(1)
    go func() {
        defer wg.Done()

        order := Order{
            OrderNumber: "202201010001",
            Amount:      100.0,
        }
        orderCh <- order
    }()

    // 创建流水
    orderDetailCh := make(chan OrderDetail)
    wg.Add(1)
    go func() {
        defer wg.Done()

        order := <-orderCh
        orderDetail := OrderDetail{
            OrderID:   order.ID,
            ProductID: 1,
            Quantity:  1,
            Price:     100.0,
        }
        orderDetailCh <- orderDetail
    }()

    // 创建子订单
    orderLogCh := make(chan OrderLog)
    wg.Add(1)
    go func() {
        defer wg.Done()

        orderDetail := <-orderDetailCh
        subOrder := Order{
            OrderNumber: "202201010001-1",
            Amount:      orderDetail.Price,
        }
        subOrderLog := OrderLog{
            OrderID:        subOrder.ID,
            Action:         "create",
            ActionDateTime: time.Now(),
        }
        orderLogCh <- subOrderLog
    }()

    // 打印订单、流水和子订单日志
    wg.Add(1)
    go func() {
        defer wg.Done()

        order := <-orderCh
        fmt.Println("Order created:", order)

        orderDetail := <-orderDetailCh
        fmt.Println("Order detail created:", orderDetail)

        orderLog := <-orderLogCh
        fmt.Println("Sub order created:", orderLog)
    }()

    wg.Wait()
}
```

# 信道与协程并发写入数据库
例：从 CSV 文件读取并将数据插入数据库
```go
package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"sync"

	"gorm.io/gorm"
)

// Contact 是数据库中表的模型
type Contact struct {
	ID    uint   `gorm:"primary_key"`
	Name  string `gorm:"size:255"`
	Phone string `gorm:"size:255"`
	Email string `gorm:"size:255"`
}

func initDB() (*gorm.DB, error) {
	// 使用 MySQL 数据库
	db, err := gorm.Open("mysql", "user:password@/dbname?charset=utf8&parseTime=True&loc=Local")
	if err != nil {
		return nil, err
	}

	// 自动迁移表结构
	db.AutoMigrate(&Contact{})
	return db, nil
}

// 处理 CSV 文件并将数据插入数据库
func processCSV(filePath string, db *gorm.DB) error {
	// 打开 CSV 文件
	file, err := os.Open(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	// 创建 CSV 阅读器
	reader := csv.NewReader(file)

	// 读取所有行
	records, err := reader.ReadAll()
	if err != nil {
		return err
	}

	// 使用 WaitGroup 来同步所有的 goroutine
	var wg sync.WaitGroup

	// 通道用于发送每行数据
	ch := make(chan Contact, len(records))

	// 启动多个 goroutine 来并发处理 CSV 数据
	// 1. 生产者 goroutines - 需要等待每一个都完成
	for i := 1; i < len(records); i++ { // 从 1 开始，跳过标题行
		wg.Add(1)
		go func(record []string) {
			defer wg.Done()
			// 将 CSV 行转换为 Contact 实例
			contact := Contact{
				Name:  record[0],
				Phone: record[1],
				Email: record[2],
			}
			ch <- contact // 发送数据到通道
		}(records[i])
	}

	// 启动一个 goroutine 来将通道中的数据插入到数据库
	// 2. 消费者 goroutine - 通过通道关闭来控制结束
	go func() {
		for contact := range ch {
			// 只有一个 goroutine 在写入数据库，避免了并发连接过多的问题
			if err := db.Create(&contact).Error; err != nil {
				fmt.Println("Error inserting record:", err)
			}
		}
	}()

	// 3. 等待所有生产者完成
	wg.Wait()

	// 4. 关闭通道，这会导致消费者 goroutine 自动退出
	close(ch)

	return nil
}

func main() {
	// 初始化数据库
	db, err := initDB()
	if err != nil {
		fmt.Println("Failed to connect to database:", err)
		return
	}
	defer db.Close()

	// 处理 CSV 文件并将数据迁移到数据库
	err = processCSV("contacts.csv", db)
	if err != nil {
		fmt.Println("Error processing CSV file:", err)
		return
	}

	fmt.Println("CSV data successfully migrated to the database.")
}

```