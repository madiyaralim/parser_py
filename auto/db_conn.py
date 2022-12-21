import  psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        con = psycopg2.connect(
            database="evaluation_data",
            user="postgres",
            password="db2022!!!",
            host="127.0.0.1",
            port="5432"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

    create_users_table = """
                CREATE TABLE IF NOT EXISTS users (
                  id SERIAL PRIMARY KEY,
                  name TEXT NOT NULL, 
                  age INTEGER,
                  gender TEXT,
                  nationality TEXT
                )
                """

    execute_query(connection, create_users_table)