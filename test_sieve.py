from sieve import Sieve


def is_even(number):
    return number % 2 == 0


def is_positive(number):
    return number >= 0


def test__Sieve__creation():
    sieve = Sieve(is_even)


def test__Sieve__repr():
    sieve = Sieve(is_even)
    assert repr(sieve) == "Sieve(is_even)"


def test__Sieve__call():
    sieve = Sieve(is_even)
    assert sieve(8) is True
    assert sieve(9) is False


def test__Sieve__negation():
    sieve = Sieve(is_even)
    is_odd = sieve._not()
    assert is_odd(8) is False
    assert is_odd(9) is True


def test__Sieve__negation_repr():
    sieve = Sieve(is_even)
    is_odd = sieve._not()
    assert repr(is_odd) == "Sieve(not(is_even))"


def test__Sieve__intersection():
    even_sieve = Sieve(is_even)
    positive_sieve = Sieve(is_positive)
    intersection_sieve = even_sieve & positive_sieve
    assert intersection_sieve(8) is True
    assert intersection_sieve(-8) is False
    assert intersection_sieve(9) is False
    assert intersection_sieve(-9) is False


def test__Sieve__intersection_repr():
    even_sieve = Sieve(is_even)
    positive_sieve = Sieve(is_positive)
    intersection_sieve = even_sieve & positive_sieve
    assert repr(intersection_sieve) == "Sieve(is_even & is_positive)"


def test__Sieve__union():
    even_sieve = Sieve(is_even)
    positive_sieve = Sieve(is_positive)
    intersection_sieve = even_sieve | positive_sieve
    assert intersection_sieve(8) is True
    assert intersection_sieve(9) is True
    assert intersection_sieve(-2) is True
    assert intersection_sieve(-8) is True
    assert intersection_sieve(-9) is False


def test__Sieve__union_repr():
    even_sieve = Sieve(is_even)
    positive_sieve = Sieve(is_positive)
    intersection_sieve = even_sieve | positive_sieve
    assert repr(intersection_sieve) == "Sieve(is_even | is_positive)"
