---
title: "python3 数据写入 Excel"
date: 2021-05-05T23:10:09+08:00
updated: 2026-02-23T05:14:07+08:00
author: "臭大佬"
categories: [Python]
description: "python3 数据写入 Excel"
cover: "https://www.choudalao.com/uploads/20210505/kOFNciRlnITYjO5S0RM0FCg9ZFoY5Eby55H9O7ib.jpeg"
click: 3067
---

# 模块安装
```python
pip install xlwt
```

# 操作
```python
# coding=utf-8
import xlwt

# 创建一个工作簿
myBook = xlwt.Workbook()
# 创建一个工作表格
mySheet = myBook.add_sheet('测试表格')
# 写入数据
# mySheet.write(i,j,value,style)
# i列、j行、value值、style样式，注意，行和列都是从0开始算的
# 创建数据格式，写入数据
myStyle = xlwt.easyxf('font:name Times New Roman,color-index red,bold on')
# 写数据的时候可以用这个格式
mySheet.write(3, 0, 'abcd', myStyle)
# 合并行4到6的列0到1，里面的内容为'品种'
mySheet.write_merge(4, 6, 0, 1, '品种', myStyle)
# 写入A3，数值等于1
mySheet.write(2, 0, 1)
# 写入B3，数值等于1
mySheet.write(2, 1, 1)
# 写入C3，数值等于2
mySheet.write(2, 2, xlwt.Formula("A3+B3"))
# 保存
myBook.save('test.xls')

```

运行结果

![](https://www.choudalao.com/uploads/20210505/20210505230802Pyzk64.png)

### myStyle 设置样式
```python
		# 创建一个工作簿
        myBook = xlwt.Workbook()
        # 创建一个工作表格
        mySheet = myBook.add_sheet('测试表格')
        # 字体
        font = xlwt.Font()
        font.bold = True
        # 设置单元格对齐方式
        alignment = xlwt.Alignment()
        # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
        alignment.horz = 0x02
        # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
        alignment.vert = 0x01
        # 设置自动换行
        alignment.wrap = 1
        # 初始化样式
        style = xlwt.XFStyle()
        style.font = font
        style.alignment = alignment
		# 写数据的时候可以用这个格式
		mySheet.write(3, 0, 'abcd', myStyle)
		.....
```