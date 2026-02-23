---
title: "docker 安装 kafka"
date: 2023-03-06T00:01:52+08:00
updated: 2026-02-23T18:59:10+08:00
author: "臭大佬"
categories: [linux]
description: "docker 安装 kafka"
cover: "https://www.choudalao.com/uploads/20230305/dNwSJDmgjVwSAvl7FnciRqKjciz0NQQXqBlQOJGQ.png"
click: 6000
---

# 说明
到 [docker hub](https://hub.docker.com/search?q=kafka "docker hub") 去搜一下`kafka`, 排在第一位的是`bitnami/kafka`,我们就用它了。

### 下载 docker-compose.yml
```go
curl -sSL https://raw.githubusercontent.com/bitnami/containers/main/bitnami/kafka/docker-compose.yml > docker-compose.yml
```
### 修改 docker-compose.yml ,配置外网访问
```go
version: "2"
services:
  zookeeper:
    image: docker.io/bitnami/zookeeper:3.8
    ports:
      - "2181:2181"
    volumes:
       - "zookeeper_data:/bitnami"
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes # 匿名登录
  kafka:
    image: docker.io/bitnami/kafka:3.4
    ports: #记得在防火墙开放端口
      - "9092:9092"
      - "9093:9093"
    volumes:
      - "kafka_data:/bitnami"
    environment:
      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
      - ALLOW_PLAINTEXT_LISTENER=yes # 配置监听者的安全协议
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CLIENT:PLAINTEXT,EXTERNAL:PLAINTEXT # 定义Kafka Broker的Listener的配置项，配置外部访问和内部访问
      - KAFKA_CFG_LISTENERS=CLIENT://:9092,EXTERNAL://0.0.0.0:9093 # 将Broker的Listener信息发布到Zookeeper中，供Clients（Producer/Consumer）使用
      - KAFKA_CFG_ADVERTISED_LISTENERS=CLIENT://kafka:9092,EXTERNAL://dev.wsl.net:9093 # dev.wsl.net 换成自己的ip
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=CLIENT
    depends_on:
      - zookeeper
volumes:
  zookeeper_data:
    driver: local
  kafka_data:
    driver: local
```


运行
```go
docker-compose up -d
```
![](https://www.choudalao.com/uploads/20230325/20230325203849tT8Ktl.png)

![](https://www.choudalao.com/uploads/20230325/202303252038585eBMUd.png)

### 可视化 kafka-map

[kafka-map 介绍](https://gitee.com/dushixiang/kafka-map "kafka-map 介绍")

记得开放端口9090
```go
docker run -d  -p 9090:8080   -v /www/wwwroot/kafka/kafka-map/data:/usr/local/kafka-map/data     -e DEFAULT_USERNAME=admin     -e DEFAULT_PASSWORD=admin  --name kafka-map   --restart always dushixiang/kafka-map:latest
```

![](https://www.choudalao.com/uploads/20230325/20230325211720UZvHbt.png)

### go中简单使用
Go语言中连接kafka使用第三方库: github.com/Shopify/sarama。
获取`go get github.com/Shopify/sarama`

发送数据
```go
package main

import (
	"fmt"
	"github.com/Shopify/sarama"
)

var topicTitle = "wsl-topic"

func main() {
	//kafka配置项
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForAll          // 发送完数据需要leader和follow都确认
	config.Producer.Partitioner = sarama.NewRandomPartitioner // 新选出一个partition
	config.Producer.Return.Successes = true                   // 成功交付的消息将在success channel返回

	// 连接kafka
	client, err := sarama.NewSyncProducer([]string{"dev.wsl.net:9093"}, config)
	if err != nil {
		fmt.Println("producer closed, err:", err)
		return
	}

	// 构造消息
	msg := &sarama.ProducerMessage{}
	msg.Topic = topicTitle
	msg.Value = sarama.StringEncoder("这是一条测试数据")
	defer client.Close()

	// 发送消息
	pid, offset, err := client.SendMessage(msg)
	if err != nil {
		fmt.Println("发送失败, err:", err)
		return
	}
	fmt.Printf("pid:%v offset:%v\n", pid, offset)
}

```

消费数据
```go
package main

import (
	"fmt"

	"github.com/Shopify/sarama"
)

var topicTitle = "wsl-topic"

func main() {
// 配置Kafka消费者
	config := sarama.NewConfig()
	config.Consumer.Return.Errors = true
	consumer, err := sarama.NewConsumer([]string{"dev.wsl.net:9093"}, config)
	if err != nil {
		panic(err)
	}
	partitionList, err := consumer.Partitions(topicTitle) // 根据topic取到所有的分区
	if err != nil {
		fmt.Printf("fail to get list of partition:err%v\n", err)
		return
	}
	fmt.Println("分区列表")
	fmt.Println(partitionList)
	for partition := range partitionList { // 遍历所有的分区
		// 针对每个分区创建一个对应的分区消费者
		pc, err := consumer.ConsumePartition(topicTitle, int32(partition), sarama.OffsetNewest)
		if err != nil {
			fmt.Printf("failed to start consumer for partition %d,err:%v\n", partition, err)
			return
		}
		go func(sarama.PartitionConsumer) {
			defer pc.AsyncClose()
			select {
			case msg := <-pc.Messages():
				fmt.Printf("Partition:%d Offset:%d Key:%v Value:%v \n", msg.Partition, msg.Offset, string(msg.Key), string(msg.Value))
			case err := <-pc.Errors():
				fmt.Printf("Error: %v\n", err)
			}
		}(pc)
	}
}
```