from dao.Account_dao import AccountDao
from model.account import Account
from exception.user_not_found import UserNotFoundError


class AccountService:
    @staticmethod
    def get_all_accounts():
        account_all_list = AccountDao.get_all_accounts()
        account_all_list_formatted = []
        for i in account_all_list:
            account_num = i[0]
            customer_id_num = i[1]
            account_type_id = i[2]
            balance = i[3]
            account_obj = Account(account_num, customer_id_num, account_type_id, balance)
            account_all_list_formatted.append(account_obj.to_dict())
        return {"Accounts": account_all_list_formatted}

    @staticmethod
    def get_customer_account(customer_id_num):
        all_accounts_of_customer = AccountDao.get_customer_account(customer_id_num)
        if all_accounts_of_customer:
            all_accounts_of_customer_formatted = tuple(map(lambda i: {"account_num": i[0], "account_type_id": i[3], "balance": i[4]}, all_accounts_of_customer))
            return {f"Accounts of {all_accounts_of_customer[0][1]} having id number {customer_id_num}": all_accounts_of_customer_formatted}
        raise UserNotFoundError(f"Accounts of Customer with id {customer_id_num} not found !!!")

    @staticmethod
    def add_customer_account(customer_id_num, data):
        account_just_created = AccountDao.add_customer_account(customer_id_num, data)
        return{
            f"Account opened for the customer with an id of {customer_id_num}": {
                "account_num": account_just_created[0],
                "account_type_id": account_just_created[2],
                "balance": account_just_created[3]
            }
        }
