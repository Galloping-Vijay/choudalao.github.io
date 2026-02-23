---
title: "Git 利用 Webhooks 实现代码的自动拉取"
date: 2020-04-30T00:43:11+08:00
updated: 2026-02-23T05:05:44+08:00
author: "臭大佬"
categories: [其他]
description: "Git 利用 Webhooks 实现代码的自动拉取"
cover: "https://www.choudalao.com/uploads/20200429/gqjSXkRS1SqpMsBpcp1Y4Awrz7ZooLN2wOZXL4Lq.jpeg"
click: 3933
---

# WebHook 简介
WebHook 功能是帮助用户 push 代码后，自动回调一个您设定的 http 地址。 这是一个通用的解决方案，用户可以自己根据不同的需求，来编写自己的脚本程序。

# 环境
服务器：ubuntu
php：7.2.28

本文以拉取码云（github、Coding等均适用）为例，利用WebHook实现PHP自动部署Git代码。
因为PHP脚本涉及到shell命令执行，所以要删除php.ini里面的禁用函数：exec、shell_exec等。
![](https://www.choudalao.com/uploads/20200429/20200429233551WWioHW.png)

由于权限问题，所以，需要为目录和文件设置拥有者、所属组。
```php
sudo chown -R www:www /www/wwwroot/choudalao

```
# 生成公钥
公钥分为
1. git用户公钥（SSH公钥），
2. 部署公钥。

### SSH公钥
```shell
// 换成自己的邮箱
ssh-keygen -t rsa -C "1937832819@qq.com"
```
![](https://www.choudalao.com/uploads/20200430/20200430002525zLVDaz.png)
查看并复制
```shell
sudo cat /home/ubuntu/.ssh/id_rsa.pub
```
![](https://www.choudalao.com/uploads/20200430/20200430002612dc4WXl.png)

打开码云，点击头像下拉框的设置。新建一个SSH公钥。
![](https://www.choudalao.com/uploads/20200430/20200430002657gNlqHW.png)

![](https://www.choudalao.com/uploads/20200430/20200430002725l43pRM.png)

如果绑定邮箱，添加成功会受到一条邮件。

![](https://www.choudalao.com/uploads/20200430/20200430002925J7G0L5.png)

### 部署公钥
```shell
// 创建 .ssh目录
sudo mkdir /home/www/.ssh
// 将目录 .ssh 的拥有者、所属组修改为 www（如果已经是就不用改了）
sudo chown -R www:www /home/www/.ssh
// 在 /home/www/.ssh 目录下生成密钥,邮箱请与码云上一致
sudo -Hu www ssh-keygen -t rsa -C "1937832819@qq.com"
```
![](https://www.choudalao.com/uploads/20200430/20200430003148ch0tj2.png)
![](https://www.choudalao.com/uploads/20200430/20200430003153PGGNdp.png)
成功后，查看并复制
```shell
// 部署公钥生成后，执行下面的代码查看公钥，复制
sudo cat /home/www/.ssh/id_rsa.pub
```
码云上回到我们的项目目录，复制粘贴我们的项目公钥。
![](https://www.choudalao.com/uploads/20200430/20200430003238ngAasV.png)

# git 的全局配置
```shell
sudo -Hu www git config --global credential.helper store # 永久保存
sudo -Hu www git config --global user.name "1937832819@qq.com" 
sudo -Hu www git config --global user.email "1937832819@qq.com" # 邮箱请与码云上一致
```
配置完成之后可以 clone 或 pull 项目来验证是否配置成功（注意：要切换成www运行用户来进行操作），若多次操作只需输入一次用户名、密码，即配置成功，若每一次操作都有输入用户名密码，则配置不成功，需要重新检查配置。

# 仓库配置
打开码云的项目，管理，然后对WebHook进行配置，大概如下
![](https://www.choudalao.com/uploads/20200429/20200429234027e9Z77R.png)

# 钩子代码
编辑web_hook.php文件
```php
<?php
/**
 * Description:钩子
 * Created by PhpStorm.
 * User: Vijay <1937832819@qq.com>
 * Date: 2020/4/29
 * Time: 22:27
 */
 
/**
 * Description:创建目录
 * User: Vijay <1937832819@qq.com>
 * Site: https://www.choudalao.com/
 * Date: 2022/3/17
 * Time: 16:26
 * @param $dir
 * @param int $mode
 * @return bool
 */
function mkdirs($dir, $mode = 0777)
{
    if (is_dir($dir) || @mkdir($dir, $mode)) return true;
    if (!mkdirs(dirname($dir), $mode)) return false;
    return @mkdir($dir, $mode);
}

// 日志目录
$path = './runtime/log';
mkdirs($path);

// 接收码云POST过来的信息
$json = $GLOBALS['HTTP_RAW_POST_DATA'];
$data = json_decode($json, true);

// 打开网站目录下的hooks.log文件 需要在服务器上创建 并给写权限
$fs = fopen($path . '/webhooks_pull_' . date("m_d_H") . '.log', 'a');
fwrite($fs, '================ Update Start ===============' . PHP_EOL . PHP_EOL);
// 自定义密码 用于验证 与码云后台设置保持一致
$access_token = 'zkym';
$client_token = $data['password'];

// 请求ip
$client_ip = $_SERVER['REMOTE_ADDR'];
// 把请求的IP和时间写进log
fwrite($fs, 'Request on [' . date("Y-m-d H:i:s") . '] from [' . $client_ip . ']' . PHP_EOL);
fwrite($fs, 'php belongs to [' . system("whoami") . ']' . PHP_EOL);

// 验证token 有错就写进日志并退出
if ($client_token !== $access_token) {
    echo "error 403";
    fwrite($fs, "Invalid token [{$client_token}]" . PHP_EOL);
    $fs and fclose($fs);
    exit(0);
}

// 如果有需要 可以打开下面，把传送过来的信息写进log 可用于调试，测试成功后注释即可
// fwrite($fs, 'Data: ' . print_r($data, true) . PHP_EOL);

// 执行shell命令,cd到网站根目录，执行git pull进行拉取代码，并把返回信息写进日志
exec('cd /www/wwwroot/choudalao; git pull 2<&1; chown -R www:www /www/wwwroot/choudalao/*;', $output);
fwrite($fs, 'Info:' . print_r($output, true) . PHP_EOL);
fwrite($fs, PHP_EOL . '================ Update End ===============' . PHP_EOL . PHP_EOL);
$fs and fclose($fs);

// 调试时打开
// echo json_encode($output);
```
# 调试
大部分已经完成了，接下来我们来测试一下，
#### 本地修改并提交
```shell
git commit -am's'
```

![](https://www.choudalao.com/uploads/20200430/20200430094231VN4Hmc.png)

```shell
git push
```
![](https://www.choudalao.com/uploads/20200430/20200430094327ZJnD8d.png)

### 查看我们的日志文件
![](https://www.choudalao.com/uploads/20200430/20200430094413jvVhF2.png)

## 发现有一个报错
```shell
fatal: could not read Username for 'https://gitee.com': No such device or address
```
这是因为git config文件中没有用户身份信息

### 解决方法
在请求串中加入身份信息即可：
格式

 ```php
https://[userName]:[password]@gitee.com/[username]/project.git
```
 操作
```shell
cd .git
vim config
```
![](https://www.choudalao.com/uploads/20200430/20200430095101DhKX0i.png)

## 问题：.git/FETCH_HEAD: Permission denied

![](https://www.choudalao.com/uploads/20220317/20220317162200ArpO0j.png)
.git/FETCH_HEAD的这个文件所属组和所属主是root权限，而我用webhook的用户组是www，解决方法就是修改文件的用户组和所属用户。
```php
cd .git/

chown www:www FETCH_HEAD
```


本地再次推送，查看日志。
![](https://www.choudalao.com/uploads/20200430/202004300952398cdQQJ.png)

大功靠成。