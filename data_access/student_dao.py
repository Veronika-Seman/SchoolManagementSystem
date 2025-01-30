from data_access.data_operations import BaseDAO
from data_access.user_dao import UserDAO
from data_access.waitlist_dao import WaitlistDAO

class StudentDAO(BaseDAO):
    """
        StudentDAO class for managing student-related database operations.
        Provides methods for creating students, fetching student details, grades, schedules, and waitlist positions.

        Methods:
            create_student(student_id, name, email, password, parent_id=None):Creates a new student entry in the system, including user and student records.
            get_student_by_id(student_id):Retrieves a student by their ID, including basic user information.
            get_all_students():Retrieves all students along with their associated user information.
            get_grades(student_id): Retrieves all grades for a specific student.
            get_schedule(student_id): Retrieves the schedule for a specific student, including course and class details.
            get_student_waitlist_position(student_id, course_id):Retrieves the waitlist position for a student in a specific course.
            close(): Closes the DAO connection and cleans up associated resources.
        """
    def __init__(self):
        super().__init__()
        self.waitlist_dao = WaitlistDAO

    def create_student(self, student_id, name, email, password, parent_id=None):
        try:
            user_dao = UserDAO()
            user_dao.create_user(id_number=student_id, name=name, email=email, password=password, role="Student")

            query = """
              INSERT INTO Students (student_id, parent_id)
              VALUES (%s, %s)
             """
            self.cursor.execute(query, (student_id, parent_id if parent_id else None))
            self.connection.commit()

            print(f"Student with ID {student_id} created successfully.")
        except Exception as e:
            print(f"Error creating student: {e}")

    def get_student_by_id(self, student_id):
        query = """
        SELECT s.student_id, u.name, u.email, u.role, s.parent_id
        FROM Students s
        JOIN Users u ON s.student_id = u.id_number
        WHERE s.student_id = %s
        """
        try:
            self.cursor.execute(query, (student_id,))
            result = self.cursor.fetchone()
            if result:
                return result
            else:
                print(f"Student with ID {student_id} not found.")
                return None
        except Exception as e:
            print(f"Error fetching student by ID: {e}")
            return None

    def get_all_students(self):
        query = """
        SELECT s.student_id, u.name, u.email, u.password
        FROM Students s
        JOIN Users u ON s.student_id = u.id_number
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all students: {e}")
            return []

    def get_grades(self, student_id):
        query = """
        SELECT g.course_id, c.course_name, g.grade
        FROM Grades g
        JOIN Courses c ON g.course_id = c.course_id
        WHERE g.student_id = %s
        """
        try:
            self.cursor.execute(query, (student_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching grades for student {student_id}: {e}")
            return []

    def get_schedule(self, student_id):
        query = """
        SELECT s.day, s.hour, c.course_name, cl.classroom_name
        FROM Schedules s
        JOIN Courses c ON s.course_id = c.course_id
        JOIN Classes cl ON s.class_id = cl.class_id
        WHERE s.student_id = %s
        ORDER BY s.day, s.hour
        """
        try:
            self.cursor.execute(query, (student_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching schedule for student {student_id}: {e}")
            return []

    def get_student_waitlist_position(self, student_id, course_id):
        return self.waitlist_dao.get_student_position(student_id, course_id)


    def close(self):
        super().close()
