Create an Employee With the following Schema

```last_name -> String 
firs_tname -> String 
email -> String 
age -> Number
phone_number -> Number 
salary -> Float
designation -> String
```


Implement a route that responds to a get request on the following endpoint '/employees' 
the method should return an array of employees present in the Database. 


- `GET /employees`: returns an array of JSON objects for all employees present in the database.
- `GET /employees/:id`: returns a single student as JSON object
- `GET /employees/paygrade`: returns an array of employees from highest paid to lowest Paid
- `GET /employees/oldest`: returns the oldest employee as an object



