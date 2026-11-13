"""Tests for scripts/add-post and the blog build. Standard library only.

Run from the repo root: python3 -m unittest discover -s tests -v
Each test builds into a throwaway copy of a site root, never this repo.
"""
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADD_POST = os.path.join(REPO, "scripts", "add-post")
sys.path.insert(0, os.path.join(REPO, "_src"))

import blog  # noqa: E402
import build  # noqa: E402

BLOG_HREF = 'href="/blog/"'


def png(path, w=1600, h=900):
    raw = zlib.compress(b"".join(b"\x00" + b"\x22\x33\x3b" * w for _ in range(h)))

    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                + chunk(b"IDAT", raw) + chunk(b"IEND", b""))


def post_md(title, slug, date, body="A first paragraph for the post.", extra=""):
    return f"""---
title: {title}
slug: {slug}
status: pack-ready
publish_date: {date}
client_named: no
client_permission: na
{extra}---

# {title}

<!-- slot: id=img-01 type=hero brief="Hero" alt="Hero image for {title}" -->

{body}
"""


class SiteCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="blog-test-")
        self.site = os.path.join(self.tmp, "site")
        os.makedirs(os.path.join(self.site, "for", "someone"))
        # Stand-in for a Grok Bot landing page: add-post must never touch it.
        with open(os.path.join(self.site, "for", "someone", "index.html"), "w") as f:
            f.write('<p>landing page</p><a href="/blog/">a link that must stay</a>')
        # Copies of this repo's pages that carry the Blog link slot (index.html included).
        for rel in build.linked_pages():
            os.makedirs(os.path.dirname(os.path.join(self.site, rel)), exist_ok=True)
            shutil.copy(os.path.join(REPO, rel), os.path.join(self.site, rel))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def pack(self, name, text, images=("img-01",)):
        """Write <tmp>/<name>/pack/blog.md and pack/assets/<id>.png, like the content repo."""
        pack = os.path.join(self.tmp, name, "pack")
        os.makedirs(os.path.join(pack, "assets"), exist_ok=True)
        with open(os.path.join(pack, "blog.md"), "w") as f:
            f.write(text)
        for img in images:
            png(os.path.join(pack, "assets", f"{img}.png"))
        return os.path.join(pack, "blog.md")

    def add(self, md, *args, ok=True):
        res = subprocess.run([sys.executable, ADD_POST, md, "--site", self.site, *args],
                             capture_output=True, text=True)
        if ok:
            self.assertEqual(res.returncode, 0, res.stderr)
        else:
            self.assertEqual(res.returncode, 1, res.stdout + res.stderr)
        return res

    def read(self, rel):
        with open(os.path.join(self.site, rel), encoding="utf-8") as f:
            return f.read()

    def snapshot(self):
        out = {}
        for d, _dirs, files in os.walk(self.site):
            for fn in files:
                p = os.path.join(d, fn)
                with open(p, "rb") as f:
                    out[os.path.relpath(p, self.site)] = hashlib.sha256(f.read()).hexdigest()
        return out


