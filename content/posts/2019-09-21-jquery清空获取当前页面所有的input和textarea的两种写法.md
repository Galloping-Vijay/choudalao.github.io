---
title: "Jquery清空（获取）当前页面所有的input和textarea的两种写法"
date: 2019-09-21T03:14:49+08:00
updated: 2026-02-23T17:12:24+08:00
author: "臭大佬"
categories: [前端]
description: "Jquery清空（获取）当前页面所有的input和textarea的两种写法"
cover: "http://www.choudalao.com/uploads/20190921/nyY99bVcdoyyqTuY78zHTnqrLj2l07EEY5w4PFZq.jpeg"
click: 4377
---

&lt;p&gt;&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;$(&quot;#myform input,#myform textarea&quot;).each(function(){
    this.value = this.value.replace(/\&amp;amp;/g,&quot;%26&quot;);//也可以清空数据this.value =&quot;&quot;;
})
$(&quot;#myform&quot;).find(&quot;input,textarea&quot;).each(function(){
   this.value = this.value.replace(/\&amp;amp;/g,&quot;%26&quot;);//也可以清空数据this.value =&quot;&quot;;
});&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;/p&gt;