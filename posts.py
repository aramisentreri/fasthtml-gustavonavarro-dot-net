from datetime import date
from pathlib import Path

import markdown

POSTS_DIR = Path(__file__).parent / "posts"


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    meta: dict = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, body


def _coerce_date(value) -> date:
    if isinstance(value, date):
        return value
    if not value:
        return date.min
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        return date.min


def _load_one(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    meta, body = _parse_frontmatter(raw)
    slug = meta.get("slug") or path.stem
    return {
        "slug": slug,
        "title": meta.get("title", slug.replace("-", " ").title()),
        "date": _coerce_date(meta.get("date")),
        "summary": meta.get("summary", ""),
        "body": body,
    }


def list_posts() -> list[dict]:
    if not POSTS_DIR.exists():
        return []
    posts = [_load_one(p) for p in POSTS_DIR.glob("*.md")]
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def get_post(slug: str) -> dict | None:
    path = POSTS_DIR / f"{slug}.md"
    if not path.exists():
        return None
    post = _load_one(path)
    post["html"] = markdown.markdown(
        post["body"],
        extensions=["fenced_code", "tables", "smarty"],
    )
    return post


def format_post_date(d: date) -> str:
    if d == date.min:
        return ""
    return f"{d.strftime('%B')} {d.day}, {d.year}"
