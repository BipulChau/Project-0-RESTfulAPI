from flask import Blueprint
from service.account_service import AccountService

ac = Blueprint("account_controller", __name__)


@ac.route("/accounts")
def get_all_accounts():
    return AccountService.get_all_accounts()
