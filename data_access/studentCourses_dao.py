from data_access.data_operations import BaseDAO

class StudentCoursesDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def remove_student_from_course(self, student_id, course_id):
        query = """
        DELETE FROM StudentCourses
        WHERE student_id = %s AND course_id = %s
        """
        try:
            self.cursor.execute(query, (student_id, course_id))
            self.connection.commit()
            print(f"Student {student_id} removed from course {course_id} successfully.")
        except Exception as e:
            print(f"Error removing student {student_id} from course {course_id}: {e}")

    def get_courses_by_student(self, student_id):
        query = """
        SELECT c.course_id, c.course_name
        FROM StudentCourses sc
        JOIN Courses c ON sc.course_id = c.course_id
        WHERE sc.student_id = %s
        """
        try:
            self.cursor.execute(query, (student_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching courses for student {student_id}: {e}")
            return []

    def get_students_by_course(self, course_id):
        query = """
        SELECT s.student_id, u.name
        FROM StudentCourses sc
        JOIN Students s ON sc.student_id = s.student_id
        JOIN Users u ON s.student_id = u.id_number
        WHERE sc.course_id = %s
        """
        try:
            self.cursor.execute(query, (course_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching students for course {course_id}: {e}")
            return []

    def get_all_student_courses(self):
        query = """
        SELECT sc.student_id, sc.course_id
        FROM StudentCourses sc
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all student-course relations: {e}")
            return []

    def close(self):
        super().close()
