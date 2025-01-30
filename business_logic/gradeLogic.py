class GradeLogic:
    """
       The GradeLogic class handles the business logic related to student grades.
       It interacts with a Data Access Object (DAO) to fetch, update, and delete grades.
       Methods:
           __init__(self, grades_dao): Initializes the GradeLogic object with a grades_dao to interact with the data layer for grade-related operations.
           get_grades_for_course(self, course_id): Fetches grades for a specific course. If no grades are found, a message is printed.
           update_student_grade(self, student_id, course_id, grade): Updates the grade for a specific student in a specific course. Validates the grade before updating.
           delete_student_grade(self, student_id, course_id): Deletes the grade for a specific student in a specific course.
       """
    def __init__(self, grades_dao):
        self.grades_dao = grades_dao

    def get_grades_for_course(self, course_id):
        if not course_id:
            raise ValueError("Course ID cannot be empty.")
        try:
            grades = self.grades_dao.get_grades_by_course(course_id)
            if not grades:
                print(f"No grades found for course ID {course_id}.")
            return grades
        except Exception as e:
            print(f"Error fetching grades for course ID {course_id}: {e}")
            return []

    def update_student_grade(self, student_id, course_id, grade):
        if not student_id or not course_id:
            raise ValueError("Student ID and Course ID cannot be empty.")
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError("Grade must be a number between 0 and 100.")
        try:
            self.grades_dao.update_grade(student_id, course_id, grade)
            print(f"Successfully updated grade for student {student_id} in course {course_id}.")
        except Exception as e:
            print(f"Error updating grade: {e}")

    def delete_student_grade(self, student_id, course_id):
        if not student_id or not course_id:
            raise ValueError("Student ID and Course ID cannot be empty.")
        try:
            self.grades_dao.delete_grade(student_id, course_id)
            print(f"Successfully deleted grade for student {student_id} in course {course_id}.")
        except Exception as e:
            print(f"Error deleting grade: {e}")

