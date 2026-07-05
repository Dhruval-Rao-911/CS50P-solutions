from fuel import convert, gauge


def test_convert_quarter():
    assert convert("1/4") == 25


def test_convert_half():
    assert convert("1/2") == 50


def test_convert_full():
    assert convert("4/4") == 100


def test_convert_zero():
    assert convert("0/4") == 0


def test_convert_invalid():
    try:
        convert("4/0")
        assert False
    except ZeroDivisionError:
        pass


def test_convert_greater():
    try:
        convert("5/4")
        assert False
    except ValueError:
        pass


def test_convert_negative():
    try:
        convert("-1/4")
        assert False
    except ValueError:
        pass


def test_gauge_empty():
    assert gauge(0) == "E"


def test_gauge_full():
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"


def test_gauge_one():
    assert gauge(1) == "E"


def test_gauge_ninetynine():
    assert gauge(99) == "F"
