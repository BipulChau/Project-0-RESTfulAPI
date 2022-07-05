import pytest
from service.customer_service import CustomerService
from exception.user_not_found import UserNotFoundError


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
    assert actual == {'AUM21': {'s_num': 4, 'name': 'Rimsha Chaudhary', 'address': 'Calgary, CA', 'mobile_phone': '647-845-0003'}}


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
