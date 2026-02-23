---
title: "Jenkins 的 Generic Webhook Trigger 插件简单使用"
date: 2024-04-12T10:58:05+08:00
updated: 2026-02-23T18:40:15+08:00
author: "臭大佬"
categories: [linux]
description: "Jenkins 的 Generic Webhook Trigger 插件简单使用"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 3799
---

# 介绍
`Generic Webhook Trigger`可以用来接收参数,传递给构建脚本,这点非常适用于`webhook`,下面我们以get传参来演示使用

# 使用
### 安装

### 配置Generic Webhook Trigger插件
在Jenkins Pipeline Job的配置中，找到“Generic Webhook Trigger”部分，进行如下配置：

Token：配置token，以验证请求的合法性。
Request Parameters：
对于每个参数，设置如下：
Name：参数名，如branch、obj、gitUser、env和gitCommit。
Value：保留空白或留空，因为插件会自动从请求URL中提取这些参数值。
Variable Name：为每个参数指定一个变量名，这个变量名将在Pipeline脚本中用来访问参数值。确保这里的变量名与Pipeline脚本中定义的参数名（包括大小写）完全一致。

### 更新Pipeline脚本
当配置完参数时,我们可以在脚本中通过全局变量`${env.参数名}`使用变量,如下:
```go
pipeline {
    agent any
    stages {
        stage('Run Shell') {
            steps {
                sh """
                    echo "env: ${env.env}"
                    echo "obj: ${env.obj}"
                    echo "branch: ${env.branch}"
                    echo "gitUser: ${env.gitUser}"
                    echo "gitCommit: ${env.gitCommit}"
                """
            }
        }
    }
}
```