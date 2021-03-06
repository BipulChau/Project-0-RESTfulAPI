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
    def get_customer_account_with_query_params_amount_less_than(customer_id_num,
                                                                amount_less_than):  # When query parameter is amountLessThan
        print(type(amount_less_than))
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT account_num, name, id_num,  account_type_id, balance FROM customers left join accounts on id_num = customer_id_num  where id_num=%s and balance<%s",
                    (customer_id_num, amount_less_than))
                got_customer = tuple(cur.fetchall())
                return got_customer

    @staticmethod
    def get_customer_account_with_query_params_amount_greater_than(customer_id_num,
                                                                   amount_greater_than):  # When query parameter is amountLessThan
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT account_num, name, id_num,  account_type_id, balance FROM customers left join accounts on id_num = customer_id_num  where id_num=%s and balance>%s",
                    (customer_id_num, amount_greater_than))
                got_customer = tuple(cur.fetchall())
                return got_customer

    @staticmethod
    def get_customer_account_with_query_params_amount_in_between(customer_id_num,
                                                                 amount_greater_than,
                                                                 amount_less_than):  # When query parameter has both amountGreaterThan and amountLessThan (i.e. multiple queries)
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT account_num, name, id_num,  account_type_id, balance FROM customers join accounts on id_num = customer_id_num  where id_num=%s and balance>%s and balance<%s",
                    (customer_id_num, amount_greater_than, amount_less_than))
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

        raise UserNotFoundError(
            f"Account cannot be created for the customer having an id of {customer_id_num} because it does not exist!!!")

    @staticmethod
    def get_account_of_a_customer_with_account_num(customer_id_num, account_num):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT account_num, name, id_num,  account_type_id, balance FROM customers join accounts on id_num = customer_id_num  where id_num=%s and account_num=%s",
                    (customer_id_num, account_num))
                got_customer = tuple(cur.fetchall())
                print(got_customer)
                return got_customer

    @staticmethod
    def update_account_of_customer(customer_id_num, account_num, data):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE accounts SET balance=%s WHERE customer_id_num =%s and account_num=%s RETURNING *",
                            (data["balance"], customer_id_num, account_num))
                updated_customer_row = cur.fetchone()

                if not updated_customer_row:
                    return None

                return updated_customer_row

    @staticmethod
    def delete_account_of_customer(customer_id_num, account_num):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM accounts where customer_id_num=%s and account_num=%s",
                            (customer_id_num, account_num))
                rows_deleted = cur.rowcount
                if not rows_deleted:
                    return False
                else:
                    conn.commit()
                    return True
