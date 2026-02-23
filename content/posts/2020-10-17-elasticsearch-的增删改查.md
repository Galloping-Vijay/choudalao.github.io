---
title: "Elasticsearch 的增删改查"
date: 2020-10-17T15:08:32+08:00
updated: 2026-02-23T19:19:23+08:00
author: "臭大佬"
categories: [其他]
description: "Elasticsearch 的增删改查"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3860
---

# ES概念
`Elasticsearch`是一个开源的搜索引擎，分布式的实时文件存储，可以处理PB级结构化或非结构化数据， 我们可以通过简单的`RESTful API`来完成各种操作。

### 全文搜索(Full-text Search)
  全文检索是指计算机索引程序通过扫描文章中的每一个词，对每一个词建立一个索引，指明该词在文章中出现的次数和位置，当用户查询时，检索程序就根据事先建立的索引进行查找，并将查找的结果反馈给用户的检索方式。
 
### 倒排索引（Inverted Index）
  该索引表中的每一项都包括一个属性值和具有该属性值的各记录的地址。由于不是由记录来确定属性值，而是由属性值来确定记录的位置，因而称为倒排索引(`inverted index`)。`Elasticsearch`能够实现快速、高效的搜索功能，正是基于倒排索引原理。

### 节点 & 集群（Node & Cluster）
`Elastic` 本质上是一个分布式数据库，允许多台服务器协同工作，每台服务器可以运行多个 `Elastic` 实例。单个 `Elastic` 实例称为一个节点（`node`），一组节点构成一个集群（`cluster`）。

### 索引（Index）
对应关系型数据库的一个数据库，索引必须为小写。使用下面的命令可以查询当前节点中所有索引：
curl -X GET 'http://localhost:9200/_cat/indices?v'

查出来提示` health status index uuid pri rep docs.count docs.deleted store.size pri.store.size` 说明还未创建索引。

### 类型（Type）
一个逻辑分组，我的理解type就相当于一个类，这个类下的数据都是这个类的实例，也就是这个分组下的数据格式都相似。

###  Document(文档)
Document(文档)，是一组json数据，类似代码中一个类的所有属性。如：
`{ "name": "James", "age": 34 }`

ES就是面向文档的，和代码中面向对象类似，它就是存储一个个文档（对象）。

# ES数据操作

如果在`win`下，使用`cmd`运行`curl xxx`提示：
~~'curl' 不是内部或外部命令，也不是可运行的程序或批处理文件。~~
如果有装`git`，可以直接使用`git`客户端运行。

### 添加和更新数据
比如需要存储上面的数据，命令如下：
```php
curl -H "Content-Type: application/json" -X PUT http://localhost:9200/project/person/1 -d '{"name":"Vijay","age":18}'
```
其中 `project`就是一个`index`（相当于一个库），`person`是`type`,相当于一个类（表），1是这个文档的`id`（表中一条数据的`id`）。执行上面的操作时如果`index`、`type`、`id`等不存在则会自动创建，如果这条id的数据已经存在则是更新这条数据。

数据返回如下：
```php
{
    "_index":"project",
    "_type":"person",
    "_id":"1",
    "_version":4,
    "result":"updated",
    "_shards":{
        "total":2,
        "successful":1,
        "failed":0
    },
    "_seq_no":3,
    "_primary_term":1
}
```

服务器返回的 `JSON` 对象，会给出 `Index`、`Type`、`Id`、`Version` 等信息。其中`result`的值为`updated`，说明这条`id`的数据已经存在，所以这次再插入就是更新。

新增记录的时候，如果不指定`Id`，这时要改成 `POST` 请求，会随机生成一个`id`。

##### 通过 _update  API的方式单独更新你想要更新的
```php
// 把id为1数据的age更新为40（原来是35）
curl -H "Content-Type: application/json" -XPOST http://localhost:9200/project/person/1/_update -d '{"doc":{"age":"40"}}'

// 查看id为1的age字段
curl http://localhost:9200/project/person/1?_source=age

// 结果
{"_index":"project","_type":"person","_id":"1","_version":3,"_seq_no":10,"_primary_term":1,"found":true,"_source":{"age":"40"}}
```
POST不能改为PUT，_update表示更新操作，-d 中的 doc 表示对文档进行更新。

