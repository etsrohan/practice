import pytest


class Car:
    def __init__(self) -> None:
        self.name = "Tesla"


my_car = Car()


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


def test_logout():
    x = "Logout"
    assert x == "Logout"
