# Project0: RESTful API

## Description:  
It's a simple API for a bank. It is created using Python programming language and supports 2 main resources: customers and banks.

## Technologies
1. Python
2. Flask
3. Psycopg
4. Pytest
5. PostgreSQL
6. MagicMock

## Postman
Use Postman to check the various endpoints. Also use the below data format while sending POST and PUT Request.

## URI and POST/PUT Data Format:
### A. Accounts:
1. GET All accounts of all the customers: http://127.0.0.1:8080/accounts 

2. Get the account details of a customer: http://127.0.0.1:8080/customers/<customer_id>/accounts. 
Query parameters are “amountLessThan” and “amountGreaterThan”

3. (POST) Add/open a new account of a customer: http://127.0.0.1:8080/customers/<customer_id>/accounts 

{
    "account_type_id": 1,
    "balance": 21000
       }

4. Get details of individual account of a customer: http://127.0.0.1:8080/customers/<customer_id>/accounts/<account_no>

5. (PUT) Update balance of a customer in an account: http://127.0.0.1:8080/customers/<customer_id>/accounts/<account_no>

{
    "balance": 1015
       }

6. Delete an account of a customer: http://127.0.0.1:8080/customers/<customer_id>/accounts/<account_no>

### B. Customers:

1. GET all customer Details : http://127.0.0.1:8080/customers

2. (POST) Add a new customer: http://127.0.0.1:8080/customers

{
            "address": "Toronto, CA",
            "id_num": "MADY24",
            "mobile_phone": "612-561-8977",
            "name": "Madhu Chaudhary"
          
        }

3.  GET Details of an individual customer: http://127.0.0.1:8080/customers/<id_num>

4. (PUT) Update an individual customer: http://127.0.0.1:8080/customers/<id_num>	

{
            "address": "Toronto, CA",
            "id_num": "MADY24",
            "mobile_phone": "612-561-8977",
            "name": "Madhu Chaudhary"
          
        }
        
5.  Delete a customer: http://127.0.0.1:8080/customers/C<id_num>