使用script也可以直接对某个id进行更新，注意字段格式为：`ctx._source.xxx`，实现同样的效果：
```php
// 更新数据
curl -H "Content-Type: application/json" -XPOST http://localhost:9200/project/person/1/_update?pretty -d '{"script":"ctx._source.age = 50"}'

// 查询
curl http://localhost:9200/project/person/1?_source=age

// 结果
{"_index":"project","_type":"person","_id":"1","_version":4,"_seq_no":11,"_primary_term":1,"found":true,"_source":{"age":50}}
```

### 删除数据

删除数据命令如下：
```php
curl -X DELETE http://localhost:9200/project/person/1
```
结果：

```php
{
    "_index":"project",
    "_type":"person",
    "_id":"1",
    "_version":5,
    "result":"deleted",
    "_shards":{
        "total":2,
        "successful":1,
        "failed":0
    },
    "_seq_no":4,
    "_primary_term":1
}
```

### 查询记录

查询命令如下：

```php
curl http://localhost:9200/project/person/1
```
后面可以加参数,
?pretty=true 表示以易读格式返回
返回的易读格式如下：
```php
{
  {
  "_index" : "project",
  "_type" : "person",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 4,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "name" : "James",
    "age" : 35
  }
}

```
如果index、type、id不正确返回的found值就是false。

`_source`获取指定的字段：

```php
// curl http://localhost:9200/project/person/1?_source=age

{
    "_index":"project",
    "_type":"person",
    "_id":"1",
    "_version":2,
    "_seq_no":6,
    "_primary_term":1,
    "found":true,
    "_source":{
        "age":35
    }
}
```

# ES中的搜索
### 查询全部数据
使用 GET 方法，直接请求/Index/Type/_search，就会返回所有记录。

```php
curl http://localhost:9200/project/person/_search?pretty=true
```

返回结果：
```php
{
    "took":97,
    "timed_out":false,
    "_shards":{
        "total":1,
        "successful":1,
        "skipped":0,
        "failed":0
    },
    "hits":{
        "total":{
            "value":3,
            "relation":"eq"
        },
        "max_score":1,
        "hits":[
            {
                "_index":"project",
                "_type":"person",
                "_id":"1",
                "_score":1,
                "_source":{
                    "name":"James",
                    "age":35
                }
            },
            {
                "_index":"project",
                "_type":"person",
                "_id":"2",
                "_score":1,
                "_source":{
                    "name":"vijay jay",
                    "age":20
                }
            },
            {
                "_index":"project",
                "_type":"person",
                "_id":"3",
                "_score":1,
                "_source":{
                    "name":"vijay",
                    "age":18
                }
            }
        ]
    }
}
```
返回结果中：
- took字段表示该操作的耗时（单位为毫秒）。
- timed_out字段表示是否超时。
- hits字段表示搜到的记录，数组形式。
- total：返回记录数，本例是1条。
- max_score：最高的匹配程度，本例是1.0。

### 条件查询

可以在url上加上参数进行检索：
```php
curl -H "Content-Type: application/json" -XGET http://localhost:9200/project/person/_search?q=name:Vijay 
```
表示查询name有Vijay的数据。经测试，发现这里是模糊查询，查询到的结果名字有Vijay和vijay jay，
返回结果，不格式化了，太占位置了....
```php
{"took":1,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":2,"relation":"eq"},"max_score":0.38845783,"hits":[{"_index":"project","_type":"person","_id":"3","_score":0.38845783,"_source":{"name":"vijay","age":18}},{"_index":"project","_type":"person","_id":"2","_score":0.2863813,"_source":{"name":"vijay jay","age":20}}]}}
```

由于查询条件是json,前面要加上请求头，参数格式为：{“query”:{“match”:{“name”:"vijay jay"}}}，

```php
curl -H "Content-Type: application/json" http://localhost:9200/project/person/_search?pretty=true -d '{"query":{"match":{"name":"vijay jay"}}}'
```
默认一次返回10条结果，可以通过size字段改变这个设置：
参数:`{"query":{"match":{"name":"vijay jay"}},"from":10, "size":1}`表示从第`10`条结果开始返回一条。

