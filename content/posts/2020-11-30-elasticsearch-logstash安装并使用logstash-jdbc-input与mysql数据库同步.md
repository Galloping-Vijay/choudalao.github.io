---
title: "ElasticSearch  logstash安装并使用logstash-jdbc-input与mysql数据库同步"
date: 2020-11-30T16:08:46+08:00
updated: 2026-02-22T10:04:56+08:00
author: "臭大佬"
categories: [其他]
description: "ElasticSearch  logstash安装并使用logstash-jdbc-input与mysql数据库同步"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4635
---

# 各软件版本及下载地址
java8 
https://pan.baidu.com/s/1YYQzYTx3kJ08jhK5lrcmKg 提取码：ihw1

elasticsearch-7.10.0-windows-x86_64
https://www.elastic.co/cn/downloads/elasticsearch

logstash-5.5.0
https://www.elastic.co/downloads/logstash

mysql-connector-java-5.1.36.jar
https://repo1.maven.org/maven2/mysql/mysql-connector-java/

`java `和 `Elasticsearch` 安装详见 [https://www.choudalao.com/article/207](在windows下安装 Elasticsearch "https://www.choudalao.com/article/207")


### Windows 部署 Logstash 概述

`Logstash `能够动态地采集、转换和传输数据，不受格式或复杂度的影响。利用`Grok` 从非结构化数据中派生出结构，从 `IP` 地址解码出地理坐标，匿名化或排除敏感字段，并简化整体处理过程。

`Logstash` 常与` Elasticsearch`、`kibana` 一起联合使用，三者合称 `ELK`。

`Logstash`是`ELK`的中央数据流引擎，用于从不同目标（文件/数据存储/MQ）收集的不同格式数据，经过过滤后支持输出到不同目的地。

`Logstash`版本需要与`ES`匹配，

### 安装

下载以下两个包
logstash-5.5.0
https://www.elastic.co/downloads/logstash

mysql-connector-java-5.1.36.jar
https://repo1.maven.org/maven2/mysql/mysql-connector-java/

**注意：网上很多教程让安装 `logstash-jdbc-input`， 我们安装的是5.X的版本，logstash5.x自带 `logstash-jdbc-input`，不需要我们去单独安装。**

`logstash`解压后，在根目录下创建一个配置目录，如` mysqletc`

![](https://www.choudalao.com/uploads/20201203/20201203155752SAhI57.png)

把`mysql-connector-java-5.1.36.jar`放到这个目录下，然后新建 `mysql.conf` ，内容如下：

```php
input {
    jdbc {
        # mysql 数据库链接,blog 为数据库名
        jdbc_connection_string => "jdbc:mysql://127.0.0.1:3306/blog"
        # 用户名和密码
        jdbc_user => "root"
        jdbc_password => "root"
        # 驱动
        jdbc_driver_library => "D:/Program/ES/logstash/mysqletc/mysql-connector-java-5.1.36.jar"
        # 驱动类名
        jdbc_driver_class => "com.mysql.jdbc.Driver"
        #启用分页，默认false
        jdbc_paging_enabled => "true"
        #页面大小，默认100000
        jdbc_page_size => "50000"
        #是否记录上次运行的结果
        record_last_run => true
        #记录上次运行结果的文件位置
        last_run_metadata_path => ""
        #是否使用数据库某一列的值，
        use_column_value => true
        tracking_column => "id"
        #numeric或者timestamp
        tracking_column_type => "numeric"
        #如果为true则会清除last_run_metadata_path记录，即重新开始同步数据
        clean_run => false
        # 执行的sql 文件路径+名称
        statement_filepath => "D:/Program/ES/logstash/mysqletc/test.sql"
        # 执行的sql 
        # statement => "SELECT * FROM rawData"
        #设置监听间隔。可以设置每隔多久监听一次什么的。
        #官方举例：
        #* 5 * 1-3 * 一月到三月的每天凌晨5点每分钟执行一次。
        #0 * * * *   将在每天每小时的第0分钟执行。
        #0 6 * * *   America/Chicago每天早上6:00（UTC / GMT -5）执行。
        #* * * * *   分、时、天、月、年，全部为*默认含义为每分钟查询一次
        # 设置监听间隔   各字段含义（由左至右）分、时、天、月、年，全部为*默认含义为每分钟都更新
        schedule => "* * * * *"
        # 索引类型
        type => "jdbc"
    }
}
# filter插件是logstash的主要功能之一，可以对logstash event进行丰富的处理。如类型转换、删除字段等。
filter {
    # json 按照json解析字段内容到指定字段中
    json {
        # source 要解析的字段名
        source => "message"
        # 解析后的存储字段
        remove_field => ["message"]
    }
}
# output 负责将数据输出到指定的位置
output {
    #输出到ES中，基于HTTP实现
    elasticsearch {
        #用户节点地址，这里对应我们的ES的IP地址和端口
        hosts => ["localhost:9200"]
        #索引名称
        index => "blog"
        #自增ID 需要关联的数据库中有有一个id字段，对应索引的id号
        document_id => "%{id}"
    }
    #stdout输出到标准输出，一般用于调试
    stdout {
        codec => json_lines
    }
}
```

如果要配置多个，可以参考如下：
```php
input {
  stdin {
  }

  jdbc {
  type => "news_info"
  #后面的test对应mysql中的test数据库
  jdbc_connection_string => "jdbc:mysql://127.0.0.1:3306/blog"
  jdbc_user => "root"
  jdbc_password => "root"
  tracking_column => "auto_id"
  record_last_run => "true"
  use_column_value => "true"
  #代表最后一次数据记录id的值存放的位置，它会自动在bin目录创建news,这个必填不然启动报错
  last_run_metadata_path => "news"
  clean_run => "false"

  # 这里代表mysql-connector-java-5.1.21.jar放在bin目录
  jdbc_driver_library => "D:/Program/ES/logstash/mysqletc/mysql-connector-java-8.0.22.jar"
  # the name of the driver class for mysql
  jdbc_driver_class => "Java::com.mysql.jdbc.Driver"
  jdbc_paging_enabled => "true"
  jdbc_page_size => "500"
  statement => "select * from wjf_articles"
#定时字段 各字段含义（由左至右）分、时、天、月、年，全部为*默认含义为每分钟都更新
  schedule => "* * * * *"
#设定ES索引类型
  }

    jdbc {
  type => "press_info"
  # mysql jdbc connection string to our backup databse 后面的test对应mysql中的test数据库
  jdbc_connection_string => "jdbc:mysql:////127.0.0.1:3306/wjf"
  jdbc_user => "root"
  jdbc_password => "root"
  tracking_column => "auto_id"
  record_last_run => "true"
  use_column_value => "true"
  last_run_metadata_path => "news"
  clean_run => "false"
  jdbc_driver_library => "D:/Program/ES/logstash/mysqletc/mysql-connector-java-8.0.22.jar"
  jdbc_driver_class => "Java::com.mysql.jdbc.Driver"
  jdbc_paging_enabled => "true"
  jdbc_page_size => "500"
  statement => "select * from wjf_articles"
#定时字段 各字段含义（由左至右）分、时、天、月、年，全部为*默认含义为每分钟都更新
  schedule => "* * * * *"
  }
}

filter {
mutate {
  convert => [ "publish_time", "string" ]
 }

date {
  timezone => "Europe/Berlin"
  match => ["publish_time" , "ISO8601", "yyyy-MM-dd HH:mm:ss"]
}
#date {
 # match => [ "publish_time", "yyyy-MM-dd HH:mm:ss,SSS" ]
  # remove_field => [ "publish_time" ]
  # }
json {
  source => "message"
  remove_field => ["message"]
  }
}

output {

if [type]=="news_info" {
  elasticsearch {
#ESIP地址与端口
  hosts => "127.0.0.1:9200"
#ES索引名称（自己定义的）
  index => "wantu_news_info"
#自增ID编号
  document_id => "%{auto_id}"
  }
}

if [type]=="press_info" {
  elasticsearch {
#ESIP地址与端口
  hosts => "127.0.0.1:9200"
#ES索引名称（自己定义的）
  index => "wantu_press_info"
#自增ID编号
  document_id => "%{auto_id}"
  }
}

}
```


新建 `test.sql` 文件，内容如下

```php
SELECT
	*
FROM
	wjf_articles
```

# 启动logstash

先启动`ES`和`elasticsearch-head`
```php
// 到ES的bin目录下执行
elasticsearch.bat
```
![](https://www.choudalao.com/uploads/20201203/20201203160815nmn2Nu.png)

```php
// 到elasticsearch-head目录下，我的是  D:\Program\ES\elasticsearch-head-master

npm run start
```
![](https://www.choudalao.com/uploads/20201203/20201203160627tZIID2.png)

```php
// 到logstash目录，进入bin目录，运行如下命令
logstash -f ../mysqletc/mysql.conf
```
![](https://www.choudalao.com/uploads/20201203/20201203160832RJxKGk.png)

# 结果

![](https://www.choudalao.com/uploads/20201203/20201203160904WkLVLY.png)

# 问题

### 问题一
> logstash-plugin.bat install logstash-input-jdbc
Cannot find Java 1.5 or higher.

### 解决方案
打开` logstash-plugin.bat`，在最上面加上你的`java_home`路径

`SET JAVA_HOME=D:\Program\java8`

![](https://www.choudalao.com/uploads/20201203/20201203100308oUzjqj.png)