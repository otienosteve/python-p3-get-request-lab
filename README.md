##  Get requests with FastApi Lab

#### setup 

Fork and clone this repo, then navigate into the cloned folder 

spawn a virtual environment `pipenv shell`

install relevant dependencies `pipenv install`

### Instructions

Here's the directory structure
```
├── lib
│   ├── models
│   │   ├── employee.py
│   ├── test
|   |   |──test_main.py
|   |   |
│   ├── main.py
├── db.db
├── Pipfile
├── Pipfile.lock
|── README.md

```
You will be working on data about Employees.
The Employee Model has been created and is available under  in the models directory under the lib folder, data to work on this lab is available in the database file (db.db). 
Your focus should be on implementing the routes and the associated functionality.

import the session object and the Employee Model from the models package and make use of them when implementing your soltution.   

Inside the lib folder you will find a file `main.py` where you are expected to write your solution. 

This is the Schema for the Employee Model you will be working with. 

```
id: Integer
last_name -> String 
firs_tname -> String 
email -> String 
age -> Integer
gender -> String
phone_number -> Integer 
salary -> Integer
designation -> String
```
Create a corresponding Pydantic class called `EmployeeSchema` for the model and use it to annotate your endpoints as per the return type.

implement the following endpoints and the required functionality.

- `GET /employees`: returns an array of JSON objects for all employees present in the database.
- `GET /employees/:id`: returns a single student as JSON object
    - For the endpoint above implement an exception handler for a non existent entry in the database which should yield the appropriate status code and the message "Employee does not exist in our databse"
- `GET /employees/salary/asc`: returns an array of employees from lowest paid to highest paid
- `GET /employees/age/old`: returns the oldest employee as an object

To run your server run `uvicorn lib.main:app` 
or `uvicorn lib.main:app --reload` to enable reloading on file changes 

To test your solution run ` pytest `

## Resources 

[Get Requests With FastAPI](https://betterprogramming.pub/how-to-create-a-get-request-in-fastapi-ecdc794b0cf)   
[Validation With Pydantic](https://docs.pydantic.dev/latest/usage/validators/)  
[Error Handling in FastAPI](https://fastapi.tiangolo.com/tutorial/handling-errors/)    
[Response Model - Return Type in FastAPI](https://fastapi.tiangolo.com/tutorial/response-model/)    
[Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)   





