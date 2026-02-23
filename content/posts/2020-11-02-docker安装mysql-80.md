---
title: "Docker安装Mysql 8.0"
date: 2020-11-02T23:21:21+08:00
updated: 2026-02-23T17:26:37+08:00
author: "臭大佬"
categories: [MYSQL]
description: "Docker安装Mysql 8.0"
cover: "https://www.choudalao.com/uploads/20201130/o1uq0vCLQymsRCI3FfDfRncr0oU6fizBkWZbXz7O.jpeg"
click: 2088
---

# 前提

已安装 docker

# 查看可用的Mysql镜像版本
登陆 https://hub.docker.com/
搜索 `mysql`,切换到tag标签,找到 mysql8.0
![](https://www.choudalao.com/uploads/20230119/202301191637316A4hdz.png)
复制箭头的命令
### 拉取镜像
```go
docker pull mysql:8.0
```
![](https://www.choudalao.com/uploads/20230119/20230119163934MTTvEn.png)
### 查看镜像
```go
docker images
```
![](https://www.choudalao.com/uploads/20230119/20230119163946qMTFhS.png)

### 启动Mysql镜像
```go
docker run -itd --name mysql-8 -p 3307:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:8.0
```

参数说明：

–name mysql-8：所建容器的名称
-p 3307:3306 ：映射容器服务的 3306 端口到宿主机的 3307 端口，外部主机可以直接通过 宿主机ip:3307 访问到 MySQL 的服务。
MYSQL_ROOT_PASSWORD=123456：设置 MySQL 服务 root 用户的密码
mysql:8.0：使用的镜像，即镜像名：tag

### 启动后：查看容器
```go
docker ps
```
![](https://www.choudalao.com/uploads/20230119/20230119164227SBNkBu.png)
### 进入镜像
```go
docker exec -it mysql-8 /bin/bash
```
### 登陆Mysql
```go
mysql -uroot -p
```
默认密码一般是123456
### 切换数据库
```go
use mysql
```
### 查看用户数据
```go
select host,user,plugin from user;
```
![](https://www.choudalao.com/uploads/20230119/20230119164520Q2NIRi.png)

### 删除多余的行
```go
delete from user where user ='root' and host='%';
```
![](https://www.choudalao.com/uploads/20230119/20230119164656iTdVKs.png)

### 设置所有host都可以访问
```go
update user set host='%' where user ='root';
```
### 修改加密方式
```go
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
```
![](https://www.choudalao.com/uploads/20230119/202301191648520GIoDm.png)

### 刷新
```go
FLUSH PRIVILEGES;
```

# 问题

## ERROR 1040 (HY000): Too many connections
mysql8默认连接数不够了.

### 方法一 
这种方法重启mysql会失效
进入容器
```go
docker exec -it mysql-8 sh
```
进入mysql
```go
mysql -hlocalhost -uroot -p12345
```
查看最大连接数
```go
SHOW VARIABLES LIKE 'max_connections';
```
当前状态的连接数量
```go
show global status like 'Max_used_connections';
```
修改连接数 （重启mysql服务后会失效）
```go
set global max_connections=1000;
```

### 方法二
把容器里面的配置文件拷贝出来
```go
docker cp mysql-8:/etc/my.cnf /www/wwwroot/sh/mysql8/etc/my.cnf
```

修改本地的配置文件my.cnf
```go
[mysqld]
max_connections=1000
```
修改的时候注意,`max_connections=1000`要在`[mysqld]`下面,不然可能不生效.

拷贝到容器中,并重启
```go
docker cp /www/wwwroot/sh/mysql8/etc/my.cnf mysql-8:/etc/my.cnf
```
```go
docker restart mysql-8
```
## 时区问题
我们通常在创建Mysql容器时忘记选择时区，这时docker就会默认给我们选择UTC时区。我们这时又不想删掉这个容器，所以我们需要修改mysql中的时区。

进入mysql命令行:
```go
select now();
```
查看时间是否有差,如果有在配置文件中加入如下配置:
```go
[mysqld]
# 其他配置...
default-time-zone = '+8:00'
```
然后用如上方法二,重启容器