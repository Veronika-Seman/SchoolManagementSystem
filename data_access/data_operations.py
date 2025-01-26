import mysql.connector
from data_access.sqlConnect import get_connection

"""
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
"""
def execute_query(query, params=None, success_message="Query executed successfully."):

    connection = get_connection()
    if connection is None:
        print("The table cannot be created due to a problem connecting to the database.")
        return

    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        print(success_message)
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
    finally:
        cursor.close()
        connection.close()

class BaseDAO:
    def __init__(self):

        self.connection = get_connection()
        if self.connection:
            self.cursor = self.connection.cursor(dictionary=True)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

