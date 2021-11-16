import pytest
import requests
import random

HOST = 'https://jsonplaceholder.typicode.com/'
R_WITH_NUMBER_OF_RETURNS = [("posts", 100), ("comments", 500), ("albums", 100),
                                    ("todos", 200),
                                    ("photos", 5000), ("users", 10)]
LIST_OF_GET = ['posts', 'posts/1', 'posts/1/comments', 'comments?postId=1']

@pytest.mark.parametrize('resource,number_of_returns', R_WITH_NUMBER_OF_RETURNS)
def test_resources(resource, number_of_returns):
    response = requests.get(HOST + resource)
    assert response.status_code == 200
    assert len(response.json()) == number_of_returns

def test_creating_resource():
    response = requests.post(HOST + 'posts', {"title": "foo",
                                              "body": "bar", "userId": 1})
    assert response.status_code == 201
    assert "title" and "body" and "userId" and "id" in (response.json())

def test_deleting_a_resource():
    response = requests.delete(HOST + 'posts/15')
    assert response.status_code == 200
    assert not response.json()

def test_updating_resource():
    response = requests.put(HOST + 'posts/1', {"id": 1,
                                               "title": "test", "body": "tester",
                                               "userId": 1})
    print((response.json().get("title")))
    assert response.status_code == 200
    assert (response.json().get("title")) == "test"
    assert (response.json().get("body")) == "tester"

@pytest.mark.parametrize('page', LIST_OF_GET)
def test_get_pages(page):
    response = requests.get(HOST + page)
    assert response.status_code == 200
