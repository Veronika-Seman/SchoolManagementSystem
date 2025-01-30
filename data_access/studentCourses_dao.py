from data_access.data_operations import BaseDAO

class StudentCoursesDAO(BaseDAO):
    """
    StudentCoursesDAO class for managing student-course relationships in the database.
    Provides methods for adding/removing students from courses, and retrieving course and student details.
    Methods:
        remove_student_from_course(student_id, course_id):Removes a student from a specific course.
        get_courses_by_student(student_id): Retrieves all courses that a specific student is enrolled in.
        get_students_by_course(course_id): Retrieves all students enrolled in a specific course.
        get_all_student_courses(): Retrieves all student-course relationships in the system.
        enroll_student_in_course(self, student_id, course_id): This function enrolls a student in
        a course by inserting their `student_id` and `course_id` into the `StudentCourses` table.
        close():Closes the DAO connection and cleans up associated resources.
        """
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

    def enroll_student_in_course(self, student_id, course_id):
        query = """
        INSERT INTO StudentCourses (student_id, course_id)
        VALUES (%s, %s)
        """
        try:
            self.cursor.execute(query, (student_id, course_id))
            self.connection.commit()
            print(f"Student {student_id} enrolled in course {course_id} successfully.")
        except Exception as e:
            print(f"Error enrolling student {student_id} in course {course_id}: {e}")

    def close(self):
        super().close()
