from data_access.worker_dao import WorkerDAO
from business_logic.userLogic import UserLogic


class WorkerLogic(UserLogic):
    """
        A class responsible for managing worker-related functionalities in the system. It extends the UserLogic class to inherit
        user management features and adds specific worker-related actions such as updating salary and fetching worker details.
        Methods:
        - __init__(self, creator_role, worker_id=None, name=None, email=None, password=None, role="Worker", salary=0):
            Initializes the WorkerLogic object with the creator's role, worker details, and salary, and sets up the WorkerDAO.
        - worker_id(self):Getter and setter for worker ID. Ensures the worker ID is not empty.
        - salary(self):Getter and setter for salary. Ensures salary is a positive numeric value.
        - get_worker(self):Fetches worker details from the WorkerDAO by worker ID.
        - update_worker(self, new_salary=None):Updates worker details, specifically the salary, and stores the changes in the database via the WorkerDAO.
        """
    def __init__(self, creator_role, worker_id=None, name=None, email=None, password=None, role="Worker", salary=0):
        super().__init__(creator_role, id_number=worker_id, name=name, email=email, password=password, role=role)
        self.worker_id = worker_id
        self.salary = salary
        self.worker_dao = WorkerDAO()

    @property
    def worker_id(self):
        return self._worker_id

    @worker_id.setter
    def worker_id(self, value):
        if not value:
            raise ValueError("Worker ID cannot be empty.")
        self._worker_id = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value is None:
            raise ValueError("Salary must be provided.")
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be a numeric value (int or float).")
        if value < 0:
            raise ValueError("Salary must be a positive number.")
        self._salary = value

    def get_worker(self):
        try:
            worker = self.worker_dao.get_worker_by_id(self.worker_id)
            if worker:
                return worker
            else:
                print(f"No worker found with ID {self.worker_id}.")
                return None
        except Exception as e:
            print(f"Error fetching worker: {e}")
            return None

    def update_worker(self, new_salary=None):
        try:
            if new_salary is not None:
                self.salary = new_salary
                self.worker_dao.update_worker(self.worker_id, salary=self.salary)
                print(f"Worker with ID {self.worker_id} updated successfully.")
            else:
                print("No updates were provided.")
        except Exception as e:
            print(f"Error updating worker: {e}")
