class Customer:
    def __init__(self, s_num, name, id_num, address, mobile_phone):
        self.s_num = s_num
        self.name = name
        self.id_num = id_num
        self.address = address
        self.mobile_phone = mobile_phone

    def to_dict(self):
        return{
            "s_num": self.s_num,
            "name": self.name,
            "id_num": self.id_num,
            "address": self.address,
            "mobile_phone": self.mobile_phone
        }
