---
title: "Warning: (1366, \"Incorrect string value: '\\\\xD6\\\\xD0\\\\xB9\\\\xFA\\\\xB1\\\\xEA...' for column 'VARIABLE_VALUE' at row 518\")   result = self._query(query)"
date: 2020-03-19T00:15:00+08:00
updated: 2026-02-23T16:07:16+08:00
author: "臭大佬"
categories: [Python]
description: "Warning: (1366, \"Incorrect string value: '\\\\xD6\\\\xD0\\\\xB9\\\\xFA\\\\xB1\\\\xEA...' for column 'VARIABLE_VALUE' at row 518\")
  result = self._query(query)"
cover: "https://www.choudalao.com/uploads/20200319/jhewy7UVggVGI9z4TpvQsp1x5e0r1XngV0fY3erm.jpeg"
click: 5422
---

# 问题
** Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 518")
  result = self._query(query)**

![](https://www.choudalao.com/uploads/20200319/20200319000450oEwZDL.png)

# 解决
安装mysql-connector-python驱动
```python
pip install mysql-connector-python
```
![](https://www.choudalao.com/uploads/20200319/20200319000548rVXpW1.png)

```python
# 连接方式替换掉
#create_engine("mysql+pymysql://root:root@127.0.0.1:3306/python_test?charset=utf8mb4",)  改成
create_engine("mysql+mysqlconnector://root:root@127.0.0.1:3306/python_test?charset=utf8mb4")
```
# 运行的代码
```python
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

# Base是declarative_base的实例化对象
Base = declarative_base()
# 定义一个常量
ENGINE = create_engine("mysql+mysqlconnector://root:root@127.0.0.1:3306/python_test")

# 每个类都要继承Base
class Users(Base):
    __tablename__ = 'users'
    # Column是列的意思，固定写法 Column(字段类型, 参数)
    # primary_key主键、index索引、nullable是否可以为空
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    # 相当于Django的ORM的class Meta，是一些元信息
    __table_args__ = (

    )

def init_db():
    # metadata.create_all创建所有表
    Base.metadata.create_all(ENGINE)

def drop_db():
    # metadata.drop_all删除所有表
    Base.metadata.drop_all(ENGINE)


if __name__ == '__main__':
    init_db()

```
![](https://www.choudalao.com/uploads/20200319/20200319001406ySM3ij.png)