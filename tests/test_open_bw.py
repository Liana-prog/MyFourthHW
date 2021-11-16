import pytest
import requests
import random

HOST = 'https://api.openbrewerydb.org/breweries'
LIST_OF_SORTING_PARAM = {"by_city": "san_diego", "by_dist": "38.8977,77.0365",
                              "by_name": "cooper",
                              "by_state": "ohio", "by_postal": "44107",
                              "by_type": "brewpub", "per_page": "44"}
LIST_OF_BY_TYPE_PARAM = ['micro', 'nano', 'regional', 'brewpub', 'large',
                              'planning', 'bar', 'contract',
                              'proprietor', 'closed']


@pytest.mark.parametrize('payload', LIST_OF_SORTING_PARAM)
def test_list_breweries_status_code_200(payload):
    response = requests.get(HOST, payload)
    assert response.status_code == 200


def test_get_brewery():
    response = requests.get(HOST + '12432')
    assert response.status_code == 200


def test_number_of_breweries_per_page():
    random_number = random.choice(range(1, 51))
    response = requests.get(HOST, {"per_page": str(random_number)})
    number_of_results_in_response = len(response.json())
    assert number_of_results_in_response == random_number


def test_autocomplete():
    response = requests.get(HOST + "autocomplete", {"query": "dog"})
    assert response.status_code == 200
    assert len(response.json()) == 15
    assert "id" and "name" in (response.json())[0]
    assert len((response.json())[0]) == 2


@pytest.mark.parametrize('by_type_param', LIST_OF_BY_TYPE_PARAM)
def test_by_type(by_type_parameter):
    response = requests.get(HOST, {"by_type": by_type_parameter})
    brewery_type_from_response = (((response.json())[0])['brewery_type'])
    assert response.status_code == 200
    assert brewery_type_from_response == by_type_parameter
