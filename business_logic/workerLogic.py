from data_access.worker_dao import WorkerDAO
from business_logic.userLogic import UserLogic


class WorkerLogic(UserLogic):
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
