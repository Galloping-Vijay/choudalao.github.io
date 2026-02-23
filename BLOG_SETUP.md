# Hugo 博客设置文档

## 目录
1. [从数据库导出文章](#从数据库导出文章)
2. [搭建 Hugo 博客](#搭建-hugo-博客)
3. [添加新文章](#添加新文章)
4. [本地预览](#本地预览)
5. [部署到 GitHub Pages](#部署到-github-pages)

---

## 从数据库导出文章

### 1. 准备导出脚本

导出脚本位于项目根目录：`export_to_hugo.py`

### 2. 修改数据库配置

编辑 `export_to_hugo.py` 文件，修改以下配置：

```python
# 数据库配置
DB_HOST = "你的数据库地址"
DB_PORT = 3306
DB_DATABASE = "数据库名"
DB_USER = "用户名"
DB_PASSWORD = "密码"
DB_PREFIX = "表前缀"  # 例如 "wjf_"
```

### 3. 运行导出脚本

```bash
python export_to_hugo.py
```

导出后的文章会保存到 `content/posts/` 目录。

---

## 搭建 Hugo 博客

### 方式一：已搭建（当前项目）

项目已搭建完成，位于：`D:\wwwroot\web\choudalao.github.io`

### 方式二：新建 Hugo 项目

#### 1. 安装 Hugo Extended

下载 Hugo Extended 版本（支持 SCSS/SASS）：
- Windows: https://github.com/gohugoio/hugo/releases
- 下载 `hugo_extended_x.x.x_windows-amd64.zip`
- 解压后得到 `hugo.exe`

#### 2. 初始化 Hugo 项目

```bash
hugo new site myblog
cd myblog
```

#### 3. 安装主题

```bash
# 使用 Mainroad 主题（推荐）
hugo mod init github.com/yourname/myblog
hugo mod get github.com/Vimux/mainroad
```

#### 4. 配置 hugo.toml

```toml
baseURL = 'https://yourname.github.io/'
languageCode = 'zh-CN'
title = '你的博客标题'
theme = 'github.com/Vimux/mainroad'

# 中文支持
hasCJKLanguage = true

# 分页
paginate = 10

# 忽略警告
ignoreLogs = ['warning-goldmark-raw-html']

# 参数配置
[params]
author = "你的名字"
description = "博客描述"
keywords = "关键词"

# 菜单
[[menu.main]]
identifier = "home"
name = "首页"
url = "/"
weight = 1

[[menu.main]]
identifier = "archives"
name = "归档"
url = "/post/"
weight = 2
```

---

## 添加新文章

### 方式一：使用 Hugo 命令创建

```bash
hugo new content/posts/新文章.md
```

生成的文件会包含 front matter 模板，编辑内容即可。

### 方式二：手动创建文章

1. 在 `content/posts/` 目录下创建 Markdown 文件
2. 文件名格式：`YYYY-MM-DD-文章标题.md`
3. 添加 front matter：

```yaml
---
title: "文章标题"
date: 2026-02-23T12:00:00+08:00
author: "作者名"
categories: ["分类"]
tags: ["标签1", "标签2"]
description: "文章摘要"
---

这里是文章内容...

## 二级标题

正文内容...
```

### 文章元数据说明

| 字段 | 说明 | 必填 |
|------|------|------|
| title | 文章标题 | ✅ |
| date | 发布日期 | ✅ |
| author | 作者 | ❌ |
| categories | 分类 | ❌ |
| tags | 标签（数组） | ❌ |
| description | 摘要 | ❌ |
| cover | 封面图片 URL | ❌ |

---

## 本地预览

### 启动预览服务器

```bash
hugo server
```

或者包含草稿：

```bash
hugo server -D
```

### 访问

打开浏览器访问：http://localhost:1313

预览时修改文件会自动刷新。

---

## 部署到 GitHub Pages

### 方式一：手动部署

```bash
# 构建静态网站
hugo

# 进入 public 目录
cd public

# 初始化 Git（如果还没有）
git init
git add .
git commit -m "部署博客"
git branch -M main
git remote add origin https://github.com/yourname/yourname.github.io.git
git push -u origin main
```

### 方式二：自动部署（推荐）

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          submodules: recursive
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.156.0'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

---

## 常用命令

```bash
# 构建网站
hugo

# 构建并最小化
hugo --minify

# 启动预览服务器
hugo server

# 预览并包含草稿
hugo server -D

# 查看版本
hugo version

# 创建新文章
hugo new content/posts/文章名.md
```

---

## 常见问题

### 1. 构建时出现 "Raw HTML omitted" 警告

在 `hugo.toml` 中添加：

```toml
ignoreLogs = ['warning-goldmark-raw-html']
```

### 2. 中文显示不正常

确保配置中添加：

```toml
hasCJKLanguage = true
```

### 3. 主题样式不显示

确认使用 Hugo Extended 版本（支持 SCSS/SASS），检查版本信息中是否包含 `extended`。

---

## 项目目录结构

```
choudalao.github.io/
├── content/
│   └── posts/           # 文章目录
│       ├── 2026-02-23-文章1.md
│       └── 2026-02-23-文章2.md
├── public/             # 生成的静态网站
├── static/             # 静态资源
├── themes/             # 主题缓存
├── hugo.exe            # Hugo 可执行文件
├── hugo.toml           # 配置文件
└── export_to_hugo.py   # 数据库导出脚本
```

---

## 更新日志

- 2026-02-23: 创建文档，记录博客搭建流程