from dao.Account_dao import AccountDao
from model.account import Account


class AccountService:
    @staticmethod
    def get_all_accounts():
        account_all_list = AccountDao.get_all_accounts()
        print(f"Accounts details at service layer: {account_all_list}")
        account_all_list_formatted = []
        for i in account_all_list:
            s_num = i[0]
            customer_id_num = i[1]
            account_type_id = i[2]
            balance = i[3]
            account_obj = Account(s_num, customer_id_num, account_type_id, balance)
            account_all_list_formatted.append(account_obj.to_dict())
        return {"Accounts": account_all_list_formatted}
