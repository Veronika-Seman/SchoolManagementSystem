from data_access.sqlConnect import get_connection

class TeacherDAO:
    def __init__(self):
        self.connection = get_connection()
        if self.connection:
            self.cursor = self.connection.cursor(dictionary=True)

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



