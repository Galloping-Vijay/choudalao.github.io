---
title: "SELECT list is not in GROUP BY clause and contains nonaggregated column 'XXX' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by"
date: 2020-06-11T11:47:24+08:00
updated: 2026-02-23T21:06:35+08:00
author: "臭大佬"
categories: [php]
description: "laravel在使用groupBy查询数据的时候报错：SELECT list is not in GROUP BY clause and contains nonaggregated column 'XXX' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by"
cover: "https://www.choudalao.com/uploads/20200611/WGhrGyeSwYs7dHytJbkKkmZDl4CQEmcLuFDYsIQl.jpeg"
click: 5890
---

# 环境
php 7.2
laravel 5.7
mysql 5.7

# 问题
在使用laravel进行分组查询的时候，发现报错了，查询语句如下：
![](https://www.choudalao.com/uploads/20200611/202006111133374HHPYd.png)

报错如下：
```sql
Expression #10 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'gd_white_ip_list_bmdapis.id' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```
![](https://www.choudalao.com/uploads/20200611/20200611114032vquYNo.png)

# 方案
网上查了一下，解决方案主要有两种，
1：修改laravel数据库配置文件;
2：修改mysql配置文件。

推荐方案 1：修改laravel的database.php文件。为什么推荐这种方式呢？作为开发仔，直接修改代码是最直接的方式啦，还有就是，很多时候mysql等配置是运维在管理的，开发仔可能木有这方面的权限，而且，也不知道直接修改mysql配置文件，会不会影响线上别的项目，以及会不会产生不安全的漏洞等等。

## 修改laravel配置文件（推荐）


找到config/database.php,修改如下：
```sql
 'mysql' => [
 ...
	'strict' => true,
]
```
改成：
```sql
 'mysql' => [
 ...
	'strict' => false,
]
```
![](https://www.choudalao.com/uploads/20200611/20200611114607g3XowO.png)

再次运行代码。可以返回结果：

![](https://www.choudalao.com/uploads/20200611/20200611122344ebIWGZ.png)
![](https://www.choudalao.com/uploads/20200611/202006111147087LpTlR.png)
 


## 修改mysql配置
构造出sql语句到Navicat上运行，sql语句
```sql
select * from `gd_white_ip_lists` inner join `gd_white_ip_list_bmdapis` on `gd_white_ip_list_bmdapis`.`bmdiplist_id` = `gd_white_ip_lists`.`id` where `gd_white_ip_lists`.`type` = 1 and `gd_white_ip_lists`.`status` = 1 group by `gd_white_ip_lists`.`id
```

运行结果：
![](https://www.choudalao.com/uploads/20200611/20200611123320E47tT7.png)

### 步骤
进入mysql的bin目录下，输入账号密码
```shell
mysql -u root -p
```

![](https://www.choudalao.com/uploads/20200611/20200611124120MsBN2u.png)

在mysql命令行下执行以下语句： 
```shell
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
```

![](https://www.choudalao.com/uploads/20200611/20200611124203Bc06kk.png)

在mysql的配置文件（linux是my.cnf，win是my.ini）中加入以下内容：
```shell
sql_mode = "STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
```
修改完成后，重启mysql服务：
```shell
systemctl restart mysqld.service
```