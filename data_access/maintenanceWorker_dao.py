from data_access.data_operations import BaseDAO
from data_access.user_dao import UserDAO
from data_access.worker_dao import WorkerDAO
from data_access.maintenanceTasks_dao import MaintenanceTaskDAO
class MaintenanceWorkerDAO(MaintenanceTaskDAO, BaseDAO):
    def __init__(self):
        super().__init__()


    def create_maintenance_worker(self, maintenance_worker_id, name, email, password, salary):
        try:
            user_dao = UserDAO()
            user_dao.create_user(id_number=maintenance_worker_id, name=name, email=email, password=password,
                                 role="MaintenanceWorkers")

            worker_dao = WorkerDAO()
            worker_dao.create_worker(worker_id=maintenance_worker_id, salary=salary)

            query = """
            INSERT INTO MaintenanceWorkers (maintenance_worker_id)
            VALUES (%s)
            """
            self.cursor.execute(query, (maintenance_worker_id,))
            self.connection.commit()
            print(f"Maintenance worker with ID {maintenance_worker_id} created successfully.")
        except Exception as e:
            print(f"Error creating maintenance worker: {e}")


    def report_maintenance_issue(self, description):
        query = """
        INSERT INTO MaintenanceTasks (description, status)
        VALUES (%s, 'Pending')
        """
        try:
            self.cursor.execute(query, (description,))
            self.connection.commit()
            print(f"New maintenance issue reported: {description}")
        except Exception as e:
            print(f"Error reporting maintenance issue: {e}")

    def get_assigned_tasks(self, maintenance_worker_id):
        query = """
        SELECT task_id, description, status
        FROM MaintenanceTasks
        WHERE maintenance_worker_id = %s
        """
        try:
            self.cursor.execute(query, (maintenance_worker_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching tasks for maintenance worker {maintenance_worker_id}: {e}")
            return []

    def close(self):
        super().close()
