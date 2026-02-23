---
title: "php中0,null,empty,空,false,字符串关系的详细介绍"
date: 2017-09-15T14:46:21+08:00
updated: 2026-02-23T06:13:04+08:00
author: "臭大佬"
categories: [php]
description: "php中0,null,empty,空,false,字符串关系的详细介绍"
cover: "http://www.choudalao.com/uploads/20191016/DkPO7TaTLi5dmwYei6JBTT5067qreCcOvd48K55Y.jpeg"
click: 2821
---

&lt;p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;// 判断 0 与 ''、null、empty、false 之间的关系   

$a = 0;

echo &quot;0 与 ''、 empty、null、false 之间的关系：&quot;;


if ($a == '') {

    echo &quot;0 == '';&quot;;//输出    

} else {

    echo &quot;0 != '';&quot;;

}


if (trim($a) == '') {

    echo &quot;trim(0) == '';&quot;;

} else {

    echo &quot;trim(0) != '';&quot;; //输出,因为trim(0)为字符串'0' 

}


if (strval($a) == '') {

    echo &quot;strval(0) == '';&quot;;

} else {

    echo &quot;strval(0) != '';&quot;; //输出  strval — 获取变量的字符串值

}

//0=='',trim(0)!='',strval(0)!='' 不是空字符串  


if ($a === '') {

    echo &quot;0 === '';&quot;;

} else {

    echo &quot;0 !=== '';&quot;;  //输出 还比较类型 

}

//0!===''  


if (empty($a)) {

    echo &quot;0 is empty;&quot;; //输出  

} else {

    echo &quot;0 is not empty;&quot;;

}

//0 is empty  


if (is_null($a)) {

    echo &quot;0 is null;&quot;;

} else {

    echo &quot;0 is not null;&quot;;  //输出 

}

//0 is not null  


if (is_numeric($a)) {

    echo &quot;0 is numeric;&quot;; //输出 如果$a='0',则结果相反  

} else {

    echo &quot;0 is not numeric;&quot;;

}

//0 is numeric  


if (is_string($a)) {

    echo &quot;0 is string;&quot;;

} else {

    echo &quot;0 is not string;&quot;; //输出   

}

//0 is not string  


if (!$a) {

    echo &quot;0 is false;&quot;; //输出  

} else {

    echo &quot;0 is not false;&quot;;

}

//0 is false  


// 判断 '' 和 0、null、empty、false 之间的关系   

$a = '';

echo &quot;'' 和 0、empty、null、false 之间的关系：&quot;;

if ($a == 0) {

    echo &quot;'' == 0;&quot;;  //输出  

} else {

    echo &quot;'' != 0;&quot;;

}


if (intval($a) == 0) {

    echo &quot;intval('') == 0;&quot;;  //输出 

} else {

    echo &quot;intval('') != 0;&quot;;

}


if (empty($a)) {

    echo &quot;'' is empty;&quot;; //输出   

} else {

    echo &quot;'' is not empty;&quot;;

}


if (is_null($a)) {

    echo &quot;'' is null;&quot;;

} else {

    echo &quot;'' is not null;&quot;;//输出    

}


if (is_numeric($a)) {

    echo &quot;'' is numeric;&quot;;

} else {

    echo &quot;'' is not numeric;&quot;; //输出  

}


if (is_string($a)) {

    echo &quot;'' is string;&quot;; //输出   

} else {

    echo &quot;'' is not string;&quot;;

}


if (!$a) {

    echo &quot;'' is false;&quot;; //输出  

} else {

    echo &quot;'' is not false;&quot;;

}


// 判断 null 和 ''、0、empty、false 之间的关系   

$a = null;

echo &quot;null 和 ''、0、empty、false 之间的关系：&quot;;

if ($a == '') {

    echo &quot;null == '';&quot;; //输出  

} else {

    echo &quot;null != '';&quot;;

}


if ($a == 0) {

    echo &quot;null == 0;&quot;; //输出  

} else {

    echo &quot;null != 0;&quot;;

}


if ($a === '') {

    echo &quot;null === '';&quot;;

} else {

    echo &quot;null !=== '';&quot;; //输出  

}


if ($a === 0) {

    echo &quot;null === 0;&quot;;

} else {

    echo &quot;null !=== 0;&quot;; //输出  

}


if (strval($a) == '') {

    echo &quot;strval(null) == '';&quot;; //输出  

} else {

    echo &quot;strval(null) != '';&quot;;

}


if (intval($a) == 0) {

    echo &quot;intval(null) == 0;&quot;; //输出  

} else {

    echo &quot;intval(null) != 0;&quot;;

}


if (empty($a)) {

    echo &quot;null is empty;&quot;; //输出  

} else {

    echo &quot;null is not empty;&quot;;

}


if (is_numeric($a)) {

    echo &quot;null is numeric;&quot;;

} else {

    echo &quot;null is not numeric;&quot;; //输出  

}


if (is_string($a)) {

    echo &quot;null is string;&quot;;

} else {

    echo &quot;null is not string;&quot;; //输出  

}


if (!$a) {

    echo &quot;null is false;&quot;;

} else {

    echo &quot;null is not false;&quot;; //输出  

}  

&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;