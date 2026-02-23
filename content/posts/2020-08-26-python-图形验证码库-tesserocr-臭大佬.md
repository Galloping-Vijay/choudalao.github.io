---
title: "Python 图形验证码库 tesserocr | 臭大佬"
date: 2020-08-26T23:00:04+08:00
updated: 2026-02-23T17:04:19+08:00
author: "臭大佬"
categories: [Python]
description: "Python 图形验证码库 tesserocr"
cover: "https://www.choudalao.com/uploads/20200826/HfbW1XnSY6Rh5L7TU35DDSkD37QeKjbD2jjIu6uN.jpeg"
click: 3546
---

# 用途
对于验证码，我们可以使用OCR技术来将其转化为电子文本，然后爬虫将识别结果提交给服务器，便可以达到自动识别验证码的过程。

# 概念
#### OCR
OCR,全称叫 Optical Character Recognition，中文翻译叫光学字符识别，是指通过扫描字符，通过其形状将其翻译成电子文本的过程；

#### tesseract
tesseract是google开源的OCR

# 安装

## WIN10
tesserocr需要安装tessoract依赖库，所以安装tesserocr前需要安装tessoract。
tesseract下载地址：https://digi.bib.uni-mannheim.de/tesseract/，（可能需要爬墙哦）

![](https://www.choudalao.com/uploads/20200826/20200826225535YmrFLg.png)

![](https://www.choudalao.com/uploads/20200826/20200826225645kE2GFU.png)

然后安装到这一步注意要勾选这一项来安装OCR识别支持的语言包，这样OCR就可以识别多国语言，然后就可以一直点击下一步完成安装。
![](https://www.choudalao.com/uploads/20200826/20200826225754j99Pxk.png)
![](https://www.choudalao.com/uploads/20200826/202008262259544OXEpY.png)

如何验证tesseract是否安装成功？直接cmd下输入tesseract即可；
![](https://www.choudalao.com/uploads/20200826/202008262323069diT2V.png)

如果提示'tesseract' 不是内部或外部命令，则是因为没有配置环境变量，手动把tesseract根目录配置到path参数下即可

![](https://www.choudalao.com/uploads/20200826/20200826232351owNpfT.png)

重启cmd控制台，再次输入tesseract；

![](https://www.choudalao.com/uploads/20200826/20200826232431JayACI.png)

##### 安装 tesserocr

windows不能用pip install tesserocr所以我这里是安装.whl文件，下载地址：https://github.com/simonflueckiger/tesserocr-windows_build/releases

![](https://www.choudalao.com/uploads/20200826/20200826234447RkfPpb.png)

把下载好的xxx.whl文件放在python安装目录下的\Lib\site-packages文件夹里面，进入该目录下，然后在这里打开cmd，输入命令pip install  xxx.whl

```python
pip install tesserocr-2.4.0-cp36-cp36m-win_amd64.whl
```

![](https://www.choudalao.com/uploads/20200826/20200826235345uvcHXG.png)

在运行过程中，我们还需要更新`pip`

```python 
pip install --upgrade pip
```
![](https://www.choudalao.com/uploads/20200826/2020082623544804F02C.png)

#### 运行代码
```python
import tesserocr
from PIL import Image

# 新建Image对象
image = Image.open("./code_img/veriCode (1).do")
# 进行置灰处理
image = image.convert('L')
# 这个是二值化阈值
threshold = 150
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# 通过表格转换成二进制图片，1的作用是白色，不然就全部黑色了
image = image.point(table, "1")
#image.show()
result = tesserocr.image_to_text(image)
print(result)
```

![](https://www.choudalao.com/uploads/20200826/20200826235928X0JOqj.png)

运行时有一个报错信息

> RuntimeError: Failed to init API, possibly an invalid tessdata path: D:\Program Files\Anaconda3\envs\tensorflow\/tessdata/

只要把刚才安装的tesseract下面的tessdata文件夹复制到python的安装路径里（与lib文件夹同级）,也就是报错报的地址处。

![](https://www.choudalao.com/uploads/20200827/2020082700094834VJxK.png)

再次执行：

![](https://www.choudalao.com/uploads/20200827/20200827001133ZUnY8h.png)

可以获取得到验证码内容了。