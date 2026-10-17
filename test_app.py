from app import render_greeting


def test_render_greeting_escapes_html():
    assert render_greeting("<b>Angelina</b>") == "Hello &lt;b&gt;Angelina&lt;/b&gt;!"


def test_requests_importable():
    import requests

    assert requests.__version__
