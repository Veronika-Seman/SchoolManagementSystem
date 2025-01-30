from data_access.data_operations import BaseDAO


class WorkerDAO(BaseDAO):
    """
        WorkerDAO class for interacting with the 'Workers' table.
        Provides methods to create, read, and update worker records in the database.
        Inherits from BaseDAO for common database functionality.
        Methods:
            create_worker(worker_id, salary): Creates a new worker record.
            get_worker_by_id(worker_id): Retrieves a worker's details by their ID.
            update_worker(worker_id, salary=None): Updates a worker's details in the 'Workers' table.
            close(): Closes the database connection and cursor.
        """
    def __init__(self):
        super().__init__()

    def create_worker(self, worker_id, salary):
        query = """
        INSERT INTO Workers (worker_id, salary)
        VALUES (%s, %s)
        """
        try:
            self.cursor.execute(query, (worker_id, salary))
            self.connection.commit()
            print(f"Worker with ID {worker_id} created successfully.")
        except Exception as e:
            print(f"Error creating worker: {e}")


    def get_worker_by_id(self, worker_id):
        query = """
        SELECT * FROM Workers
        WHERE worker_id = %s
        """
        try:
            self.cursor.execute(query, (worker_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching worker with ID {worker_id}: {e}")
            return None

    def update_worker(self, worker_id, salary=None):
        query = "UPDATE Workers SET "
        params = []
        if salary is not None:
            query += "salary = %s "
            params.append(salary)
        query += "WHERE worker_id = %s"
        params.append(worker_id)
        try:
            self.cursor.execute(query, tuple(params))
            self.connection.commit()
            print(f"Worker {worker_id} updated successfully.")
        except Exception as e:
            print(f"Error updating worker: {e}")

    def close(self):
        super().close()
