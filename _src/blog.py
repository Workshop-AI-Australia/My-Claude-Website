"""Blog for workshopai.com.au: post pages, the /blog/ index, the RSS feed and the
blog entries in sitemap.xml.

Source of truth: one markdown file per post in _src/blog/<slug>.md. Images live
beside the published page in blog/<slug>/. Everything else is regenerated from
those two places on every run, so output is deterministic and re-running is safe.

Add a post with scripts/add-post (see docs/blog.md). `python3 _src/build.py`
also rebuilds the blog, so a normal site build never drops blog pages.
Standard library only, like the rest of _src/.
"""
import datetime as dt
import html
import json
import os
import re
import shutil
import struct
from email.utils import format_datetime

import build
from data import SITE

BLOG_PATH = "/blog/"
FEED_PATH = "/blog/feed.xml"
BLOG_TITLE = "Workshop AI blog"
BLOG_DESCRIPTION = ("Articles from Workshop AI on putting AI to work in Australian trade, "
                    "service and industrial businesses.")
BLOG_STARTED = "2026-11-13"   # sitemap lastmod for the index until the first post
SRC_DIR = os.path.join("_src", "blog")
OUT_DIR = "blog"

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
IMAGE_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*\.(png|jpe?g|gif|webp)$", re.I)
SLOT_RE = re.compile(r"^<!--\s*slot:(.*?)-->$")
SLOT_ATTR_RE = re.compile(r'([a-z_]+)=(?:"([^"]*)"|(\S+))')
SAFE_URL_RE = re.compile(r"^(https?://|mailto:|tel:|/|#)", re.I)
SCHEME_RE = re.compile(r"^[a-z][a-z0-9+.-]*:", re.I)
SLOT_EXTS = (".png", ".jpg", ".jpeg")


class BlogError(Exception):
    """A post that can't be published as written. Nothing is written when raised."""


