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
            address = i[2]
            mobile_phone = i[3]
            customer_obj = Customer(s_num, name, address, mobile_phone)
            customers_all_list_formatted.append(customer_obj.to_dict())

        return customers_all_list_formatted

    @staticmethod
    def add_customer(data):

        name = data["name"]
        address = data["address"]
        mobile_phone = data["mobile_phone"]
        customer_data = (name, address, mobile_phone)
        print(f"Customer details at Service layer: {customer_data}")
        return CustomerDao.add_customer(customer_data)


CustomerService.get_all_customers()
