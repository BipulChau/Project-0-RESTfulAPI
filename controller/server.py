from flask import Flask, request

app = Flask(__name__)

customers_db = {
    "1": {
        "name": "Bipul Chaudhary",
        "address": "33 S Kings way",
        "tel_num": "947-333-3367",
        "account": [
            {"account_type": "saving account",
             "is_open": False,
             "balance": None},
            {"account_type": "checking account",
             "is_open": True,
             "balance": 10000.00
             }
        ]
    },
    "2": {
        "name": "Pramesh Pradhan",
        "address": "14 Toll View",
        "tel_num": "984-177-8899",
        "account": [
            {"account_type": "saving account",
             "is_open": True,
             "balance": 5000.00},
            {"account_type": "checking account",
             "is_open": True,
             "balance": 2000.00
             }
        ]
    }
}


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return "Welcome to MyBank : Fast, Friendly & Accurate Service", 200


@app.route('/customers')
def customer_details():
    print(type(customers_db))

    return customers_db, 200


#
#
# @app.route('/customers/', methods=['POST'])
# def customers():
#     return "Creates a new customer", 201
#

# @app.route('/customer/<customer_id>')
# def customer(customer_id):
#     return "Get customer with an id, if the customer exists", 200
#
#
# @app.route('/customer/<customer_id>', methods=['PUT'])
# def customer_id(customer_id):
#     return "Update customer with an id, if the customer exists"
#

if __name__ == "__main__":
    app.run(debug=True, port=3133)
