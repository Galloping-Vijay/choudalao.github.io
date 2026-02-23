---
title: "RESTful API风格"
date: 2021-01-15T11:46:15+08:00
updated: 2026-02-23T09:23:23+08:00
author: "臭大佬"
categories: [php]
description: "RESTful API风格"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4125
---

## 什么是 RESTful API 风格
一种软件架构风格、设计风格，而不是标准，只是提供了一组设计原则和约束条件。它主要用于客户端和服务器交互类的软件。基于这个风格设计的软件可以更简洁，更有层次，更易于实现缓存等机制。

## 为什么要用 RESTful API风格
	适用于前后端分离，后端组专注于业务功能的开发，提高开发效率。
	近年随着移动互联网的发展，各种类型的客户端层出不穷，Restful可以通过一套统一的接口为PC、微信(H5)、IOS和Android提供服务，这样的接口不需要前端样式，只提供数据。其实就是，后端一套代码，适配所有的端。

![](https://www.choudalao.com/uploads/20210115/20210115110649mkVr0d.png)

## 如何设计Restful风格的API
RestfulAPI就是由后台(SERVER端)来提供接口，前端来调用。前端调用API向后台发起HTTP请求，后台响应请求将处理结果反馈给前端。也就是说Restful 是典型的基于HTTP的协议。

### RESTful API 特征
#### Resource 资源
资源就是网络上的一个实体、一段文本、一张图片或者一首歌曲。资源总是要通过一种载体来反应它的内容。文本可以用TXT，也可以用HTML或者XML、图片可以用JPG格式或者PNG格式，JSON是现在最常用的资源表现形式。
#### 统一接口
Restful风格的数据元操作CRUD(create,read,update,delete)分别对应HTTP方法：GET用来获取资源，POST用来新建资源(也可以用于更新资源)，PUT(PATCH)用来更新资源，DELETE用来删除资源，这样就统一了数据操作的接口。

> PATCH和PUT方法的区别？
PUT全部更新资源，举个栗子，user里面有id、name、email等字段，PUT更新资源，要求前端提供的一定是一个完整的资源对象，也就是整个user，如果前端缺少字段，那么缺了的字段会被清空。

> PATCH是局部更新资源，后端仅更新接收到的字段。，比如 user现在只需更新name字段，那么后端只会更新user的name字段，前端传什么字段，后端只更新传过来的字段值。

> 补充一下，PATCH 与 PUT 属性上的一个重要区别还在于：PUT 是幂等的，而 PATCH 不是幂等的。

#### HTTP状态码
在REST中都有特定的意义：200，201，202，204，400，401，403，500。比如401表示用户身份认证失败，403表示你验证身份通过了，但这个资源你不能操作。

#### 无状态
所谓无状态即所有的资源都可以URI定位，而且这个定位与其他资源无关，也不会因为其他资源的变化而变化。

Restful 是典型的基于HTTP的协议，HTTP连接最显著的特点是客户端发送的每次请求都需要服务器回送响应，在请求结束后，会主动释放连接。从建立连接到关闭连接的过程称为“一次连接”。前面一次请求与后面一次请求没有必然的联系，所以是无状态的。

#### 版本号
将API的版本号放入URL。GET:http://www.choudalao.com/v1/article/123。或者将版本号放在HTTP头信息中，我个人觉得版本号能够较好的控制缓存问题，推荐放在HTTP头信息中。

#### 过滤信息
如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。如`limit`、`page`等。

#### 规范返回的数据
为了保障前后端的数据交互的顺畅，建议规范数据的返回，并采用固定的数据格式封装。
```json
{
    "data":{

    },
    "msg":"uri_not_found",
    "code":10001,
    "request":"GET/v1/article/230"
}
```

#### 方便测试
采用Restful风格的API可以方便测试，便于apizz、swagger等构建文档。