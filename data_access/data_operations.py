import mysql.connector
from data_access.sqlConnect import get_connection

"""
Database Utility Module

This module provides foundational database access functionality, including query execution 
and base operations for Data Access Objects (DAO). It establishes a connection to a MySQL 
database using the `get_connection` function from `data_access.sqlConnect`.

Functions:
- `execute_query(query, params=None, success_message="Query executed successfully.")`:  
  Executes an SQL query with optional parameters, commits the changes, and prints a success 
  or error message. Ensures proper connection handling.

Classes:
- `BaseDAO`:  
  A base class for DAOs that provides a reusable database connection and cursor.

  Methods:
  - `__init__()`: Initializes a database connection and creates a dictionary-based cursor 
    for handling query results.
  - `close()`: Closes the database cursor and connection to free resources.

This module serves as a foundation for database operations, ensuring efficient query 
execution and proper resource management.
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
        super().__init__()
        self.connection = get_connection()
        if self.connection:
            self.cursor = self.connection.cursor(dictionary=True)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

