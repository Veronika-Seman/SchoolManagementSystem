from data_access.course_dao import CourseDAO

class CourseLogic:
    """
       CourseLogic handles the business logic for managing courses in the system.
       It interacts with CourseDAO to perform data operations related to courses.
       Methods:
       - update_course(): Updates an existing course with new details.
       - delete_course(): Deletes a course by ID.
       - get_course_by_id(): Retrieves course details by course ID.
       - get_all_courses(): Retrieves all available courses in the system.
         get_course_name():
                This function retrieves the name of a course from the database based on the given `course_id`.

       - close(): Closes the database connection.
       """
    def __init__(self, course_id=None, course_name=None, teacher_id=None, max_students=None, cost=None):
        self.course_dao = CourseDAO()
        self._course_id = course_id
        self._course_name = course_name
        self._teacher_id = teacher_id
        self._max_students = max_students
        self._cost = cost

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("course_id must be an integer or None.")
        self._course_id = value

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("course_name must be a string or None.")
        self._course_name = value

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self._teacher_id = value

    @property
    def max_students(self):
        return self._max_students

    @max_students.setter
    def max_students(self, value):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError("max_students must be a non-negative integer or None.")
        self._max_students = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise ValueError("cost must be a numeric type (int/float) or None.")
        if isinstance(value, (int, float)) and value < 0:
            raise ValueError("cost must be non-negative.")
        self._cost = value

    def update_course(self, course_name=None, teacher_id=None, max_students=None, cost=None):
        if self._course_id is None:
            print("Cannot update a course without course_id.")
            return

        if course_name is not None:
            self.course_name = course_name
        if teacher_id is not None:
            self.teacher_id = teacher_id
        if max_students is not None:
            self.max_students = max_students
        if cost is not None:
            self.cost = cost

        try:
            self.course_dao.update_course(
                course_id=self._course_id,
                course_name=self._course_name,
                teacher_id=self._teacher_id,
                max_students=self._max_students,
                cost=self._cost
            )
            print(f"Course {self._course_id} updated successfully.")
        except Exception as e:
            print(f"Error Could not update the course (ID={self._course_id}): {e}")

    def delete_course(self):
        if self._course_id is None:
            print("Cannot delete a course without course_id.")
            return
        try:
            self.course_dao.delete_course(self._course_id)
            print(f"Course {self._course_id} deleted successfully.")
        except Exception as e:
            print(f"Error Could not delete the course (ID={self._course_id}): {e}")

    @staticmethod
    def get_course_by_id(course_id):
        dao = CourseDAO()
        try:
            row = dao.get_course_by_id(course_id)
            if row:
                return CourseLogic(
                    course_id=row.get("course_id"),
                    course_name=row.get("course_name"),
                    teacher_id=row.get("teacher_id"),
                    max_students=row.get("max_students"),
                    cost=row.get("cost")
                )
        except Exception as e:
            print(f"Error Could not fetch the course (ID={course_id}): {e}")
        finally:
            dao.close()
        return None

    @staticmethod
    def get_all_courses():
        dao = CourseDAO()
        courses = []
        try:
            rows = dao.get_all_courses()
            for row in rows:
                courses.append(CourseLogic(
                    course_id=row.get("course_id"),
                    course_name=row.get("course_name"),
                    teacher_id=row.get("teacher_id"),
                    max_students=row.get("max_students"),
                    cost=row.get("cost")
                ))
        except Exception as e:
            print(f"Error Could not fetch the list of courses: {e}")
        finally:
            dao.close()
        return courses

    def get_course_name(self, course_id):
        try:
            course_name = self.course_dao.get_course_name(course_id)
            if not course_name:
                print(f"Course with ID {course_id} not found.")
                return None
            return course_name
        except Exception as e:
            print(f"Error fetching course name for course ID {course_id}: {e}")
            return None

    def close(self):
        self.course_dao.close()
