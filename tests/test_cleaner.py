from processing.cleaner import clean_text

def test_clean_text():
    assert clean_text("<p>Hello   world</p>") == "Hello world"
