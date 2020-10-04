# Pytest fixtures con acceso a la base de datos

Para que un test pueda acceder a la BD necesitamos que el test use el pytest mark *django_db*
o alguno de los fixtures *db* o *transactional_db*. Ver todos los detalles en
https://pytest-django.readthedocs.io/en/latest/helpers.html#pytest-mark-django-db-request-database-access


Algo importante a tener en cuenta es que pytest django no permite (hasta el momento, 28/8/2020)
tener fixtures con acceso a la base de datos con scope mayor al default, que es *function*.
Esto se presenta si crean un fixture que accede a la BD. Para ver un ejemplo de qué es lo
que pasa cuando tratamos de crear un fixture con acceso a la base y scope mayor al válido
pueden correr el siguiente comando: `pytest -m failing scopes_with_db_access`

¿En qué impacta esta situación? A diferencia de los tests de Django que permiten
reutilizar datos creados en la BD, en pytest necesariamente hay que recrearlos
luego de cada test. Esto puede tener un impacto negativo en la performance de
nuestros tests. Para evitar este impacto en la performance se pueden usar 3
alternativas:

1. En los casos que se necesite reutilizar datos de la DB, usar los tests
   normales de Django (heredando de TestCase). Ver archivo `test_using_django_testcase.py`
2. Muchas veces se puede evitar el acceso a la DB usando mocks o instancias de
   nuestros modelos no guardadas en la DB. Para que esto no sea tedioso es
   importante que nuestra lógica de negocio no dependa del ORM de django
   sino de iterables. De esta manera es más sencillo mockear o utilizar instancias
   sin guardar en la DB. Ver archivo `test_using_unsaved_objects.py`
3. Si necesitamos que en la DB haya datos cargados para todos los tests, se puede
   crear un fixture especial con scope *session* que ingrese datos a la DB y que
   estarán disponibles durante toda la corrida de tests. Ver estos links:
   1. https://pytest-django.readthedocs.io/en/latest/database.html#populate-the-database-with-initial-test-data
   2. https://pytest-django.readthedocs.io/en/latest/database.html?highlight=django_db_setup#django-db-setup
   3. https://github.com/pytest-dev/pytest-django/issues/243#issuecomment-457956838