class NewPost(SiteCase):
    def test_new_post_writes_page_index_feed_sitemap(self):
        md = self.pack("2026-11-20-quotes-first", post_md(
            "Quotes come first", "quotes-first", "2026-11-20",
            body="Opening paragraph with a [link](https://example.com/) and an image.\n\n"
                 "<!-- slot: id=img-02 type=diagram brief=\"D\" alt=\"Diagram of the steps\" -->"),
            images=("img-01", "img-02"))
        self.add(md)

        page = self.read("blog/quotes-first/index.html")
        url = "https://workshopai.com.au/blog/quotes-first/"
        self.assertIn("<h1>Quotes come first</h1>", page)
        self.assertIn('<time datetime="2026-11-20">20 November 2026</time>', page)
        self.assertIn(f'<link rel="canonical" href="{url}" />', page)
        self.assertIn('<meta property="og:type" content="article" />', page)
        self.assertIn(f'<meta property="og:image" content="{url}img-01.png" />', page)
        self.assertIn('<meta name="twitter:card" content="summary_large_image" />', page)
        self.assertIn(f'<meta name="twitter:image" content="{url}img-01.png" />', page)
        self.assertIn('<a href="/blog/">&larr; All posts</a>', page)
        self.assertNotIn("noindex", page)
        # Every image has non-empty alt text and the files sit beside the page.
        imgs = re.findall(r"<img [^>]*>", page.split("<main", 1)[1].split("</main>")[0])
        self.assertEqual(len(imgs), 2)
        for tag in imgs:
            self.assertRegex(tag, r'alt="[^"]+"')
        self.assertTrue(os.path.isfile(os.path.join(self.site, "blog/quotes-first/img-01.png")))
        self.assertTrue(os.path.isfile(os.path.join(self.site, "blog/quotes-first/img-02.png")))
        # Article structured data.
        ld = json.loads(re.search(r'<script type="application/ld\+json">\n(.*?)\n</script>', page, re.S).group(1))
        article = next(n for n in ld["@graph"] if n.get("@type") == "Article")
        self.assertEqual(article["headline"], "Quotes come first")
        self.assertEqual(article["datePublished"], "2026-11-20")
        self.assertEqual(article["image"]["url"], f"{url}img-01.png")
        self.assertEqual((article["image"]["width"], article["image"]["height"]), (1600, 900))

        self.assertIn('href="/blog/quotes-first/">Quotes come first</a>', self.read("blog/index.html"))
        self.assertIn(f"<link>{url}</link>", self.read("blog/feed.xml"))
        self.assertIn(f"<loc>{url}</loc>", self.read("sitemap.xml"))
        self.assertIn("<loc>https://workshopai.com.au/blog/</loc>", self.read("sitemap.xml"))
        self.assertTrue(os.path.isfile(os.path.join(self.site, "_src/blog/quotes-first.md")))

    def test_only_blog_files_sitemap_and_blog_links_are_written(self):
        before = self.snapshot()
        self.add(self.pack("2026-11-20-a", post_md("A", "a", "2026-11-20")))
        after = self.snapshot()
        self.assertEqual(after["for/someone/index.html"], before["for/someone/index.html"])
        allowed = set(build.linked_pages()) | {"sitemap.xml"}
        for rel in after:
            if after[rel] != before.get(rel):
                self.assertTrue(rel in allowed or rel.startswith(("blog/", "_src/blog/")), rel)
        # On the linked pages, only the Blog link slots changed.
        for rel in build.linked_pages():
            with open(os.path.join(REPO, rel), encoding="utf-8") as f:
                original = f.read()
            self.assertEqual(build.set_blog_link(self.read(rel), False), build.set_blog_link(original, False), rel)

    def test_slug_from_article_folder_when_frontmatter_has_none(self):
        text = post_md("No slug", "x", "2026-11-21").replace("slug: x\n", "")
        self.add(self.pack("2026-11-21-from-the-folder", text))
        self.assertTrue(os.path.isfile(os.path.join(self.site, "blog/from-the-folder/index.html")))

    def test_slug_and_date_overrides_are_saved_with_the_source(self):
        text = post_md("Override", "x", "2026-11-21").replace("publish_date: 2026-11-21\n", "")
        self.add(self.pack("o", text), "--slug", "overridden", "--date", "2026-11-23")
        src = self.read("_src/blog/overridden.md")
        self.assertIn("slug: overridden\n", src)
        self.assertIn("publish_date: 2026-11-23\n", src)
        self.assertIn('datetime="2026-11-23"', self.read("blog/overridden/index.html"))