# ---------------------------------------------------------------- frontmatter
def parse_frontmatter(text):
    """Split `---` YAML-style frontmatter (flat `key: value` pairs) from the body."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        raise BlogError("frontmatter starts with --- but never closes")
    meta = {}
    for line in text[4:end].split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise BlogError(f"frontmatter line is not key: value: {line!r}")
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[key.strip()] = value
    body = text[end + 4:]
    return meta, body.lstrip("\n")


def truthy(value):
    return str(value).strip().lower() in ("yes", "true", "1")


# ---------------------------------------------------------------- images
def image_size(path):
    """(width, height) for PNG, GIF and JPEG files, or None."""
    with open(path, "rb") as f:
        data = f.read(65536)
    if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR":
        return struct.unpack(">II", data[16:24])
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return struct.unpack("<HH", data[6:10])
    if data[:2] == b"\xff\xd8":
        with open(path, "rb") as f:
            data = f.read()
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7 or marker == 0xFF:
                i += 1 if marker == 0xFF else 2
                continue
            length = struct.unpack(">H", data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None


class Images:
    """Finds the image files a post refers to and remembers which ones it used."""

    def __init__(self, search_dirs):
        self.search_dirs = [d for d in search_dirs if d]
        self.used = {}      # published file name -> absolute source path, in order of use
        self.hero = None    # (name, alt)

    def _take(self, name, path):
        if name in self.used and os.path.realpath(self.used[name]) != os.path.realpath(path):
            raise BlogError(f"two different images are both called {name}")
        self.used[name] = path
        return name

    def slot(self, slot_id):
        for d in self.search_dirs:
            for ext in SLOT_EXTS:
                path = os.path.join(d, slot_id + ext)
                if os.path.isfile(path):
                    return self._take(slot_id + ext, path)
        raise BlogError(f"no image file for slot {slot_id} (looked for {slot_id}.png or .jpg "
                        f"in {', '.join(self.search_dirs)})")

    def file(self, ref):
        if SCHEME_RE.match(ref) or ref.startswith("//"):
            raise BlogError(f"images must be local files, not {ref}")
        name = os.path.basename(ref)
        if not IMAGE_NAME_RE.match(name):
            raise BlogError(f"unsupported image file name: {ref} (png, jpg, gif or webp)")
        for d in self.search_dirs:
            for candidate in (os.path.join(d, ref), os.path.join(d, name)):
                if os.path.isfile(candidate):
                    return self._take(name, candidate)
        raise BlogError(f"image not found: {ref}")


def img_tag(name, alt, path, extra=""):
    e = html.escape
    size = image_size(path)
    dims = f' width="{size[0]}" height="{size[1]}"' if size else ""
    return f'<img src="{e(name)}" alt="{e(alt)}"{dims}{extra} />'


def require_alt(alt, what):
    if not alt or not alt.strip():
        raise BlogError(f"{what} has no alt text; every image needs it")
    return alt.strip()


# ---------------------------------------------------------------- markdown (a small, safe subset)
INLINE_RE = re.compile(
    r"`([^`]+)`"                                     # 1 code
    r"|!\[([^\]]*)\]\(([^)\s]+)\)"                   # 2,3 image
    r"|\[([^\]]+)\]\(([^)\s]+)\)"                    # 4,5 link
    r"|\*\*(.+?)\*\*"                                # 6 bold
    r"|(?<![\w*])\*(?![\s*])(.+?)(?<![\s*])\*(?![\w*])"   # 7 em
    r"|(?<![\w])_(?![\s_])(.+?)(?<![\s_])_(?![\w])")      # 8 em


def safe_url(url):
    if SAFE_URL_RE.match(url) or not SCHEME_RE.match(url):
        return url
    raise BlogError(f"link scheme not allowed: {url}")


def inline(text, images):
    e = html.escape
    out, pos = [], 0
    for m in INLINE_RE.finditer(text):
        out.append(e(text[pos:m.start()]))
        pos = m.end()
        if m.group(1) is not None:
            out.append(f"<code>{e(m.group(1))}</code>")
        elif m.group(3) is not None:
            alt = require_alt(m.group(2), f"image {m.group(3)}")
            name = images.file(m.group(3))
            out.append(img_tag(name, alt, images.used[name], LAZY))
        elif m.group(5) is not None:
            url = safe_url(m.group(5))
            rel = ' rel="noopener"' if url.lower().startswith(("http://", "https://")) else ""
            out.append(f'<a href="{e(url)}"{rel}>{inline(m.group(4), images)}</a>')
        elif m.group(6) is not None:
            out.append(f"<strong>{inline(m.group(6), images)}</strong>")
        else:
            out.append(f"<em>{inline(m.group(7) or m.group(8), images)}</em>")
    out.append(e(text[pos:]))
    return "".join(out)


def parse_slot(line):
    m = SLOT_RE.match(line.strip())
    if not m:
        return None
    attrs = {a.group(1): a.group(2) if a.group(2) is not None else a.group(3)
             for a in SLOT_ATTR_RE.finditer(m.group(1))}
    if not attrs.get("id"):
        raise BlogError(f"image slot without an id: {line.strip()}")
    return attrs


LAZY = ' loading="lazy"'


def figure(name, alt, images):
    return f"<figure>\n  {img_tag(name, alt, images.used[name], LAZY)}\n</figure>"


def markdown(body, images, title=""):
    """Render the post body. Raw HTML is escaped, never passed through; HTML comments
    are dropped except image slots, which become images. The first hero slot (or a
    standalone image before any text) becomes the post's hero image."""
    lines = body.split("\n")
    blocks, para = [], []
    i, seen_text = 0, False

    def flush():
        nonlocal seen_text
        if para:
            blocks.append(f"<p>{inline(' '.join(s.strip() for s in para), images)}</p>")
            para.clear()
            seen_text = True

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush()
            i += 1
            continue
        if s.startswith("```"):
            flush()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            blocks.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
            i += 1
            continue
        slot = parse_slot(s)
        if slot:
            flush()
            alt = require_alt(slot.get("alt"), f"image slot {slot['id']}")
            name = images.slot(slot["id"])
            if slot.get("type") == "hero" and images.hero is None:
                images.hero = (name, alt)
            else:
                blocks.append(figure(name, alt, images))
            i += 1
            continue
        if s.startswith("<!--"):
            flush()
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*$", s)
        if m:
            flush()
            text = m.group(2)
            if len(m.group(1)) == 1 and not seen_text and text.strip() == title.strip():
                i += 1      # the title is already the page's h1
                continue
            level = max(2, len(m.group(1)))
            blocks.append(f"<h{level}>{inline(text, images)}</h{level}>")
            seen_text = True
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            flush()
            blocks.append("<hr />")
            i += 1
            continue
        m = re.match(r"^!\[([^\]]*)\]\(([^)\s]+)\)$", s)
        if m and not para:
            alt = require_alt(m.group(1), f"image {m.group(2)}")
            name = images.file(m.group(2))
            if images.hero is None and not seen_text and not blocks:
                images.hero = (name, alt)
            else:
                blocks.append(figure(name, alt, images))
            i += 1
            continue
        if s.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append(f"<blockquote>\n{markdown(chr(10).join(quote), images)}\n</blockquote>")
            seen_text = True
            continue
        lm = re.match(r"^([-*+]|\d+[.)])\s+(.*)$", s)
        if lm:
            flush()
            ordered = lm.group(1)[0].isdigit()
            items = []
            while i < len(lines):
                cur = lines[i]
                im = re.match(r"^\s*([-*+]|\d+[.)])\s+(.*)$", cur)
                if im and im.group(1)[0].isdigit() == ordered:
                    items.append([im.group(2)])
                elif cur.strip() and cur.startswith((" ", "\t")) and items:
                    items[-1].append(cur.strip())
                else:
                    break
                i += 1
            tag = "ol" if ordered else "ul"
            lis = "\n".join(f"  <li>{inline(' '.join(it), images)}</li>" for it in items)
            blocks.append(f"<{tag}>\n{lis}\n</{tag}>")
            seen_text = True
            continue
        para.append(line)
        i += 1
    flush()
    return "\n".join(blocks)


