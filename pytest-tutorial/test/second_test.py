import pytest
import sys


class Car:
    def __init__(self) -> None:
        self.name = "Tesla"


my_car = Car()


@pytest.mark.skipif(sys.version_info < (3, 9), reason="Python version not supported")
def test_car():
    assert my_car.name == "Tesla"


@pytest.mark.smoke
def test_login():
    x = "Login"
    assert x == "Login"


@pytest.mark.regression
def test_checkout():
    x = "Checkout"
    assert x == "Checkout"


@pytest.mark.skip
def test_logout():
    x = "Logout"
    assert x == "Logout"
