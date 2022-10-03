import pytest
import requests
from voluptuous import Schema
from pytest_voluptuous import S

schema = Schema(
    {
        'data': {
            'id': int,
            'email': str,
            'first_name': str,
            'last_name': str,
            'avatar': str
        },
        'support': {
            'url': str,
            'text': str
        }
    }
)

def test_list_users():
    response = requests.get('https://reqres.in/api/users?page=2', verify=False)
    assert response.json()['page'] == 2
    assert isinstance(response.json()['page'], int)


def test_single_user():
    response = requests.get('https://reqres.in/api/users/2', verify=False)
    body = response.json()
    body_data = response.json()['data']
    try:
        assert response.json()['data']['first_name'] == 'Janet'
    except AssertionError:
        assert_error = True

    try:
        assert isinstance(response.json()['data']['first_name'], int)
    except AssertionError:
        assert_error = True

    if assert_error:
        raise AssertionError


def test_single_user_schema_validation():
    response = requests.get('https://reqres.in/api/users/2', verify=False)
    assert S(schema) == response.json()


