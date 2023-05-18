#  write your solution here
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Employee():
    pass

@app.get('/')
def root() -> None:
    return {"message" : "success"}
