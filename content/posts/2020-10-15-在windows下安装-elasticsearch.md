---
title: "在windows下安装 Elasticsearch"
date: 2020-10-15T12:08:35+08:00
updated: 2026-02-23T17:20:17+08:00
author: "臭大佬"
categories: [其他]
description: "在windows下使用 Elasticsearch"
cover: "https://www.choudalao.com/uploads/20201015/EhyKLAotxA2nsXqkwbQLJo3Hlr7iOtZTFJYUAGqK.jpeg"
click: 4008
---

# 介绍

Elasticsearch简称ES。 是一个全文搜索服务器，也可作为NoSQL数据库，存储任意格式的文档和数据，也可做大数据的分析，是一个跨界开源产品。

ES的特点：

　　全文搜索引擎

　　文档存储和查询

　　大数据分析

　　提供了REST API，用来简化对ES的操作

　　常常配合传统数据库一起使用，ES用来负责大数据的查询、搜索、统计分析。

# 安装

ElasticSearch 是基于 lucence 开发的，也就是运行需要java jdk支持。所以要先安装JAVA环境。

### java 安装
下载地址：https://www.oracle.com/java/technologies/javase-jdk15-downloads.html

![](https://www.choudalao.com/uploads/20201015/20201015134534LBmizS.png)

安装过程比较简单，这里不做展示，安装完成后，需要配置环境变量，比如我的安装目录是：D:\Program Files (x86)\java

![](https://www.choudalao.com/uploads/20201015/20201015115257BtHlsS.png)

新建变量，变量名JAVA_HOME（代表你的JDK安装路径），值对应的是你的JDK的安装路径。

```java
变量名：JAVA_HOME 
变量值：D:\Program Files (x86)\java
```

![](https://www.choudalao.com/uploads/20201015/20201015115352RueGXf.png)

验证是否成功 输入` set java_home`，会得到地址说明成功。

```php
λ set java_home
JAVA_HOME=D:\Program Files (x86)\java;
```

新建CLASSPATH的值配置如下：
```java
变量名：CLASSPATH  
变量值：%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar
（如果CLASSPATH存在；在后面加上：  ;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar）
```

编辑系统变量Path，添加如下
```java
%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;
```

![](https://www.choudalao.com/uploads/20201015/202010151208294t1MCg.png)

部分系统是这样拆成两条的

```java
%JAVA_HOME%\bin
%JAVA_HOME%\jre\bin
```

![](https://www.choudalao.com/uploads/20201202/20201202150910SoYNMw.png)


如果配置成功的话，打开cmd输入以下内容，会返回如下内容。

![](https://www.choudalao.com/uploads/20201015/20201015134949niNF40.png)

# ES 安装

配置好 java 后，我们就可以下载并运行Elasticsearch。

下载地址：https://www.elastic.co/cn/downloads/elasticsearch

![](https://www.choudalao.com/uploads/20201015/20201015135124lzdpBZ.png)

下载解压后，放到安装目录，注意，ElasticSearch安装的目录不能带有空格，比如我的，

![](https://www.choudalao.com/uploads/20201015/20201015135559SrBEkY.png)

进入bin目录下,双击执行elasticsearch.bat，出现 started 字样说明启动成功了。

![](https://www.choudalao.com/uploads/20201015/20201015140427LsBslD.png)

图中标记部分，其中包含有关可从中访问节点的HTTP地址（127.0.0.1）和端口（9200）的信息。默认情况下，Elasticsearch使用port 9200来提供对其REST API的访问。如有必要，可以配置此端口。

在浏览器中打开如上网址：http://127.0.0.1:9200/ ， 或者cmd中访问 ： `curl http://localhost:9200/`

![](https://www.choudalao.com/uploads/20201015/202010151409034QSLeA.png)

# 问题

## 问题一

##### could not find java in JAVA_HOME at
```php
#进入elasticsearch.bat文件所在目录，然后运行如下命令
elasticsearch.bat
```
出现如下错误：

>  elasticsearch.bat "could not find java in JAVA_HOME at "D:\Program\java\jdk;\bin\java.exe""
 
 ##### 解决方式
 把环境变量JAVA_HOME改个名字或去掉，就会使用自带的jdk，再次执行，就ok了。