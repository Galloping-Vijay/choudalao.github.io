---
title: "Git 2.0 from 'matching' to 'simple'. To squelch this message"
date: 2019-12-08T11:15:21+08:00
updated: 2026-02-23T03:14:19+08:00
author: "臭大佬"
categories: [其他]
description: "Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:"
cover: "https://www.choudalao.com/uploads/20191208/oBSwwWRZQUHOTBHvmLcPYF3HzIC9rU4vUOCft8eq.jpeg"
click: 4330
---

# 起因
最近在使用git的时候,总是会出现如下提示:
```shell
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

```

![](https://www.choudalao.com/uploads/20191208/201912081113129UnAHa.png)

#解释
当 push.default 的值设置成 ‘matching’ ，git 将会推送所有本地已存在的同名分支到远程仓库
从 Git 2.0 开始，git 采用更加保守的值'simple'，只会推送当前分支到相应的远程仓库，'git pull' 也将值更新当前分支。

警告：push.default （默认push）未设置；在Git 2.0 中，push.default 的值从‘matching’改为‘simple’了。消除此警告并保留以前的习惯，输入：
`git config --global push.default matching
`
消除此警告并采用新的设置值，输入：`git config --global push.default simple
`

Git 2.0 需要设置 push.default 的值，两者的区别上面也说了，所以我就采用新的保守值吧，输入：
```shell
git config --global push.default simple

```