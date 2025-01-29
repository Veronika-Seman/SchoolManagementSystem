from data_access.course_dao import CourseDAO

class CourseLogic:
    def __init__(self, course_id=None, course_name=None, teacher_id=None, max_students=None, cost=None):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher_id = teacher_id
        self.max_students = max_students
        self.cost = cost
        self._course_dao = CourseDAO()

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
        if value is not None and not (isinstance(value, int) or isinstance(value, float)):
            raise ValueError("cost must be a numeric type (int/float) or None.")
        if isinstance(value, (int, float)) and value < 0:
            raise ValueError("cost must be non-negative.")
        self._cost = value

    def update_course(self, course_name=None, teacher_id=None, max_students=None, cost=None):

        if self.course_id is None:
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
            self._course_dao.update_course(
                course_id=self.course_id,
                course_name=self.course_name,
                teacher_id=self.teacher_id,
                max_students=self.max_students,
                cost=self.cost
            )
        except Exception as e:
            print(f"[Error] Could not update the course (ID={self.course_id}): {e}")

    def delete_course(self):
        if self.course_id is None:
            print("Cannot delete a course without course_id.")
            return
        try:
            self._course_dao.delete_course(self.course_id)
        except Exception as e:
            print(f"[Error] Could not delete the course (ID={self.course_id}): {e}")

    @staticmethod
    def get_course_by_id(course_id):

        dao = CourseDAO()
        try:
            row = dao.get_course_by_id(course_id)
        except Exception as e:
            print(f"[Error] Could not fetch the course (ID={course_id}): {e}")
            row = None
        finally:
            dao.close()

        if row:
            return CourseLogic(*row)
        return None

    @staticmethod
    def get_all_courses():

        dao = CourseDAO()
        courses = []
        try:
            rows = dao.get_all_courses()
            for row in rows:
                courses.append(CourseLogic(*row))
        except Exception as e:
            print(f"[Error] Could not fetch the list of courses: {e}")
        finally:
            dao.close()
        return courses

    def close(self):
        self._course_dao.close()

