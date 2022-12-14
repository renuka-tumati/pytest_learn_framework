import pytest
from _pytest.python import Metafunc


def test_compute(param1, param2):
    assert param1 < 100


def test_compute2(param2, param1):
    assert param2 < 100


def range_list():
    return range(2)


def pytest_generate_tests(metafunc):

    if "param2" in metafunc.fixturenames or "param1" in metafunc.fixturenames:
        metafunc.parametrize("param1", range_list())
        metafunc.parametrize("param2", range(5))


@pytest.fixture
def fixt(request):
    print(request.param)
    return request.param * 3


@pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
def test_indirect(fixt):
    assert fixt == "aaa"
