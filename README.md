# DjangoTesxample (learning-pytest)

Repositorio de ejemplos documentados de test para Django y Python en general.

## Introducción

La idea de este respositorio es ser exáctamente eso, un repositorio. O sea, en lugar de ser el repositorio de código de un aplicativo, la idea es que este contenga código de ejemplos de diversos casos de test, que se puedan bajar y correr en el mismo. La idea es subir ejemplos típicos de las diversas cosas que habitualmente se necesitan testear (patrones de diseño, testeo de envio de emails, testeo de vistas/formularios de django, armados de mocks para diferentes cosas, etc), y definir una forma de documentar los ejemplos para colaborar con el repo ordenadamente.

Principalmente nos gustaría llegar a cumplir las siguientes metas:
* Definir un flujo y estilo para colaborar con el repo.
    * Toda funcionalidad, modelos o código dentro del repo va a ser especificamente para realizar algún test.
    * Todo los tests tienen que estar documentados como se especificará en la sección [cómo colaborar](#como-colaborar)
    * Cada nuevo módulo (que funcionalmente agrupe cierta categoria de test) dentro del repo debe contener un README en su carpeta principal. 
    * Distitnas personas por mérito o recomendación van  a estar autorizadas para aceptar PRs al repo y/o aclarar correcciones a hacer antes.
* Tener alguna forma de encontrar los test y su documentación fácilmente.
* Que la mayoria de la documentación sea autogenerada desde los docstrings (SPHINX??).
* Tener una sección de articulos con tutoriales o documentaciones mas extensas de ciertas temáticas de test que hagan referencia a código dentro de este mismo repo (O la WIKI?).
* Inicialmente el repo es para la comunidad de habla hispana, pero idealmente (si es que toma forma) se podría poder pensar en traducir a otros idomas.
* ¿Base de todos los test hasta el momento documentados?

## Estilos

* Se intenta que todo el código dentro del repo (al menos el de autor) respete PEP8, se recomienda usar el linter flake8 dentro del IDE. 
* La forma de escribir los docstring va a ser la propuesta por la guia de estilos de [google](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings). 
* (TODO: creo qeu esto tiene otro nombre) El manejo de ramas va a ser un resumen de [git-flow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow). Al no ser un producto solo se va a conservar como rama principal **master**, desde la misma se crearan ramas **feature** y se mergearan a master desde un PR.
* Si el ejemplo desarrollado es extraido de alguna fuente, en el Docstring del mismo, bajo el encabezado *"Sources:"* se deben agregar las fuentes como una lista de markdown, de las misma forma que con *"Args:"* se listan los argumentos de la función.
* Idioma para los docstings???

## Como colaborar

Primero con ganas 😁


### Ejemplo de Docstrings


## Que tenemos hasta ahora
Hay que ver si esta sección es mantenible o solo una utopía, pero la idea es tener una lista al menos a nivel módulo de todo lo que se puede encontrar dentro del repo.
### Tests por tematicas
* [Infraestructura](src/nodjango_tests/infrastructure): Test que tengan realción con algo de infraestructura, actualmente solo hay un test con chequeo de estilos del repo.
* [Servicios externos](src/nodjango_test/external_services): Ejemplos de test y de formas de mocker servicios externos como por ejemplo una petición por request, acceso a una cola sqs de amazon, etc.
* mails: TODO la clave deberia ser un link al README, correspondiente a la carpeta donde esten los test que tienen que ver con procesos con mails

### Tutoriales/Artículos
* [Fixtures y Scopes](src/nodjango_tests/fixtures_tutorial) : Tutorial con ejemplos locales de los diferentes tipos de scopes que pueden tener los fixtures y como funcionan.
* [Introducción a Pytest](src/nodjango_tests/pyconar2020_tutorial) : Tutorial de introduccón a pytest.
