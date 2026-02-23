---
title: "vscode 中使用 php xdebug"
date: 2025-03-31T18:34:03+08:00
updated: 2026-02-23T19:57:04+08:00
author: "臭大佬"
categories: [php]
description: "vscode 中使用 php xdebug"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 1778
---

# 前提
#### 环境:
win本地使用vscode,php环境是在wsl中的.

# 安装
## php安装xdebug扩展
在wsl的php中安装xdebug,此步骤比较简单,网上教程很多,这里略过.安装完配置如下:
php.ini
```go
[Xdebug]
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_port=9003
xdebug.client_host=localhost
;xdebug.log=/tmp/xdebug.log
xdebug.discover_client_host=true
xdebug.log_level=3
zend_extension=/www/server/php/73/lib/php/extensions/no-debug-non-zts-20180731/xdebug.so

```
#### 配置项解释
> zend_extension: 指定Xdebug扩展的路径。在你的配置里，它指向了PHP 7.3扩展库目录 no-debug-non-zts-20180731 下的 xdebug.so 文件。
xdebug.mode: 设定Xdebug的工作模式，debug 表示开启调试模式。
xdebug.start_with_request: 开启该选项后，每次HTTP请求都会自动启动调试会话。
xdebug.client_port: 这是Xdebug用于连接调试客户端的端口号，默认是 9003。
xdebug.client_host: 此配置指定调试客户端的主机名或IP地址。host.docker.internal 是Docker环境里的特殊主机名，用于指代宿主机。
xdebug.log: 该配置指定Xdebug日志文件的路径，在排查问题时非常有用。
xdebug.discover_client_host: 开启此选项后，Xdebug会自动发现调试客户端的IP地址，适用于客户端IP地址经常变化的场景。


## vscode 安装 PHP Debug
vscode的扩展中搜索PHP Debug 并安装
![](https://www.choudalao.com/uploads/20250331/20250331180839JH89Wa.png)
安装完,安装左侧的小虫子,然后点击设置按钮,配置相关的信息
![](https://www.choudalao.com/uploads/20250331/20250331180934y0QyZn.png)

launch.json 文件的配置重点
```go
    {
      "name": "Listen for Xdebug (WSL)",
      "type": "php",
      "request": "launch",
      "port": 9003,
      "pathMappings": {
         "/mnt/d/wwwroot/hz/php": "${workspaceFolder}"
      }
    },
```
### 配置项解释
> pathMappings:这里的 /mnt/d/wwwroot/hz/php 是WSL中对应的项目路径，你要根据实际情况修改.${workspaceFolder}为当前工作区.
port:监听的端口,


我们开启了9003端口监听,这时候,需要把win的端口和wsl端口进行映射:
登录wsl
```go
bash
```
获取wsl的ip
```go
ip addr | grep eth0
```
*inet 172.19.129.11/20 brd 172.19.143.255 scope global eth0*

172.19.129.11 就是wsl的ip,下面命令会用到.
在win的下运行 powershell,对端口进行映射:
```go
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=9003 connectaddress=172.19.129.11 connectport=9003
```
查看所有映射端口
```go
netsh interface portproxy show all
```
如果要删除某些端口的映射的话(非不要步骤)
```go
netsh interface portproxy delete v4tov4 listenport=9003 listenaddress=0.0.0.0
```



配置完成后,点击就可以进行调试了.

![](https://www.choudalao.com/uploads/20250331/20250331182110vHtvGS.png)

# 问题
### 开启后无效果
###### 检查launch.json的目录配置是否正确
###### 查看端口占用(win下运行)
```go
netstat -ano | findstr "9003"
```
开启后正常是2条监听,如果xdebug无效果,建议全部进程关闭后再开启.
如果看到有进程占用，使用以下命令关闭
```go
taskkill /F /PID <进程ID>
```
重启 web 服务器和 VSCode 后再试。

### 开启Xdebug后请求变慢
开启Xdebug后请求变慢是比较常见的现象，这是因为Xdebug在运行过程中会进行大量的调试信息收集和处理工作，增加了额外的性能开销。把 xdebug.start_with_request 设置为 trigger，这样只有在请求中包含特定的调试触发参数时，Xdebug才会启动调试会话。修改 php.ini 文件如下：
php.ini
```go
xdebug.start_with_request = trigger
```
之后，若要开启调试，可在请求的URL里添加 XDEBUG_SESSION_START=1 参数，例如 http://xxx.com/?XDEBUG_SESSION_START=1。

xdebug.log 开启后，Xdebug会把调试信息记录到日志文件中，频繁的文件写入操作会影响性能。
```go
; 关闭日志记录
; xdebug.log = /tmp/xdebug.log
; 设置日志级别为更高的值，减少日志输出
xdebug.log_level = 3
```