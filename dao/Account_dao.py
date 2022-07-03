import psycopg


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
                cur.execute("SELECT account_num, name, id_num,  account_type_id, balance FROM customers left join accounts on id_num = customer_id_num  where id_num=%s", (customer_id_num,))
                got_customer = tuple(cur.fetchall())
                print(got_customer)
                print(type(got_customer))
                return got_customer




