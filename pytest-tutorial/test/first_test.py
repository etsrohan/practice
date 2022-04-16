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
