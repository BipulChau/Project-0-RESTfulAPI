import pytest
from service.customer_service import CustomerService
from exception.user_not_found import UserNotFoundError
from exception.customer_already_exist import CustomerAlreadyExistError


def test_get_all_customers(mocker):
    # Arrange
    def mock_get_all_customers():  # Mock Method for CustomerDao class
        return [(3, 'Rashmi Chaudhary', 'KO11PA', 'Vancouver, CA', '647-845-0002'),
                (4, 'Rimsha Chaudhary', 'AUM21', 'Calgary, CA', '647-845-0003'),
                (5, 'Laxmi Chaudhary', 'NAMAN108', 'Edmonton, CA', '647-845-0004'),
                (6, 'BADRI PRASAD CHAUDHARY', 'SADHGURU21', 'KTM, NP', '416-845-0009'),
                (9, 'OGGY CHAUDHARY', 'CSBY367', 'Toronto, CA', '647-111-7777'),
                (10, 'Vinod Thallaivi', 'MSD111', 'Coimbatore, IN', '917-000-6789'),
                (11, 'Madhu Chaudhary', 'MADY24', 'Toronto, CA', '612-561-8977')]

    mocker.patch("dao.customer_dao.CustomerDao.get_all_customers", mock_get_all_customers)

    # Act
    actual = CustomerService.get_all_customers()

    # Assert
    assert actual == [{'s_num': 3, 'name': 'Rashmi Chaudhary', 'id_num': 'KO11PA', 'address': 'Vancouver, CA',
                       'mobile_phone': '647-845-0002'},
                      {'s_num': 4, 'name': 'Rimsha Chaudhary', 'id_num': 'AUM21', 'address': 'Calgary, CA',
                       'mobile_phone': '647-845-0003'},
                      {'s_num': 5, 'name': 'Laxmi Chaudhary', 'id_num': 'NAMAN108', 'address': 'Edmonton, CA',
                       'mobile_phone': '647-845-0004'},
                      {'s_num': 6, 'name': 'BADRI PRASAD CHAUDHARY', 'id_num': 'SADHGURU21', 'address': 'KTM, NP',
                       'mobile_phone': '416-845-0009'},
                      {'s_num': 9, 'name': 'OGGY CHAUDHARY', 'id_num': 'CSBY367', 'address': 'Toronto, CA',
                       'mobile_phone': '647-111-7777'},
                      {'s_num': 10, 'name': 'Vinod Thallaivi', 'id_num': 'MSD111', 'address': 'Coimbatore, IN',
                       'mobile_phone': '917-000-6789'},
                      {'s_num': 11, 'name': 'Madhu Chaudhary', 'id_num': 'MADY24', 'address': 'Toronto, CA',
                       'mobile_phone': '612-561-8977'}]


def test_get_customer_by_id_positive(mocker):
    # Arrange
    def mock_get_customer_by_id(id_num):
        if id_num == "AUM21":
            return 4, 'Rimsha Chaudhary', 'AUM21', 'Calgary, CA', '647-845-0003'
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    # Act
    actual = CustomerService.get_customer_by_id("AUM21")
    # Assert
    assert actual == {
        'AUM21': {'s_num': 4, 'name': 'Rimsha Chaudhary', 'address': 'Calgary, CA', 'mobile_phone': '647-845-0003'}}


def test_get_customer_by_id_negative(mocker):
    # Arrange
    def mock_test_get_customer_by_id(id_num):
        if id_num == "AUM21":
            return 4, 'Rimsha Chaudhary', 'AUM21', 'Calgary, CA', '647-845-0003'
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_test_get_customer_by_id)
    # Act

    # Assert
    with pytest.raises(UserNotFoundError) as e:
        actual = CustomerService.get_customer_by_id("DOGGIE999")


