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
def test_multiplication_two_numbs(a, b):
    assert Calculator().multiplication(*a) == b


@pytest.mark.parametrize("a, b", [([0, 5], 0)])
def test_multiplication_with_zero(a, b):
    with pytest.raises(ValueError):
        Calculator().multiplication(*a)


@pytest.mark.parametrize("a, b", [([1, 5, 1], 5), ([5, 5, 2], 50), ([1, 2, 10], 20)])
def test_multiplication_multi_numbs(a, b):
    assert Calculator().multiplication(*a) == b


@pytest.mark.parametrize("a, b, c", [(1, 5, 0.2)])
def test_division_two_numbs(a, b, c):
    assert Calculator().division(a, b) == c


@pytest.mark.parametrize("a, b, c", [(5, 0, float("inf"))])
def test_division_two_numbs_with_zero(a, b, c):
    assert Calculator().division(a, b) == c


@pytest.mark.parametrize("a, b", [([5, 5, 5], 5)])
def test_avg(a, b):
    assert Calculator().avg(*a) == b


@pytest.mark.parametrize("a, b,c ", [([5, 5, 5, 10, 500, 100], 5, 5)])
def test_avg_below(a, b, c):
    assert Calculator().avg(*a, lt=b) == c


@pytest.mark.parametrize("a, b,c ", [([5, 5, 5, 10, 10, 10], 10, 10)])
def test_avg_gt(a, b, c):
    assert Calculator().avg(*a, gt=b) == c


@pytest.mark.parametrize("a, b,c ", [([5, 5, 5, 10, 10, 10], 0, 0)])
def test_avg_gt_lt(a, b, c):
    assert Calculator().avg(*a, gt=b, lt=b) == c


@pytest.mark.parametrize("a, c", [([], 0)])
def test_empty_num_list(a, c):
    assert Calculator().avg(*a) == c
