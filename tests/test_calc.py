from calc import Calculator
import pytest


@pytest.mark.parametrize("a, b, c", [(1, 5, 6), (69, 1, 70), (1, 2, 3)])
def test_add_two_numbs(a, b, c):
    assert Calculator().add(a, b) == c


@pytest.mark.parametrize("a, b, c, d", [(1, 5, 6, 12), (69, 1, 70, 140), (1, 2, 3, 6)])
def test_add_three_numbs(a, b, c, d):
    assert Calculator().add(a, b, c) == d


@pytest.mark.parametrize("a, b", [([1, 5, 6, 6, 6], 24), ([69], 69), ([], 0), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10)])
def test_add_multi_numbs(a, b):
    assert Calculator().add(*a) == b


@pytest.mark.parametrize("a, b, c", [(1, 5, -4), (69, 1, 68), (1, 2, -1), (-2, -3, 1)])
def test_minus_two_numbs(a, b, c):
    assert Calculator().minus(a, b) == c


@pytest.mark.parametrize("a, b", [([1, 5], 5), ([69, 1], 69), ([1, 2], 2), ([2, 3], 6)])
def test_multiplication_to_numbs(a, b):
    with pytest.raises(ValueError):
        assert Calculator().multiplication(*a) == b


@pytest.mark.parametrize("a, b", [([1, 5, 1], 5), ([5, 5, 2], 50), ([1, 2, 10], 20), ([2, 0, -1], 6)])
def test_multiplication_multi_numbs(a, b):
    with pytest.raises(ValueError):
        assert Calculator().multiplication(*a) == b




