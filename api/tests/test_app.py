from http import HTTPStatus

from fastapi.testclient import TestClient


def test_root_deve_retornar_ok_e_ola_mundo(client: TestClient):
    # Arrange / Given

    # Act / When
    response = client.get('/')

    # Assert / Then
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Bem vindo!'}


def test_create_user(client: TestClient):

    response = client.post(
        '/auth/',
        json={
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client: TestClient):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_delete_user(client):

    response = client.delete('/users/1')

    response.status_code == HTTPStatus.OK
    response.json() == {'menssage': 'user deleted'}
