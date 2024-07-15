import pytest
from plates import is_valid

def test_is_valid():
    assert is_valid("HEELL0") == True
    assert is_valid("HELLO, WORLD") == False