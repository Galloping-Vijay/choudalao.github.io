---
title: "Laravel 上传文件存储之后变 zip 格式？"
date: 2020-09-28T23:29:08+08:00
updated: 2026-02-23T17:15:23+08:00
author: "臭大佬"
categories: [php]
description: "默认情况下，本地 excel 表格通过laravel上传到服务器上变成 zip 格式了。"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 4587
---

# 问题

今天在做项目的时候，通过`laravel`上传 `excel` 表格文件，到服务端变成了压缩包（zip格式），之前上传图片是不会出现这样的问题的，不知道怎么回事，然后去查了一下中文社区的文档，里面有一句话是这么说的：

> Laravel上传文件的扩展名将通过检查文件的 MIME 类型来确定。

那我们来获取一下文件的 MIME 类型，代码如下：

```php
$file = 'D:\我的文件\期货\测试.xlsx';
if (!is_file($file)) {
$msg = '没有找到该文件';
echo $msg . "\n";
return ;
}
$msg = '文件名：' . $file;
echo $msg . "\n";
$mime_type = mime_content_type($file);
echo $mime_type;

// application/octet-stream
```

打印出来是`application/octet-stream`，至于为什么 excel 文档上传之后不是 application/x-xls 或 application/vnd.ms-excel 类型，这就不知道了。这种情况下 laravel 无法判断此文件是什么类型的，得到的是一个`zip`格式包，我还尝试解压看一下里面是什么东东，发现解压后是一堆别的东西，并不是我们上传的文件。

为了能得到自己想要的后缀，好对文件数据进行处理，我们得修改一下上传文件的后缀，下面的代码是未做处理前和处理后的代码以及得到的结果对比。

# 解决

### 前端代码
前端上传插件是用到了layui的上传组件，具体使用方法[请查看layui文档](https://www.layui.com/doc/modules/upload.html "请查看layui文档")。

```php
// html部分

<button type="button" class="layui-btn" id="up_file">
<i class="layui-icon">&#xe67c;</i>导入数据</button>
```
```php
// js部分


// 引入上传模块
//upload = layui.upload
// csrf，根据自己的配置赋值哦
var csrf_token = $('meta[name="csrf-token"]').attr('content');

//上传代码
var uploadInst = upload.render({
                elem: '#up_file'
                , url: '接口地址'
                , headers: {
                    'X-CSRF-TOKEN': csrf_token  // 根据自身情况配置或者忽略
                }
                , accept: 'file'
                , field: "file"
                , type: 'file'
                , exts: 'xls|xlsx' //设置一些后缀，用于演示前端验证和后端的验证
                , before: function (obj) {
                    //预读本地文件示例，不支持ie8
                }
                , done: function (res) {
                    //如果上传失败
                    if (res.code > 0) {
                        return layer.msg('上传失败', {icon: 2});
                    }
                    //上传成功
                    layer.msg(res.msg, {icon: 1});
                    //table.reload('LAY-app-list'); // 重载表格
                }
                , error: function () {
                    //演示失败状态，并实现重传
                    var up_logo_text = $('#up_logo_text');
                    up_logo_text.html('<span style="color: #FF5722;">上传失败</span> <a class="layui-btn layui-btn-xs demo-reload">重试</a>');
                    up_logo_text.find('.demo-reload').on('click', function () {
                        uploadInst.upload();
                    });
                }
            });
```

### 后端

*self::resJson() 是自己封装的返回方式，请自行替换*

#### 修改前的接口

```php
/**
     * Description:
     * User: Vijay <1937832819@qq.com>
     * Date: 2020/09/09
     * Time: 11:21
     * @param Request $request
     * @return \Illuminate\Contracts\Routing\ResponseFactory|\Illuminate\Http\Response
     * @throws \PhpOffice\PhpSpreadsheet\Exception
     * @throws \PhpOffice\PhpSpreadsheet\Reader\Exception
     */
public function import(Request $request)
    {
        if (!$request->isMethod('post')) {
            return self::resJson(1, '请求方式错误');
        }
        //上传文件
        if (!$request->hasFile('file')) {
            return self::resJson(1, '请上传文件');
        }
        $date = date('Ymd');
        $path = $request->file('file')->store('', 'uploads');
        if (!$path) {
            return self::resJson(1, '上传失败');
        }
        $filename = public_path('/uploads/' . $date . '/' . $path);
        if (!is_file($filename)) {
            return self::resJson(1, '未找到该文件');
        }
        // XlsxJob::dispatch($filename);// 压入后台队列处理表格数据
        return self::resJson(0, '上传成功，已在后台处理数据');
}
```
上传后得到的文件如下：
![](https://www.choudalao.com/uploads/20200928/20200928232657w4NshM.png)

#### 修改后端接口
```php
/**
     * Description:
     * User: Vijay <1937832819@qq.com>
     * Date: 2020/09/09
     * Time: 11:21
     * @param Request $request
     * @return \Illuminate\Contracts\Routing\ResponseFactory|\Illuminate\Http\Response
     * @throws \PhpOffice\PhpSpreadsheet\Exception
     * @throws \PhpOffice\PhpSpreadsheet\Reader\Exception
     */
    public function import(Request $request)
    {
        if (!$request->isMethod('post')) {
            return self::resJson(1, '请求方式错误');
        }
        //上传文件
        if (!$request->hasFile('file')) {
            return self::resJson(1, '请上传文件');
        }
        //设置文件后缀白名单
        $allowExt = ["csv", "xls", "xlsx"];
        //设置存储目录
        $date    = date('Ymd');
        $tmpPath = '/uploads/' . $date;
        // 绝对路径
        $dirPath = public_path($tmpPath);
        //如果目标目录不能创建
        if (!is_dir($dirPath) && !mkdir($dirPath, 0777, true)) {
            return self::resJson(1, '上传目录没有创建文件夹权限');
        }
        //如果目标目录没有写入权限
        if (is_dir($dirPath) && !is_writable($dirPath)) {
            return self::resJson(1, '上传目录没有写入权限');
        }
        //获取文件
        $file = $request->file('file');
        //校验文件
        if (!isset($file) || !$file->isValid()) {
            return self::resJson(1, '上传失败');
        }
        $ext = $file->getClientOriginalExtension(); //上传文件的后缀
        //判断是否是Excel
        if (empty($ext) or in_array(strtolower($ext), $allowExt) === false) {
            return self::resJson(1, '不允许的文件类型');
        }
        //生成文件名
        $fileName = uniqid() . '_' . dechex(microtime(true)) . '.' . $ext;
        try {
            //存储文件
            $file->move($dirPath, $fileName);
            // 获取文件路径
            $filename = $dirPath . '/' . $fileName;
            if (!is_file($filename)) {
                return self::resJson(1, '未找到该文件');
            }
            // 队列处理表格数据
            XlsxJob::dispatch($filename);
            return self::resJson(0, '上传成功，已在后台处理数据');
        } catch (\Exception $ex) {
            return self::resJson(1, $ex->getMessage());
        }
    }
```

这样上传就可以得到源文件的后缀了，

![](https://www.choudalao.com/uploads/20200928/202009282332405Z9g7m.png)