import flask
from flask import Blueprint, request
from dao.customer_dao import CustomerDao
from service.customer_service import CustomerService

cc = Blueprint("customer_controller", __name__)


@cc.route("/")
@cc.route("/home")
@cc.route("/index")
def get_home_page():
    return "Oggy App - One stop to get all the details about customers, create accounts and update customers & account info !!! "


@cc.route("/customers", methods=["GET", "POST"])
def get_all_customers():
    if flask.request.method == "POST":
        data = request.get_json()
        print(f"Data at controller layer: {data}")
        print(type(data))
        return CustomerService.add_customer(data)
    else:
        return {
            "customers": CustomerService.get_all_customers()
        }


@cc.route("/customers/<id_num>", methods=["GET", "PUT", "DELETE"])
def get_customer_by_id(id_num):
    if flask.request.method == "GET":
        print(f"Searching details of customer {id_num} at controller layer")
        return CustomerDao.get_customer_by_id(id_num)
    elif flask.request.method == "PUT":
        return "PUT at DAO"
    else:
        return "DELETE at DAO"

# app = Flask
# app = Flask(__name__)
#
# customers_db = {
#     "1": {
#         "name": "Bipul Chaudhary",
#         "address": "33 S Kings way",
#         "tel_num": "947-333-3367",
#         "account": [
#             {"account_type": "saving account",
#              "is_open": True,
#              "balance": 5000},
#             {"account_type": "checking account",
#              "is_open": True,
#              "balance": 10000.00
#              }
#         ]
#     },
#     "2": {
#         "name": "Pramesh Pradhan",
#         "address": "14 Toll View",
#         "tel_num": "984-177-8899",
#         "account": [
#             {"account_type": "saving account",
#              "is_open": True,
#              "balance": 5000.00},
#             {"account_type": "checking account",
#              "is_open": True,
#              "balance": 2000.00
#              }
#         ]
#     }
# }
#
#
# @app.route('/')
# @app.route('/home')
# @app.route('/index')
# def home():
#     return "Welcome to MyBank : Fast, Friendly & Accurate Service", 200
#
#
# @app.route('/customers')
# def customer_details():
#     all_customers = []
#     for key in customers_db:
#         customer_individual = {customers_db[key]["name"]:
#                                    {"customer_id": key,
#                                     "address": customers_db[key]["address"],
#                                     "tel_num": customers_db[key]["tel_num"],
#                                     "account": customers_db[key]["account"]}
#                                }
#         all_customers.append(customer_individual)
#     return {
#                "customers": all_customers
#            }, 200
#
#
# @app.route("/customers/<customer_id>")
# def get_customer_by_customer_id(customer_id):
#     if customer_id in customers_db:
#         return {customers_db[customer_id]["name"]:
#                     {"customer_id": customer_id,
#                      "address": customers_db[customer_id]["address"],
#                      "tel_num": customers_db[customer_id]["tel_num"],
#                      "account": customers_db[customer_id]["account"]}
#                 }, 200
#     else:
#         return f"Account with customer id {customer_id} could not be found", 404
#
#
# @app.route("/customers", methods=['POST'])
# def create_profile():
#     data = request.get_json()
#     print(data["customer_id"])
#     if data["customer_id"] in customers_db:
#         return "Profile already exists!!! Cannot create a new Profile", 400
#     else:
#         customers_db[data["customer_id"]] = {"name": data["name"],
#                                              "address": data["address"],
#                                              "tel_num": data["tel_num"],
#                                              "account": []
#                                              }
#         return {"name": data["name"],
#                 "customer_id": data["customer_id"],
#                 "address": data["address"],
#                 "tel_num": data["tel_num"],
#                 "account": []
#                 }, 200
#
#
# @app.route("/customers/<customer_id>/account")
# def get_all_accounts_of_customer(customer_id):
#     if customer_id not in customers_db:
#         return f"Customer with id {customer_id} does not exist", 404
#
#     # GET /customer/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300:
#     # Get all accounts for customer id of X with balances between Y and Z (if customer exists)
#     args = request.args
#     balance = args.getlist('balance')
#     print(balance)
#
#     if balance:
#         maximum_balance = int(balance[0][1::])
#         minimum_balance = int(balance[1][1::])
#         print(maximum_balance, minimum_balance)
#         account_with_balance = []
#         if not customers_db[customer_id]["account"]:
#             return f"For customer with id {customer_id} accounts not opened yet"
#         for account in customers_db[customer_id]["account"]:
#             if minimum_balance < account["balance"] < maximum_balance:
#                 account_with_balance.append(account)
#         if account_with_balance:
#             return {"account": account_with_balance}, 200
#         return f"There are no accounts for customer id {customer_id} with balances between {minimum_balance} and {maximum_balance}."
#
#     return {"name": customers_db[customer_id]["name"],
#             "account": customers_db[customer_id]["account"]
#             }
#
#
# if __name__ == "__main__":
#     app.run(debug=True, port=3135)
