import mysql
from data_access.sqlConnect import get_connection


def execute_query(query, success_message):
    connection = get_connection()
    if connection is None:
        print("The table cannot be created due to a problem connecting to the database.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(success_message)
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
    finally:
        connection.close()




