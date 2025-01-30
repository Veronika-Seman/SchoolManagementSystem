from business_logic.workerLogic import WorkerLogic
from data_access.maintenanceWorker_dao import MaintenanceWorkerDAO

class MaintenanceWorkerLogic(WorkerLogic):
    """
       The MaintenanceWorkerLogic class extends WorkerLogic to handle the business logic related to maintenance workers.
       It interacts with the MaintenanceWorkerDAO to retrieve assigned tasks and report maintenance issues.
       Methods:
           __init__(self, creator_role, maintenance_worker_id=None, name=None, email=None, password=None, salary=None):
               Initializes the MaintenanceWorkerLogic object and its attributes.
           maintenance_worker_id(self):Gets or sets the maintenance worker ID. Ensures the ID is not empty when setting.
           get_assigned_tasks(self):Retrieves the tasks assigned to the maintenance worker.
           report_maintenance_issue(self, description):Reports a new maintenance issue with the provided description.
       """
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



    def report_maintenance_issue(self, description):

        try:
            self.maintenance_worker_dao.report_maintenance_issue(description)
            print(f"Maintenance issue reported: {description}")
        except Exception as e:
            print(f"Error reporting maintenance issue: {e}")





