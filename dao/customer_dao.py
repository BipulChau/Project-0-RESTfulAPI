import psycopg
from exception.customer_already_exist import CustomerAlreadyExistError



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
        if not CustomerDao.get_customer_by_id(data[1]):
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
                    return customer_row_that_was_just_inserted

        raise CustomerAlreadyExistError(f"Customer already exists with id {data[1]}")

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
                print(f"get_customer_by_id at DAO layer: {got_customer}")
                if got_customer:
                    return got_customer[0]
                return None

    @staticmethod
    def delete_customer_by_id(id_num):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM customers WHERE id_num=%s", (id_num,)
                )
                rows_deleted = cur.rowcount

                if not rows_deleted:
                    return False
                else:
                    conn.commit()
                    return True

    @staticmethod
    def update_customer_by_id(id_num, data):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE customers SET name = %s, id_num = %s, address = %s, mobile_phone = %s WHERE id_num = %s RETURNING *",
                    (data["name"], data["id_num"], data["address"], data["mobile_phone"], id_num))

                conn.commit()
                updated_customer_row = cur.fetchone()

                print(updated_customer_row)
                print(f" Data type of fetchone at DAO {type(updated_customer_row)}")
                if not updated_customer_row:
                    return None

                return {
                    f"Information of customer with id number {id_num} is updated as": {"name": updated_customer_row[1],
                                                                                       "id_num": updated_customer_row[
                                                                                           2],
                                                                                       "address": updated_customer_row[
                                                                                           3],
                                                                                       "mobile_phone":
                                                                                           updated_customer_row[4]
                                                                                       }}
