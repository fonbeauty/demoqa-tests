import requests
from pytest_voluptuous import S

from schemas.reqres import schema_single_user


def test_list_users_with_session(reqres_session):
    response = reqres_session.get(url='/users', params={'page': 2})
    assert response.json()['page'] == 2
    assert isinstance(response.json()['page'], int)


def test_single_user(reqres_session):
    response = reqres_session.get(url='/users/2')
    assert response.json()['data']['first_name'] == 'Janet'
    assert isinstance(response.json()['data']['first_name'], str)


def test_single_user_schema_validation(reqres_session):
    response = reqres_session.get(url='/users/2')
    assert S(schema_single_user) == response.json()


def test_single_user_not_found(reqres_session):
    response = reqres_session.get(url='/users/23')
    assert response.status_code == 404


def test_create_user(reqres_session):
    user = {
        'name': 'morpheus',
        'job': 'leader'
    }
    response = reqres_session.post(url='/users', json=user)
    assert response.status_code == 201
    assert response.json()['name'] == 'morpheus'


