---
title: "理解PHP依赖注入容器(dependency injection container)系列(一) 什么是依赖注入"
date: 2018-07-01T18:58:28+08:00
updated: 2026-02-23T15:53:20+08:00
author: "臭大佬"
categories: [php]
description: "理解php的依赖注入概念"
cover: "http://www.choudalao.com/uploads/20191016/35Q72ria8QOWKwNWAkPM5cehpQI14UlwlVSb5WVD.jpeg"
click: 3025
---

&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;本文是PHP依赖注入容器的实现这个系列的第一章。&amp;nbsp;&lt;br&gt;今天，先不谈容器(container),首先用一些具体的例子来介绍&lt;span&gt;依赖注入&lt;/span&gt;的概念，证明依赖注入这种模式可以解决哪些问题，同时能给开发人员带来哪些好处。&amp;nbsp;&lt;br&gt;如果你已经知道了依赖注入的概念，你可以跳过这篇文章。&lt;/p&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;依赖注入可能是我所知道的最简单设计模式之一，很多情况下可能你无意识中已经使用了依赖注入。不过它也是最难解释的一个。我认为有一部分原因是由于大多数介绍依赖注入的例子缺乏实际意义，让人难理解。因为PHP主要用于Web开发，那就先来看一个简单的web开发实例。&lt;/p&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;HTTP本身是一个无状态的连接协议，为了支持客户在发起WEB请求时应用程序能存储用户信息，我们就需要通过一种技术来实现存储状态交互。理所当然最简单的是使用cookie，更好的方式是PHP内置的Session机制。&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;$_SESSION['language'] = 'fr';1&lt;/code&gt;&lt;/pre&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;上面代码将用户语言存储在了名为language的Session变量中，因此在该用户随后的请求中，可以通过全局数组$_SESSION来获取language：&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;$user_language = $_SESSION['language'];1&lt;/code&gt;&lt;/pre&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;依赖注入主要用于面向对像开发，现在让我们假设我们有一个SessionStorage类，该类封装了PHP Session机制：&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;class SessionStorage
{
    function __construct($cookieName = 'PHP_SESS_ID')
    {
        session_name($cookieName);
        session_start();
    }

    function set($key, $value)
    {
        $_SESSION[$key] = $value;
    }

    function get($key)
    {
        return $_SESSION[$key];
    }
    // ...
}&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&lt;code class=&quot;JavaScript&quot;&gt;&lt;br&gt;&lt;/code&gt;&lt;/p&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;同时还有一个User类提供了更高级的封装：&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;class User
{
    protected $storage;

    function __construct()
    {
        $this-&amp;gt;storage = new SessionStorage();
    }

    function setLanguage($language)
    {
        $this-&amp;gt;storage-&amp;gt;set('language', $language);
    }

    function getLanguage()
    {
        return $this-&amp;gt;storage-&amp;gt;get('language');
    }  
    // ...
}&lt;/code&gt;&lt;/pre&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;代码很简单，同样使用User类也很简单：&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;$user = new User();
$user-&amp;gt;setLanguage('fr');
$user_language = $user-&amp;gt;getLanguage();&lt;/code&gt;&lt;/pre&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;一切都很美好，除非你的程序需要更好的扩展性。假设现在你想要更改保存session_id的COOKIE键值，以下有一些可供选择的方法：&lt;/p&gt;&lt;ul class=&quot; list-paddingleft-2&quot;&gt;&lt;li&gt;&lt;p&gt;User类中创建SessionStorage实例时，在SessionStorage构造方法中使用字符串’SESSION_ID’硬编码:&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;class User
{
    function __construct()
    {
        $this-&amp;gt;storage = new SessionStorage('SESSION_ID');
    }
    // ..
}&lt;/code&gt;&lt;/pre&gt;&lt;/li&gt;&lt;/ul&gt;&lt;ul class=&quot; list-paddingleft-2&quot;&gt;&lt;li&gt;&lt;p&gt;在User类外部设置一个常量(名为STORAGE_SESSION_NAME)&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;class User
{
    function __construct()
    {
        $this-&amp;gt;storage = new SessionStorage(STORAGE_SESSION_NAME);
    }

    // ...
}

define('STORAGE_SESSION_NAME', 'SESSION_ID');&lt;/code&gt;&lt;/pre&gt;&lt;/li&gt;&lt;/ul&gt;&lt;ul class=&quot; list-paddingleft-2&quot;&gt;&lt;li&gt;&lt;p&gt;通过User类构造函数中的参数传递Session name&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;class User
{
    function __construct($sessionName)
    {
        $this-&amp;gt;storage = new SessionStorage($sessionName);
    }  // ...
}

$user = new User('SESSION_ID');&lt;/code&gt;&lt;/pre&gt;&lt;/li&gt;&lt;/ul&gt;&lt;ul class=&quot; list-paddingleft-2&quot;&gt;&lt;li&gt;&lt;p&gt;还是通过User类构造函数中的参数传递Session name，不过这次参数采用数组的方式&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;class User
{
    function __construct($storageOptions)
    {
        $this-&amp;gt;storage = new SessionStorage($storageOptions['session_name']);
    }  // ...
}

