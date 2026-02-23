---
title: "PHP isset()与empty()的使用区别详解"
date: 2017-12-27T09:31:14+08:00
updated: 2026-02-23T07:08:10+08:00
author: "臭大佬"
categories: [php]
description: "PHP isset()与empty()的使用区别详解"
cover: "http://www.choudalao.com/uploads/20191016/10QGyB6mYCaLRs8UC5ScR88W6SrKWxSXK0j0FEUy.jpeg"
click: 3031
---

&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;PHP的isset()函数 一般用来检测变量是否设置&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;格式：bool isset ( mixed var [, mixed var [, ...]] )&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;功能：检测变量是否设置&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;返回值：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;若变量不存在则返回 FALSE&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;若变量存在且其值为NULL，也返回 FALSE&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;若变量存在且值不为NULL，则返回 TURE&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;同时检查多个变量时，每个单项都符合上一条要求时才返回 TRUE，否则结果为 FALSE&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;版本：PHP 3, PHP 4, PHP 5&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;更多说明：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;使用 unset() 释放变量之后，它将不再是 isset()。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;PHP函数isset()只能用于变量，传递任何其它参数都将造成解析错误。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;检测常量是否已设置可使用 defined() 函数。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;&lt;br&gt;&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;PHP的empty()函数 判断值为否为空&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;格式：bool empty ( mixed var )&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;功能：检查一个变量是否为空&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;返回值：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;若变量不存在则返回 TRUE&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;若变量存在且其值为&quot;&quot;、0、&quot;0&quot;、NULL、、FALSE、array()、var $var; 以及没有任何属性的对象，则返回 TURE&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;若变量存在且值不为&quot;&quot;、0、&quot;0&quot;、NULL、、FALSE、array()、var $var; 以及没有任何属性的对象，则返回 FALSE&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;版本：PHP 3, PHP 4, PHP 5&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;更多说明：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot;color: rgb(51, 51, 51); font-family: &amp;quot;Courier New&amp;quot;;&quot;&gt;empty()的返回值=!(boolean) var，但不会因为变量未定义而产生警告信息。参见转换为布尔值获取更多信息。&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;empty() 只能用于变量，传递任何其它参数都将造成Paser error而终止运行。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;检测常量是否已设置可使用 defined() 函数。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;例子： empty() 与 isset() 的一个简单比较&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;&lt;br&gt;&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;复制代码 代码如下:&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;$var = 0;

// 结果为 true，因为 $var 为空

if (empty($var)) {

    echo '$var is either 0 or not set at all';

}

// 结果为 false，因为 $var 已设置

