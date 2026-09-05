---
title: Welcome to the Blog
date: 2026-09-01
author: Barath
summary: How this blog works and how to add your own posts.
tags: [meta, guide]
---

This is a **test Flask blog** built to run on Vercel. Every post is just a
Markdown file dropped into the `posts/` folder — no database, no CMS.

## Adding a new post

1. Create a file at `posts/your-slug.md`.
2. Add frontmatter at the top (`title`, `date`, `author`, `summary`, `tags`).
3. Write the rest of the file in Markdown.
4. Push to your Git repo — Vercel redeploys automatically.

The filename (minus `.md`) becomes the post's URL slug, e.g. this file is
served at `/post/welcome-to-the-blog`.

## What's supported

- **Bold**, *italic*, `inline code`
- Fenced code blocks with syntax highlighting
- Tables, blockquotes, lists
- Images (drop them in `static/` and reference with a normal `![alt](url)`)

```python
def hello():
    return "Hello, blog!"
```

> Swap this content for anything you like — it's just a starting point.
