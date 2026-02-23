---
title: "备份docker中的mysql8数据到本地"
date: 2023-05-03T11:40:06+08:00
updated: 2026-02-23T17:02:52+08:00
author: "臭大佬"
categories: [MYSQL]
description: "备份docker中的mysql8数据到本地"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 2576
---

# 摘要
如果没有备份，数据误操作将是灾难性的事件，作为开发要做好数据备份的习惯。最近测试数据库就被误操作了，导致运营辛辛苦苦上传的数据全没了。

# 原理
命令行的方式较为快捷。仅仅须要在命令行中使用`mysqldump`命令,命令如下:
```go
mysqldump -u <USERNAME> -p<PASSWORD> <DATABASE_NAME> > <BACKUP_FILE_NAME>.sql
```
其中，<USERNAME> 是用来连接数据库的用户名，<PASSWORD> 是该用户的密码，<DATABASE_NAME> 是要备份的数据库名称，<BACKUP_FILE_NAME> 是备份数据存放的文件名。

上述命令会将备份数据输出到一个 SQL 文件中保存。

# 脚本
写个脚本,每天执行一次,备份`docker`中的测试数据库,防止备份文件过多,删除超过5天的备份文件,代码如下:
```go
!/bin/bash

# Docker 容器名称或 ID
CONTAINER_NAME_OR_ID="mysql-8"
# MySQL 用户名和密码
MYSQL_USERNAME="root"
MYSQL_PASSWORD="123456"
DATABASE_NAME="red"
# 本地备份文件路径
LOCAL_BACKUP_DIR="/www/wwwroot/sh/mysql8/backup/${DATABASE_NAME}"
# docker容器备份文件路径
DOCKER_BACKUP_DIR="/backup/${DATABASE_NAME}"
# 备份文件名（包含日期）
BACKUP_FILE_NAME="${DATABASE_NAME}.$(date +'%Y%m%d').sql"

# 确认并创建目录
mkdir -p ${LOCAL_BACKUP_DIR}
docker exec ${CONTAINER_NAME_OR_ID} /bin/sh -c "mkdir -p ${DOCKER_BACKUP_DIR}"

# 备份指定数据库到容器内部备份文件
docker exec ${CONTAINER_NAME_OR_ID} /bin/sh -c "mysqldump -u${MYSQL_USERNAME} -p${MYSQL_PASSWORD} ${DATABASE_NAME} > ${DOCKER_BACKUP_DIR}/${BACKUP_FILE_NAME}"

# 进入容器内部，执行 mysqldump 命令生成备份数据 备份所有数据
# docker exec ${CONTAINER_NAME_OR_ID} /bin/sh -c "mysqldump -u${MYSQL_USERNAME} -p${MYSQL_PASSWORD} --all-databases > ${DOCKER_BACKUP_DIR}/${BACKUP_FILE_NAME}"

# 下载备份文件到本地
docker cp ${CONTAINER_NAME_OR_ID}:${DOCKER_BACKUP_DIR}/${BACKUP_FILE_NAME} "${LOCAL_BACKUP_DIR}/${BACKUP_FILE_NAME}"

# 删除本地 5 天前的备份文件
find ${LOCAL_BACKUP_DIR} -maxdepth 1 -name "${DATABASE_NAME}.*.sql" -type f -mtime +4 -exec rm {} \;
# 删除docker容器中 5 天前的备份文件
docker exec ${CONTAINER_NAME_OR_ID} /bin/sh -c "find ${DOCKER_BACKUP_DIR} -maxdepth 1 -name '${DATABASE_NAME}.*.sql' -type f -mtime +4 -exec rm {} \;"

# 打印日志信息
echo "MySQL backup completed successfully!"

```

需要注意的是`-mtime +4`是文件更新的时间


### binlog操作
当无备份时,可以对binlog进行数据修复,
复制docker容器文件到本地
```go
docker cp mysql-8:/var/lib/mysql/binlog.000012 /backup/binlog/
```
把binlog文件解析成sql
```go
mysqlbinlog --base64-output=DECODE-ROWS binlog.000012 -v > 000012.sql
```
解析时间区间的数据
```go
mysqlbinlog --start-datetime='2023-04-01 00:00:00' --stop-datetime='2023-05-02 00:00:00' --base64-output=DECODE-ROWS -s binlog.000012 > output.sql
```

里面会有sql语句和操作信息,如`thread_id=xxx`,这个thread_id是操作连接的id,可以进去mysql命令,通过`SHOW PROCESSLIST;`查看所有的连接id,`SELECT connection_id();`查看当前连接的id.