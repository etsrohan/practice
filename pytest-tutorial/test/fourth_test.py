import random
import pytest


@pytest.mark.xfail
def test_random():
    x = random.randint(0, 5)
    y = 3
    assert x == y
