import logging

from dao.customer_dao import CustomerDao
from model.customer import Customer
from dao.customer_dao import CustomerDao
from exception.user_not_found import UserNotFoundError
from exception.customer_already_exist import CustomerAlreadyExistError


class CustomerService:
    @staticmethod
    def get_all_customers():
        customers_all_list = CustomerDao.get_all_customers()
        customers_all_list_formatted = []
        for i in customers_all_list:
            s_num = i[0]
            name = i[1]
            id_num = i[2]
            address = i[3]
            mobile_phone = i[4]
            customer_obj = Customer(s_num, name, id_num, address, mobile_phone)
            customers_all_list_formatted.append(customer_obj.to_dict())
        print(customers_all_list_formatted)
        return customers_all_list_formatted

    @staticmethod
    def add_customer(data):
        name = data["name"]
        id_num = data["id_num"]
        address = data["address"]
        mobile_phone = data["mobile_phone"]
        try:
            print(data)
            # name = data["name"]
            # id_num = data["id_num"]
            # address = data["address"]
            # mobile_phone = data["mobile_phone"]
            customer_data = (name, id_num, address, mobile_phone)
            print(f"Customer details at Service layer: {customer_data}")
            customer_row_that_was_just_inserted = CustomerDao.add_customer(customer_data)
            print(f"at service layer {customer_row_that_was_just_inserted}")
            if customer_row_that_was_just_inserted:
                print({"Data successfully inserted": {
                    "s_num": customer_row_that_was_just_inserted[0],
                    "name": customer_row_that_was_just_inserted[1],
                    "id_num": customer_row_that_was_just_inserted[2],
                    "address": customer_row_that_was_just_inserted[3],
                    "mobile_phone": customer_row_that_was_just_inserted[4]
                }})
                return {"Data successfully inserted": {
                    "s_num": customer_row_that_was_just_inserted[0],
                    "name": customer_row_that_was_just_inserted[1],
                    "id_num": customer_row_that_was_just_inserted[2],
                    "address": customer_row_that_was_just_inserted[3],
                    "mobile_phone": customer_row_that_was_just_inserted[4]
                }}
        except CustomerAlreadyExistError:
            print("kappu")
            raise CustomerAlreadyExistError(f"Customer already exists with id {id_num}")
            # return {"message": str(e)}, 400

    @staticmethod
    def get_customer_by_id(id_num):
        customer_by_id = CustomerDao.get_customer_by_id(id_num)
        print(customer_by_id)
        if not customer_by_id:
            # return f"At service layer: Customer with id number {id_num} does not exist!!"
            raise UserNotFoundError(f"Customer with id {id_num} was not found")
        print({f"{id_num}": {
            "s_num": customer_by_id[0],
            "name": customer_by_id[1],
            "address": customer_by_id[3],
            "mobile_phone": customer_by_id[4]
        }})
        return {f"{id_num}": {
            "s_num": customer_by_id[0],
            "name": customer_by_id[1],
            "address": customer_by_id[3],
            "mobile_phone": customer_by_id[4]
        }}

    @staticmethod
    def delete_customer_by_id(id_num):
        customer_by_id = CustomerDao.delete_customer_by_id(id_num)

        if not customer_by_id:
            # return f"At service layer: Customer with id number {id_num} does not exist!!"
            raise UserNotFoundError(f"Customer with id {id_num} was not found")

        return f"Customer with id number {id_num} successfully deleted"

    @staticmethod
    def update_customer_by_id(id_num, data):
        updated_info = CustomerDao.update_customer_by_id(id_num, data)
        if not updated_info:
            raise UserNotFoundError(f"Customer with id {id_num} was not found")

        return updated_info
