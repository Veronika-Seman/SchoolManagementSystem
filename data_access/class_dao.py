from data_access.data_operations import BaseDAO


class ClassDAO(BaseDAO):
    """
      ClassDAO class for managing class-related operations in the system.
      Includes methods for creating, updating, deleting, and retrieving class records.
      Methods:
          create_class(course_id, classroom_name): Creates a new class record.
          update_class(class_id, course_id=None, classroom_name=None): Updates details of an existing class.
          delete_class(class_id): Deletes a class from the database.
          get_class_by_id(class_id): Retrieves a class record by its ID.
          get_classes_by_course(course_id): Retrieves all classes associated with a specific course.
          get_all_classes(): Retrieves all class records in the system.
          get_class_by_name(class_name): Retrieves a class by its name.
          close(): Closes the DAO connection.
      """
    def __init__(self):
        super().__init__()

    def create_class(self, course_id, classroom_name):
        query = """
        INSERT INTO Classes (course_id, classroom_name)
        VALUES (%s, %s)
        """
        try:
            self.cursor.execute(query, (course_id, classroom_name))
            self.connection.commit()
            print(f"Class '{classroom_name}' for course ID {course_id} created successfully.")
        except Exception as e:
            print(f"Error creating class for course ID {course_id}: {e}")

    def update_class(self, class_id, course_id=None, classroom_name=None):
        query = "UPDATE Classes SET "
        params = []
        if course_id:
            query += "course_id = %s, "
            params.append(course_id)
        if classroom_name:
            query += "classroom_name = %s, "
            params.append(classroom_name)
        query = query.rstrip(", ") + " WHERE class_id = %s"
        params.append(class_id)
        try:
            self.cursor.execute(query, tuple(params))
            self.connection.commit()
            print(f"Class ID {class_id} updated successfully.")
        except Exception as e:
            print(f"Error updating class ID {class_id}: {e}")

    def delete_class(self, class_id):
        query = "DELETE FROM Classes WHERE class_id = %s"
        try:
            self.cursor.execute(query, (class_id,))
            self.connection.commit()
            print(f"Class ID {class_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting class ID {class_id}: {e}")

    def get_class_by_id(self, class_id):
        query = "SELECT * FROM Classes WHERE class_id = %s"
        try:
            self.cursor.execute(query, (class_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching class ID {class_id}: {e}")
            return None

    def get_classes_by_course(self, course_id):
        query = """
        SELECT * FROM Classes
        WHERE course_id = %s
        """
        try:
            self.cursor.execute(query, (course_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching classes for course ID {course_id}: {e}")
            return []

    def get_all_classes(self):
        query = "SELECT * FROM Classes"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all classes: {e}")
            return []

    def get_class_by_name(self, class_name):
        query = """
        SELECT * FROM Classes
        WHERE class_name = %s
        """
        try:
            self.cursor.execute(query, (class_name,))
            result = self.cursor.fetchone()
            if result:
                print(f"Class '{class_name}' found: {result}")
                return result
            else:
                print(f"Class '{class_name}' not found.")
                return None
        except Exception as e:
            print(f"Error fetching class by name '{class_name}': {e}")
            return None

    def close(self):
        super().close()
