# Flask Blog (Vercel test app)

A minimal Flask blog meant for testing on Vercel. Content lives as Markdown
files in `posts/` — no database required.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python main.py
```

Visit http://localhost:5000

## Deploy to Vercel

```bash
npm i -g vercel   # if you don't have the CLI
vercel
```

Or push this folder to a Git repo and import it in the Vercel dashboard —
`vercel.json` already tells Vercel to run it as a Python (`@vercel/python`)
serverless function.

## Add a post

Create `posts/my-post.md`:

```markdown
---
title: My Post
date: 2026-09-05
author: Your Name
summary: One-line summary shown on the index page.
tags: [example]
---

Your Markdown content here.
```

The filename becomes the URL: `posts/my-post.md` → `/post/my-post`.

## Project layout

```
blog.py           Flask app + post loading/rendering
api/index.py      Vercel entrypoint (imports app from blog.py)
main.py           Local dev entrypoint
templates/        Jinja2 templates
static/style.css  Styling (light/dark aware)
posts/*.md        Blog content
vercel.json       Vercel build/route config
```
