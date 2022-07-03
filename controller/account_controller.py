import flask
from flask import Blueprint, request
from service.account_service import AccountService
from exception.user_not_found import UserNotFoundError

ac = Blueprint("account_controller", __name__)


@ac.route("/accounts")
def get_all_accounts():
    return AccountService.get_all_accounts()


@ac.route("/customers/<customer_id_num>/accounts", methods=["GET", "POST"])
def get_customer_account(customer_id_num):
    if flask.request.method == "GET":  # Get all accounts for customer with id
        try:
            print(f"From controller layer: passing to service layer: /customers/<customer_id_num>/accounts")
            return AccountService.get_customer_account(customer_id_num)
        except UserNotFoundError as e:
            return {
                       "message": str(e)
                   }, 404

    data = request.get_json()  # Create a new account for a customer with id of X
    return AccountService.add_customer_account(customer_id_num, data)
