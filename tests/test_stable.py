from app import add, mul


def test_add_positive_numbers():
    assert add(2, 4) == 6


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_mul_positive_numbers():
    assert mul(1, 2) > 0


def test_mul_negative_numbers():
    assert mul(-1, -3) > 0
