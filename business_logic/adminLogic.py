from data_access.admin_dao import AdminDAO
from business_logic.workerLogic import WorkerLogic

class AdminLogic(WorkerLogic, ):
    def __init__(self, creator_role, admin_id=None, name=None, email=None, password=None, role="Admin", salary=None, budget=None):
        super().__init__(creator_role, worker_id=admin_id, name=name, email=email, password=password, role=role, salary=salary)
        self.admin_id = admin_id
        self.budget = budget
        self.admin_dao = AdminDAO()

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Budget must be a numeric value.")
        if value < 0:
            raise ValueError("Budget cannot be negative.")
        self._budget = value

    def get_admin(self):
        try:
            admin = self.admin_dao.get_admin_by_id(self.admin_id)
            if admin:
                return admin
            else:
                print(f"No admin found with ID {self.admin_id}.")
                return None
        except Exception as e:
            print(f"Error fetching admin: {e}")
            return None

    def is_admin(self):
        try:
            return self.admin_dao.is_admin(self.admin_id)
        except Exception as e:
            print(f"Error checking if admin: {e}")
            return False

    def update_admin(self, name=None, email=None, password=None, new_salary=None, new_budget=None):
        try:
            if name or email or password:
                self.user_dao.update_user(self.admin_id, name=name, email=email, password=password)

            if new_salary is not None:
                self.salary = new_salary
                self.worker_dao.update_worker(self.admin_id, salary=self.salary)

            if new_budget is not None:
                self.budget = new_budget
                self.admin_dao.update_admin(self.admin_id, budget=self.budget)

            print(f"Admin with ID {self.admin_id} updated successfully.")
        except Exception as e:
            print(f"Error updating admin: {e}")

    def create_course(self, course_name, teacher_id, max_students, cost):
        try:
            self.admin_dao.create_course(course_name, teacher_id, max_students, cost)
            print(f"Course '{course_name}' created successfully.")
        except Exception as e:
            print(f"Error creating course: {e}")

    def assign_teacher_to_course(self, teacher_id, course_id):
        try:
            self.admin_dao.assign_teacher_to_course(teacher_id, course_id)
            print(f"Teacher {teacher_id} assigned to course {course_id} successfully.")
        except Exception as e:
            print(f"Error assigning teacher to course: {e}")

    def manage_waitlist(self, student_id, course_id, action):
        try:
            self.admin_dao.manage_waitlist(student_id, course_id, action)
            print(f"Waitlist for course {course_id} updated successfully with action '{action}' for student {student_id}.")
        except Exception as e:
            print(f"Error managing waitlist: {e}")

    def create_task(self, description, status="Pending", maintenance_worker_id=None):
        try:
            self.admin_dao.create_task(description, status, maintenance_worker_id)
            print(f"Task '{description}' created successfully.")
        except Exception as e:
            print(f"Error creating task: {e}")


    def generate_financial_report(self):
        try:
            report = self.admin_dao.generate_financial_report()
            print("Financial report generated successfully.")
            return report
        except Exception as e:
            print(f"Error generating financial report: {e}")
            return []
