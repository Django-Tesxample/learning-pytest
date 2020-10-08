import pytest
from nodjango_tests.pyconar2020_tutorial.prices import get_min_price, get_min_value


def test_get_min_value_returns_min():
    prices_list = [8, 3, 5, 7, 6]
    assert 3 == get_min_value(sorted, prices_list)


def test_get_min_value_except_on_empty_list():
    prices_list = []
    with pytest.raises(IndexError):
        get_min_value(sorted, prices_list)


@pytest.mark.xfail
def test_get_min_value_fails():
    prices_list = ['100', '90', '400']
    assert '90' == get_min_value(sorted, prices_list)


def test_get_min_value_returns_min_on_string_numbers():
    def sort_string_numbers(string_numbers):
        return sorted(string_numbers, key=lambda x: int(x))

    prices_list = ['100', '90', '400']
    assert '90' == get_min_value(sort_string_numbers, prices_list)
