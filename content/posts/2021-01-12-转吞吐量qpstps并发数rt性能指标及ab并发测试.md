---
title: "【转】吞吐量、QPS（TPS）、并发数、RT性能指标及ab并发测试"
date: 2021-01-12T00:32:26+08:00
updated: 2026-02-23T18:04:55+08:00
author: "臭大佬"
categories: [linux]
description: "吞吐量、QPS（TPS）、并发数、RT性能指标理解"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 6817
---

# 概念
### 吞吐量
系统的吞吐量是指系统的抗压、负载能力，指的是单位时间内处理的请求数量。通常情况下，吞吐率用 “字节数/秒” 来衡量，也可以用 “请求数/秒”，“页面数/秒”，其实，不管是一个请求还是一个页面，本质都是网络上传输的数据，那么表示数据的单位就是字节数。

系统吞吐量的几个重要参数：QPS（TPS），并发数，响应时间等，系统的吞吐量通常由这几个参数值来决定。

### 吞吐率（Requests per second）

服务器并发处理能力的量化描述，单位是reqs/s，指的是在某个并发用户数下单位时间内处理的请求数。某个并发用户数下单位时间内能处理的最大请求数，称之为最大吞吐率。

记住：吞吐率是基于并发用户数的。这句话代表了两个含义：

a、吞吐率和并发用户数相关

b、不同的并发用户数下，吞吐率一般是不同的

计算公式：总请求数/处理完成这些请求数所花费的时间，即

Request per second=Complete requests/Time taken for tests

###### 必须要说明的是，这个数值表示当前机器的整体性能，值越大越好。

### QPS

Queries Per Second，每秒查询数，即是每秒能够响应的查询次数，注意这里的查询是指用户发出请求到服务器做出响应成功的次数，简单理解可以认为查询=请求request

qps = 每秒钟request数量

### TPS

Transactions Per Second ，每秒处理的事务数。一个事务是指一个客户机向服务器发送请求然后服务器做出反应的过程。客户机在发送请求时开始计时，收到服务器响应后结束计时，以此来计算使用的时间和完成的事务个数。
针对单接口而言，TPS可以认为是等价于QPS的，比如访问一个页面/index.html，是一个TPS，而访问/index.html页面可能请求了3次服务器比如css、js、index接口，产生了3个QPS。

tps = 每秒钟事务数量

### 并发数

并发数是指系统同时能处理的请求数量，反映了系统的负载能力。

并发数 = 系统同时处理的request/事务数

### 响应时间RT

Response Time，简单理解为系统从输入到输出的时间间隔，宽泛的来说，代表从客户端发起请求到服务端接收到请求并响应所有数据的时间差。一般取平均响应时间。

### QPS，RT，并发数三者关系

QPS = 并发数 / 评价响应时间

一个系统吞吐量通常由QPS（TPS）、并发数两个因素决定，每套系统这两个值都有一个相对极限值，在应用场景访问压力下，只要某一项达到系统最高值，系统的吞吐量就上不去了，如果压力继续增大，系统的吞吐量反而会下降，原因是系统超负荷工作，上下文切换、内存等等其它消耗导致系统性能下降。

# ab测试

### ab操作说明
#### 介绍
ab是apache bench的简称，是apache提供的压力测试工具。
#### 说明
```php
ab [options] [http://]hostname[:port]/path
```

##### options

命令其余请参见  http://apache.jz123.cn/programs/ab.html

##### 发起总请求数：-n
-n1000 //代表本次测试发起1000个请求

##### 请求并发数：-c
-c1000 代表每次都同时发起1000次请求,也就是并发数为1000

##### 本次测试的最大秒速,默认没有限制：-t
-t10 代表10秒后就结束测试

##### 每次请求的超时时间,默认为30：-s
-s30 代表每个请求如果超时30秒,则直接代表该请求超时

##### 包含需要post的文件地址,一般和-T一起使用：-p
##### POST数据所使用的Content-type头信息：-T
栗子：
```php
ab -c100 -n10000 -p index.txt -T "application/x-www-form-urlencoded"  http://dev.host.net/
```
index.txt 里面是请求参数：如下
```php
username=choudalao&pwd=123456
```

##### 显示请求的显示详细程度,默认是只显示上面已完成请求数等：-v

-v1 默认值为1,只显示请求的总统计
-v2 显示响应头,响应数据,并包含1的显示
-v3 显示响应状态码,并包含2的显示
-v4 显示更多信息

##### 添加cookie：-C
```php
-C "cookie1=cookie1,cookie2=cookie2"
```
##### 以html表格的元素显示ab的测试结果：-w


