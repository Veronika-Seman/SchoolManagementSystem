from data_access.studentCourses_dao import StudentCoursesDAO

class StudentCoursesLogic:
    def __init__(self):
        self.student_courses_dao = StudentCoursesDAO()

    def remove_student_from_course(self, student_id, course_id):
        try:
            self.student_courses_dao.remove_student_from_course(student_id, course_id)
        except Exception as e:
            print(f"Error removing student {student_id} from course {course_id}: {e}")

    def get_courses_by_student(self, student_id):
        try:
            return self.student_courses_dao.get_courses_by_student(student_id)
        except Exception as e:
            print(f"Error fetching courses for student {student_id}: {e}")
            return []

    def get_students_by_course(self, course_id):
        try:
            return self.student_courses_dao.get_students_by_course(course_id)
        except Exception as e:
            print(f"Error fetching students for course {course_id}: {e}")
            return []

    def get_all_student_courses(self):
        try:
            return self.student_courses_dao.get_all_student_courses()
        except Exception as e:
            print(f"Error fetching all student-course relationships: {e}")
            return []

    def close(self):
        self.student_courses_dao.close()
