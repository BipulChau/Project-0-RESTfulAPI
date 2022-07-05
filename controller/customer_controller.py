import flask
from flask import Blueprint, request
from dao.customer_dao import CustomerDao
from service.customer_service import CustomerService
from exception.user_not_found import UserNotFoundError
from exception.customer_already_exist import CustomerAlreadyExistError

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
        try:
            return CustomerService.add_customer(data)
        except CustomerAlreadyExistError as e:
            # raise CustomerAlreadyExistError(str(e))
            print("Tappu")
            return {"message": str(e)}, 400

    else:
        return {
            "customers": CustomerService.get_all_customers()
        }


@cc.route("/customers/<id_num>",
          methods=["GET", "DELETE", "PUT"])
def get_customer_by_id(id_num):
    if flask.request.method == "GET":  # Get customer with an id of X (if the customer exists)
        try:
            return CustomerService.get_customer_by_id(id_num)
        except UserNotFoundError as e:
            return {
                       "message": str(e)
                   }, 404
    elif flask.request.method == "DELETE":  # Delete customer with an id of X (if the customer exists)
        try:
            return CustomerService.delete_customer_by_id(id_num)
        except UserNotFoundError as e:
            return {
                       "message": str(e)
                   }, 404
    else:  # Update customer with an id of X (if the customer exists)
        try:
            data = request.get_json()
            return CustomerService.update_customer_by_id(id_num, data)
        except UserNotFoundError as e:
            return {"message": str(e)}

