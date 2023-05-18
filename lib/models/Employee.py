from flask_sqlalchemy  import create_engine, Column, String, Integer, Float 
from sqlalchemy.orm import declarative_base, session

Base= declarative_base()


class Employee():
    first_name = Column(String)