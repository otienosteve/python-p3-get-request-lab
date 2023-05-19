## Practice creating Get requests with FastApi Lab
### Instructions

Inside the lib folder you will find a file main.py where you are expected to write your solution. 

To test if your solution is working run ` pytest `



Create an Employee Schema With the following fields.
This should be the Base Schema for the employee data type you will be working with. 

```last_name -> String 
firs_tname -> String 
email -> String 
age -> Integer
phone_number -> Integer 
salary -> Integer
designation -> String
```

implement the following endpoints 
- `GET /employees`: returns an array of JSON objects for all employees present in the database.
- `GET /employees/:id`: returns a single student as JSON object
- `GET /employees/salary/asc`: returns an array of employees from highest paid to lowest Paid
- `GET /employees/age/old`: returns the oldest employee as an object



