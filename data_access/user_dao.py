import hashlib

from data_access.data_operations import BaseDAO

class UserDAO(BaseDAO):


    """
    UserDAO is a Data Access Object (DAO) class responsible for managing operations related to the 'Users' table in the database.
    It provides methods for creating, reading, updating, and deleting user records.
    Methods:
        create_user(id_number, name, email, password, role):Creates a new user in the database if the user does not already exist.
        user_exists(id_number): Checks if a user with a given ID exists in the database.
        get_user_by_id(id_number):Retrieves user details by their ID.
        get_user_by_email(email): Retrieves user details by their email.
        update_user(id_number, name=None, email=None, password=None): Updates a user's information in the database.
        delete_user(id_number):Deletes a user from the database by their ID.
        close():Closes the DAO connection and cleans up resources.
    """
    def __init__(self):
        super().__init__()

    def create_user(self, id_number, name, email, password, role):
        try:
            query_check = "SELECT * FROM Users WHERE id_number = %s"
            self.cursor.execute(query_check, (id_number,))
            if self.cursor.fetchone():
                print(f"User with ID {id_number} already exists. Skipping creation.")
                return

            query_insert = """
            INSERT INTO Users (id_number, name, email, password, role)
            VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query_insert, (id_number, name, email, password, role))
            self.connection.commit()
            print(f"User with ID {id_number} created successfully.")
        except Exception as e:
            print(f"Error creating user: {e}")

    def user_exists(self, id_number):

        query = "SELECT * FROM Users WHERE id_number = %s"
        try:
            self.cursor.execute(query, (id_number,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print(f"Error checking if user with ID {id_number} exists: {e}")
            return False

    def get_user_by_id(self, id_number):
        query = "SELECT * FROM Users WHERE id_number = %s"
        try:
            self.cursor.execute(query, (id_number,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    def get_user_by_email(self, email):
        query = "SELECT * FROM Users WHERE email = %s"
        try:
            self.cursor.execute(query, (email,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None


    def update_user(self, id_number, name=None, email=None, password=None):
        query = "UPDATE Users SET "
        params = []
        if name:
            query += "name = %s, "
            params.append(name)
        if email:
            query += "email = %s, "
            params.append(email)
        if password:
            query += "password = %s, "
            params.append(password)
        query = query.rstrip(", ") + " WHERE id_number = %s"
        params.append(id_number)
        try:
            self.cursor.execute(query, tuple(params))
            self.connection.commit()
            print(f"User {id_number} updated successfully.")
        except Exception as e:
            print(f"Error updating user: {e}")

    def delete_user(self, id_number):
        query = "DELETE FROM Users WHERE id_number = %s"
        try:
            self.cursor.execute(query, (id_number,))
            self.connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")

    def close(self):
        super().close()
