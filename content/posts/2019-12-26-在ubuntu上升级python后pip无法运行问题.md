---
title: "在Ubuntu上升级python后pip无法运行问题"
date: 2019-12-26T22:22:02+08:00
updated: 2026-02-23T18:40:01+08:00
author: "臭大佬"
categories: [Python]
description: "ERROR: Exception:
Traceback (most recent call last):
  File \"/usr/local/lib/python3.7/site-packages/pip/_internal/cli/base_command.py\", line 153, in _main"
cover: "https://www.choudalao.com/uploads/20191226/bDfZmopW3PJsaXAPKtqIXmbkxhO39wBoOyRStESI.jpeg"
click: 11235
---

# 起因

今天把ubuntu上python3.5升级成了3.7之后，`pip -V`输出结果正常，

![](https://www.choudalao.com/uploads/20191226/20191226221023nAVBm4.png)

但是执行`pip install xxx`就报错，如下一长串：

```shell
ERROR: Exception:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/base_command.py", line 153, in _main
    status = self.run(options, args)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/commands/install.py", line 328, in run
    session = self.get_default_session(options)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/req_command.py", line 72, in get_default_session
    self._session = self.enter_context(self._build_session(options))
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/req_command.py", line 84, in _build_session
    index_urls=self._get_index_urls(options),
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/network/session.py", line 240, in __init__
    self.headers["User-Agent"] = user_agent()
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/network/session.py", line 133, in user_agent
    zip(["name", "version", "id"], distro.linux_distribution()),
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 122, in linux_distribution
    return _distro.linux_distribution(full_distribution_name)
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 677, in linux_distribution
    self.version(),
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 737, in version
    self.lsb_release_attr('release'),
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 899, in lsb_release_attr
    return self._lsb_release_info.get(attribute, '')
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 552, in __get__
    ret = obj.__dict__[self._fname] = self._f(obj)
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 1012, in _lsb_release_info
    stdout = subprocess.check_output(cmd, stderr=devnull)
  File "/usr/local/lib/python3.7/subprocess.py", line 395, in check_output
    **kwargs).stdout
  File "/usr/local/lib/python3.7/subprocess.py", line 487, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '('lsb_release', '-a')' returned non-zero exit status 1.
Traceback (most recent call last):
  File "/home/ubuntu/.local/bin/pip", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/main.py", line 47, in main
    return command.main(cmd_args)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/base_command.py", line 103, in main
    return self._main(args)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/base_command.py", line 191, in _main
    self.handle_pip_version_check(options)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/req_command.py", line 139, in handle_pip_version_check
    timeout=min(5, options.timeout)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/req_command.py", line 84, in _build_session
    index_urls=self._get_index_urls(options),
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/network/session.py", line 240, in __init__
    self.headers["User-Agent"] = user_agent()
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/network/session.py", line 133, in user_agent
    zip(["name", "version", "id"], distro.linux_distribution()),
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 122, in linux_distribution
    return _distro.linux_distribution(full_distribution_name)
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 677, in linux_distribution
    self.version(),
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 737, in version
    self.lsb_release_attr('release'),
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 899, in lsb_release_attr
    return self._lsb_release_info.get(attribute, '')
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 552, in __get__
    ret = obj.__dict__[self._fname] = self._f(obj)
  File "/usr/local/lib/python3.7/site-packages/pip/_vendor/distro.py", line 1012, in _lsb_release_info
    stdout = subprocess.check_output(cmd, stderr=devnull)
  File "/usr/local/lib/python3.7/subprocess.py", line 395, in check_output
    **kwargs).stdout
  File "/usr/local/lib/python3.7/subprocess.py", line 487, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '('lsb_release', '-a')' returned non-zero exit status 1.

```

![](https://www.choudalao.com/uploads/20191226/20191226221146vW0ynh.png)
![](https://www.choudalao.com/uploads/20191226/20191226221201AIhXjR.png)

网上查了各种资料，尝试了很多方式，如最多的就是修改`/usr/bin/pip3`的，最后看到错误信息的最后一行，终于找到了突破口。

# 分析

原因是找不到lsb_release模块

# 解决

找到lsb_release模块所在的目录，将其复制到设置python3.7的系统模块加载位置，也就是报错处subprocess.py所在的目录
`/usr/local/lib/python3.7/`

### 查找

```shell
sudo find / -name 'lsb_release.py'
```

![](https://www.choudalao.com/uploads/20191226/201912262216227iw9Fw.png)

### 复制

```shell
sudo cp  /usr/lib/python3/dist-packages/lsb_release.py /usr/local/lib/python3.7/

```

![](https://www.choudalao.com/uploads/20191226/20191226221723Xtr7BG.png)

### 查看结果

![](https://www.choudalao.com/uploads/20191226/20191226221753zLj21R.png)

哎，花费了我一晚上时间啊，吃一堑长一智，记录一下。