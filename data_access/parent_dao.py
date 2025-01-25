from data_access.data_operations import BaseDAO
from data_access.student_dao import StudentDAO
from data_access.waitlist_dao import WaitlistDAO


class ParentDAO(BaseDAO):
    def __init__(self):
        super().__init__()
        self.waitlist_dao = WaitlistDAO
        self.student_dao = StudentDAO()

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

    def generate_payment_report(self, parent_id):
        query = """
        SELECT p.payment_id, c.course_name, p.amount, p.payment_date
        FROM Payments p
        JOIN Courses c ON p.course_id = c.course_id
        WHERE p.parent_id = %s
        """
        try:
            self.cursor.execute(query, (parent_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error generating payment report for parent {parent_id}: {e}")
            return []

    def pay_for_course(self, parent_id, course_id, amount):
        query = """
        INSERT INTO Payments (parent_id, course_id, amount, payment_date)
        VALUES (%s, %s, %s, CURDATE())
        """
        try:
            self.cursor.execute(query, (parent_id, course_id, amount))
            self.connection.commit()
            print(f"Payment of {amount} for course {course_id} by parent {parent_id} was successful.")
        except Exception as e:
            print(f"Error processing payment for parent {parent_id}: {e}")

    def get_student_waitlist_position(self, student_id, course_id):
        return self.waitlist_dao.get_student_position(student_id, course_id)

    def get_child_grades(self, student_id):
        return self.student_dao.get_grades(student_id)

    def get_child_schedule(self, student_id):
        return self.student_dao.get_schedule(student_id)

    def close(self):
        self.student_dao.close()
        super().close()
