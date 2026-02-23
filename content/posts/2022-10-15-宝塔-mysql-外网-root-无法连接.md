---
title: "宝塔 mysql 外网 root 无法连接"
date: 2022-10-15T23:08:16+08:00
updated: 2026-02-23T09:07:59+08:00
author: "臭大佬"
categories: [linux]
description: "宝塔 mysql 外网 root 无法连接"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3587
---

# 问题
默认情况下，宝塔里数据库的 root 账号是无法访问数据库的，如果用各个库去连接的话，又多又麻烦，所以，像测试库或者本地，不需要考虑安全因素的，完全可以直接用 root账号来管理。

# 解决
### 前提
数据库端口（默认是3306）已经放行，

### 配置

#### mysql5.7
```go
# 进入终端连接到服务器
mysql -u root -p
# 输入密码
use mysql;
# 授权root用户对所有数据库在任何ip都可以进行操作
grant all on *.* to root@'%' identified by '123456' with grant option;
# 刷新数据库
flush privileges;
```

#### mysql8.0
```go
# 使用root用户进入数据库 输入上面复制的root密码
mysql -u root -p;
# 输入密码
# 使用mysql
use mysql;
# 查看数据
select User,Host,plugin,password from user;
# 更新root用户权限，“%”指的是所有地址都可以访问
update user set Host='%' where User='root' and host='localhost';
# 更新密码
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root12345';

# 刷新权限
flush privileges;

# 如果无法操作,
# 删除数据库,重新安装
rm -rf /www/server/mysql
```