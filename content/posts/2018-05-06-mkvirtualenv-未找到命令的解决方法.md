---
title: "mkvirtualenv： 未找到命令的解决方法"
date: 2018-05-06T06:55:14+08:00
updated: 2026-02-23T16:06:15+08:00
author: "臭大佬"
categories: [Python]
description: "mkvirtualenv： 未找到命令的解决方法"
cover: "http://www.choudalao.com/uploads/20191016/BMc4lopFAIM9lipkfAY0iFeXr7uj2rYGKR4Xc7Rr.jpeg"
click: 6048
---

&lt;p style=&quot;text-align: justify;&quot;&gt;1.升级python包管理工具pip&lt;span&gt;(如果您的pip可以用,不建议升级,因为升级后可能和您的python版本的包不匹配,导致无法使用,所以,pip可以用的话,跳过步骤1)&lt;/span&gt;&lt;/p&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;pip install --upgrade pip&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;&lt;span&gt;备注：当你想升级一个包的时候 `pip install --upgrade 包名`&lt;/span&gt;&lt;/p&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;&lt;span&gt;&lt;br&gt;&lt;/span&gt;&lt;/p&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;2.python虚拟环境安装&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;sudo apt-get install python-virtualenv
sudo easy_install virtualenvwrapper&lt;/code&gt;&lt;/pre&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;上述工具装好后找不到mkvirtualenv命令，需要执行以下环境变量设置。&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;1.创建目录用来存放虚拟环境
    mkdir $HOME/.virtualenvs
2.在~/.bashrc中添加行：
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
3.运行:
    source ~/.bashrc&lt;/code&gt;&lt;/pre&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;3.创建python虚拟环境&lt;/p&gt;&lt;pre lay-lang=&quot;JavaScript&quot;&gt;&lt;code class=&quot;JavaScript&quot;&gt;mkvirtualenv [虚拟环境名称]
workon [虚拟环境名称]&lt;/code&gt;&lt;/pre&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;4.退出虚拟环境 离开 deactivate&lt;/p&gt;&lt;p style=&quot;text-align: justify;&quot;&gt;5.删除(慎用)&amp;nbsp;&lt;br&gt;rmvirtualenv [虚拟环境名称]&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;