import pytest
from ..main import app, Employee
from fastapi.testclient import TestClient
from fastapi import status
from ..models.employee import Employee, session

@pytest.fixture(scope='session')
def data() -> None:
    employees = session.query(Employee).all()
    return employees

@pytest.fixture(scope='session')
def client():
    return TestClient(app)

def test_schema()-> None:
    pass
    # emp = Employee(first_name="Donald", last_name='Knuth', age=24, salary=43000, phone_number=254712345678, email='donaldknuth@gmail.com', designation='It Dept')
    # last_name , firs_tname, email, age, phone_number, salary, designation

def test_root(client: TestClient, data: data):
    res = client.get('/')
    assert res.status_code == status.HTTP_200_OK, "unsuccesful request"
    assert res.json() == data
    
    
def test_students(client: TestClient):
    res = client.get('/students')
    assert res.status_code == 404