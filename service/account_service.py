from dao.Account_dao import AccountDao
from model.account import Account
from exception.user_not_found import UserNotFoundError
from exception.account_not_found import AccountNotFoundError
from exception.invalid_parameter import InvalidParameter
from utility.account_utility import AccountUtility


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
            return AccountUtility.get_and_format_customer_account(customer_id_num, all_accounts_of_customer)

        raise UserNotFoundError(f"Accounts of Customer with id {customer_id_num} not found !!!")

    @staticmethod
    def get_customer_account_with_query_params(customer_id_num, query_params):
        amount_less_than = query_params.get("amountLessThan")
        amount_greater_than = query_params.get("amountGreaterThan")
        if amount_less_than and not amount_greater_than:  # if query parameter has only one key as amountLessThan
            all_accounts_of_customer = AccountDao.get_customer_account_with_query_params_amount_less_than(
                customer_id_num, amount_less_than)
            if all_accounts_of_customer:
                return AccountUtility.get_and_format_customer_account(customer_id_num, all_accounts_of_customer)
            raise AccountNotFoundError(
                f"Accounts with balance less than {amount_less_than} not found for the customer having an id number {customer_id_num}")
        elif amount_greater_than and not amount_less_than:  # if query parameter has only one key as amountGreaterThan
            all_accounts_of_customer = AccountDao.get_customer_account_with_query_params_amount_greater_than(
                customer_id_num, amount_greater_than)
            if all_accounts_of_customer:
                return AccountUtility.get_and_format_customer_account(customer_id_num, all_accounts_of_customer)
            raise AccountNotFoundError(
                f"Accounts with balance greater than {amount_greater_than} not found for the customer having an id number {customer_id_num}")
        else:
            amount_less_than = int(query_params.get("amountLessThan"))
            amount_greater_than = int(query_params.get("amountGreaterThan"))
            if amount_greater_than < amount_less_than:  # if there are both amountGreaterThan and amountLessThan params and amount_greater_than < amount_less_than
                all_accounts_of_customer = AccountDao.get_customer_account_with_query_params_amount_in_between(
                    customer_id_num, amount_greater_than, amount_less_than)
                if all_accounts_of_customer:
                    return AccountUtility.get_and_format_customer_account(customer_id_num, all_accounts_of_customer)
                raise AccountNotFoundError(
                    f"Accounts with balance less than {amount_less_than}  and balance greater than {amount_greater_than} not found for the customer having an id number {customer_id_num}")
            else:
                raise InvalidParameter(f"Invalid parameters: amountGreaterThan should be smaller than amountLessthan")

    @staticmethod
    def add_customer_account(customer_id_num, data):
        try:
            account_just_created = AccountDao.add_customer_account(customer_id_num, data)
            if account_just_created:
                return {
                    f"Account opened for the customer with an id of {customer_id_num}": {
                        "account_num": account_just_created[0],
                        "account_type_id": account_just_created[2],
                        "balance": account_just_created[3]
                    }
                }
        except UserNotFoundError as e:
            return {
                       "message": str(e)
                   }, 404

    @staticmethod
    def get_account_of_a_customer_with_account_num(customer_id_num, account_num):
        # return AccountDao.get_account_of_a_customer_with_account_num(customer_id_num, account_num)
        account_of_a_customer = AccountDao.get_account_of_a_customer_with_account_num(customer_id_num, account_num)
        if account_of_a_customer:
            return AccountUtility.get_and_format_customer_individual_account(customer_id_num, account_of_a_customer)
        raise UserNotFoundError(f"Account number {account_num} of Customer having id {customer_id_num} not found !!!")



