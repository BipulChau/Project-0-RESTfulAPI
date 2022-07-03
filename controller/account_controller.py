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
        query_param = request.args
        if not query_param:  # check if there are any query parameter
            try:
                return AccountService.get_customer_account(customer_id_num)
            except UserNotFoundError as e:
                return {
                           "message": str(e)
                       }, 404
        try:
            return AccountService.get_customer_account_with_query_params(customer_id_num, query_param)  # when query params is truthy
        except UserNotFoundError as e:
            return {
                "message": str(e)
            }, 404

    data = request.get_json()  # Create a new account for a customer with id of X. This block of code executes when flask.request.method == "POST"
    return AccountService.add_customer_account(customer_id_num, data)