def first_paragraph_text(body_html):
    m = re.search(r"<p>(.*?)</p>", body_html, re.S)
    return build.plain(m.group(1)) if m else ""


def shorten(text, limit=160):
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(",;:.")
    return cut + "..."


# ---------------------------------------------------------------- reading a post
def human_date(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B')} {d.year}"


def read_post(md_path, search_dirs, slug=None, date=None):
    """Parse and render one post. Raises BlogError if it can't be published."""
    with open(md_path, encoding="utf-8") as f:
        raw = f.read()
    meta, body = parse_frontmatter(raw)

    if truthy(meta.get("client_named", "no")) and not truthy(meta.get("client_permission", "")):
        raise BlogError("this post names a client without permission (client_named: yes, "
                        "client_permission is not yes); it can't be published")
    if meta.get("status") and meta["status"] not in ("pack-ready", "published") and not truthy(meta.get("sample")):
        raise BlogError(f"status is {meta['status']}; only pack-ready posts can be added")

    title = meta.get("title", "").strip()
    if not title:
        m = re.search(r"^#\s+(.+?)\s*$", body, re.M)
        title = m.group(1).strip() if m else ""
    if not title:
        raise BlogError("no title (add title: to the frontmatter or a # heading)")

    slug = slug or meta.get("slug", "").strip() or slug_from_path(md_path)
    if not slug or not SLUG_RE.match(slug):
        raise BlogError(f"slug must be lower-case words joined by hyphens, got {slug!r}")

    date = date or meta.get("publish_date", "").strip() or meta.get("date", "").strip()
    if not DATE_RE.match(date or ""):
        raise BlogError(f"publish_date (or date) must be yyyy-mm-dd, got {date!r}")
    dt.date.fromisoformat(date)
    updated = meta.get("updated", "").strip() or date
    if not DATE_RE.match(updated):
        raise BlogError(f"updated must be yyyy-mm-dd, got {updated!r}")

    images = Images(search_dirs)
    body_html = markdown(body, images, title)
    if images.hero is None:
        raise BlogError("no hero image (add an image slot with type=hero)")
    description = (meta.get("description") or meta.get("summary") or "").strip()
    description = description or shorten(first_paragraph_text(body_html))
    return {
        "title": title, "slug": slug, "date": date, "updated": updated,
        "description": description, "sample": truthy(meta.get("sample")),
        "body_html": body_html, "hero": images.hero, "images": dict(images.used),
        "raw": raw.replace("\r\n", "\n").replace("\r", "\n"),
    }


def slug_from_path(md_path):
    """articles/<yyyy-mm-dd>-<slug>/pack/blog.md gives <slug>."""
    parent = os.path.dirname(os.path.abspath(md_path))
    if os.path.basename(parent) == "pack":
        folder = os.path.basename(os.path.dirname(parent))
        return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", folder)
    return ""


# ---------------------------------------------------------------- page parts
BLOG_CSS = """
  .page-hero .eyebrow a{color:inherit;text-decoration:none}
  .post-page .page-hero h1{text-transform:none;max-width:26ch}
  .post{padding:40px 0 56px}
  .post-hero{margin:0 0 32px}
  .post-hero img,.post-body figure img{display:block;width:100%;height:auto;border-radius:10px;border:1px solid var(--line-soft)}
  .post-body{max-width:68ch}
  .post-body h2{font-size:clamp(22px,2.8vw,28px);text-transform:none;margin:36px 0 14px}
  .post-body h3,.post-body h4{margin:26px 0 10px}
  .post-body a{color:var(--amber-deep)}
  .post-body figure{margin:28px 0}
  .post-body figcaption{font-size:14px;color:var(--ink-faint);margin-top:8px}
  .post-body blockquote{border-left:4px solid var(--amber);padding:4px 0 4px 18px;margin:20px 0;color:var(--ink-soft)}
  .post-body pre{background:var(--paper-2);border-radius:6px;padding:14px 16px;overflow-x:auto;font-size:14px;margin:0 0 14px}
  .post-body code{font-family:"JetBrains Mono",monospace;font-size:0.9em}
  .post-body hr{border:none;border-top:1px solid var(--line);margin:32px 0}
  .back{margin-top:40px;font-family:"JetBrains Mono",monospace;font-size:13px;letter-spacing:0.04em}
  .back a{color:var(--ink-soft)}
  .sample-banner{background:var(--amber-soft);color:var(--navy);font-weight:700;font-size:15px;padding:12px 0;text-align:center}
  .post-list{list-style:none;margin:0;max-width:none}
  .post-list li{padding:26px 0;border-top:1px solid var(--line-soft);margin:0}
  .post-list li:first-child{border-top:none}
  .post-list time{font-family:"JetBrains Mono",monospace;font-size:12px;letter-spacing:0.06em;color:var(--ink-faint)}
  .post-list h2{font-size:clamp(21px,2.6vw,26px);text-transform:none;margin:6px 0 8px;max-width:none}
  .post-list h2 a{text-decoration:none}
  .post-list h2 a:hover{color:var(--amber-deep)}
  .post-list p{color:var(--ink-soft)}
"""

FEED_LINK = (f'<link rel="alternate" type="application/rss+xml" title="{BLOG_TITLE}" '
             f'href="{FEED_PATH}" />')


def page_head(title, description, path, jsonld, og_type="website", image=None, image_alt="",
              published=None, modified=None, noindex=False):
    """Like build.head(), with article, image, Twitter and feed tags for the blog."""
    e = html.escape
    url = f"{SITE}{path}"
    img = image or build.OG_IMAGE
    alt = image_alt or "Workshop AI"
    extra = []
    if noindex:
        extra.append('<meta name="robots" content="noindex, nofollow" />')
    if published:
        extra.append(f'<meta property="article:published_time" content="{published}" />')
        extra.append(f'<meta property="article:modified_time" content="{modified or published}" />')
        extra.append('<meta property="article:author" content="Justin Watts" />')
    extra_s = ("\n".join(extra) + "\n") if extra else ""
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{e(title)}</title>
<meta name="description" content="{e(description)}" />
{extra_s}<link rel="canonical" href="{url}" />
<link rel="icon" type="image/png" href="/favicon.png" />
{FEED_LINK}
<meta property="og:type" content="{og_type}" />
<meta property="og:site_name" content="Workshop AI" />
<meta property="og:locale" content="en_AU" />
<meta property="og:title" content="{e(title)}" />
<meta property="og:description" content="{e(description)}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{e(img)}" />
<meta property="og:image:alt" content="{e(alt)}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{e(title)}" />
<meta name="twitter:description" content="{e(description)}" />
<meta name="twitter:image" content="{e(img)}" />
<meta name="twitter:image:alt" content="{e(alt)}" />
<meta name="author" content="Justin Watts, Workshop AI" />
{build.GA_SNIPPET}
{build.FONTS}
<style>{build.CSS}{BLOG_CSS}</style>
<script type="application/ld+json">
{jsonld}
</script>
</head>
"""


def post_url(slug):
    return f"{SITE}{BLOG_PATH}{slug}/"


def render_post(post):
    e = html.escape
    path = f"{BLOG_PATH}{post['slug']}/"
    url = post_url(post["slug"])
    hero_name, hero_alt = post["hero"]
    hero_abs = f"{url}{hero_name}"
    hero_size = image_size(post["images"][hero_name])
    image_node = {"@type": "ImageObject", "url": hero_abs, "caption": hero_alt}
    if hero_size:
        image_node.update({"width": hero_size[0], "height": hero_size[1]})
    nodes = [
        {"@type": "Article", "@id": f"{url}#article", "headline": post["title"],
         "description": post["description"], "url": url, "mainEntityOfPage": url,
         "image": image_node, "datePublished": post["date"], "dateModified": post["updated"],
         "author": {"@id": build.PERSON_ID}, "publisher": {"@id": build.ORG_ID},
         "isPartOf": {"@id": f"{SITE}{BLOG_PATH}#blog"}, "inLanguage": "en-AU"},
        {"@type": "BreadcrumbList", "@id": f"{url}#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}{BLOG_PATH}"},
            {"@type": "ListItem", "position": 3, "name": post["title"], "item": url}]},
    ]
    banner = ""
    if post["sample"]:
        banner = ('<div class="sample-banner" role="note">Sample post: placeholder text that shows the '
                  'layout. It is not listed on the blog, in the feed or in the sitemap.</div>\n')
    hero_img = img_tag(hero_name, hero_alt, post["images"][hero_name], ' fetchpriority="high"')
    body = f"""<body class="post-page">
{build.nav(BLOG_PATH)}{banner}<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="{BLOG_PATH}">Blog</a></p>
    <h1>{e(post['title'])}</h1>
    <p class="lede">{e(post['description'])}</p>
    <p class="byline">Written by Justin Watts, Director of <a href="/facts/">Workshop AI</a>, Hobsons Bay, Melbourne &middot; <time datetime="{post['date']}">{human_date(post['date'])}</time></p>
  </div>
</header>

<main class="wrap post">
<figure class="post-hero">
  {hero_img}
</figure>
<article class="post-body">
{post['body_html']}
</article>
<p class="back"><a href="{BLOG_PATH}">&larr; All posts</a></p>
</main>
"""
    head = page_head(f"{post['title']} | Workshop AI", post["description"], path, build.graph(nodes),
                     og_type="article", image=hero_abs, image_alt=hero_alt, published=post["date"],
                     modified=post["updated"], noindex=post["sample"])
    return head + body + build.FOOTER + build.END


def listed(posts):
    """Posts shown on the index, feed and sitemap: not samples, newest first, then by slug."""
    real = [p for p in posts if not p["sample"]]
    return sorted(sorted(real, key=lambda p: p["slug"]), key=lambda p: p["date"], reverse=True)


def render_index(posts):
    e = html.escape
    items = "\n".join(
        f"""<li><article>
  <time datetime="{p['date']}">{human_date(p['date'])}</time>
  <h2><a href="{BLOG_PATH}{p['slug']}/">{e(p['title'])}</a></h2>
  <p>{e(p['description'])}</p>
</article></li>""" for p in posts)
    listing = (f'<ul class="post-list">\n{items}\n</ul>' if posts
               else "<p>No posts yet.</p>")
    url = f"{SITE}{BLOG_PATH}"
    nodes = [{"@type": "Blog", "@id": f"{url}#blog", "url": url, "name": BLOG_TITLE,
              "description": BLOG_DESCRIPTION, "publisher": {"@id": build.ORG_ID},
              "isPartOf": {"@id": build.WEBSITE_ID}, "inLanguage": "en-AU",
              "blogPost": [{"@type": "Article", "@id": f"{post_url(p['slug'])}#article",
                            "headline": p["title"], "url": post_url(p["slug"]),
                            "datePublished": p["date"]} for p in posts]}]
    body = f"""<body>
{build.nav(BLOG_PATH)}<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Workshop AI &middot; Blog</p>
    <h1>Blog</h1>
    <p class="lede">{e(BLOG_DESCRIPTION)}</p>
    <p class="byline">Newest first &middot; <a href="{FEED_PATH}">RSS feed</a></p>
  </div>
</header>

<main class="wrap">
<section id="posts">
{listing}
</section>
</main>
"""
    head = page_head("Blog | Workshop AI", BLOG_DESCRIPTION, BLOG_PATH, build.graph(nodes))
    return head + body + build.FOOTER + build.END


def rfc822(iso):
    d = dt.date.fromisoformat(iso)
    return format_datetime(dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone.utc), usegmt=True)


def render_feed(posts):
    e = html.escape
    items = "".join(f"""  <item>
    <title>{e(p['title'])}</title>
    <link>{post_url(p['slug'])}</link>
    <guid isPermaLink="true">{post_url(p['slug'])}</guid>
    <pubDate>{rfc822(p['date'])}</pubDate>
    <description>{e(p['description'])}</description>
  </item>
""" for p in posts)
    last = f"  <lastBuildDate>{rfc822(posts[0]['date'])}</lastBuildDate>\n" if posts else ""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{BLOG_TITLE}</title>
  <link>{SITE}{BLOG_PATH}</link>
  <atom:link href="{SITE}{FEED_PATH}" rel="self" type="application/rss+xml" />
  <description>{e(BLOG_DESCRIPTION)}</description>
  <language>en-AU</language>
{last}{items}</channel>
</rss>
"""


# ---------------------------------------------------------------- building
def load_posts(root):
    src = os.path.join(root, SRC_DIR)
    posts = []
    if not os.path.isdir(src):
        return posts
    for fn in sorted(os.listdir(src)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        post = read_post(os.path.join(src, fn), [os.path.join(root, OUT_DIR, slug)])
        if post["slug"] != slug:
            raise BlogError(f"{SRC_DIR}/{fn} has slug {post['slug']}; the file name must match")
        posts.append(post)
    return posts


def sitemap_entries(root):
    """(path, lastmod, priority) for the blog index and every listed post."""
    posts = listed(load_posts(root))
    newest = max([BLOG_STARTED] + [p["updated"] for p in posts])
    return [(BLOG_PATH, newest, "0.6")] + [(f"{BLOG_PATH}{p['slug']}/", p["updated"], "0.6") for p in posts]


def write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def build_all(root):
    """Regenerate every post page, the index and the feed. Returns the rel paths written."""
    posts = load_posts(root)
    written = []
    for p in posts:
        rel = f"{OUT_DIR}/{p['slug']}/index.html"
        write(root, rel, render_post(p))
        written.append(rel)
    shown = listed(posts)
    write(root, f"{OUT_DIR}/index.html", render_index(shown))
    write(root, f"{OUT_DIR}/feed.xml", render_feed(shown))
    return written + [f"{OUT_DIR}/index.html", f"{OUT_DIR}/feed.xml"]


def add_post(root, md_path, assets_dir=None, slug=None, date=None):
    """Validate a post, then install its source and images and rebuild the blog and sitemap.
    Safe to re-run: the same input gives byte-identical output."""
    md_path = os.path.abspath(md_path)
    md_dir = os.path.dirname(md_path)
    assets_dir = assets_dir or os.path.join(md_dir, "assets")
    post = read_post(md_path, [assets_dir, md_dir], slug=slug, date=date)   # raises before writing

    raw = post["raw"]
    meta, _ = parse_frontmatter(raw)
    fixed = {}
    if meta.get("slug", "").strip() != post["slug"]:
        fixed["slug"] = post["slug"]          # came from --slug or the article folder name
    if (meta.get("publish_date", "").strip() or meta.get("date", "").strip()) != post["date"]:
        fixed["publish_date"] = post["date"]  # came from --date
    if fixed:
        raw = set_frontmatter(raw, fixed)
    out = os.path.join(root, OUT_DIR, post["slug"])
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    for name, path in post["images"].items():
        shutil.copyfile(path, os.path.join(out, name))
    write(root, f"{SRC_DIR}/{post['slug']}.md", raw)
    build_all(root)
    build.build_sitemap(root)
    return post


def set_frontmatter(raw, values):
    """Set keys in the frontmatter (adding a block if there is none)."""
    meta_lines, body = [], raw
    if raw.startswith("---\n"):
        end = raw.find("\n---", 4)
        meta_lines = raw[4:end].split("\n")
        body = raw[end + 4:].lstrip("\n")
    for key, value in values.items():
        for n, line in enumerate(meta_lines):
            if line.split(":", 1)[0].strip() == key:
                meta_lines[n] = f"{key}: {value}"
                break
        else:
            meta_lines.append(f"{key}: {value}")
    return "---\n" + "\n".join(meta_lines) + "\n---\n\n" + body


def page_paths(root):
    """Generated blog pages, for the build's template-leak guard."""
    return [f"{OUT_DIR}/{p['slug']}/index.html" for p in load_posts(root)] + [f"{OUT_DIR}/index.html"]


if __name__ == "__main__":
    print(json.dumps(build_all(build.ROOT), indent=1))
