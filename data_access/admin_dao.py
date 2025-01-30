from data_access.data_operations import BaseDAO
from data_access.parent_dao import ParentDAO
from data_access.student_dao import StudentDAO
from data_access.teacher_dao import TeacherDAO
from data_access.user_dao import UserDAO
from data_access.worker_dao import WorkerDAO
from data_access.maintenanceWorker_dao import MaintenanceWorkerDAO
from data_access.maintenanceTasks_dao import MaintenanceTaskDAO

class AdminDAO(MaintenanceTaskDAO, BaseDAO):
    """
       AdminLogic handles the business logic for Admin users in the system.
       This class extends WorkerLogic and provides additional functionality specific to administrators.
       It interacts with AdminDAO for data operations related to admins, courses, and financial management.

       Methods:
       - get_admin(): Retrieves admin details by ID.
       - is_admin(): Checks if the current user is an admin.
       - update_admin(): Updates admin details such as name, email, password, salary, or budget.
       - create_course(): Creates a new course.
       - assign_teacher_to_course(): Assigns a teacher to a course.
       - create_task(): Creates and assigns tasks.
       - generate_financial_report(): Generates a financial report.
       """
    def __init__(self):
        self.parent_dao = ParentDAO()
        self.maintenance_worker_dao = MaintenanceWorkerDAO()
        self.user_dao = UserDAO()
        self.teacher_dao = TeacherDAO()
        self.student_dao = StudentDAO()
        self.worker_dao = WorkerDAO()
        super().__init__()

    def create_admin(self, admin_id, name, email, password, salary, budget):
        try:
            user_dao = UserDAO()
            user_dao.create_user(id_number=admin_id, name=name, email=email, password=password, role='Admin')

            worker_dao = WorkerDAO()
            worker_dao.create_worker(worker_id=admin_id, salary=salary)

            query = """
            INSERT INTO Admins (admin_id, budget)
            VALUES (%s, %s)
            """
            self.cursor.execute(query, (admin_id, budget))
            self.connection.commit()
            print(f"Admin with ID {admin_id} created successfully.")
        except Exception as e:
            print(f"Error creating admin: {e}")


    def get_admin_by_id(self, admin_id):
        query = "SELECT * FROM Admins WHERE admin_id = %s"
        try:
            self.cursor.execute(query, (admin_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching admin with ID {admin_id}: {e}")
            return None

    def is_admin(self, admin_id):
        query = "SELECT 1 FROM Admins WHERE admin_id = %s"
        try:
            self.cursor.execute(query, (admin_id,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print(f"Error checking if admin: {e}")
            return False

    def update_admin(self, admin_id, name=None, email=None, password=None, salary=None, budget=None):
        user_dao = UserDAO()
        user_dao.update_user(admin_id, name=name, email=email, password=password)

        worker_dao = WorkerDAO()
        worker_dao.update_worker(worker_id=admin_id, salary=salary)

        if budget is not None:
            query = "UPDATE Admins SET budget = %s WHERE admin_id = %s"
            try:
                self.cursor.execute(query, (budget, admin_id))
                self.connection.commit()
                print(f"Admin {admin_id} updated successfully.")
            except Exception as e:
                print(f"Error updating admin: {e}")

    def create_course(self, course_name, teacher_id, max_students, cost):
        query = """
        INSERT INTO Courses (course_name, teacher_id, max_students, cost)
        VALUES (%s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, (course_name, teacher_id, max_students, cost))
            self.connection.commit()
        except Exception as e:
            print(f"Error creating course: {e}")

    def assign_teacher_to_course(self, teacher_id, course_id):
        query = """
        UPDATE Courses
        SET teacher_id = %s
        WHERE course_id = %s
        """
        try:
            self.cursor.execute(query, (teacher_id, course_id))
            self.connection.commit()
        except Exception as e:
            print(f"Error assigning teacher to course: {e}")

    def create_task(self, description, status="Pending", maintenance_worker_id=None):
        query = """
        INSERT INTO MaintenanceTasks (description, status, maintenance_worker_id)
        VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(query, (description, status, maintenance_worker_id))
            self.connection.commit()
            print(f"Task '{description}' created successfully.")
        except Exception as e:
            print(f"Error creating task: {e}")


    def generate_financial_report(self):
        query = """
        SELECT 'Payments' AS category, SUM(amount) AS total
        FROM Payments
        UNION ALL
        SELECT 'Salaries', SUM(Workers.salary)
        FROM Workers
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error generating financial report: {e}")
            return []

    def close(self):
        super().close()

