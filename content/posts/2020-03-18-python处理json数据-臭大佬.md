---
title: "python处理json数据 | 臭大佬"
date: 2020-03-18T20:21:13+08:00
updated: 2026-02-23T16:05:22+08:00
author: "臭大佬"
categories: [Python]
description: "python处理json数据"
cover: "https://www.choudalao.com/uploads/20200318/4kRLKQybTQsgIe7DzC7TOAXbzA6wZ0wgBJ66mAlz.jpeg"
click: 2976
---

# 介绍
Python 对 json 文件的支持通过内置模块 json 来实现。
json 模块中主要两类四种方法：
- json.load(obj)：从一个 json 文件中加载 json 数据；
- json.loads(str)：从一个 json 字符串中加载 json 数据；
- json.dump()：将 json 数据编码为 json 字符串文件；
- json.dumps()：将 json 数据编码为 json 字符串

# 栗子
```python
# coding:utf-8
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.choudalao.com/"

wbdata = requests.get(url).text

soup = BeautifulSoup(wbdata, 'lxml')

news = soup.select("#body_app > article > div.blogs > ul > li > h3 > a")

with open('news.json', 'a', encoding='utf-8') as files:
    dataList = []
    for d in news:
        # 提取出标题和连接信息
        title = d.get_text()
        link = d.get("href")
        # 将提取出来的信息拼接为一个字典
        data = {
            '标题': title,
            '链接': link
        }
        dataList.append(data)
    data_json = {'data': dataList}
    # 解决中文乱码 ensure_ascii=False
    json.dump(data_json, files, ensure_ascii=False)

```