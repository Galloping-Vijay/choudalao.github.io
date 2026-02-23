---
title: "PHP之get_class — 返回对象的类名"
date: 2017-06-01T18:50:10+08:00
updated: 2026-02-23T21:08:39+08:00
author: "臭大佬"
categories: [php]
description: "PHP之get_class — 返回对象的类名"
cover: "http://www.choudalao.com/uploads/20191016/hjj4tTYY5Qn9Kn2tPXZ5YHxOFLcmxthlKW66mC0a.jpeg"
click: 2982
---

&lt;p&gt;&lt;span class=&quot;type&quot; fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot;&gt;string&lt;/span&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; background-color:=&quot;&quot;&gt;&amp;nbsp;&lt;/span&gt;&lt;span class=&quot;methodname&quot; fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot;&gt;&lt;span&gt;get_class&lt;/span&gt;&lt;/span&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; background-color:=&quot;&quot;&gt;&amp;nbsp;([&amp;nbsp;&lt;/span&gt;&lt;span class=&quot;methodparam&quot; fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot;&gt;&lt;span class=&quot;type&quot;&gt;object&lt;/span&gt;&amp;nbsp;&lt;code class=&quot;parameter&quot; fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; word-wrap:=&quot;&quot; color:=&quot;&quot; cursor:=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; margin:=&quot;&quot;&gt;$object&lt;/code&gt;&lt;span class=&quot;initializer&quot;&gt;&amp;nbsp;=&amp;nbsp;&lt;span&gt;&lt;code fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; word-wrap:=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; margin:=&quot;&quot;&gt;NULL&lt;/code&gt;&lt;/span&gt;&lt;/span&gt;&lt;/span&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; background-color:=&quot;&quot;&gt;&amp;nbsp;] )&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; background-color:=&quot;&quot;&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; sans=&quot;&quot; background-color:=&quot;&quot;&gt;返回对象实例&amp;nbsp;&lt;/span&gt;&lt;code class=&quot;parameter&quot; fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; word-wrap:=&quot;&quot; color:=&quot;&quot; cursor:=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot;&gt;object&lt;/code&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; sans=&quot;&quot; background-color:=&quot;&quot;&gt;&amp;nbsp;所属类的名字。&lt;/span&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; background-color:=&quot;&quot;&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;class Car
{
    function getName()
    {
        echo &quot;My name is &quot; . get_class() . &quot;&lt;br&gt;&quot;;
        echo &quot;My name is &quot; . get_class($this) . &quot;&lt;br&gt;&quot;;
    }
}

//类内部调用  $bar = new Car();
$bar-&amp;gt;getName();

//类外部调用  echo &quot;Its name is &quot; . get_class($bar) .&quot;&lt;br&gt;&quot;;&lt;/code&gt;&lt;/pre&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; code=&quot;&quot; letter-spacing:=&quot;&quot; word-spacing:=&quot;&quot; background-color:=&quot;&quot;&gt;&lt;span fira=&quot;&quot; source=&quot;&quot; sans=&quot;&quot; background-color:=&quot;&quot;&gt;&lt;/span&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;运行结果&lt;/p&gt;&lt;p&gt;My name is Car&lt;/p&gt;&lt;p&gt;My name is Car&lt;br&gt;Its name is Car&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;