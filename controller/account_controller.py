from flask import Blueprint
from service.account_service import AccountService
from exception.user_not_found import UserNotFoundError

ac = Blueprint("account_controller", __name__)


@ac.route("/accounts")
def get_all_accounts():
    return AccountService.get_all_accounts()


@ac.route("/customers/<customer_id_num>/accounts")
def get_customer_account(customer_id_num):
    try:
        print(f"From controller layer: passing to service layer: /customers/<customer_id_num>/accounts")
        return AccountService.get_customer_account(customer_id_num)
    except UserNotFoundError as e:
        return {
                   "message": str(e)
               }, 404



