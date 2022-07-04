from service.customer_service import CustomerService


def test_get_all_customers(mocker):
    # Arrange
    def mock_get_all_customers(): # Mock Method for CustomerDao class
        return [(3, 'Rashmi Chaudhary', 'KO11PA', 'Vancouver, CA', '647-845-0002'), (4, 'Rimsha Chaudhary', 'AUM21', 'Calgary, CA', '647-845-0003'), (5, 'Laxmi Chaudhary', 'NAMAN108', 'Edmonton, CA', '647-845-0004'), (6, 'BADRI PRASAD CHAUDHARY', 'SADHGURU21', 'KTM, NP', '416-845-0009'), (9, 'OGGY CHAUDHARY', 'CSBY367', 'Toronto, CA', '647-111-7777'), (10, 'Vinod Thallaivi', 'MSD111', 'Coimbatore, IN', '917-000-6789'), (11, 'Madhu Chaudhary', 'MADY24', 'Toronto, CA', '612-561-8977')]

    mocker.patch("dao.customer_dao.CustomerDao.get_all_customers", mock_get_all_customers)
    # customer_service = CustomerService()

    # Act
    actual = CustomerService.get_all_customers()

    # Assert
    assert actual == [{'s_num': 3, 'name': 'Rashmi Chaudhary', 'id_num': 'KO11PA', 'address': 'Vancouver, CA', 'mobile_phone': '647-845-0002'}, {'s_num': 4, 'name': 'Rimsha Chaudhary', 'id_num': 'AUM21', 'address': 'Calgary, CA', 'mobile_phone': '647-845-0003'}, {'s_num': 5, 'name': 'Laxmi Chaudhary', 'id_num': 'NAMAN108', 'address': 'Edmonton, CA', 'mobile_phone': '647-845-0004'}, {'s_num': 6, 'name': 'BADRI PRASAD CHAUDHARY', 'id_num': 'SADHGURU21', 'address': 'KTM, NP', 'mobile_phone': '416-845-0009'}, {'s_num': 9, 'name': 'OGGY CHAUDHARY', 'id_num': 'CSBY367', 'address': 'Toronto, CA', 'mobile_phone': '647-111-7777'}, {'s_num': 10, 'name': 'Vinod Thallaivi', 'id_num': 'MSD111', 'address': 'Coimbatore, IN', 'mobile_phone': '917-000-6789'}, {'s_num': 11, 'name': 'Madhu Chaudhary', 'id_num': 'MADY24', 'address': 'Toronto, CA', 'mobile_phone': '612-561-8977'}]

