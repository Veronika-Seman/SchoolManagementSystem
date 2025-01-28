from business_logic.workerLogic import WorkerLogic
from data_access.maintenance_worker import MaintenanceWorkerDAO

class MaintenanceWorkerLogic(WorkerLogic):
    def __init__(self, creator_role, maintenance_worker_id=None, name=None, email=None, password=None, salary=None):
        super().__init__(creator_role, worker_id=maintenance_worker_id, name=name, email=email, password=password, role="MaintenanceWorker", salary=salary)
        self.maintenance_worker_id = maintenance_worker_id
        self.maintenance_worker_dao = MaintenanceWorkerDAO()

    @property
    def maintenance_worker_id(self):
        return self._maintenance_worker_id

    @maintenance_worker_id.setter
    def maintenance_worker_id(self, value):
        if not value:
            raise ValueError("Maintenance worker ID cannot be empty.")
        self._maintenance_worker_id = value

    def get_assigned_tasks(self):

        try:
            tasks = self.maintenance_worker_dao.get_assigned_tasks(self.maintenance_worker_id)
            if tasks:
                return tasks
            else:
                print(f"No tasks assigned to maintenance worker {self.maintenance_worker_id}.")
                return []
        except Exception as e:
            print(f"Error fetching tasks: {e}")
            return []

    def update_task_status(self, task_id, status):

        try:
            self.maintenance_worker_dao.update_task_status(task_id, status)
            print(f"Task {task_id} status updated to {status}.")
        except Exception as e:
            print(f"Error updating task status: {e}")

    def report_maintenance_issue(self, description):

        try:
            self.maintenance_worker_dao.report_maintenance_issue(description)
            print(f"Maintenance issue reported: {description}")
        except Exception as e:
            print(f"Error reporting maintenance issue: {e}")





