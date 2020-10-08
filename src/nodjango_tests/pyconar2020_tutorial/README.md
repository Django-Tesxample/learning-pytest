# Tutorail Pytest (PyconAr 2020)

## Proposito
El siguiente tutorial esta basado en la charla dada en la [PyconAr2020](http://ponerlink.com). 
El propósito de la misma es hablar un poco de las problemáticas a la hora de hacer test, otro poco sobre la gama de cosas que uno puede llegar a encontrarse al iniciar la práctica de testear y mostrar a partir de un ejemplo sencillo algunas de las herramientas disponibles. En este documento
mostaremos directamente la parte practica de la charla.

## Testeando
Bueno como en cualquier lenguaje nuevo que aprendemos escribimos un *hola mundo*, para aprender a testar también podes hacer algo parecido. Iniciemos con una función sin demasiada utlidad y luego pasemos a testearla.

```python {.line-numbers}
from services import get_prices_list


def get_min_value(sort_function, values):
    """Retorna el mínimo valor de una lista basado
    en un funcion de orden.
    """
    ordered = sort_function(values)
    return ordered[0]


def get_min_price():
    """Retorna el mínimo precio de una lista de precios obtenida desde
    un servicio
    """
    prices = get_prices_list()
    min_price = get_min_value(sorted, prices)
    return min_price

```
La función principal es ```get_min_price```, esta obtiene desde un servicio una lista de enteros, que para nosotros representan precios, luego
llama a la función ```get_min_value``` y retorna el valor devuelto como 
el mínimo precio.