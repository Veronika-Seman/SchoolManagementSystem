from data_access.course_dao import CourseDAO
from data_access.studentCourses_dao import StudentCoursesDAO
from business_logic.waitlistLogic import WaitlistLogic  # Or whatever exists in your system

class EnrollmentLogic:
    def __init__(self):
        self.course_dao = CourseDAO()
        self.student_courses_dao = StudentCoursesDAO()
        self.waitlist_logic = WaitlistLogic()

    def enroll_student_in_course(self, student_id, course_id):
        if not student_id or not course_id:
            raise ValueError("Student ID and Course ID must be provided.")

        course_data = self.course_dao.get_course_by_id(course_id)
        if not course_data:
            raise ValueError(f"Course {course_id} not found.")

        max_students = course_data[3]

        enrolled_list = self.student_courses_dao.get_students_by_course(course_id)
        current_count = len(enrolled_list)

        if current_count >= max_students:
            position = self.waitlist_logic.add_student_to_waitlist(student_id, course_id)
            print(f"Course {course_id} is full. Student {student_id} added to the waitlist at position {position}.")
            return {"status": "WAITLIST", "message": f"Position: {position}"}
        else:
            self.student_courses_dao.enroll_student_in_course(student_id, course_id)
            print(f"Student {student_id} enrolled in course {course_id} successfully.")
            return {"status": "ENROLLED", "message": "OK"}
