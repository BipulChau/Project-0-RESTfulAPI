import pytest

import dao.Account_dao
from dao.Account_dao import AccountDao
from service.account_service import AccountService
from exception.user_not_found import UserNotFoundError


def test_get_all_accounts(mocker):
    # Arrange
    def mock_get_all_accounts():
        return [(4, 'CSBY367', 2, 150000), (6, 'NAMAN108', 1, 21000)]

    mocker.patch("dao.Account_dao.AccountDao.get_all_accounts", mock_get_all_accounts)

    # ACT
    actual = AccountService.get_all_accounts()

    # Assert
    var = actual == {
        "Accounts": [
            {
                "account_num": 4,
                "account_type_id": 2,
                "balance": 150000,
                "customer_id_num": "CSBY367"
            },
            {
                "account_num": 6,
                "account_type_id": 1,
                "balance": 21000,
                "customer_id_num": "NAMAN108"
            }
        ]
    }


def test_get_customer_account_positive(mocker):
    # Arrange
    def mock_get_customer_account(customer_id_num):
        if customer_id_num == "NAMAN108":
            return (6, 'Laxmi Chaudhary', 'NAMAN108', 1, 21000),
        else:
            return ()

    mocker.patch("dao.Account_dao.AccountDao.get_customer_account", mock_get_customer_account)

    # Act
    actual = AccountService.get_customer_account("NAMAN108")

    # Assert
    var = actual == {
        "Accounts of Laxmi Chaudhary having id number NAMAN108": [
            {
                "account_num": 6,
                "account_type_id": 1,
                "balance": 21000
            }
        ]
    }


def test_get_customer_account_negative(mocker):
    # Arrange
    def mock_get_customer_account(customer_id_num):
        if customer_id_num == "NAMAN108":
            return (6, 'Laxmi Chaudhary', 'NAMAN108', 1, 21000),
        else:
            return ()

    mocker.patch("dao.Account_dao.AccountDao.get_customer_account", mock_get_customer_account)

    # Act and Assert
    with pytest.raises(UserNotFoundError) as e:
        actual = AccountService.get_customer_account("CSBY367")


def test_add_customer_account_positive(mocker):
    # Arrange
    def mock_add_customer_account(customer_id_num, data):
        if customer_id_num == "NAMAN108" and data == {'account_type_id': 2, 'balance': 21000}:
            return 7, 'NAMAN108', 2, 21000
        else:
            raise (
                f"Account cannot be created for the customer having an id of {customer_id_num} because it does not exist!!!")

    mocker.patch("dao.Account_dao.AccountDao.add_customer_account", mock_add_customer_account)

    # Act
    actual = AccountService.add_customer_account("NAMAN108", {'account_type_id': 2, 'balance': 21000})

    # Assert
    var = actual == {
        "Account opened for the customer with an id of NAMAN108": {
            "account_num": 8,
            "account_type_id": 2,
            "balance": 21000
        }
    }


def test_get_account_of_a_customer_with_account_num_positive(mocker):
    # Arrange
    def mock_get_account_of_a_customer_with_account_num(customer_id_num, account_num):
        if customer_id_num == "NAMAN108" and account_num == 6:
            ((6, 'Laxmi Chaudhary', 'NAMAN108', 1, 21000),)
        else:
            raise UserNotFoundError(
                f"Account number {account_num} of Customer having id {customer_id_num} not found !!!")

        mocker.patch("dao.Account_dao.AccountDao.get_account_of_a_customer_with_account_num",
                     mock_get_account_of_a_customer_with_account_num)

    # Act
    actual = AccountService.get_account_of_a_customer_with_account_num("NAMAN108", 6)

    # Assert
    var = actual == {
        "Details of account number 6 ": [
            {
                "account_type_id": 1,
                "balance": 21000,
                "name": "Laxmi Chaudhary"
            }
        ]
    }


def test_get_account_of_a_customer_with_account_num_negative(mocker):
    # Arrange
    def mock_get_account_of_a_customer_with_account_num(customer_id_num, account_num):
        if customer_id_num == "NAMAN108" and account_num == 6:
            ((6, 'Laxmi Chaudhary', 'NAMAN108', 1, 21000),)
        else:
            raise UserNotFoundError(
                f"Account number {account_num} of Customer having id {customer_id_num} not found !!!")

        mocker.patch("dao.Account_dao.AccountDao.get_account_of_a_customer_with_account_num",
                     mock_get_account_of_a_customer_with_account_num)

    # Act & Assert
    with pytest.raises(UserNotFoundError) as e:
        actual = AccountService.get_account_of_a_customer_with_account_num("CSBY367", 21)