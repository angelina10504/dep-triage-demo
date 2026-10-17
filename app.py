"""Tiny demo app used as the scan target for the Dependency Advisory Triage agent.

The pinned versions in requirements.txt are deliberately old and vulnerable:
- requests 2.19.0 -> the safe upgrade keeps this code working (CI passes)   -> TC1
- Jinja2 2.10     -> the safe upgrade is Jinja2 3.x, which removed
                     `jinja2.Markup`, so this import breaks (CI fails)       -> TC3
"""
import requests
from jinja2 import Markup, Template


def render_greeting(name):
    return Template("Hello {{ name }}!").render(name=Markup.escape(name))


def fetch_status(url):
    return requests.get(url, timeout=5).status_code
