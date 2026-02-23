---
title: "WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available."
date: 2020-10-07T00:39:31+08:00
updated: 2026-02-23T17:16:54+08:00
author: "臭大佬"
categories: [Python]
description: "WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available."
cover: "https://www.choudalao.com/uploads/20201007/M7O7Ot9vWz8BpOQBb0wDZ0HNJfCGmw0zGD300xPh.jpeg"
click: 14772
---

# 问题
`win10`下使用`Anaconda`，在`vscode`中格式化`python`代码时，提示安装`yapf`、`flake8`等包时，报如下错误；
```python
// 按照提示，点击安装就会在终端自动运行如下代码
& "D:/Program Files/Anaconda3/python.exe" d:\Program\ms-python.python-2020.9.112786\pythonFiles\pyvsc-run-isolated.py pip install -U yapf
```

![](https://www.choudalao.com/uploads/20201007/20201007003421RmCFwN.png)

~~WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Collecting yapf
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  Could not fetch URL https://pypi.org/simple/yapf/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/yapf/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
  ERROR: Could not find a version that satisfies the requirement yapf (from versions: none)
ERROR: No matching distribution found for yapf
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
PS D:\wwwroot\waibao\dev.qihuo.net> & "D:/Program Files/Anaconda3/python.exe" d:\Program\ms-python.python-2020.9.112786\pythonFiles\pyvsc-run-isolated.py pip --trusted-host pypi.python.org install -U yapf
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Collecting yapf
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/yapf/
  Could not fetch URL https://pypi.org/simple/yapf/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/yapf/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
  ERROR: Could not find a version that satisfies the requirement yapf (from versions: none)
ERROR: No matching distribution found for yapf
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping~~

# 解决方法
看样子是证书错了。
打开这个链接下载：https://slproweb.com/products/Win32OpenSSL.html

下载安装，

![](https://www.choudalao.com/uploads/20201007/20201007003620pXpcIs.png)

安装完成后，再次格式化代码，这次提示安装`autopep8`，点击确定，查看效果

![](https://www.choudalao.com/uploads/20201007/20201007003847NjA2FG.png)

这次安装成功了，再次格式化，已经可以对齐了。