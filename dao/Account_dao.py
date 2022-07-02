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


