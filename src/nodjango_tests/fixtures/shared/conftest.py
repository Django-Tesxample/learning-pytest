import logging
import pytest
import time


@pytest.fixture(scope='package')
def data_from_file():
    logging.info('Calling data_from_file fixture')
    return {'values': [1, 2, 3]}
