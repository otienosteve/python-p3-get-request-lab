Create an Employee Schema With the following fields.
This should be the Base Schema for the employee data type you are dealing with. 

```last_name -> String 
firs_tname -> String 
email -> String 
age -> Integer
phone_number -> Integer 
salary -> Integer
designation -> String
```


Implement a route that responds to a get request on the following endpoint '/employees' 
the method should return an array of employees present in the Database. 


- `GET /employees`: returns an array of JSON objects for all employees present in the database.
- `GET /employees/:id`: returns a single student as JSON object
- `GET /employees/salary/asc`: returns an array of employees from highest paid to lowest Paid
- `GET /employees/age/old`: returns the oldest employee as an object



