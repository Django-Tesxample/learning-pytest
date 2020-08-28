import logging
import pytest
import time


@pytest.fixture(scope='class')
def person_data():
    time.sleep(1)
    logging.info('Calling person_data fixture')
    return {'first_name': 'Juan', 'last_name': 'Lee'}


class Test1:
    def test_check_first_name(self, person_data):
        assert person_data.get('first_name') == 'Juan'

    def test_check_last_name(self, person_data):
        assert person_data.get('last_name') == 'Lee'


class Test2:
    def test_check_first_name(self, person_data):
        assert person_data.get('first_name') == 'Juan'

    def test_check_last_name(self, person_data):
        assert person_data.get('last_name') == 'Lee'
