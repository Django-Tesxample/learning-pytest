import logging
import pytest


@pytest.fixture  # function scope
def person_data():
    logging.info('Calling person_data fixture')
    return {'first_name': 'Juan', 'last_name': 'Lee'}


def test_check_first_name(person_data):
    assert person_data.get('first_name') == 'Juan'


def test_check_last_name(person_data):
    assert person_data.get('last_name') == 'Lee'
