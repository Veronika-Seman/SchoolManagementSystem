from data_access.data_operations import BaseDAO
from data_access.student_dao import StudentDAO
from data_access.user_dao import UserDAO
from data_access.waitlist_dao import WaitlistDAO

class ParentDAO(BaseDAO):
    """
       ParentDAO class for managing operations related to parents and their children in the system.
       Provides methods for creating parents, generating payment reports,
       and retrieving information about students' grades and schedules.
       Methods:
           create_parent(parent_id, name, email, password): Creates a new parent in the system and associates the parent with a user account.
           get_parent_by_id(parent_id):Retrieves a parent by their ID.
           generate_payment_report(parent_id):Generates a payment report for a specified parent.
           pay_for_course(parent_id, course_id, amount):Processes a payment for a parent for a specific course.
           get_student_waitlist_position(student_id, course_id):Retrieves the waitlist position of a student in a specific course.
           get_child_grades(student_id):Retrieves the grades of a child/student.
           get_child_schedule(student_id):Retrieves the schedule of a child/student.
           close():Closes the DAO connection and cleans up associated resources.
       """
    def __init__(self):
        super().__init__()
        self.waitlist_dao = WaitlistDAO
        self.student_dao = StudentDAO()

    def create_parent(self, parent_id, name, email, password):
        try:
            user_dao = UserDAO()
            user_dao.create_user(id_number=parent_id, name=name, email=email, password=password, role="Parent")

            query = """
                        INSERT INTO Parents (parent_id)
                        VALUES (%s)
                        """
            self.cursor.execute(query, (parent_id,))
            self.connection.commit()
            print(f"Parent with ID {parent_id} created successfully.")
        except Exception as e:
            print(f"Error creating parent: {e}")
            raise

    def get_parent_by_id(self, parent_id):
        query = """
        SELECT u.id_number, u.name, u.email, p.parent_id
        FROM Users u
        JOIN Parents p ON u.id_number = p.parent_id
        WHERE u.id_number = %s
        """
        try:
            self.cursor.execute(query, (parent_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching parent by ID {parent_id}: {e}")
            return None

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
        self.waitlist_dao.close()
        super().close()

