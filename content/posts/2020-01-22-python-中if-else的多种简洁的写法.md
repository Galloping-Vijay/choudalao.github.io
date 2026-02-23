---
title: "python 中if-else的多种简洁的写法"
date: 2020-01-22T10:05:51+08:00
updated: 2026-02-23T15:48:14+08:00
author: "臭大佬"
categories: [Python]
description: "python 中if-else的多种简洁的写法"
cover: "https://www.choudalao.com/uploads/20200122/yqiCSu7G2lL8MF3Z1yh0RT6a8WDxk3QbvBlmLIwy.jpeg"
click: 4030
---

# 普通写法
```python
a, b, c = 1, 2, 3
if a>b:
    c = a
else:
    c = b
```

# 一行表达式,为真时放if前

```python
c = a if a>b else b
```

# 二维列表，利用大小判断的0，1当作索引

```python 
c= [b, a][a > b]
```

# 传说中的黑客，利用逻辑运算符进行操作，都是最简单的东西，却发挥无限能量啊

```python
c = (a>b and [a] or [b])[0]
# 改编版
c = (a>b and a or b)
```

第四种最有意思了，

利用and 的特点，若and前位置为假则直接判断为假。

利用 or的特点，若or前位置为真则判断为真。

```python
# 从前往后找，and找假，or找真
# 前真返后，
print(111 and 222)  # 222
# 前假返前
print(0 and 333)  #0

# 若x真【x】, x假,y真【y】，xy假【y】,只有前真返回前
print(111 or 222) #111
print(0 or 222) #222
print('' or 0) # 0
```
对于c = (a>b and a or b)而言，
若（a>b and a）
　　真：a >b and a,
　　　　则a > b 为真
　　假：b，
　　　　则 a> b为假
 补充：对于and的理解
 
```python
 id_ = '12345'
# 判断长度为5或者为8
if len(id_) == 5 or len(id_) == 8:
    print(id_, '------')
# 相反的表达为非5且非8
if len(id_) != 5 and len(id_) != 8:
    print(id_, '+++++++')
```

原文地址：https://www.cnblogs.com/xiexiaoxiao/p/7772441.html