if (!isset($var)) {

    echo '$var is not set at all';

}&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;span style=&quot;color: rgb(51, 51, 51); font-family: &amp;quot;Courier New&amp;quot;;&quot;&gt;注: 由于这是一个语言结构而非函数，因此它无法被变量函数调用。&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;注: empty() 只检测变量，检测任何非变量的东西都将导致解析错误。换句话说，后边的语句将不会起作用： empty(addslashes($name))。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;&lt;br&gt;&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;下面是经过脚本之家测试过的一段isset与empty函数详细例子的代码,看完这个基本上就差不多了:&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;复制代码 代码如下:&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;error_reporting(E_ALL);
echo '未定义$var';
echo &quot;isset测试:&quot;;
if (isset ($var)) {
    echo '变量$var存在!';
}
echo &quot;empty测试:&quot;;
if (empty ($var)) {
    echo '变量$var的值为空';
} else {
    echo '变量$var的值不为空';
}
echo &quot;变量直接测试:&quot;;
if ($var) {
    echo '变量$var存在!';
} else {
    echo '变量$var不存在!';
}
echo '----------------------------------';
echo '$var = \'\'';
echo &quot;isset测试:&quot;;
$var = '';
if (isset ($var)) {
    echo '变量$var存在!';
}
echo &quot;empty测试:&quot;;
if (empty ($var)) {
    echo '变量$var的值为空';
} else {
    echo '变量$var的值不为空';
}
echo &quot;变量直接测试:&quot;;
if ($var) {
    echo '变量$var存在!';
} else {
    echo '变量$var不存在!';
}
echo '----------------------------------';
echo '$var = 0';
echo 'isset测试:';
$var = 0;
if (isset ($var)) {
    echo '变量$var存在!';
}
echo &quot;empty测试:&quot;;
if (empty ($var)) {
    echo '变量$var的值为空';
} else {
    echo '变量$var的值不为空';
}
echo &quot;变量直接测试:&quot;;
if ($var) {
    echo '变量$var存在!';
} else {
    echo '变量$var不存在!';
}
echo '----------------------------------';
echo '$var = null';
echo 'isset测试:';
$var = null;
if (isset ($var)) {
    echo '变量$var存在!';
}
echo &quot;empty测试:&quot;;
if (empty ($var)) {
    echo '变量$var的值为空';
} else {
    echo '变量$var的值不为空';
}
echo &quot;变量直接测试:&quot;;
if ($var) {
    echo '变量$var存在!';
} else {
    echo '变量$var不存在!';
}
echo '----------------------------------';
echo '$var =&quot;php&quot;';
echo 'isset测试:';
$var = &quot;php&quot;;
if (isset ($var)) {
    echo '变量$var存在!';
}
echo &quot;empty测试:&quot;;
if (empty ($var)) {
    echo '变量$var的值为空';
} else {
    echo '变量$var的值不为空';
}
echo &quot;变量直接测试:&quot;;
if ($var) {
    echo '变量$var存在!';
} else {
    echo '变量$var不存在!';
}&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;span style=&quot;color: rgb(51, 51, 51); font-family: &amp;quot;Courier New&amp;quot;;&quot;&gt;在使用 php 编写页面程序时，我经常使用变量处理函数判断 php 页面尾部参数的某个变量值是否为空，开始的时候我习惯了使用 empty() 函数，却发现了一些问题，因此改用 isset() 函数，问题不再。&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;顾名思义，empty() 判断一个变量是否为“空”，isset() 判断一个变量是否已经设置。正是这种所谓的“顾名思义”，令我开始时走了些弯路：当一个变量值等于0时，empty()也会成立（True），因而会发生 一些意外。原来，empty() 和 isset() 虽然都是变量处理函数，它们都用来判断变量是否已经配置，它们却是有一定的区别：empty还会检测变量是否为空、为零。当一个变量值为0，empty() 认为这个变量同等于空，即相当于没有设置。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;比如检测 $id 变量，当 $id=0 时，用empty() 和 isset() 来检测变量 $id 是否已经配置，两都将返回不同的值—— empty() 认为没有配置，isset() 能够取得 $id 的值：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;复制代码 代码如下:&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;$id=0;
empty($id)?print &quot;It's empty .&quot;:print &quot;It's $id .&quot;;
//结果：It's empty .
print &quot;&quot;;
!isset($id)?print &quot;It's empty .&quot;:print &quot;It's $id .&quot;;
//结果：It's 0 .&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;span style=&quot;color: rgb(51, 51, 51); font-family: &amp;quot;Courier New&amp;quot;;&quot;&gt;这意味着，我们在使用变量处理函数时，当该变量可能出现0的值，使用 empty() 要小心，这个时候用 isset 取代它更明智一些。&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;当一个php页面的 URL 尾部参数出现 id=0 时（比如：test.php?id=0），试比较：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;复制代码 代码如下:&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;if(empty($id)) $id=1; - 若 id=0 ，id 也会为1
if(!isset($id)) $id=1; - 若 id=0 ，id 不会为1&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;span style=&quot;color: rgb(51, 51, 51); font-family: &amp;quot;Courier New&amp;quot;;&quot;&gt;可分开运行以下代码检测上述推断：&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;复制代码 代码如下:&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;if(empty($id)) $id=1;
print $id; // 得到 1
if(!isset($id)) $id=1;
print $id; //得到 0&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;span style=&quot;color: rgb(51, 51, 51); font-family: &amp;quot;Courier New&amp;quot;;&quot;&gt;要说它们的联系，其共同点就是empty()和 isset()都是变量处理函数，作用是判断变量是否已经配置，正是由于它们在处理变量过程中有很大的相似性，才导致对它们的关系认识不足。单从 empty()和isset()这两个函数本身来考虑的话会把人弄得更糊涂，换一个角度来它。empty()和isset()的处理对象无外乎未定义变量，0，空字符串。&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;如果变量为0，则empty()会返回TRUE，isset()会返回TRUE；&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;如果变量为空字符串，则empty()会返回TRUE，isset()会返回TRUE；&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;如果变量未定义，则empty()会返回TRUE，isset()会返回FLASE；&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;手册中对empty()的解释如下：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;描述bool empty( mixed var )&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;如果 var 是非空或非零的值，则 empty() 返回 FALSE。换句话说，”&quot;、0、”0″、NULL、FALSE、array()、var $var; 以及没有任何属性的对象都将被认为是空的，如果 var 为空，则返回 TRUE。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;手册中对isset()的解释如下：&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;isset()检测变量是否设置&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;描述bool isset ( mixed var [, mixed var [, ...]] )&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;如果 var 存在则返回 TRUE，否则返回 FALSE。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;如果已经使用 unset() 释放了一个变量之后，它将不再是 isset()。若使用 isset() 测试一个被设置成 NULL 的变量，将返回 FALSE。同时要注意的是一个 NULL 字节（”?”）并不等同于 PHP 的 NULL 常数。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;警告: isset() 只能用于变量，因为传递任何其它参数都将造成解析错误。若想检测常量是否已设置，可使用 defined()函数。&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;当要 判断一个变量是否已经声明的时候 可以使用 isset 函数&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;当要 判断一个变量是否已经赋予数据且不为空 可以用 empty 函数&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;font color=&quot;#333333&quot; face=&quot;Courier New&quot;&gt;&lt;span&gt;当要 判断 一个变量 存在且不为空 先isset 函数 再用 empty 函数&lt;/span&gt;&lt;/font&gt;&lt;/p&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;