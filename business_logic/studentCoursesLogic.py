from data_access.studentCourses_dao import StudentCoursesDAO

class StudentCoursesLogic:
    """
        The StudentCoursesLogic class manages the business logic related to the relationship between
        students and courses. It interacts with the StudentCoursesDAO to add, remove, and retrieve
        student-course relationships from the data source.
        Methods:
            __init__(self):
                Initializes the StudentCoursesLogic object and its associated StudentCoursesDAO.
            remove_student_from_course(self, student_id, course_id):Removes a student from a specific course.
            get_courses_by_student(self, student_id):Retrieves all courses associated with a specific student.
            get_students_by_course(self, course_id):Retrieves all students enrolled in a specific course.
            get_all_student_courses(self):Retrieves all student-course relationships.
            close(self):Closes the connection to the StudentCoursesDAO.
        """
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
