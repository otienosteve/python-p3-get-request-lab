import pytest
from ..main import app
from fastapi.testclient import TestClient
from fastapi import status

@pytest.fixture(scope='session')
def client():
    return TestClient(app)

def test_root(client: TestClient):
    res = client.get('/')
    assert res.status_code == status.HTTP_200_OK, "unsuccesful request"
    assert res.json() == {"message" : "Welcome to Kenya"} , "Unexpected json response"

def test_students(client: TestClient):
    res =client.get('/students')