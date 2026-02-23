---
title: "【转】tinyint(1)和tinyint(4)的区别和用法"
date: 2020-11-29T16:04:34+08:00
updated: 2026-02-23T18:48:18+08:00
author: "臭大佬"
categories: [MYSQL]
description: "tinyint(1)和tinyint(4)的区别和用法"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4053
---

![](https://www.choudalao.com/uploads/20201129/20201129160212ysHpzf.png)


1 bytes = 8 bit ,一个字节最多可以代表的数据长度是2的8次方 11111111 在计算机中也就是

-128到127

### BIT[M]

位字段类型，M表示每个值的位数，范围从1到64，如果M被忽略，默认为1

### TINYINT[(M)] [UNSIGNED] [ZEROFILL]  M默认为4
很小的整数。带符号的范围是-128到127。无符号的范围是0到255。

### BOOL，BOOLEAN

是TINYINT(1)的同义词。zero值被视为假。非zero值视为真。

### SMALLINT[(M)] [UNSIGNED] [ZEROFILL] M默认为6
小的整数。带符号的范围是-32768到32767。无符号的范围是0到65535。

### MEDIUMINT[(M)] [UNSIGNED] [ZEROFILL] M默认为9

中等大小的整数。带符号的范围是-8388608到8388607。无符号的范围是0到16777215。

### INT[(M)] [UNSIGNED] [ZEROFILL]   M默认为11
普通大小的整数。带符号的范围是-2147483648到2147483647。无符号的范围是0到4294967295。

### BIGINT[(M)] [UNSIGNED] [ZEROFILL] M默认为20
大整数。带符号的范围是-9223372036854775808到9223372036854775807。无符号的范围是0到18446744073709551615。

注意：这里的M代表的并不是存储在数据库中的具体的长度，以前总是会误以为int(3)只能存储3个长度的数字，int(11)就会存储11个长度的数字，这是大错特错的。

tinyint(1) 和 tinyint(4) 中的1和4并不表示存储长度，只有字段指定zerofill是有用，
如tinyint(4)，如果实际值是2，如果列指定了zerofill，查询结果就是0002，左边用0来填充。


转自：https://blog.csdn.net/jaryle/article/details/52025023