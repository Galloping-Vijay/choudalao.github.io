---
title: "Redirecting to https://open.wein.qq.com/..."
date: 2022-03-29T16:00:43+08:00
updated: 2026-02-22T08:57:52+08:00
author: "臭大佬"
categories: [php]
description: "解决Easywechat授权登录页面出现：Redirecting to https://open.wein.qq.com/..."
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 2708
---

# 问题
在用`Easywechat` 做微信授权登录的时候，发现会请求两次`https://open.weixin.qq.com/connect/oauth2/authorize`,

![](https://www.choudalao.com/uploads/20220329/20220329154542Tdvl58.png)

中间会跳如下页面，

![](https://www.choudalao.com/uploads/20220329/20220329154618MN7rOH.png)

网上说，在请求接口`https://open.weixin.qq.com/connect/oauth2/authorize`的时候加一个参数`connect_redirect=1`,可以解决这个问题，

模拟地址如下：
`https://open.weixin.qq.com/connect/oauth2/authorize?appid=xxx&redirect_uri=xxx&response_type=code&scope=snsapi_userinfo&state=STATE&connect_redirect=1#wechat_redirect`,

但是看`Easywechat`本来就带有这个参数，

![](https://www.choudalao.com/uploads/20220329/2022032915495093W64A.png)

这个我们就不管他了，

现在主要解决跳`Redirecting to https://open.wein.qq.com/...`页的问题，这个页面给人的体验很不好，

# 解决
根据页面的title，可以定位到`vendor/symfony/http-foundation/RedirectResponse.php`,

![](https://www.choudalao.com/uploads/20220329/20220329155411V9yXpo.png)

把`title`改成`跳转中...`，并且隐藏`body`，

![](https://www.choudalao.com/uploads/20220329/20220329155727MBTLqy.png)

效果如下：

![](https://www.choudalao.com/uploads/20220329/20220329155636edgA8M.png)

这样用户体验就会好点，至少看上去不会像bug页面。