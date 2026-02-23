# 如何写一篇博客并发布到 GitHub Pages

## 完整流程概览

```
写文章 → 本地预览 → 构建网站 → 提交到 Git → 自动部署
```

---

## 第一步：写文章

### 方式一：使用 Hugo 命令创建文章模板

在项目目录（`D:\wwwroot\web\choudalao.github.io`）运行：

```bash
./hugo.exe new content/posts/你的文章标题.md
```

生成的文件会包含基本的 front matter 模板：

```yaml
---
title: "你的文章标题"
date: 2026-02-23T12:00:00+08:00
draft: true
---
```

### 方式二：手动创建文章

1. 进入 `content/posts/` 目录
2. 创建新文件，命名格式：`YYYY-MM-DD-文章标题.md`
3. 添加 front matter 和内容

示例：

```markdown
---
title: "Hugo 博客搭建教程"
date: 2026-02-23T12:00:00+08:00
author: "臭大佬"
categories: ["技术"]
tags: ["Hugo", "博客"]
description: "从零开始搭建 Hugo 博客的详细教程"
draft: true
---

# Hugo 博客搭建教程

这是一篇关于如何搭建 Hugo 博客的文章...

## 环境准备

首先需要安装 Hugo...

## 开始搭建

### 1. 创建新站点

```bash
hugo new site myblog
```

### 2. 添加主题

...
```

### Front Matter 字段说明

| 字段 | 说明 | 示例 | 必填 |
|------|------|------|------|
| title | 文章标题 | `"Hugo 教程"` | ✅ |
| date | 发布日期 | `2026-02-23T12:00:00+08:00` | ✅ |
| draft | 是否为草稿 | `true`/`false` | ❌ |
| author | 作者 | `"臭大佬"` | ❌ |
| categories | 分类（单选） | `["技术"]` | ❌ |
| tags | 标签（多选） | `["Hugo", "博客"]` | ❌ |
| description | 文章摘要 | `"这是文章的简介..."` | ❌ |
| cover | 封面图片 URL | `"https://..."` | ❌ |
| weight | 文章权重（用于排序） | `100` | ❌ |

---

## 第二步：本地预览

### 启动预览服务器

```bash
./hugo.exe server
```

预览服务器默认运行在：http://localhost:1313

### 常用预览选项

```bash
# 包含草稿文章
./hugo.exe server -D

# 指定端口
./hugo.exe server --port 8080

# 绑定到所有网络接口（局域网访问）
./hugo.exe server --bind 0.0.0.0
```

### 实时编辑

预览服务器启动后，修改文章内容会自动刷新浏览器，无需重启服务器。

---

## 第三步：发布文章

### 方法一：将文章设为已发布

编辑文章，将 `draft: true` 改为 `draft: false`，或者直接删除 `draft` 字段。

```markdown
---
title: "Hugo 博客搭建教程"
date: 2026-02-23T12:00:00+08:00
# draft: true  ← 删除或改为 false
---
```

### 方法二：使用 -D 参数构建

发布时使用 `-D` 参数构建，会包含所有草稿：

```bash
./hugo.exe -D
```

---

## 第四步：构建网站

### 构建静态网站

```bash
./hugo.exe
```

构建完成后，生成的静态文件在 `public/` 目录。

### 构建并最小化（推荐生产环境）

```bash
./hugo.exe --minify
```

---

## 第五步：提交到 Git

### 1. 查看修改状态

```bash
git status
```

### 2. 添加文件

```bash
# 添加所有修改
git add .

# 或只添加特定文件
git add content/posts/新文章.md
```

### 3. 提交

```bash
git commit -m "新增文章：Hugo 博客搭建教程"
```

### 4. 推送到 GitHub

```bash
git push
```

---

## 自动部署（推荐）

### 配置 GitHub Actions

项目已配置自动部署，提交代码后会自动部署到 GitHub Pages。

**触发条件：**
- 推送到 `main` 分支

**部署位置：**
- https://choudalao.github.io

**部署时间：**
- 通常 1-3 分钟

**查看部署状态：**
1. 访问 GitHub 仓库
2. 点击 "Actions" 标签
3. 查看最新工作流运行状态

---

## 完整示例

### 示例：发布一篇关于 Python 的文章

#### 1. 创建文章

```bash
cd D:\wwwroot\web\choudalao.github.io
./hugo.exe new content/posts/python-list-sort.md
```

#### 2. 编辑文章

编辑 `content/posts/python-list-sort.md`：

```markdown
---
title: "Python 列表排序方法总结"
date: 2026-02-23T12:00:00+08:00
author: "臭大佬"
categories: ["Python"]
tags: ["基础", "排序"]
description: "Python 中常用的列表排序方法，包括 sort() 和 sorted()"
---

# Python 列表排序方法总结

## sort() 方法

sort() 方法用于对原列表进行排序：

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5]
```

## sorted() 函数

sorted() 函数返回一个新的排序列表：

```python
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 3, 4, 5]
```

...
```

#### 3. 本地预览

```bash
./hugo.exe server
```

浏览器打开 http://localhost:1313 查看效果。

#### 4. 发布到 GitHub

```bash
git add content/posts/python-list-sort.md
git commit -m "新增文章：Python 列表排序方法总结"
git push
```

等待 GitHub Actions 自动部署完成，访问 https://choudalao.github.io 查看新文章。

---

## 常用 Markdown 语法

### 标题

```markdown
# 一级标题
## 二级标题
### 三级标题
```

### 列表

```markdown
- 无序列表项1
- 无序列表项2

1. 有序列表项1
2. 有序列表项2
```

### 代码块

```markdown
`行内代码`

```python
def hello():
    print("Hello, World!")
```
```

### 链接和图片

```markdown
[链接文字](https://example.com)

![图片描述](https://example.com/image.png)
```

### 表格

```markdown
| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 数据1 | 数据2 | 数据3 |
```

---

## 快速命令参考

| 操作 | 命令 |
|------|------|
| 创建新文章 | `./hugo.exe new content/posts/标题.md` |
| 本地预览 | `./hugo.exe server` |
| 构建网站 | `./hugo.exe` |
| 查看状态 | `git status` |
| 添加文件 | `git add .` |
| 提交 | `git commit -m "说明"` |
| 推送 | `git push` |

---

## 注意事项

1. **文件命名**：使用英文和数字，避免中文和特殊字符
2. **日期格式**：使用 ISO 8601 格式 `YYYY-MM-DDTHH:mm:ss+08:00`
3. **草稿状态**：新文章默认是草稿，记得修改 `draft` 字段
4. **图片路径**：图片放在 `static/images/` 目录，引用时使用 `/images/文件名.png`
5. **分类和标签**：分类建议只选一个，标签可以选多个

---

## 故障排查

### 文章没有显示

1. 检查 `draft` 字段是否为 `false` 或已删除
2. 检查日期是否为未来日期
3. 查看构建日志：`./hugo.exe --logLevel info`

### 图片无法显示

1. 确认图片在 `static/` 目录下
2. 检查图片路径是否正确（以 `/` 开头）
3. 确认文件名大小写正确

### 部署失败

1. 检查 GitHub Actions 运行日志
2. 确认配置文件格式正确
3. 检查文章的 Markdown 语法是否有错误

---

## 联系方式

如有问题，请参考项目文档或提交 Issue。