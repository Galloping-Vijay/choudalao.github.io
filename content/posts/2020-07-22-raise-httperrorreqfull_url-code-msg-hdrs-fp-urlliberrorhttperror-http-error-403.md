---
title: "raise HTTPError(req.full_url, code, msg, hdrs, fp) urllib.error.HTTPError: HTTP Error 403: Forbidden"
date: 2020-07-22T12:22:11+08:00
updated: 2026-02-23T16:47:09+08:00
author: "臭大佬"
categories: [Python]
description: "raise HTTPError(req.full_url, code, msg, hdrs, fp) urllib.error.HTTPError: HTTP Error 403: Forbidden"
cover: "https://www.choudalao.com/uploads/20200722/EqvVANNS5DSGXfO3GQFFul2aG6dnT8oc08WbS86N.jpeg"
click: 5134
---

# 问题
使用 `urllib.request.urlretrieve` 下载图片时报如下错误：
>  raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

![](https://www.choudalao.com/uploads/20200722/20200722122034soCSAy.png)

有些网站验证请求信息中的UserAgent(它的信息包括硬件平台、系统软件、应用软件和用户个人偏好),如果UserAgent存在异常或者是不存在,那么这次请求将会被拒绝(如上错误信息所示)
所以可以尝试在请求中加入UserAgent的信息。

# 解决方法

运行有惊喜哦。

```python
# coding:utf-8
from pathlib import Path
import random
from urllib import request
import os

url = 'https://uploadbeta.com/api/pictures/random/?key=%E6%8E%A8%E5%A5%B3%E9%83%8E'
img_nmae = str(random.randint(100000, 999999)) + '.jpg'
path_str = './img/'
setu_file = Path(path_str)
if not os.path.exists(setu_file):
    os.makedirs(setu_file)
    print("目录创建成功！")
path = path_str + img_nmae
# 创建一个opener对象
opener = request.build_opener()
# 向opener传入请求头信息
opener.addheaders = ([
    ('User-Agent',
     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
])
# 将创建好的opener对象装入request
request.install_opener(opener)
# 下载
request.urlretrieve(url, path)
print(path)

```