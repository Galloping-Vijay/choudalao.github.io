---
title: "beego 获取 axios 请求数据 | 臭大佬"
date: 2020-08-24T01:15:08+08:00
updated: 2026-02-23T17:02:02+08:00
author: "臭大佬"
categories: [Go]
description: "发现一个很奇怪的问题，`Beego`中用`GetString(key string) string`无法获取`Axios`请求数据。"
cover: "https://www.choudalao.com/uploads/20200824/Lz2t8fYwF5HflUcjPc5mSAOp24xCNhVwkOogopfy.jpeg"
click: 4014
---

# 开发环境
前端：Vue
后端：Beego

# 问题

发现一个很奇怪的问题，`Beego`中用`GetString(key string) string`无法获取`Axios`请求数据。

`Beego`中用`GetString(key string) string`获取请求参数,使用工具`apizza`(类似于postman的工具)发起请求，可以正常得到数据：

```go
# admin.go 中接收数据的代码


func (self *AdminController) Login() {
	...
	inputData := map[string]string{}

	inputData["username"] = username
	inputData["password"] = password
	// 返回参数
	self.ResJson(1, "获取数据", inputData, nil)
	
}
```
![](https://www.choudalao.com/uploads/20200824/20200824004214Le8vxC.png)

返回结果：

![](https://www.choudalao.com/uploads/20200824/20200824003846gAZWrF.png)

而当在前端使用`axios `传递参数时，发现无法获取：

![](https://www.choudalao.com/uploads/20200824/20200824004448Rk1wdW.png)
![](https://www.choudalao.com/uploads/20200824/20200824004453sH1xHu.png)

前端代码之前是请求`php`获取数据，之前在`php`接口端是可以获取到请求参数的。这就很奇怪了，网上找了一圈都没有找到比较好的答案。在一个帖子里面看到，`ajax`和`axios`请求数据的格式是不同的,然后特意写了个页面研究一下。
```go
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"> 
<title>请求方式对比</title> 
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
<script>
$(document).ready(function(){
    var data =  {
        username: 'Fred',
        password: 'Flintstone'
    }
  $("#p1").click(function(){
    $.post("http://localhost:8181/api/admin/login",data,
    function(data,status){
        console.log(data);
    });
  });
 
  $("#p2").click(function(){
    axios.post('http://localhost:8181/api/admin/login',data
    )
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    });
  })
});
</script>
</head>
<body>
<p id="p1">ajax 请求</p>
<p id="p2">axios 请求</p>
</body>
</html>
```
上面的两个请求方式，发现`ajax`请求可以返回结果，而`axios`请求无法得到参数。

# 解决

默认情况下，`jquery`的`ajax`，`Content-Type`是`application/x-www-form-urlencoded`，

`axios`的话会做判断，如果`data`是字符串，`Content-Type`是`application/x-www-form-urlencoded`，如果`data`是对象，`Content-Type是application/json`，

所以`axios`要和默认`ajax`请求一样，需要把`data`以`key=value&key1=value1`形式传递，同时，`headers`的`content-type`参数修改为`application/x-www-form-urlencoded`

解决方案有两种，一种是在前端把`axios`参数修改为后端能够用`GetString(key string) string`获取得到的形式（ajax比较通用），二是后端做个兼容，既能接收`ajax`的参数，又能获取到`axios`请求的参数。

### 前端解决方案

需要修改的地方有两处，
1：参数以`key=value&key1=value1`形式传递；
2：`headers`的`content-type`参数修改为`application/x-www-form-urlencoded`

```go
axios.post('http://localhost:8181/api/admin/login',
'username=ssss&password=12345', {
        headers: {'content-type':'application/x-www-form-urlencoded'}
    })
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    });
```
![](https://www.choudalao.com/uploads/20200824/20200824010437mfaXXx.png)

### 后端解决方案

在配置文件`app.conf`中加上如下代码：
```go
# 获取ajax提交的json数据，不然全是空的
copyrequestbody = true
```

用`GetString`接收常规参数，用`json`接收`axios`传递的参数，获取参数代码如下：
```go

// 如果参数名和模型中的字段相同，可以用模型 struct 代替
type InputData struct {
	Username string
	Password string
}

//用户登录
func (self *AdminController) Login() {
	var Input InputData
	// 获取字符串形式的参数，用于ajax
	username := self.GetString("username")
	password := self.GetString("password")

	if username == "" && password == "" {
		// 获取 axios 传递的参数
		data := self.Ctx.Input.RequestBody
		err := json.Unmarshal(data, &Input)
		if err != nil {
			self.ResJson(1, "存入失败", err.Error(), nil)
		}
		username = Input.Username
		password = Input.Password
	}
	//...
	
}
```

##### 注意，前后端方案只需要改其中一个，不需要两边都进行修改。