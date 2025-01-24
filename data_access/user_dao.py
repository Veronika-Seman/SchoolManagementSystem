from data_access.data_operations import BaseDAO


class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def create_user(self, id_number, name, email, password, role):
        query = """
        INSERT INTO Users (id_number, name, email, password, role)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, (id_number, name, email, password, role))
            self.connection.commit()
        except Exception as e:
            print(f"Error creating user: {e}")

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
