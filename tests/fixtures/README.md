# Pytest fixture


## Scopes

Fixtures set up a test context satisfying any preconditions the test can have.

Pytest handle fixtures as dependency injections, making them easy to use and maintain.

Sometimes fixtures are time-expensive to create (i.e: smtp connection, file, etc) so pytest
has fixture scopes to re-use them through different tests. The available scopes are:
- function (default)
- class
- module
- package
- session



### Useful links

* https://docs.pytest.org/en/stable/fixture.html
