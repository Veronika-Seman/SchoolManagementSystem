from data_access.data_operations import BaseDAO

class CourseDAO(BaseDAO):
    """
        CourseDAO class for managing course-related operations in the system.
        Includes methods for creating, updating, deleting, and retrieving course records.
        Methods:
            update_course(course_id, course_name=None, teacher_id=None, max_students=None, cost=None):
                Updates the details of an existing course, including its name, teacher, max students, and cost.
            delete_course(course_id):
                Deletes a course from the database by its ID.
            get_course_by_id(course_id):
                Retrieves a course record by its ID.
            get_all_courses():
                Retrieves all course records in the system.
            get_course_name():
                This function retrieves the name of a course from the database based on the given `course_id`.

            close():
                Closes the DAO connection.
                """
    def __init__(self):
        super().__init__()

    def update_course(self, course_id, course_name=None, teacher_id=None, max_students=None, cost=None):
        query = "UPDATE Courses SET "
        params = []
        if course_name:
            query += "course_name = %s, "
            params.append(course_name)
        if teacher_id:
            query += "teacher_id = %s, "
            params.append(teacher_id)
        if max_students:
            query += "max_students = %s, "
            params.append(max_students)
        if cost:
            query += "cost = %s, "
            params.append(cost)
        query = query.rstrip(", ") + " WHERE course_id = %s"
        params.append(course_id)
        try:
            self.cursor.execute(query, tuple(params))
            self.connection.commit()
            print(f"Course ID {course_id} updated successfully.")
        except Exception as e:
            print(f"Error updating course ID {course_id}: {e}")

    def delete_course(self, course_id):
        query = "DELETE FROM Courses WHERE course_id = %s"
        try:
            self.cursor.execute(query, (course_id,))
            self.connection.commit()
            print(f"Course ID {course_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting course ID {course_id}: {e}")

    def get_course_by_id(self, course_id):
        query = """
           SELECT course_id, course_name, teacher_id, max_students
           FROM Courses
           WHERE course_id = %s
           """
        try:
            self.cursor.execute(query, (course_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching course {course_id}: {e}")
            return None


    def get_all_courses(self):
        query = "SELECT * FROM Courses"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all courses: {e}")
            return []

    #הוספת מתודה
    def get_course_name(self, course_id):
        query = """
        SELECT course_name FROM Courses WHERE course_id = %s
        """
        try:
            self.cursor.execute(query, (course_id,))
            result = self.cursor.fetchone()
            return result["course_name"] if result else None
        except Exception as e:
            print(f"Error fetching course name: {e}")
            return None


    def close(self):
        super().close()
