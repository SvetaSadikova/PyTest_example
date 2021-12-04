import pytest


@pytest.fixture(scope='session')
def start():
    print('Start fixture')
    yield 1
    print('End test')


def pytest_addoption(parser):
    parser.addoption("--foofoo", action="store", default="bar", help="foo: bar or baz")


@pytest.fixture()
def get_option_my_foo(request):
    return request.config.getoption("--foofoo")
