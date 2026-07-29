from seasons import convert
from datetime import date


def test_today():
    today = date.today()
    result = convert(today)
    assert result == "Zero minutes"


def test_one_day():
    from datetime import timedelta
    yesterday = date.today() - timedelta(days=1)
    result = convert(yesterday)
    assert "thousand" in result.lower() or "hundred" in result.lower()


def test_returns_string():
    today = date.today()
    result = convert(today)
    assert isinstance(result, str)


def test_ends_with_minutes():
    today = date.today()
    result = convert(today)
    assert result.endswith("minutes")
