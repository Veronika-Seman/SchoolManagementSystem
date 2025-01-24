import mysql.connector
from data_access.sqlConnect import get_connection

from data_access.sqlConnect import get_connection


def drop_all_tables():
    tables = [
        "Teachers",
        "Users"
    ]

    connection = get_connection()
    if connection is None:
        print("The tables cannot be dropped due to a problem connecting to the database.")
        return

    cursor = connection.cursor()
    try:
        for table in tables:
            drop_query = f"DROP TABLE IF EXISTS {table};"
            cursor.execute(drop_query)
            print(f"Table {table} dropped successfully.")
        connection.commit()
    except Exception as e:
        print(f"Error dropping tables: {e}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    drop_all_tables()
