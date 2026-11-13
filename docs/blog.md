# Blog

The blog lives at `/blog/`. Every post is a static page built by `scripts/add-post` from a markdown file and its images. The index, the RSS feed and the sitemap entries are regenerated from the same files on every run.

## Where things live

| Path | What it is |
| -- | -- |
| `_src/blog/<slug>.md` | Source of truth for each post. Not published (folders starting with `_` are skipped by GitHub Pages). |
| `_src/blog.py` | Builds the post pages, the index and the feed. Uses the site's shared CSS, nav, footer and structured data from `_src/build.py`. |
| `blog/<slug>/index.html` | The post page, at `https://workshopai.com.au/blog/<slug>/`. |
| `blog/<slug>/<image>` | The post's images, served beside the page. |
| `blog/index.html` | The index, newest first. |
| `blog/feed.xml` | RSS 2.0 feed, newest first. |
| `sitemap.xml` | Built by `build_sitemap()` in `_src/build.py`, which adds `/blog/` and every listed post. |
| `scripts/add-post` | Adds or updates a post. |
| `tests/test_add_post.py` | Tests for `scripts/add-post`. |
| `.github/workflows/open-blog-pr.yml` | Opens a pull request when a `blog/**` branch is pushed. |
| `.github/workflows/blog-checks.yml` | Runs the tests and lint on pull requests. |

The Blog link is in the nav and footer of every page built by `_src/build.py`, and in the hand-written nav and footer of `index.html`.

## Adding a post

```
scripts/add-post <path/to/blog.md> [--assets <dir>] [--slug <slug>] [--date <yyyy-mm-dd>]
```

* Images are read from `--assets`, or by default from the `assets/` folder beside `blog.md`. That matches the content engine's pack layout: `pack/blog.md` with `pack/assets/<slot id>.png` or `.jpg`.
* The script writes `blog/<slug>/` (page and images) and `_src/blog/<slug>.md`, then rebuilds every post page, `blog/index.html`, `blog/feed.xml` and `sitemap.xml`. It writes nothing else.
* It is deterministic and safe to re-run. The same input gives byte-identical output. Re-running with the same slug replaces that post and removes images it no longer uses.
* If the post can't be published as written, it exits with status 1 and a message, and writes nothing.
* `scripts/add-post --rebuild` regenerates the blog and sitemap from `_src/blog/` without adding anything.
* `python3 _src/build.py` also rebuilds the blog, so a full site build never drops blog pages.

Commit everything the script changed, on a branch, and raise a pull request. Nothing is live until the pull request is merged.

## The blog.md format

Frontmatter, then markdown:

```
---
title: The post title
slug: the-post-title
publish_date: 2026-11-20
description: One or two sentences for the index, the feed and link previews.
client_named: no
client_permission: na
---

<!-- slot: id=img-01 type=hero brief="..." alt="What the image shows" -->

The first paragraph.
```

| Field | Required | Notes |
| -- | -- | -- |
| `title` | yes | Falls back to the first `# ` heading. A leading `# ` heading that matches the title is dropped, since the page already shows it. |
| `slug` | yes | Lower-case words joined by hyphens. Falls back to the article folder name (`articles/<yyyy-mm-dd>-<slug>/pack/blog.md`), then `--slug` overrides both. |
| `publish_date` | yes | `yyyy-mm-dd`. `date` also works. `--date` overrides it. |
| `updated` | no | `yyyy-mm-dd`. Used for `dateModified` and the sitemap. Defaults to the publish date. |
| `description` | no | Defaults to the first paragraph, cut to about 160 characters. |
| `status` | no | If present it must be `pack-ready` or `published` (sample posts excepted). |
| `client_named`, `client_permission` | no | A post with `client_named: yes` is refused unless `client_permission: yes`. |
| `sample` | no | `yes` marks a sample post (see below). |

Overrides given with `--slug` or `--date`, and a slug taken from the folder name, are written into the saved copy in `_src/blog/` so rebuilds give the same result.

### Images

* An image slot, `<!-- slot: id=<id> type=<type> brief="..." alt="..." -->` on its own line, becomes an image. The file is `<id>.png`, `.jpg` or `.jpeg` in the assets folder.
* The first slot with `type=hero` is the hero image. A post must have one.
* A markdown image, `![alt](file.png)`, also works. Files must be local PNG, JPEG, GIF or WebP.
* Every image needs alt text. A missing or empty alt stops the script.

### Markdown

Supported: paragraphs, `##` to `######` headings (a `#` heading becomes `##`), bold, italic, inline code, fenced code blocks, links, bullet and numbered lists, block quotes and horizontal rules. Links may be `http`, `https`, `mailto`, `tel` or site paths; other schemes are refused. Raw HTML is shown as text, never passed through. HTML comments other than image slots are dropped.

## What each post page has

Title, date, hero image, body, alt text on every image, a canonical URL, Open Graph tags (`og:type` article, hero image and alt text), Twitter card tags (`summary_large_image`), Article structured data with a breadcrumb in JSON-LD, a link to the feed, and a link back to `/blog/`.

## Order

The index, the feed and the sitemap list posts newest first by publish date. Posts with the same date are listed by slug, A to Z.

## Sample post

`_src/blog/sample-post.md` builds `/blog/sample-post/`, a page of placeholder text that shows the layout. Any post with `sample: yes` gets a `noindex, nofollow` tag and a visible sample banner, and is left out of the index, the feed and the sitemap. Delete `_src/blog/sample-post.md` and `blog/sample-post/` once a real post is live.

## Pull request workflow

`.github/workflows/open-blog-pr.yml` runs when a branch matching `blog/**` is pushed. If no pull request into `main` is open for that branch, it opens one. The title is the first line of the head commit message and the body is the rest of it. It uses the workflow's built-in token with `contents: read` and `pull-requests: write`, and no personal access token. It never merges; Justin merges.

This lets the content engine publish with a deploy key alone: push a `blog/<slug>` branch with the output of `scripts/add-post`, and the pull request opens itself.

Two GitHub behaviours to know:

* The built-in token can only open pull requests if the repository allows GitHub Actions to create pull requests (Settings, Actions, General, Workflow permissions). That setting is handled outside this repo's files.
* A pull request opened with the built-in token does not trigger other workflows, so `blog-checks.yml` won't run on it until someone pushes another commit to the branch or the Blog checks workflow is run by hand from the Actions tab on that branch.

## Tests and lint

From the repo root, with Python 3.12 or later (`_src/build.py` needs it):

```
python3 -m unittest discover -s tests -v
uvx ruff@0.14.0 check
actionlint
```

`ruff.toml` limits lint to the blog tooling. `_config.yml` keeps `scripts/`, `docs/`, `tests/` and `ruff.toml` off the live site.
