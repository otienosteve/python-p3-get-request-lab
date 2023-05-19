#  write your solution here
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models.employee import Employee, session

app= FastAPI()

class EmployeeSchema(BaseModel):
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
def root() -> List[EmployeeSchema]:
    employees = session.query(Employee).all()

    return employees

@app.get('/employees/{employee_id}')
def employee(employee_id: int) -> EmployeeSchema:
    single = session.query(Employee).filter_by(id = employee_id).first()
    if not single:
        raise HTTPException(status_code=404, detail="Employee does not exist in our databse")
    return single

@app.get('/employees/salary/asc')
def paygrade() -> List[EmployeeSchema]:
    order = session.query(Employee).order_by(Employee.salary.asc()).all()
    return order

@app.get('/employees/age/old')
def oldest()-> EmployeeSchema:
    oldest = session.query(Employee).order_by(Employee.age.desc()).all()[0]
    return oldest 







