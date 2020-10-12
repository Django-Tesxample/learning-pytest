import logging
import requests
from urllib.parse import urlencode


def get_prices_list():
    """Retrona una lista de 10 numeros enteros obtenidos desde un servicio externo

    Returns:
        list[int]: lista de numeros enteros
    """
    base_service_url = 'https://www.random.org/integers/'
    params = {
        'num': 10,
        'min': 1,
        'max': 100,
        'col': 1,
        'base': 10,
        'format': 'plain',
        'rnd': 'new'
    }
    query_string = urlencode(params)
    url = f'{base_service_url}?{query_string}'

    response = requests.request("GET", url, headers={}, data={})

    if response.status_code != 200:
        response.raise_for_status()

    response_list = response.text.split('\n')
    logging.info(response_list)
    return [int(value) for value in response_list if value != '']
