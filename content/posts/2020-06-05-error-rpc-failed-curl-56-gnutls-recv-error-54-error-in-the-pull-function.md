---
title: "error: RPC failed; curl 56 GnuTLS recv error (-54): Error in the pull function."
date: 2020-06-05T00:23:20+08:00
updated: 2026-02-23T16:37:20+08:00
author: "臭大佬"
categories: [其他]
description: "error: RPC failed; curl 56 GnuTLS recv error (-54): Error in the pull function."
cover: "https://www.choudalao.com/uploads/20200605/UcxCAW0DGp57evIi4gCBkRPAsLDQG6xTsYyx8amF.jpeg"
click: 9466
---

# 报错信息
```php
error: RPC failed; curl 56 GnuTLS recv error (-54): Error in the pull function.
fatal: The remote end hung up unexpectedly
fatal: early EOF
fatal: index-pack failed
```
![](https://www.choudalao.com/uploads/20200605/20200605001917OPLMIR.png)

# 解决
1：在ssh终端输入如下命令：
```php
git config --global http.postBuffer 524288000
```
2：修改配置文件~/.bashrc，打开配置文件
```php
vim ~/.bashrc
```

3：在配置文件最后面加上下面三行代码。
```php
export GIT_TRACE_PACKET=1

export GIT_TRACE=1

export GIT_CURL_VERBOSE=1
```
![](https://www.choudalao.com/uploads/20200605/20200605002200OlTZwA.png)

4： 保存退出，配置文件生效。

# 追加
如果上面的方式依旧不行，不如就重新克隆一份代码。
```php
git clone https://github.com/Galloping-Vijay/laravel-wjfcms --depth 1
```
```php
cd laravel-wjfcms
```
```php
git fetch --unshallow
```

depth用于指定克隆深度，为1即表示只克隆最近一次commit.（git shallow clone）

git clone 默认会下载项目的完整历史版本，如果你只关心最新版的代码，而不关心之前的历史信息，可以使用 git 的浅复制功能：
```php
git clone --depth=1 https://github.com/Galloping-Vijay/laravel-wjfcms
```

--depth=1 表示只下载最近一次的版本，使用浅复制可以大大减少下载的数据量，例如， CodeIgniter 项目完整下载有近 100MiB ，而使用浅复制只有 5MiB 多，这样即使在恶劣的网络环境下，也可以快速的获得代码。如果之后又想获取完整历史信息，可以使用下面的命令：
```php
git fetch --unshallow
```

或者，如果你只是想下载最新的代码看看，你也可以直接从 GitHub 上下载打包好的 ZIP 文件，这比浅复制更快，因为它只包含了最新的代码文件，而且是经过 ZIP 压缩的。但是很显然，浅复制要更灵活一点。
————————————————
版权声明：本文为CSDN博主「莱宝」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_21508727/article/details/89413590