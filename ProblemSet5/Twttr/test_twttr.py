import pytest

from twttr import shorten

def test_shoten():
    assert shorten("aeiou") == ""
    assert shorten("arri") == "rr"
    assert shorten("rrr") == "rrr"
