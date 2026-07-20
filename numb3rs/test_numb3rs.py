from numb3rs import validate


def test_valid():
    assert validate("1.2.3.4") == True


def test_valid_zeros():
    assert validate("0.0.0.0") == True


def test_valid_max():
    assert validate("255.255.255.255") == True


def test_invalid_first_byte():
    assert validate("256.2.3.4") == False


def test_invalid_second_byte():
    assert validate("1.256.3.4") == False


def test_invalid_third_byte():
    assert validate("1.2.256.4") == False


def test_invalid_fourth_byte():
    assert validate("1.2.3.256") == False


def test_invalid_format():
    assert validate("1.2.3") == False


def test_invalid_five_bytes():
    assert validate("1.2.3.4.5") == False


def test_invalid_letters():
    assert validate("cat") == False


def test_leading_zeros():
    assert validate("000.001.010.100") == False
