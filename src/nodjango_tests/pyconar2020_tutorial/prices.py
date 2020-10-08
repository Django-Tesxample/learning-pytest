from nodjango_tests.pyconar2020_tutorial.services import get_prices_list


def get_first_value(sort_function, values):
    """Retorna el primer valor de una lista luego de
    ordenarla con la funcion de orden pasada
    """
    ordered = sort_function(values)
    return ordered[0]


def get_min_price():
    """Retorna el minimo precio de una lista de precios obtenida desde
    un servicio
    """
    prices = get_prices_list()
    min_price = get_first_value(sorted, prices)
    return min_price


def get_min_price_bad():
    """Mal ejemplo de totalización de función en caso de error
    """
    prices = get_prices_list()
    try:
        min_price = get_first_value(sorted, prices)
    except IndexError:
        return 0

    return min_price
