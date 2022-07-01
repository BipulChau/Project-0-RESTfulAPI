import psycopg
from model.customer import Customer


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

    @staticmethod
    def add_customer(data):
        print(f"Data at DAO is {data}")
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO customers (name, id_num, address, mobile_phone) VALUES (%s, %s, %s, %s) RETURNING *",
                    (data[0],
                     data[1],
                     data[
                         2], data[3]))
                customer_row_that_was_just_inserted = cur.fetchone()
                print(f"Data inserted is {customer_row_that_was_just_inserted}")
                print(type(customer_row_that_was_just_inserted))
                conn.commit()

                return {"Data successfully inserted": {
                    "s_num": customer_row_that_was_just_inserted[0],
                    "name": customer_row_that_was_just_inserted[1],
                    "id_num": customer_row_that_was_just_inserted[2],
                    "address": customer_row_that_was_just_inserted[3],
                    "mobile_phone": customer_row_that_was_just_inserted[4]
                }}

    @staticmethod
    def get_customer_by_id(id_num):
        print(f"get_customer_by_id_num at DAO Layer")
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM customers WHERE id_num=%s", (id_num,)
                )
                got_customer = cur.fetchall()
                print(got_customer)
                print(type(got_customer))
                if got_customer:
                    got_customer_tuple = got_customer[0]
                    return {f"{id_num}": {
                        "s_num": got_customer_tuple[0],
                        "name": got_customer_tuple[1],
                        "address": got_customer_tuple[3],
                        "mobile_phone": got_customer_tuple[4]
                    }}
                # return f"Customer with id number {id_num} does not exist!!"
                return None
