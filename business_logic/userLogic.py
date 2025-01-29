import hashlib

from data_access.user_dao import UserDAO
from data_access.admin_dao import AdminDAO
from data_access.teacher_dao import TeacherDAO
from data_access.maintenanceWorker_dao import MaintenanceWorkerDAO
from data_access.parent_dao import ParentDAO
from data_access.student_dao import StudentDAO
import re
class UserLogic:

    VALID_ROLES = ["Admin", "Teacher", "MaintenanceWorker", "Parent", "Student"]

    def __init__(self, creator_role, id_number=None, name=None, email=None, password=None, role=None):
        self.creator_role = creator_role
        self._id_number = id_number
        self._name = name
        self._email = email
        self._password = password
        self._role = role
        self.user_dao = UserDAO()
        self.admin_dao = AdminDAO()
        self.teacher_dao = TeacherDAO()
        self.maintenance_worker_dao = MaintenanceWorkerDAO()
        self.parent_dao = ParentDAO()
        self.student_dao = StudentDAO()
        self.current_user = None

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        self._name = value

    @property
    def email(self):
        return self._email

    @staticmethod
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @email.setter
    def email(self, value):
        if not self.is_valid_email(value):
            raise ValueError("Invalid email address.")
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value or len(value) < 2:
            raise ValueError("Password must be at least 2 characters long.")
        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in self.VALID_ROLES:
            raise ValueError(f"Invalid role. Must be one of: {', '.join(self.VALID_ROLES)}.")
        self._role = value

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, email, password):
        user = self.user_dao.get_user_by_email(email)
        if user and self.hash_password(password) == user[2]:
            self.current_user = {
                "user_id": user[0],
                "email": user[1],
                "role": user[3]
            }
            print(f"✅ Login successful! Welcome {self.current_user['email']}.")
            return True
        else:
            print("❌ Invalid email or password.")
            return False

    def logout(self):
        if self.current_user:
            print(f"👋 User {self.current_user['email']} logged out.")
            self.current_user = None
        else:
            print("⚠ No user is logged in.")

    def get_current_user(self):
        return self.current_user

    def create_user_with_role(self, id_number, name, email, password, role, **kwargs):
        try:
            # Ensure only Admin can create users
            if self.creator_role != "Admin":
                raise PermissionError("Only admins can create users.")

            # Validate inputs
            self.id_number = id_number
            self.name = name
            self.email = email
            self.password = password
            self.role = role

            # Check if user already exists
            if self.user_dao.user_exists(id_number):
                raise ValueError(f"User with ID {id_number} already exists.")

            # Create user in Users table
            self.user_dao.create_user(
                id_number=id_number,
                name=name,
                email=email,
                password=password,
                role=role
            )

            # Add user to role-specific table
            if role == "Admin":
                salary = kwargs.get("salary")
                budget = kwargs.get("budget")
                if salary is None or budget is None:
                    raise ValueError("Admin requires 'salary' and 'budget'.")
                self.admin_dao.create_admin(
                    admin_id=id_number, name=name, email=email, password=password, salary=salary, budget=budget
                )

            elif role == "Teacher":
                salary = kwargs.get("salary")
                subject = kwargs.get("subject")
                if salary is None or subject is None:
                    raise ValueError("Teacher requires 'salary' and 'subject'.")
                self.teacher_dao.create_teacher(
                    teacher_id=id_number, name=name, email=email, password=password, salary=salary, subject=subject
                )

            elif role == "MaintenanceWorker":
                salary = kwargs.get("salary")
                if salary is None:
                    raise ValueError("MaintenanceWorker requires 'salary'.")
                self.maintenance_worker_dao.create_maintenance_worker(
                    maintenance_worker_id=id_number, name=name, email=email, password=password, salary=salary
                )

            elif role == "Parent":
                self.parent_dao.create_parent(parent_id=id_number, name=name, email=email, password=password)

            elif role == "Student":
                parent_id = kwargs.get("parent_id")
                if parent_id is None:
                    raise ValueError("Student requires 'parent_id'.")
                self.student_dao.create_student(
                    student_id=id_number, name=name, email=email, password=password, parent_id=parent_id
                )
            else:
                raise ValueError(f"Invalid role: {role}")

            print(f"User {id_number} with role {role} created successfully.")

        except PermissionError as pe:
            print(f"Permission Error: {pe}")
            raise
        except ValueError as ve:
            print(f"Validation Error: {ve}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def get_user_by_id(self, id_number):
        try:
            user = self.user_dao.get_user_by_id(id_number)
            if user is None:
                print(f"User with ID {id_number} not found.")
                return None
            return user
        except Exception as e:
            print(f"Error fetching user by ID {id_number}: {e}")
            raise

    def get_user_by_email(self, email):
        try:
            user = self.user_dao.get_user_by_email(email)
            if user is None:
                print(f"User with email {email} not found.")
                return None
            return user
        except Exception as e:
            print(f"Error fetching user by email {email}: {e}")
            raise

    def update_user(self, id_number, name=None, email=None, password=None):
        try:
            # Validate inputs
            if not self.user_dao.user_exists(id_number):
                raise ValueError(f"User with ID {id_number} does not exist.")

            if email and not self.is_valid_email(email):
                raise ValueError("Invalid email address.")

            self.user_dao.update_user(id_number, name=name, email=email, password=password)
            print(f"User {id_number} updated successfully.")
        except ValueError as ve:
            print(f"Validation Error: {ve}")
            raise
        except Exception as e:
            print(f"Error updating user {id_number}: {e}")
            raise

    def delete_user(self, id_number):
        try:
            if not self.user_dao.user_exists(id_number):
                raise ValueError(f"User with ID {id_number} does not exist.")

            self.user_dao.delete_user(id_number)
            print(f"User {id_number} deleted successfully.")
        except ValueError as ve:
            print(f"Validation Error: {ve}")
            raise
        except Exception as e:
            print(f"Error deleting user {id_number}: {e}")
            raise
