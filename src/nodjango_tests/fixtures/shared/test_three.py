import logging
import pytest


@pytest.fixture
def data_from_file():  # re-define fixture
    logging.info('Calling local data_from_file fixture!!!!')
    return {'ids': ['a']}


def test_check_values(data_from_file):
    assert 'ids' in data_from_file
    assert data_from_file.get('ids') == ['a']
