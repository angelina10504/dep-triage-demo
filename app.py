"""Demo scan target. Deliberately old, vulnerable pins:
- requests 2.28.0 -> safe upgrade keeps code working, CI passes (TC1)
- Werkzeug 2.2.2  -> safe upgrade is 3.x, which removed werkzeug.urls.url_quote, CI fails (TC3)
"""
import requests
from werkzeug.urls import url_quote


def quote_path(path):
    return url_quote(path)


def fetch_status(url):
    return requests.get(url, timeout=5).status_code