class Rerun(SiteCase):
    def test_rerun_same_slug_is_byte_identical(self):
        md = self.pack("2026-11-20-a", post_md("A post", "a-post", "2026-11-20"))
        self.add(md)
        first = self.snapshot()
        self.add(md)
        self.assertEqual(self.snapshot(), first)

    def test_rerun_with_changes_replaces_post_and_drops_stale_images(self):
        md = self.pack("2026-11-20-a", post_md(
            "A post", "a-post", "2026-11-20",
            body="Old text.\n\n<!-- slot: id=img-02 type=diagram brief=\"D\" alt=\"Old diagram\" -->"),
            images=("img-01", "img-02"))
        self.add(md)
        self.assertTrue(os.path.isfile(os.path.join(self.site, "blog/a-post/img-02.png")))
        md = self.pack("2026-11-20-a", post_md("A post, revised", "a-post", "2026-11-22", body="New text."))
        self.add(md)
        page = self.read("blog/a-post/index.html")
        self.assertIn("New text.", page)
        self.assertNotIn("Old text.", page)
        self.assertFalse(os.path.exists(os.path.join(self.site, "blog/a-post/img-02.png")))
        self.assertEqual(self.read("blog/index.html").count('href="/blog/a-post/"'), 1)
        self.assertEqual(self.read("blog/feed.xml").count("<item>"), 1)
        self.assertEqual(self.read("sitemap.xml").count("/blog/a-post/"), 1)

    def test_rebuild_reproduces_add_post_output(self):
        self.add(self.pack("2026-11-20-a", post_md("A", "a", "2026-11-20")))
        first = self.snapshot()
        res = subprocess.run([sys.executable, ADD_POST, "--rebuild", "--site", self.site],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(self.snapshot(), first)


class BlogSwitch(SiteCase):
    """The blog is hidden until it has a listed post; sample posts never count."""

    def rebuild(self):
        res = subprocess.run([sys.executable, ADD_POST, "--rebuild", "--site", self.site],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stderr)
        return res

    def remove(self, slug):
        res = subprocess.run([sys.executable, ADD_POST, "--remove", slug, "--site", self.site],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stderr)
        return res

    def assert_hidden(self):
        for rel in build.linked_pages():
            page = self.read(rel)
            self.assertNotIn(BLOG_HREF, page, rel)
            self.assertEqual(page.count(build.BLOG_LINK_START + build.BLOG_LINK_END), 2, rel)
        self.assertNotIn("/blog/", self.read("sitemap.xml"))
        index = self.read("blog/index.html")
        self.assertIn('<meta name="robots" content="noindex" />', index)
        self.assertNotIn(BLOG_HREF, index.split("<header", 1)[0])   # no Blog link in the blog's own nav
        self.assertTrue(os.path.isfile(os.path.join(self.site, "blog/feed.xml")))

    def assert_live(self):
        link = build.BLOG_LINK_START + build.BLOG_LINK + build.BLOG_LINK_END
        for rel in build.linked_pages():
            page = self.read(rel)
            self.assertEqual(page.count(link), 2, rel)          # nav and footer
            self.assertEqual(page.count(BLOG_HREF), 2, rel)
        self.assertIn("<loc>https://workshopai.com.au/blog/</loc>", self.read("sitemap.xml"))
        index = self.read("blog/index.html")
        self.assertNotIn('name="robots"', index)
        self.assertIn('<a href="/blog/" aria-current="page">Blog</a><!-- /blog-link -->', index)
        self.assertIn('      <!-- blog-link --><a href="/blog/">Blog</a><!-- /blog-link -->', index)

    def test_zero_listed_posts_gives_no_link_and_no_sitemap_entry(self):
        # Start from pages that show the link, as if the blog had been live before.
        for rel in build.linked_pages():
            shown = build.set_blog_link(self.read(rel), True)
            with open(os.path.join(self.site, rel), "w", encoding="utf-8") as f:
                f.write(shown)
            self.assertEqual(shown.count(BLOG_HREF), 2, rel)
        self.rebuild()
        self.assert_hidden()
        self.assertIn("No posts yet.", self.read("blog/index.html"))

    def test_first_listed_post_adds_link_and_sitemap_entry_on_every_page(self):
        self.add(self.pack("sample", post_md("Sample", "sample-post", "2026-11-25", extra="sample: yes\n")))
        self.assert_hidden()
        landing = self.read("for/someone/index.html")
        res = self.add(self.pack("2026-11-20-first", post_md("First", "first", "2026-11-20")))
        self.assertIn("blog is live", res.stdout)
        self.assert_live()
        for rel in ("blog/first/index.html", "blog/sample-post/index.html"):
            self.assertIn('<a href="/blog/" aria-current="page">Blog</a>', self.read(rel), rel)
        self.assertEqual(self.read("for/someone/index.html"), landing)
        # Re-running with the blog already live changes nothing.
        live = self.snapshot()
        self.add(self.pack("2026-11-20-first", post_md("First", "first", "2026-11-20")))
        self.rebuild()
        self.assertEqual(self.snapshot(), live)

    def test_removing_the_only_listed_post_removes_link_and_sitemap_entry(self):
        self.rebuild()
        hidden = self.snapshot()
        self.add(self.pack("2026-11-20-only", post_md("Only", "only", "2026-11-20")))
        self.assert_live()
        res = self.remove("only")
        self.assertIn("blog is hidden", res.stdout)
        self.assert_hidden()
        self.assertFalse(os.path.exists(os.path.join(self.site, "blog/only")))
        self.assertFalse(os.path.exists(os.path.join(self.site, "_src/blog/only.md")))
        self.assertEqual(self.snapshot(), hidden)   # back to exactly where it started

    def test_removing_by_hand_then_rebuilding_also_hides_the_blog(self):
        self.add(self.pack("2026-11-20-only", post_md("Only", "only", "2026-11-20")))
        os.remove(os.path.join(self.site, "_src/blog/only.md"))
        shutil.rmtree(os.path.join(self.site, "blog/only"))
        self.rebuild()
        self.assert_hidden()

    def test_sample_posts_never_count(self):
        for slug in ("sample-post", "another-sample"):
            self.add(self.pack(slug, post_md(slug, slug, "2026-11-25", extra="sample: yes\n")))
            self.assert_hidden()
        # With a real post and a sample, taking the real one away hides the blog again.
        self.add(self.pack("2026-11-20-real", post_md("Real", "real", "2026-11-20")))
        self.assert_live()
        self.remove("real")
        self.assert_hidden()
        self.assertTrue(blog.load_posts(self.site))       # the samples are still there
        self.assertFalse(blog.is_live(self.site))

    def test_remove_unknown_post_is_refused(self):
        before = self.snapshot()
        res = subprocess.run([sys.executable, ADD_POST, "--remove", "nope", "--site", self.site],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 1)
        self.assertIn("no post called nope", res.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_set_blog_link_is_idempotent_and_keeps_aria_current(self):
        on = '<!-- blog-link --><a href="/blog/" aria-current="page">Blog</a><!-- /blog-link -->'
        self.assertEqual(build.set_blog_link(on, True), on)
        off = build.set_blog_link(on, False)
        self.assertEqual(off, "<!-- blog-link --><!-- /blog-link -->")
        self.assertEqual(build.set_blog_link(off, False), off)
        self.assertEqual(build.set_blog_link(off, True), '<!-- blog-link --><a href="/blog/">Blog</a><!-- /blog-link -->')
        self.assertEqual(build.set_blog_link("<p>no slot</p>", True), "<p>no slot</p>")


class Ordering(SiteCase):
    def test_index_and_feed_are_newest_first(self):
        # Added out of date order on purpose; two posts share a date (then by slug).
        for slug, date in [("middle", "2026-11-15"), ("oldest", "2026-11-01"),
                           ("newest-b", "2026-12-01"), ("newest-a", "2026-12-01")]:
            self.add(self.pack(f"{date}-{slug}", post_md(slug.title(), slug, date)))
        expected = ["newest-a", "newest-b", "middle", "oldest"]
        index = re.findall(r'<h2><a href="/blog/([a-z-]+)/">', self.read("blog/index.html"))
        self.assertEqual(index, expected)
        feed = self.read("blog/feed.xml")
        items = re.findall(r"<item>\s*<title>[^<]*</title>\s*<link>https://workshopai.com.au/blog/([a-z-]+)/", feed)
        self.assertEqual(items, expected)
        self.assertIn("<lastBuildDate>Tue, 01 Dec 2026 00:00:00 GMT</lastBuildDate>", feed)
        sitemap = re.findall(r"/blog/([a-z-]+)/</loc>", self.read("sitemap.xml"))
        self.assertEqual(sitemap, expected)


class SampleAndSafety(SiteCase):
    def test_sample_post_is_built_but_not_listed(self):
        self.add(self.pack("2026-11-20-real", post_md("Real", "real", "2026-11-20")))
        self.add(self.pack("sample", post_md("Sample", "sample-post", "2026-11-25", extra="sample: yes\n")))
        page = self.read("blog/sample-post/index.html")
        self.assertIn('<meta name="robots" content="noindex, nofollow" />', page)
        self.assertIn("sample-banner", page)
        for rel in ("blog/index.html", "blog/feed.xml", "sitemap.xml"):
            self.assertNotIn("sample-post", self.read(rel), rel)
            self.assertIn("/blog/real/", self.read(rel), rel)

    def test_missing_alt_text_is_refused_and_nothing_written(self):
        text = post_md("A", "a", "2026-11-20").replace('alt="Hero image for A"', 'alt=""')
        before = self.snapshot()
        res = self.add(self.pack("a", text), ok=False)
        self.assertIn("alt text", res.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_missing_image_is_refused(self):
        res = self.add(self.pack("a", post_md("A", "a", "2026-11-20"), images=()), ok=False)
        self.assertIn("no image file for slot img-01", res.stderr)

    def test_client_named_without_permission_is_refused(self):
        text = post_md("A", "a", "2026-11-20").replace(
            "client_named: no\nclient_permission: na", "client_named: yes\nclient_permission: no")
        res = self.add(self.pack("a", text), ok=False)
        self.assertIn("names a client without permission", res.stderr)

    def test_draft_status_is_refused(self):
        text = post_md("A", "a", "2026-11-20").replace("status: pack-ready", "status: drafting")
        self.add(self.pack("a", text), ok=False)

    def test_bad_date_and_slug_are_refused(self):
        self.add(self.pack("a", post_md("A", "a", "20 Nov 2026")), ok=False)
        self.add(self.pack("b", post_md("B", "Not A Slug", "2026-11-20")), ok=False)

    def test_raw_html_is_escaped_and_script_links_refused(self):
        self.add(self.pack("a", post_md("A", "a", "2026-11-20", body="<script>alert(1)</script> text")))
        page = self.read("blog/a/index.html")
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt; text", page)
        res = self.add(self.pack("b", post_md("B", "b", "2026-11-20", body="[x](javascript:alert(1))")), ok=False)
        self.assertIn("link scheme not allowed", res.stderr)


class Markdown(unittest.TestCase):
    def test_subset(self):
        images = blog.Images([])
        out = blog.markdown("## Head\n\nSome **bold** and *em* and `code`.\n\n- one\n- two\n\n1. a\n2. b\n\n"
                            "> quoted\n\n<!-- a comment -->\n\n---", images)
        self.assertIn("<h2>Head</h2>", out)
        self.assertIn("<strong>bold</strong>", out)
        self.assertIn("<em>em</em>", out)
        self.assertIn("<code>code</code>", out)
        self.assertIn("<ul>\n  <li>one</li>\n  <li>two</li>\n</ul>", out)
        self.assertIn("<ol>\n  <li>a</li>\n  <li>b</li>\n</ol>", out)
        self.assertIn("<blockquote>\n<p>quoted</p>\n</blockquote>", out)
        self.assertNotIn("comment", out)
        self.assertIn("<hr />", out)


class ThisRepo(unittest.TestCase):
    """Checks on the committed site, not a temp copy."""

    def test_sample_post_exists_and_is_unlisted(self):
        with open(os.path.join(REPO, "blog", "sample-post", "index.html"), encoding="utf-8") as f:
            self.assertIn("noindex", f.read())
        for rel in ("blog/index.html", "blog/feed.xml", "sitemap.xml"):
            with open(os.path.join(REPO, rel), encoding="utf-8") as f:
                self.assertNotIn("sample-post", f.read(), rel)

    def test_committed_blog_is_up_to_date(self):
        """Rebuilding from _src/blog/ into a copy must match what is committed, Blog links included."""
        tmp = tempfile.mkdtemp(prefix="blog-repo-")
        try:
            for d in ("_src", "blog"):
                shutil.copytree(os.path.join(REPO, d), os.path.join(tmp, d),
                                ignore=shutil.ignore_patterns("__pycache__"))
            for rel in ["sitemap.xml"] + build.linked_pages():
                os.makedirs(os.path.dirname(os.path.join(tmp, rel)), exist_ok=True)
                shutil.copy(os.path.join(REPO, rel), os.path.join(tmp, rel))
            res = subprocess.run([sys.executable, ADD_POST, "--rebuild", "--site", tmp],
                                 capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, res.stderr)
            for rel in (["sitemap.xml", "blog/index.html", "blog/feed.xml"] + blog.page_paths(REPO)
                        + build.linked_pages()):
                with open(os.path.join(REPO, rel), encoding="utf-8") as a, \
                        open(os.path.join(tmp, rel), encoding="utf-8") as b:
                    self.assertEqual(a.read(), b.read(), f"{rel} is stale; run scripts/add-post --rebuild")
        finally:
            shutil.rmtree(tmp)

    def test_every_linked_page_has_a_blog_link_slot_in_nav_and_footer(self):
        for rel in build.linked_pages():
            with open(os.path.join(REPO, rel), encoding="utf-8") as f:
                self.assertEqual(len(build.BLOG_LINK_RE.findall(f.read())), 2, rel)

    def test_blog_link_matches_listed_posts(self):
        """While no post is listed, no page outside /blog/ links to it and the sitemap leaves it out."""
        live = blog.is_live(REPO)
        for d, dirs, files in os.walk(REPO):
            dirs[:] = [x for x in dirs if not x.startswith((".", "_"))]
            rel_dir = os.path.relpath(d, REPO)
            if rel_dir == "blog" or rel_dir.startswith("blog" + os.sep):
                continue
            for fn in files:
                if fn.endswith(".html") and rel_dir.split(os.sep)[0] not in ("for", "floor-ready"):
                    rel = os.path.normpath(os.path.join(rel_dir, fn))
                    with open(os.path.join(REPO, rel), encoding="utf-8") as f:
                        text = f.read()
                    if not live:
                        self.assertNotIn(BLOG_HREF, text, rel)
        with open(os.path.join(REPO, "sitemap.xml"), encoding="utf-8") as f:
            self.assertEqual("/blog/" in f.read(), live)

    def test_open_blog_pr_workflow(self):
        with open(os.path.join(REPO, ".github", "workflows", "open-blog-pr.yml"), encoding="utf-8") as f:
            wf = f.read()
        self.assertIn('- "blog/**"', wf)
        self.assertIn("permissions:\n  contents: read\n  pull-requests: write\n", wf)
        self.assertIn("${{ github.token }}", wf)
        self.assertNotIn("secrets.", wf)
        self.assertNotIn("merge", wf.split("jobs:", 1)[1].lower())
        # The commit message reaches the shell through env, never inline in the script.
        self.assertNotIn("${{ github.event.head_commit.message }}", wf.split("run: |", 1)[1])


if __name__ == "__main__":
    unittest.main()
