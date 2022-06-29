import psycopg


class CustomerDao:
    @staticmethod
    def get_all_customers():
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")
                print(f"cur is {cur}")
                customer_all_list = cur.fetchall()
                print(f"Fetch Dats is {customer_all_list}")
                return customer_all_list



