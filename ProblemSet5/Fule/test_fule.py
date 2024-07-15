import pytest
from fule import convert, gauge


def test_covert():
    assert convert("3/4") == ['3', '4']
    assert convert("1/2") == ['1', '2']

def test_gauge():
    with pytest.raises(ValueError):
        gauge(['cat', 'mouse'])
    assert gauge(['1', '2']) == "50%"