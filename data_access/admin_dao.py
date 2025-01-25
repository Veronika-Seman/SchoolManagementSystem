from data_access.data_operations import BaseDAO
from data_access.user_dao import UserDAO
from data_access.worker_dao import WorkerDAO
from data_access.maintenance_worker import MaintenanceWorkerDAO

class AdminDAO(BaseDAO):
    def __init__(self):
        self.maintenance_worker_dao = MaintenanceWorkerDAO()
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
        VALUES (%s, %s, %s, %s, %s)
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

    def manage_waitlist(self, student_id, course_id, action):

        if action == 'add':
            query = """
            INSERT INTO Waitlist (student_id, course_id, position)
            VALUES (%s, %s, 
            (SELECT IFNULL(MAX(position), 0) + 1 FROM Waitlist WHERE course_id = %s))
            """
            try:
                self.cursor.execute(query, (student_id, course_id, course_id))
                self.connection.commit()
            except Exception as e:
                print(f"Error adding student to waitlist: {e}")
        elif action == 'remove':
            query = """
            DELETE FROM Waitlist
            WHERE student_id = %s AND course_id = %s
            """
            try:
                self.cursor.execute(query, (student_id, course_id))
                self.connection.commit()
            except Exception as e:
                print(f"Error removing student from waitlist: {e}")

    def assign_task_to_worker(self, description, worker_id):
        query = """
        INSERT INTO MaintenanceTasks (description, status, assigned_worker_id)
        VALUES (%s, 'Pending', %s)
        """
        try:
            self.cursor.execute(query, (description, worker_id))
            self.connection.commit()
        except Exception as e:
            print(f"Error assigning task to worker: {e}")

    def update_task_status(self, task_id, status):
        try:
            self.maintenance_worker_dao.update_task_status(task_id, status)
            print(f"Task {task_id} status updated to {status} by admin.")
        except Exception as e:
            print(f"Error updating task status by admin: {e}")

    def generate_financial_report(self):
        query = """
        SELECT 'Payments' AS category, SUM(amount) AS total
        FROM Payments
        UNION ALL
        SELECT 'Salaries', SUM(Workers.salary)
        FROM Workers
        JOIN Users ON Workers.id_number = Users.id_number
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error generating financial report: {e}")
            return []

    def close(self):
        super().close()
