from bank import value


def test_hello():
    assert value("Hello") == 0


def test_hello_there():
    assert value("Hello, there!") == 0


def test_how():
    assert value("How are you?") == 20


def test_hi():
    assert value("Hi there!") == 20


def test_other():
    assert value("What's up?") == 100


def test_good_morning():
    assert value("Good morning!") == 100


def test_hola():
    assert value("Hola!") == 20
