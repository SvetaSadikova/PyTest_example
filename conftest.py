import pytest


@pytest.fixture(scope='session')
def start():
    print('Start fixture')
    yield 1
    print('End test')