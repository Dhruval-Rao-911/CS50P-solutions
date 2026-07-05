from twttr import shorten


def test_vowels():
    assert shorten("Twitter") == "Twttr"


def test_all_vowels():
    assert shorten("aeiou") == ""


def test_uppercase_vowels():
    assert shorten("AEIOU") == ""


def test_numbers():
    assert shorten("cs50") == "cs50"


def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
