from data_access.maintenanceTasks_dao import MaintenanceTaskDAO

"""
    The MaintenanceTaskLogic class handles the business logic related to maintenance tasks.
    It interacts with the MaintenanceTaskDAO to fetch, update, and manage tasks.
    Methods:
        __init__(self): Initializes the MaintenanceTaskLogic object and the associated MaintenanceTaskDAO.
        get_task_by_id(self, task_id): Retrieves a maintenance task by its ID.
        get_unresolved_tasks(self): Retrieves all unresolved maintenance tasks.
        notify_manager_about_unresolved_tasks(self): Notifies the manager about unresolved tasks.
        update_task_status(self, task_id, status): Updates the status of a task.
        close(self): Closes the connection to the DAO.
    """
class MaintenanceTaskLogic:
    def __init__(self):
        self.task_dao = MaintenanceTaskDAO()

    def get_task_by_id(self, task_id):
        try:
            task = self.task_dao.get_task_by_id(task_id)
            if task:
                print(f"Task found: {task}")
                return task
            else:
                print(f"No task found with ID {task_id}.")
        except Exception as e:
            print(f"Error in logic layer fetching task by ID {task_id}: {e}")

    def get_unresolved_tasks(self):
        try:
            tasks = self.task_dao.get_unresolved_tasks()
            if tasks:
                print(f"Found {len(tasks)} unresolved tasks.")
                return tasks
            else:
                print("All tasks are resolved.")
        except Exception as e:
            print(f"Error in logic layer fetching unresolved tasks: {e}")

    def notify_manager_about_unresolved_tasks(self):
        try:
            self.task_dao.notify_manager_about_unresolved_tasks()
        except Exception as e:
            print(f"Error notifying manager about unresolved tasks: {e}")

    def update_task_status(self, task_id, status):
        try:
            self.task_dao.update_task_status(task_id, status)
            print(f"Task {task_id} status updated to '{status}' successfully.")
        except Exception as e:
            print(f"Error updating task status: {e}")
    def close(self):
        self.task_dao.close()

