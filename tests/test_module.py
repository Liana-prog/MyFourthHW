import pytest
import requests


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def st_code(request):
    return request.config.getoption("--status_code")


def test_module(url, st_code):
    response = requests.get(url)
    assert response.status_code == int(st_code)
