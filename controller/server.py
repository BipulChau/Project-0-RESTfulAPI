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
    all_customers = []
    for key in customers_db:
        customer_individual = {customers_db[key]["name"]:
                                   {"customer_id": key,
                                    "address": customers_db[key]["address"],
                                    "tel_num": customers_db[key]["tel_num"],
                                    "account": customers_db[key]["account"]}
                               }
        all_customers.append(customer_individual)
    return {
               "customers": all_customers
           }, 200


@app.route("/customers/<customer_id>")
def get_customer_by_customer_id(customer_id):
    if customer_id in customers_db:
        return {customers_db[customer_id]["name"]:
                    {"customer_id": customer_id,
                     "address": customers_db[customer_id]["address"],
                     "tel_num": customers_db[customer_id]["tel_num"],
                     "account": customers_db[customer_id]["account"]}
                }, 200
    else:
        return f"Account with customer id {customer_id} could not be found", 404


if __name__ == "__main__":
    app.run(debug=True, port=3133)
