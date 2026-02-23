---
title: "js将post请求的参数对象转换成get的形式拼接在url上"
date: 2021-06-10T16:36:34+08:00
updated: 2026-02-23T07:19:37+08:00
author: "臭大佬"
categories: [前端]
description: "js将post请求的参数对象转换成get的形式拼接在url上"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4558
---

# 代码

```php
/**
     * js将post请求的参数对象转换成get的形式拼接在url上
     * @param param
     * @returns {string}
     */
    function changeParam(param) {
        return JSON.stringify(param).replace(/:/g, '=').replace(/,/g, '&').replace(/{/g, '?').replace(/}/g, '').replace(/"/g, '');
    }
	
// 结果示例
// ?reconciliation_status=&purchase_sn=&main_order_sn=&reconciliation_sn=&order_delivery_sn=&supplier_name=&ship_status=&user_name=&ship_time=&brand_ids=&search_brand_keyword=&purchase_admin_time=&finance_admin_time=2021-06-13 ~ 2021-05-15&ids=
```