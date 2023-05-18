from flask_sqlalchemy  import create_engine, Column, String, Integer, Float 
from sqlalchemy.orm import declarative_base, session

Base= declarative_base()


class Employee():
    __tablename__ = 'employees'
    first_name = Column(String)











engine= create_engine()