import pytest
from ..main import app, Employee
from fastapi.testclient import TestClient
from fastapi import status


@pytest.fixture(scope='session')
def client():
    return TestClient(app)

def test_schema()-> None:
    emp = Employee(first_name="Donald", last_name='Knuth', age=24, salary=43000, phone_number=254712345678, email='donaldknuth@gmail.com', designation='It Dept')
    # last_name , firs_tname, email, age, phone_number, salary, designation
def test_root(client: TestClient):
    res = client.get('/')
    assert res.status_code == status.HTTP_200_OK, "unsuccesful request"
    assert res.json() == {"message" : "Welcome to Kenya"} , "Unexpected json response"

    
def test_students(client: TestClient):
    res = client.get('/students')
    assert res.status_code == status.HTTP_404__not_found