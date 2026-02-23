---
title: "set_time_limit() 设置程序执行时间的函数"
date: 2017-11-27T07:36:22+08:00
updated: 2026-02-23T19:29:52+08:00
author: "臭大佬"
categories: [php]
description: "set_time_limit() 设置程序执行时间的函数"
cover: "http://www.choudalao.com/uploads/20191016/wWNJ5pLVye9yylF0lF7d3ggj0towXQ9qELZzCZC3.jpeg"
click: 3763
---

&lt;p&gt;&amp;nbsp; &amp;nbsp;之前做数据迁移的时候,遇到一个问题,情况是这样的,要把数据移动到另一个数据库里面,自己写了个迁移程序,文章数据比较多,大概10万来条,当程序跑了1000来条的时候,突然就停止了,后来去网上查了一下,原来是未设置失效时间导致的:&lt;/p&gt;&lt;p&gt;&amp;nbsp; &amp;nbsp;一个简单的例子，在网页里显示1500条语句，如果未设置失效时间，则程序执行到791时结束了，如果使用 set_time_limit(0),则程序直到1才结束。&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;//set_time_limit(0); 
$i = 1500;
include(&quot;inc/conn.php&quot;);
while ($i &amp;gt; 0) {
    $sql = &quot;INSERT INTO php (php) 
VALUES ('$i')&quot;;
    if ($conn-&amp;gt;execute($sql) === flase) {
//echo &quot;数据插入错误&quot;.$conn-&amp;gt;errormsg(); 
    } else {
        $phpid = $conn-&amp;gt;Insert_ID();
        echo $i . &quot;已经存入数据库,编号：&quot; . $phpid;
    }
    $i--;
    echo &quot;&quot;;
}&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;span class=&quot;refname&quot; fira=&quot;&quot; source=&quot;&quot; sans=&quot;&quot; background-color:=&quot;&quot;&gt;set_time_limit&lt;/span&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; sans=&quot;&quot; background-color:=&quot;&quot;&gt;&amp;nbsp;—&amp;nbsp;&lt;/span&gt;&lt;span class=&quot;dc-title&quot; fira=&quot;&quot; source=&quot;&quot; sans=&quot;&quot; background-color:=&quot;&quot;&gt;设置脚本最大执行时间&lt;/span&gt;,当php运行于&lt;a href=&quot;http://php.net/manual/zh/ini.sect.safe-mode.php#ini.safe-mode&quot; _href=&quot;http://php.net/manual/zh/ini.sect.safe-mode.php#ini.safe-mode&quot;&gt;安全模式&lt;/a&gt;时，此功能不能生效。除了关闭安全模式或改变php.ini中的时间限制，没有别的办法。&lt;/p&gt;