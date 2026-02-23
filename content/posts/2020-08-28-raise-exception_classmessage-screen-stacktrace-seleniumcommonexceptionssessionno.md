---
title: "raise exception_class(message, screen, stacktrace) selenium.common.exceptions.SessionNotCreatedException"
date: 2020-08-28T16:39:02+08:00
updated: 2026-02-23T17:06:12+08:00
author: "臭大佬"
categories: [Python]
description: "raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 80"
cover: "https://www.choudalao.com/uploads/20200828/D2c7BvKpt4yuzrZmuJf9GUJbPhX5FpkVtUeZKVyc.jpeg"
click: 14470
---

# 问题
> selenium中遇到这种报错
DevTools listening on ws://127.0.0.1:56919/devtools/browser/7517880e-0888-4503-84a1-d8080d70bbe6
Traceback (most recent call last):
  File "qince.py", line 233, in <module>
    login(user, pw)  # 后面会继续实现cookie保存，爬取信息，存储数据库。
  File "qince.py", line 202, in login
    login_button = driver.find_element_by_name('imageField2')  # 找到登录按钮
  File "E:\Program Files (x86)\Anaconda3\envs\tensorflow\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 496, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "E:\Program Files (x86)\Anaconda3\envs\tensorflow\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "E:\Program Files (x86)\Anaconda3\envs\tensorflow\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "E:\Program Files (x86)\Anaconda3\envs\tensorflow\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[name="imageField2"]"}
  (Session info: chrome=85.0.4183.83)
  
![](https://www.choudalao.com/uploads/20200828/20200828163816mKolAY.png)

# 解决

那是因为版本对不上，根据文章重新下载配置就可以：
https://www.choudalao.com/article/123