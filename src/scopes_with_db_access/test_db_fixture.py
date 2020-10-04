"""
La idea de este módulo es mostrar como falla un test cuyo fixture tiene mal
configurado su scope. En este caso, el fixture foobar_user tiene un scope
module pero usa un fixture (db) con scope menor (function) por lo que el test
arroja el siguiente error:

ScopeMismatch: You tried to access the 'function' scoped fixture 'db' with
a 'module' scoped request object

Además se muestra otro error comun al tratar de acceder a la DB desde un
fixture sin usar el fixture db. Esto tira el siguiente error:

RuntimeError: Database access not allowed, use the "django_db" mark, or
the "db" or "transactional_db" fixtures to enable it
"""

import sys

import pytest
from django.contrib.auth import get_user_model


# Primer error comun

@pytest.fixture(scope='module')
def foo_user(db, django_user_model):
    return django_user_model.objects.create(username='foo')


@pytest.mark.skipif('failing' not in sys.argv,
                    reason="test using invalid fixture")
@pytest.mark.failing
def test_failing_with_scope_mismatch(foo_user, django_user_model):
    assert django_user_model.objects.get(username='foo') == foo_user


# Segundo error comun

@pytest.fixture(scope='module')
def bar_user():
    return get_user_model().objects.create(username='bar')


@pytest.mark.skipif('failing' not in sys.argv,
                    reason="test using invalid fixture")
@pytest.mark.failing
def test_failing_with_access_not_allowed(bar_user, django_user_model):
    assert django_user_model.objects.get(username='bar') == bar_user
