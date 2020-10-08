import pytest
from nodjango_tests.pyconar2020_tutorial.prices import get_min_price, get_first_value
from unittest.mock import Mock


def test_get_first_value_returns_min():
    prices_list = [8, 3, 5, 7, 6]
    assert 3 == get_first_value(sorted, prices_list)


def test_get_first_value_except_on_empty_list():
    prices_list = []
    with pytest.raises(IndexError):
        get_first_value(sorted, prices_list)


@pytest.mark.xfail
def test_get_first_value_fails():
    prices_list = ['100', '90', '400']
    assert '90' == get_first_value(sorted, prices_list)


def test_get_first_value_returns_min_on_string_numbers():
    def sort_string_numbers(string_numbers):
        return sorted(string_numbers, key=lambda x: int(x))

    prices_list = ['100', '90', '400']
    assert '90' == get_first_value(sort_string_numbers, prices_list)


def test_get_first_value_returns_ordered_first():
    prices_list = [8, 3, 5, 7, 6]
    mock_sort_function = Mock(return_value=[3, 5, 6, 7, 8])
    assert 3 == get_first_value(mock_sort_function, prices_list)
    assert mock_sort_function.call_count == 1
    # verificamos que se llama a la funcion de orden con la lista incial
    mock_sort_function.assert_called_with(prices_list)
