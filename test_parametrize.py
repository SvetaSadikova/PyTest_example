import pytest


@pytest.mark.parametrize('a, b, result', [
        (1, 2, 3),
        (2, 5, 9),
        (100, 200, 301)
])
def test_sum(a, b, result):
    assert a + b == result, "Результат сложения не совпадает"