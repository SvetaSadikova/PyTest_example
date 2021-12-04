import pytest

"pytest -v -m my_marker"
"pytest -v -m smoke_test"


@pytest.mark.smoke_test
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.smoke_test
def test_failed():
    assert (1, 2, 3) == (3, 2, 1)


@pytest.mark.my_marker
def test_my_mark():
    text = 'Test'
    assert len(text) == 4


@pytest.mark.xfail(reason='must be four')
def test_mark_fail():
    text = 'Test'
    assert len(text) == 6


@pytest.mark.skip(reason='must be four')
def test_mark_skip():
    text = 'Test'
    assert len(text) == 5


@pytest.mark.skipif(10 > 1, reason='Because 10 > 1')
def test_mark_skipif():
    text = 'Test'
    assert len(text) == 5


def test_mark_k_test():
    text = 'Test'
    assert len(text) == 4
