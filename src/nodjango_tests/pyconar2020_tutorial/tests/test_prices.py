import pytest
from nodjango_tests.pyconar2020_tutorial.prices import get_min_price, get_first_value
from unittest.mock import Mock, patch


def test_get_first_value_returns_min():
    prices_list = [8, 3, 5, 7, 6]
    assert 3 == get_first_value(sorted, prices_list)


def test_get_first_value_except_on_empty_list():
    prices_list = []
    with pytest.raises(IndexError):
        get_first_value(sorted, prices_list)


def test_get_min_price_returns_min_values():
    prices_list = [8, 3, 5, 7, 6]
    with patch('nodjango_tests.pyconar2020_tutorial.prices.get_prices_list') as mock_prices:
        mock_prices.return_value = prices_list
        assert 3 == get_min_price()


@patch('nodjango_tests.pyconar2020_tutorial.prices.get_first_value')
@patch('nodjango_tests.pyconar2020_tutorial.prices.get_prices_list')
def test_get_min_price_use_get_first_value(mock_g_prices, mock_g_first):
    prices_list = [8, 3, 5, 7, 6]
    mock_g_prices.return_value = prices_list
    mock_g_first.return_value = 4  # 😁
    assert 4 == get_min_price()
    mock_g_first.assert_called_once_with(sorted, prices_list)


@pytest.mark.xfail
def test_get_first_value_fails():
    prices_list = ['100', '90', '400']
    assert '90' == get_first_value(sorted, prices_list)


def test_get_first_value_returns_min_on_string_numbers():
    def sort_string_numbers(string_numbers):
        return sorted(string_numbers, key=lambda x: int(x))

    prices_list = ['100', '90', '400']
    assert get_first_value(sort_string_numbers, prices_list) == '90'


def test_get_first_value_returns_ordered_first():
    prices_list = [8, 3, 5, 7, 6]
    mock_sort_function = Mock(return_value=[3, 5, 6, 7, 8])
    assert get_first_value(mock_sort_function, prices_list) == 3
    assert mock_sort_function.call_count == 1
    # verificamos que se llama a la funcion de orden con la lista incial
    mock_sort_function.assert_called_with(prices_list)
