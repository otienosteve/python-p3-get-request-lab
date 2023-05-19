#  write your solution here
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from .models.employee import Employee, session

app= FastAPI()

class EmployeeSch(BaseModel):
    id : int
    first_name : str
    last_name : str
    email : str
    age : int
    gender : str
    phone_number : int
    salary : int 
    designation : str

    class Config:
        orm_mode=True

@app.get('/')
def root() -> List[EmployeeSch]:
    employees = session.query(Employee).all()

    return employees

@app.get('/employee/{employee_id}')
def employee(employee_id: int):
    single = session.query(Employee).filter_by(id = employee_id).first()
    return single