def test_add_customer_positive(mocker):
    # Arrange
    def mock_test_add_customer(customer_data):
        if customer_data == ('Oggy Poggy', 'POGU108', 'Toronto, CA', '612-561-8977'):
            return 39, 'Oggy Poggy', 'POGU108', 'Toronto, CA', '612-561-8977'
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_test_add_customer)

    # ACT
    data1 = {'address': 'Toronto, CA', 'id_num': 'POGU108', 'mobile_phone': '612-561-8977', 'name': 'Oggy Poggy'}
    actual = CustomerService.add_customer(data1)
    print(f"actual is {actual}")

    # Assert
    assert actual == {
        'Data successfully inserted': {'s_num': 39, 'name': 'Oggy Poggy', 'id_num': 'POGU108', 'address': 'Toronto, CA',
                                       'mobile_phone': '612-561-8977'}}


def test_add_customer_negative(mocker):
    # Arrange
    def mock_test_add_customer(customer_data):
        if customer_data == ('Oggy Poggy', 'POGU108', 'Toronto, CA', '612-561-8977'):
            raise CustomerAlreadyExistError(f"Customer already exists with id POGU108")

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_test_add_customer)

    with pytest.raises(CustomerAlreadyExistError) as e:
        data1 = {'address': 'Toronto, CA', 'id_num': 'POGU108', 'mobile_phone': '612-561-8977', 'name': 'Oggy Poggy'}
        actual = CustomerService.add_customer(data1)


def test_delete_customer_by_id_positive(mocker):
    # Arrange
    def mock_delete_customer_by_id(id_num):
        if id_num == "CSBY367":
            return True
        else:
            return False

    mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mock_delete_customer_by_id)

    # ACT
    actual = CustomerService.delete_customer_by_id("CSBY367")

    # Assert
    assert actual == f"Customer with id number CSBY367 successfully deleted"


def test_delete_customer_by_id_negative(mocker):
    # Arrange
    def mock_delete_customer_by_id(id_num):
        if id_num == "CSBY367":
            return True
        else:
            return False

    mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mock_delete_customer_by_id)

    # Act & Assert
    with pytest.raises(UserNotFoundError) as e:
        actual = CustomerService.delete_customer_by_id("AUM21")


def test_update_customer_by_id_positive(mocker):
    # Arrange
    def mocker_update_customer_by_id(id_num, data):
        if id_num == "POGUwa12" and data == {'address': 'NEPAL', 'id_num': 'POGUwa12', 'mobile_phone': '612-561-8977',
                                             'name': 'Oggy-Poggy'}:
            return {
                "Information of customer with id number POGUwa12 is updated as": {
                    "address": "NEPAL",
                    "id_num": "POGUwa12",
                    "mobile_phone": "612-561-8977",
                    "name": "Oggy-Poggy"
                }
            }
        else:
            return None

        mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mocker_update_customer_by_id)

        # Actual
        id_num = "POGUwa12"
        data = {'address': 'NEPAL', 'id_num': 'POGUwa12', 'mobile_phone': '612-561-8977',
                'name': 'Oggy-Poggy'}
        actual = CustomerService.update_customer_by_id(id_num, data)

        # Assert
        var = actual == {
            "Information of customer with id number POGUwa12 is updated as": {
                "address": "NEPAL",
                "id_num": "POGUwa12",
                "mobile_phone": "612-561-8977",
                "name": "Oggy-Poggy"
            }
        }


def test_update_customer_by_id_negative(mocker):
    # Arrange
    def mocker_update_customer_by_id(id_num, data):
        if id_num == "POGUwa12" and data == {'address': 'NEPAL', 'id_num': 'POGUwa12', 'mobile_phone': '612-561-8977',
                                             'name': 'Oggy-Poggy'}:
            return {
                "Information of customer with id number POGUwa12 is updated as": {
                    "address": "NEPAL",
                    "id_num": "POGUwa12",
                    "mobile_phone": "612-561-8977",
                    "name": "Oggy-Poggy"
                }
            }
        else:
            return None

        mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mocker_update_customer_by_id)

        # Act & Assert
        with pytest.raises(UserNotFoundError) as e:
            actual = CustomerService.update_customer_by_id("AUM21", {'address': 'NEPAL', 'id_num': 'AUM21',
                                                                     'mobile_phone': '612-561-8977',
                                                                     'name': 'Bunu Chau'})
