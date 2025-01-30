from business_logic.workerLogic import WorkerLogic
from data_access.teacher_dao import TeacherDAO
from business_logic.enrollmentLogic import EnrollmentLogic


class TeacherLogic(WorkerLogic, EnrollmentLogic):
    """
      The TeacherLogic class manages the business logic related to teacher operations.
      It inherits from WorkerLogic for worker-specific functionality and EnrollmentLogic
      for managing course enrollments. The class interacts with the TeacherDAO for database operations.
      Methods:
          __init__(self, creator_role=None, teacher_id=None, name=None, email=None, password=None, role="Teacher", salary=0, subject=None):
              Initializes the TeacherLogic object with necessary details and the associated TeacherDAO.
          subject(self):The getter and setter for the subject the teacher teaches.
          get_teacher(self): Retrieves a teacher by their unique ID.
          update_teacher(self, new_name=None, new_email=None, new_password=None, new_salary=None, new_subject=None):Updates the teacher's details (name, email, password, salary, subject).
          get_students_in_course(self, course_id):Retrieves a list of students enrolled in the course assigned to the teacher.
          insert_student_grade(self, student_id, course_id, grade):Adds or updates a student's grade for a specific course.
          report_class_issue(self, class_id, description):Reports an issue with a particular class.
          get_student_grades(self, student_id):Retrieves the grades for a specific student.
      """
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
            print(f"DEBUG: Calling DAO with worker_id={self.worker_id}, course_id={course_id}")
            students = self.teacher_dao.get_students_in_course(course_id)
            print(f"DEBUG: Students fetched from DAO -> {students}")
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
