class Customer:
    def __init__(self, s_num, name, address, mobile_phone):
        self.s_num = s_num
        self.name = name
        self.address = address
        self.mobile_phone = mobile_phone

    def to_dict(self):
        return{
            "s_num": self.s_num,
            "name": self.name,
            "address": self.address,
            "mobile_phone": self.mobile_phone
        }
