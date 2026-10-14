# Site source for the AEO pages

`data.py` holds the company facts, services, prices and every Q&A answer.
`build.py` turns it into:

- `facts/index.html` (company fact sheet, AboutPage structured data)
- `ai-for-tradies/index.html` (Q&A, FAQPage structured data)
- `sitemap.xml` and `llms.txt`
- the structured data block in `index.html` (between the `jsonld:start` and `jsonld:end` markers)

To change a fact, price or answer: edit `data.py`, run `python3 _src/build.py` from the repo root, and commit the results.
Update `UPDATED` and `UPDATED_HUMAN` in `data.py` whenever answers change, since the pages show a "last reviewed" date.

Folders starting with `_` aren't published by GitHub Pages, so nothing here goes live.
