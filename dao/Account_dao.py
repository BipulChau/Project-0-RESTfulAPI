import psycopg
from exception.user_not_found import UserNotFoundError


class AccountDao:
    @staticmethod
    def get_all_accounts():
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts")
                account_all_list = cur.fetchall()
                return account_all_list

    @staticmethod
    def get_customer_account(customer_id_num):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT account_num, name, id_num,  account_type_id, balance FROM customers left join accounts on id_num = customer_id_num  where id_num=%s",
                    (customer_id_num,))
                got_customer = tuple(cur.fetchall())
                return got_customer

    @staticmethod
    def get_customer_account_with_query_params_amount_less_than(customer_id_num, amount_less_than):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT account_num, name, id_num,  account_type_id, balance FROM customers left join accounts on id_num = customer_id_num  where id_num=%s and balance<%s",
                    (customer_id_num, amount_less_than))
                got_customer = tuple(cur.fetchall())
                return got_customer

    @staticmethod
    def add_customer_account(customer_id_num, data):
        if AccountDao.get_customer_account(customer_id_num):
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="postgres") as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO accounts(customer_id_num, balance, account_type_id) VALUES (%s, %s, %s) RETURNING *",
                        (customer_id_num, data["balance"], data["account_type_id"]))

                    account_just_created = cur.fetchone()
                    print(account_just_created)
                    print(type(account_just_created))
                    return account_just_created
        raise UserNotFoundError(f"Account cannot be created for the customer having an id of {customer_id_num} because it does not exist!!!")

