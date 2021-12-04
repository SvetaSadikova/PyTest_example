import os
import random

import pytest

folder = 'new_folder'


# @pytest.fixture(scope="function")
# def create_folder():
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#
#
# def test_created(create_folder):
#     assert os.path.exists(folder), 'folder not exist'
#
#
# def test_created_2(create_folder):
#     assert os.path.exists(folder), 'folder not exist'


@pytest.fixture(scope='session')
def get_rand_num():
    num = random.randint(1, 100)
    print(num)
    return num


def test_rand_number(get_rand_num):
    assert 0 < get_rand_num <= 100


def test_rand_number_2(get_rand_num):
    assert 0 < get_rand_num <= 100


class TestRandNumber:
    def test_rand_number_2(self, get_rand_num):
        assert 0 < get_rand_num <= 100

    def test_rand_number_4(self, get_rand_num):
        assert 0 < get_rand_num <= 100
