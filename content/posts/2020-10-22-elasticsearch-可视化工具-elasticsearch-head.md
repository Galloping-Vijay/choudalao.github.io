---
title: "Elasticsearch 可视化工具 ElasticSearch-head"
date: 2020-10-22T20:11:19+08:00
updated: 2026-02-23T19:54:31+08:00
author: "臭大佬"
categories: [其他]
description: "Elasticsearch 可视化工具 ElasticSearch-head"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4889
---

# 安装
`ElasticSearch-head` 类似于 `mysql` 的 `phpMyAdmin`，可以让数据库中的数据一目了然。

`ElasticSearch-head` 基于node，需要先安装`node.js`，`node.js`下载地址：
[http://nodejs.cn/download/](http://nodejs.cn/download/ "http://nodejs.cn/download/")
安装很简单，一直 `next` 就行，这里`node.js`不是主角，直接跳过。

node.js安装好后运行命令安装 grunt

```shell
npm install -g grunt-cli
```
elasticsearch-head的github地址：[https://github.com/mobz/elasticsearch-head](https://github.com/mobz/elasticsearch-head "https://github.com/mobz/elasticsearch-head")

克隆到指定目录，然后进入目录执行

```shell
npm install
```
执行完成后，进入到`elasticsearch`的安装目录下的config目录，打开`elasticsearch.yml` 在末尾添加

```shell
# 开启跨域访问支持，默认为false
http.cors.enabled: true
# 跨域访问允许的域名地址，支持用正则
http.cors.allow-origin: "*"
```

完成之后重启ES 再运行就可以将期启动：

```shell
npm run start
```

> \> grunt server
Running "connect:server" (connect) task
Waiting forever...
Started connect web server on http://localhost:9100

打开浏览器输入：127.0.0.1:9100

![](https://www.choudalao.com/uploads/20201022/202010222055401WrCU5.png)

# 状态说明
集群健康值的几种状态如下：

- 绿色，最健康的状态，代表所有的分片包括备份都可用

- 黄色，基本的分片可用，但是备份不可用（也可能是没有备份）

- 红色，部分的分片可用，表明分片有一部分损坏。此时执行查询部分数据仍然可以查到，遇到这种情况，还是赶快解决比较好

- 灰色，未连接到elasticsearch服务


### 问题
如果一直都是未连接状态，可以参考：[elasticsearch-head 集群健康值: 未连接](https://zhuanlan.zhihu.com/p/128969541 "elasticsearch-head 集群健康值: 未连接")