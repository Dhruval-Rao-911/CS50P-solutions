from working import convert
import pytest


def test_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"


def test_midnight():
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"


def test_noon():
    assert convert("9 AM to 12 PM") == "09:00 to 12:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:65 AM to 5 PM")
