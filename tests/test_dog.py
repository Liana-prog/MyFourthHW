import pytest
import requests
import random

HOST = 'https://dog.ceo/api'
INVALID_VALUE = 'https://dog.ceo/ap'
LIST_ALL_BREEDS = '/breeds/list/all'
RANDOM_IMAGE = '/breeds/image/random'
BY_BREED = '/breed/hound/images'
LIST_OF_BREEDS = list(dict.keys((requests.get(
    HOST + LIST_ALL_BREEDS)).json().get('message')))


def test_invalid_page():
    response = requests.get(HOST + INVALID_VALUE)
    assert response.status_code == 404


@pytest.mark.parametrize("page", [LIST_ALL_BREEDS, RANDOM_IMAGE])
def test_status_code_200(page):
    response = requests.get(HOST + page)
    assert response.status_code == 200


@pytest.mark.parametrize("page", [LIST_ALL_BREEDS, RANDOM_IMAGE])
def test_success(page):
    response = requests.get(HOST + page)
    status = response.json().get('status')
    assert status == "success"


@pytest.mark.parametrize('breed', LIST_OF_BREEDS)
def test_random_image_breeds_list(breed):
    response = requests.get(HOST + '/breed/' + breed + '/images/random')
    assert response.status_code == 200


def test_number_random_dog_images():
    random_number = random.choice(range(1, 51))
    response = requests.get(HOST + '/breed/' + random.choice(LIST_OF_BREEDS)
                            + '/images/random/' + str(random_number))
    number_of_results_in_response = len(response.json().get('message'))
    assert number_of_results_in_response == random_number
