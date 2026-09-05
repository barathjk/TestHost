"""Flask blog app. Posts are Markdown files in /posts with YAML frontmatter."""
from datetime import datetime, date
from pathlib import Path

import frontmatter
import markdown as md
from flask import Flask, abort, render_template

BASE_DIR = Path(__file__).resolve().parent
POSTS_DIR = BASE_DIR / "posts"

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

MD_EXTENSIONS = ["fenced_code", "tables", "codehilite", "toc"]


def _parse_date(value):
    if isinstance(value, (datetime, date)):
        return value
    if isinstance(value, str):
        for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"):
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                continue
    return date.today()


def _load_post(path: Path):
    post = frontmatter.load(path)
    slug = path.stem
    meta = post.metadata
    html = md.markdown(post.content, extensions=MD_EXTENSIONS)
    return {
        "slug": slug,
        "title": meta.get("title", slug.replace("-", " ").title()),
        "date": _parse_date(meta.get("date")),
        "author": meta.get("author", "Anonymous"),
        "summary": meta.get("summary", ""),
        "tags": meta.get("tags", []),
        "html": html,
    }


def load_all_posts():
    if not POSTS_DIR.exists():
        return []
    posts = [_load_post(p) for p in POSTS_DIR.glob("*.md")]
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def load_post(slug: str):
    path = POSTS_DIR / f"{slug}.md"
    if not path.exists():
        return None
    return _load_post(path)


@app.route("/")
def index():
    return render_template("index.html", posts=load_all_posts())


@app.route("/post/<slug>")
def post_detail(slug):
    post = load_post(slug)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