## 测试栗子及说明
命令：
```php
ab -c1000 -n100000 http://dev.host.net/
```
结果：
```php
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking dev.host.net (be patient)
Completed 10000 requests #已经完成的请求数
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        nginx/1.15.11 # nginx 版本（服务器名称）
Server Hostname:        dev.host.net #请求的URL主机名
Server Port:            80 #端口号
# SSL/TLS Protocol: TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256 //SSL/TLS 协议
# TLS Server Name: youxi.test # TLS服务器名
Document Path:          / #请求路径
Document Length:        327 bytes #响应数据长度

Concurrency Level:      1000 #并发数,我们自己设置的-c参数
Time taken for tests:   260.292 seconds #请求完成时间
Complete requests:      100000 #完成请求数
Failed requests:        96673 #错误请求数
   (Connect: 0, Receive: 0, Length: 96673, Exceptions: 0)  
Non-2xx responses:      95644  
Total transferred:      31248236 bytes  #整个场景中的网络传输量
HTML transferred:       16095964 bytes #html响应总长度(去除了响应头的长度)
Requests per second:    384.18 [#/sec] (mean)  #每秒处理的请求数，相当于 LR 中的 每秒事务数 ，后面括号中的 mean 表示这是一个平均值
Time per request:       2602.921 [ms] (mean) #用户平均请求等待时间，相当于 LR 中的 平均事务响应时间 ，后面括号中的 mean 表示这是一个平均值
Time per request:       2.603 [ms] (mean, across all concurrent requests)  #服务器平均处理时间
Transfer rate:          117.24 [Kbytes/sec] received #带宽传输速度，可以帮助排除是否存在网络流量过大导致响应时间延长的问题

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2  33.0      0     507
Processing:  1006 2556 283.2   2397    4679
Waiting:     1005 1865 454.6   1789    4668
Total:       1008 2559 284.0   2397    4679

Percentage of the requests served within a certain time (ms)
  50%   2397
  66%   2842
  75%   2864
  80%   2874
  90%   2909
  95%   2948
  98%   2992
  99%   3014
 100%   4679 (longest request)
 
# 整个场景中所有请求的响应情况。在场景中每个请求都有一个响应时间，其中50％的用户响应时间小于2397 毫秒，66％ 的用户响应时间小于2842 毫秒，最大的响应时间小于4679 毫秒
```
测试结果显示：nginx吞吐率为：Requests per second: 384.18 [#/sec] (mean)。

通过上面的数据可分析出服务器响应情况,并发处理能力,尤其是`Requests per second `参数,它确定了服务器的秒并发能力。
###### 性能指标`Requests per second`吞吐率越高，服务器性能越好。

## 查看服务器相关数据
##### 查看Web服务器（Nginx Apache）的并发请求数及其TCP连接状态：   
 ```php
   netstat -n |awk '/^tcp/ {++S[$NF]}END{for(a in S)print a,S[a]}'
```
或者
  ```php
  netstat -n|grep  ^tcp|awk '{print $NF}'|sort -nr|uniq -c   
```
或者：
```php
netstat -n |awk '/^tcp/ {++state[$NF]} END {for(key in state) print key,"t",state[key]}'
```
返回结果一般如下：   
*LAST_ACK 5 （正在等待处理的请求数）
ESTABLISHED 1597 （正常数据传输状态） FIN_WAIT1 51 FIN_WAIT2 504 
TIME_WAIT 1057 （处理完毕，等待超时结束的请求数）   *

>    其他参数说明：   
    CLOSED：无连接是活动的或正在进行
    LISTEN：服务器在等待进入呼叫 
    SYN_RECV：一个连接请求已经到达，等待确认
    SYN_SENT：应用已经开始，打开一个连接 
    ESTABLISHED：正常数据传输状态 
    FIN_WAIT1：应用说它已经完成 
    FIN_WAIT2：另一边已同意释放 
    ITMED_WAIT：等待所有分组死掉 
    CLOSING：两边同时尝试关闭 
    TIME_WAIT：另一边已初始化一个释放 
    LAST_ACK：等待所有分组死掉    LAST_ACK 5 （正在等待处理的请求数）
    ESTABLISHED 1597 （正常数据传输状态） FIN_WAIT1 51 FIN_WAIT2 504 
    TIME_WAIT 1057 （处理完毕，等待超时结束的请求数）   
	
##### 查看Nginx运行进程数 
```php
ps -ef |grep nginx|wc -l
```
##### 返回的数字就是nginx的运行进程数，如果是apache则执行  
```php
 ps -ef |grep httpd|wc -l
```
##### 查看Web服务器进程连接数： 
```php
netstat -antp|grep 80|grep ESTABLISH -c
```
#####查看MySQL进程连接数：
```php
ps -axef|grep mysqld -c
```