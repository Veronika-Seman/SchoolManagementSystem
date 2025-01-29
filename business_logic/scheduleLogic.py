from data_access.schedule_dao import SchedulesDAO


class ScheduleLogic:
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