$user = new User(array('session_name' =&amp;gt; 'SESSION_ID'));&lt;/code&gt;&lt;/pre&gt;&lt;/li&gt;&lt;/ul&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;上面的方式都很糟糕。&amp;nbsp;&lt;br&gt;在user类中硬编码设置session name的做法没有真正解决问题，如果以后你还需要更改保存session_id的COOKIE键值，你不得不再一次修改user类(User类不应该关心COOKIE键值)。&amp;nbsp;&lt;br&gt;使用常量的方式同样很糟，造成User类依赖于一个常量设置。&amp;nbsp;&lt;br&gt;通过User类构造函数的参数或数组来传递session name相对来说好一些，不过也不完美，这样做干扰了User类构造函数的参数，因为如何存储Session并不是User类需要关心的，User类不应该和它们扯上关联。&lt;/p&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;另外，还有一个问题不太好解决：我们如何改变SessionStorage类。这种应用场景很多，比如你要用一个Session模拟类来做测试，或者你要将Session存储在数据库或者内存中。目前这种实现方式，在不改变User类的情况下，很难做到这点。&lt;/p&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;现在，让我们来使用依赖注入。回忆一下，之前我们是在User类内部创建SessionStorage对像的，现在我们修改一下，让SessionStorage对像通过User类的构造函数传递进去。&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;class User
{
    function __construct($storage)
    {
        $this-&amp;gt;storage = $storage;
    }

    // ...
}&lt;/code&gt;&lt;/pre&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;这就是依赖注入最经典的案例，没有之一。现在使用User类有一些小小的改变，首先你需要创建SessionStorage对像。&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;$storage = new SessionStorage('SESSION_ID');
$user = new User($storage);&lt;/code&gt;&lt;/pre&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;现在，配置session存储对像很简单了，同样如果改变session存储对像也很简单，所有这一切并不需要去更新User类，降低了业务类之间的耦合。&amp;nbsp;&lt;br&gt;Pico Container 的网站上是这样描述依赖注入：&lt;/p&gt;&lt;blockquote sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; font-size:=&quot;&quot; white-space:=&quot;&quot;&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;依赖注入是通过类的构造函数、方法、或者直接写入的方式，将所依赖的组件传递给类的方式。&lt;/p&gt;&lt;/blockquote&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;所以依赖注入并不只限于通过构造函数注入。下面来看看几种注入方式：&lt;/p&gt;&lt;ul class=&quot; list-paddingleft-2&quot;&gt;&lt;li&gt;&lt;p&gt;构造函数注入&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;class User
{
    function __construct($storage)
    {
        $this-&amp;gt;storage = $storage;
    }

    // ...
}&lt;/code&gt;&lt;/pre&gt;&lt;/li&gt;&lt;/ul&gt;&lt;ul class=&quot; list-paddingleft-2&quot;&gt;&lt;li&gt;&lt;p&gt;setter方法注入&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;class User
{
    function setSessionStorage($storage)
    {
        $this-&amp;gt;storage = $storage;
    }

    // ...
}&lt;/code&gt;&lt;/pre&gt;&lt;/li&gt;&lt;/ul&gt;&lt;ul class=&quot; list-paddingleft-2&quot;&gt;&lt;li&gt;&lt;p&gt;属性直接注入&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;class User
{
    public $sessionStorage;
}

$user-&amp;gt;sessionStorage = $storage;&lt;/code&gt;&lt;/pre&gt;&lt;/li&gt;&lt;/ul&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;根据经验，一般通过构造函数注入的是强依赖关系的组件，setter方式用来注入可选的依赖组件。&amp;nbsp;&lt;br&gt;现在，大多数流行的PHP框架都采用了依赖注入的模式实现业务组件间的高内聚低耦合。&lt;/p&gt;&lt;pre lay-lang=&quot;PHP&quot;&gt;&lt;code class=&quot;PHP&quot;&gt;// symfony: 构造函数注入的例子
$dispatcher = new sfEventDispatcher();
$storage = new sfMySQLSessionStorage(array('database' =&amp;gt; 'session', 'db_table' =&amp;gt; 'session'));
$user = new sfUser($dispatcher, $storage, array('default_culture' =&amp;gt; 'en'));
// Zend Framework: setter方式注入的例子
$transport = new Zend_Mail_Transport_Smtp('smtp.gmail.com', array('auth' =&amp;gt; 'login', 'username' =&amp;gt; 'foo', 'password' =&amp;gt; 'bar', 'ssl' =&amp;gt; 'ssl', 'port' =&amp;gt; 465,
));
$mailer = new Zend_Mail();
$mailer-&amp;gt;setDefaultTransport($transport);&lt;/code&gt;&lt;/pre&gt;&lt;p sf=&quot;&quot; ui=&quot;&quot; pingfang=&quot;&quot; hiragino=&quot;&quot; sans=&quot;&quot; microsoft=&quot;&quot; wenquanyi=&quot;&quot; micro=&quot;&quot; white-space:=&quot;&quot; background-color:=&quot;&quot; style=&quot;text-align: justify;&quot;&gt;如果对依赖注入有兴趣，强烈推荐你看《Martin Fowler introduction》或者著名的《Jeff More presentation》&amp;nbsp;&lt;br&gt;这就是本章的全部内容，希望对大家在理解依赖注入上有所帮助。在该系列后面的内容中，我们将讨论依赖注入的容器实现。&lt;/p&gt;