---
title: "phpstorm 输入法中文不同步 phpstorm 输入法不跟随光标解决办法"
date: 2017-09-14T10:46:50+08:00
updated: 2026-02-23T09:10:26+08:00
author: "臭大佬"
categories: [php]
description: "phpstorm 输入法中文不同步 phpstorm 输入法不跟随光标解决办法"
cover: "http://www.choudalao.com/uploads/20191016/mvtwfcqoAIlIb6uPrJwzb2XMg5T47KQjUnA3qSeT.jpeg"
click: 2878
---

&lt;p&gt;&lt;span&gt;昨天刚刚把phpstrom更新到2017.2.4，发现输入法中文输入的时候，候选字没有跟随光标移动。百度了一波,终于找到决方案。&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span&gt;就是替换phpstorm安装目录下的 jre64文件夹。&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span&gt;下载&amp;nbsp;&amp;nbsp;&lt;p&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://bintray.com/jetbrains/intellij-jdk/download_file?file_path=jbsdk8u112b736.21_windows_x64.tar.gz&quot;&gt;https://bintray.com/jetbrains/intellij-jdk/download_file?file_path=jbsdk8u112b736.21_windows_x64.tar.gz&lt;/a&gt;&lt;/p&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;解压更名&amp;nbsp;&lt;code class=&quot;inline-code prettyprint prettyprinted&quot; courier=&quot;&quot;&gt;jre64&lt;/code&gt;&amp;nbsp; 替换掉安装目录下的jre64，注意是解压的目录直接改成jre64，不是复制其中的jre文件夹改名。&lt;br&gt;&lt;br&gt;替换前，原jre64目录注意备份!&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span&gt;重新启动phpstorm，一切正常！谢谢前辈的总结~&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span&gt;&lt;br&gt;&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span&gt;转载自&amp;nbsp;&lt;/span&gt;&lt;a target=&quot;_blank&quot; href=&quot;http://www.cnblogs.com/guohong-hu/p/7258014.html&quot;&gt;http://www.cnblogs.com/guohong-hu/p/7258014.html&lt;/a&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;