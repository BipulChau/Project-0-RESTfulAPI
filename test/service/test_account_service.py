import pytest

import dao.Account_dao
from service.account_service import AccountService


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

