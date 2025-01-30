from data_access.course_dao import CourseDAO
from data_access.studentCourses_dao import StudentCoursesDAO
from data_access.user_dao import UserDAO  # ✅ נוסיף גישה לטבלת Users
from business_logic.waitlistLogic import WaitlistLogic

class EnrollmentLogic:
    """
       EnrollmentLogic handles student enrollment in courses, including direct enrollment
       and waitlist management when a course reaches its capacity.
       Methods:
       - enroll_student_in_course(student_id, course_id): Enrolls a student in a course.
         If the course is full, the student is added to the waitlist.
       """
    def __init__(self):
        self.course_dao = CourseDAO()
        self.student_courses_dao = StudentCoursesDAO()
        self.user_dao = UserDAO()
        self.waitlist_logic = WaitlistLogic()

    def enroll_student_in_course(self, student_id, course_id):
        if not student_id or not course_id:
            raise ValueError("Student ID and Course ID must be provided.")

        student_exists = self.user_dao.get_user_by_id(student_id)
        if not student_exists:
            print(f"Student {student_id} does not exist in the system.")
            return {"status": "ERROR", "message": f"Student {student_id} does not exist."}

        course_data = self.course_dao.get_course_by_id(course_id)
        if not course_data:
            print(f"Course {course_id} not found.")
            return {"status": "ERROR", "message": f"Course {course_id} not found."}

        max_students = course_data["max_students"]

        enrolled_list = self.student_courses_dao.get_students_by_course(course_id)
        current_count = len(enrolled_list)

        if current_count >= max_students:
            position = self.waitlist_logic.add_student_to_waitlist(student_id, course_id)
            print(f"Course {course_id} is full. Student {student_id} added to the waitlist at position {position}.")
            return {"status": "WAITLIST", "message": f"Position: {position}"}

        self.student_courses_dao.enroll_student_in_course(student_id, course_id)
        print(f"Student {student_id} enrolled in course {course_id} successfully.")
        return {"status": "ENROLLED", "message": "OK"}

