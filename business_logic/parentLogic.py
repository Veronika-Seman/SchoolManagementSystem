from business_logic.waitlistLogic import WaitlistLogic
from data_access.course_dao import CourseDAO
from data_access.parent_dao import ParentDAO
from business_logic.userLogic import UserLogic
from data_access.studentCourses_dao import StudentCoursesDAO
from business_logic.enrollmentLogic import EnrollmentLogic


class ParentLogic(UserLogic, EnrollmentLogic):
    def __init__(self, creator_role, parent_id=None, name=None, email=None, password=None):
        super().__init__(creator_role, id_number=parent_id, name=name, email=email, password=password, role="Parent")
        self.waitlist_dao = None
        self.studentLogic = None
        self.waitlist_logic = WaitlistLogic()
        self.course_dao = CourseDAO()
        self.parent_dao = ParentDAO()
        self.studentCourses_dao = StudentCoursesDAO()
        EnrollmentLogic.__init__(self)

    def get_parent_by_id(self, parent_id):
        if not parent_id:
            raise ValueError("Parent ID cannot be empty.")
        try:
            parent = self.parent_dao.get_parent_by_id(parent_id)
            if not parent:
                print(f"Parent with ID {parent_id} not found.")
            return parent
        except Exception as e:
            print(f"Error fetching parent by ID: {e}")
            return None

    def generate_payment_report(self, parent_id):
        if not parent_id:
            raise ValueError("Parent ID cannot be empty.")
        try:
            payments = self.parent_dao.generate_payment_report(parent_id)
            if not payments:
                print(f"No payments found for parent ID {parent_id}.")
            return payments
        except Exception as e:
            print(f"Error generating payment report for parent {parent_id}: {e}")
            return []

    def pay_for_course(self, course_id, amount):
        if not self.id_number or not course_id or amount is None:
            raise ValueError("Parent ID, Course ID, and Amount must be provided.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        try:
            self.parent_dao.pay_for_course(
                parent_id=self.id_number,
                course_id=course_id,
                amount=amount,
            )
        except Exception as e:
            print(f"Error processing payment: {e}")

    def get_student_waitlist_position(self, student_id, course_id):
        if not student_id or not course_id:
            raise ValueError("Student ID and Course ID must be provided.")
        try:
            position = self.parent_dao.get_student_waitlist_position(student_id, course_id)
            if position is None:
                print(f"Student {student_id} is not on the waitlist for course {course_id}.")
            return position
        except Exception as e:
            print(f"Error fetching waitlist position: {e}")
            return None

    def get_child_grades(self, student_id):
        if not student_id:
            raise ValueError("Student ID cannot be empty.")
        try:
            grades = self.parent_dao.get_child_grades(student_id)
            if not grades:
                print(f"No grades found for student {student_id}.")
            return grades
        except Exception as e:
            print(f"Error fetching grades for student {student_id}: {e}")
            return []

    def get_child_schedule(self, student_id):
        if not student_id:
            raise ValueError("Student ID cannot be empty.")
        try:
            schedule = self.parent_dao.get_child_schedule(student_id)
            if not schedule:
                print(f"No schedule found for student {student_id}.")
            return schedule
        except Exception as e:
            print(f"Error fetching schedule for student {student_id}: {e}")
            return []


    def close(self):
        self.parent_dao.close()
