---
title: "error during connect: Get http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.40/images/json:"
date: 2020-07-23T15:40:25+08:00
updated: 2026-02-23T16:50:07+08:00
author: "臭大佬"
categories: [Go]
description: "error during connect: Get http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.40/images/json: open //./pipe/docker_engine: The system cannot find the file specified. In the default daemon configuration on Windows"
cover: "https://www.choudalao.com/uploads/20200723/aWbqNsx6avjfSvI4NINgtv0ywqRyU2tuxDGUNmX4.jpeg"
click: 7559
---

# 问题

Win10在运行 `docker` 命令的时候报如下错误:

> error during connect: Get http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.40/images/json: open //./pipe/docker_engine: The system cannot find the file specified. In the default daemon configuration on Windows, the docker client must be run elevated to connect. This error may also indicate that the docker daemon is not running.

![](https://www.choudalao.com/uploads/20200723/202007231537202ExhLx.png)

# 解决方案

点击工具栏docker desktop的小图标上右键，然后 Setting--> General-->勾选Expose daemon on tcp localhost那个选项。重启

![](https://www.choudalao.com/uploads/20200723/20200723153912wrLxDi.png)

![](https://www.choudalao.com/uploads/20200723/20200723154011BsTOiN.png)