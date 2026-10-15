# Site source for the AEO pages

`data.py` holds the company facts, services, prices and every Q&A answer.
`pages.py` holds the industry pages, the Melbourne's west page and the Simpro page, with their sources.
`build.py` turns them into:

- `facts/index.html` (company fact sheet, AboutPage structured data)
- `ai-for-tradies/index.html` (Q&A, FAQPage structured data)
- one folder per page in `pages.py`, such as `ai-for-hvac/index.html` (FAQPage, Service and breadcrumb structured data, plus a sources list built from the page's links)
- `privacy/index.html`
- `sitemap.xml`, `llms.txt` and the IndexNow key file (`<key>.txt` at the root)
- the structured data block in `index.html` (between the `jsonld:start` and `jsonld:end` markers)

To change a fact, price, answer or page: edit `data.py` or `pages.py`, run `python3 _src/build.py` from the repo root, and commit the results.
Update `UPDATED` and `UPDATED_HUMAN` in `data.py` whenever content changes, since the pages show a "last reviewed" date.

Every new page must pass the doorway test: if you could swap the trade or place name and nothing else needed to change, rewrite it. Every rule or figure needs a source in `pages.py`.

After a change is live, run `python3 _src/indexnow.py` to tell Bing which pages changed (or pass paths, for example `python3 _src/indexnow.py /facts/`).

Folders starting with `_` aren't published by GitHub Pages, so nothing here goes live.
