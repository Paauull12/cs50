from jar import Jar
import pytest

def test_jar():
    jar1 = Jar()
    assert jar1.capacity == 12

    jar2 = Jar(1)
    assert jar2.capacity == 1

    with pytest.raises(ValueError):
        jar3 = Jar(-1)

    jar2.deposit(1)
    assert int(jar2.size) == 1

    jar2.withdraw(1)

    assert int(jar2.size) == 0

    with pytest.raises(ValueError):
        jar2.withdraw(10)
