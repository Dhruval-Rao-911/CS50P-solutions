from um import count


def test_single():
    assert count("um") == 1


def test_multiple():
    assert count("Hello, um, world") == 1


def test_two_ums():
    assert count("um um um hello") == 3


def test_no_um():
    assert count("This has no filler words.") == 0


def test_um_in_word():
    assert count("Umbrella and Uma went out.") == 0


def test_uppercase():
    assert count("UM, this is loud.") == 1


def test_mixed():
    assert count("This is, um... CS50.") == 1
