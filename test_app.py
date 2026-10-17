from app import quote_path


def test_quote_path_encodes_spaces():
    assert quote_path("a b/c") == "a%20b/c"


def test_requests_importable():
    import requests

    assert requests.__version__
