---
title: "vscode格式化导致 20:1  error  Expected indentation of 2 spaces but found 8   indent"
date: 2022-04-13T22:31:54+08:00
updated: 2026-02-22T10:57:06+08:00
author: "臭大佬"
categories: [前端]
description: "20:1  error  Expected indentation of 2 spaces but found 8   indent"
cover: "https://www.choudalao.com/uploads/20220413/sqYu2xxXNPKTM8f7TxGNgTVGDogI8BakGVijALSv.jpeg"
click: 4373
---

# 问题一

vscode 保存代码时，对代码格式化了，导致vue代码报错:
~~'  error  Expected indentation of 2 spaces but found 8   indent'~~

![](https://www.choudalao.com/uploads/20220413/20220413222913Hawdiv.png)

## 原因

本来需要2个空格，实际在格式化的时候出现了8个

# 解决

找到`.eslintrc.js` 文件，注释掉 `'@vue/standard'`

```php
 env: {
        node: true
    },
    'extends': [
        'plugin:vue/essential',
        //'@vue/standard'
    ],
```
![](https://www.choudalao.com/uploads/20220413/20220413223100OoaZyG.png)

最后重启服务
```php
npm run serve // npm run dev

```

![](https://www.choudalao.com/uploads/20220413/20220413223148VdzTzi.png)


# 问题二

另外，如果出现如下问题：
```php
 1:1   error    Component name "index" should always be multi-word  vue/multi-word-component-names
```
![](https://www.choudalao.com/uploads/20220414/20220414000102ym3AWs.png)

 这是组件命名不够规范导致的，解决方式也是修改`.eslintrc.js`这个文件，修改如下：
 ```php
 rules: {
        //关闭组件命名规则
        "vue/multi-word-component-names": "off",
       // ...
    },
 
 ```
 ![](https://www.choudalao.com/uploads/20220413/20220413234706F7wFlQ.png)
 
修改完记得重启哦。

# 问题三
当有警告信息如下时：
`xxx\index.vue
   49:15  warning  Strings must use singlequote  quotes`

![](https://www.choudalao.com/uploads/20220413/20220413234611SMHIQZ.png)


解决方法:配置文件`eslintrc.js`中设置
```php
rules: {
		// ...
        "quotes": "off",
        'semi': "off",
        'comma-dangle': 'off',
    },
```
![](https://www.choudalao.com/uploads/20220414/20220414000303r7hwZM.png)

修改完记得重启哦。