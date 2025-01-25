from data_access.data_operations import BaseDAO
class SchedulesDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def add_schedule(self, course_id, class_id, student_id, day, hour):
        query = """
        INSERT INTO Schedules (course_id, class_id, student_id, day, hour)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, (course_id, class_id, student_id, day, hour))
            self.connection.commit()
            print(f"Schedule added successfully for course {course_id}, class {class_id}, student {student_id}.")
        except Exception as e:
            print(f"Error adding schedule: {e}")

    def update_schedule(self, schedule_id, day=None, hour=None):
        query = "UPDATE Schedules SET "
        params = []
        if day:
            query += "day = %s, "
            params.append(day)
        if hour:
            query += "hour = %s, "
            params.append(hour)
        query = query.rstrip(", ") + " WHERE schedule_id = %s"
        params.append(schedule_id)
        try:
            self.cursor.execute(query, tuple(params))
            self.connection.commit()
            print(f"Schedule {schedule_id} updated successfully.")
        except Exception as e:
            print(f"Error updating schedule: {e}")

    def delete_schedule(self, schedule_id):
        query = "DELETE FROM Schedules WHERE schedule_id = %s"
        try:
            self.cursor.execute(query, (schedule_id,))
            self.connection.commit()
            print(f"Schedule {schedule_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting schedule: {e}")

    def close(self):
        super().close()
