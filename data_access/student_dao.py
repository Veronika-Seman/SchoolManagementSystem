from data_access.data_operations import BaseDAO
from data_access.user_dao import UserDAO


class StudentDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def create_student(self, student_id, name, email, password, parent_id=None):
        try:
            user_dao = UserDAO()
            user_dao.create_user(id_number=student_id, name=name, email=email, password=password, role="Student")

            if parent_id:
                query = """
                INSERT INTO Students (student_id, parent_id)
                VALUES (%s, %s)
                """
                self.cursor.execute(query, (student_id, parent_id))
                self.connection.commit()
            print(f"Student with ID {student_id} created successfully.")
        except Exception as e:
            print(f"Error creating student: {e}")

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

    def get_waitlist_position(self, student_id, course_id):
        query = """
        SELECT position
        FROM Waitlist
        WHERE student_id = %s AND course_id = %s
        """
        try:
            self.cursor.execute(query, (student_id, course_id))
            result = self.cursor.fetchone()
            if result:
                return result['position']
            else:
                print(f"Student {student_id} is not in the waitlist for course {course_id}.")
                return None
        except Exception as e:
            print(f"Error fetching waitlist position for student {student_id} in course {course_id}: {e}")
            return None

    def close(self):
        super().close()
