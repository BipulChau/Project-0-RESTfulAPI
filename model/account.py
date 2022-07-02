class Account:
    def __init__(self, s_num, customer_id_num, account_type_id, balance):
        self.s_num = s_num
        self.customer_id_num = customer_id_num
        self.account_type_id = account_type_id
        self.balance = balance

    def to_dict(self):
        return {
            "s_num": self.s_num,
            "customer_id_num": self.customer_id_num,
            "account_type_id": self.account_type_id,
            "balance": self.balance

        }
