from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True


def test_too_short():
    assert is_valid("C") == False


def test_too_long():
    assert is_valid("CS50PY") == False


def test_starts_with_number():
    assert is_valid("50CS") == False


def test_starts_with_zero():
    assert is_valid("CS05") == False


def test_letters_after_numbers():
    assert is_valid("CS50P") == False


def test_punctuation():
    assert is_valid("CS.50") == False


def test_spaces():
    assert is_valid("CS 50") == False

def test_starts_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
