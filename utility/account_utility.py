from exception.user_not_found import UserNotFoundError


class AccountUtility:
    @staticmethod
    def get_and_format_customer_account(customer_id_num, all_accounts_of_customer):
        if all_accounts_of_customer:
            all_accounts_of_customer_formatted = tuple(
                map(lambda i: {"account_num": i[0], "account_type_id": i[3], "balance": i[4]},
                    all_accounts_of_customer))
            return {
                f"Accounts of {all_accounts_of_customer[0][1]} having id number {customer_id_num}": all_accounts_of_customer_formatted}
        raise UserNotFoundError(f"Accounts of Customer with id {customer_id_num} not found !!!")
