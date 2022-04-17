import pytest
import sys


def test1():
    x = 10 + 10
    y = 20
    assert x == y


def test2():
    name = "Rohan"
    title = "Rohan is a programmer"
    assert name in title


def test3():
    name = "Jenkins"
    title = "Jenkins"
    assert name is title, "Title does not match"


@pytest.mark.skipif(sys.version_info < (3, 6), reason="Python version not supported")
@pytest.mark.parametrize(
    "first_name, last_name, full_name",
    [
        ("Rohan", "Srivastava", "Rohan Srivastava"),
        ("Rohit", "Rastogi", "Rohit Rastogi"),
        ("Nitish", "Ragunathan", "Nitish Ragunathan"),
    ],
)
def test4(first_name, last_name, full_name):
    assert f"{first_name} {last_name}" == full_name
