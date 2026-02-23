# 臭大佬博客 - Claude 工作指南

## 项目概述

这是一个基于 Hugo 的静态博客项目，托管在 GitHub Pages。

**项目路径**：`D:\wwwroot\web\choudalao.github.io`

**技术栈**：
- Hugo Extended v0.156.0
- Mainroad 主题
- GitHub Actions 自动部署

---

## 项目结构

```
choudalao.github.io/
├── content/posts/      # 342 篇 Markdown 文章
├── public/             # 生成的静态网站（不要手动修改）
├── static/             # 静态资源（图片、样式等）
├── themes/             # Hugo 主题缓存
├── hugo.exe            # Hugo Extended 可执行文件
├── hugo.toml           # Hugo 配置文件
├── export_to_hugo.py   # 从数据库导出文章的脚本
├── BLOG_SETUP.md       # 博客搭建文档
├── WRITE_BLOG.md       # 写博客流程文档
└── README.md           # 项目说明
```

---

## 常用命令

```bash
# 进入项目目录
cd D:/wwwroot/web/choudalao.github.io

# 构建静态网站
./hugo.exe

# 构建并最小化
./hugo.exe --minify

# 启动本地预览服务器
./hugo.exe server

# 预览并包含草稿
./hugo.exe server -D

# 创建新文章
./hugo.exe new content/posts/文章标题.md
```

---

## 文章格式

所有文章位于 `content/posts/` 目录，文件名格式：`YYYY-MM-DD-文章标题.md`

文章 front matter 示例：

```yaml
---
title: "文章标题"
date: 2026-02-23T12:00:00+08:00
author: "臭大佬"
categories: ["分类"]
tags: ["标签1", "标签2"]
description: "文章摘要"
---
```

---

## 部署流程

项目已配置 GitHub Actions 自动部署，推送代码到 `main` 分支后自动部署。

```bash
git add .
git commit -m "提交说明"
git push
```

---

## 相关文档

- [博客搭建文档](../BLOG_SETUP.md) - 如何搭建和迁移博客
- [写博客流程文档](../WRITE_BLOG.md) - 如何写新文章并发布
- [项目 README](../README.md) - 项目介绍

---

## 数据库导出

如需从数据库重新导出文章：

1. 编辑 `export_to_hugo.py` 中的数据库配置
2. 运行：`python export_to_hugo.py`
3. 文章会导出到 `content/posts/` 目录

---

## 注意事项

1. 不要手动修改 `public/` 目录，那是构建生成的
2. 文章中的 HTML 标签会自动处理，无需手动转换
3. 图片放在 `static/` 目录，引用时使用 `/images/` 路径
4. 使用 Hugo Extended 版本构建（已包含 `hugo.exe`）

---

## 联系方式

- GitHub: https://github.com/Galloping-Vijay/choudalao.github.io
- 博客: https://choudalao.github.io