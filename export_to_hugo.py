"""
从 Laravel 数据库导出文章数据到 Hugo 格式
"""

import mysql.connector
from datetime import datetime
import os
import re

# 数据库配置（从 .env 读取）
DB_HOST = "39.107.248.179"
DB_PORT = 3306
DB_DATABASE = "choudalao"
DB_USER = "choudalao"
DB_PASSWORD = "xzdWdkcPEcSwXwX3"
DB_PREFIX = "wjf_"

# 导出目录（直接导出到 Hugo 的 content/posts）
EXPORT_DIR = os.path.abspath("content/posts")
# Windows 路径最大长度
MAX_PATH_LENGTH = 200


def escape_yaml_string(text):
    """转义 YAML 字符串中的特殊字符"""
    if not text:
        return ""
    text = text.replace('\\', '\\\\')
    text = text.replace('"', '\\"')
    return text


def slugify(text):
    """生成 URL 友好的 slug"""
    text = str(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def truncate_slug(slug, max_length=80):
    """截断过长的 slug"""
    if len(slug) > max_length:
        return slug[:max_length].rstrip('-')
    return slug


def connect_db():
    """连接数据库"""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            charset='utf8mb4'
        )
        return conn
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return None


def export_articles():
    """导出文章到 Hugo 格式"""
    conn = connect_db()
    if not conn:
        return False

    cursor = conn.cursor(dictionary=True)

    # 创建导出目录
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    # 查询所有已发布的文章
    query = f"""
    SELECT
        a.id,
        a.title,
        a.author,
        a.content,
        a.markdown,
        a.description,
        a.keywords,
        a.cover,
        a.is_top,
        a.click,
        a.created_at,
        a.updated_at,
        c.name as category_name,
        GROUP_CONCAT(DISTINCT t.name) as tags
    FROM {DB_PREFIX}articles a
    LEFT JOIN {DB_PREFIX}categories c ON a.category_id = c.id
    LEFT JOIN {DB_PREFIX}article_tags at ON a.id = at.article_id
    LEFT JOIN {DB_PREFIX}tags t ON at.tag_id = t.id
    WHERE a.status = 1 AND a.deleted_at IS NULL
    GROUP BY a.id
    ORDER BY a.created_at DESC
    """

    cursor.execute(query)
    articles = cursor.fetchall()

    print(f"找到 {len(articles)} 篇文章")

    for article in articles:
        # 使用 markdown 内容，如果没有则使用 content
        content = article['markdown'] if article['markdown'] else article['content']

        # 构建 Hugo front matter
        front_matter = f"""---
title: "{escape_yaml_string(article['title'])}"
date: {article['created_at'].strftime('%Y-%m-%dT%H:%M:%S+08:00') if article['created_at'] else datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')}
updated: {article['updated_at'].strftime('%Y-%m-%dT%H:%M:%S+08:00') if article['updated_at'] else datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')}
author: "{escape_yaml_string(article['author'] or '臭大佬')}"
"""

        # 分类
        if article['category_name']:
            front_matter += f"categories: [{article['category_name']}]\n"

        # 标签
        if article['tags']:
            tags = article['tags'].split(',')
            tags_str = ', '.join([f'"{t.strip()}"' for t in tags])
            front_matter += f"tags: [{tags_str}]\n"

        # 摘要
        if article['description']:
            front_matter += f'description: "{escape_yaml_string(article["description"])}"\n'

        # 封面图
        if article['cover']:
            front_matter += f'cover: "{escape_yaml_string(article["cover"])}"\n'

        # 是否置顶
        if article['is_top']:
            front_matter += "weight: 100\n"

        # 点击数（作为自定义字段）
        front_matter += f"click: {article['click']}\n"

        front_matter += "---\n\n"

        # 完整文章内容
        full_content = front_matter + (content or '')

        # 生成文件名（处理路径长度限制）
        date_str = article['created_at'].strftime('%Y-%m-%d') if article['created_at'] else '0000-00-00'
        slug = truncate_slug(slugify(article['title']))
        fallback_slug = f'article-{article["id"]}'
        filename = f"{date_str}-{slug or fallback_slug}.md"

        # 确保完整路径不超过 Windows 限制
        filepath = os.path.join(EXPORT_DIR, filename)
        if len(filepath) > MAX_PATH_LENGTH:
            # 如果路径太长，使用更短的文件名
            base_name = f"{date_str}-article-{article['id']}"
            filename = base_name + '.md'
            filepath = os.path.join(EXPORT_DIR, filename)

        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"[OK] {filename}")

    cursor.close()
    conn.close()

    print(f"\n成功导出 {len(articles)} 篇文章到 {EXPORT_DIR}")
    return True


if __name__ == "__main__":
    print("开始导出文章...")
    export_articles()