from dao.customer_dao import CustomerDao
from model.customer import Customer
from dao.customer_dao import CustomerDao


class CustomerService:
    @staticmethod
    def get_all_customers():
        customers_all_list = CustomerDao().get_all_customers()
        customers_all_list_formatted = []
        for i in customers_all_list:
            s_num = i[0]
            name = i[1]
            id_num = i[2]
            address = i[3]
            mobile_phone = i[4]
            customer_obj = Customer(s_num, name, id_num, address, mobile_phone)
            customers_all_list_formatted.append(customer_obj.to_dict())

        return customers_all_list_formatted

    @staticmethod
    def add_customer(data):

        name = data["name"]
        id_num = data["id_num"]
        address = data["address"]
        mobile_phone = data["mobile_phone"]
        customer_data = (name, id_num, address, mobile_phone)
        print(f"Customer details at Service layer: {customer_data}")
        return CustomerDao.add_customer(customer_data)

    @staticmethod
    def get_customer_by_name(data):
        return "add_customer_by_name at customer_service layer"


if __name__ == "__main__":
    CustomerService.get_all_customers()
