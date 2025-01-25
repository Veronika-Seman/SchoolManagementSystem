from data_access.data_operations import BaseDAO

class MaintenanceTaskDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def get_task_by_id(self, task_id):
        query = """
        SELECT task_id, description, status, maintenance_worker_id
        FROM MaintenanceTasks
        WHERE task_id = %s
        """
        try:
            self.cursor.execute(query, (task_id,))
            result = self.cursor.fetchone()
            if result:
                return result
            else:
                print(f"No task found with ID {task_id}.")
                return None
        except Exception as e:
            print(f"Error fetching task by ID {task_id}: {e}")
            return None

    def get_unresolved_tasks(self):
        query = """
        SELECT task_id, description, status, maintenance_worker_id
        FROM MaintenanceTasks
        WHERE status != 'Completed'
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching unresolved tasks: {e}")
            return []

    def notify_manager_about_unresolved_tasks(self):
        unresolved_tasks = self.get_unresolved_tasks()
        if unresolved_tasks:
            print(f"Notification: There are {len(unresolved_tasks)} unresolved maintenance tasks.")
        else:
            print("All maintenance tasks are resolved.")

    def close(self):
        super().close()
