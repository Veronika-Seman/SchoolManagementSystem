from business_logic.workerLogic import WorkerLogic
from data_access.teacher_dao import TeacherDAO
from business_logic.enrollmentLogic import EnrollmentLogic


class TeacherLogic(WorkerLogic, EnrollmentLogic):
    def __init__(self, creator_role=None, teacher_id=None, name=None, email=None, password=None, role="Teacher",
                 salary=0,
                 subject=None):
        super().__init__(creator_role=creator_role, worker_id=teacher_id, name=name, email=email, password=password,
                         role=role,
                         salary=salary)
        self._subject = subject
        self.teacher_dao = TeacherDAO()
        EnrollmentLogic.__init__(self)

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Subject must be a non-empty string.")
        self._subject = value

    def get_teacher(self):
        try:
            teacher = self.teacher_dao.get_teacher_by_id(self.worker_id)
            if teacher:
                return teacher
            else:
                print(f"No teacher found with ID {self.worker_id}.")
                return None
        except Exception as e:
            print(f"Error fetching teacher: {e}")
            return None

    def update_teacher(self, new_name=None, new_email=None, new_password=None, new_salary=None, new_subject=None):
        try:
            if new_name:
                self.name = new_name
            if new_email:
                self.email = new_email
            if new_password:
                self.password = new_password
            if new_salary:
                self.salary = new_salary
            if new_subject:
                self.subject = new_subject

            self.teacher_dao.update_teacher(
                teacher_id=self.worker_id,
                name=self.name,
                email=self.email,
                password=self.password,
                salary=self.salary,
                subject=self.subject
            )
            print(f"Teacher with ID {self.worker_id} updated successfully.")
        except Exception as e:
            print(f"Error updating teacher: {e}")

    def get_students_in_course(self, course_id):
        try:
            students = self.teacher_dao.get_students_in_course(self.worker_id, course_id)
            return students
        except Exception as e:
            print(f"Error fetching students for course {course_id}: {e}")
            return []

    def insert_student_grade(self, student_id, course_id, grade):
        try:
            self.teacher_dao.insert_student_grade(student_id, course_id, grade)
            print(f"Grade {grade} for student {student_id} in course {course_id} added/updated successfully.")
        except Exception as e:
            print(f"Error inserting/updating grade: {e}")

    def report_class_issue(self, class_id, description):
        try:
            self.teacher_dao.report_class_issue(class_id, description)
            print(f"Issue reported for class {class_id} successfully.")
        except Exception as e:
            print(f"Error reporting issue: {e}")

    def get_student_grades(self, student_id):
        if not student_id:
            raise ValueError("Student ID cannot be empty.")
        try:
            grades = self.teacher_dao.get_student_grades(student_id)
            if not grades:
                print(f"No grades found for student {student_id}.")
            return grades
        except Exception as e:
            print(f"Error fetching grades for student {student_id}: {e}")
            return []
