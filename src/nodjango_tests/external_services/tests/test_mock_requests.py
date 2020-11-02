import requests_mock
from unittest.mock import patch, Mock
from nodjango_tests.pyconar2020_tutorial.services import get_prices_list


@patch("nodjango_tests.pyconar2020_tutorial.services.requests.request")
def test_get_prices_list_converts_to_int(mock_request):
    """Verifica que la funcion get_prices_list ante un texto de respuesta válido
    retorna una lista de enteros

    Given: (Dado) un patch de la funcion request, para mocker una respuesta
    When: (Cuando) se llama a la funcion get_prices_list
    Then: (Entonces) la respuesta es transformada a una lista de enteros

    """
    response = Mock(status_code=200, text="7\n10\n5\n8")
    mock_request.return_value = response

    assert get_prices_list() == [7, 10, 5, 8]


def test_get_prices_converts_to_int_using_request_mock():
    """Verifica que la funcion get_prices_list ante un texto de respuesta válido
    retorna una lista de enteros, usando request_mock en lugar de patchear todo
    request.

    Given: (Dada) que mockeamos la peticion con request_mock
    When: (Cuando) se llama a la funcion get_prices_list
    Then: (Entonces) la respuesta es transformada a una lista de enteros

    Note: En este caso el mock es contruido solo y además es más fácil mockear
        la url especifica que queresmos. Este test también estaría verificando que
        la función llama a la url especificada.
    """
    with requests_mock.Mocker() as request_mock:
        request_mock.get(
            'https://www.random.org/integers/?num=10&min=1&max=100&col=1&base=10&format=plain&rnd=new',
            text="7\n10\n5\n8"
        )
        assert get_prices_list() == [7, 10, 5, 8]