match 并不是准确检索，而是不完全匹配，只要匹配上参数中的任何一个分词，都会返回。
参数：`{“query”:{“match”:{“name”:"vijay jay"}}}`
表示查询`name`有`vijay`、`jay`、`vijay jay`三种的结果都会返回。

如果仅仅期望找到其中完全匹配的信息，则需要使用 `match_phrase` ：

```php
{"query": {"match_phrase": {"name": "vijay jay"}}}
```
这个命令只会返回`name`严格等于”`vijay jay`”的文档。

### 范围检索
-d 前面不变，后面的json串为：
```php
{
    "query":{
        "bool":{
            "filter":{
                "range":{
                    "age":{
                        "gt":"18"
                    }
                }
            },
            "must":{
                "match":{
                    "name":"vijay"
                }
            }
        }
    }
}
```
其中，bool下包含两个条件：
- age大于”18”
- name=”vijay”的数据

从上面全部数据可以看出，我的数据里面有三条数据，`name`带有`vijay`的有两条，但是同时`age`大于`18`的只有一条，结果如下

```php
// curl -H "Content-Type: application/json" http://localhost:9200/project/person/_search?pretty=true -d '{"query": {"bool": {"filter": {"range": {"age": { "gt": "18" } }},"must": {"match": {"name": "vijay" }}}}}'

{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.39019167,
    "hits" : [
      {
        "_index" : "project",
        "_type" : "person",
        "_id" : "2",
        "_score" : 0.39019167,
        "_source" : {
          "name" : "vijay jay",
          "age" : 20
        }
      }
    ]
  }
}

```

### AND、OR、NOT的用法
这属`于bool query`，是一种复合查询，逻辑的最外层由”`bool`”包裹。支持以下三种逻辑关系：
- must： AND
- must_not：NOT
- should：OR

比如想要查询年龄为`18`，并且`name`有”vijay”或”James”的文档，则可以用：
```php
{
    "query":{
        "bool":{
            "should":[
                {
                    "term":{
                        "age":18
                    }
                },
                {
                    "bool":{
                        "must":[
                            {
                                "term":{
                                    "name":"vijay"
                                }
                            },
                            {
                                "term":{
                                    "name":"James"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
}
```
返回结果：

```php
// curl -H "Content-Type: application/json" http://localhost:9200/project/person/_search?pretty=true -d '{"query" : {"bool" : {"should" : [{ "term" : {"age" : 18}},{ "bool" : {"must" : [{"term" : {"name" : "vijay"}},{"term" : {"name" : "James"}}]}}]}}}'

{
  "took" : 19,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "project",
        "_type" : "person",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "vijay",
          "age" : 18
        }
      }
    ]
  }
}
```

### 其他查询参数
在下面的例子里，我们指定了要返回结果的数量、偏移位置（对分页有用）、要返回的字段和高亮显示的项。

```php
// _source获取指定的字段
{
    "query":{
        "match":{
            "name":"vijay"
        }
    },
    "size":2,
    "from":0,
    "_source":[
        "age"
    ],
    "highlight":{
        "fields":{
            "age":{

            }
        }
    }
}
```

返回结果：

```php
// curl -H "Content-Type: application/json" http://localhost:9200/project/person/_search?pretty=true -d '{"query": {"match" : {"name": "vijay"}},"size": 2,"from": 0,"_source": [ "age"],"highlight": {"fields" : {"age" : {}}}}'

{
  "took" : 36,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 0.52354836,
    "hits" : [
      {
        "_index" : "project",
        "_type" : "person",
        "_id" : "3",
        "_score" : 0.52354836,
        "_source" : {
          "age" : 18
        }
      },
      {
        "_index" : "project",
        "_type" : "person",
        "_id" : "2",
        "_score" : 0.39019167,
        "_source" : {
          "age" : 20
        }
      }
    ]
  }
}
```

# 声明
文章参考：
https://blog.csdn.net/weixin_44993178/article/details/92400425

https://blog.csdn.net/HappyRocking/article/details/81172664?depth_1-

https://www.cnblogs.com/DreamDrive/p/6819449.html