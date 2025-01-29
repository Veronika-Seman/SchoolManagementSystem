from business_logic.userLogic import UserLogic
from data_access.student_dao import StudentDAO

class StudentLogic(UserLogic):
    def __init__(self, creator_role, student_id=None, name=None, email=None, password=None, parent_id=None):
        super().__init__(creator_role, id_number=student_id, name=name, email=email, password=password, role="Student")
        self.student_id = student_id
        self.parent_id = parent_id
        self.student_dao = StudentDAO()

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not value:
            raise ValueError("Student ID cannot be empty.")
        self._student_id = value

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        if not value:
            raise ValueError("Each student must have a parent ID.")
        self._parent_id = value

    def get_student_by_id(self):
        try:
            student = self.student_dao.get_student_by_id(self.student_id)
            if not student:
                print(f"Student with ID {self.student_id} not found.")
            return student
        except Exception as e:
            print(f"Error fetching student by ID: {e}")
            return None

    def get_all_students(self):
        try:
            students = self.student_dao.get_all_students()
            if not students:
                print("No students found.")
            return students
        except Exception as e:
            print(f"Error fetching all students: {e}")
            return []

    def get_grades(self):
        try:
            grades = self.student_dao.get_grades(self.student_id)
            if not grades:
                print(f"No grades found for student {self.student_id}.")
            return grades
        except Exception as e:
            print(f"Error fetching grades for student {self.student_id}: {e}")
            return []

    def get_schedule(self):
        try:
            schedule = self.student_dao.get_schedule(self.student_id)
            if not schedule:
                print(f"No schedule found for student {self.student_id}.")
            return schedule
        except Exception as e:
            print(f"Error fetching schedule for student {self.student_id}: {e}")
            return []

    def get_student_waitlist_position(self, course_id):
        try:
            position = self.student_dao.get_student_waitlist_position(self.student_id, course_id)
            if position is None:
                print(f"Student {self.student_id} is not on the waitlist for course {course_id}.")
            return position
        except Exception as e:
            print(f"Error fetching waitlist position for student {self.student_id} in course {course_id}: {e}")
            return None
