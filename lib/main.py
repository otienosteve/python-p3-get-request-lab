#  write your solution here
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from .models.employee import Employee, session

app= FastAPI()

class EmployeeSchema():
    id : int
    first_name : str
    last_name : str
    email : str
    age : str
    gender : str
    phone_number : str
    salary :str
    designation = str

    class Config:
        orm_mode=True

@app.get('/')
def root() -> List[EmployeeSchema]:
    employees = session.query(Employee).all()

    return employees



