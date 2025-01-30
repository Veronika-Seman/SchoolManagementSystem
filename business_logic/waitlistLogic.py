from data_access.waitlist_dao import WaitlistDAO

class WaitlistLogic:
    """
      A class responsible for managing student waitlists for courses in the system. It handles the addition, removal,
      position checking, and assignment of students to courses from the waitlist. Additionally, it checks if the waitlist
      exceeds a given threshold and notifies the admin.
      Methods:
       __init__(self):
          Initializes the WaitlistLogic object with a reference to the WaitlistDAO.

       add_student_to_waitlist(self, student_id, course_id):Adds a student to the waitlist for a specific course and checks if the waitlist exceeds the threshold.
       get_student_position(self, student_id, course_id):Retrieves the position of a student on the waitlist for a specific course.
       remove_student_from_waitlist(self, student_id, course_id):Removes a student from the waitlist for a specific course.
       get_waitlist(self, course_id):Retrieves the full waitlist for a specific course.
       assign_student_to_class(self, course_id, class_id):Assigns a student from the waitlist to a class for a specific course.
       check_waitlist_threshold(self, course_id, threshold=5):Checks if the waitlist for a course exceeds the threshold and notifies the admin if necessary.
       close(self):Closes the connection to the WaitlistDAO.
      """
    def __init__(self):
        self.waitlist_dao = WaitlistDAO()

    def add_student_to_waitlist(self, student_id, course_id):
        try:
            self.waitlist_dao.add_to_waitlist(student_id, course_id)

            self.waitlist_dao.notify_admin_if_waitlist_exceeds(course_id, threshold=5)

            position = self.waitlist_dao.get_student_position(student_id, course_id)
            return position

        except Exception as e:
            print(f"Error Unable to add student {student_id} to the waitlist for course {course_id}: {e}")
            return None

    def get_student_position(self, student_id, course_id):
        try:
            return self.waitlist_dao.get_student_position(student_id, course_id)
        except Exception as e:
            print(f"Error fetching position of student {student_id} in course {course_id}: {e}")
            return None

    def remove_student_from_waitlist(self, student_id, course_id):
        try:
            self.waitlist_dao.remove_from_waitlist(student_id, course_id)
        except Exception as e:
            print(f"Error removing student {student_id} from the waitlist for course {course_id}: {e}")

    def get_waitlist(self, course_id):
        try:
            return self.waitlist_dao.get_waitlist(course_id)
        except Exception as e:
            print(f"Error fetching waitlist for course {course_id}: {e}")
            return []

    def assign_student_to_class(self, course_id, class_id):
        try:
            self.waitlist_dao.assign_student_to_class(course_id, class_id)
        except Exception as e:
            print(f"Error Unable to assign a student from the waitlist to class {class_id} for course {course_id}: {e}")

    def check_waitlist_threshold(self, course_id, threshold=5):
        try:
            self.waitlist_dao.notify_admin_if_waitlist_exceeds(course_id, threshold=threshold)
        except Exception as e:
            print(f"Error Checking the number of students in the waitlist for course {course_id}: {e}")

    def close(self):
        try:
            self.waitlist_dao.close()
        except Exception as e:
            print(f"Error closing the connection to WaitlistDAO: {e}")
