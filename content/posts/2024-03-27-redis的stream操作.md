---
title: "Redis的Stream操作"
date: 2024-03-27T17:47:01+08:00
updated: 2026-02-23T19:19:29+08:00
author: "臭大佬"
categories: [linux]
description: "Redis的Stream操作"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3395
---

# 介绍

# 基本操作
### 添加
*号表示服务器自动生成ID，后面顺序跟着一堆key/value,`stream-name`表示Stream名
```go
XADD stream-name * name boy age 20
```
### 获取列表
~~ 获取消息列表，会自动过滤已经删除的消息
 -表示最小值, +表示最大值~~
```go
xrange stream-name - +
```
指定最小消息ID的列表
```go
xrange stream-name 1711530121454-0 +
```
指定最大消息ID的列表
```go
xrange stream-name - 1711530139482-1
```
### 删除
单条
```go
xdel stream-name 1711530139482-1
```
删除整个Stream
```go
del stream-name
```
### 长度
```go
xlen stream-name
```

## 独立消费
从Stream头部读取两条消息
```go
xread count 2 streams stream-name 0-0
```
## 消费组消费
### 创建消费组
表示从头开始消费,`group-name`表示消费组名称
```go
xgroup create stream-name group-name 0-0
```
$表示从尾部开始消费，只接受新消息，当前Stream消息会全部忽略
```go
xgroup create stream-name group-name2 $
```
获取Stream信息
```go
xinfo stream stream-name
```
返回:

    1) "length"
    2) 2 # 共2个消息
    3) "radix-tree-keys"
    4) 1
    5) "last-generated-id"
    6) "1711530139482-1"
    7) "max-deleted-entry-id"
    8) "1711530139482-1"
    9) "recorded-first-entry-id"
    10) "1711530121454-0"
    11) "groups"
    12) 1  # 1个消费组
    13) "radix-tree-nodes"
    14) 2
    15) "entries-added"
    16) 3
    17) "first-entry" # 第一个消息
    18)     1) "1711530121454-0"
            2)      1) "name"
            2) "boy"
            3) "age"
            4) "20"
    19) "last-entry" # 最后一个消息
    20)     1) "1711530139482-0"
            2)      1) "name"
            2) "girl"
            3) "age"
            4) "17"


#### 获取Stream的消费组信息
```go
xinfo groups stream-name
```
返回:

    1) 1) "entries-read"
    2) 0 # 消费组已成功读取并处理了N条事件
    3) "lag"
      4) 0 #消费者落后于流中最新消息N个条目
    5) "name"
      6) "group-name" # 消费组名称
    7) "consumers"
      8) 1  # 1个消费组
    9) "pending"
      10) 0 # 0条正在处理的信息还有没有ack
    11) "last-delivered-id"
      12) "1711530139482-0"
	  
	  
#### 获取Stream的消费组中消费者信息
xinfo consumers Stream名 消费组
```go
xinfo consumers stream-name group-name
```
#### 删除消费组里面的某个消费者
```go
XGROUP DELCONSUMER stream-name group-name consumer-name
```

### 消费组消费
Stream提供了xreadgroup指令可以进行消费组的组内消费，需要提供消费组名称、消费者名称和起始消息ID。它同xread一样，也可以阻塞等待新消息。读到新消息后，对应的消息ID就会进入消费者的PEL(正在处理的消息)结构里，客户端处理完毕后使用xack指令通知服务器，本条消息已经处理完毕，该消息ID就会从PEL中移除。
————————————————

 ">"号表示从当前消费组的last_delivered_id后面开始读
每当消费者读取一条消息，last_delivered_id变量就会前进
```go
xreadgroup GROUP stream-name group-name count 1 streams stream-name >
```
再继续读取，就没有新消息了
```go
 xinfo groups stream-name
 ```
 返回:
 
    1) 1) "entries-read"
    2) 0 # 消费组已成功读取并处理了N条事件
    3) "lag"
      4) #消费者落后于流中最新消息N个条目
    5) "name"
      6) "group-name"
    7) "consumers"
      8) 1 # 一个消费者
    9) "pending"
      10) 2 # 共2条正在处理的信息还有没有ack
    11) "last-delivered-id"
      12) "1711530139482-0"
    
ack一条消息
```go
xack stream-name group-name 1711530139482-0
```
```go
xinfo groups stream-name
```
返回:

    1) 1) "pending"
    2) 1 # 少了1条
    3) "last-delivered-id"
      4) "1711530139482-0"
    5) "entries-read"
      6) 
    7) "lag"
      8) 
    9) "name"
      10) "group-name"
    11) "consumers"
      12) 1
      
查看
```go
xinfo consumers stream-name group-name
```

文章参考:https://blog.csdn.net/weixin_43064185/article/details/122012628