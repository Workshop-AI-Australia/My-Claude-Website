"""Tell Bing (and other IndexNow search engines) that pages have changed.

Run after a change is live on workshopai.com.au:
    python3 _src/indexnow.py            # every URL in sitemap.xml
    python3 _src/indexnow.py /facts/    # just these paths

The key file /<INDEXNOW_KEY>.txt is written by build.py and must be live first.
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from data import SITE, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def urls():
    if len(sys.argv) > 1:
        return [SITE + p for p in sys.argv[1:]]
    sitemap = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", sitemap)


def main():
    host = SITE.split("//", 1)[1]
    body = {"host": host, "key": INDEXNOW_KEY,
            "keyLocation": f"{SITE}/{INDEXNOW_KEY}.txt", "urlList": urls()}
    req = urllib.request.Request("https://api.indexnow.org/indexnow",
                                 data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        print(resp.status, f"submitted {len(body['urlList'])} URLs")


if __name__ == "__main__":
    main()
