from data_access.data_operations import BaseDAO

class GradesDAO(BaseDAO):
    """
       GradesDAO class for managing grade-related operations in the system.
       Includes methods for retrieving, updating, and deleting grades associated with students and courses.
       Methods:
           get_grades_by_course(course_id):
               Retrieves all grades for a given course, including student IDs and names.
           update_grade(student_id, course_id, grade):
               Updates the grade for a specific student in a given course.
           delete_grade(student_id, course_id):
               Deletes the grade for a specific student in a given course.
           close():
               Closes the DAO connection.
       """
    def __init__(self):
        super().__init__()

    def get_grades_by_course(self, course_id):
        query = """
        SELECT g.student_id, u.name, g.grade
        FROM Grades g
        JOIN Students s ON g.student_id = s.student_id
        JOIN Users u ON s.student_id = u.id_number
        WHERE g.course_id = %s
        """
        try:
            self.cursor.execute(query, (course_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching grades for course {course_id}: {e}")
            return []

    def update_grade(self, student_id, course_id, grade):
        query = """
        UPDATE Grades
        SET grade = %s
        WHERE student_id = %s AND course_id = %s
        """
        try:
            self.cursor.execute(query, (grade, student_id, course_id))
            self.connection.commit()
            print(f"Grade updated for student {student_id} in course {course_id} to {grade}.")
        except Exception as e:
            print(f"Error updating grade: {e}")

    def delete_grade(self, student_id, course_id):
        query = """
        DELETE FROM Grades
        WHERE student_id = %s AND course_id = %s
        """
        try:
            self.cursor.execute(query, (student_id, course_id))
            self.connection.commit()
            print(f"Grade for student {student_id} in course {course_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting grade: {e}")

    def close(self):
        super().close()
