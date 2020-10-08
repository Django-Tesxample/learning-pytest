# Tutorial Pytest (PyconAr 2020)

## Propósito
El siguiente tutorial esta basado en la charla dada en la [PyconAr2020](http://ponerlink.com). 
El propósito de la misma es hablar un poco de las problemáticas a la hora de hacer test, otro poco sobre la gama de cosas que uno puede llegar a encontrarse al iniciar la práctica de testear y mostrar a partir de un ejemplo sencillo algunas de las herramientas disponibles. En este documento
mostaremos directamente la parte práctica de la charla. No aesguramos que este documento sea autocontenido y en cualquier caso es recomendable mirar la charla.

## Testeando
Bueno como en cualquier lenguaje nuevo que aprendemos escribimos un *hola mundo*, para aprender a testar también podemos hacer algo parecido. Iniciemos con una función sin demasiada utlidad y luego pasemos a testearla.

```python
# nodjango_tests/pyconar2020_tutorial/prices.py

from nodjango_tests.pyconar2020_tutorial.services import get_prices_list


def get_first_value(sort_function, values):
    """Retorna el primer valor de una lista luego de
    ordenarla con la función de orden pasada
    """
    ordered = sort_function(values)
    return ordered[0]


def get_min_price():
    """Retorna el mínimo precio de una lista de precios obtenida desde
    un servicio
    """
    prices = get_prices_list()
    min_price = get_first_value(sorted, prices)
    return min_price

```
La función principal es ```get_min_price```, esta obtiene desde un servicio una lista de enteros, que para nosotros representan precios, luego
llama a la función ```get_first_value``` y retorna el valor devuelto como 
el mínimo precio.

Iniciemos testeando la función ```get_first_value``` que es utilizada por la función principal. Claramente uno no puede siempre testear todo, y en general tampoco es la idea, pero según nuestro entender por cada funcionalidad que uno escribe, idelamente debería pensar en testear las siguientes tres premisas:

* Funcionalidad: la función calcula lo que espero, para esto definimos algún/os casos normales muy específicos y los chequeamos (evitar replicar lógica de la función dentro del test).
* Comportamiento: como no modelamos lo que se supone que no debe suceder hay casos en los que mi función debe retornar una excepción y es bueno saber que nuestra función falle cuando tiene que fallar.
* Utilidad: nuetra función es llamada cuando se necesita. Lo normal es que las funciones que escribimos sean llamadas desde algún otro lugar, y eso es parte de la lógica del dominio que también podemos testear.

pasemos ahora si a los test escritos

```python
# nodjango_tests/pyconar2020_tutorial/tests/test_prices.py
import pytest
from nodjango_tests.pyconar2020_tutorial.prices import get_first_value


def test_get_first_value_returns_min():
    prices_list = [8, 3, 5, 7, 6]
    assert 3 == get_first_value(sorted, prices_list)


def test_get_first_value_except_on_empty_list():
    prices_list = []
    with pytest.raises(IndexError):
        get_first_value(sorted, prices_list)

```
Es fácil notar que el primer test ```test_get_first_value_returns_min``` esta verificando la funcionalidad para un caso muy especifico, y el siguiente test 
```test_get_first_value_except_on_empty_list```, verifica que la función falla
cuando uno espera. O sea no se debería llamar a una función que retorna el primer elemento de una lista, con un lista vacia. Notar que en este caso estamos haciendo abuso de la función ```sorted```, pero nuestra función ```get_first_value``` podría ser llamada con cualquier lista y con cualquier función de orden, particularmente nosotros lo estamos usando de una forma muy rara para obtener el mínimo valor de una lista, por ejemplo el próximo test fallaría

```python
def test_get_first_value_fails():
    prices_list = ['100', '90', '400']
    assert '90' == get_first_value(sorted, prices_list)
```
no por que get_first_value este mal, sino por la forma en que la utilizamos (recordemos que la funcionalidad no es retornar el mínimo valor, sino tan solo el primer elemento luego de aplicar la función de orden), en cambio si hicieramos la misma llamada cambiando la función de orden como se muestra a continuación el mismo test estaría pasando.

```python
def test_get_first_value_returns_min_on_string_numbers():
    def sort_string_numbers(string_numbers):
        return sorted(string_numbers, key=lambda x: int(x))

    prices_list = ['100', '90', '400']
    assert '90' == get_first_value(sort_string_numbers, prices_list)
```
Lo único que nosotro deberiamos poder asegurar de la función de orden es que nos retorna la lista de elementos en otro orden, y como no es una función nuestra, tampoco deberiamos testearla. Aca es donde aparece la necesidad de Mock.

### Mock y MagicMock

```python
from unittest.mock import Mock


def test_get_first_value_returns_ordered_first():
    prices_list = [8, 3, 5, 7, 6]
    mock_sort_function = Mock(return_value=[3, 5, 6, 7, 8])
    assert 3 == get_first_value(mock_sort_function, prices_list)
```

Uno podría plantearse para que usamos la clase Mock o MagicMock si directamente podemos hacer algo de la siguiente pinta:

```python
def test_get_first_value_returns_ordered_first():
    prices_list = [8, 3, 5, 7, 6]
    assert 3 == get_first_value(lambda :[3, 5, 6, 7, 8], prices_list)
```
Es verdad que en este caso con ```lambda``` podemos representar un buen mock de la función de orden, pero la librería mock nos provee un montón de herramientas más, muchas de las cuales sirven para ayudarnos a mockear objetos y funciones mas complicados y otras para testear como son usados esos objectos y funciones que mockeamos. En el siguiente ejemplo podemos ver como a partir del mismo mock, en nuestro test podemos corroborar que la función de orden es llamada, y que es llamada con los parámetros que esperamos.

```python
def test_get_first_value_returns_ordered_first():
    prices_list = [8, 3, 5, 7, 6]
    mock_sort_function = Mock(return_value=[3, 5, 6, 7, 8])
    assert 3 == get_first_value(mock_sort_function, prices_list)
    assert mock_sort_function.call_count == 1
    # verificamos que se llama a la funcion de orden con la lista incial
    mock_sort_function.assert_called_with(prices_list)
```

Otros ejemplos de funciones que nos provee mock son:
* assert_called: chequea que fue llamado.
* assert_called_once: chequea que fue llamado solo una vez.
* assert_called_once_with: chequea que fue llamado solo una vez y con los parámetros especificados.
* assert_called_with: chequea que fue llamado con los parámetros especificados
* assert_has_calls: chequea llamados desde una lista de llamados
* assert_not_called: chequea que no se llama
* etc

En todos los ejemplos anteriores podriamos haber usado MagicMock en lugar de Mock, la gran diferencia entre estas dos clases es que MagicMock tiene implementaciones por defecto de los magic methods. Luego el uso debería ser por necesidad y criterio de cada uno.

Ahora estaría faltando la última premisa, que es ver que nuestra función es usada donde corresponde, para algo la escribimos. Volvamos la función desde la cual usamos ```get_first_value```

```python
def get_min_price():
    """Retorna el mínimo precio de una lista de precios obtenida desde
    un servicio
    """
    prices = get_prices_list()
    min_price = get_first_value(sorted, prices)
    return min_price
```

Si recordamos, en el último test que hicimos de ```get_first_value```, pudimos mockear la función ```sorted```, verificar que se usaba, y como se usaba dentro de nuestra función muy fácilmente. Esta facilidad radica en que ```get_first_value``` recibe la función de ordenamiento como parámetro. Luego sencillamente pasamos nuestro mock como parámetro y listo. Pero en el caso de la función ```get_min_price```, no recibe ningún parametro y hace uso de nuesra funcion ```get_first_value``` (que ya testeamos y ahora queremos testear que es llamada dentro de esta función), como también hace uso de un servicio que nos retorna una lista de precios, el cual no nos corresponde testear y deberiamos mockearlo también, especialmente siendo un servicio externo sobre el cual no tenemos gobernanza. Pero como hacemos para reemplaza estas funciones en nuestro test por mocks que controlemos. Aca es donde aparece Patch.

### Patch
Patch
