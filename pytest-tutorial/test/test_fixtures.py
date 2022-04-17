import pytest


@pytest.fixture
def setup():
    print("Start server")
    yield
    print("Close browser")


def test1(setup):
    print("Test 1 execute")


def test2(setup):
    print("Test 2 execute")


def test3(setup):
    print("Test 3 execute")
