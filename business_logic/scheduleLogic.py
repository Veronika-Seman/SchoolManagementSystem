from data_access.schedule_dao import SchedulesDAO


class ScheduleLogic:
    """
        The ScheduleLogic class manages the logic for handling student schedules.
        It interacts with the SchedulesDAO to add, update, and delete schedule entries
        for students, as well as closing the connection to the schedule data source.
        Methods:
            __init__(self):
                Initializes the ScheduleLogic object and its associated SchedulesDAO.
            add_schedule(self, course_id, class_id, student_id, day, hour):Adds a new schedule entry for a student in the system.
            update_schedule(self, schedule_id, day=None, hour=None):Updates the schedule of an existing entry based on schedule ID.
            delete_schedule(self, schedule_id):Deletes a specific schedule entry by its ID.
            close(self):Closes the connection to the SchedulesDAO.
        """
    def __init__(self):
        self.schedule_dao = SchedulesDAO()

    def add_schedule(self, course_id, class_id, student_id, day, hour):
        try:
            self.schedule_dao.add_schedule(course_id, class_id, student_id, day, hour)
        except Exception as e:
            print(f"[Error] Unable to add schedule: {e}")

    def update_schedule(self, schedule_id, day=None, hour=None):
        try:
            self.schedule_dao.update_schedule(schedule_id, day=day, hour=hour)
        except Exception as e:
            print(f"[Error] Unable to update schedule ID={schedule_id}: {e}")

    def delete_schedule(self, schedule_id):
        try:
            self.schedule_dao.delete_schedule(schedule_id)
        except Exception as e:
            print(f"[Error] Unable to delete schedule ID={schedule_id}: {e}")

    def close(self):
        self.schedule_dao.close()
