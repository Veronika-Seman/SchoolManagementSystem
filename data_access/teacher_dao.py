from data_access.data_operations import BaseDAO
from data_access.student_dao import StudentDAO
from data_access.user_dao import UserDAO
from data_access.waitlist_dao import WaitlistDAO
from data_access.worker_dao import WorkerDAO
from data_access.parent_dao import ParentDAO

class TeacherDAO(BaseDAO):
    """
      TeacherDAO class for interacting with the 'Teachers' table and related tables.
      It provides methods for creating, reading, updating, and managing teachers,
      as well as enrolling students in courses and handling grades.
      Methods:
          create_teacher(teacher_id, name, email, password, salary, subject): Creates a new teacher record.
          teacher_exists(teacher_id): Checks if a teacher exists by their ID.
          get_teacher_by_id(teacher_id): Retrieves teacher details by ID, including user data.
          update_teacher(teacher_id, name=None, email=None, password=None, salary=None, subject=None): Updates teacher details.
          get_students_in_course(self, course_id): Retrieves students enrolled in a course taught by a specific course id.
          insert_student_grade(student_id, course_id, grade): Inserts or updates a student's grade for a course.
          report_class_issue(class_id, description): Reports an issue with a class for maintenance.
           def get_student_grades(self, student_id): fetch grades for specific student.
          close(): Closes the DAO connections.
      """
    def __init__(self):
        super().__init__()
        self.student_dao = StudentDAO()
        self.waitlist_dao = WaitlistDAO()
        self.parent_dao = ParentDAO()

    def create_teacher(self, teacher_id, name, email, password, salary, subject):
        try:
            user_dao = UserDAO()
            user_dao.create_user(id_number=teacher_id, name=name, email=email, password=password, role='Teacher')

            worker_dao = WorkerDAO()
            worker_dao.create_worker(worker_id=teacher_id, salary=salary)

            create_teacher_query = """
            INSERT INTO Teachers (teacher_id, subject)
            VALUES (%s, %s)
            """
            self.cursor.execute(create_teacher_query, (teacher_id, subject))
            self.connection.commit()
            print(f"Teacher with ID {teacher_id} created successfully.")
        except Exception as e:
            print(f"Error creating teacher: {e}")


    def teacher_exists(self, teacher_id):
        query = "SELECT * FROM Teachers WHERE teacher_id = %s"
        self.cursor.execute(query, (teacher_id,))
        return self.cursor.fetchone() is not None


    def get_teacher_by_id(self, teacher_id):
        query = """
        SELECT t.teacher_id, u.name, u.email, t.subject, t.salary
        FROM Teachers t
        JOIN Users u ON t.teacher_id = u.id_number
        WHERE t.teacher_id = %s
        """
        try:
            self.cursor.execute(query, (teacher_id,))
            teacher = self.cursor.fetchone()
            if teacher:
                print(f"Teacher found: {teacher}")
            else:
                print(f"No teacher found with ID: {teacher_id}")
            return teacher
        except Exception as e:
            print(f"Error fetching teacher by ID: {e}")
            return None

    def update_teacher(self, teacher_id, name=None, email=None, password=None, salary=None, subject=None):
        user_dao = UserDAO()
        user_dao.update_user(teacher_id, name=name, email=email, password=password)

        worker_dao = WorkerDAO()
        worker_dao.update_worker(worker_id=teacher_id, salary=salary)

        if subject is not None:
            query = "UPDATE Teachers SET subject = %s WHERE teacher_id = %s"
            try:
                self.cursor.execute(query, (subject, teacher_id))
                self.connection.commit()
                print(f"Teacher {teacher_id} updated successfully.")
            except Exception as e:
                print(f"Error updating teacher: {e}")

    def get_students_in_course(self, course_id):
        query = """
            SELECT s.student_id, u.name, u.email
            FROM StudentCourses sc
            JOIN Students s ON sc.student_id = s.student_id
            JOIN Users u ON s.student_id = u.id_number
            WHERE sc.course_id = %s
            """
        try:
            self.cursor.execute(query, (course_id,))
            students = self.cursor.fetchall()
            print(f"DEBUG: Students fetched from DB -> {students}")
            return students
        except Exception as e:
            print(f"Error fetching students for course {course_id}: {e}")
            return []

    def insert_student_grade(self, student_id, course_id, grade):
        query = """
        INSERT INTO Grades (student_id, course_id, grade)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE grade = %s
        """
        try:
            self.cursor.execute(query, (student_id, course_id, grade, grade))
            self.connection.commit()
            print(f"Grade {grade} for student {student_id} in course {course_id} added/updated successfully.")
        except Exception as e:
            print(f"Error inserting/updating grade: {e}")

    def report_class_issue(self, class_id, description):
        query = """
        INSERT INTO MaintenanceTasks (description, status, maintenance_worker_id)
        VALUES (%s, 'Pending', NULL)
        """
        try:
            self.cursor.execute(query, (description,))
            self.connection.commit()
            print(f"Issue reported for class {class_id} successfully.")
        except Exception as e:
            print(f"Error reporting issue for class: {e}")

    def get_student_grades(self, student_id):
        return self.student_dao.get_grades(student_id)

    def close(self):
        self.parent_dao.close()
        self.waitlist_dao.close()
        super().close()

